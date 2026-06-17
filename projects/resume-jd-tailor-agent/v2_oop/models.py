"""
Data Models using Pydantic and Dataclasses.

OOP Concepts Demonstrated:
- Dataclasses: Lightweight structured data with auto-generated methods
- Pydantic Models: Validation + serialization for API boundaries
- Magic Methods: __str__, __repr__, __len__, __bool__
- Properties: Computed attributes derived from stored data
- Class Methods: Alternative constructors (from_dict, from_llm_response)
- Composition: Models contain other models (AgentResult contains data models)
- Type Hints: Full typing for IDE support and documentation
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator


# ── Enums ────────────────────────────────────────────────────────────────────


class SeniorityLevel(str, Enum):
    """
    Enum for seniority levels.

    OOP Concept: Enums restrict values to a known set,
    preventing invalid data from entering the system.
    """

    ENTRY = "Entry Level"
    MID = "Mid Level"
    SENIOR = "Senior"
    LEAD = "Lead"
    PRINCIPAL = "Principal"
    UNKNOWN = "Unknown"

    @classmethod
    def from_string(cls, value: str) -> "SeniorityLevel":
        """Fuzzy match a string to a seniority level."""
        value_lower = value.lower().strip()
        for member in cls:
            if member.value.lower() in value_lower or value_lower in member.value.lower():
                return member
        return cls.UNKNOWN


class PipelineStep(int, Enum):
    """Pipeline step identifiers."""

    JD_EXTRACTION = 0
    RESUME_MATCHING = 1
    BULLET_REWRITING = 2
    COVER_LETTER = 3
    CRITIC_REVIEW = 4
    REVISION = 5
    INTERVIEW_QUESTIONS = 6


# ── Pydantic Models (for validated, serializable data) ───────────────────────


class JDAnalysis(BaseModel):
    """
    Structured output from JD extraction.

    OOP Concept: Pydantic models provide automatic validation.
    If you try to create a JDAnalysis with invalid data, it raises an error.
    """

    top_keywords: list[str] = Field(default_factory=list, max_length=10)
    must_have_skills: list[str] = Field(default_factory=list)
    nice_to_have_skills: list[str] = Field(default_factory=list)
    tools_technologies: list[str] = Field(default_factory=list)
    responsibilities: list[str] = Field(default_factory=list, max_length=8)
    seniority_level: str = "Unknown"

    @field_validator("seniority_level", mode="before")
    @classmethod
    def normalize_seniority(cls, v: str) -> str:
        """Normalize seniority level string."""
        return SeniorityLevel.from_string(v).value

    @property
    def total_skills_count(self) -> int:
        """Total number of skills identified."""
        return len(self.must_have_skills) + len(self.nice_to_have_skills)

    def __len__(self) -> int:
        """Number of keywords extracted."""
        return len(self.top_keywords)


class MatchAnalysis(BaseModel):
    """Resume-to-JD match analysis result."""

    match_score: int = Field(default=0, ge=0, le=100)
    matched_skills: list[str] = Field(default_factory=list)
    missing_skills: list[str] = Field(default_factory=list)
    weak_skills: list[str] = Field(default_factory=list)
    sections_to_improve: list[str] = Field(default_factory=list)
    score_explanation: str = ""

    @field_validator("match_score", mode="before")
    @classmethod
    def clamp_score(cls, v: Any) -> int:
        """Ensure score is within 0-100 range."""
        return max(0, min(100, int(v)))

    @property
    def is_strong_match(self) -> bool:
        """Whether the match score indicates a strong fit."""
        return self.match_score >= 70

    @property
    def gap_count(self) -> int:
        """Number of missing + weak skills."""
        return len(self.missing_skills) + len(self.weak_skills)

    def __bool__(self) -> bool:
        """A match analysis is 'truthy' if score > 0."""
        return self.match_score > 0


class RewrittenBullet(BaseModel):
    """A single rewritten resume bullet."""

    original: str
    rewritten: str
    changes_made: str = ""

    def __str__(self) -> str:
        """Display the rewritten version."""
        return self.rewritten

    @property
    def was_changed(self) -> bool:
        """Whether the bullet was actually modified."""
        return self.original.strip() != self.rewritten.strip()


class CriticResult(BaseModel):
    """Critic agent evaluation result."""

    score: int = Field(default=5, ge=1, le=10)
    issues: list[str] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)

    @field_validator("score", mode="before")
    @classmethod
    def clamp_score(cls, v: Any) -> int:
        """Clamp score to 1-10 range."""
        return max(1, min(10, int(v)))

    @property
    def passes_threshold(self) -> bool:
        """Whether the score meets the default threshold (8/10)."""
        return self.score >= 8

    @property
    def needs_revision(self) -> bool:
        """Whether revision is recommended."""
        return not self.passes_threshold

    def __bool__(self) -> bool:
        """Truthy if passes threshold."""
        return self.passes_threshold


class InterviewQuestion(BaseModel):
    """A generated interview question with context."""

    question: str
    why_asked: str = ""
    preparation_hint: str = ""

    def __str__(self) -> str:
        return self.question


# ── Dataclass for internal pipeline state ────────────────────────────────────


@dataclass
class AgentResult:
    """
    Container for an agent's execution result.

    OOP Concept: Dataclass auto-generates __init__, __repr__, __eq__.
    We add custom magic methods for richer behavior.

    This wraps the actual data with metadata about the execution.
    """

    agent_name: str
    step: PipelineStep
    data: Any
    success: bool = True
    error: str = ""
    execution_time_ms: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    retries_used: int = 0

    def __str__(self) -> str:
        """Human-readable summary."""
        status = "✓" if self.success else "✗"
        return (
            f"{status} [{self.agent_name}] "
            f"Step {self.step.value}: "
            f"{'OK' if self.success else self.error} "
            f"({self.execution_time_ms:.0f}ms)"
        )

    def __bool__(self) -> bool:
        """Result is truthy if successful."""
        return self.success

    def __repr__(self) -> str:
        return (
            f"AgentResult(agent={self.agent_name!r}, "
            f"step={self.step.name}, "
            f"success={self.success}, "
            f"time={self.execution_time_ms:.0f}ms)"
        )

    @property
    def failed(self) -> bool:
        """Inverse of success for readability."""
        return not self.success

    @classmethod
    def failure(cls, agent_name: str, step: PipelineStep, error: str) -> "AgentResult":
        """
        Factory method to create a failed result.

        OOP Concept: Class method as alternative constructor.
        Instead of AgentResult(success=False, error=...), we have
        a semantic factory: AgentResult.failure(...)
        """
        return cls(
            agent_name=agent_name,
            step=step,
            data=None,
            success=False,
            error=error,
        )


@dataclass
class PipelineState:
    """
    Tracks the full state of a pipeline execution.

    OOP Concept: Encapsulation — all pipeline state in one place.
    External code interacts through methods, not direct attribute access.
    """

    results: list[AgentResult] = field(default_factory=list)
    current_step: PipelineStep = PipelineStep.JD_EXTRACTION
    revision_count: int = 0
    is_complete: bool = False

    def add_result(self, result: AgentResult) -> None:
        """Add a step result to the pipeline state."""
        self.results.append(result)

    @property
    def total_execution_time_ms(self) -> float:
        """Total time across all steps."""
        return sum(r.execution_time_ms for r in self.results)

    @property
    def has_errors(self) -> bool:
        """Whether any step failed."""
        return any(r.failed for r in self.results)

    @property
    def completed_steps(self) -> int:
        """Number of successfully completed steps."""
        return sum(1 for r in self.results if r.success)

    def __len__(self) -> int:
        """Number of results recorded."""
        return len(self.results)

    def __iter__(self):
        """Iterate over results."""
        return iter(self.results)
