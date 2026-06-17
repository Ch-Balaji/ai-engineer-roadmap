"""
AWS Bedrock Claude LLM client.

Provides reusable functions to call Claude via AWS Bedrock.
Uses the same pattern as the existing sb4-poc-bkx project.
"""

import json
import os
from pathlib import Path

import boto3
from botocore.config import Config
from dotenv import load_dotenv

# Load .env from project root
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_env_path)

# Configuration from environment
AWS_REGION = os.getenv("AWS_REGION", "eu-central-1")
AWS_PROFILE = os.getenv("AWS_PROFILE", "")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "eu.anthropic.claude-sonnet-4-20250514")

# Bedrock client config — generous timeout for longer generations
BEDROCK_CONFIG = Config(
    read_timeout=300,
    connect_timeout=10,
    retries={"max_attempts": 2, "mode": "adaptive"},
)

_client = None


def _get_client():
    """Lazy-init the Bedrock runtime client."""
    global _client
    if _client is None:
        # Use a named profile (e.g. SSO) if configured, otherwise default chain
        session = boto3.Session(
            profile_name=AWS_PROFILE if AWS_PROFILE else None,
            region_name=AWS_REGION,
        )
        _client = session.client(
            "bedrock-runtime",
            config=BEDROCK_CONFIG,
        )
    return _client


def call_llm(system_prompt: str, user_prompt: str, max_tokens: int = 4096) -> str:
    """
    Call Claude via AWS Bedrock and return the text response.

    Args:
        system_prompt: The system-level instruction for the model.
        user_prompt: The user message / task content.
        max_tokens: Maximum tokens in the response.

    Returns:
        The model's text response.

    Raises:
        RuntimeError: If the response is truncated or the API call fails.
    """
    try:
        response = _get_client().invoke_model(
            modelId=BEDROCK_MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": max_tokens,
                "system": system_prompt,
                "messages": [{"role": "user", "content": user_prompt}],
            }),
        )
        result = json.loads(response["body"].read())

        # Check for truncation
        stop_reason = result.get("stop_reason", "")
        if stop_reason == "max_tokens":
            raise RuntimeError(
                f"LLM response truncated at {max_tokens} tokens. "
                "Try increasing max_tokens or reducing prompt size."
            )

        return result["content"][0]["text"]

    except RuntimeError:
        raise
    except Exception as e:
        raise RuntimeError(f"LLM call failed: {e}") from e


def call_llm_json(system_prompt: str, user_prompt: str, max_tokens: int = 4096) -> dict | list:
    """
    Call Claude and parse the response as JSON.

    Appends an instruction to respond only with valid JSON.

    Args:
        system_prompt: The system-level instruction.
        user_prompt: The user message / task content.
        max_tokens: Maximum tokens in the response.

    Returns:
        Parsed JSON as a dict or list.

    Raises:
        RuntimeError: If the API call fails.
        json.JSONDecodeError: If the response isn't valid JSON.
    """
    enhanced_system = (
        system_prompt
        + "\n\nRespond ONLY with valid JSON. "
        "No markdown fences, no explanation outside the JSON."
    )
    raw = call_llm(enhanced_system, user_prompt, max_tokens)

    # Strip markdown code fences if the model wraps them anyway
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text[3:]
    if text.endswith("```"):
        text = text.rsplit("```", 1)[0]

    return json.loads(text.strip())
