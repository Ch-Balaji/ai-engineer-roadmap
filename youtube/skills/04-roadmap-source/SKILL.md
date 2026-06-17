---
name: roadmap-source
description: Treats data.js (the 9-phase Roadmap-2026 curriculum) as the single source of truth for every video. Enforces phase mapping, prerequisite checks, and prevents teaching advanced concepts before foundations. Use when planning any video, deciding video order, or auditing whether a video belongs in the channel.
---

# Roadmap-as-Source

The repo's `site/data.js` defines 9 phases and ~60 sections. Every published video must map to a specific phase + section. This skill enforces that mapping.

## The 9 Phases (snapshot)

| # | Phase | Weeks | Difficulty |
|---|---|---|---|
| 1 | Python Foundations | 1–3 | 2 |
| 2 | Mental Model of an LLM | 4 | 1 |
| 3 | Prompt Engineering & API Access | 5–7 | 2 |
| 4 | RAG + Evaluation (capstone) | 8–12 | 4 |
| 5 | Tools, MCP, and the Agent Loop | (continues from site/data.js) | varies |
| 6 | Memory Architecture | varies | varies |
| 7 | Context Engineering | varies | varies |
| 8 | Multi-Agent Orchestration (capstone) | varies | varies |
| 9 | Guardrails & Production Deployment (capstone) | varies | varies |

(Read `site/data.js` directly for the authoritative section list — it can change.)

## Mapping a Video to the Roadmap

For every video, fill this header at the top of its script:

```
ROADMAP MAPPING
- Phase: 4 — RAG + Evaluation
- Sections covered: 4.3 (Document ingestion), 4.4 (Chunking strategies)
- Prerequisites needed: 4.1 (Why RAG), 4.2 (Embeddings), 1.7 (FastAPI)
- Prerequisite videos: V12, V13, V07
- Capstone contribution: yes — feeds Capstone 1 (Distributed Document Ingestion)
```

If a draft video doesn't fit any phase + section: STOP. Either reshape it to fit, or add it to the off-roadmap "Bonus" list (industry news, motivational, career — these don't need a roadmap mapping).

## Prerequisite Check (hard rule)

Before teaching a section, the prerequisite sections MUST already have a published video.

Examples of forbidden orderings:

- ❌ Video on "Late chunking" (4.4) before "Embeddings" (4.2) is published
- ❌ Video on "Tool calling" (Phase 5) before "Calling LLMs via API" (3.2)
- ❌ Video on "Context window management" (Phase 7) before "BPE tokenization & context" (2.2)

If a viewer can hit "play" on the new video without prerequisite knowledge gained from prior videos, the video order is wrong.

## Bonus / Off-Roadmap Videos

Some videos don't map to a phase. They're still published, but they live in a separate playlist:

| Type | Examples | Playlist |
|---|---|---|
| Career / motivational | "Why I left mainframes", "8 years in AI summarized" | "Career Path" |
| Industry news reaction | "GPT-5 dropped — what changes for agents", "Claude 4 vs Gemini 3" | "Industry Pulse" |
| Job market take | "The kid took the senior's job", "Stop learning ML in 2026" | "Job Market Reality" |
| Interview prep | "AI engineer system design interview", "Resume teardown" | "Interview Prep" |
| Tools / setup | "My agent dev setup", "Best models for coding in 2026" | "Setup & Tools" |

Bonus videos do NOT need a phase mapping but DO need a clear viewer-purpose statement.

## Phase Breakdown Heuristics (deciding video count per phase)

This skill *decides* how many videos a phase becomes, based on depth signals from `site/data.js`:

| Signal | Outcome |
|---|---|
| Phase has 8+ sections | Each section becomes its own 15–25 min tutorial |
| Phase has 5–7 sections | Group sections into 3–5 tutorials by theme |
| Phase has fewer than 5 sections, low difficulty | Single 25-min tutorial covering the whole phase |
| Phase has a `capstone: 1` flag | Reserve a final "Capstone Build" video at the end of the phase, separate from section tutorials |
| Multiple sections share an obvious dependency chain | Build a 2–3 video mini-series that resolves a single end-to-end problem |

Always end each phase with a **"Phase N Recap + What's Next"** video (5–8 min, light edit). This is required, not optional. It anchors the binge-watch flow.

## Cross-Phase Bridges (cliffhanger discipline)

The end of every phase's tutorials must tease the next phase. The start of the next phase's first tutorial must resolve that tease.

Phase ending example:

> "We built a working RAG pipeline. It retrieves the right chunk 78% of the time. But here's the problem — when we ask it a question that requires *acting* on the data (booking a meeting, sending an email, updating a database), retrieval alone fails. Next phase: tools, MCP, and the agent loop."

Phase 5 opening callback:

> "Last phase, we built a RAG system that retrieves data. Today, we're going to give it the ability to *act* — to call APIs, run code, update systems. This is where 'chatbot' becomes 'agent'."

## Cross-Linking in the Video & Description

Every tutorial video's description includes:

```
🗺️ Where this fits in the Roadmap:
Phase {N} — {Phase Title}
Section(s): {list}
Prerequisite videos: {V## titles + links}
Next video: {V## title + link}
Full Roadmap: {link to site/Roadmap.html}

📂 Code:
GitHub repo: {link to per-video repo}
```

In-video, around minute 1, briefly cite the roadmap position: *"This is Phase 4, section 4.3 — document ingestion."* One line, then move on.

## When site/data.js Changes

If a section is renamed, split, merged, or reordered:

1. Old videos covering the changed section get a **pinned comment** linking to the updated section name.
2. The video description gets updated with the new section reference.
3. The roadmap site is updated first; videos follow within a week.
4. Major reorderings (a phase moves) trigger a "Roadmap update" video explaining what changed and why.

## Quality Pass

Before publishing:

- [ ] Video has a phase + section mapping in its script
- [ ] All prerequisite videos exist and are linked
- [ ] In-video citation of phase + section happens once, briefly
- [ ] Description includes the roadmap-mapping block
- [ ] If this is a phase's last tutorial, a recap video is queued
- [ ] If this teases the next phase, the next phase's opener already plans the callback
