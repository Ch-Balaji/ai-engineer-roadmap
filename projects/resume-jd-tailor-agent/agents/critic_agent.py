"""
Step 5: Critic Agent

A second LLM persona that reviews the rewritten bullets
and cover letter, scoring them on multiple criteria.
"""

from utils.llm_client import call_llm_json
from utils.prompts import CRITIC_SYSTEM, CRITIC_USER


def critique(
    bullets: list[dict],
    cover_letter: str,
    keywords: list[str],
) -> dict:
    """
    Review rewritten bullets and cover letter.

    Args:
        bullets: List of bullet dicts (each with 'rewritten' key).
        cover_letter: The generated cover letter text.
        keywords: JD keywords for relevance checking.

    Returns:
        Dict with keys: score (1-10), issues, suggestions.
    """
    # Format bullets for the prompt
    bullets_text = "\n".join(
        f"- {b.get('rewritten', b.get('original', ''))}"
        for b in bullets
    )

    user_prompt = CRITIC_USER.format(
        bullets_text=bullets_text,
        cover_letter=cover_letter,
        keywords=", ".join(keywords),
    )

    result = call_llm_json(CRITIC_SYSTEM, user_prompt)

    # Ensure expected keys
    defaults = {"score": 5, "issues": [], "suggestions": []}
    for key, default in defaults.items():
        if key not in result:
            result[key] = default

    # Clamp score
    result["score"] = max(1, min(10, int(result["score"])))

    return result
