"""
Critic Agent — Evaluates quality of rewritten content.

OOP Concepts Demonstrated:
- Inheritance: Extends BaseAgent
- Encapsulation: Scoring logic and threshold checking internal
- Properties: passes_threshold computed from result
- Composition: Works with RewrittenBullet models from other agents
"""

from typing import Any

from agents.base import BaseAgent
from models import CriticResult, PipelineStep, RewrittenBullet
from prompts import CRITIC_SYSTEM, CRITIC_USER


class CriticAgent(BaseAgent):
    """
    Reviews rewritten bullets and cover letter, scoring quality.

    This agent acts as a QUALITY GATE in the pipeline.
    If its score is below threshold, the pipeline triggers revision.

    OOP Concept: Single Responsibility — this agent ONLY evaluates.
    It doesn't rewrite or fix anything. That's the rewriter's job.
    """

    def __init__(self, llm_client, threshold: int = 8):
        """
        Initialize with LLM client and quality threshold.

        OOP Concept: Extended constructor — adds threshold parameter
        beyond what BaseAgent requires. Calls super().__init__() to
        ensure base class initialization still happens.
        """
        super().__init__(llm_client)
        self._threshold = threshold

    @property
    def name(self) -> str:
        return "Critic"

    @property
    def step(self) -> PipelineStep:
        return PipelineStep.CRITIC_REVIEW

    @property
    def threshold(self) -> int:
        """The minimum score to pass without revision."""
        return self._threshold

    def _validate_input(self, **kwargs) -> None:
        """Validate bullets and cover letter are provided."""
        bullets = kwargs.get("bullets", [])
        cover_letter = kwargs.get("cover_letter", "")

        if not bullets:
            from exceptions import InputValidationError
            raise InputValidationError("bullets", "no bullets to evaluate")
        if not cover_letter or not cover_letter.strip():
            from exceptions import InputValidationError
            raise InputValidationError("cover_letter", "no cover letter to evaluate")

    def _process(self, **kwargs) -> dict:
        """Call LLM to evaluate content quality."""
        bullets = kwargs["bullets"]
        cover_letter = kwargs["cover_letter"]
        keywords = kwargs.get("keywords", [])

        # Format bullets for the prompt
        # Handle both RewrittenBullet objects and plain dicts
        bullets_text = "\n".join(
            f"- {b.rewritten if isinstance(b, RewrittenBullet) else b.get('rewritten', b.get('original', ''))}"
            for b in bullets
        )

        user_prompt = CRITIC_USER(
            bullets_text=bullets_text,
            cover_letter=cover_letter,
            keywords=", ".join(keywords),
        )

        return self._llm_client.call_json(
            system_prompt=str(CRITIC_SYSTEM),
            user_prompt=user_prompt,
        )

    def _format_output(self, raw_result: Any) -> CriticResult:
        """Parse into validated CriticResult model."""
        try:
            return CriticResult(**raw_result)
        except Exception:
            defaults = {"score": 5, "issues": [], "suggestions": []}
            merged = {**defaults, **raw_result}
            return CriticResult(**merged)

    # ── Extended Methods ─────────────────────────────────────────────────────

    def needs_revision(self, result: CriticResult) -> bool:
        """
        Check if the critic score requires revision.

        OOP Concept: Encapsulation — the threshold logic is inside
        the critic agent. External code asks "needs_revision?" rather
        than checking score < threshold themselves.
        """
        return result.score < self._threshold
