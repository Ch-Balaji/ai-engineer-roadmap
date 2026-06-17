"""
Custom Exception Hierarchy for the Resume JD Tailor Agent.

OOP Concepts Demonstrated:
- Inheritance: All exceptions inherit from a base AgentError
- Encapsulation: Each exception carries relevant context data
- Polymorphism: Different exceptions can be caught at different levels
- Magic Methods: __str__ and __repr__ for readable error messages

Exception Hierarchy:
    AgentError (base)
    ├── LLMError
    │   ├── RateLimitError
    │   ├── TokenLimitError
    │   └── ModelUnavailableError
    ├── ValidationError
    │   ├── InputValidationError
    │   └── OutputValidationError
    ├── PipelineError
    │   ├── StepFailedError
    │   └── MaxRevisionsExceededError
    └── ConfigurationError
"""


class AgentError(Exception):
    """
    Base exception for all agent-related errors.

    All custom exceptions in this project inherit from this class,
    allowing you to catch all agent errors with a single except clause.

    OOP Concept: This is the ROOT of our exception hierarchy.
    """

    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        """Human-readable error message."""
        if self.details:
            detail_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{self.message} [{detail_str}]"
        return self.message

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"{self.__class__.__name__}(message={self.message!r}, details={self.details!r})"


# ── LLM Errors ───────────────────────────────────────────────────────────────


class LLMError(AgentError):
    """Base class for all LLM-related errors."""

    def __init__(self, message: str, model_id: str = "", **kwargs):
        super().__init__(message, details={"model_id": model_id, **kwargs})
        self.model_id = model_id


class RateLimitError(LLMError):
    """
    Raised when the LLM API rate limit is exceeded.

    Carries retry_after information so the caller knows how long to wait.
    """

    def __init__(self, message: str = "Rate limit exceeded", retry_after: float = 0, **kwargs):
        super().__init__(message, **kwargs)
        self.retry_after = retry_after
        self.details["retry_after_seconds"] = retry_after


class TokenLimitError(LLMError):
    """Raised when the response is truncated due to max_tokens."""

    def __init__(self, max_tokens: int, **kwargs):
        message = f"Response truncated at {max_tokens} tokens"
        super().__init__(message, **kwargs)
        self.max_tokens = max_tokens
        self.details["max_tokens"] = max_tokens


class ModelUnavailableError(LLMError):
    """Raised when the specified model is not available or accessible."""

    def __init__(self, model_id: str, region: str = "", **kwargs):
        message = f"Model '{model_id}' is not available in region '{region}'"
        super().__init__(message, model_id=model_id, **kwargs)
        self.details["region"] = region


# ── Validation Errors ────────────────────────────────────────────────────────


class ValidationError(AgentError):
    """Base class for input/output validation errors."""

    def __init__(self, message: str, field: str = "", **kwargs):
        super().__init__(message, details={"field": field, **kwargs})
        self.field = field


class InputValidationError(ValidationError):
    """Raised when input data fails validation (e.g., empty resume)."""

    def __init__(self, field: str, reason: str):
        message = f"Invalid input for '{field}': {reason}"
        super().__init__(message, field=field, reason=reason)
        self.reason = reason


class OutputValidationError(ValidationError):
    """Raised when LLM output doesn't match expected schema."""

    def __init__(self, field: str, expected_type: str, got: str):
        message = f"Output validation failed for '{field}': expected {expected_type}, got {got}"
        super().__init__(message, field=field, expected_type=expected_type, got=got)


# ── Pipeline Errors ──────────────────────────────────────────────────────────


class PipelineError(AgentError):
    """Base class for pipeline orchestration errors."""

    def __init__(self, message: str, step: int = -1, **kwargs):
        super().__init__(message, details={"step": step, **kwargs})
        self.step = step


class StepFailedError(PipelineError):
    """Raised when a specific pipeline step fails."""

    def __init__(self, step: int, step_name: str, original_error: Exception):
        message = f"Pipeline step {step} ({step_name}) failed: {original_error}"
        super().__init__(message, step=step, step_name=step_name)
        self.step_name = step_name
        self.original_error = original_error


class MaxRevisionsExceededError(PipelineError):
    """Raised when the revision loop exceeds the maximum allowed iterations."""

    def __init__(self, max_revisions: int, final_score: int):
        message = (
            f"Max revisions ({max_revisions}) exceeded. "
            f"Final critic score: {final_score}/10"
        )
        super().__init__(message, step=5, max_revisions=max_revisions, final_score=final_score)
        self.max_revisions = max_revisions
        self.final_score = final_score


# ── Configuration Errors ─────────────────────────────────────────────────────


class ConfigurationError(AgentError):
    """Raised when configuration is missing or invalid."""

    def __init__(self, param: str, reason: str = "missing or invalid"):
        message = f"Configuration error: '{param}' is {reason}"
        super().__init__(message, details={"param": param, "reason": reason})
        self.param = param
