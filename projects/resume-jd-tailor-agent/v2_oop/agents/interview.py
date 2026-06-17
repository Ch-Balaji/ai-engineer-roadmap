"""
Interview Question Generator Agent.

OOP Concepts Demonstrated:
- Inheritance: Extends BaseAgent
- Method Override: Implements abstract methods
- Type Safety: Returns list of InterviewQuestion models
"""

from typing import Any

from agents.base import BaseAgent
from models import InterviewQuestion, PipelineStep
from prompts import INTERVIEW_SYSTEM, INTERVIEW_USER


class InterviewAgent(BaseAgent):
    """
    Generates likely interview questions based on JD and resume.

    This is the final agent in the pipeline. It uses information
    gathered by earlier agents (keywords, missing skills) to generate
    targeted interview preparation material.
    """

    @property
    def name(self) -> str:
        return "Interview Generator"

    @property
    def step(self) -> PipelineStep:
        return PipelineStep.INTERVIEW_QUESTIONS

    def _validate_input(self, **kwargs) -> None:
        """Validate resume, JD, and keywords are provided."""
        self._require_non_empty(kwargs.get("resume_text", ""), "resume_text")
        self._require_non_empty(kwargs.get("jd_text", ""), "jd_text")
        self._require_non_empty_list(kwargs.get("keywords", []), "keywords")

    def _process(self, **kwargs) -> dict:
        """Call LLM to generate interview questions."""
        missing_skills = kwargs.get("missing_skills", [])

        user_prompt = INTERVIEW_USER(
            resume_text=kwargs["resume_text"],
            jd_text=kwargs["jd_text"],
            keywords=", ".join(kwargs["keywords"]),
            missing_skills=", ".join(missing_skills) if missing_skills else "None identified",
        )

        return self._llm_client.call_json(
            system_prompt=str(INTERVIEW_SYSTEM),
            user_prompt=user_prompt,
        )

    def _format_output(self, raw_result: Any) -> list[InterviewQuestion]:
        """Parse into list of InterviewQuestion models."""
        questions_data = raw_result.get("questions", [])
        questions = []
        for q in questions_data:
            try:
                questions.append(InterviewQuestion(**q))
            except Exception:
                continue
        return questions
