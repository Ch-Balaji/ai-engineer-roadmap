"""
Step 2: Resume Matcher

Compares a resume against a job description and produces
a match score with detailed skill analysis.
"""

from utils.llm_client import call_llm_json
from utils.prompts import RESUME_MATCHER_SYSTEM, RESUME_MATCHER_USER


def match_resume(resume_text: str, jd_text: str) -> dict:
    """
    Compare resume against job description.

    Args:
        resume_text: The candidate's resume text.
        jd_text: The job description text.

    Returns:
        Dict with keys: match_score, matched_skills,
        missing_skills, weak_skills, sections_to_improve,
        score_explanation.
    """
    user_prompt = RESUME_MATCHER_USER.format(
        resume_text=resume_text,
        jd_text=jd_text,
    )

    result = call_llm_json(RESUME_MATCHER_SYSTEM, user_prompt)

    # Ensure all expected keys exist
    defaults = {
        "match_score": 0,
        "matched_skills": [],
        "missing_skills": [],
        "weak_skills": [],
        "sections_to_improve": [],
        "score_explanation": "",
    }
    for key, default in defaults.items():
        if key not in result:
            result[key] = default

    # Clamp score to 0-100
    result["match_score"] = max(0, min(100, int(result["match_score"])))

    return result
