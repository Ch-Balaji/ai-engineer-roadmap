---
name: story-bank
description: Balaji Chippada's canon of reusable personal stories (NIT EEE, Infosys mainframes, Warner Bros / Deutsche Telekom / Swiss telecom journey, Netherlands relocation, after-full-time-job hustle). Use when an opener, mid-video bridge, or close needs a personal anecdote. Enforces cooldown rules so no story gets stale.
---

# Story Bank

Five canon stories. Each has multiple framings. Pick by video type and topic. Track usage so the same story doesn't appear in 3 consecutive videos.

## The 5 Canon Stories

| # | Tag | One-line | Best for |
|---|---|---|---|
| 1 | `STORY_NIT_EEE` | NIT Calicut, EEE branch (non-IT), 2018 | "Non-IT can pivot" / fresher-targeting videos |
| 2 | `STORY_INFOSYS_MAINFRAMES` | First job: Infosys, mainframes, 3 LPA, felt stuck | "Stuck in legacy stack" / pivot videos |
| 3 | `STORY_WB_DT_SWISS` | Warner Bros & Discovery → Deutsche Telekom → Swiss telecom | Authority / "I've actually shipped this" |
| 4 | `STORY_NETHERLANDS_NOW` | Currently in Netherlands, working remote for Switzerland's largest telecom | "AI engineering opens borders" / global market |
| 5 | `STORY_AFTER_FULLTIME` | This entire channel is built after a full-time job + gym + freelance | Discipline / "free course = your discipline" |

Full 30-second written versions of each: see [STORIES.md](STORIES.md).

## Picking a Story

Match story to **video purpose**, not video topic:

| Video purpose | Default story |
|---|---|
| Convincing a non-IT viewer they can do this | `STORY_NIT_EEE` |
| Convincing a stuck-in-legacy viewer to start | `STORY_INFOSYS_MAINFRAMES` |
| Establishing authority on a hard production topic (RAG eval, multi-agent, AWS) | `STORY_WB_DT_SWISS` |
| Painting the upside (global jobs, remote, salary) | `STORY_NETHERLANDS_NOW` |
| Asking for effort / discipline from viewer | `STORY_AFTER_FULLTIME` |

## Cooldown Rules (prevent staleness)

- A story can appear as the **opener** at most **once per 4 videos**.
- A story can appear as a **mid-video bridge** more often (once per 2 videos).
- Never use the same story as opener AND closer in the same video.
- Track usage in `STORIES_USAGE.md` (created when first invoked).

If all 5 stories are on cooldown, skip to a non-personal opener (live demo / shock stat / production incident).

## Framing Rules (so the same story feels fresh)

Every canon story has **3 framings**. Pick the framing that matches the video's *insight*:

### Story 2 example (`STORY_INFOSYS_MAINFRAMES`)

| Framing | Use when video is about |
|---|---|
| **Trapped** — "I was on mainframes. I didn't see a future." | A pivot tutorial / "you can leave legacy" |
| **Grateful** — "Infosys gave me my start. I learned discipline there." | Soft skills / work ethic videos |
| **Lost** — "I had no roadmap. I didn't know what to learn next." | Roadmap / structure-of-learning videos |

Each canon story in [STORIES.md](STORIES.md) has its 3 framings written out.

## Where Stories Go in a Video

| Position | What the story does | Length |
|---|---|---|
| **Opener (0:00–0:30)** | Hook the viewer with stakes | 20–30 seconds, ≤4 sentences |
| **Mid-video bridge (5:00–8:00)** | Justify *why* this concept matters in real careers | 15–20 seconds |
| **Closer (last 30s before next-video tease)** | Land the takeaway emotionally | 10–15 seconds |

Never insert a story just to insert a story. If it doesn't tighten the *insight*, cut it.

## Adding a New Canon Story

When the instructor mentions a new strong personal anecdote in a recording or chat:

1. Confirm it can be reused across multiple video types (not a one-off).
2. Add it to [STORIES.md](STORIES.md) with a tag, one-liner, and 3 framings.
3. Update the table above.
4. Mark cooldown as fresh.

## Anti-Patterns

- Don't tell the same friend-got-laid-off story again until 8+ videos have passed since its last use.
- Don't combine 2 stories in one opener — pick one.
- Don't add a story to a video that's already at length (15+ min); a story stretches without paying off.
- Don't use stories in pure technical Shorts — Shorts need the *insight* in 60s, no storytelling room.
