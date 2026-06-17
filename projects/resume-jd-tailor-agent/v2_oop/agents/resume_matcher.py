"""
Resume Matcher Agent — Compares resume against JD.

OOP Concepts Demonstrated:
- Inheritance: Extends BaseAgent
- Method Override: Implements abstract methods
- Encapsulation: Match-specific logic isolated here
- Type Safety: Returns typed MatchAnalysis model
"""

from typing import Any

from agents.base import BaseAgent
from models import MatchAnalysis, PipelineStep
from prompts import RESUME_MATCHER_SYSTEM, RESUME_MATCHER_USER


class ResumeMatcherAgent(BaseAgent):
    """
    Compares a resume against a job description and produces a match score.

    This agent needs BOTH resume_text and jd_text — demonstrating how
    different agents have different input requirements while sharing
    the same execute() interface (polymorphism).
    """

    @property
    def name(self) -> str:
        return "Resume Matcher"

    @property
    def step(self) -> PipelineStep:
        return PipelineStep.RESUME_MATCHING

    def _validate_input(self, **kwargs) -> None:
        """Validate both resume and JD text are provided."""
        self._require_non_empty(kwargs.get("resume_text", ""), "resume_text")
        self._require_non_empty(kwargs.get("jd_text", ""), "jd_text")

    def _process(self, **kwargs) -> dict:
        """Call LLM to compare resume against JD."""
        user_prompt = RESUME_MATCHER_USER(
            resume_text=kwargs["resume_text"],
            jd_text=kwargs["jd_text"],
        )

        return self._llm_client.call_json(
            system_prompt=str(RESUME_MATCHER_SYSTEM),
            user_prompt=user_prompt,
        )

    def _format_output(self, raw_result: Any) -> MatchAnalysis:
        """Parse into validated MatchAnalysis model."""
        try:
            return MatchAnalysis(**raw_result)
        except Exception:
            defaults = {
                "match_score": 0,
                "matched_skills": [],
                "missing_skills": [],
                "weak_skills": [],
                "sections_to_improve": [],
                "score_explanation": "",
            }
            merged = {**defaults, **raw_result}
            return MatchAnalysis(**merged)
