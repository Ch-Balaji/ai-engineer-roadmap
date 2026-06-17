"""
Step 7: Interview Question Generator

Generates likely interview questions based on the JD,
resume, and identified gaps.
"""

from utils.llm_client import call_llm_json
from utils.prompts import INTERVIEW_SYSTEM, INTERVIEW_USER


def generate_interview_questions(
    resume_text: str,
    jd_text: str,
    keywords: list[str],
    missing_skills: list[str],
) -> list[dict]:
    """
    Generate 5 likely interview questions.

    Args:
        resume_text: The candidate's resume.
        jd_text: The job description.
        keywords: Top JD keywords.
        missing_skills: Skills missing from the resume.

    Returns:
        List of dicts, each with: question, why_asked,
        preparation_hint.
    """
    user_prompt = INTERVIEW_USER.format(
        resume_text=resume_text,
        jd_text=jd_text,
        keywords=", ".join(keywords),
        missing_skills=", ".join(missing_skills) if missing_skills else "None identified",
    )

    result = call_llm_json(INTERVIEW_SYSTEM, user_prompt)
    return result.get("questions", [])
