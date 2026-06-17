"""
Cover Letter Agent — Generates and revises cover letters.

OOP Concepts Demonstrated:
- Inheritance: Extends BaseAgent
- Method Override: Different _process returns text (not JSON)
- Polymorphism: Same execute() interface, different internal behavior
- Extended Methods: revise() adds revision capability
"""

from typing import Any

from agents.base import BaseAgent
from models import PipelineStep
from prompts import (
    COVER_LETTER_SYSTEM,
    COVER_LETTER_USER,
    REVISION_SYSTEM,
    REVISION_COVER_LETTER_USER,
)


class CoverLetterAgent(BaseAgent):
    """
    Generates a 3-paragraph cover letter.

    OOP Concept: POLYMORPHISM in action.
    Unlike other agents that return JSON (call_json), this agent
    returns plain text (call). Same execute() interface, different
    internal behavior. The pipeline doesn't need to know the difference.
    """

    @property
    def name(self) -> str:
        return "Cover Letter Writer"

    @property
    def step(self) -> PipelineStep:
        return PipelineStep.COVER_LETTER

    def _validate_input(self, **kwargs) -> None:
        """Validate resume text and keywords are provided."""
        self._require_non_empty(kwargs.get("resume_text", ""), "resume_text")
        self._require_non_empty_list(kwargs.get("keywords", []), "keywords")

    def _process(self, **kwargs) -> str:
        """
        Call LLM to generate cover letter.

        OOP Concept: This returns a STRING, not a dict.
        Other agents return dicts from call_json(). This demonstrates
        polymorphism — same interface, different return types handled
        by _format_output.
        """
        role_context = f"Target Role: {kwargs.get('target_role', '')}" if kwargs.get("target_role") else ""

        user_prompt = COVER_LETTER_USER(
            resume_text=kwargs["resume_text"],
            keywords=", ".join(kwargs["keywords"]),
            responsibilities=", ".join(kwargs.get("responsibilities", [])),
            role_context=role_context,
        )

        # Note: call() not call_json() — cover letter is plain text
        return self._llm_client.call(
            system_prompt=str(COVER_LETTER_SYSTEM),
            user_prompt=user_prompt,
        )

    def _format_output(self, raw_result: Any) -> str:
        """
        Format output — for cover letter, it's already a string.

        OOP Concept: Even though this is trivial, we still implement it
        to satisfy the abstract method contract. The base class doesn't
        know that some agents return strings and some return dicts.
        """
        return raw_result.strip()

    # ── Extended Method ──────────────────────────────────────────────────────

    def revise(
        self,
        cover_letter: str,
        keywords: list[str],
        issues: list[str],
        suggestions: list[str],
        resume_text: str,
    ) -> str:
        """
        Revise cover letter based on critic feedback.

        Args:
            cover_letter: Current cover letter text.
            keywords: JD keywords.
            issues: Critic-identified issues.
            suggestions: Critic suggestions.
            resume_text: Original resume for fact-checking.

        Returns:
            Revised cover letter string.
        """
        user_prompt = REVISION_COVER_LETTER_USER(
            cover_letter=cover_letter,
            keywords=", ".join(keywords),
            issues="\n".join(f"  - {i}" for i in issues),
            suggestions="\n".join(f"  - {s}" for s in suggestions),
            resume_text=resume_text,
        )

        try:
            return self._llm_client.call(
                system_prompt=str(REVISION_SYSTEM),
                user_prompt=user_prompt,
            ).strip()
        except Exception as e:
            import logging
            logging.getLogger(__name__).warning(f"Cover letter revision failed: {e}. Keeping original.")
            return cover_letter
