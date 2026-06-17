"""
JD Extractor Agent — Analyzes job descriptions.

OOP Concepts Demonstrated:
- Inheritance: Extends BaseAgent, inherits execute() template method
- Method Override: Implements all abstract methods from BaseAgent
- Composition: Uses LLMClient and PromptTemplate objects
- Encapsulation: JD-specific logic contained in this class
- Type Safety: Returns typed JDAnalysis model
"""

from typing import Any

from agents.base import BaseAgent
from models import JDAnalysis, PipelineStep
from prompts import JD_EXTRACTOR_SYSTEM, JD_EXTRACTOR_USER


class JDExtractorAgent(BaseAgent):
    """
    Extracts structured information from a job description.

    Inherits from BaseAgent and implements the three abstract methods:
    - _validate_input: Ensures jd_text is provided
    - _process: Calls LLM with JD extraction prompts
    - _format_output: Parses into JDAnalysis model

    OOP Concept: This is a CONCRETE class — it implements all abstract
    methods, so it CAN be instantiated (unlike BaseAgent itself).
    """

    # ── Abstract Property Implementations ────────────────────────────────────

    @property
    def name(self) -> str:
        """Human-readable agent name."""
        return "JD Extractor"

    @property
    def step(self) -> PipelineStep:
        """Pipeline step this agent handles."""
        return PipelineStep.JD_EXTRACTION

    # ── Abstract Method Implementations ──────────────────────────────────────

    def _validate_input(self, **kwargs) -> None:
        """
        Validate that jd_text is provided and non-empty.

        OOP Concept: Each agent defines its OWN validation rules.
        The base class calls this method, but doesn't know what
        specific validation each agent needs — that's polymorphism.
        """
        jd_text = kwargs.get("jd_text", "")
        self._require_non_empty(jd_text, "jd_text")

    def _process(self, **kwargs) -> dict:
        """
        Call the LLM to extract JD information.

        OOP Concept: This is where the agent's unique logic lives.
        The base class handles timing, error wrapping, and result creation.
        """
        jd_text = kwargs["jd_text"]
        target_role = kwargs.get("target_role", "")

        # Format the prompt using our PromptTemplate objects
        role_context = f"Target Role: {target_role}" if target_role else ""

        user_prompt = JD_EXTRACTOR_USER(
            jd_text=jd_text,
            role_context=role_context,
        )

        # Call LLM and get JSON response
        result = self._llm_client.call_json(
            system_prompt=str(JD_EXTRACTOR_SYSTEM),
            user_prompt=user_prompt,
        )

        return result

    def _format_output(self, raw_result: Any) -> JDAnalysis:
        """
        Parse raw LLM output into a validated JDAnalysis model.

        OOP Concept: The Pydantic model handles validation automatically.
        If the LLM returns invalid data, Pydantic raises a clear error.
        """
        try:
            return JDAnalysis(**raw_result)
        except Exception:
            # If parsing fails, create with defaults for missing fields
            defaults = {
                "top_keywords": [],
                "must_have_skills": [],
                "nice_to_have_skills": [],
                "tools_technologies": [],
                "responsibilities": [],
                "seniority_level": "Unknown",
            }
            merged = {**defaults, **raw_result}
            return JDAnalysis(**merged)
