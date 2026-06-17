"""
Abstract Base Agent class.

OOP Concepts Demonstrated:
- Abstract Base Class (ABC): Defines interface that all agents MUST implement
- @abstractmethod: Forces subclasses to provide their own implementation
- Template Method Pattern: execute() defines the algorithm skeleton,
  subclasses fill in the specific steps
- Inheritance: All agents inherit common behavior from BaseAgent
- Encapsulation: Shared logic (validation, timing, error handling) in base class
- Properties: Common computed attributes available to all agents
- Magic Methods: __repr__, __str__ for all agents
"""

from abc import ABC, abstractmethod
import logging
import time
from typing import Any

from llm_client import LLMClient
from models import AgentResult, PipelineStep
from exceptions import AgentError, InputValidationError, StepFailedError

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Abstract base class for all pipeline agents.

    OOP Concepts:
    - ABC (Abstract Base Class): Cannot be instantiated directly.
      You MUST create a subclass that implements all @abstractmethod methods.
    - Template Method Pattern: execute() is the template that calls
      abstract methods (_validate_input, _process, _format_output) in order.
    - Inheritance: Subclasses get all the shared behavior for free.

    Why use ABC?
    - Enforces a contract: every agent MUST have execute(), _process(), etc.
    - Provides shared infrastructure: timing, logging, error handling
    - Enables polymorphism: you can treat any agent as a BaseAgent

    Usage:
        class MyAgent(BaseAgent):
            @property
            def name(self) -> str:
                return "My Agent"

            @property
            def step(self) -> PipelineStep:
                return PipelineStep.JD_EXTRACTION

            def _validate_input(self, **kwargs) -> None:
                ...

            def _process(self, **kwargs) -> Any:
                ...

            def _format_output(self, raw_result: Any) -> Any:
                ...
    """

    def __init__(self, llm_client: LLMClient):
        """
        Initialize the agent with an LLM client.

        OOP Concept: Constructor — all agents need an LLM client,
        so we accept it in the base class constructor.
        Subclasses call super().__init__(llm_client) to inherit this.
        """
        self._llm_client = llm_client
        self._execution_count = 0
        self._total_time_ms = 0.0

    # ── Abstract Properties (MUST be implemented by subclasses) ──────────────

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable name of this agent.

        OOP Concept: Abstract property — subclasses MUST define this.
        Trying to instantiate a class without implementing this raises TypeError.
        """
        ...

    @property
    @abstractmethod
    def step(self) -> PipelineStep:
        """Which pipeline step this agent handles."""
        ...

    # ── Abstract Methods (MUST be implemented by subclasses) ─────────────────

    @abstractmethod
    def _validate_input(self, **kwargs) -> None:
        """
        Validate input data before processing.

        OOP Concept: Abstract method — each agent defines its own
        validation rules. JDExtractor needs jd_text, ResumeMatcher
        needs both resume_text and jd_text, etc.

        Raises:
            InputValidationError: If input is invalid.
        """
        ...

    @abstractmethod
    def _process(self, **kwargs) -> Any:
        """
        Core processing logic — the actual LLM call and data extraction.

        This is where each agent does its unique work.
        """
        ...

    @abstractmethod
    def _format_output(self, raw_result: Any) -> Any:
        """
        Format/validate the raw LLM output into the expected structure.

        Ensures the output matches our data models.
        """
        ...

    # ── Template Method (the algorithm skeleton) ─────────────────────────────

    def execute(self, **kwargs) -> AgentResult:
        """
        Execute the agent pipeline: validate → process → format.

        OOP Concept: TEMPLATE METHOD PATTERN
        This method defines the SKELETON of the algorithm:
            1. Validate input
            2. Process (call LLM)
            3. Format output
            4. Wrap in AgentResult

        Subclasses don't override execute() — they override the
        individual steps (_validate_input, _process, _format_output).
        This ensures consistent behavior (timing, error handling, logging)
        across ALL agents.

        Returns:
            AgentResult with the processed data or error information.
        """
        start_time = time.time()
        logger.info(f"[{self.name}] Starting execution...")

        try:
            # Step 1: Validate input
            self._validate_input(**kwargs)

            # Step 2: Process (call LLM)
            raw_result = self._process(**kwargs)

            # Step 3: Format output
            formatted = self._format_output(raw_result)

            # Calculate timing
            elapsed_ms = (time.time() - start_time) * 1000
            self._execution_count += 1
            self._total_time_ms += elapsed_ms

            logger.info(f"[{self.name}] Completed in {elapsed_ms:.0f}ms")

            return AgentResult(
                agent_name=self.name,
                step=self.step,
                data=formatted,
                success=True,
                execution_time_ms=elapsed_ms,
            )

        except InputValidationError as e:
            elapsed_ms = (time.time() - start_time) * 1000
            logger.warning(f"[{self.name}] Validation failed: {e}")
            return AgentResult.failure(self.name, self.step, str(e))

        except AgentError as e:
            elapsed_ms = (time.time() - start_time) * 1000
            logger.error(f"[{self.name}] Agent error: {e}")
            raise StepFailedError(
                step=self.step.value,
                step_name=self.name,
                original_error=e,
            ) from e

        except Exception as e:
            elapsed_ms = (time.time() - start_time) * 1000
            logger.error(f"[{self.name}] Unexpected error: {e}")
            raise StepFailedError(
                step=self.step.value,
                step_name=self.name,
                original_error=e,
            ) from e

    # ── Shared Helper Methods ────────────────────────────────────────────────

    def _require_non_empty(self, value: str, field_name: str) -> None:
        """
        Helper: Validate that a string field is not empty.

        OOP Concept: Code reuse via inheritance — all subclasses
        can use this helper without reimplementing it.
        """
        if not value or not value.strip():
            raise InputValidationError(field_name, "cannot be empty")

    def _require_non_empty_list(self, value: list, field_name: str) -> None:
        """Helper: Validate that a list is not empty."""
        if not value:
            raise InputValidationError(field_name, "cannot be empty")

    # ── Properties ───────────────────────────────────────────────────────────

    @property
    def execution_count(self) -> int:
        """How many times this agent has been executed."""
        return self._execution_count

    @property
    def average_time_ms(self) -> float:
        """Average execution time in milliseconds."""
        if self._execution_count == 0:
            return 0.0
        return self._total_time_ms / self._execution_count

    # ── Magic Methods ────────────────────────────────────────────────────────

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(step={self.step.name}, executions={self._execution_count})"

    def __str__(self) -> str:
        return f"{self.name} (Step {self.step.value})"
