"""
Resume Rewriter Agent — Rewrites bullets for better JD alignment.

OOP Concepts Demonstrated:
- Inheritance: Extends BaseAgent
- Method Overriding: Implements abstract methods + adds revise() method
- Encapsulation: Rewriting logic isolated in this class
- Composition: Uses PromptTemplate objects for different operations
- Open/Closed Principle: Open for extension (revise method), closed for modification
"""

from typing import Any

from agents.base import BaseAgent
from models import PipelineStep, RewrittenBullet
from prompts import (
    REWRITER_SYSTEM,
    REWRITER_USER,
    REVISION_SYSTEM,
    REVISION_BULLETS_USER,
)


class ResumeRewriterAgent(BaseAgent):
    """
    Rewrites resume bullets to better align with JD keywords.

    This agent demonstrates the OPEN/CLOSED PRINCIPLE:
    - The base execute() method handles the standard rewrite flow
    - The revise() method EXTENDS functionality for the revision loop
    - We didn't modify BaseAgent to add revision — we extended this class

    OOP Concept: A class can have methods beyond what the abstract
    base class requires. The base class defines the minimum contract;
    subclasses can add more.
    """

    @property
    def name(self) -> str:
        return "Resume Rewriter"

    @property
    def step(self) -> PipelineStep:
        return PipelineStep.BULLET_REWRITING

    def _validate_input(self, **kwargs) -> None:
        """Validate resume text and keywords are provided."""
        self._require_non_empty(kwargs.get("resume_text", ""), "resume_text")
        self._require_non_empty_list(kwargs.get("keywords", []), "keywords")

    def _process(self, **kwargs) -> dict:
        """Call LLM to rewrite resume bullets."""
        user_prompt = REWRITER_USER(
            resume_text=kwargs["resume_text"],
            keywords=", ".join(kwargs["keywords"]),
        )

        return self._llm_client.call_json(
            system_prompt=str(REWRITER_SYSTEM),
            user_prompt=user_prompt,
        )

    def _format_output(self, raw_result: Any) -> list[RewrittenBullet]:
        """Parse into list of RewrittenBullet models."""
        bullets_data = raw_result.get("bullets", [])
        bullets = []
        for b in bullets_data:
            try:
                bullets.append(RewrittenBullet(**b))
            except Exception:
                # Skip malformed bullets rather than failing entirely
                continue
        return bullets

    # ── Extended Method (beyond base class contract) ─────────────────────────

    def revise(
        self,
        bullets: list[RewrittenBullet],
        keywords: list[str],
        issues: list[str],
        suggestions: list[str],
        resume_text: str,
    ) -> list[RewrittenBullet]:
        """
        Revise bullets based on critic feedback.

        OOP Concept: This method EXTENDS the class beyond the base
        contract. BaseAgent doesn't know about revision — that's
        specific to this agent's role in the pipeline.

        Args:
            bullets: Current bullet list.
            keywords: JD keywords.
            issues: Critic-identified issues.
            suggestions: Critic suggestions.
            resume_text: Original resume for fact-checking.

        Returns:
            Revised list of RewrittenBullet objects.
        """
        # Format current bullets for the prompt
        bullets_text = "\n".join(
            f"- {b.rewritten}" for b in bullets
        )

        user_prompt = REVISION_BULLETS_USER(
            bullets_text=bullets_text,
            keywords=", ".join(keywords),
            issues="\n".join(f"  - {i}" for i in issues),
            suggestions="\n".join(f"  - {s}" for s in suggestions),
            resume_text=resume_text,
        )

        try:
            result = self._llm_client.call_json(
                system_prompt=str(REVISION_SYSTEM),
                user_prompt=user_prompt,
            )
            return self._format_output(result)
        except Exception as e:
            # On revision failure, return original bullets
            import logging
            logging.getLogger(__name__).warning(f"Revision failed: {e}. Keeping original bullets.")
            return bullets
