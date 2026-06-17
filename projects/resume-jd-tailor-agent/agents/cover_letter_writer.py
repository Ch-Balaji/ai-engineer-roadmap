"""
Step 4: Cover Letter Writer

Generates a 3-paragraph cover letter that maps resume
strengths to JD requirements without faking experience.
"""

from utils.llm_client import call_llm
from utils.prompts import (
    COVER_LETTER_SYSTEM,
    COVER_LETTER_USER,
    REVISION_SYSTEM,
    REVISION_COVER_LETTER_USER,
)


def write_cover_letter(
    resume_text: str,
    keywords: list[str],
    responsibilities: list[str],
    target_role: str = "",
) -> str:
    """
    Generate a 3-paragraph cover letter.

    Args:
        resume_text: The candidate's resume text.
        keywords: Top keywords from the JD.
        responsibilities: Key responsibilities from the JD.
        target_role: Optional target role title.

    Returns:
        The cover letter as a string.
    """
    role_context = f"Target Role: {target_role}" if target_role else ""

    user_prompt = COVER_LETTER_USER.format(
        resume_text=resume_text,
        keywords=", ".join(keywords),
        responsibilities=", ".join(responsibilities),
        role_context=role_context,
    )

    return call_llm(COVER_LETTER_SYSTEM, user_prompt)


def revise_cover_letter(
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
    user_prompt = REVISION_COVER_LETTER_USER.format(
        cover_letter=cover_letter,
        keywords=", ".join(keywords),
        issues="\n".join(f"  - {i}" for i in issues),
        suggestions="\n".join(f"  - {s}" for s in suggestions),
        resume_text=resume_text,
    )

    return call_llm(REVISION_SYSTEM, user_prompt)
