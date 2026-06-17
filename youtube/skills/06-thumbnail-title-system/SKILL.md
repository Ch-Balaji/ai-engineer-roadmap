---
name: thumbnail-title-system
description: Indian-YouTube-tuned title and thumbnail brief generator for the Roadmap-2026 channel. Pairs a title formula with a matching thumbnail brief (face emotion, highlight word, Telugu accent text). Use after a video script is drafted, before recording, to lock the title + thumbnail brief together.
---

# Thumbnail + Title System

Title and thumbnail are designed **together**, never separately. The title makes the promise; the thumbnail makes the click. They must agree.

This skill outputs a single brief that drives both.

## Step 1 — Pick a title formula

The title must do ONE of: create curiosity gap, name the transformation, or stake a claim. Pick the formula that matches the video's purpose:

| # | Formula | When to use | Example (Roadmap-2026) |
|---|---|---|---|
| T1 | `[Topic] — What Nobody Tells You` | Counter-intuitive truth | "RAG — What Nobody Tells You About Production" |
| T2 | `Why [Common Belief] Is Wrong` | Challenging mainstream advice | "Why 'Use LangChain' Is Wrong Advice for Beginners" |
| T3 | `[Topic] in [X] Minutes (No Black Box)` | Promise-driven tutorial | "Build a Tool-Calling Agent in 18 Minutes (No Black Box)" |
| T4 | `The #1 Mistake [Audience] Makes With [Topic]` | Mistake-driven hook | "The #1 Mistake Beginners Make with Embeddings" |
| T5 | `I Built [System]. Here's What Broke.` | Production-incident style | "I Deployed a Multi-Agent System. Here's What Broke at 3 AM." |
| T6 | `[Old Way] vs [New Way] — Which Wins in 2026?` | Comparison hook | "Vector DB vs GraphDB — Which Wins for Agents in 2026?" |
| T7 | `Stop Doing [Thing]. Do [This] Instead.` | Strong opinion / pivot | "Stop Learning ML in 2026. Do This Instead." |
| T8 | `From [Bad State] to [Good State] in [X] Steps` | Transformation arc | "From ChatGPT User to Engineer Who Controls LLMs — In 7 Steps" |
| T9 | `[Number] Things I Wish I Knew Before [Action]` | Listicle / reflective | "5 Things I Wish I Knew Before Building My First Agent" |
| T10 | `[Topic] Explained Like You're a Senior Engineer` | Authority signal | "RAG Evaluation Explained Like You're a Senior Engineer" |

### Title rules

- Under 60 characters (mobile cutoff)
- Include the main topic keyword (search)
- Use a number when it tightens the promise
- Never clickbait — body must deliver the title's promise (`no-clickbait` non-negotiable)
- Avoid `🔥`, `💯`, all-caps, multiple `?`/`!`. (Indian dev audience reads them as low-effort.)
- Don't put `(Telugu)` in the title — that's the thumbnail's job

## Step 2 — Pair the thumbnail brief

Each title formula maps to a thumbnail face/emotion + highlight word. Don't improvise.

| Title formula | Face emotion | Highlight word (yellow) | Telugu accent text |
|---|---|---|---|
| T1 (Nobody Tells) | Confident, slight smirk, knowing | The taboo word (e.g., `BROKEN`) | "ఇది అందరికీ తెలియదు" (Most don't know this) |
| T2 (Why X is Wrong) | Direct stare, serious | The wrong belief (e.g., `WRONG`) | "నిజం చెప్పనా?" (Shall I tell the truth?) |
| T3 (X Minutes) | Approachable smile, hand up | The number (`18 MINUTES`) | "తెలుగులో FULL GUIDE" |
| T4 (#1 Mistake) | Concerned, finger pointing | `MISTAKE` or the noun being misused | "ఇది చేయొద్దు" (Don't do this) |
| T5 (I Built / Broke) | Surprised / eyebrows up, slight grimace | `BROKE` or `FAILED` | "ప్రొడక్షన్ లో" (In production) |
| T6 (X vs Y) | Neutral, looking between two halves | The winner (e.g., `WINS`) | "ఏది బెటర్?" (Which is better?) |
| T7 (Stop Doing) | Stern, palm out | `STOP` | "ఇంకా చేస్తున్నారా?" (Are you still doing this?) |
| T8 (From X to Y) | Hopeful, looking up-right | The transformation noun (e.g., `ENGINEER`) | "అవ్వడం ఎలా?" (How to become?) |
| T9 (Things I Wish) | Reflective, slight smile | The number | "నేర్చుకున్న పాఠాలు" (Lessons I learned) |
| T10 (Senior Engineer) | Confident, calm, arms crossed | `SENIOR` or the topic | "ప్రొఫెషనల్ గైడ్" (Professional guide) |

## Step 3 — Output the locked brief

For every video, the brief looks like this:

```
THUMBNAIL + TITLE BRIEF
- Title formula: T3 (X Minutes — No Black Box)
- Final title: "Build a Tool-Calling Agent in 18 Minutes (No Black Box)"
- Char count: 56
- Subject pose: Approachable smile, hand mid-gesture (explaining)
- Outfit: Brown bomber jacket + black zip-up (locked)
- Background: Black + circuit overlay + warm rim light
- Primary text (white, Anton bold, ALL CAPS):
    BUILD A TOOL-CALLING
    AGENT IN
- Highlight text (yellow + brush band):
    18 MINUTES
- Telugu badge (red bg, white text, bottom-right):
    "తెలుగులో FULL GUIDE"
- Social-proof badge (top-left, optional):
    "8+ YEARS IN AI"
- Tech-stack icon row (bottom):
    Python · OpenAI SDK · LangGraph · pydantic
```

Pass this brief to the thumbnail producer (or feed into ChatGPT image / Photoshop) per [03-visual-identity/THUMBNAIL_RULES.md](../03-visual-identity/THUMBNAIL_RULES.md).

## Indian-YouTube CTR Tactics (calibration notes)

- **Face on every thumbnail.** No exceptions. Indian dev audience clicks faces.
- **Telugu accent text is a CTR multiplier** for the Telugu segment. Always include.
- **Numbers in the title** outperform vague claims. `18 minutes`, `5 mistakes`, `3 patterns`.
- **One word in yellow.** Two yellow words = visual chaos = lower CTR.
- **Brown bomber jacket consistency.** Face recognition over time = direct-traffic compound.
- **Never use `🔥` in titles.** It signals "hindi-belt mass-market YouTuber" — wrong audience for this channel's positioning.

## A/B Decision (when unsure)

When two title/thumbnail options seem equally strong, default to:

1. The **more specific** option (concrete number > vague intensifier)
2. The **more honest** option (no clickbait survives)
3. The option that **continues the playlist's tone** (don't break tone mid-series)

If still unsure, log both in the metadata tracker and run a YT A/B test (YouTube Studio → Test & Compare).

## Anti-Patterns

- ❌ Title without a topic keyword (kills search)
- ❌ Thumbnail with two highlight words (visual chaos)
- ❌ Different outfit per thumbnail (kills face recognition)
- ❌ No Telugu badge (loses Telugu segment CTR)
- ❌ Stock-photo subject (loses authenticity)
- ❌ Title and thumbnail promising different things
- ❌ Numbers like "100% guaranteed" / "secret hack" (clickbait flavor)
