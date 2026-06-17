"""
Step 3: Resume Bullet Rewriter

Rewrites resume bullet points to better align with the JD
without inventing fake experience.
"""

from utils.llm_client import call_llm_json
from utils.prompts import (
    REWRITER_SYSTEM,
    REWRITER_USER,
    REVISION_SYSTEM,
    REVISION_BULLETS_USER,
)


def rewrite_bullets(resume_text: str, keywords: list[str]) -> list[dict]:
    """
    Rewrite 4-5 resume bullets for better JD alignment.

    Args:
        resume_text: The candidate's resume text.
        keywords: Top keywords from the JD.

    Returns:
        List of dicts, each with: original, rewritten, changes_made.
    """
    user_prompt = REWRITER_USER.format(
        resume_text=resume_text,
        keywords=", ".join(keywords),
    )

    result = call_llm_json(REWRITER_SYSTEM, user_prompt)
    return result.get("bullets", [])


def revise_bullets(
    bullets: list[dict],
    keywords: list[str],
    issues: list[str],
    suggestions: list[str],
    resume_text: str,
) -> list[dict]:
    """
    Revise bullets based on critic feedback.

    Args:
        bullets: Current bullet list (each with original/rewritten).
        keywords: JD keywords.
        issues: Critic-identified issues.
        suggestions: Critic suggestions.
        resume_text: Original resume for fact-checking.

    Returns:
        Revised list of bullet dicts.
    """
    # Format current bullets for the prompt
    bullets_text = "\n".join(
        f"- {b.get('rewritten', b.get('original', ''))}"
        for b in bullets
    )

    user_prompt = REVISION_BULLETS_USER.format(
        bullets_text=bullets_text,
        keywords=", ".join(keywords),
        issues="\n".join(f"  - {i}" for i in issues),
        suggestions="\n".join(f"  - {s}" for s in suggestions),
        resume_text=resume_text,
    )

    result = call_llm_json(REVISION_SYSTEM, user_prompt)
    return result.get("bullets", bullets)
