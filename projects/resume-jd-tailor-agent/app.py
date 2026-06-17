"""
Resume JD Tailor Agent — Flask Backend

Serves the frontend and provides an SSE endpoint that streams
pipeline progress to the browser in real time.

Run with:  python app.py
"""

import sys
import json
import traceback
from pathlib import Path

from flask import Flask, request, Response, send_from_directory

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from agents.jd_extractor import extract_jd_skills
from agents.resume_matcher import match_resume
from agents.resume_rewriter import rewrite_bullets, revise_bullets
from agents.cover_letter_writer import write_cover_letter, revise_cover_letter
from agents.critic_agent import critique
from agents.interview_generator import generate_interview_questions

app = Flask(__name__, static_folder="static", static_url_path="/static")

MAX_REVISION_LOOPS = 2
CRITIC_THRESHOLD = 8


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/run", methods=["POST"])
def run_pipeline():
    """
    SSE endpoint — streams JSON events as the pipeline progresses.
    Each event is: data: {"step": ..., "status": ..., "payload": ...}
    """
    data = request.get_json()
    resume_text = data.get("resume", "").strip()
    jd_text = data.get("jd", "").strip()
    target_role = data.get("role", "").strip()

    if not resume_text or not jd_text:
        return Response(
            json.dumps({"error": "Resume and JD are required."}),
            status=400,
            content_type="application/json",
        )

    def generate():
        try:
            # Step 1
            yield _event("step", {"step": 1, "label": "Analyzing Job Description"})
            jd_analysis = extract_jd_skills(jd_text, target_role)
            keywords = jd_analysis.get("top_keywords", [])
            responsibilities = jd_analysis.get("responsibilities", [])
            yield _event("result", {"step": 1, "data": jd_analysis})

            # Step 2
            yield _event("step", {"step": 2, "label": "Matching Resume"})
            match_analysis = match_resume(resume_text, jd_text)
            missing_skills = match_analysis.get("missing_skills", [])
            yield _event("result", {"step": 2, "data": match_analysis})

            # Step 3
            yield _event("step", {"step": 3, "label": "Rewriting Bullets"})
            bullets = rewrite_bullets(resume_text, keywords)
            yield _event("result", {"step": 3, "data": {"bullets": bullets}})

            # Step 4
            yield _event("step", {"step": 4, "label": "Drafting Cover Letter"})
            cover_letter = write_cover_letter(
                resume_text, keywords, responsibilities, target_role
            )
            yield _event("result", {"step": 4, "data": {"cover_letter": cover_letter}})

            # Step 5
            yield _event("step", {"step": 5, "label": "Critic Review"})
            critic_result = critique(bullets, cover_letter, keywords)
            yield _event("result", {"step": 5, "data": critic_result})

            # Step 6 — revision loop
            revision_count = 0
            while (
                critic_result["score"] < CRITIC_THRESHOLD
                and revision_count < MAX_REVISION_LOOPS
            ):
                revision_count += 1
                yield _event("step", {
                    "step": 6,
                    "label": f"Revision {revision_count}/{MAX_REVISION_LOOPS}",
                })
                issues = critic_result.get("issues", [])
                suggestions = critic_result.get("suggestions", [])

                bullets = revise_bullets(
                    bullets, keywords, issues, suggestions, resume_text
                )
                cover_letter = revise_cover_letter(
                    cover_letter, keywords, issues, suggestions, resume_text
                )
                critic_result = critique(bullets, cover_letter, keywords)

            yield _event("result", {
                "step": 6,
                "data": {
                    "bullets": bullets,
                    "cover_letter": cover_letter,
                    "critic": critic_result,
                    "revision_count": revision_count,
                },
            })

            # Step 7
            yield _event("step", {"step": 7, "label": "Generating Interview Questions"})
            interview_qs = generate_interview_questions(
                resume_text, jd_text, keywords, missing_skills
            )
            yield _event("result", {"step": 7, "data": {"questions": interview_qs}})

            # Done
            yield _event("done", {"message": "Pipeline complete"})

        except Exception as e:
            traceback.print_exc()
            yield _event("error", {"message": str(e)})

    return Response(generate(), content_type="text/event-stream")


def _event(event_type: str, payload: dict) -> str:
    """Format a Server-Sent Event."""
    data = json.dumps({"type": event_type, **payload})
    return f"data: {data}\n\n"


if __name__ == "__main__":
    app.run(debug=False, port=5000)
