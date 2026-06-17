"""
Step 1: JD Skill Extractor

Analyzes a job description and extracts structured information
including keywords, skills, tools, responsibilities, and seniority.
"""

from utils.llm_client import call_llm_json
from utils.prompts import JD_EXTRACTOR_SYSTEM, JD_EXTRACTOR_USER


def extract_jd_skills(jd_text: str, target_role: str = "") -> dict:
    """
    Extract structured information from a job description.

    Args:
        jd_text: The full job description text.
        target_role: Optional target role/title for context.

    Returns:
        Dict with keys: top_keywords, must_have_skills,
        nice_to_have_skills, tools_technologies,
        responsibilities, seniority_level.
    """
    role_context = f"Target Role: {target_role}" if target_role else ""

    user_prompt = JD_EXTRACTOR_USER.format(
        jd_text=jd_text,
        role_context=role_context,
    )

    result = call_llm_json(JD_EXTRACTOR_SYSTEM, user_prompt)

    # Ensure all expected keys exist with defaults
    defaults = {
        "top_keywords": [],
        "must_have_skills": [],
        "nice_to_have_skills": [],
        "tools_technologies": [],
        "responsibilities": [],
        "seniority_level": "Unknown",
    }
    for key, default in defaults.items():
        if key not in result:
            result[key] = default

    return result
