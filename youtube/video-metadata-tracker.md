# Per-Video Metadata Tracker — Roadmap 2026

This file tracks every published video's title, description, tags, links, and performance. Title formulas + thumbnail rules live in [skills/06-thumbnail-title-system/SKILL.md](skills/06-thumbnail-title-system/SKILL.md). This file is the *log*, not the system.

## Title + Thumbnail Brief (one row per video)

For each video, record the brief produced by skill 06:

```
V0__ — {Slug}
- Final title: "..."
- Char count: __
- Title formula: T_
- Thumbnail subject pose: ...
- Highlight word: ...
- Telugu badge: ...
- Social-proof badge: ...
- Tech-stack icons: ...
```

## Tags Template (every video uses these + topic-specific additions)

**Base tags** (do not vary):
```
agentic ai, generative ai, llm, ai engineer, production ai, roadmap 2026,
balaji chippada, telugu ai tutorial, no black box, build from scratch,
ai engineering, aws bedrock, langchain alternative, langgraph, rag
```

**Topic-specific tags** (add 5–10 per video):
- The exact technique / library name
- The phase number ("phase 4 rag")
- Adjacent concepts the video touches
- The dataset / benchmark / framework if used

## Description Block

Use the description block from [video-script-template.md](video-script-template.md). Copy / paste it into YouTube, then add timestamps as you watch the final cut.

---

## Video Log (append a row per published video)

| # | Date | Title | Phase / Section | Length | Repo | Story Used | Hint Pattern (skill 09) | Views (7d) | Views (30d) | CTR | Avg Watch % | Avg Duration | Subscribers / video | Top Comment Theme | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V001 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| V002 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| V003 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

---

## Performance Targets (Indian-YouTube Agentic-AI niche)

These are calibrated for this niche, not generic. Update quarterly.

| Metric | First 3 months | 3–6 months | 6–12 months |
|---|---|---|---|
| CTR | 4–6% | 6–9% | 9–12% |
| Avg Watch % | 35–45% | 45–55% | 50–60% |
| Avg View Duration | 5–7 min | 8–11 min | 10–14 min |
| Subscribers / video | 10–25 | 30–80 | 80–250 |
| Comments / video | 30–80 | 80–200 | 200–500 |

### What to optimize when a metric is low

| Symptom | Likely cause | Fix |
|---|---|---|
| Low CTR | Title or thumbnail | Re-brief per skill 06 — try different title formula, change face emotion, swap highlight word |
| Low watch % at first 30s | Hook is weak | Re-write per skill 07 — try different opener pattern |
| Drop-off at minute 8–12 | Mid-video momentum loss | Add a medium switch (sketchbook → demo), plant a fresh open loop |
| Low subs/video | Audience isn't sticking past one video | Strengthen end-screen cliffhanger, ensure cross-linking to playlist |
| Low avg duration on long videos | Content too dense or slow | Cut filler, tighten pacing, more concrete numbers |
| High CTR + low watch % | Clickbait suspicion | Audit title vs body — they must agree |

---

## Phase-Detection Snapshot (for skill 09 — Monetization Runway)

Update at the end of every month:

```
Month: ____
Subscribers: ______
Long-form videos published: ____
Months since launch: ____
Community asking for paid? (Y/N): __
Wait-list signups: ____
Detected phase: 1 / 2 / 3
Next-month plan: keep building trust / launch first webinar / scale funnel
```

---

## Notes Field (per video — append, don't overwrite)

Use this for honest post-mortems. Examples:
- "Hook B (production incident) outperformed expectations — 62% retention at 0:30"
- "Sketchbook segment at 9:00 caused drop-off — too long, cut next time"
- "Comment cluster: viewers want a separate AWS Bedrock setup video — queue for V0__"
- "Tried T7 (Stop Doing X) title — CTR jumped to 9.4%; replicate when topic supports it"

---

*Update this tracker after every video. Review monthly. The Indian-YouTube CTR baseline is volatile — what works in month 1 may not in month 6.*
