# Balaji Chippada — YouTube Creator Skills

Project-scoped skills that encode the voice, visuals, story bank, roadmap, and operating rhythm of the **Roadmap 2026 Agentic AI** YouTube channel ([@balajichippada](https://www.youtube.com/@balajichippada)).

These skills are NOT generic. They are personalized to one creator with one curriculum, one face, one outfit, one accent, one cadence. Generic content advice has been removed; only opinionated, decision-ready rules remain.

## When to read which skill

| Authoring task | Skill to load first |
|---|---|
| Writing any line that will be spoken on camera | `01-balaji-voice/` |
| Picking which personal anecdote to open with | `02-story-bank/` |
| Designing a slide, lower-third, sketchbook page, thumbnail | `03-visual-identity/` |
| Deciding which roadmap phase a video maps to | `04-roadmap-source/` |
| Cutting a 60s Short out of a long video | `05-shorts-from-longs/` |
| Writing a title or briefing a thumbnail | `06-thumbnail-title-system/` |
| Generating 5 hook variants for a topic | `07-hook-factory/` |
| Planning a Sunday 7 PM IST live doubt session | `08-live-doubt-session/` |
| Deciding when/how to mention paid offerings | `09-monetization-runway/` |
| Generating the YouTube upload package (description + timestamps + tags + pinned comment + Shorts hooks) from an SRT | `10-description-generator/` |

## How to invoke

These skills live in `youtube/skills/` (project-scoped, lives with the roadmap). To apply one, read the relevant `SKILL.md` and follow it. For complex video planning, load **multiple** skills together — voice + story-bank + roadmap-source + hook-factory is the default combo for any new video script.

## Source-of-truth files

- `site/data.js` — the 9-phase curriculum. Every video maps here.
- `media/subtitles/` — past video transcripts (SRT). The voice skill is extracted from these.
- `media/thumbnails/` — canonical thumbnail examples. Visual identity references these.
- `site/uploads/balaji-chippada.png` — the brown bomber jacket reference subject photo.

## Non-negotiables (apply across all skills)

1. **No "guys"** — speak as if to one person, directly.
2. **No "hey guys, welcome to my channel"** — never. Get into value in <30 seconds.
3. **No clickbait** — if the title says X, the video must deliver X.
4. **No translating technical jargon** — `agent`, `embedding`, `RAG`, AWS service names, library names, error messages stay English even in Telugu delivery.
5. **No paid pitch in first 2 minutes** — and per `09-monetization-runway/`, no real pitches at all in Phase 1 of the channel; subtle hints only.
6. **No toy-only examples** — every concept ends with a production consideration.
7. **No happy path only** — show errors, debug live.
8. **MWF schedule is sacred** — buffer 2 weeks ahead.
