# I Made My AI Agent 3x Faster With One Python Keyword (2026)

**Full scene-by-scene script** — Phase 1.5 retrofit (async + agents). Companion code: `async_agent_demo/`. Title and 3x speedup are live-verified against the OpenAI account on 2 June 2026.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V012 |
| Slug | async-ai-agent-2026 |
| Playlist | AI Engineer Roadmap 2026 |
| Phase | 1.5 retrofit (async fundamentals) + Phase 5 preview (agents) |
| Target length | 13–15 min (hard cap 16) |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | V011 — *Reasoning Models vs Base Models* (or whichever published last) |
| Next video | Multi-agent orchestration with async (cliffhanger) |

## Roadmap Mapping

- **Phase 1.5** — Python fundamentals every AI engineer needs (async/await, asyncio.gather, coroutines)
- **Phase 5 preview** — agent loops, tool calling, OpenAI tool API
- **Prerequisites:** `Working with API`, `Tokens in LLM` (basic Python comfort assumed)
- **End state:** viewer understands what async is, why every AI framework uses it, and can build a 3x faster agent in one sitting

## Why this video, now

| Reality (verified live, 2 June 2026) | Script implication |
|---|---|
| `async_agent_demo/` 5-city run: SYNC 32.81s, ASYNC 11.80s, **2.8x speedup** | Headline number rounded honestly to **3x** |
| Minimal `asyncio.gather` demo (3 sleeps): exact 6.01s vs 2.00s = **3.0x** | Scene 7 conceptual reveal — clean 3x with no LLM noise |
| LLM round-trip floor (~10s combined for plan + synthesis with `gpt-4o-mini`) | Honest disclosure in Scene 10 — speedup floor is structural, not a bug |
| LangChain, AWS Strands, CrewAI all use async to the core | Scene 3 framework-authority drop |
| 21 seconds saved per query at 1000 queries/day = 5.8 hours/day | Production framing in Scene 9 |

---

## FINAL HOOK — The Side-by-Side Demo (LOCKED)

**Setup on screen:** Two browser windows side-by-side. Both running Streamlit.
- LEFT — `localhost:8501` — labeled **🐢 Sync Agent**
- RIGHT — `localhost:8502` — labeled **⚡ Async Agent**

**Same prompt typed into both at the same time:**

> *Plan a 5-day trip across Hyderabad, Bangalore, Chennai, Mysore, and Pondicherry. Tell me the weather and top attractions for each city.*

**What viewer sees (verified live 2 June 2026):**

- LEFT: Six tools tick by one at a time. `weather:Hyderabad` 2.0s. `weather:Bangalore` 2.0s. Slow drumbeat. Final timer: **🔴 32.81s**
- RIGHT: All ten tools light up at once. Timer barely ticks. Final timer: **🟢 11.80s**
- Big overlay between the two windows: **2.8× FASTER**  ·  **21 seconds saved**

**Spoken (face cam after the demo lands):**

> Two chatbots. Same prompt. Same model. Same code — almost.
>
> The slow one took **thirty-three seconds**. The fast one — **twelve**. **Twenty-one seconds saved on a single question.**
>
> Run that a thousand times a day in production — that is **six hours of human waiting time saved every day**, on the same OpenAI bill.
>
> The difference between these two chatbots is **one Python keyword**. By the end of this video — fifteen minutes — you will have built both of these. From scratch. With code that fits on one screen.



## SCENE 1 — HOOK (0:00 – 0:50)

Already locked above. Two browser windows side-by-side, real timers, real `gpt-4o-mini`, mocked tools at 2s each.

---

## SCENE 2 — HONEST BRIDGE + PHASE 1.5 RETROFIT (0:50 – 1:20)

**On screen:** Sketchbook drawn live — `Phase 1` box, big arrow, `Phase 1.5 — RETROFIT` chip glowing yellow. CapCut lower-third (3 sec) showing the *Working with API* video thumbnail.

**Spoken:**

> Real talk before we go further. When I designed Phase 1 of the roadmap, I left this concept out. Many of you noticed and asked — *"how do AI engineers actually make their agents fast in production?"* Today's video fixes that gap.
>
> This is **Phase 1 point five.** The trick I should have taught you the first time. And it is not just for AI agents — every backend you ever build will use this.

**[Bridge ends fast. No padding.]**

---

## SCENE 3 — FRAMEWORK AUTHORITY DROP (1:20 – 1:50)

**On screen:** Three rapid ChatGPT screenshots, ~5 seconds each. No reading the responses out loud — let the **Yes** speak.

**Spoken:**

> Quick check. *(Cut to screenshot 1.)* Does **LangChain** use async programming? **Yes — extensively.**
>
> *(Screenshot 2.)* Does **AWS Strands**, Amazon's agent framework? **Yes — async-first.**
>
> *(Screenshot 3.)* Does **CrewAI**, the multi-agent framework everyone is using? **Yes — async to the core.**
>
> *(Cut to face cam.)* If every agent framework you will ever touch uses this concept under the hood — you should at least know what it is. Which is what the next twelve minutes are about.

**[Retention beat: viewer just got the "this is important" stamp from three brands they recognize. Now they will sit through the explanation.]**

---

## SCENE 4 — THE CHEF ANALOGY (1:50 – 3:30) | L1 analogy

**On screen:** Sketchbook full-screen. Two stick-figure chefs drawn live, one panel each.

**Spoken:**

> Now the analogy. Hold this picture in your head for the rest of the video.
>
> **Chef A** — one stove. One burner. Three dishes to cook — biryani, sambar, and curry. Each dish needs to simmer for two minutes.
>
> *(Draw timeline below Chef A: three orange blocks, stacked end-to-end.)*
>
> Biryani — two minutes, done. Sambar — two minutes, done. Curry — two minutes, done. Total time on the clock: **six minutes.** Chef A is doing one thing at a time. This is **synchronous** — sync for short.
>
> **Chef B** — same kitchen, same three dishes. But Chef B's stove has **three burners.** Lights all three at once. Walks around, watches them, plates them as each is ready.
>
> *(Draw timeline below Chef B: three orange blocks, side-by-side.)*
>
> Two minutes. **All three dishes done at once.** Three times faster. This is **asynchronous** — async.
>
> Both chefs follow the same recipe. Both deliver the same food. The only difference — Chef B can wait on multiple things in parallel.
>
> An AI agent is exactly the same. It is a chef. The dishes are the API calls. **Sync agent = one burner. Async agent = three burners.** That is the whole video.

---

## SCENE 5 — TIMELINE DIAGRAM, ONE FRAME (3:30 – 5:00) | L2 visual

**On screen:** Sketchbook — two timelines, drawn live, side-by-side.

**Spoken:**

> Now the same picture for an actual agent. Five cities. Two API calls per city — weather and attractions. Ten tool calls in total.
>
> *(Top half of sketchbook — sync timeline. Draw ten orange blocks left to right, each labeled "tool 2s". Below it, write "+ LLM 10s overhead". Total: 30 seconds.)*
>
> Sync. Each tool call waits for the one before it. **Twenty seconds of tool time, plus ten seconds the LLM takes to plan and answer. Thirty seconds.**
>
> *(Bottom half — async timeline. Draw all ten orange blocks stacked vertically — they all start at the same time, all end at 2 seconds.)*
>
> Async. All ten tools fire at once. **Two seconds for the tools, plus the same ten seconds the LLM needs.** **Twelve seconds total.**
>
> Sync minus async — **eighteen seconds saved on every single query.** Across ten thousand queries — **fifty hours of human waiting time gone.** From one keyword change.

---

## SCENE 6 — DEFINITIONS: `async def`, `await`, SUBROUTINE vs COROUTINE (5:00 – 6:30) | L3 name

**On screen:** Open `async_agent_demo/minimal_demo.ipynb` — **Section 1** (three-keyword table) visible. Then sketchbook for ASCII.

**Spoken:**

> The chef trick has a real name. **Async input/output.** In Python — **asyncio.**
>
> One sentence. Async I/O means your program does **other useful work while it waits** on something slow — a network call, disk, an API. It juggles instead of freezing.
>
> Three Python keywords. Put this table on screen — it is in the notebook repo.
>
> **`def`** — normal function. Do this now, block until done.
>
> **`async def`** — you are defining a **coroutine**. This function *can* pause and let other work run.
>
> **`await`** — pause **only this** coroutine. "I'm waiting on I/O — event loop, please run something else."
>
> Rule: `await` only works **inside** `async def`.
>
> A **subroutine** is plain `def fetch(name)` — call it, it runs start to finish, caller waits.
>
> A **coroutine** is `async def fetch_async(name)` — call it and you get a **coroutine object**, not the result yet. Something must drive it: `await fetch_async()` or `asyncio.run(...)`.
>
> **(Optional 15s — run notebook Section 6 micro-example on screen.)**
>
> Watch this. `coro = hello()` — type is coroutine, body **not** executed. `await hello()` — **now** it prints. Beginners miss this; engineers nod.

**ASCII to draw on sketchbook (sync — Section 2 of notebook):**

```
TIME ───────────────────────────────────────────────►

fetch(weather)     [████ 2s ████]
fetch(attractions)            [████ 2s ████]
fetch(news)                              [████ 2s ████]
TOTAL ≈ 6s
```

**[Do not rush this scene — definitions + `async def`/`await` are what comments will ask about.]**

---

## SCENE 7 — MINIMAL CODE DEMO + ASCII FLOW (6:30 – 8:00) | L4 code

**On screen:** Same notebook. Scroll: Section 3 sync cell → run. Section 5 async ASCII → draw. Section 8 async cell → run. End on Section 9 side-by-side diff.

**Spoken:**

> Ignore the agent for ninety seconds. Same notebook you will fork — `minimal_demo.ipynb`.
>
> **(Run sync cell — Section 3.)**
>
> ```python
> def fetch(name):
>     time.sleep(2)   # blocks the whole thread
>     return f"got {name}"
> results = [fetch(n) for n in ("weather", "attractions", "news")]
> ```
>
> Six seconds. Draw the sync timeline from the notebook — three blocks **stacked**.
>
> **(Scroll to Section 4–5 markdown — async ASCII on screen.)**
>
> Now async. **`async def`** means the function can yield at **`await`**. **`await asyncio.sleep(2)`** does not freeze the whole program — the **event loop** runs other coroutines during those two seconds.
>
> Draw the async timeline — three blocks **overlapping** in the same 2-second window. Chef with three burners.
>
> **(Run micro-example Section 6 if you skipped it in Scene 6.)**
>
> **(Run async cell — Section 8.)**
>
> ```python
> async def fetch_async(name):
>     await asyncio.sleep(2)
>     return f"got {name}"
>
> results = await asyncio.gather(
>     fetch_async("weather"),
>     fetch_async("attractions"),
>     fetch_async("news"),
> )
> ```
>
> Two seconds. **Exactly three times faster.** Show the **`asyncio.gather` fan-out diagram** from Section 7 — one call splits into three tasks, one join when all finish.
>
> Three changes. `def` → `async def`. `time.sleep` → `await asyncio.sleep`. Loop → **`await asyncio.gather`**. That gather line is what we paste into the agent next.

**Notebook sections map (for editor / teleprompter):**

| On camera | Notebook section |
|-----------|------------------|
| Keyword table | §1 |
| Sync ASCII + run | §2–3 |
| `async def` / `await` prose | §4 |
| Async ASCII | §5 |
| Coroutine object demo | §6 |
| `gather` ASCII | §7 |
| Async run | §8 |
| One-frame diff | §9 |
| Bridge to agent | §10 |

**[Retention beat: viewer saw definitions, ASCII flow, and live numbers. Now Scene 8 opens `agent_core.py`.]**

---

## SCENE 8 — THE AGENT BUILD (7:30 – 10:30) | L4 real code

**On screen:** VSCode side-by-side — `agent_core.py` open. Show the sync agent loop, then the async one. Highlight only the diff.

**Spoken:**

> Same trick. Real agent. Open `agent_core.py`. The sync agent's tool execution is this loop —
>
> ```python
> for tc in assistant_msg.tool_calls:
>     result = _execute_tool_sync(tc.function.name, json.loads(tc.function.arguments))
>     messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
> ```
>
> Ten tool calls. Two seconds each. Twenty seconds, sequential.
>
> Now the async agent. Same task. Same model. Same tools. Five lines change —
>
> ```python
> results = await asyncio.gather(*[
>     _execute_tool_async(tc.function.name, json.loads(tc.function.arguments))
>     for tc in assistant_msg.tool_calls
> ])
> for tc, result in zip(assistant_msg.tool_calls, results):
>     messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
> ```
>
> The whole video is in those five lines. **`asyncio.gather`** — fire every tool, wait for all of them at once. Same answer back from the LLM. Same final itinerary. **Twelve seconds instead of thirty-three.**
>
> One file. Eighty lines for the chatbot UI. Eighty more for the agent core. Repo link in description — fork it tonight.

---

## SCENE 9 — PUSH TO THE LIMIT (10:30 – 11:30)

**On screen:** Both browser windows again. Bigger prompt this time — the **headline 5-city / 10-tool demo**.

**Spoken:**

> One more demo. Not the toy three-city version. The full prompt. Five cities — Hyderabad, Bangalore, Chennai, Mysore, Pondicherry. Weather and attractions for each. **Ten tool calls.**
>
> *(Hit Enter on both windows simultaneously.)*
>
> Sync chef. Ten dishes, one burner. **Thirty-two point eight seconds.**
>
> Async chef. Ten dishes, ten burners. **Eleven point eight seconds.**
>
> **Twenty-one seconds saved. Two point eight times faster.** On one query.
>
> Now multiply this by *one thousand queries a day* in a real product — that is **almost six hours of total user waiting time, gone, every day.** From one keyword.

---

## SCENE 10 — WHEN ASYNC HURTS (11:30 – 12:30) | L5 honest deferral

**On screen:** Sketchbook — three small warning callouts.

**Spoken:**

> One step deeper, then I am stopping. Async is not free. Three things will bite you in production.
>
> **One — rate limits.** Firing ten requests at once means your API provider sees ten at once. Free tier of OpenAI is twenty requests per minute. Hit that limit and your async agent is suddenly slower than the sync one. Add a semaphore — `asyncio.Semaphore(5)` — limits how many run at once. Engineers, that is your homework.
>
> **Two — order.** `asyncio.gather` does **not** preserve order in time, only in the result list. If your tools have dependencies — *get user, then get user's orders* — you do not parallelize. You run sequentially.
>
> **Three — debugging.** Async stack traces are harder to read than sync ones. Use `asyncio.run` carefully. Print early, print often.
>
> Same warnings every senior engineer learns on the job. Now you know them before you ship anything.

---

## SCENE 11 — CLIFFHANGER (12:30 – 13:30)

**On screen:** Face cam.

**Spoken:**

> Today we made **one** agent fast. Ten tools running in parallel. Same brain, more hands.
>
> **Next video — multiple agents working together.** Researcher agent talking to a writer agent talking to a critic agent. All running async. The same trick — but now between agents, not just between tools. That is what frameworks like **CrewAI** and **AWS Strands** are actually doing under the hood. We will build a tiny one in under a hundred lines.
>
> If today's video unlocked something for you — fork the repo, run both chatbots side by side tonight, swap the mock tools for real ones. Comment your timer numbers below. I read every comment.

---

## SCENE 12 — CTA (13:30 – 14:00)

**On screen:** Description link card + WhatsApp QR.

**Spoken:**

> Repo is in the description. WhatsApp community for serious AI learners — link below. Roadmap link. Subscribe so the next video reaches you.
>
> See you in the next one.



## RETENTION MAP (planning lens)

| Time | Beat | Why it holds |
|---|---|---|
| 0:00 – 0:50 | Live demo: 33s vs 12s side-by-side | Visual proof before any explanation |
| 0:50 – 1:20 | "I missed this in Phase 1" honesty | Trust + roadmap callback |
| 1:20 – 1:50 | LangChain + AWS Strands + CrewAI all use this | Authority drop without lecture |
| 1:50 – 3:30 | Chef analogy + timeline sketch | L1 — anyone can follow |
| 3:30 – 5:00 | Same picture for the actual agent | L2 — math becomes visceral |
| 5:00 – 6:30 | `async def`, `await`, coroutine vs subroutine + ASCII sync timeline | L3 — definitions beginners need |
| 6:30 – 8:00 | Notebook: sync run, async ASCII, micro-example, gather, exact 3x | L4 — code + flow diagrams |
| 8:00 – 10:30 | Real agent, 5-line diff | L4 — the payoff |
| 10:30 – 11:30 | Push to 10 tools, 21s saved | Visceral production framing |
| 11:30 – 12:30 | Three things that hurt in production | L5 — engineers stay |
| 12:30 – 13:30 | Multi-agent cliffhanger | Drives next click |
| 13:30 – 14:00 | CTA | Standard close |

**Highest-risk drop-off:** Scene 6 (definitions). Mitigation — keep it under 60 seconds, only two new words (subroutine, coroutine), and immediately cut to code.

---

## TITLE OPTIONS (CTR-tested formulas)

1. **I Made My AI Agent 3x Faster With One Python Keyword (2026)** ⭐ recommended — specific number, curiosity gap, year tag
2. The Async Trick Every AI Engineer Learns Too Late (2026)
3. Why Your AI Agent Is Slow — And One Keyword Fixes It (2026)
4. From 33 Seconds to 12 — One Line of Python (2026)
5. LangChain, CrewAI, AWS Strands All Use This. You Should Too. (2026)

**Final pick:** #1.

---

## THUMBNAIL BRIEF

**Layout:** classic 60/40 split, you on the right (chest-up, surprised reaction, looking up-left toward the numbers).

**Left side — two stacked screenshot cards:**

- TOP card — red border, big bold timer overlay: **🐢 33s** with the word **SYNC** in small caps below.
- BOTTOM card — green border, big bold timer overlay: **⚡ 12s** with the word **ASYNC** in small caps below.

**Center divider:** glowing yellow vertical bar with a giant white **3×** badge in the middle, slight tilt.

**Bottom-left badge (small, subtle):** *Phase 1.5 · Async*

**Title text bar (top of frame, 2 lines max):**
> ONE PYTHON KEYWORD
> **3× FASTER AGENT**

**Color rules:** follow `youtube/skills/03-visual-identity/THUMBNAIL_RULES.md` — channel red on the SYNC card, channel green on the ASYNC card, off-white background, navy text.

---

## SHORTS HOOKS (3 candidates, ≤45s each)

1. **The 5-line agent speedup** — open with the 33s vs 12s timer, cut to the `asyncio.gather` diff, end with "fork the repo, link below."
2. **Chef analogy in 30 seconds** — sketchbook only, one stove vs three burners, "your AI agent is the chef."
3. **The framework reveal** — three rapid ChatGPT screenshots showing LangChain/Strands/CrewAI all confirming async, end with "if every framework uses it, you should at least know what it is."

---

## REPO + ASSET CHECKLIST (for record day)

- [ ] `async_agent_demo/` venv works, both Streamlit apps boot on 8501 / 8502
- [ ] `.env` `openaiapikey` present (auto-loaded by `agent_core.py`)
- [ ] `minimal_demo.ipynb` runs cleanly, prints exact 6.01s and 2.00s
- [ ] Two browser windows pre-positioned side-by-side at 1920x1080 each
- [ ] Three ChatGPT screenshots ready: LangChain async, AWS Strands async, CrewAI async
- [ ] Sketchbook page set: chef A vs chef B, sync vs async timeline, three warnings
- [ ] On-screen lower-thirds: "Phase 1.5", "asyncio.gather", "Coroutine vs Subroutine"

---

## DESCRIPTION + TAGS + PINNED COMMENT

To be generated separately via `youtube/skills/10-description-generator/SKILL.md` after recording, using the published transcript. Keep the WhatsApp link reference fresh from `links.config.md`.

---

## NOTES TO SELF (from prep)

- The **3x** number is real and verified — do not round up to 5x on camera; the comments will catch it.
- The **21 seconds saved** number is the hero stat, not the multiplier. Lead with seconds saved, follow with multiplier.
- Honest disclosure in Scene 10 about LLM round-trip floor builds long-term trust with engineers — they will be the ones who stick around for the multi-agent video.
- All code is `gpt-4o-mini`. If asked in comments why not `gpt-5` — answer: "tool calling is fast and cheap on `4o-mini`, the lesson is the same on any model. Phase 5 covers reasoning models for agents."

