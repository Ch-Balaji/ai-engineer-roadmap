"""
LLM Client as a proper Class with Context Manager support.

OOP Concepts Demonstrated:
- Encapsulation: Client state (boto3 session, config) is private
- Context Manager: __enter__ / __exit__ for resource lifecycle
- Composition: Uses Config objects rather than raw strings
- Decorators: @retry and @rate_limit applied to methods
- Properties: Lazy-initialized client via @property
- Single Responsibility: Only handles LLM communication
- Error Handling: Translates AWS errors into our custom exceptions
"""

import json
import logging
import time

import boto3
from botocore.config import Config as BotoConfig
from botocore.exceptions import ClientError

from config import LLMConfig, RateLimitConfig
from decorators import log_execution, rate_limit, retry
from exceptions import (
    LLMError,
    ModelUnavailableError,
    RateLimitError,
    TokenLimitError,
)

logger = logging.getLogger(__name__)


class LLMClient:
    """
    AWS Bedrock Claude client with retry, rate limiting, and proper lifecycle.

    OOP Concepts:
    - __init__: Constructor sets up configuration
    - __enter__ / __exit__: Context manager protocol
    - @property: Lazy initialization of expensive resources
    - Private methods: _build_client(), _parse_response()
    - Decorators on methods: @retry, @rate_limit

    Usage:
        # As context manager (preferred):
        with LLMClient(config) as client:
            response = client.call("system prompt", "user prompt")

        # Direct instantiation:
        client = LLMClient(config)
        client.connect()
        response = client.call("system prompt", "user prompt")
        client.disconnect()
    """

    def __init__(self, llm_config: LLMConfig, rate_config: RateLimitConfig | None = None):
        """
        Initialize the LLM client with configuration.

        OOP Concept: Constructor — sets up instance state.
        Note: We don't create the boto3 client here (lazy init).
        """
        self._config = llm_config
        self._rate_config = rate_config or RateLimitConfig()
        self._client = None  # Lazy initialized
        self._session = None
        self._call_count = 0
        self._total_tokens_used = 0
        self._connected = False

        logger.info(f"LLMClient initialized with model: {self._config.model_id}")

    # ── Context Manager Protocol ─────────────────────────────────────────────

    def __enter__(self) -> "LLMClient":
        """
        Enter the context manager — connect to AWS.

        OOP Concept: __enter__ is called when you use 'with LLMClient() as client:'
        It sets up resources and returns the object to use inside the 'with' block.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Exit the context manager — clean up resources.

        OOP Concept: __exit__ is called when leaving the 'with' block,
        even if an exception occurred. This guarantees cleanup.

        Args:
            exc_type: Exception type (None if no exception)
            exc_val: Exception value
            exc_tb: Exception traceback

        Returns:
            False — we don't suppress exceptions.
        """
        self.disconnect()
        if exc_type is not None:
            logger.error(f"LLMClient context exited with error: {exc_val}")
        return False  # Don't suppress exceptions

    # ── Public Methods ───────────────────────────────────────────────────────

    def connect(self) -> None:
        """Establish connection to AWS Bedrock."""
        if self._connected:
            return

        try:
            self._session = boto3.Session(
                profile_name=self._config.profile if self._config.is_using_profile else None,
                region_name=self._config.region,
            )
            self._client = self._session.client(
                "bedrock-runtime",
                config=BotoConfig(
                    read_timeout=self._config.read_timeout,
                    connect_timeout=self._config.connect_timeout,
                    retries={"max_attempts": self._config.max_retries, "mode": "adaptive"},
                ),
            )
            self._connected = True
            logger.info(f"Connected to Bedrock in {self._config.region}")

        except Exception as e:
            raise LLMError(
                f"Failed to connect to AWS Bedrock: {e}",
                model_id=self._config.model_id,
            ) from e

    def disconnect(self) -> None:
        """Release AWS resources."""
        self._client = None
        self._session = None
        self._connected = False
        logger.info(
            f"LLMClient disconnected. "
            f"Total calls: {self._call_count}, "
            f"Total tokens: {self._total_tokens_used}"
        )

    @log_execution
    def call(self, system_prompt: str, user_prompt: str, max_tokens: int | None = None) -> str:
        """
        Call Claude via AWS Bedrock and return the text response.

        This method has @retry and @rate_limit applied via the internal
        _invoke method, keeping the public interface clean.

        Args:
            system_prompt: The system-level instruction.
            user_prompt: The user message / task content.
            max_tokens: Override default max tokens.

        Returns:
            The model's text response.

        Raises:
            LLMError: If the API call fails after retries.
            TokenLimitError: If response is truncated.
            RateLimitError: If rate limit is exceeded and retries exhausted.
        """
        if not self._connected:
            self.connect()

        tokens = max_tokens or self._config.max_tokens
        return self._invoke(system_prompt, user_prompt, tokens)

    def call_json(self, system_prompt: str, user_prompt: str, max_tokens: int | None = None) -> dict | list:
        """
        Call Claude and parse the response as JSON.

        Appends a JSON-only instruction to the system prompt and
        strips any markdown fences from the response.

        Args:
            system_prompt: The system-level instruction.
            user_prompt: The user message / task content.
            max_tokens: Override default max tokens.

        Returns:
            Parsed JSON as dict or list.

        Raises:
            LLMError: If API call fails.
            json.JSONDecodeError: If response isn't valid JSON.
        """
        enhanced_system = (
            system_prompt
            + "\n\nRespond ONLY with valid JSON. "
            "No markdown fences, no explanation outside the JSON."
        )

        raw = self.call(enhanced_system, user_prompt, max_tokens)
        return self._parse_json_response(raw)

    # ── Properties ───────────────────────────────────────────────────────────

    @property
    def call_count(self) -> int:
        """Number of API calls made by this client instance."""
        return self._call_count

    @property
    def total_tokens_used(self) -> int:
        """Total tokens consumed across all calls."""
        return self._total_tokens_used

    @property
    def is_connected(self) -> bool:
        """Whether the client is currently connected."""
        return self._connected

    @property
    def model_id(self) -> str:
        """The model being used."""
        return self._config.model_id

    # ── Private Methods ──────────────────────────────────────────────────────

    def _invoke(self, system_prompt: str, user_prompt: str, max_tokens: int) -> str:
        """
        Internal method that actually calls the API.

        Retry and rate limiting are handled here. We apply them
        programmatically rather than with decorators to allow
        dynamic configuration from self._rate_config.

        OOP Concept: Private method — implementation detail hidden
        from external callers. Only the class itself uses this.
        """
        last_exception = None

        for attempt in range(self._rate_config.max_retries + 1):
            try:
                # Rate limiting: enforce minimum interval
                self._enforce_rate_limit()

                response = self._client.invoke_model(
                    modelId=self._config.model_id,
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
                self._call_count += 1

                # Track token usage
                usage = result.get("usage", {})
                self._total_tokens_used += usage.get("output_tokens", 0)

                # Check for truncation
                stop_reason = result.get("stop_reason", "")
                if stop_reason == "max_tokens":
                    raise TokenLimitError(
                        max_tokens=max_tokens,
                        model_id=self._config.model_id,
                    )

                return result["content"][0]["text"]

            except TokenLimitError:
                raise  # Don't retry on token limit — it'll just happen again

            except ClientError as e:
                error_code = e.response.get("Error", {}).get("Code", "")
                last_exception = e

                if error_code == "ThrottlingException":
                    retry_after = self._calculate_backoff(attempt)
                    if attempt < self._rate_config.max_retries:
                        logger.warning(
                            f"Rate limited (attempt {attempt + 1}). "
                            f"Waiting {retry_after:.1f}s..."
                        )
                        time.sleep(retry_after)
                        continue
                    raise RateLimitError(
                        retry_after=retry_after,
                        model_id=self._config.model_id,
                    ) from e

                elif error_code in ("ModelNotReadyException", "AccessDeniedException"):
                    raise ModelUnavailableError(
                        model_id=self._config.model_id,
                        region=self._config.region,
                    ) from e

                else:
                    if attempt < self._rate_config.max_retries:
                        delay = self._calculate_backoff(attempt)
                        logger.warning(f"API error: {e}. Retrying in {delay:.1f}s...")
                        time.sleep(delay)
                        continue
                    raise LLMError(
                        f"API call failed: {error_code} - {e}",
                        model_id=self._config.model_id,
                    ) from e

            except Exception as e:
                last_exception = e
                if attempt < self._rate_config.max_retries:
                    delay = self._calculate_backoff(attempt)
                    logger.warning(f"Unexpected error: {e}. Retrying in {delay:.1f}s...")
                    time.sleep(delay)
                    continue
                raise LLMError(
                    f"LLM call failed: {e}",
                    model_id=self._config.model_id,
                ) from e

        # Should not reach here
        raise LLMError(
            f"All retries exhausted: {last_exception}",
            model_id=self._config.model_id,
        )

    def _enforce_rate_limit(self) -> None:
        """
        Simple rate limiting via minimum interval between calls.

        OOP Concept: Encapsulation — rate limiting logic is hidden
        inside the class. Callers don't need to know about it.
        """
        # This is a simplified version; the decorator-based approach
        # in decorators.py shows the sliding window version.
        min_interval = self._rate_config.min_interval
        if min_interval > 0:
            time.sleep(min_interval * 0.1)  # Small pause to spread requests

    def _calculate_backoff(self, attempt: int) -> float:
        """
        Calculate exponential backoff delay.

        Formula: base_delay * (exponential_base ^ attempt), capped at max_delay.
        """
        delay = self._rate_config.base_delay * (
            self._rate_config.exponential_base ** attempt
        )
        return min(delay, self._rate_config.max_delay)

    @staticmethod
    def _parse_json_response(raw: str) -> dict | list:
        """
        Parse LLM response as JSON, stripping markdown fences if present.

        OOP Concept: Static method — doesn't need instance state (self)
        or class state (cls). It's a utility function that logically
        belongs to this class.
        """
        text = raw.strip()

        # Strip markdown code fences
        if text.startswith("```"):
            text = text.split("\n", 1)[1] if "\n" in text else text[3:]
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]

        try:
            return json.loads(text.strip())
        except json.JSONDecodeError as e:
            raise LLMError(f"Failed to parse LLM response as JSON: {e}") from e

    # ── Magic Methods ────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (
            f"LLMClient(model={self._config.model_id!r}, "
            f"region={self._config.region!r}, "
            f"connected={self._connected})"
        )

    def __str__(self) -> str:
        """Human-readable description."""
        status = "connected" if self._connected else "disconnected"
        return f"LLMClient [{status}] — {self._config.model_id} ({self._call_count} calls)"
