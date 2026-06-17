"""
Custom Decorators for cross-cutting concerns.

OOP Concepts Demonstrated:
- Decorators: Functions that wrap other functions to add behavior
- Closures: Inner functions capturing outer scope variables
- Higher-order Functions: Functions that take/return functions
- Separation of Concerns: Retry logic, rate limiting, and logging
  are separate from business logic

These decorators can be applied to any method to add:
- Automatic retry with exponential backoff
- Rate limiting (requests per minute)
- Execution logging with timing
"""

import functools
import logging
import time
from collections import deque
from threading import Lock
from typing import Any, Callable, TypeVar

from exceptions import LLMError, RateLimitError

logger = logging.getLogger(__name__)

# Type variable for preserving function signatures
F = TypeVar("F", bound=Callable[..., Any])


def retry(
    max_retries: int = 3,
    base_delay: float = 2.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    retryable_exceptions: tuple = (LLMError, ConnectionError, TimeoutError),
) -> Callable[[F], F]:
    """
    Decorator: Retry a function with exponential backoff.

    OOP Concept: This is a DECORATOR FACTORY — a function that returns
    a decorator. The outer function accepts configuration, the middle
    function is the actual decorator, and the inner function is the wrapper.

    Three levels of nesting:
    1. retry(max_retries=3)     → returns the decorator
    2. @decorator               → wraps the function
    3. wrapper(*args, **kwargs) → executes with retry logic

    Args:
        max_retries: Maximum number of retry attempts.
        base_delay: Initial delay in seconds before first retry.
        max_delay: Maximum delay cap (prevents absurdly long waits).
        exponential_base: Multiplier for each subsequent delay.
        retryable_exceptions: Tuple of exception types that trigger a retry.

    Example:
        @retry(max_retries=3, base_delay=2.0)
        def call_api():
            ...
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)  # Preserves original function's name and docstring
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                    # Log if we succeeded after retries
                    if attempt > 0:
                        logger.info(
                            f"[RETRY] {func.__name__} succeeded on attempt {attempt + 1}"
                        )
                    return result

                except retryable_exceptions as e:
                    last_exception = e

                    if attempt == max_retries:
                        logger.error(
                            f"[RETRY] {func.__name__} failed after {max_retries + 1} attempts: {e}"
                        )
                        raise

                    # Calculate delay with exponential backoff
                    delay = min(
                        base_delay * (exponential_base ** attempt),
                        max_delay,
                    )

                    # If it's a RateLimitError with retry_after, use that instead
                    if isinstance(e, RateLimitError) and e.retry_after > 0:
                        delay = e.retry_after

                    logger.warning(
                        f"[RETRY] {func.__name__} attempt {attempt + 1}/{max_retries + 1} "
                        f"failed: {e}. Retrying in {delay:.1f}s..."
                    )
                    time.sleep(delay)

            # Should never reach here, but just in case
            raise last_exception  # type: ignore

        return wrapper  # type: ignore

    return decorator


def rate_limit(max_requests_per_minute: int = 30) -> Callable[[F], F]:
    """
    Decorator: Enforce a maximum request rate using a sliding window.

    OOP Concept: This uses a CLOSURE to maintain state (the request
    timestamps deque and lock) across multiple calls to the decorated
    function. The state persists for the lifetime of the decorated function.

    How it works:
    - Maintains a deque of timestamps for recent calls
    - Before each call, removes timestamps older than 60 seconds
    - If at capacity, sleeps until the oldest request expires
    - Thread-safe via Lock

    Args:
        max_requests_per_minute: Maximum allowed calls within a 60-second window.

    Example:
        @rate_limit(max_requests_per_minute=30)
        def call_api():
            ...
    """

    def decorator(func: F) -> F:
        # State maintained via closure — persists between calls
        request_times: deque = deque()
        lock = Lock()

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with lock:
                now = time.time()

                # Remove timestamps older than 60 seconds (sliding window)
                while request_times and request_times[0] < now - 60:
                    request_times.popleft()

                # If at capacity, wait until the oldest request expires
                if len(request_times) >= max_requests_per_minute:
                    wait_time = 60 - (now - request_times[0])
                    if wait_time > 0:
                        logger.info(
                            f"[RATE LIMIT] {func.__name__}: "
                            f"at {max_requests_per_minute} req/min capacity. "
                            f"Waiting {wait_time:.1f}s..."
                        )
                        time.sleep(wait_time)

                # Record this request
                request_times.append(time.time())

            # Execute the actual function (outside the lock)
            return func(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator


def log_execution(func: F) -> F:
    """
    Decorator: Log function entry, exit, and execution time.

    OOP Concept: This is a SIMPLE DECORATOR (no factory needed).
    It takes a function and returns a wrapped version that adds logging.

    Unlike retry() and rate_limit(), this doesn't need configuration,
    so it's applied directly: @log_execution (no parentheses).

    Example:
        @log_execution
        def process_data():
            ...
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_name = func.__qualname__  # Includes class name if it's a method
        logger.info(f"[START] {func_name}")
        start_time = time.time()

        try:
            result = func(*args, **kwargs)
            elapsed_ms = (time.time() - start_time) * 1000
            logger.info(f"[DONE]  {func_name} completed in {elapsed_ms:.0f}ms")
            return result

        except Exception as e:
            elapsed_ms = (time.time() - start_time) * 1000
            logger.error(f"[FAIL]  {func_name} failed after {elapsed_ms:.0f}ms: {e}")
            raise

    return wrapper  # type: ignore


def validate_input(**validators: Callable) -> Callable[[F], F]:
    """
    Decorator Factory: Validate function arguments before execution.

    OOP Concept: Decorator with keyword arguments that map parameter
    names to validation functions.

    Args:
        **validators: Keyword args where key = param name,
                      value = validation function that raises on failure.

    Example:
        @validate_input(
            resume_text=lambda x: x.strip() if x else raise ValueError("empty"),
            jd_text=lambda x: x.strip() if x else raise ValueError("empty"),
        )
        def process(resume_text: str, jd_text: str):
            ...
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            import inspect

            # Get the function's parameter names
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            # Run validators on matching parameters
            for param_name, validator_fn in validators.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    try:
                        validator_fn(value)
                    except (ValueError, TypeError) as e:
                        from exceptions import InputValidationError

                        raise InputValidationError(param_name, str(e)) from e

            return func(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator
