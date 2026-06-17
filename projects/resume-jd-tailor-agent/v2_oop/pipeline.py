"""
Pipeline Orchestrator — Composes agents into a complete workflow.

OOP Concepts Demonstrated:
- Composition: Pipeline is COMPOSED of agent objects (has-a, not is-a)
- Iterator Protocol: __iter__ to iterate over results
- Context Manager: Uses LLMClient as context manager
- Encapsulation: Pipeline logic hidden behind simple run() interface
- Observer Pattern (simplified): Callbacks for progress updates
- Strategy Pattern: Agents are interchangeable strategies for each step
- State Management: PipelineState tracks execution progress
"""

import logging
import time
from typing import Any, Callable, Generator

from config import PipelineConfig
from llm_client import LLMClient
from models import (
    AgentResult,
    CriticResult,
    JDAnalysis,
    MatchAnalysis,
    PipelineState,
    PipelineStep,
    RewrittenBullet,
)
from exceptions import (
    MaxRevisionsExceededError,
    PipelineError,
    StepFailedError,
)
from agents.jd_extractor import JDExtractorAgent
from agents.resume_matcher import ResumeMatcherAgent
from agents.resume_rewriter import ResumeRewriterAgent
from agents.cover_letter import CoverLetterAgent
from agents.critic import CriticAgent
from agents.interview import InterviewAgent

logger = logging.getLogger(__name__)

# Type alias for progress callback
ProgressCallback = Callable[[int, str, Any], None]


class Pipeline:
    """
    Orchestrates the full resume tailoring pipeline.

    OOP Concepts:
    - COMPOSITION: Contains agent instances (doesn't inherit from them)
    - FACADE PATTERN: Simple run() interface hides complex multi-step logic
    - ITERATOR: Can iterate over results with for...in
    - CONTEXT MANAGER: Manages LLMClient lifecycle

    The Pipeline doesn't DO the work — it COORDINATES agents that do.
    This is the Composition over Inheritance principle in action.

    Usage:
        config = PipelineConfig.from_env()
        pipeline = Pipeline(config)

        # Simple usage:
        results = pipeline.run(resume_text="...", jd_text="...")

        # With progress callback:
        def on_progress(step, label, data):
            print(f"Step {step}: {label}")

        results = pipeline.run(
            resume_text="...",
            jd_text="...",
            on_progress=on_progress,
        )

        # Streaming (for SSE):
        for event in pipeline.run_streaming(resume_text="...", jd_text="..."):
            send_sse(event)
    """

    def __init__(self, config: PipelineConfig | None = None):
        """
        Initialize the pipeline with configuration.

        OOP Concept: The constructor sets up the COMPOSITION.
        We create all agent instances here, injecting the shared
        LLM client into each one (Dependency Injection).
        """
        self._config = config or PipelineConfig.from_env()
        self._llm_client = LLMClient(
            llm_config=self._config.llm,
            rate_config=self._config.rate_limit,
        )
        self._state = PipelineState()

        # Create agent instances (Composition)
        self._jd_extractor = JDExtractorAgent(self._llm_client)
        self._resume_matcher = ResumeMatcherAgent(self._llm_client)
        self._resume_rewriter = ResumeRewriterAgent(self._llm_client)
        self._cover_letter_writer = CoverLetterAgent(self._llm_client)
        self._critic = CriticAgent(self._llm_client, threshold=self._config.critic_threshold)
        self._interview_gen = InterviewAgent(self._llm_client)

        logger.info(f"Pipeline initialized: {self._config}")

    # ── Public Interface ─────────────────────────────────────────────────────

    def run(
        self,
        resume_text: str,
        jd_text: str,
        target_role: str = "",
        on_progress: ProgressCallback | None = None,
    ) -> dict[str, Any]:
        """
        Run the complete pipeline synchronously.

        OOP Concept: FACADE PATTERN — one simple method hides
        the complexity of 7 steps, revision loops, and error handling.

        Args:
            resume_text: The candidate's resume.
            jd_text: The job description.
            target_role: Optional target role title.
            on_progress: Optional callback for progress updates.

        Returns:
            Dict with all pipeline results.

        Raises:
            PipelineError: If a critical step fails.
        """
        self._state = PipelineState()  # Reset state

        # Use LLMClient as context manager
        with self._llm_client:
            return self._execute_pipeline(resume_text, jd_text, target_role, on_progress)

    def run_streaming(
        self,
        resume_text: str,
        jd_text: str,
        target_role: str = "",
    ) -> Generator[dict, None, None]:
        """
        Run the pipeline and yield SSE-compatible events.

        OOP Concept: GENERATOR — uses yield to produce events
        one at a time, enabling streaming without buffering all results.

        Yields:
            Dict events with type: "step" | "result" | "error" | "done"
        """
        self._state = PipelineState()

        with self._llm_client:
            try:
                # Step 1: JD Extraction
                yield {"type": "step", "step": 0, "label": "Analyzing Job Description..."}
                jd_result = self._jd_extractor.execute(jd_text=jd_text, target_role=target_role)
                self._state.add_result(jd_result)

                if jd_result.failed:
                    yield {"type": "error", "message": jd_result.error}
                    return

                jd_analysis: JDAnalysis = jd_result.data
                keywords = jd_analysis.top_keywords
                responsibilities = jd_analysis.responsibilities
                yield {"type": "result", "step": 0, "key": "jd_analysis", "data": jd_analysis.model_dump()}

                # Step 2: Resume Matching
                yield {"type": "step", "step": 1, "label": "Matching Resume to JD..."}
                match_result = self._resume_matcher.execute(resume_text=resume_text, jd_text=jd_text)
                self._state.add_result(match_result)

                if match_result.failed:
                    yield {"type": "error", "message": match_result.error}
                    return

                match_analysis: MatchAnalysis = match_result.data
                missing_skills = match_analysis.missing_skills
                yield {"type": "result", "step": 1, "key": "match_analysis", "data": match_analysis.model_dump()}

                # Step 3: Bullet Rewriting
                yield {"type": "step", "step": 2, "label": "Rewriting Resume Bullets..."}
                bullets_result = self._resume_rewriter.execute(resume_text=resume_text, keywords=keywords)
                self._state.add_result(bullets_result)

                if bullets_result.failed:
                    yield {"type": "error", "message": bullets_result.error}
                    return

                bullets: list[RewrittenBullet] = bullets_result.data
                yield {"type": "result", "step": 2, "key": "bullets", "data": [b.model_dump() for b in bullets]}

                # Step 4: Cover Letter
                yield {"type": "step", "step": 3, "label": "Drafting Cover Letter..."}
                cover_result = self._cover_letter_writer.execute(
                    resume_text=resume_text,
                    keywords=keywords,
                    responsibilities=responsibilities,
                    target_role=target_role,
                )
                self._state.add_result(cover_result)

                if cover_result.failed:
                    yield {"type": "error", "message": cover_result.error}
                    return

                cover_letter: str = cover_result.data
                yield {"type": "result", "step": 3, "key": "cover_letter", "data": cover_letter}

                # Step 5: Critic Review
                yield {"type": "step", "step": 4, "label": "Running Critic Review..."}
                critic_result_agent = self._critic.execute(
                    bullets=bullets,
                    cover_letter=cover_letter,
                    keywords=keywords,
                )
                self._state.add_result(critic_result_agent)

                if critic_result_agent.failed:
                    yield {"type": "error", "message": critic_result_agent.error}
                    return

                critic_result: CriticResult = critic_result_agent.data
                yield {"type": "result", "step": 4, "key": "critic", "data": critic_result.model_dump()}

                # Step 6: Revision Loop
                revision_count = 0
                while self._critic.needs_revision(critic_result) and revision_count < self._config.max_revision_loops:
                    revision_count += 1
                    self._state.revision_count = revision_count

                    yield {
                        "type": "step", "step": 5,
                        "label": f"Revising (attempt {revision_count}/{self._config.max_revision_loops})...",
                    }

                    issues = critic_result.issues
                    suggestions = critic_result.suggestions

                    # Revise bullets and cover letter
                    bullets = self._resume_rewriter.revise(
                        bullets=bullets,
                        keywords=keywords,
                        issues=issues,
                        suggestions=suggestions,
                        resume_text=resume_text,
                    )
                    cover_letter = self._cover_letter_writer.revise(
                        cover_letter=cover_letter,
                        keywords=keywords,
                        issues=issues,
                        suggestions=suggestions,
                        resume_text=resume_text,
                    )

                    # Re-evaluate
                    critic_result_agent = self._critic.execute(
                        bullets=bullets,
                        cover_letter=cover_letter,
                        keywords=keywords,
                    )
                    if critic_result_agent.success:
                        critic_result = critic_result_agent.data

                yield {"type": "result", "step": 5, "key": "revision", "data": {
                    "bullets": [b.model_dump() if isinstance(b, RewrittenBullet) else b for b in bullets],
                    "cover_letter": cover_letter,
                    "critic": critic_result.model_dump(),
                    "revision_count": revision_count,
                }}

                # Step 7: Interview Questions
                yield {"type": "step", "step": 6, "label": "Generating Interview Questions..."}
                interview_result = self._interview_gen.execute(
                    resume_text=resume_text,
                    jd_text=jd_text,
                    keywords=keywords,
                    missing_skills=missing_skills,
                )
                self._state.add_result(interview_result)

                if interview_result.failed:
                    yield {"type": "error", "message": interview_result.error}
                    return

                yield {
                    "type": "result", "step": 6, "key": "interview_questions",
                    "data": [q.model_dump() for q in interview_result.data],
                }

                self._state.is_complete = True
                yield {"type": "done"}

            except StepFailedError as e:
                yield {"type": "error", "message": str(e)}
            except Exception as e:
                yield {"type": "error", "message": f"Pipeline error: {e}"}

    # ── Private Methods ──────────────────────────────────────────────────────

    def _execute_pipeline(
        self,
        resume_text: str,
        jd_text: str,
        target_role: str,
        on_progress: ProgressCallback | None,
    ) -> dict[str, Any]:
        """
        Internal pipeline execution logic.

        OOP Concept: Private method — implementation detail.
        External code uses run() or run_streaming(), not this.
        """
        results = {}

        def notify(step: int, label: str, data: Any = None):
            if on_progress:
                on_progress(step, label, data)

        # Step 1: JD Extraction
        notify(0, "Analyzing Job Description...")
        jd_result = self._jd_extractor.execute(jd_text=jd_text, target_role=target_role)
        self._state.add_result(jd_result)
        if jd_result.failed:
            raise PipelineError(f"JD extraction failed: {jd_result.error}", step=0)
        jd_analysis: JDAnalysis = jd_result.data
        results["jd_analysis"] = jd_analysis
        notify(0, "JD Analysis complete", jd_analysis)

        # Step 2: Resume Matching
        notify(1, "Matching Resume to JD...")
        match_result = self._resume_matcher.execute(resume_text=resume_text, jd_text=jd_text)
        self._state.add_result(match_result)
        if match_result.failed:
            raise PipelineError(f"Resume matching failed: {match_result.error}", step=1)
        match_analysis: MatchAnalysis = match_result.data
        results["match_analysis"] = match_analysis
        notify(1, "Matching complete", match_analysis)

        keywords = jd_analysis.top_keywords
        responsibilities = jd_analysis.responsibilities
        missing_skills = match_analysis.missing_skills

        # Step 3: Bullet Rewriting
        notify(2, "Rewriting Resume Bullets...")
        bullets_result = self._resume_rewriter.execute(resume_text=resume_text, keywords=keywords)
        self._state.add_result(bullets_result)
        if bullets_result.failed:
            raise PipelineError(f"Bullet rewriting failed: {bullets_result.error}", step=2)
        bullets: list[RewrittenBullet] = bullets_result.data
        results["bullets"] = bullets
        notify(2, "Bullets rewritten", bullets)

        # Step 4: Cover Letter
        notify(3, "Drafting Cover Letter...")
        cover_result = self._cover_letter_writer.execute(
            resume_text=resume_text,
            keywords=keywords,
            responsibilities=responsibilities,
            target_role=target_role,
        )
        self._state.add_result(cover_result)
        if cover_result.failed:
            raise PipelineError(f"Cover letter failed: {cover_result.error}", step=3)
        cover_letter: str = cover_result.data
        results["cover_letter"] = cover_letter
        notify(3, "Cover letter drafted", cover_letter)

        # Step 5: Critic Review
        notify(4, "Running Critic Review...")
        critic_agent_result = self._critic.execute(
            bullets=bullets, cover_letter=cover_letter, keywords=keywords
        )
        self._state.add_result(critic_agent_result)
        if critic_agent_result.failed:
            raise PipelineError(f"Critic review failed: {critic_agent_result.error}", step=4)
        critic_result: CriticResult = critic_agent_result.data
        results["critic"] = critic_result
        notify(4, "Critic review complete", critic_result)

        # Step 6: Revision Loop
        revision_count = 0
        while self._critic.needs_revision(critic_result) and revision_count < self._config.max_revision_loops:
            revision_count += 1
            notify(5, f"Revising (attempt {revision_count}/{self._config.max_revision_loops})...")

            bullets = self._resume_rewriter.revise(
                bullets=bullets,
                keywords=keywords,
                issues=critic_result.issues,
                suggestions=critic_result.suggestions,
                resume_text=resume_text,
            )
            cover_letter = self._cover_letter_writer.revise(
                cover_letter=cover_letter,
                keywords=keywords,
                issues=critic_result.issues,
                suggestions=critic_result.suggestions,
                resume_text=resume_text,
            )
            critic_agent_result = self._critic.execute(
                bullets=bullets, cover_letter=cover_letter, keywords=keywords
            )
            if critic_agent_result.success:
                critic_result = critic_agent_result.data

        results["revision_count"] = revision_count
        results["final_bullets"] = bullets
        results["final_cover_letter"] = cover_letter
        results["final_critic"] = critic_result
        self._state.revision_count = revision_count

        # Step 7: Interview Questions
        notify(6, "Generating Interview Questions...")
        interview_result = self._interview_gen.execute(
            resume_text=resume_text,
            jd_text=jd_text,
            keywords=keywords,
            missing_skills=missing_skills,
        )
        self._state.add_result(interview_result)
        if interview_result.failed:
            raise PipelineError(f"Interview generation failed: {interview_result.error}", step=6)
        results["interview_questions"] = interview_result.data
        notify(6, "Interview questions generated", interview_result.data)

        self._state.is_complete = True
        return results

    # ── Properties ───────────────────────────────────────────────────────────

    @property
    def state(self) -> PipelineState:
        """Current pipeline execution state."""
        return self._state

    @property
    def config(self) -> PipelineConfig:
        """Pipeline configuration."""
        return self._config

    # ── Magic Methods ────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"Pipeline(agents=6, "
            f"max_revisions={self._config.max_revision_loops}, "
            f"threshold={self._config.critic_threshold})"
        )

    def __str__(self) -> str:
        status = "complete" if self._state.is_complete else "ready"
        return f"Resume JD Tailor Pipeline [{status}]"

    def __iter__(self):
        """Iterate over pipeline results."""
        return iter(self._state)

    def __len__(self) -> int:
        """Number of completed steps."""
        return len(self._state)
