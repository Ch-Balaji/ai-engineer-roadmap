"""
Resume JD Tailor Agent — FastAPI Backend

Serves the HTML frontend and provides an SSE endpoint
that streams pipeline progress to the browser in real time.

Run with:  uvicorn server:app --reload --port 8501
"""

import sys
import json
import asyncio
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from agents.jd_extractor import extract_jd_skills
from agents.resume_matcher import match_resume
from agents.resume_rewriter import rewrite_bullets, revise_bullets
from agents.cover_letter_writer import write_cover_letter, revise_cover_letter
from agents.critic_agent import critique
from agents.interview_generator import generate_interview_questions

app = FastAPI(title="Resume JD Tailor Agent")

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

MAX_REVISION_LOOPS = 2
CRITIC_THRESHOLD = 8


@app.get("/", response_class=HTMLResponse)
async def index():
    """Serve the main HTML page."""
    html_path = Path(__file__).parent / "static" / "index.html"
    return HTMLResponse(html_path.read_text())


@app.post("/api/run")
async def run_pipeline(request: Request):
    """
    Run the agent pipeline and stream results via Server-Sent Events.

    Each SSE message is a JSON object with:
      - type: "step" | "result" | "error" | "done"
      - step: current step number (0-6)
      - label: human-readable step label
      - data: step result payload (for "result" type)
    """
    body = await request.json()
    resume_text = body.get("resume", "").strip()
    jd_text = body.get("jd", "").strip()
    target_role = body.get("role", "").strip()

    if not resume_text or not jd_text:
        return {"error": "Resume and JD text are required."}

    async def event_stream():
        try:
            # Step 1: JD Extraction
            yield _sse({"type": "step", "step": 0, "label": "Analyzing Job Description..."})
            await asyncio.sleep(0)  # yield control
            jd_analysis = await asyncio.to_thread(extract_jd_skills, jd_text, target_role)
            keywords = jd_analysis.get("top_keywords", [])
            responsibilities = jd_analysis.get("responsibilities", [])
            yield _sse({"type": "result", "step": 0, "key": "jd_analysis", "data": jd_analysis})

            # Step 2: Resume Matching
            yield _sse({"type": "step", "step": 1, "label": "Matching Resume to JD..."})
            match_analysis = await asyncio.to_thread(match_resume, resume_text, jd_text)
            missing_skills = match_analysis.get("missing_skills", [])
            yield _sse({"type": "result", "step": 1, "key": "match_analysis", "data": match_analysis})

            # Step 3: Bullet Rewriting
            yield _sse({"type": "step", "step": 2, "label": "Rewriting Resume Bullets..."})
            bullets = await asyncio.to_thread(rewrite_bullets, resume_text, keywords)
            yield _sse({"type": "result", "step": 2, "key": "bullets", "data": bullets})

            # Step 4: Cover Letter
            yield _sse({"type": "step", "step": 3, "label": "Drafting Cover Letter..."})
            cover_letter = await asyncio.to_thread(
                write_cover_letter, resume_text, keywords, responsibilities, target_role
            )
            yield _sse({"type": "result", "step": 3, "key": "cover_letter", "data": cover_letter})

            # Step 5: Critic Review
            yield _sse({"type": "step", "step": 4, "label": "Running Critic Review..."})
            critic_result = await asyncio.to_thread(critique, bullets, cover_letter, keywords)
            yield _sse({"type": "result", "step": 4, "key": "critic", "data": critic_result})

            # Step 6: Revision Loop
            revision_count = 0
            while critic_result["score"] < CRITIC_THRESHOLD and revision_count < MAX_REVISION_LOOPS:
                revision_count += 1
                yield _sse({
                    "type": "step", "step": 5,
                    "label": f"Revising (attempt {revision_count}/{MAX_REVISION_LOOPS})..."
                })
                issues = critic_result.get("issues", [])
                suggestions = critic_result.get("suggestions", [])

                bullets = await asyncio.to_thread(
                    revise_bullets, bullets, keywords, issues, suggestions, resume_text
                )
                cover_letter = await asyncio.to_thread(
                    revise_cover_letter, cover_letter, keywords, issues, suggestions, resume_text
                )
                critic_result = await asyncio.to_thread(critique, bullets, cover_letter, keywords)

            yield _sse({"type": "result", "step": 5, "key": "revision", "data": {
                "bullets": bullets,
                "cover_letter": cover_letter,
                "critic": critic_result,
                "revision_count": revision_count,
            }})

            # Step 7: Interview Questions
            yield _sse({"type": "step", "step": 6, "label": "Generating Interview Questions..."})
            interview_qs = await asyncio.to_thread(
                generate_interview_questions, resume_text, jd_text, keywords, missing_skills
            )
            yield _sse({"type": "result", "step": 6, "key": "interview_questions", "data": interview_qs})

            yield _sse({"type": "done"})

        except Exception as e:
            yield _sse({"type": "error", "message": str(e)})

    return StreamingResponse(event_stream(), media_type="text/event-stream")


def _sse(data: dict) -> str:
    """Format a dict as an SSE message."""
    return f"data: {json.dumps(data)}\n\n"
