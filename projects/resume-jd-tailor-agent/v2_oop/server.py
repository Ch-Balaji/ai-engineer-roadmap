"""
Resume JD Tailor Agent v2 — FastAPI Backend (OOP Version)

OOP Concepts Demonstrated:
- Composition: Server uses Pipeline object
- Context Manager: LLMClient lifecycle managed by Pipeline
- Generator: Streaming via run_streaming()
- Separation of Concerns: Server only handles HTTP, Pipeline handles logic

Run with:  uvicorn server:app --reload --port 8502
"""

import sys
import json
import asyncio
import logging
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import PipelineConfig
from pipeline import Pipeline
from exceptions import AgentError, InputValidationError, PipelineError

# ── Logging Setup ────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# ── App Setup ────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Resume JD Tailor Agent v2 (OOP)",
    description="OOP-refactored version with classes, error handling, and rate limiting",
    version="2.0.0",
)

# Serve static files from the v1 static directory (reuse frontend)
_static_dir = Path(__file__).parent.parent / "static"
if _static_dir.exists():
    app.mount("/static", StaticFiles(directory=_static_dir), name="static")

# Load configuration
config = PipelineConfig.from_env()
logger.info(f"Server starting with config: {config}")


# ── Routes ───────────────────────────────────────────────────────────────────


@app.get("/", response_class=HTMLResponse)
async def index():
    """Serve the main HTML page."""
    html_path = _static_dir / "index.html"
    if not html_path.exists():
        raise HTTPException(status_code=404, detail="Frontend not found")
    return HTMLResponse(html_path.read_text())


@app.post("/api/run")
async def run_pipeline(request: Request):
    """
    Run the agent pipeline and stream results via Server-Sent Events.

    OOP in action:
    - Pipeline object handles all orchestration
    - Custom exceptions provide clear error codes
    - Streaming via generator pattern
    """
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON body")

    resume_text = body.get("resume", "").strip()
    jd_text = body.get("jd", "").strip()
    target_role = body.get("role", "").strip()

    # Input validation with proper HTTP error codes
    if not resume_text:
        raise HTTPException(
            status_code=422,
            detail={"error": "Resume text is required", "field": "resume"},
        )
    if not jd_text:
        raise HTTPException(
            status_code=422,
            detail={"error": "Job description text is required", "field": "jd"},
        )

    async def event_stream():
        """
        Async generator that wraps the synchronous pipeline streaming.

        OOP Concept: Adapter pattern — adapts sync generator to async.
        """
        # Create a fresh pipeline for each request
        pipeline = Pipeline(config)

        try:
            # Run the pipeline in a thread to not block the event loop
            # The pipeline's run_streaming() is a sync generator,
            # so we iterate it in a thread
            def run_sync():
                return list(pipeline.run_streaming(
                    resume_text=resume_text,
                    jd_text=jd_text,
                    target_role=target_role,
                ))

            events = await asyncio.to_thread(run_sync)

            for event in events:
                yield _sse(event)
                await asyncio.sleep(0)  # Yield control to event loop

        except InputValidationError as e:
            logger.warning(f"Validation error: {e}")
            yield _sse({"type": "error", "message": str(e), "code": 422})

        except PipelineError as e:
            logger.error(f"Pipeline error at step {e.step}: {e}")
            yield _sse({"type": "error", "message": str(e), "code": 500, "step": e.step})

        except AgentError as e:
            logger.error(f"Agent error: {e}")
            yield _sse({"type": "error", "message": str(e), "code": 500})

        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            yield _sse({"type": "error", "message": f"Internal error: {e}", "code": 500})

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/api/health")
async def health_check():
    """
    Health check endpoint.

    Returns server status and configuration summary.
    """
    return {
        "status": "healthy",
        "version": "2.0.0",
        "model": config.llm.model_id,
        "region": config.llm.region,
        "max_revisions": config.max_revision_loops,
        "critic_threshold": config.critic_threshold,
    }


# ── Helpers ──────────────────────────────────────────────────────────────────


def _sse(data: dict) -> str:
    """Format a dict as a Server-Sent Event message."""
    return f"data: {json.dumps(data)}\n\n"
