"""
Configuration Management using Dataclasses.

OOP Concepts Demonstrated:
- Dataclasses: Structured configuration with defaults and type hints
- Class Methods: Factory pattern with from_env()
- Encapsulation: Configuration is bundled into cohesive objects
- Composition: PipelineConfig contains LLMConfig and RateLimitConfig
- Properties: Computed/derived configuration values
- Immutability: frozen=True prevents accidental mutation
"""

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the v2_oop directory
_env_path = Path(__file__).resolve().parent / ".env"
if not _env_path.exists():
    # Fall back to parent project .env
    _env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_env_path)


@dataclass(frozen=True)
class LLMConfig:
    """
    Configuration for the LLM client.

    frozen=True makes instances immutable — once created, values can't change.
    This prevents bugs from accidental config mutation at runtime.

    OOP Concept: Encapsulation — all LLM settings bundled together.
    """

    region: str = "eu-central-1"
    profile: str = ""
    model_id: str = "eu.anthropic.claude-sonnet-4-20250514"
    max_tokens: int = 4096
    read_timeout: int = 300
    connect_timeout: int = 10
    max_retries: int = 2

    @classmethod
    def from_env(cls) -> "LLMConfig":
        """
        Factory method: Create config from environment variables.

        OOP Concept: Class Method as a factory — alternative constructor
        that builds the object from a different source (env vars vs direct args).
        """
        return cls(
            region=os.getenv("AWS_REGION", "eu-central-1"),
            profile=os.getenv("AWS_PROFILE", ""),
            model_id=os.getenv("BEDROCK_MODEL_ID", "eu.anthropic.claude-sonnet-4-20250514"),
            max_tokens=int(os.getenv("LLM_MAX_TOKENS", "4096")),
            read_timeout=int(os.getenv("LLM_READ_TIMEOUT", "300")),
            connect_timeout=int(os.getenv("LLM_CONNECT_TIMEOUT", "10")),
            max_retries=int(os.getenv("LLM_MAX_RETRIES", "2")),
        )

    @property
    def is_using_profile(self) -> bool:
        """Whether a named AWS profile is configured."""
        return bool(self.profile)


@dataclass(frozen=True)
class RateLimitConfig:
    """
    Rate limiting configuration.

    OOP Concept: Single Responsibility — this class ONLY handles rate limit settings.
    """

    max_requests_per_minute: int = 30
    max_retries: int = 3
    base_delay: float = 2.0
    max_delay: float = 60.0
    exponential_base: float = 2.0

    @classmethod
    def from_env(cls) -> "RateLimitConfig":
        """Factory method to create from environment variables."""
        return cls(
            max_requests_per_minute=int(os.getenv("LLM_MAX_REQUESTS_PER_MINUTE", "30")),
            max_retries=int(os.getenv("LLM_MAX_RETRIES", "3")),
            base_delay=float(os.getenv("LLM_RETRY_BASE_DELAY", "2.0")),
            max_delay=float(os.getenv("LLM_RETRY_MAX_DELAY", "60.0")),
        )

    @property
    def min_interval(self) -> float:
        """Minimum seconds between requests to stay within rate limit."""
        return 60.0 / self.max_requests_per_minute


@dataclass(frozen=True)
class PipelineConfig:
    """
    Top-level pipeline configuration.

    OOP Concept: Composition — PipelineConfig is COMPOSED of LLMConfig
    and RateLimitConfig. It doesn't inherit from them; it contains them.
    This is "has-a" vs "is-a" relationship.
    """

    llm: LLMConfig = field(default_factory=LLMConfig.from_env)
    rate_limit: RateLimitConfig = field(default_factory=RateLimitConfig.from_env)
    max_revision_loops: int = 2
    critic_threshold: int = 8
    server_port: int = 8502

    @classmethod
    def from_env(cls) -> "PipelineConfig":
        """Factory method to create full config from environment."""
        return cls(
            llm=LLMConfig.from_env(),
            rate_limit=RateLimitConfig.from_env(),
            max_revision_loops=int(os.getenv("MAX_REVISION_LOOPS", "2")),
            critic_threshold=int(os.getenv("CRITIC_THRESHOLD", "8")),
            server_port=int(os.getenv("SERVER_PORT", "8502")),
        )

    def __repr__(self) -> str:
        """Custom repr for readable config display."""
        return (
            f"PipelineConfig(\n"
            f"  model={self.llm.model_id},\n"
            f"  region={self.llm.region},\n"
            f"  rate_limit={self.rate_limit.max_requests_per_minute} req/min,\n"
            f"  max_revisions={self.max_revision_loops},\n"
            f"  critic_threshold={self.critic_threshold}/10\n"
            f")"
        )
