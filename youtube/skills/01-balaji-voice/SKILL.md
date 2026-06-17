---
name: balaji-voice
description: Encodes Balaji Chippada's on-camera voice — direct address (no "guys"), Telugu delivery with English technical terms, signature phrases ("no black box", "step by step", "real time, in production"), and the anti-pattern blocklist. Use when writing any script line that will be spoken on camera, captioned, or burned into a video.
---

# Balaji Voice

This skill defines how Balaji Chippada speaks on camera. Apply it to every spoken line, every caption, every title card, every Telugu-delivered tutorial. The goal is one consistent voice across 60+ Roadmap-2026 videos.

## The Voice in One Sentence

> A senior AI engineer working remote-from-Netherlands for a Swiss telecom, talking *directly* to *one* viewer — usually a stuck IT pro, fresher, or upskilling engineer — about how to actually build production-grade Agentic AI, with no jargon-translation tricks and no framework worship.

## Address Rules

| Rule | Yes | No |
|---|---|---|
| Audience address | `you`, `nuvvu` (Telugu singular "you"), direct second-person | `guys`, `you guys`, `everyone`, `folks`, `viewers` |
| Inclusive teaching | `manam` (we), `let's`, `we'll see` | royal "we", "one might say" |
| Self-reference | `I`, `nenu` — confident, first-person | "this video will...", passive constructions |

The viewer is **one person**, not a crowd. Write as if recording a 1:1 voice memo to a friend who asked for help.

## Language Split (Telugu delivery, English content)

All written deliverables — scripts, slides, code, GitHub READMEs, captions, on-screen text — are **English**. The on-camera delivery is **Telugu** with English technical terms preserved.

### English-only terms (never Telugu-translate, never accent-swap)

- All library / framework / service names: `LangChain`, `LangGraph`, `Pinecone`, `pgvector`, `AWS Bedrock`, `Docling`, `FastAPI`, `pydantic`, `tenacity`
- All technical concepts: `agent`, `embedding`, `RAG`, `chunking`, `retrieval`, `tool calling`, `context window`, `tokenization`, `vector database`, `system prompt`, `temperature`, `inference`
- All cloud / infra terms: `S3`, `Lambda`, `IAM`, `endpoint`, `deployment`, `container`
- Code, error messages, log lines: read in English exactly as written
- Numbers and metrics: `cosine similarity`, `top-k`, `MMLU`, `latency`, `p99`

### Telugu is welcome for

- Connectors, transitions, comprehension checks, intuition framing, encouragement
- Real-life analogies and stories
- Emotional beats (the friend-laid-off story, the goosebumps moment)

The skill does not prescribe specific Telugu phrases. The instructor delivers in his natural Telugu; this skill only protects English terms from being translated.

## Signature Phrases (use deliberately, not on every video)

These are the **three** locked promise-phrases. They are part of the brand. Use one per video, not all three:

1. **"No black box."** — Use when introducing a framework or abstraction. Promises that the video will demystify it from scratch.
2. **"Step by step."** — Use when starting a build / walkthrough. Promises pacing.
3. **"In real time, in production."** — Use when contrasting tutorials against reality. Promises stakes.

Do NOT manufacture other catchphrases. Do NOT repeat all three in one video. Do NOT say them in the first 5 seconds — earn them by demonstrating them first.

### Phrases that DO NOT belong (extracted from SRTs but explicitly dropped)

- `guys` — removed everywhere
- `trust me guys` — removed
- `literally` as filler — use only when something is literally true
- `as if I'm explaining to my own brother` — keep only for the rare deeply personal motivational video, not in tutorials
- `200% effort from my side` — used once in the channel announcement, not a recurring catchphrase

## Opener Rotation (5 patterns, choose by video type)

The opener is decided per video, not by default. Match opener to video type:

| Video type | Default opener pattern | Example seed |
|---|---|---|
| Tutorial (roadmap phase) | **Live demo first** | "Watch this. *[runs the agent]* That's what we're building today." |
| Career / motivational | **Personal story** | "Last month a working pro with 8 years experience messaged me on LinkedIn..." |
| Industry news reaction | **Shock statistic** | "OpenAI just dropped a model that breaks 70% of existing RAG pipelines. Here's why." |
| Q&A / clarification | **Comment callback** | "A lot of you asked the same question after the last video. So let me answer it properly." |
| Project walkthrough | **Production incident** | "This system was running fine for 3 weeks. Then one user typed a single emoji and it crashed at 3 AM." |

The hook MUST land in **<30 seconds**. No "hey, welcome to my channel". No "in this video we'll cover". No throat-clearing.

## Sentence-Level Rules

| Do | Don't |
|---|---|
| Short, declarative sentences | Long compound sentences with three "and"s |
| Concrete numbers (`28 out of 100`, `47 times`, `3 LPA`) | Vague intensifiers (`a lot`, `huge`, `massive`) |
| Name the specific tool / company / version | Say `some library` or `there are tools that` |
| Show a real failure, then fix it | Hide errors, only show success |
| Use `I`, `you`, `we` (active voice) | `One can`, `it is recommended` (passive) |

## Honesty Markers (build trust)

Use these explicitly when applicable. They are part of the voice:

- **"I'm simplifying here."** — when collapsing detail to teach intuition
- **"This breaks in production. Here's why."** — when the demo is fragile
- **"In 2020 I'd say X. In 2026 it's outdated."** — when teaching what changed
- **"I don't know, let me check."** — on live sessions, when you don't know

## Energy / Tone Per Video Type

Tone evolves over time. As of channel-launch:

| Video type | Tone mix |
|---|---|
| Tutorial | Calm + technical confidence + "no black box" patience |
| Motivational / career | Warm + grateful + opinionated about industry |
| Job market take | Urgent + assertive + slightly intense ("the kid took the job") |
| Shorts | Punchy + 1-idea + provocative |
| Live doubts | Patient + collaborative + thinking-out-loud |

Update this table per quarter as analytics reveal which mix retains best.

## Anti-Pattern Blocklist (hard fails)

Reject any draft that contains:

- [ ] Greeting opener (`hey guys`, `hello everyone`, `welcome to my channel`)
- [ ] Generic preview (`in this video we'll cover...`)
- [ ] Translated technical jargon (`vector database` rendered fully in Telugu)
- [ ] Passive `one might`, `it is recommended`
- [ ] Clickbait promise the body doesn't deliver
- [ ] Paid product pitch in first 2 minutes (per `09-monetization-runway/`)
- [ ] Toy-only example with no production note
- [ ] Hidden errors / happy-path-only walkthrough
- [ ] Framework-first explanation (always build-from-scratch first)

## Quick Quality Pass (before recording)

Read the script aloud. For each line ask:

1. Am I talking to **one person**?
2. Did I keep technical terms in English?
3. Is there a concrete number, tool name, or example?
4. Is this sentence shorter than 18 words?
5. If I cut this line, would the video lose anything?

If line fails 5, cut it.
