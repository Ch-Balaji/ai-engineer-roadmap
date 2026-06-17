---
name: shorts-from-longs
description: Pipeline to extract a 60-second YouTube Short from each long-form Roadmap-2026 video — identify the hook moment, the aha moment, or the strongest demo clip, then reframe vertical, burn captions in CapCut. Use when a long video has been recorded/published and Shorts are needed for the off-days (Tue/Thu/Sat).
---

# Shorts From Longs

Shorts on this channel are NOT native — they are **best-clip extractions** from long-form videos. The strategy: every long video produces 1–2 Shorts that re-promote the long.

## What a Short on this channel looks like

- 45–60 seconds (60s ceiling)
- Vertical 9:16 (1080×1920)
- Burned-in captions (yellow `#FFD60A` highlight on keyword, white text, 1px black outline)
- Hook in first 1.5 seconds
- One idea, one payoff
- Outro card (last 1s): "Full breakdown — 18 minutes — link in description / comments"

## The 4 Extraction Patterns

Pick ONE per Short. Don't combine.

### Pattern A — The Hook Replay
The first 30 seconds of the long video, tightened to 45–60 seconds. Adds a CTA at the end pointing to the full video.

> Use when: the long video's opener is a strong story, demo, or shock-stat that stands alone.

### Pattern B — The Aha Moment
The 60 seconds where the viewer "gets it" — the demystification beat (often around the 60–70% mark of the long). Strip out the buildup, keep just the reveal + the "see, no magic" line.

> Use when: the long video has a clear "OH!" moment isolatable from context.

### Pattern C — The Demo Highlight
A 30–50 second clip of a working agent / system doing the thing. Add a 5-sec setup at the start ("This agent is reading my resume against a job description and rewriting it...") and a 5-sec CTA at the end.

> Use when: the long video features a finished system that's visually impressive even without explanation.

### Pattern D — The Hot Take
A 30–45 second clip of an opinionated claim made in the long video, isolated and amplified.

> Use when: the long video had a strong assertion ("RAG is fundamentally broken for 40% of use cases") that stands alone as a debate-starter.

## Production Pipeline (CapCut)

1. **Identify the clip** — open the long video timeline, find the segment matching one of the 4 patterns. Mark in/out points.
2. **Duplicate to a vertical project** — new CapCut project, 1080×1920.
3. **Reframe** — center subject in upper-middle 60% of the frame; the bottom 30% reserved for caption burn-in.
4. **Re-cut tightly** — remove all "uhms", pauses, false starts. Aim for sub-60 seconds.
5. **Caption burn-in** — auto-caption in CapCut, then manually:
   - Bold sans, white, 1px black outline
   - Yellow `#FFD60A` highlight on the most important word per phrase
   - Captions sit in the bottom 25% of the frame (not overlapping the subject's face)
6. **Outro card (last 1s)** — text: "Full video — link in description". White text on dark bar at the bottom.
7. **Cover frame** — pick a frame where Balaji's face shows expression + the caption keyword is visible. This is the Short's preview thumbnail.
8. **Export** — H.264, vertical 1080×1920, 30 fps, ~10 Mbps.

## File Naming

```
shorts/
├── V012_intro-to-RAG/
│   ├── short_01_hook.mp4
│   ├── short_02_aha.mp4
│   └── source_clips/
```

`V012` = the long video's number; `_01`, `_02` = which Short variant.

## Publishing Cadence

The default schedule: **Mon/Wed/Fri longs**, **Tue/Thu/Sat Shorts** (one per off-day, optional). Sunday is the live session.

If the instructor is over-loaded: drop Shorts before dropping longs. Longs are the curriculum; Shorts are the marketing layer.

## Hooking the Long from the Short

The last 1–2 seconds of every Short MUST point back to the long. Three patterns:

| Pattern | Phrasing |
|---|---|
| Curiosity gap | "If you want to see how this actually works in production — full video, link in description." |
| Direct CTA | "18-minute deep dive — top comment." |
| Cliffhanger | "But here's what breaks at scale — and that's what the full video is about." |

The Short is a **trailer** for the long. It must drive watch-through to the long video.

## Anti-Patterns

- ❌ Native Shorts that don't reference any long. (You said no — only re-purpose.)
- ❌ Shorts longer than 60 seconds. They get throttled.
- ❌ Burned captions covering the subject's face.
- ❌ A Short that "spoils" the long video's aha moment fully — leave the *why* unanswered, only show the *what*.
- ❌ Multiple ideas in one Short. Pick one.
- ❌ Shorts uploaded without a horizontal long-form companion live within 7 days.

## Quality Pass

- [ ] Hook lands in <2 seconds
- [ ] Single idea — passes the "what was that Short about" test in one sentence
- [ ] Burned captions; yellow highlight on keyword
- [ ] Outro 1s pointing to full video
- [ ] 9:16, ≤60 seconds
- [ ] Subject's face visible (not covered by captions)
- [ ] Cover frame chosen
