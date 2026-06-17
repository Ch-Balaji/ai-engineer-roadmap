# Async AI Agent Demo

Companion code for the YouTube video **"I Made My AI Agent 3× Faster With One Python Keyword (2026)"**.

Two minimal Streamlit chatbots side-by-side. Same UI, same model (`gpt-4o-mini`), same mocked travel-planner tools. The **only** difference is the agent loop — sync vs `asyncio.gather`.

## What you'll see

| | 🐢 Sync (port 8501) | ⚡ Async (port 8502) |
|---|---|---|
| Tool execution | One at a time | All in parallel via `asyncio.gather` |
| 5-city demo (10 tool calls) | ~33 seconds | ~12 seconds |
| Speedup | — | **2.8×** (verified live, 29 May 2026) |

## Setup

```bash
cd projects/async-agent-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The chatbot reads `OPENAI_API_KEY` automatically from the project-root `.env` (key name: `openaiapikey`).

## Run both side-by-side

In two terminals:

```bash
# Terminal 1
streamlit run sync_agent.py --server.port 8501
```

```bash
# Terminal 2
streamlit run async_agent.py --server.port 8502
```

Open `http://localhost:8501` and `http://localhost:8502` side-by-side. Paste the same prompt in both:

> Plan a 5-day trip across Hyderabad, Bangalore, Chennai, Mysore, and Pondicherry. I want weather and top attractions for each city.

Watch the timers.

## Files

| File | What it is |
|---|---|
| `agent_core.py` | LLM client, mocked tools, both agent loops. The sync/async diff is ~5 lines. |
| `sync_agent.py` | Streamlit UI for the sync agent. ~50 lines. |
| `async_agent.py` | Streamlit UI for the async agent. ~50 lines. |
| `minimal_demo.ipynb` | Scene 6–7 teaching notebook: `async def` / `await` definitions, ASCII flow diagrams, micro-example, sync vs `asyncio.gather` (3× demo). |
| `_verify.py` | CLI smoke test — runs both agents and prints timings. |

## The actual diff between sync and async

```python
# sync — one tool at a time
for tc in assistant_msg.tool_calls:
    result = _execute_tool_sync(tc.function.name, json.loads(tc.function.arguments))
    messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})

# async — every tool fired at once
results = await asyncio.gather(*[
    _execute_tool_async(tc.function.name, json.loads(tc.function.arguments))
    for tc in assistant_msg.tool_calls
])
for tc, result in zip(assistant_msg.tool_calls, results):
    messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
```

That's the whole lesson.

## Honest disclosure (matches video)

Tools are mocked with `await asyncio.sleep(2.0)` — that's a realistic average for a real weather, web-search, or scraping API. Swap in real APIs (OpenWeather, SerpAPI, etc.) and you get the same speedup; the mock just makes the timer clean and reproducible.

The two LLM round-trips (`planning` + `synthesis`) take ~10 seconds combined and **cannot** be parallelized in this style of agent — that's why the speedup floor is around 3× and not 10×. We discuss this honestly in Scene 10 of the video.
