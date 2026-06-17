# Agentic AI: Production-Grade — Course Design Spec

**Date:** 2026-06-16
**Status:** Draft for review
**Owner:** (channel owner)

---

## 1. Vision

A premium, flagship course that takes a learner from understanding how LLMs
work to **building, deploying, and monitoring production-grade agentic AI
systems** in Python. The course is the deep, paid counterpart to the channel's
free YouTube explainers.

- **Audience:** Broad — students, working professionals, career-switchers, and
  curious people from other fields. The course assumes the learner can code at a
  basic level (see Prerequisite below) but assumes **no prior AI/agent
  knowledge**.
- **Promise / outcomes (all four):**
  1. Understand agents deeply by building them from scratch (no magic).
  2. Master production agent frameworks (LangGraph et al.).
  3. Ship a production-grade agentic app to real users.
  4. Be portfolio- and interview-ready as an AI/Agent engineer.
- **Delivery / monetization:** Premium paid flagship on own platform.
- **Primary language/stack:** Python.
- **Target length:** ~70–80 hrs of content (this course), excluding the separate
  Foundations prerequisite.

---

## 2. Prerequisite (separate product)

Pure software-engineering foundations are pulled OUT of this course into their
own standalone prerequisite course, so every hour here is about agents.

**Foundations course (separate):** Python · SQL · OOP · FastAPI · Pydantic.

- Learners who already code can skip straight to this course.
- True beginners are routed to Foundations first.
- This becomes a second sellable product and a funnel into the flagship.

> Note: **Pydantic** concepts are re-touched briefly where structured outputs
> appear; **FastAPI** is taught/used in the Deployment module so it's fresh when
> shipping.

---

## 3. Pedagogical model

### 3.1 Theory video → Project video rhythm
Each chapter is delivered as **paired videos**:

- **Theory video** — self-contained concept explainer. Has a small (60–90s)
  concrete hook/visual so it works as a standalone YouTube upload. **No
  dependency on the running app** → fully repurposable as evergreen channel
  content / funnel.
- **Project video** — applies the concept by advancing the **single running
  example app**. This is the paid value; hard to find free.

This decoupling is also a maintenance superpower: when a framework API changes,
re-record the *project* video; the *theory* stays valid.

### 3.2 Architecture: Approach B (Layered Mastery) + spiral spine
Clean, navigable, sellable **layered modules** (Approach B), but the project
videos build **ONE coherent running app** end-to-end (spiral spine) for
motivation and a satisfying final product.

### 3.3 Time-to-first-agent
A **cold-open Module 0** lets learners build a tiny working agent in the first
~30–45 minutes, *before* the fundamentals grind. Critical for retention on a
70–80 hr course.

---

## 4. The running example app

**Recommended: "Atlas" — a personal research & operations assistant.** It grows
across the whole course:

| Stage (module) | What Atlas gains |
|---|---|
| 0 Cold-open | A tiny one-shot agent that answers a question |
| 3 Agentic foundations | A real agent loop (reason → act → observe) |
| 4 Tools + MCP + RAG | Web search, calculators, MCP tools, RAG over docs |
| 5 Memory | Remembers user prefs + past research (episodic/semantic) |
| 6 State machines/DAGs | Deterministic routing + human-in-the-loop |
| 7 Multi-agent | Researcher + Writer + Critic collaboration |
| 8 Evaluation | Success-rate + trajectory benchmarks |
| 9 Security/Guardrails | I/O guardrails, prompt-injection defense, sandboxing |
| 10 Deployment | FastAPI + Docker + cloud + UI, CI/CD |
| 11 Monitoring | Live tracing, cost dashboards, feedback loops |
| 12 Capstone | Learner builds their OWN variant end-to-end |

> **Decision needed:** confirm "Atlas / research assistant" as the running app,
> or swap for another domain (e.g., customer-support agent, coding agent,
> personal finance agent).

---

## 5. Module map (this course)

> Foundations (Python/SQL/OOP/FastAPI/Pydantic) = separate prerequisite course.

| # | Module | ~Hrs |
|---|---|---|
| 0 | Cold-open: build a tiny agent today | 1 |
| 1 | NLP Basics (intuition-first) | 6–8 |
| 2 | LLMs: internals, parameters, benchmarking, cost | 5–6 |
| 3 | Foundations of Agentic Systems | 5 |
| 4 | Tools + MCP + RAG | 8 |
| 5 | Memory & optimization | 5 |
| 6 | State machines & DAGs | 5 |
| 7 | Multi-agent orchestration | 6 |
| 8 | Evaluation | 5 |
| 9 | Security & Guardrails | 4 |
| 10 | Deployment (incl. FastAPI) | 8 |
| 11 | Monitoring & Operations | 5 |
| 12 | Capstone projects | 8–10 |

**Total ≈ 71–76 hrs** (premium flagship; trim room available).

---

## 6. Module detail (theory/project breakdown)

> Each bullet = a chapter delivered as a Theory video + Project video pair,
> unless marked (T-only) for pure-concept chapters.

### Module 0 — Cold-open: build a tiny agent today (~1h)
- (T-only) What you'll build by the end of this course (Atlas demo)
- Project: a 40-line "agent" that takes a goal, calls an LLM, uses one tool,
  returns a result. No frameworks. The "aha".

### Module 1 — NLP Basics, intuition-first (~6–8h)
- Theory: what "deep learning" means (no math); tokens & tokenization
- Theory: embeddings & vector similarity (visual intuition)
- Theory: transformers & attention / self-attention (visual, no derivations)
- Theory: positional encodings, NER, classic NLP tasks
- (Bonus track) "Under the hood": the math for those who want it
- Project: build a tiny semantic search over text using embeddings

### Module 2 — LLMs: internals & economics (~5–6h)
- Theory: what an LLM is; how they're trained; knowledge cutoff dates
- Theory: controlling LLMs — temperature, top-p, max tokens, reasoning modes
- Theory: how LLMs are evaluated / benchmarked
- Theory: choosing the right LLM for the job; pricing & cost models
- Project: a provider-agnostic LLM wrapper (OpenAI default; local via Ollama)

### Module 3 — Foundations of Agentic Systems (~5h) *(from handwritten notes)*
- **A. Core architecture**
  - Theory: what is an agent? (vs LLM vs workflow)
  - Theory: the agent loop (input → reasoning → action → output, + feedback)
  - Theory: autonomy levels (rule-based → fully autonomous)
- **B. Cognitive frameworks**
  - Theory: ReAct protocol (reasoning + acting)
  - Theory: Plan-and-Solve (complex requirement → sub-tasks)
  - Theory: self-reflective loop (validation)
- Project: upgrade Atlas into a real ReAct agent loop, from scratch

### Module 4 — Tools + MCP + RAG (~8h) *(extends handwritten "Action & Tool")*
- Theory: function calling / structured tool use
- Theory: tool sandboxing (security protocols)
- Theory: error handling & the self-correction loop
- Theory: MCP — connecting agents to the world (standard, servers, clients)
- Theory: RAG — chunking, embeddings, retrieval, reranking, grounding/citations
- Project: give Atlas tools (search, calc), an MCP integration, and a RAG
  pipeline over a document set

### Module 5 — Memory & optimization (~5h) *(from handwritten notes)*
- Theory: short-term memory (managing the context window)
- Theory: long-term memory (vector DBs, profiling)
- Theory: episodic vs semantic memory (specific logs vs generalized facts)
- Theory: context optimization & token budgeting
- Project: Atlas remembers user preferences + past research across sessions

### Module 6 — State machines & DAGs (~5h) *(from handwritten notes)*
- Theory: stateful agents (single source of truth)
- Theory: deterministic routing (conditional code + flexible AI decisions)
- Theory: human-in-the-loop
- Theory: framing LangGraph as graphs/state/nodes
- Project: re-architect Atlas on LangGraph with routing + an approval step

### Module 7 — Multi-agent orchestration (~6h) *(from handwritten notes)*
- Theory: personas & specialization (coder, reviewer, researcher…)
- Theory: orchestration patterns (hierarchical vs peer-to-peer)
- Theory: communication protocols (message passing, shared memory)
- Theory: brief tour of OpenAI Agents SDK / CrewAI as alternatives
- Project: Atlas becomes a Researcher + Writer + Critic team

### Module 8 — Evaluation (~5h) *(from handwritten notes)*
- Theory: agentic evaluation — success rate for non-deterministic outcomes
- Theory: trajectory benchmarking (test for the most efficient path)
- Theory: building eval datasets & regression suites
- Project: an eval harness for Atlas + a regression suite

### Module 9 — Security & Guardrails (~4h) *(from handwritten notes)*
- Theory: input/output guardrails (prevent prompt injection / jailbreaks)
- Theory: tool sandboxing & least-privilege (revisited at depth)
- Theory: secrets, PII, data handling
- Project: add guardrails + injection defenses to Atlas

### Module 10 — Deployment (~8h)
- Theory: serving agents with FastAPI; async basics for agents
- Theory: containerization with Docker
- Theory: cloud deploy (start simple → real cloud), CI/CD
- Theory: reliability — retries, timeouts, queues, scaling
- Project: deploy Atlas (FastAPI + Docker + cloud) with a chat UI + CI/CD

### Module 11 — Monitoring & Operations (~5h) *(from handwritten notes)*
- Theory: traceability — log every step / tool call / cost
- Theory: observability tooling (Langfuse): tracing, dashboards, alerts
- Theory: token & cost optimization in production
- Theory: feedback loops & continuous improvement
- Project: instrument Atlas with Langfuse; build a cost/quality dashboard

### Module 12 — Capstone projects (~8–10h)
- Learners build their OWN agentic product end-to-end, deployed + monitored.
- Provide 2–3 capstone briefs in different domains.
- Portfolio + interview-prep guidance.

---

## 7. Stack & defaults (assumptions — confirm/veto)

- **Frameworks:** raw/from-scratch first → LangGraph (primary) → OpenAI Agents
  SDK + CrewAI (alternatives/tour).
- **Models:** OpenAI default; local/open-source via Ollama to remove cost
  barriers; provider-agnostic wrapper.
- **RAG/vector:** a beginner-friendly vector store (e.g., Chroma) → note
  production options.
- **Observability:** Langfuse.
- **Deployment:** progression — simple cloud (Render/HF Spaces) → Docker + real
  cloud + CI/CD.

---

## 8. Existing assets that map in

The channel already has content that can seed early modules:

- `AI_Agent_tool_From_Scratch.ipynb` → Modules 0/3 (agent from scratch)
- `19.1.5_calling_openai_in_practice.ipynb` → Module 2 (LLM wrapper)
- `youtube/scripts/V_prompt-engineering-masterclass-2026.md` → Module 2 / prompting
- `youtube/scripts/V_genai-vs-agentic-vs-agents*.md` → Module 3 (what is an agent)
- `youtube/scripts/V_giving-llm-hands-and-legs-2026.md` → Module 4 (tools)
- `youtube/scripts/V_context-engineering-2026.md` → Module 5 (context/memory)
- `media/audio/AI gents from scratch.*` → Modules 0/3

---

## 9. Open decisions (for review)

1. **Running app:** confirm "Atlas / research assistant" or pick another domain.
2. **Hour ceiling:** accept ~71–76 hrs (slightly under 80) as final, or expand
   capstone/bonus tracks toward 80+?
3. **Stack defaults** in §7 — any swaps (e.g., different vector DB, add
   Anthropic/Gemini as first-class)?
4. **Bonus "under the hood" math track** in Module 1 — include from launch or
   add later?
5. **Frameworks emphasis:** LangGraph as the single primary OK, or give OpenAI
   Agents SDK equal weight?

---

## 10. Appendix — original handwritten notes (transcribed verbatim)

**Phase 1: Foundations of Agentic Systems**
- A) Core Architecture
  - What is an Agent?
  - The Agent Loop (i/p → Reasoning → Action → o/p) [+ Feedback]
  - Autonomy levels (Rule-based vs. Fully autonomous)
- B) Cognitive Frameworks
  - ReAct Protocol (Reasoning + Acting)
  - Plan and Solve (Complex Requirement → sub-tasks)
  - Self-Reflective loop (Validation)

**Phase 2: Core Components & Memory Architecture**
- A) Action and Tool Integration
  - Function Calling
  - Tool Sandboxing (security protocols)
  - Error Handling (Self-correction loop)
- B) Memory System Design
  - Short-Term Memory (Managing context window)
  - Long-Term Memory (Vector databases / Profiling)
  - Episodic vs Semantic Memory (Specific past logs vs Generalized facts)

**Phase 3: Advanced Agent Paradigms**
- 1) State Machines and DAGs
  - Stateful Agents (Systems that maintain a single source of truth)
  - Deterministic Routing (Conditional code with flexible AI decision)
  - Human-In-the-loop
- 2) Multi-Agent Networks
  - Personas & Specialization (Coder, Reviewer)
  - Orchestration Pattern (Hierarchical vs. Peer-to-peer)
  - Communication Protocols (Message & Memory sharing)

**Phase 4: Production, Evaluation & Security**
- 1) Evaluation and Guardrails
  - Agentic Evaluation (Success Rate for Non-deterministic outcome)
  - Trajectory Benchmarking (Test for most efficient path)
  - Input/Output Guardrails (Prevent prompt injection / Jailbreaks)
- 2) Monitoring and Optimization
  - Traceability (Log every step / tool call / cost)
  - Token and cost optimization

---

## 11. Your teaching style (analyzed from existing scripts + voice skill)

Before designing the video flow, here's the DNA extracted from
`youtube/skills/01-balaji-voice`, `07-hook-factory`, and shipped scripts
(`V_giving-llm-hands-and-legs`, `V_genai-vs-agentic-vs-agents`,
`V_how-llms-are-built`, etc.). **Every video title and ordering decision below is
built to fit this style.**

### 11.1 The 5-level explanation ladder (your core move)
Every concept is taught as: **L1 analogy → L2 plain story → L3 name the term →
L4 one step deeper (code/production) → L5 honest "saved for later".**
Example: "brain in a jar" (L1) → "it can only think and talk" (L2) → "this is
*tool calling*" (L3) → `finish_reason: tool_calls`, `content: None` (L4) → "tools
could be shared… that's MCP, next video" (L5).

### 11.2 One running metaphor per video
Each video is held together by a single concrete metaphor: *brain in a jar*,
*brain in a windowless room*, *give it hands and legs*, *the menu (JSON schema)*.
The metaphor is named in the first 40 seconds and paid off in the recap.

### 11.3 Hook in <30s, no throat-clearing
No "hey guys / in this video we'll cover". Tutorials open **live-demo-first** or
**production-incident-first**. A knowledge gap is created immediately.

### 11.4 "No black box" — build from scratch before naming a framework
The hard rule: build the raw thing by hand once (the agent loop, RAG, memory),
*then* reveal that LangGraph/MCP/etc. are "just sugar over this." Frameworks are
never the first explanation.

### 11.5 Show the real failure, then fix it
Demos must break on camera (rate limits, prompt injection, lost-in-the-middle)
and then get fixed. No happy-path-only walkthroughs. This is the production
credibility beat.

### 11.6 Voice mechanics
Direct address to **one** person (`you`, never "guys"). Telugu delivery, English
technical terms preserved. Short declarative sentences (<18 words). Concrete
numbers and named tools, never "some library". Signature phrases used sparingly:
*"no black box"*, *"step by step"*, *"in real time, in production"*.

### 11.7 Retention scaffolding
Each video has retention beats (mini-cliffhangers mid-video), 1–2 playlist
callbacks ("remember the brain in the jar?"), and a next-video cliffhanger.
**This is why the running app matters:** every project video can callback the
previous one and tease the next.

> **Implication for this course:** the **Theory video** carries the metaphor +
> ladder (L1–L3, evergreen, repurposable to YouTube). The **Project video**
> carries L4 (real code on Atlas) + the "show the failure, then fix" beat + the
> callbacks/cliffhanger. This is exactly the decoupling in §3.1.

---

## 12. Chapter & video flow (the build order)

> **Reading key.** Each module → chapters. Each chapter ships as a
> **[T] Theory video** (evergreen, YouTube-repurposable, no app dependency) and a
> **[P] Project video** (advances the single running app, *Atlas*).
> **[T-only]** = pure-concept chapter, no project beat.
> Titles are draft, written in channel voice (metaphor + concrete). Each [P]
> video is named *"Build It: …"* so the paid track reads as one continuous build.
> The **spine line** under each module states the one sentence the learner can
> say after finishing it — each builds on the previous.

### Module 0 — Cold-open: build a tiny agent today
*Spine: "I built a working agent on day one."*

- **0.1 — What we're building (the whole course in one demo)**
  - [T] *Meet Atlas: The AI Assistant You'll Build, Deploy & Monitor*
- **0.2 — Your first agent, no frameworks**
  - [P] *Build It: A Working AI Agent in 40 Lines (No Frameworks, No Magic)*

### Module 1 — NLP Basics (intuition-first)
*Spine: "I know what text becomes before an LLM ever sees it."*

- **1.1 — How machines learned to understand language**
  - [T] *Deep Learning Explained Without a Single Equation*
- **1.2 — Tokens: how AI actually reads**
  - [T] *Tokens: Why AI Doesn't See Words the Way You Do*
- **1.3 — Embeddings: turning meaning into numbers**
  - [T] *Embeddings: How a Computer Learns That "King" and "Queen" Are Close*
- **1.4 — Vector similarity**
  - [T] *Cosine Similarity: How Machines Measure "These Two Things Mean the Same"*
- **1.5 — Transformers & attention**
  - [T] *Attention, Explained for Humans: How a Model Decides What Matters*
  - [T] *Self-Attention: How a Sentence Understands Itself*
- **1.6 — Positional encoding, NER & classic NLP tasks**
  - [T] *Word Order, Names & the Classic NLP Tasks You Still Need in 2026*
- **1.7 — (Bonus track) Under the hood**
  - [T-only] *Bonus: The Actual Math Behind Transformers (For the Curious)*
- **1.8 — First build with embeddings**
  - [P] *Build It: Semantic Search Over Your Own Notes (Atlas Learns to "Find Meaning")*

### Module 2 — LLMs: internals, parameters, benchmarking, cost
*Spine: "I can pick and control the right model for a job — and predict its cost."*

- **2.1 — What an LLM really is & how it's trained**
  - [T] *What Is an LLM, Really? Next-Token Prediction Explained From Scratch*
- **2.2 — Knowledge cutoffs & why models hallucinate**
  - [T] *The Brain in a Windowless Room: Cutoffs, Hallucination & What LLMs Can't Know*
- **2.3 — Controlling the model**
  - [T] *Temperature, Top-p & Max Tokens: The Dials That Change Everything*
  - [T] *Reasoning vs Base Models: When "Thinking" Models Actually Win*
- **2.4 — How LLMs are evaluated / benchmarked**
  - [T] *MMLU, Benchmarks & Lies: How to Actually Judge an LLM*
- **2.5 — Choosing the right LLM + pricing & cost**
  - [T] *Picking the Right LLM: Quality vs Speed vs Cost (The Real Tradeoff)*
- **2.6 — One wrapper for every model**
  - [P] *Build It: A Provider-Agnostic LLM Client (OpenAI + Local via Ollama) for Atlas*

### Module 3 — Foundations of Agentic Systems
*Spine: "I understand the agent loop deeply because I built it by hand."*

- **3.1 — What is an agent? (vs LLM vs workflow)**
  - [T] *Chatbot vs Agent: The One Difference Nobody Explains Clearly*
- **3.2 — The agent loop (reason → act → observe → repeat)**
  - [T] *The Loop Inside Every AI Agent on Earth*
  - [P] *Build It: Upgrade Atlas Into a Real Reason-Act-Observe Loop (From Scratch)*
- **3.3 — Autonomy levels**
  - [T] *From Rule-Based to Fully Autonomous: The 5 Levels of Agent Autonomy*
- **3.4 — Cognitive framework: ReAct**
  - [T] *ReAct: How an Agent Thinks Out Loud Before It Acts*
  - [P] *Build It: Give Atlas a ReAct Brain*
- **3.5 — Cognitive framework: Plan-and-Solve**
  - [T] *Plan-and-Solve: Breaking a Hard Goal Into Steps an Agent Can Do*
  - [P] *Build It: Atlas Plans a Multi-Step Research Task*
- **3.6 — Self-reflection loop**
  - [T] *Self-Reflection: How an Agent Catches Its Own Mistakes*
  - [P] *Build It: Atlas Critiques and Fixes Its Own Output*

### Module 4 — Tools + MCP + RAG
*Spine: "My agent can act on the real world and answer from my own documents."*

- **4.1 — Function calling / tool use**
  - [T] *Give Your LLM Hands: Tool Calling From Scratch* (existing script V036)
  - [P] *Build It: Atlas Gets Its First Tools (Live Search + Calculator)*
- **4.2 — Tool sandboxing (intro)**
  - [T] *Letting an AI Run Code Without Burning Your House Down*
  - [P] *Build It: A Safe Tool Sandbox for Atlas*
- **4.3 — Error handling & self-correction**
  - [T] *When Tools Fail: Retries, Backoff & the Self-Correction Loop*
  - [P] *Build It: Make Atlas Recover From Failing Tools*
- **4.4 — MCP: the universal tool standard**
  - [T] *MCP: The USB-C Port for AI Agents*
  - [P] *Build It: Plug Atlas Into MCP Servers (GitHub, Files, More)*
- **4.5 — RAG fundamentals**
  - [T] *RAG Explained: Why a 200k Context Window Still Isn't Enough*
  - [T] *Chunking, Retrieval & Reranking: The Anatomy of a RAG Pipeline*
- **4.6 — Grounding & citations**
  - [T] *Grounded Answers: How to Make an Agent Cite Its Sources*
  - [P] *Build It: A RAG Pipeline So Atlas Answers From Your Documents*

### Module 5 — Memory & optimization
*Spine: "My agent remembers across sessions and doesn't blow the context window."*

- **5.1 — Short-term memory & the context window**
  - [T] *The Context Window: Why Your Agent Forgets Mid-Conversation*
  - [P] *Build It: Conversation Memory for Atlas*
- **5.2 — Long-term memory (vector DBs, profiling)**
  - [T] *Long-Term Memory: How Production Agents Remember You*
  - [P] *Build It: Atlas Remembers Your Preferences Across Sessions*
- **5.3 — Episodic vs semantic memory**
  - [T] *Episodic vs Semantic Memory: Specific Logs vs Learned Facts*
  - [P] *Build It: Atlas Recalls Past Research and Generalizes From It*
- **5.4 — Context optimization & token budgeting**
  - [T] *Lost in the Middle: Why Long Context Degrades & How to Fight It*
  - [P] *Build It: Trim, Summarize & Budget Atlas's Context for Cost*

### Module 6 — State machines & DAGs
*Spine: "I can control an agent's flow deterministically and pause for a human."*

- **6.1 — Stateful agents (single source of truth)**
  - [T] *Why Loops Aren't Enough: State as the Single Source of Truth*
- **6.2 — Thinking in graphs (nodes, edges, state)**
  - [T] *Agents as Graphs: The Mental Model Behind LangGraph*
  - [P] *Build It: Re-Architect Atlas on LangGraph (No Black Box)*
- **6.3 — Deterministic routing**
  - [T] *Conditional Routing: Letting Code Decide When the AI Shouldn't*
  - [P] *Build It: Add Smart Routing to Atlas*
- **6.4 — Human-in-the-loop**
  - [T] *Human-in-the-Loop: Pausing an Agent for Approval Before It Acts*
  - [P] *Build It: An Approval Checkpoint Before Atlas Takes Risky Actions*

### Module 7 — Multi-agent orchestration
*Spine: "I can make specialized agents collaborate without burning $400 in a loop."*

- **7.1 — Personas & specialization**
  - [T] *One Genius vs a Team: When Multiple Agents Beat One*
- **7.2 — Orchestration patterns**
  - [T] *Hierarchical vs Peer-to-Peer: How Agent Teams Are Organized*
  - [P] *Build It: Turn Atlas Into a Researcher + Writer + Critic Team*
- **7.3 — Communication protocols**
  - [T] *How Agents Talk: Message Passing vs Shared Memory*
  - [P] *Build It: Wire Up Communication Between Atlas's Agents*
- **7.4 — Framework tour**
  - [T] *LangGraph vs OpenAI Agents SDK vs CrewAI: When to Use Which*
  - [P] *Build It: The Same Atlas Team, Rebuilt in the OpenAI Agents SDK*

### Module 8 — Evaluation
*Spine: "I can prove my agent works and catch regressions before users do."*

- **8.1 — Why agents are hard to evaluate**
  - [T] *Non-Deterministic Nightmares: Why You Can't Unit-Test an Agent*
- **8.2 — Success-rate evaluation**
  - [T] *Success Rate: Scoring an Agent That Gives a Different Answer Every Time*
  - [P] *Build It: A Success-Rate Eval Harness for Atlas*
- **8.3 — Trajectory benchmarking**
  - [T] *Trajectory Benchmarking: Did the Agent Take the Efficient Path?*
  - [P] *Build It: Measure How Atlas Gets to the Answer, Not Just the Answer*
- **8.4 — Eval datasets & regression suites**
  - [T] *LLM-as-Judge & Eval Datasets: Building a Test Set for Agents*
  - [P] *Build It: A Regression Suite That Blocks Bad Atlas Changes*

### Module 9 — Security & Guardrails
*Spine: "My agent survives malicious users and handles sensitive data safely."*

- **9.1 — Input/output guardrails**
  - [T] *Prompt Injection: How One Sentence Hijacks Your Agent*
  - [P] *Build It: Input & Output Guardrails for Atlas*
- **9.2 — Sandboxing & least privilege (at depth)**
  - [T] *Least Privilege for Agents: Don't Give the AI the Master Key*
  - [P] *Build It: Lock Down Atlas's Tools and Permissions*
- **9.3 — Secrets, PII & data handling**
  - [T] *Secrets, PII & Compliance: What an Agent Must Never Leak*
  - [P] *Build It: Safe Secrets & PII Redaction in Atlas*

### Module 10 — Deployment (incl. FastAPI)
*Spine: "Real users can use my agent over the internet."*

- **10.1 — Serving agents with FastAPI**
  - [T] *From Notebook to API: Serving an Agent With FastAPI*
  - [P] *Build It: Wrap Atlas in a FastAPI Service*
- **10.2 — Async for agents**
  - [T] *Why Agents Need Async: One Hanging LLM Call Shouldn't Freeze Everything*
  - [P] *Build It: Make Atlas's API Async & Streaming*
- **10.3 — Containerization with Docker**
  - [T] *Docker for AI Apps: "It Works on My Machine" Is Not a Deploy*
  - [P] *Build It: Dockerize Atlas*
- **10.4 — Shipping to the cloud + CI/CD**
  - [T] *From Localhost to the Internet: Deploying Agents to the Cloud*
  - [P] *Build It: Deploy Atlas to the Cloud With CI/CD*
- **10.5 — Reliability (retries, timeouts, queues, scaling)**
  - [T] *Reliability for Agents: Timeouts, Queues & Surviving Traffic*
  - [P] *Build It: A Chat UI + Reliability Layer for Atlas*

### Module 11 — Monitoring & Operations
*Spine: "I can see what my live agent is doing, what it costs, and improve it."*

- **11.1 — Traceability**
  - [T] *You Can't Fix What You Can't See: Tracing Every Agent Step*
  - [P] *Build It: Full-Trace Logging for Live Atlas*
- **11.2 — Observability tooling (Langfuse)**
  - [T] *Observability for Agents: Traces, Dashboards & Alerts With Langfuse*
  - [P] *Build It: Instrument Atlas With Langfuse*
- **11.3 — Token & cost optimization in production**
  - [T] *The 3 AM Bill: Cutting Agent Token Costs in Production*
  - [P] *Build It: A Cost & Quality Dashboard for Atlas*
- **11.4 — Feedback loops & continuous improvement**
  - [T] *Closing the Loop: Turning Live Feedback Into a Better Agent*
  - [P] *Build It: A Feedback → Eval → Improve Loop for Atlas*

### Module 12 — Capstone projects
*Spine: "I shipped and monitored my OWN agentic product — I'm portfolio-ready."*

- **12.1 — Choosing & scoping your capstone**
  - [T] *How to Scope an Agentic Project That Actually Ships*
- **12.2 — Capstone brief A (e.g., customer-support agent)**
  - [P] *Capstone A: Build, Deploy & Monitor a Support Agent End-to-End*
- **12.3 — Capstone brief B (e.g., coding/dev agent)**
  - [P] *Capstone B: Build, Deploy & Monitor a Coding Agent End-to-End*
- **12.4 — Capstone brief C (e.g., personal-finance agent)**
  - [P] *Capstone C: Build, Deploy & Monitor a Finance Agent End-to-End*
- **12.5 — Portfolio & interviews**
  - [T] *From Project to Job: Portfolio, Resume & Agent-Engineer Interview Prep*

---

## 13. Audience-flow evaluation (does each topic build on the last?)

A dependency check from the learner's seat — every module consumes only what
earlier modules already taught:

| Module | Needs (already taught) | Unlocks (used later) |
|---|---|---|
| 0 Cold-open | nothing (frameworks-free) | motivation + the loop shape |
| 1 NLP | 0 | embeddings → RAG (4), memory (5) |
| 2 LLMs | 1 (tokens/embeddings) | model control → every agent call |
| 3 Foundations | 2 (LLM control) | the loop → all later agents |
| 4 Tools/MCP/RAG | 3 (loop), 1 (embeddings) | tools/RAG → memory, multi-agent |
| 5 Memory | 4 (RAG/vectors), 2 (cost) | stateful agents (6) |
| 6 State/DAGs | 3 (loop), 5 (state) | routing → multi-agent (7) |
| 7 Multi-agent | 6 (graphs), 4 (tools) | systems to evaluate (8) |
| 8 Evaluation | 3–7 (something to test) | safe-to-ship gate (9–10) |
| 9 Security | 4 (tools), 8 (eval) | hardened app to deploy (10) |
| 10 Deployment | 9 (hardened), FastAPI | live system to monitor (11) |
| 11 Monitoring | 10 (live app) | feedback → capstone (12) |
| 12 Capstone | everything | portfolio |

**Strengths of this ordering**
- **Mental-model-first.** NLP → LLMs → agent loop means by Module 3 the learner
  understands *why* the loop works, not just how (matches "no black box").
- **The spiral spine works.** Every [P] video has a built-in callback to the
  previous Atlas state and a cliffhanger to the next — your retention engine.
- **Evaluation before deployment** is the correct production instinct and rare in
  courses; it sells the "production-grade" promise.

**Risks & recommended mitigations**
1. **Module 1 (NLP) is the retention danger zone** — 8 theory videos before a
   build. *Mitigation:* the Module 0 cold-open buys goodwill; keep 1.1–1.6 tight
   (10–15 min each), push the bonus math (1.7) to a clearly-optional track, and
   open each with a live "watch this break" micro-demo.
2. **Module 4 is the heaviest (Tools+MCP+RAG, ~8h).** *Consider* splitting RAG
   (4.5–4.6) into its own module later if analytics show drop-off — the chapter
   structure above already makes that a clean cut.
3. **LangGraph introduced in Module 6, but tools/loop built raw in 3–4.** This is
   *intentional and on-style* ("build from scratch, then reveal the framework"),
   but state it explicitly in 6.2 so framework-hungry learners don't feel it came
   late.
4. **Theory/Project decoupling must stay honest:** a [T] video must never depend
   on Atlas state, or it can't be repurposed to YouTube. Audit each [T] title
   above against §3.1 before scripting.

**Net:** the flow is sound and genuinely "one topic on top of another." The only
real intervention needed is protecting retention through the NLP module.
