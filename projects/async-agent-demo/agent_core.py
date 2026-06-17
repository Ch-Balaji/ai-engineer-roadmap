"""Shared core: LLM client, mocked tools, and the two agent loops.

The ONLY real difference between the sync and async agent is in how the
tool calls are executed:

    sync :   for tc in tool_calls:    result = tool(...)        # one at a time
    async:   await asyncio.gather(*[tool_async(...) for tc in tool_calls])   # in parallel

Everything else is identical so the comparison is honest.
"""

from __future__ import annotations

import asyncio
import json
import os
import random
import time
from pathlib import Path

from openai import AsyncOpenAI, OpenAI


def _load_api_key() -> None:
    """Load OPENAI_API_KEY from the project .env (key name: openaiapikey)."""
    if os.environ.get("OPENAI_API_KEY"):
        return
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        if "=" not in line:
            continue
        k, v = line.strip().split("=", 1)
        if k.lower() == "openaiapikey":
            os.environ["OPENAI_API_KEY"] = v
            return


_load_api_key()

MODEL = "gpt-4o-mini"
MOCK_LATENCY_SECONDS = 2.0

sync_client = OpenAI()
async_client = AsyncOpenAI()


def _mock_weather(city: str) -> dict:
    return {
        "city": city,
        "temperature_c": random.randint(22, 36),
        "condition": random.choice(["sunny", "partly cloudy", "light rain", "humid"]),
        "humidity_pct": random.randint(40, 85),
    }


def _mock_attractions(city: str) -> dict:
    pool = {
        "Hyderabad": ["Charminar", "Golconda Fort", "Ramoji Film City"],
        "Bangalore": ["Lalbagh", "Cubbon Park", "Bangalore Palace"],
        "Chennai": ["Marina Beach", "Kapaleeshwarar Temple", "Fort St. George"],
        "Mysore": ["Mysore Palace", "Chamundi Hill", "Brindavan Gardens"],
        "Pondicherry": ["Promenade Beach", "Auroville", "French Quarter"],
    }
    return {"city": city, "top_attractions": pool.get(city, ["City Center", "Local Market", "Old Town"])}


def get_weather_sync(city: str) -> dict:
    time.sleep(MOCK_LATENCY_SECONDS)
    return _mock_weather(city)


def get_attractions_sync(city: str) -> dict:
    time.sleep(MOCK_LATENCY_SECONDS)
    return _mock_attractions(city)


async def get_weather_async(city: str) -> dict:
    await asyncio.sleep(MOCK_LATENCY_SECONDS)
    return _mock_weather(city)


async def get_attractions_async(city: str) -> dict:
    await asyncio.sleep(MOCK_LATENCY_SECONDS)
    return _mock_attractions(city)


TOOL_SPECS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city. Mocked, ~2s latency (like a real API).",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_attractions",
            "description": "Get top tourist attractions for a city. Mocked, ~2s latency.",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    },
]


SYSTEM_PROMPT = (
    "You are a travel-planner assistant. When the user asks about cities, "
    "call get_weather and get_attractions for each city in parallel before answering. "
    "After tools return, write a short, helpful itinerary. Keep the final answer under 300 words."
)


def _execute_tool_sync(name: str, args: dict) -> str:
    if name == "get_weather":
        return json.dumps(get_weather_sync(args["city"]))
    if name == "get_attractions":
        return json.dumps(get_attractions_sync(args["city"]))
    return json.dumps({"error": f"unknown tool {name}"})


async def _execute_tool_async(name: str, args: dict) -> str:
    if name == "get_weather":
        return json.dumps(await get_weather_async(args["city"]))
    if name == "get_attractions":
        return json.dumps(await get_attractions_async(args["city"]))
    return json.dumps({"error": f"unknown tool {name}"})


def run_sync_agent(user_message: str, on_tool_start=None, on_tool_done=None) -> dict:
    """Sync agent loop. Tools are called one after another."""
    t0 = time.perf_counter()
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    first = sync_client.chat.completions.create(
        model=MODEL, messages=messages, tools=TOOL_SPECS,
    )
    assistant_msg = first.choices[0].message

    tool_timings = []
    if assistant_msg.tool_calls:
        messages.append(assistant_msg)
        for tc in assistant_msg.tool_calls:
            args = json.loads(tc.function.arguments)
            label = f"{tc.function.name}({args.get('city', '')})"
            if on_tool_start:
                on_tool_start(label)
            t_tool = time.perf_counter()
            result = _execute_tool_sync(tc.function.name, args)
            elapsed = time.perf_counter() - t_tool
            tool_timings.append((label, elapsed))
            if on_tool_done:
                on_tool_done(label, elapsed)
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })

        final = sync_client.chat.completions.create(model=MODEL, messages=messages)
        answer = final.choices[0].message.content or ""
    else:
        answer = assistant_msg.content or ""

    tools_elapsed = sum(t for _, t in tool_timings)
    return {
        "answer": answer,
        "total_time": time.perf_counter() - t0,
        "tool_timings": tool_timings,
        "tool_count": len(tool_timings),
        "tools_elapsed": tools_elapsed,
    }


async def run_async_agent(user_message: str, on_tools_start=None, on_tools_done=None) -> dict:
    """Async agent loop. All tool calls run concurrently."""
    t0 = time.perf_counter()
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    first = await async_client.chat.completions.create(
        model=MODEL, messages=messages, tools=TOOL_SPECS,
    )
    assistant_msg = first.choices[0].message

    tool_labels = []
    parallel_elapsed = 0.0
    if assistant_msg.tool_calls:
        messages.append(assistant_msg)
        labels = []
        coros = []
        for tc in assistant_msg.tool_calls:
            args = json.loads(tc.function.arguments)
            label = f"{tc.function.name}({args.get('city', '')})"
            labels.append(label)
            coros.append(_execute_tool_async(tc.function.name, args))

        if on_tools_start:
            on_tools_start(labels)
        t_tools = time.perf_counter()
        results = await asyncio.gather(*coros)
        parallel_elapsed = time.perf_counter() - t_tools
        if on_tools_done:
            on_tools_done(labels, parallel_elapsed)

        for tc, result in zip(assistant_msg.tool_calls, results):
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result,
            })
        tool_labels = labels

        final = await async_client.chat.completions.create(model=MODEL, messages=messages)
        answer = final.choices[0].message.content or ""
    else:
        answer = assistant_msg.content or ""

    return {
        "answer": answer,
        "total_time": time.perf_counter() - t0,
        "tool_labels": tool_labels,
        "tool_count": len(tool_labels),
        "tools_elapsed": parallel_elapsed,
        "parallel_elapsed": parallel_elapsed,
    }
