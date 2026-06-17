"""
Prompt Templates as a Class with validation and formatting.

OOP Concepts Demonstrated:
- Encapsulation: Template text + metadata bundled together
- Inheritance: PromptTemplate base, specialized subclasses
- Magic Methods: __str__, __repr__, __format__, __call__
- Properties: Computed attributes (variable_names, word_count)
- Class Methods: Factory for creating common prompt types
- Operator Overloading: + to combine system + user prompts
- Validation: Ensures all required variables are provided
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class PromptTemplate:
    """
    A reusable prompt template with variable substitution and validation.

    OOP Concepts:
    - Encapsulation: Template + metadata in one object
    - __call__: Makes instances callable like functions
    - __add__: Operator overloading for combining prompts
    - __str__: Human-readable display
    - Properties: Derived data computed on access

    Usage:
        template = PromptTemplate(
            name="jd_extractor",
            template="Analyze this JD: {jd_text}",
            role="system",
        )
        # Call it like a function to format:
        formatted = template(jd_text="Software Engineer at Google...")
    """

    name: str
    template: str
    role: str = "user"  # "system" or "user"
    description: str = ""
    version: str = "1.0"
    _variable_pattern: re.Pattern = field(
        default_factory=lambda: re.compile(r"\{(\w+)\}"),
        repr=False,
    )

    # ── Properties ───────────────────────────────────────────────────────────

    @property
    def variable_names(self) -> list[str]:
        """
        Extract all variable names from the template.

        OOP Concept: Property — computed on access, not stored.
        Stays in sync with the template automatically.
        """
        return list(set(self._variable_pattern.findall(self.template)))

    @property
    def word_count(self) -> int:
        """Approximate word count of the template."""
        return len(self.template.split())

    @property
    def is_system_prompt(self) -> bool:
        """Whether this is a system-level prompt."""
        return self.role == "system"

    # ── Magic Methods ────────────────────────────────────────────────────────

    def __call__(self, **kwargs) -> str:
        """
        Make the template callable — format with provided variables.

        OOP Concept: __call__ lets you use an object like a function.
        template(jd_text="...") is equivalent to template.format(jd_text="...")

        Raises:
            ValueError: If required variables are missing.
        """
        self._validate_variables(kwargs)
        return self.template.format(**kwargs)

    def __str__(self) -> str:
        """Human-readable: show the template text."""
        return self.template

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (
            f"PromptTemplate(name={self.name!r}, "
            f"role={self.role!r}, "
            f"vars={self.variable_names})"
        )

    def __add__(self, other: "PromptTemplate") -> "PromptPair":
        """
        Combine two templates with + operator.

        OOP Concept: Operator overloading — redefining what + means
        for our custom class. system_prompt + user_prompt = PromptPair.

        Example:
            pair = system_template + user_template
        """
        if not isinstance(other, PromptTemplate):
            return NotImplemented
        return PromptPair(system=self, user=other)

    def __len__(self) -> int:
        """Length = number of characters in template."""
        return len(self.template)

    # ── Public Methods ───────────────────────────────────────────────────────

    def format(self, **kwargs) -> str:
        """
        Format the template with provided variables.

        Same as __call__ but more explicit.
        """
        return self(**kwargs)

    def preview(self, **kwargs) -> str:
        """
        Preview the formatted prompt (truncated for display).

        Useful for logging without dumping entire prompts.
        """
        formatted = self(**kwargs)
        if len(formatted) > 200:
            return formatted[:200] + "..."
        return formatted

    # ── Private Methods ──────────────────────────────────────────────────────

    def _validate_variables(self, provided: dict) -> None:
        """
        Ensure all required template variables are provided.

        OOP Concept: Encapsulation — validation logic is internal.
        External code just calls the template and gets clear errors.
        """
        required = set(self.variable_names)
        provided_keys = set(provided.keys())
        missing = required - provided_keys

        if missing:
            raise ValueError(
                f"Prompt '{self.name}' missing required variables: {missing}. "
                f"Required: {required}, Provided: {provided_keys}"
            )

    # ── Class Methods ────────────────────────────────────────────────────────

    @classmethod
    def system(cls, name: str, template: str, **kwargs) -> "PromptTemplate":
        """Factory method for system prompts."""
        return cls(name=name, template=template, role="system", **kwargs)

    @classmethod
    def user(cls, name: str, template: str, **kwargs) -> "PromptTemplate":
        """Factory method for user prompts."""
        return cls(name=name, template=template, role="user", **kwargs)


@dataclass
class PromptPair:
    """
    A paired system + user prompt, ready to send to the LLM.

    OOP Concept: Composition — contains two PromptTemplate objects.
    Created via the + operator on PromptTemplate.
    """

    system: PromptTemplate
    user: PromptTemplate

    def format(self, **kwargs) -> tuple[str, str]:
        """Format both prompts and return as (system_text, user_text) tuple."""
        return (self.system(**kwargs), self.user(**kwargs))

    def __repr__(self) -> str:
        return f"PromptPair(system={self.system.name!r}, user={self.user.name!r})"


# ══════════════════════════════════════════════════════════════════════════════
# PROMPT DEFINITIONS — All prompts for the agent pipeline
# ══════════════════════════════════════════════════════════════════════════════


# ── Step 1: JD Skill Extractor ───────────────────────────────────────────────

JD_EXTRACTOR_SYSTEM = PromptTemplate.system(
    name="jd_extractor_system",
    description="System prompt for JD analysis agent",
    template=(
        "You are an expert recruiter and job description analyst.\n"
        "Analyze the given job description and extract structured information.\n"
        "Be precise and only extract what is explicitly stated or clearly implied.\n"
        "Consider industry context and common skill associations when categorizing."
    ),
)

JD_EXTRACTOR_USER = PromptTemplate.user(
    name="jd_extractor_user",
    description="User prompt for JD analysis with role context",
    template=(
        "Analyze this job description and return a JSON object with these keys:\n\n"
        '- "top_keywords": list of top 8 keywords/skills from the JD\n'
        '- "must_have_skills": list of required/must-have skills\n'
        '- "nice_to_have_skills": list of preferred/nice-to-have skills\n'
        '- "tools_technologies": list of specific tools, technologies, platforms mentioned\n'
        '- "responsibilities": list of key role responsibilities (max 6)\n'
        '- "seniority_level": detected seniority level (e.g., "Entry Level", "Mid Level", "Senior", "Unknown")\n\n'
        "{role_context}\n\n"
        'Job Description:\n"""\n{jd_text}\n"""'
    ),
)

# ── Step 2: Resume Matcher ───────────────────────────────────────────────────

RESUME_MATCHER_SYSTEM = PromptTemplate.system(
    name="resume_matcher_system",
    description="System prompt for ATS matching agent",
    template=(
        "You are an expert ATS (Applicant Tracking System) analyst.\n"
        "Compare a resume against a job description and provide an honest assessment.\n"
        "Do not inflate scores. Be helpful and specific.\n"
        "Consider both explicit keyword matches and transferable skills."
    ),
)

RESUME_MATCHER_USER = PromptTemplate.user(
    name="resume_matcher_user",
    description="User prompt for resume-JD comparison",
    template=(
        "Compare this resume against the job description and return a JSON object:\n\n"
        '- "match_score": integer from 0 to 100\n'
        '- "matched_skills": list of skills found in both resume and JD\n'
        '- "missing_skills": list of JD skills NOT found in the resume\n'
        '- "weak_skills": list of skills mentioned in resume but not strongly demonstrated\n'
        '- "sections_to_improve": list of resume sections that need work\n'
        '- "score_explanation": 2-3 sentence explanation of the score\n\n'
        'Job Description:\n"""\n{jd_text}\n"""\n\n'
        'Resume:\n"""\n{resume_text}\n"""'
    ),
)

# ── Step 3: Resume Bullet Rewriter ───────────────────────────────────────────

REWRITER_SYSTEM = PromptTemplate.system(
    name="rewriter_system",
    description="System prompt for bullet rewriting with honesty guardrails",
    template=(
        "You are an expert resume writer specializing in ATS optimization.\n\n"
        "CRITICAL RULES:\n"
        "- Do NOT invent fake experience, projects, metrics, or tools\n"
        "- Do NOT add skills, companies, or technologies not present in the original resume\n"
        "- ONLY improve wording, action verbs, clarity, and keyword alignment\n"
        "- If measurable impact is not in the original, do NOT fabricate numbers\n"
        "- Keep bullets concise and professional\n"
        "- Use strong action verbs (Led, Architected, Optimized, Delivered)\n"
        "- Quantify impact ONLY when the original provides data"
    ),
)

REWRITER_USER = PromptTemplate.user(
    name="rewriter_user",
    description="User prompt for bullet rewriting",
    template=(
        "Rewrite 4-5 resume bullet points to better align with the job description.\n\n"
        'Return a JSON object with key "bullets" containing a list of objects, each with:\n'
        '- "original": the original bullet or source context from the resume\n'
        '- "rewritten": the improved version\n'
        '- "changes_made": brief note on what was improved\n\n'
        "Job Description Keywords: {keywords}\n\n"
        'Resume:\n"""\n{resume_text}\n"""'
    ),
)

# ── Step 4: Cover Letter Writer ──────────────────────────────────────────────

COVER_LETTER_SYSTEM = PromptTemplate.system(
    name="cover_letter_system",
    description="System prompt for cover letter generation",
    template=(
        "You are a professional cover letter writer.\n\n"
        "RULES:\n"
        "- Write exactly 3 paragraphs\n"
        "- Do NOT fake or exaggerate experience\n"
        "- Keep tone professional, confident, and fresher-friendly\n"
        "- Be specific — reference actual skills/projects from the resume\n"
        "- Do NOT use generic filler phrases\n"
        "- Show genuine enthusiasm without being over-the-top\n"
        "- Connect the candidate's background to the role's needs"
    ),
)

COVER_LETTER_USER = PromptTemplate.user(
    name="cover_letter_user",
    description="User prompt for cover letter generation",
    template=(
        "Write a 3-paragraph cover letter for this candidate.\n\n"
        "Paragraph 1: Interest in the role + short positioning statement\n"
        "Paragraph 2: Map resume strengths to JD requirements, mention relevant projects/skills\n"
        "Paragraph 3: Motivation, availability/interest, and professional closing\n\n"
        "{role_context}\n\n"
        "Job Description Summary:\n"
        "- Key skills: {keywords}\n"
        "- Responsibilities: {responsibilities}\n\n"
        'Candidate\'s Resume:\n"""\n{resume_text}\n"""\n\n'
        "Return ONLY the cover letter text, no JSON wrapping."
    ),
)

# ── Step 5: Critic Agent ─────────────────────────────────────────────────────

CRITIC_SYSTEM = PromptTemplate.system(
    name="critic_system",
    description="System prompt for quality evaluation",
    template=(
        "You are a strict but fair resume and cover letter critic.\n"
        "You evaluate content for job applications with high standards.\n"
        "Be specific in your feedback — vague praise is not helpful.\n"
        "Focus on actionable improvements, not just identifying problems."
    ),
)

CRITIC_USER = PromptTemplate.user(
    name="critic_user",
    description="User prompt for critic evaluation",
    template=(
        "Review the following rewritten resume bullets and cover letter.\n\n"
        "Score from 1 to 10 based on:\n"
        "- JD relevance (do the bullets/letter address what the JD asks for?)\n"
        "- ATS keyword alignment (are important keywords naturally included?)\n"
        "- Truthfulness (nothing appears fabricated or exaggerated?)\n"
        "- Clarity (is the writing clear and easy to scan?)\n"
        "- Impact (do bullets show value, not just duties?)\n"
        "- Professional tone (appropriate for the role level?)\n\n"
        "Return a JSON object:\n"
        '- "score": integer 1-10\n'
        '- "issues": list of specific problems found\n'
        '- "suggestions": list of actionable improvement suggestions\n\n'
        "Job Description Keywords: {keywords}\n\n"
        "Rewritten Bullets:\n{bullets_text}\n\n"
        'Cover Letter:\n"""\n{cover_letter}\n"""'
    ),
)

# ── Step 6: Revision ─────────────────────────────────────────────────────────

REVISION_SYSTEM = PromptTemplate.system(
    name="revision_system",
    description="System prompt for revision based on critic feedback",
    template=(
        "You are an expert resume writer revising content based on critic feedback.\n\n"
        "CRITICAL RULES (same as before):\n"
        "- Do NOT invent fake experience, projects, metrics, or tools\n"
        "- Do NOT add skills not present in the original resume\n"
        "- ONLY improve based on the specific feedback given\n"
        "- Keep bullets concise and professional\n"
        "- Address each issue raised by the critic"
    ),
)

REVISION_BULLETS_USER = PromptTemplate.user(
    name="revision_bullets_user",
    description="User prompt for bullet revision with feedback",
    template=(
        "Revise these resume bullets based on the critic feedback.\n\n"
        'Return a JSON object with key "bullets" containing a list of objects, each with:\n'
        '- "original": the source context\n'
        '- "rewritten": the improved version\n'
        '- "changes_made": what was changed in this revision\n\n'
        "Critic Feedback:\n"
        "- Issues: {issues}\n"
        "- Suggestions: {suggestions}\n\n"
        "Job Description Keywords: {keywords}\n\n"
        "Current Bullets:\n{bullets_text}\n\n"
        'Original Resume (for fact-checking):\n"""\n{resume_text}\n"""'
    ),
)

REVISION_COVER_LETTER_USER = PromptTemplate.user(
    name="revision_cover_letter_user",
    description="User prompt for cover letter revision with feedback",
    template=(
        "Revise this cover letter based on the critic feedback.\n\n"
        "Critic Feedback:\n"
        "- Issues: {issues}\n"
        "- Suggestions: {suggestions}\n\n"
        "Job Description Keywords: {keywords}\n\n"
        'Current Cover Letter:\n"""\n{cover_letter}\n"""\n\n'
        'Original Resume (for fact-checking):\n"""\n{resume_text}\n"""\n\n'
        "Return ONLY the revised cover letter text, no JSON wrapping."
    ),
)

# ── Step 7: Interview Question Generator ─────────────────────────────────────

INTERVIEW_SYSTEM = PromptTemplate.system(
    name="interview_system",
    description="System prompt for interview question generation",
    template=(
        "You are an experienced technical interviewer and career coach.\n"
        "Generate realistic interview questions based on the job description and candidate profile.\n"
        "Consider both technical and behavioral questions.\n"
        "Focus on areas where the candidate might be challenged."
    ),
)

INTERVIEW_USER = PromptTemplate.user(
    name="interview_user",
    description="User prompt for interview question generation",
    template=(
        "Generate 5 likely interview questions for this candidate.\n\n"
        'Return a JSON object with key "questions" containing a list of objects, each with:\n'
        '- "question": the interview question\n'
        '- "why_asked": why an interviewer would ask this (1-2 sentences)\n'
        '- "preparation_hint": a short tip on how to prepare (1-2 sentences)\n\n'
        "Base questions on:\n"
        "- Job description keywords: {keywords}\n"
        "- Missing skills: {missing_skills}\n"
        "- Candidate's background from resume\n\n"
        'Resume:\n"""\n{resume_text}\n"""\n\n'
        'Job Description:\n"""\n{jd_text}\n"""'
    ),
)
