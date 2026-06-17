# Interview Prep — Skill Gap Questions

> 5 questions targeting Ravi's biggest gaps from the match report. Each includes what the interviewer is really probing and a study pointer.

---

## Question 1: "Walk us through how you'd build a RAG pipeline from scratch for our customer support product."

**What they're really asking:** Do you understand retrieval-augmented generation end-to-end — not just the concept, but the engineering decisions (chunking, embedding, retrieval, prompt assembly, evaluation)?

**Why this targets Ravi:** Zero RAG experience on resume. This is the #1 skill gap for the role.

**Study pointer:**
- Build a minimal RAG demo: ingest documents → chunk → embed with OpenAI/Cohere → store in pgvector → retrieve top-k → pass to LLM with a system prompt
- Understand tradeoffs: chunk size, overlap, top-k vs. reranking, metadata filtering
- Read: LangChain RAG tutorial, Anthropic's "Building Effective Agents" guide

---

## Question 2: "How would you evaluate whether our LLM responses are good enough for production? What metrics would you track?"

**What they're really asking:** Can you think about AI systems operationally — not just "does it work in a demo" but how do you measure quality, detect regressions, and build feedback loops?

**Why this targets Ravi:** No LLM evaluation experience. JD explicitly requires "evaluation pipelines" and "feedback loops."

**Study pointer:**
- Learn: exact match, BLEU/ROUGE (limitations), LLM-as-judge, human eval sampling, A/B testing for prompts
- Understand production metrics: latency (p50/p95), token usage, cost per query, hallucination rate, user thumbs-up/down
- Tooling: LangSmith, Ragas, or a simple custom eval script with golden Q&A pairs

---

## Question 3: "Explain the difference between keyword search and vector/semantic search. When would you use each?"

**What they're really asking:** Ravi's resume mentions a keyword search tool — they want to know if he understands why AI products need embeddings and vector search, and whether his past work gives him a foundation to grow from.

**Why this targets Ravi:** His closest relevant experience (Flask search tool) uses keyword matching. They'll probe whether he understands the leap to semantic search.

**Study pointer:**
- Understand: TF-IDF/BM25 vs. embedding cosine similarity, why synonyms and paraphrases break keyword search
- Know vector DB options: pgvector (extension on PostgreSQL he already knows), Pinecone, Weaviate, ChromaDB
- Be ready to say: "My search tool used keyword matching — here's what I'd change to make it semantic and why"

---

## Question 4: "Describe how you'd design a production API that wraps an LLM call. What concerns would you handle that you wouldn't have with a regular REST API?"

**What they're really asking:** Can you apply your backend engineering experience to the unique challenges of LLM APIs — latency, streaming, token limits, cost, retries, caching, and fallbacks?

**Why this targets Ravi:** Strongest area (Flask REST APIs), but LLM APIs have different failure modes. They'll test if he knows the delta.

**Study pointer:**
- Learn: streaming responses (SSE), timeout handling for 30s+ LLM calls, token counting before sending, prompt caching, rate limiting, circuit breakers
- Understand: async patterns in FastAPI for concurrent LLM calls, response caching for identical queries
- Practice: wrap OpenAI API in a Flask/FastAPI endpoint with error handling, logging, and token usage tracking

---

## Question 5: "What are AI agents, and how do they differ from a simple LLM API call with a good prompt?"

**What they're really asking:** Do you understand agentic AI patterns (tool calling, ReAct loop, multi-step reasoning) that the JD lists as nice-to-have — and can you articulate when agents are worth the complexity?

**Why this targets Ravi:** No agentic AI experience. QuantumLeap builds "AI-powered customer support automation" which likely uses agent patterns.

**Study pointer:**
- Learn the loop: Think → Act (tool call) → Observe → repeat
- Understand: function calling / tool use in OpenAI and Anthropic APIs, ReAct prompting, when agents help vs. when a single RAG call suffices
- Build: a simple agent that can call 2-3 tools (e.g., search docs, check order status, escalate to human) using LangChain or raw API function calling
- Read: Anthropic "Building Effective Agents", OpenAI function calling docs

---

## Quick Study Plan (1–2 weeks before interview)

| Day | Focus | Deliverable |
|-----|-------|-------------|
| 1–2 | RAG pipeline end-to-end | Working demo with pgvector + OpenAI |
| 3 | Vector vs keyword search | Blog post or README explaining tradeoffs |
| 4–5 | LLM API wrapper with observability | FastAPI endpoint with logging, token tracking, error handling |
| 6 | LLM evaluation basics | 10 golden Q&A pairs with automated scoring |
| 7 | Agentic AI intro | Simple 2-tool agent demo |
| 8 | Review + mock answers | Practice answering all 5 questions out loud |
