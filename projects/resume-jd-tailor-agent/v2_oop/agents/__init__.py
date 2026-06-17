"""
Agent classes for the Resume JD Tailor pipeline.

All agents inherit from BaseAgent and implement the execute() method.
"""

from agents.base import BaseAgent
from agents.jd_extractor import JDExtractorAgent
from agents.resume_matcher import ResumeMatcherAgent
from agents.resume_rewriter import ResumeRewriterAgent
from agents.cover_letter import CoverLetterAgent
from agents.critic import CriticAgent
from agents.interview import InterviewAgent

__all__ = [
    "BaseAgent",
    "JDExtractorAgent",
    "ResumeMatcherAgent",
    "ResumeRewriterAgent",
    "CoverLetterAgent",
    "CriticAgent",
    "InterviewAgent",
]
