---
name: hook-factory
description: Given a Roadmap-2026 topic, generates 5 first-30-second hooks across Balaji's opener rotation — personal story, production incident, live demo first, comment callback, shock statistic. Enforces the no-clickbait, no-"hey-guys-welcome", under-30-seconds rules. Use after the video's roadmap mapping is locked, before writing the rest of the script.
---

# Hook Factory

The hook is 0:00–0:30. It decides whether 70% of viewers stay or leave. This skill produces 5 hook drafts per topic across the locked rotation. The instructor picks one.

## Inputs the skill needs

Before generating hooks, get these:

1. **Topic** (e.g., "Late chunking — embed first, chunk later")
2. **Phase + section** from `site/data.js` (e.g., Phase 4, Section 4.4)
3. **Video purpose** (tutorial / motivational / industry news / interview prep / project walkthrough / hot take)
4. **Most recent stories used** (for cooldown — see `02-story-bank/STORIES.md` usage log)

## Output format

5 hooks, each tagged with its pattern. Each hook is **2–4 sentences** and reads as ≤30 seconds spoken.

```
HOOK A — Personal Story
"<2-4 sentences>"
[Visual: <what's on screen during this hook>]

HOOK B — Production Incident
"<2-4 sentences>"
[Visual: <what's on screen>]

HOOK C — Live Demo First
"<2-4 sentences>"
[Visual: <demo running>]

HOOK D — Comment Callback
"<2-4 sentences>"
[Visual: <screenshot of comment>]

HOOK E — Shock Statistic
"<2-4 sentences>"
[Visual: <stat / chart / log>]
```

## The 5 Hook Patterns (with seed templates)

### A. Personal Story
A canon story (from `02-story-bank/`) framed to set up today's topic. Cooldown rule applies — don't repeat the same story as opener within 4 videos.

> Seed: *"In 2018, I was on Infosys mainframes. Every day I was solving problems that the world had stopped caring about. I read 50 articles trying to learn ML — and got lost in the first month. The reason I'm teaching {topic} the way I am today is because I remember exactly what 'lost' feels like."*

### B. Production Incident
A real or composite production failure that the topic solves. Specific and concrete.

> Seed: *"This RAG system was running fine for 3 weeks. Then a user asked a question, and the agent retrieved a chunk that ended mid-sentence. The LLM hallucinated the rest. {topic} is the fix that should've been in the pipeline from day one."*

### C. Live Demo First
Run the working thing FIRST. No setup. The viewer sees a result before they hear an explanation.

> Seed: *"Watch this. {Run the demo on screen.} That agent just {what it did}. In the next 18 minutes, we'll build it from scratch — and you'll understand exactly why each piece is there. No black box."*

### D. Comment Callback
Quote a specific comment (or composite of comments) from a previous video.

> Seed: *"After the last video, this comment came in: '{comment text}.' That's a great question. Today's video is the answer."*

### E. Shock Statistic
A real, defensible number. No fake stats. The number must hold up if a senior engineer in the audience checks.

> Seed: *"OpenAI's own eval shows {model} drops {N}% accuracy when context exceeds {tokens} tokens. That's the failure mode behind {topic}. Here's how to design around it."*

## Seed Examples Per Phase

To bootstrap drafting, here are seed angles per phase:

| Phase | Strong angles |
|---|---|
| 1. Python Foundations | "Async won't matter until your agent calls 3 LLMs in parallel and one hangs. Then it's everything." |
| 2. LLM Mental Model | "ChatGPT made up a fact. Same model, same prompt, second time — different fact. This is the part nobody explains." |
| 3. Prompt Engineering | "Your prompt works 7 times out of 10. That's why it's not in production." |
| 4. RAG | "You can paste 200 documents into Gemini's context window. So why does anyone still build RAG?" |
| 5. Tools / MCP | "An agent without tools is a chatbot. The line between them is one function call." |
| 6. Memory | "Your agent forgets you between conversations. Production agents don't. Here's the difference." |
| 7. Context Engineering | "The agent has 200k token context. It still failed. Because long context degrades — 'lost in the middle'." |
| 8. Multi-Agent | "Two agents talking to each other looks magical. Until one of them goes into an infinite loop and burns $400 in 12 minutes." |
| 9. Guardrails / Production | "A user typed one emoji. The agent prompt-injected itself. The system was down for 4 hours." |

## Hard Rules

- ❌ Never start with "Hey guys, welcome to my channel."
- ❌ Never start with "In this video we'll cover..."
- ❌ Never start with a static title card alone — the human voice or a working demo should appear in the first 1–2 seconds.
- ❌ Never use a "shock stat" that isn't defensible.
- ❌ Never tell the same canon story as opener twice within 4 videos.
- ✅ Always create a **knowledge gap** the viewer wants closed.
- ✅ Always specify what's visually on screen during the hook.

## Picking from the 5

After the 5 hooks are generated, recommend the best one based on:

1. **Match to video purpose** — tutorial defaults to C (Demo First) or B (Incident); motivational defaults to A (Story); hot-take defaults to E (Shock Stat).
2. **Story cooldown** — if A's chosen story was used 2 videos ago, drop A.
3. **Production cost** — C (Demo First) requires a working demo by recording day; if not ready, fall back to B.
4. **Series tone** — don't break the rhythm of a phase mid-stream.

## Quality Pass

For each hook output:

- [ ] 2–4 sentences, ≤30 seconds spoken
- [ ] Specific noun, number, or named thing in the first sentence
- [ ] Knowledge gap created
- [ ] Visual cue specified
- [ ] Doesn't violate `01-balaji-voice/` (no "guys", no greeting)
- [ ] Sets up a payoff the rest of the video will deliver
