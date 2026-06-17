---
name: live-doubt-session
description: Sunday 7 PM IST one-hour live doubt-clearing format for Roadmap-2026. Includes comment-mining workflow, question prioritization, live overlay templates, post-live followup doc, and the comment-to-Short repurposing pipeline. Use the day before a Sunday live, or when planning the live broadcast itself.
---

# Live Doubt-Clearing Session

Format: Sunday 7 PM IST. 60 minutes. Pure doubt-clearing — no curriculum, no slides, no demos prepared in advance. The instructor reads questions and answers them.

## Why pure doubt-clearing (no recap)

Recap belongs in the MWF tutorials. The live session is for the *new* problems — the ones a viewer hit while practicing. Mixing recap dilutes the unique value of being live.

If a recap is needed, queue a separate "Phase N Recap" recorded video on the next Friday.

## Pre-Live Workflow (Saturday — day before)

### Step 1 — Comment mining

Pull all comments from the past 7 days across:
- The 3 long videos (Mon/Wed/Fri)
- Any Shorts published
- Pinned comment thread on the channel page
- Direct doubts from the community tab

### Step 2 — Cluster by topic

Group comments into 5–7 clusters. Each cluster has a one-line problem statement. Examples:
- "RAG retrieving wrong chunks" → 8 comments
- "FastAPI + async LLM call hanging" → 5 comments
- "How to choose embedding model" → 12 comments
- "Career advice — am I too late at 28?" → 6 comments
- "AWS Bedrock vs OpenAI cost confusion" → 4 comments

### Step 3 — Prioritize

Pick the **top 8–10 questions** to answer live. Prioritize by:

1. **Frequency** — how many viewers asked variants of this
2. **Severity** — is this blocking practice (e.g., setup error)? Answer first.
3. **Teach-ability live** — can this be answered without slides/code? Live-friendly questions go in.
4. **Variety** — mix technical + career to keep the audience engaged

Hard cap: 10 questions in 60 minutes. Average ~5–6 minutes per answer leaves room for live chat questions in the last 10 minutes.

### Step 4 — Prep file (`live/{date}/prep.md`)

```
LIVE PREP — {YYYY-MM-DD}

Q1 — RAG retrieving wrong chunks (8 comments)
- Original comment: "@viewer1: my RAG returns the right doc but wrong chunk"
- Asker(s): @viewer1, @viewer2, @viewer3, ...
- Answer outline:
  - Chunk size mismatch
  - Need parent-child chunking
  - Show in live: a 30-line code snippet of parent-child retrieval
- Time budget: 7 minutes

Q2 — ...
```

The prep file is for the instructor; it's NOT scripted. Loose talking points only. Live energy depends on actually thinking aloud.

## Live Broadcast Setup

### Tech
- Mac screen as primary scene (terminal + browser + IDE if needed)
- Insta360 webcam PiP (top-right, larger than usual — this is a "look at me" session)
- DJI mic
- iPad GoodNotes sidecar for live whiteboard sketching
- Streaming: YouTube Live, public, "Allow live comments"

### Live overlay template

| Position | Element |
|---|---|
| Bottom band (cream `#F5EFE6`, ~10% screen height) | Question text + asker handle |
| Bottom-right corner | Small countdown timer ("Q3 of 10 · 4:12 left") |
| Top-right | Webcam PiP |
| Bottom-left lower-third | "LIVE — Sunday Doubts · {YYYY-MM-DD}" |
| Top-left (rotating) | Pinned-question indicator if super-chat / heart-given |

CapCut / OBS / Streamlabs scenes pre-built — switch with hotkeys, don't fumble.

### Energy & pacing

- First 90 seconds: "Welcome back. Top question this week is {Q1}. Let's go." No long intros.
- Each answer: ~5 minutes. If hitting 7, wrap.
- Mid-session pivot (~30 min mark): "Two career questions next, then back to technical."
- Last 10 minutes: take live chat questions ("Pin a question with a heart and I'll answer in order").
- Last 60 seconds: wrap → "Next live in 7 days. Wednesday's video is on {topic}. See you Monday."

## Post-Live Workflow (Sunday night / Monday morning)

### Followup doc (`live/{date}/followup.md`)

Compile the live's Q&A into a written followup:

```
LIVE Q&A FOLLOWUP — {YYYY-MM-DD}

Q1 — RAG retrieving wrong chunks
Answer summary: ...
Code sample: ...
Mentioned video: V07 (Embeddings)
Watch the live segment: {timestamp}

Q2 — ...
```

Pin this doc as a comment on Monday's video. Link it in the next Friday's video description.

### Comment-to-Short pipeline

Pick the **best 1–2 live answers** (the ones with strongest single-idea payoff) and:

1. Trim the live recording to that answer's clip (30–50 seconds).
2. Re-process per `05-shorts-from-longs/` Pattern B (Aha Moment).
3. Publish as a Short on Tuesday or Thursday.
4. Caption credits the asker: *"Question by @viewer1, answered live. Full live: link in comments."*

This loop reinforces: ask doubts → get answered → maybe become a Short. Gives the audience a reason to keep asking publicly in comments rather than DMs.

## What NOT to do live

- ❌ Pre-record and pretend it's live. The trust is the live-ness.
- ❌ Read from a script.
- ❌ Skip the comment-mining and wing it. Quality drops fast.
- ❌ Spend 20 minutes on one question. Cap at 7 minutes.
- ❌ Promise paid offerings. Phase 1 = trust only (`09-monetization-runway/`). A subtle hint at the end is fine; an actual pitch is not.
- ❌ Get defensive on hard questions. "I don't know, let me check and reply on Monday's video" is the right answer when you don't know.
- ❌ Run over time. 60 minutes ends at 60 minutes.

## Quality Pass

Before going live:

- [ ] Comment mining complete; 5–7 clusters identified
- [ ] Top 8–10 questions selected, written into prep file
- [ ] OBS scenes pre-built; webcam framing tested
- [ ] DJI mic battery checked
- [ ] iPad GoodNotes ready, blank page open
- [ ] Stream title set: "Sunday Doubts · Roadmap 2026 · {Date}"
- [ ] Stream thumbnail: live-format variant (red LIVE badge + "RAG, Embeddings, Career — your questions" subtitle)
- [ ] Family / housemates know not to interrupt for 60 minutes

After:

- [ ] Followup doc written and pinned on Monday's video
- [ ] 1–2 best clips identified for Short repurposing
- [ ] Notable questions logged into next phase's video planning
