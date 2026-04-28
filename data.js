// Phase data extracted from the curriculum
window.PHASE_COLORS = ["teal-deep", "teal", "purple", "pink", "emerald", "amber", "rust", "mustard", "indigo"];
window.ROADMAP = [
  {
    id: 1,
    title: "Python Foundations",
    short: "Python + Async Engineering",
    color: "teal-deep",
    weeks: "Weeks 1–3",
    weeksDetail: "3 weeks · 8 modules",
    difficulty: 2,
    summary: "Every agent framework runs on Python. Skip this and everything later breaks in mysterious ways.",
    endState: "You can build a FastAPI endpoint that calls three different LLMs in parallel, times out the slow one, and logs the result without blocking the response.",
    sections: [
      { n: "1.1", title: "Core Python", items: ["Variables, types, control flow", "Functions, *args/**kwargs, decorators", "List & dict comprehensions", "Generator expressions", "Type hints (you'll need these for Pydantic later)"] },
      { n: "1.2", title: "Object-Oriented Python", items: ["Classes, __init__, instance vs class methods", "Inheritance, encapsulation, polymorphism", "Dataclasses", "Pydantic models — every agent framework uses them for tool schemas"] },
      { n: "1.3", title: "Data Structures", items: ["List, Tuple, Set, Dict, NamedTuple", "collections.defaultdict, Counter, deque", "When to use which (interview territory)"] },
      { n: "1.4", title: "Error & File Handling", items: ["try/except/finally", "Custom exception classes", "Context managers (with, contextlib)", "Reading/writing JSON, CSV, plain text, binary"] },
      { n: "1.5", title: "Working with HTTP APIs", items: ["The requests library", "HTTP verbs, headers, status codes", "Authentication (Bearer tokens, API keys)", "Rate limits, retries, exponential backoff with tenacity"] },
      { n: "1.6", title: "Database Connectivity", items: ["psycopg2 for raw PostgreSQL", "SQLAlchemy ORM basics", "Connection pooling and why it matters under load", "Raw SQL when the ORM gets in the way"] },
      { n: "1.7", title: "FastAPI", items: ["First /chat endpoint", "Pydantic request/response models", "Dependency injection", "Automatic OpenAPI docs", "Running with uvicorn"] },
      { n: "1.8", title: "Async Programming", items: ["asyncio fundamentals — event loop, coroutines", "async/await syntax", "asyncio.gather for parallel LLM calls", "asyncio.wait_for for timeout protection", "asyncio.create_task for fire-and-forget logging"] }
    ]
  },
  {
    id: 2,
    title: "The Mental Model of an LLM",
    short: "LLM Mental Model",
    color: "teal",
    weeks: "Week 4",
    weeksDetail: "1 week · 5 modules",
    difficulty: 1,
    summary: "Conceptual phase. Almost no code. Where the brain-in-a-windowless-room analogy lives, and where most \"why is my agent broken\" questions get answered six months later.",
    endState: "You can explain to a non-technical PM why ChatGPT made up a fact, and tell a hiring panel which model to pick for which job — backed by benchmarks, not vibes.",
    sections: [
      { n: "2.1", title: "What an LLM actually is", items: ["Trained on a fixed snapshot", "Knowledge cutoff dates and what they imply", "Probabilistic generation, not retrieval", "Why the same prompt gives different outputs"] },
      { n: "2.2", title: "How an LLM thinks", items: ["BPE tokenization — why \"hello\" is 1 token but \"antidisestablishmentarianism\" is 6", "Context windows — what fits, what gets silently truncated", "Sampling parameters: temperature, top-p, top-k — when to set what", "Transformer at 30,000 feet — attention preserves position, no math, no multi-head diagrams", "Why long context degrades (\"lost in the middle\")"] },
      { n: "2.3", title: "Reasoning models vs base models", items: ["The 2025 split: o1 / o3, Claude 3.7 thinking, Gemini 2.5 thinking, DeepSeek R1, Qwen QwQ", "What \"thinking tokens\" actually are and why they're billed", "When reasoning models are worth the latency and cost", "Reasoning effort knobs (low / medium / high) and how to budget them", "When a base model + good prompting beats a thinking model"] },
      { n: "2.4", title: "Reading model evals & benchmarks", items: ["The benchmarks worth knowing — MMLU, GSM8K, HumanEval, SWE-bench, GPQA, MMMU, BFCL (function calling)", "Why benchmarks lie — contamination, prompt sensitivity, eval gaming", "How to read a leaderboard skeptically (LMArena, Artificial Analysis, Vellum, Aider)", "Building your own micro-eval for the task you actually care about"] },
      { n: "2.5", title: "Comparing the major models", items: ["GPT family, Claude family, Gemini, Llama, Mistral, DeepSeek, Qwen", "Cost vs quality vs speed vs context-length tradeoffs", "When model choice matters vs when it really doesn't"] }
    ]
  },
  {
    id: 3,
    title: "Prompt Engineering & API Access",
    short: "Prompt Engineering",
    color: "purple",
    weeks: "Weeks 5–7",
    weeksDetail: "3 weeks · 7 modules",
    difficulty: 2,
    summary: "The pivot from \"ChatGPT user\" to \"engineer who controls LLMs.\"",
    endState: "You can take a flaky prompt that works \"sometimes\" and systematically make it reliable — and cut its cost in half with caching while you're at it.",
    sections: [
      { n: "3.1", title: "UI vs API — the hinge moment", items: ["Same prompt, same model, different output — why?", "System prompts you don't see", "Skills/tools the chat UI calls silently", "Why production work happens via API"] },
      { n: "3.2", title: "Calling LLMs via API", items: ["OpenAI SDK, Anthropic SDK", "Message format (system / user / assistant)", "Streaming responses", "Structured output (JSON mode, tool-call schemas, XML tags)"] },
      { n: "3.3", title: "Prompt anatomy", items: ["System prompt vs user turn vs assistant prefill", "Role and persona assignment", "Positive framing over negative constraints", "Markdown vs XML structure"] },
      { n: "3.4", title: "Core techniques", items: ["Zero-shot", "Few-shot with curated examples", "COSTAR framework (Context, Objective, Style, Tone, Audience, Response)", "Iterative refinement loop"] },
      { n: "3.5", title: "Applied prompt patterns", items: ["Extraction (entities, dates, relationships)", "Classification (intent, sentiment, routing)", "Transformation (summarize, translate, reformat)", "Generation (reports, SQL, code)", "Decomposition (break complex queries into sub-prompts)"] },
      { n: "3.6", title: "Advanced reasoning techniques", items: ["Chain of Thought — \"think step by step\"", "Self-Consistency — sample multiple paths, majority vote", "Self-Refine — generate, critique, refine loop", "Least-to-Most — decompose hard problems into ordered sub-problems", "Tree of Thought (research-flavoured; mention but don't drill)"] },
      { n: "3.7", title: "Prompt management & cost in production", items: ["Versioning prompts in code vs as managed resources", "A/B testing prompt variants", "AWS Bedrock Prompt Management for the lifecycle without code deploys", "Prompt caching — Anthropic cache_control and OpenAI's automatic cached input pricing (5–10× cost cuts on long system prompts)", "DSPy — programmatic prompt optimisation when you want the framework to tune your prompts for you (mention; depth is optional)"] }
    ]
  },
  {
    id: 4,
    title: "RAG + Evaluation",
    short: "Ingestion Pipeline + RAG",
    color: "pink",
    weeks: "Weeks 8–12",
    weeksDetail: "5 weeks · 9 modules",
    difficulty: 4,
    capstone: 1,
    summary: "The longest phase. RAG looks simple in tutorials and is brutal in production.",
    endState: "You can build a RAG system, measure why it's wrong, and fix it with data instead of vibes.",
    sections: [
      { n: "4.1", title: "Why RAG exists", items: ["LLMs can't see your private data", "The brain-in-a-windowless-room reaches its limit", "Use cases: internal docs, company policies, recent data"] },
      { n: "4.2", title: "Embeddings", items: ["What an embedding actually is (vector in N-dim space)", "Cosine similarity, dot product, Euclidean distance", "Embedding models — Titan Multimodal, SentenceTransformer, OpenAI ada/text-embedding-3, Cohere", "Choosing dimensions vs cost"] },
      { n: "4.3", title: "Document ingestion pipeline", items: ["Layout identification with Docling (headers, paragraphs, tables, code blocks, formulas)", "Serialization to structured objects", "Why PyMuPDF alone fails on complex PDFs"] },
      { n: "4.4", title: "Chunking strategies", items: ["Fixed-width chunking and why it breaks", "Semantic chunking by structure", "Overlap windows", "Parent-child chunking", "Late chunking — embed first, chunk later — preserves context across boundaries", "Chunk size vs retrieval quality tradeoff"] },
      { n: "4.5", title: "Chunk enrichment", items: ["PII detection and redaction", "NER for entities", "Key-phrase extraction", "Metadata for hybrid search"] },
      { n: "4.6", title: "Vector databases", items: ["Pinecone, Weaviate, pgvector", "Chroma for local dev", "S3 Vector Buckets, OpenSearch", "HNSW vs IVF indexes", "Decision matrix: managed (Pinecone) vs self-hosted (Weaviate, Qdrant) vs in-process (Chroma, FAISS) vs already-in-your-stack (pgvector)"] },
      { n: "4.7", title: "Hybrid retrieval & next-gen retrievers", items: ["Vector search + BM25 keyword", "Reranking with cross-encoders (Cohere Rerank, BGE)", "Metadata filtering", "Query expansion", "Late-interaction retrievers — ColBERT (text), ColPali (multimodal/PDF pages as images) — when they beat dense retrieval and what they cost"] },
      { n: "4.8", title: "Graph-augmented RAG", items: ["Neo4j basics", "Cypher query language", "When graph relationships beat pure vector search", "Multi-hop queries"] },
      { n: "4.9", title: "RAG evaluation — the part most courses skip", items: ["LLM-as-judge: RAG Triad — Faithfulness, Context Relevance, Answer Relevance", "Deterministic retrieval metrics: Precision@k, Recall@k, F1, Hit Rate@k, MRR, NDCG@k", "Tooling: Ragas (the de-facto eval framework), MLflow for run logging, LangSmith for tracing", "Golden datasets: Q&A pairs with expected chunks, regression testing on every code change"] }
    ]
  },
  {
    id: 5,
    title: "Tools, MCP, and Single Agents",
    short: "Tools, MCP & Single Agents",
    color: "emerald",
    weeks: "Weeks 13–16",
    weeksDetail: "4 weeks · 8 modules",
    difficulty: 4,
    summary: "The brain gets hands and legs.",
    endState: "You can build a single agent that searches the web, reads internal docs, queries a DB, and emails you a summary — and stops if it tries to do something dumb.",
    sections: [
      { n: "5.1", title: "Function calling / tool use", items: ["Tool schemas (JSON Schema, Pydantic)", "How the LLM decides which tool to call", "Parsing tool-call responses", "Handling tool errors gracefully"] },
      { n: "5.2", title: "Tool design principles", items: ["One tool, one job", "Clear docstrings — the LLM reads them", "Return structured data, not free text", "Fallbacks inside tools, not in the agent"] },
      { n: "5.3", title: "MCP — Model Context Protocol", items: ["What MCP is and why it exists (universal adapter for tools)", "MCP servers vs MCP clients", "Using existing MCP servers (filesystem, GitHub, Slack)", "Building your own MCP server", "stdio vs HTTP transports", "MCP is moving fast — bookmark modelcontextprotocol.io and re-read the spec every few months; the registry, auth model, and resource semantics are still evolving"] },
      { n: "5.4", title: "The ReAct pattern", items: ["Reasoning + Acting loop", "Thought → action → observation → thought", "Why \"thinking\" models exist", "When to force ReAct vs let the model decide"] },
      { n: "5.5", title: "LangChain agents", items: ["create_agent — model + tools + middleware + store", "@tool(parse_docstring=True) for auto schemas", "Parallel tool execution with asyncio.gather", "Structured outputs via Pydantic"] },
      { n: "5.6", title: "Human in the loop", items: ["HumanInTheLoopMiddleware for sensitive operations", "Checkpointers and InMemorySaver", "Resume flows after human approval", "When to pause (DB writes, payments, emails)"] },
      { n: "5.7", title: "Tool security", items: ["Retrieval Sanitiser — strip injection patterns from tool results", "Read-only DB enforcement", "Max retries per tool", "Timeouts on every external call"] },
      { n: "5.8", title: "Computer use & app SDKs — agents with eyes and a mouse", items: ["Anthropic Computer Use — agent takes screenshots and drives a desktop/browser", "OpenAI Operator / Apps SDK — agent runs inside ChatGPT or controls a browser tab", "Browser-automation agents (Playwright + LLM, browser-use, Stagehand)", "When this is the right tool vs API integration", "Sandboxing, audit trails, and \"are you sure?\" gates — these agents can do real damage"] }
    ]
  },
  {
    id: 6,
    title: "Memory & Context Engineering",
    short: "Memory + Context Engineering",
    color: "amber",
    weeks: "Weeks 17–19",
    weeksDetail: "3 weeks · 7 modules",
    difficulty: 4,
    difficultyNote: "Advanced — but the highest-leverage skill in the whole curriculum.",
    summary: "The hardest conceptual phase. Easy to do badly, expensive when you do. Worth every hour of attention.",
    endState: "You can explain why your agent forgot what you said three turns ago, and fix it with the right memory layer instead of throwing more tokens at it.",
    sections: [
      { n: "6.1", title: "The context window as working memory", items: ["Why agents \"forget\" mid-conversation", "Token budgeting per section", "The lost-in-the-middle problem", "Recency bias"] },
      { n: "6.2", title: "Context structure — SYSTEM / CONTEXT / USER separation", items: ["What goes where", "@dynamic_prompt patterns", "Structural separation as a security defence against prompt injection", "Token budgets per section (e.g. SYSTEM=instructions, CONTEXT=retrieved data, ~2000 tokens each)"] },
      { n: "6.3", title: "Short-term memory — session history", items: ["Sliding window of last N turns", "Message-pair preservation (don't split user from assistant)", "When to keep tool calls in history vs strip them"] },
      { n: "6.4", title: "Semantic caching", items: ["FAISS IndexFlatIP for sub-millisecond cosine search", "Similarity thresholds (0.97 high-stakes, 0.88 general Q&A)", "Cache HIT skips everything downstream", "Daemon-thread writes so cache never blocks response"] },
      { n: "6.5", title: "Episodic memory", items: ["LangChain's InMemoryStore", "LLM tags answers as EPISODIC: YES/NO so the model decides what's worth remembering", "Episodic hits enrich CONTEXT only — tools and LLM still run"] },
      { n: "6.6", title: "Context compression", items: ["Trigger threshold (>3000 tokens)", "Keep last 10 messages verbatim", "LLM summarises the rest into a single compressed entry", "When compression destroys information"] },
      { n: "6.7", title: "Long-term memory", items: ["User profiles, preferences, facts to persist", "Vector stores vs structured stores", "Managed memory layers — mem0 (open-source) and Zep (managed) — when to skip building this yourself", "When memory becomes a privacy problem (GDPR, right-to-be-forgotten flows)"] }
    ]
  },
  {
    id: 7,
    title: "Multi-Agent Orchestration",
    short: "Multi-Agent Orchestration",
    color: "rust",
    weeks: "Weeks 20–22",
    weeksDetail: "3 weeks · 8 modules",
    difficulty: 5,
    capstone: 2,
    summary: "When one agent isn't enough.",
    endState: "You can design a multi-step agent workflow on a whiteboard, build it in LangGraph, and debug it when one node loops infinitely.",
    sections: [
      { n: "7.1", title: "When to go multi-agent (and when not to)", items: ["Single-agent-with-tools beats multi-agent for ~80% of tasks", "Multi-agent earns its weight when steps need different prompts, tools, or specialised reasoning", "The Tableau→QuickSight conversion case as a worked example"] },
      { n: "7.2", title: "LangGraph fundamentals", items: ["Nodes, edges, state", "StateGraph and reducers", "Conditional edges and routing", "Cycles and termination conditions"] },
      { n: "7.3", title: "Common patterns", items: ["Supervisor + workers", "Sequential pipeline", "Parallel fan-out / fan-in", "Plan-and-execute", "Reflection loops"] },
      { n: "7.4", title: "Agent-as-tool — the lightweight alternative", items: ["Wrap a sub-agent behind a normal @tool interface", "Parent agent calls it like any other function — no graph, no state plumbing", "When this beats LangGraph (clear hierarchy, no shared state, deterministic flow)", "Composing specialist agents (researcher, summariser, critic) without orchestration overhead"] },
      { n: "7.5", title: "State management", items: ["Typed state with Pydantic", "What to put in state vs context", "Checkpointers for resumability (MemorySaver, SqliteSaver, PostgresSaver)"] },
      { n: "7.6", title: "A2A — Agent-to-Agent Protocol", items: ["Agent discovery and capability cards", "Cross-framework delegation", "When A2A beats just calling another function"] },
      { n: "7.7", title: "Frameworks compared (briefly)", items: ["LangGraph (most mature)", "CrewAI (simpler, opinionated)", "AutoGen (Microsoft)", "Pydantic AI (typed, FastAPI-flavoured ergonomics)", "OpenAI Swarm / its successor — minimal handoff-style orchestration", "Custom orchestration with raw asyncio", "Pick one and stick with it"] },
      { n: "7.8", title: "Debugging multi-agent systems", items: ["LangSmith tracing", "Why your agents are talking past each other", "Cycles that won't terminate", "Cost explosions"] }
    ]
  },
  {
    id: 8,
    title: "Guardrails & LLMOps",
    short: "Guardrails + LLMOps",
    color: "mustard",
    weeks: "Weeks 23–24",
    weeksDetail: "2 weeks · 4 modules",
    difficulty: 3,
    summary: "You know what to build. Now make it not embarrass you in production — measure failure, catch it before users do, and prove the agent is improving release-over-release.",
    endState: "You can put a number on how often your agent fails, and ship it anyway with confidence.",
    sections: [
      { n: "8.1", title: "Three-layer guardrail architecture", items: ["Input Guardrails (gateway, <1ms, deterministic): prompt-injection regex, PII redaction, out-of-domain rejection, toxic filter — code-based, never LLM", "Output Guardrails (LLM-judge OK): faithfulness, contradiction check, medical/legal disclaimers when confidence < threshold, hard-fail to safe fallback", "Action Guardrails (inside tools, pure functions): max retries, max tool calls per request, query validation, read-only DB, top_k caps"] },
      { n: "8.2", title: "AWS Bedrock Guardrails", items: ["Contextual grounding", "Automated reasoning checks", "Harmful content filtering", "Topic blocking", "When managed guardrails are enough vs custom"] },
      { n: "8.3", title: "LLMOps — observability", items: ["LangSmith / LangFuse for traces", "Token cost dashboards", "Latency percentiles (p50, p95, p99)", "Failure rate by tool, by route, by model"] },
      { n: "8.4", title: "LLMOps — evaluation in production", items: ["Golden dataset regression tests in CI", "A/B testing prompt and model changes", "Feedback loops from user thumbs-up/down", "Drift detection on retrieval quality"] }
    ]
  },
  {
    id: 9,
    title: "Cloud Infrastructure & Deployment",
    short: "Cloud + Deployment",
    color: "indigo",
    weeks: "Weeks 25–26",
    weeksDetail: "2 weeks · 6 modules",
    difficulty: 3,
    capstone: 3,
    summary: "The final mile. Minimum AWS to make everything earlier deployable, plus how to actually put an agent in production and keep costs sane.",
    endState: "You can take any system you built in earlier phases, dockerize it, deploy to ECS Fargate behind API Gateway, manage secrets, stream tokens to a chat UI, load-test it, and watch the cost dashboard move only when it should.",
    sections: [
      { n: "9.1", title: "Storage & data", items: ["S3 — durable object storage, document lakes", "RDS PostgreSQL — managed relational DB for agent state", "DynamoDB — KV state for ingestion pipelines"] },
      { n: "9.2", title: "Compute", items: ["Lambda — serverless event-driven flows", "ECS Fargate — serverless containers for long-running agents", "ECR — container registry"] },
      { n: "9.3", title: "Networking & access", items: ["VPC, subnets, security groups (just enough not to break)", "IAM roles and policies", "API Gateway for exposing endpoints"] },
      { n: "9.4", title: "AI-specific services (and other clouds)", items: ["AWS Bedrock — managed foundation models", "AWS AgentCore — production agent infrastructure", "Bedrock embeddings", "Equivalents on other clouds: GCP Vertex AI (Model Garden, Agent Builder) and Azure AI Foundry (model catalog, prompt flow) — same primitives, different SKUs"] },
      { n: "9.5", title: "Deployment & realtime delivery", items: ["Dockerizing FastAPI agents", "ECS Fargate task definitions", "API Gateway + ALB routing", "Secrets management with AWS Secrets Manager", "Environment promotion (dev → staging → prod)", "Streaming responses to chat UIs — SSE for one-way token streaming, WebSockets when you also need client → server messages mid-stream"] },
      { n: "9.6", title: "Cost & capacity control", items: ["Semantic cache HIT rate as a KPI", "Model routing — cheap model for simple queries, expensive for complex", "Prompt compression", "Max-tokens caps", "Load testing with locust or k6 — agents fall over under concurrency long before the LLM does; rate-limit at the gateway, not the model"] }
    ]
  }
];

window.CAPSTONES = [
  {
    n: 1,
    title: "Distributed Document Ingestion + RAG Pipeline",
    phase: "Built during Phase 4 · Weeks 10–12",
    domain: "Unstructured document Q&A (legal, pharma, technical docs)",
    build: [
      "PDF ingestion: Docling layout detection → semantic chunking → PII redaction → entity extraction → embeddings → Pinecone + Neo4j",
      "Distributed async workers on ECS Fargate processing thousands of PDFs concurrently",
      "DynamoDB state tracking per document (queued / processing / done / failed)",
      "Hybrid retrieval (vector + BM25 + graph) with reranking",
      "Evaluation harness with golden dataset, Precision@k / Recall@k / RAG Triad",
      "FastAPI Q&A endpoint with citation-backed answers"
    ],
    stack: ["Docling", "Pinecone", "Neo4j", "ECS Fargate", "DynamoDB", "S3", "Bedrock embeddings", "LangSmith"],
    proves: "You can build production RAG, not a Streamlit demo."
  },
  {
    n: 2,
    title: "Multi-Agent Natural Language → SQL on E-commerce Data",
    phase: "Built during Phase 7 · Weeks 21–22",
    domain: "E-commerce analytics for non-technical users",
    build: [
      "Multi-agent: Planner → SQL Writer → Validator → Executor → Explainer",
      "Schema-aware context injection per query (only relevant tables sent to writer)",
      "LangGraph orchestration with conditional routing and retry loops",
      "Read-only DB enforcement, query timeout, max-row caps",
      "Streamlit frontend, FastAPI backend, RDS PostgreSQL with realistic data",
      "Benchmarked on a golden NLQ test set, target 85%+ accuracy"
    ],
    stack: ["LangChain", "LangGraph", "LangSmith", "AgentCore", "RDS PostgreSQL", "FastAPI", "Streamlit", "Bedrock"],
    proves: "You can orchestrate multiple specialised agents safely against real production data."
  },
  {
    n: 3,
    title: "Clinical Trials Knowledge Base",
    phase: "Built during Phases 8–9 · Weeks 23–26",
    domain: "Life sciences AI (substitute legal, finance, or your industry)",
    build: [
      "Real ClinicalTrials.gov dataset ingestion (or your domain equivalent)",
      "Hybrid knowledge layer: Pinecone for unstructured PDFs + Neo4j for trial-drug-condition relationships",
      "Multi-hop relationship queries (\"what other trials used drug X for condition Y?\")",
      "Full three-layer guardrails — disclaimer auto-injection, contradiction checks, action limits",
      "Evidence-backed answers — every claim cites the source chunk",
      "Deployed on AWS with monitoring, regression tests in CI, semantic cache, cost dashboard"
    ],
    stack: ["LangChain", "LangGraph", "Neo4j + Cypher", "Pinecone", "Bedrock + AgentCore + Lambda", "S3", "LangSmith", "MLflow"],
    proves: "You can ship an agent into a regulated domain without it killing anyone (or your career)."
  }
];

window.OUT_OF_SCOPE = [
  {
    title: "Fine-tuning foundation models",
    why: "RAG, prompting, and tool use solve 95% of business problems faster, cheaper, and with no infra overhead. Fine-tuning earns its weight only when you have a narrow domain, lots of clean labelled data, and prompting has hit a wall — which almost never happens before you've shipped your first agent. Learn it after this roadmap, not during.",
    pointer: "Start with LoRA + a 7B open model (Llama, Mistral, Qwen) on a single A10/L4 once you have a real motivating use case."
  },
  {
    title: "Voice agents",
    why: "A whole sub-discipline — STT, TTS, turn-taking, latency budgets, barge-in. Worth its own track, not a side note. You can graft it on top of any agent you build in this roadmap.",
    pointer: "OpenAI Realtime API, Deepgram + ElevenLabs + LiveKit, or pipecat — pick after you've shipped one text agent."
  },
  {
    title: "ML fundamentals (gradient descent, backprop, transformers from scratch)",
    why: "Lovely to know. Not required to be an excellent agent engineer in 2026. The Karpathy series is there when you're curious — don't let it block you from shipping.",
    pointer: "Andrej Karpathy's \"Neural Networks: Zero to Hero\" + the \"Let's build GPT\" video, on weekends."
  },
  {
    title: "Frontend frameworks (Next.js, React, Tailwind)",
    why: "You need enough to ship a Streamlit or basic chat UI for capstones. Beyond that, partner with a frontend engineer or a design system. Don't get lost in framework wars.",
    pointer: "Streamlit for internal tools, Vercel AI SDK + Next.js when you need a real product UI."
  }
];

window.NEXT_STEPS = [
  {
    label: "Portfolio",
    title: "Three repos, three READMEs, one demo video each",
    body: "The capstones are your portfolio. For each one: a clean GitHub repo with a README that explains the problem, the architecture, the trade-offs, and the eval numbers; a 90-second Loom walking through it; one screenshot of the trace UI showing it actually working."
  },
  {
    label: "LinkedIn",
    title: "Headline that says what you can ship",
    body: "Don't write \"AI Engineer\" in your headline — write \"AI Engineer · production RAG, multi-agent systems, AWS Bedrock + LangGraph · shipping in regulated domains.\" Specific gets interviews. Generic gets ignored."
  },
  {
    label: "60-second pitch",
    title: "What to say in the first interview round",
    body: "\"I spent six months building three production-grade AI systems end-to-end: a distributed RAG pipeline that ingests thousands of PDFs, a multi-agent NL→SQL system with read-only enforcement, and a clinical-trials knowledge base with three-layer guardrails. I can show you the traces, the eval numbers, and the cost dashboard for any of them.\" That's the whole pitch. Numbers and artefacts beat adjectives."
  },
  {
    label: "Keep learning",
    title: "What to read once you're shipping",
    body: "Anthropic's \"Building effective agents\" essay, the Latent Space podcast, the LangChain blog, Eugene Yan's writing on production ML, and the original papers when something keeps confusing you (Self-RAG, RAG-as-judge, ReAct). Skim, don't drown."
  }
];
