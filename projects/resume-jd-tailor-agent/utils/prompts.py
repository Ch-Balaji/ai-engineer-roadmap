"""
All LLM prompts used by the agent pipeline.

Keeping prompts in one place makes them easy to tweak and review.
"""

# ── Step 1: JD Skill Extractor ──────────────────────────────────────────────

JD_EXTRACTOR_SYSTEM = """You are an expert recruiter and job description analyst.
Analyze the given job description and extract structured information.
Be precise and only extract what is explicitly stated or clearly implied."""

JD_EXTRACTOR_USER = """Analyze this job description and return a JSON object with these keys:

- "top_keywords": list of top 8 keywords/skills from the JD
- "must_have_skills": list of required/must-have skills
- "nice_to_have_skills": list of preferred/nice-to-have skills
- "tools_technologies": list of specific tools, technologies, platforms mentioned
- "responsibilities": list of key role responsibilities (max 6)
- "seniority_level": detected seniority level (e.g., "Entry Level", "Mid Level", "Senior", "Unknown")

{role_context}

Job Description:
\"\"\"
{jd_text}
\"\"\"
"""

# ── Step 2: Resume Matcher ───────────────────────────────────────────────────

RESUME_MATCHER_SYSTEM = """You are an expert ATS (Applicant Tracking System) analyst.
Compare a resume against a job description and provide an honest assessment.
Do not inflate scores. Be helpful and specific."""

RESUME_MATCHER_USER = """Compare this resume against the job description and return a JSON object:

- "match_score": integer from 0 to 100
- "matched_skills": list of skills found in both resume and JD
- "missing_skills": list of JD skills NOT found in the resume
- "weak_skills": list of skills mentioned in resume but not strongly demonstrated
- "sections_to_improve": list of resume sections that need work (e.g., "Projects", "Skills")
- "score_explanation": 2-3 sentence explanation of the score

Job Description:
\"\"\"
{jd_text}
\"\"\"

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

# ── Step 3: Resume Bullet Rewriter ───────────────────────────────────────────

REWRITER_SYSTEM = """You are an expert resume writer specializing in ATS optimization.

CRITICAL RULES:
- Do NOT invent fake experience, projects, metrics, or tools
- Do NOT add skills, companies, or technologies not present in the original resume
- ONLY improve wording, action verbs, clarity, and keyword alignment
- If measurable impact is not in the original, do NOT fabricate numbers
- Keep bullets concise and professional"""

REWRITER_USER = """Rewrite 4-5 resume bullet points to better align with the job description.

Return a JSON object with key "bullets" containing a list of objects, each with:
- "original": the original bullet or source context from the resume
- "rewritten": the improved version
- "changes_made": brief note on what was improved

Job Description Keywords: {keywords}

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

# ── Step 4: Cover Letter Writer ──────────────────────────────────────────────

COVER_LETTER_SYSTEM = """You are a professional cover letter writer.

RULES:
- Write exactly 3 paragraphs
- Do NOT fake or exaggerate experience
- Keep tone professional, confident, and fresher-friendly
- Be specific — reference actual skills/projects from the resume
- Do NOT use generic filler phrases"""

COVER_LETTER_USER = """Write a 3-paragraph cover letter for this candidate.

Paragraph 1: Interest in the role + short positioning statement
Paragraph 2: Map resume strengths to JD requirements, mention relevant projects/skills
Paragraph 3: Motivation, availability/interest, and professional closing

{role_context}

Job Description Summary:
- Key skills: {keywords}
- Responsibilities: {responsibilities}

Candidate's Resume:
\"\"\"
{resume_text}
\"\"\"

Return ONLY the cover letter text, no JSON wrapping.
"""

# ── Step 5: Critic Agent ────────────────────────────────────────────────────

CRITIC_SYSTEM = """You are a strict but fair resume and cover letter critic.
You evaluate content for job applications with high standards.
Be specific in your feedback — vague praise is not helpful."""

CRITIC_USER = """Review the following rewritten resume bullets and cover letter.

Score from 1 to 10 based on:
- JD relevance (do the bullets/letter address what the JD asks for?)
- ATS keyword alignment (are important keywords naturally included?)
- Truthfulness (nothing appears fabricated or exaggerated?)
- Clarity (is the writing clear and easy to scan?)
- Impact (do bullets show value, not just duties?)
- Professional tone (appropriate for the role level?)

Return a JSON object:
- "score": integer 1-10
- "issues": list of specific problems found
- "suggestions": list of actionable improvement suggestions

Job Description Keywords: {keywords}

Rewritten Bullets:
{bullets_text}

Cover Letter:
\"\"\"
{cover_letter}
\"\"\"
"""

# ── Step 6: Revision ────────────────────────────────────────────────────────

REVISION_SYSTEM = """You are an expert resume writer revising content based on critic feedback.

CRITICAL RULES (same as before):
- Do NOT invent fake experience, projects, metrics, or tools
- Do NOT add skills not present in the original resume
- ONLY improve based on the specific feedback given
- Keep bullets concise and professional"""

REVISION_BULLETS_USER = """Revise these resume bullets based on the critic feedback.

Return a JSON object with key "bullets" containing a list of objects, each with:
- "original": the source context
- "rewritten": the improved version
- "changes_made": what was changed in this revision

Critic Feedback:
- Issues: {issues}
- Suggestions: {suggestions}

Job Description Keywords: {keywords}

Current Bullets:
{bullets_text}

Original Resume (for fact-checking):
\"\"\"
{resume_text}
\"\"\"
"""

REVISION_COVER_LETTER_USER = """Revise this cover letter based on the critic feedback.

Critic Feedback:
- Issues: {issues}
- Suggestions: {suggestions}

Job Description Keywords: {keywords}

Current Cover Letter:
\"\"\"
{cover_letter}
\"\"\"

Original Resume (for fact-checking):
\"\"\"
{resume_text}
\"\"\"

Return ONLY the revised cover letter text, no JSON wrapping.
"""

# ── Step 7: Interview Question Generator ────────────────────────────────────

INTERVIEW_SYSTEM = """You are an experienced technical interviewer and career coach.
Generate realistic interview questions based on the job description and candidate profile."""

INTERVIEW_USER = """Generate 5 likely interview questions for this candidate.

Return a JSON object with key "questions" containing a list of objects, each with:
- "question": the interview question
- "why_asked": why an interviewer would ask this (1-2 sentences)
- "preparation_hint": a short tip on how to prepare (1-2 sentences)

Base questions on:
- Job description keywords: {keywords}
- Missing skills: {missing_skills}
- Candidate's background from resume

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{jd_text}
\"\"\"
"""
