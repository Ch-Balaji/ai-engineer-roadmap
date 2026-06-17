# 🎯 Resume JD Tailor Agent

A beginner-friendly AI agent that analyzes your resume against a job description and generates tailored content to help you land interviews.

Built with **Python**, **FastAPI**, **vanilla HTML/CSS/JS**, and **AWS Bedrock Claude**.

---

## What It Does

Paste your resume and a job description, and the agent runs a 7-step pipeline:

| Step | What Happens |
|------|-------------|
| 1. JD Skill Extractor | Extracts keywords, skills, tools, and seniority from the JD |
| 2. Resume Matcher | Scores your resume (0-100) and identifies matched/missing skills |
| 3. Bullet Rewriter | Rewrites 4-5 resume bullets for better ATS alignment |
| 4. Cover Letter Writer | Generates a 3-paragraph cover letter |
| 5. Critic Agent | A second AI persona scores the output (1-10) |
| 6. Revision Loop | If score < 8/10, revises and re-critiques (up to 2 times) |
| 7. Interview Questions | Generates 5 likely interview questions with prep hints |

**Important:** The agent never fakes experience. It only improves wording based on what's already in your resume.

---

## Project Structure

```
resume_jd_tailor_agent/
├── server.py                       # FastAPI backend + SSE streaming
├── static/
│   ├── index.html                  # Frontend HTML
│   ├── style.css                   # Modern light-mode CSS
│   └── app.js                      # Frontend logic + SSE client
├── agents/
│   ├── jd_extractor.py             # Step 1: JD analysis
│   ├── resume_matcher.py           # Step 2: Resume scoring
│   ├── resume_rewriter.py          # Step 3 + 6: Bullet rewriting & revision
│   ├── cover_letter_writer.py      # Step 4 + 6: Cover letter & revision
│   ├── critic_agent.py             # Step 5: Quality critic
│   └── interview_generator.py      # Step 7: Interview questions
├── utils/
│   ├── llm_client.py               # AWS Bedrock Claude API client
│   └── prompts.py                  # All LLM prompts in one place
├── requirements.txt
├── .env.example
└── README.md
```

---

## Setup Instructions

### 1. Prerequisites

- Python 3.10+
- AWS account with Bedrock access (Claude model enabled)
- AWS credentials configured (via `aws configure`, SSO, env vars, or IAM role)

### 2. Create a virtual environment

```bash
cd projects/resume-jd-tailor-agent
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your environment

```bash
cp .env.example .env
```

Edit `.env`:

```
AWS_REGION=eu-central-1
AWS_PROFILE=your-aws-profile        # if using SSO
BEDROCK_MODEL_ID=eu.anthropic.claude-sonnet-4-6
```

### 5. Run the app

```bash
uvicorn server:app --reload --port 8501
```

Open **http://localhost:8501** in your browser.

---

## How the Agentic Loop Works

```
Input (Resume + JD)
    │
    ▼
Step 1: Extract JD Skills ──────────────────────┐
    │                                            │
    ▼                                            │
Step 2: Match Resume vs JD                       │
    │                                            │
    ▼                                            │
Step 3: Rewrite Resume Bullets ◄─────────────┐   │
    │                                        │   │
    ▼                                        │   │
Step 4: Write Cover Letter ◄─────────────┐   │   │
    │                                    │   │   │
    ▼                                    │   │   │
Step 5: Critic Reviews Output            │   │   │
    │                                    │   │   │
    ├── Score ≥ 8/10 → Continue          │   │   │
    │                                    │   │   │
    └── Score < 8/10 → Revise ──────────►┘───┘   │
         (max 2 loops)                            │
    │                                            │
    ▼                                            │
Step 7: Generate Interview Questions ◄───────────┘
    │
    ▼
  Output (streamed to browser via SSE)
```

The **critic agent** acts as a quality gate using a different LLM persona. If the score is below 8/10, the pipeline feeds specific issues and suggestions back into the rewriter and cover letter agents for targeted improvements.

Results stream to the browser in real time via **Server-Sent Events (SSE)**, so you see each step complete as it happens.

---

## YouTube Demo Talking Points

1. **What is an AI Agent?** — Multiple specialized AI steps working together with a feedback loop
2. **The Architecture** — 7 specialized agents, each with a focused job
3. **The Feedback Loop** — Critic scores output, auto-revises if below threshold
4. **Honesty Guardrails** — Never fakes experience, missing skills flagged separately
5. **Real-time Streaming** — SSE streams results as each step completes
6. **Tech Stack** — Python + FastAPI backend, vanilla HTML/CSS/JS frontend, AWS Bedrock Claude

---

## License

Demo project for educational purposes. Use freely.
