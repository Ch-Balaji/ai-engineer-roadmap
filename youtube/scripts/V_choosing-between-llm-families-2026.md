# Which AI Model Should You Actually Use? GPT, Claude, Gemini, Llama & More (2026)

**Full scene-by-scene video script** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway), 10 (description). Phase 2.5. Follows *Reading Benchmarks* (V012), bridges into Phase 3 (UI vs API).

> **Teaching style locked (V010–V012):** L1 obvious case → L2 plain story → L3 name the term → L4 one step deeper → L5 honest "saved for later". The framework is DERIVED on the sketchbook in front of the viewer, not asserted.
> **V013 spine (theory-first):** the whole video lives on one reframe — **"which model is best?" is the wrong question. Models are trade-off bundles.** Once you can name the 4 levers (cost · quality · speed · context), you can place ANY model — today's or next month's — in seconds, and decide when the choice matters and when it truly doesn't. Almost no code: this is a mental-model video.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V013 |
| Slug | `choosing-between-llm-families-2026` |
| Playlist | Phase 2 — LLM Mental Model |
| Target length | 16 min (hard cap 18) |
| Slot | Fri 7 PM IST |
| Previous video | AI Benchmarks — What Nobody Tells You (V012) |
| Next video | UI vs API — The Hinge Moment Most Beginners Miss (Phase 3 opener) |
| Medium | **Sketchbook-driven theory.** One cost-chart graphic (rendered from `youtube/notebooks/V013_model_comparison.ipynb`), no live coding on camera. |

## Roadmap Mapping (skill 04)

```
- Phase: 2 — Mental Model of an LLM
- Sections covered: 2.5 (Comparing the major model families + the trade-off levers)
- Prerequisites needed: 2.1–2.4 (How an LLM thinks, reasoning vs base, reading benchmarks)
- Prerequisite videos: V010, V011, V012
- Capstone contribution: no (feeds Phase 3 API model-selection and Phase 4 RAG model choice)
- End state: viewer can look at ANY model release, place it on the 4-lever map, and decide
  in seconds whether to switch — a skill that survives every future launch.
- This is a Phase 2 closer-companion to V012. Tease Phase 3 (UI vs API) at the end.
```

## Why this video (now)

| Reality (June 2026) | What it means for the script |
|---|---|
| V012 taught "read evals + build a micro-eval"; the obvious next question is "okay, so WHICH family do I even start with?" | This video is the payoff — go from *judging* a model to *choosing* one. |
| Every other channel does "GPT-5.5 vs Gemini 3 vs Claude vs Llama" spec recitals — dead in 60 days | Teach the **4 levers** + the **"when it doesn't matter"** punchline. Families are examples only. The levers are evergreen. |
| Beginners agonize over model choice for tasks where it's irrelevant, then under-think it where it's critical (cost at scale, latency UX, long-doc, privacy) | The "matters vs doesn't matter" act is the channel's edge — make it the memorable close. |
| Open-weight models (Llama, Mistral, DeepSeek, Qwen) now genuinely compete; self-hosting is real | Group by *closed frontier* vs *open-weight you can self-host* — that grouping IS a lever (control / privacy / cost). |

## Playlist Callback Map (3 references, ~30 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 1:00 | Backward bridge | V012 — *Benchmarks* | "You can judge a model now — so which do you even start with?" |
| 2 | 8:00 | Lean-in | V011 2×2 | The 4-lever map extends the reasoning-vs-base 2×2 |
| 3 | 15:00 | Cliffhanger | Phase 3 — *UI vs API* | "You can pick a model — now learn to actually talk to it" |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–1:00 | **Hook — same answer, 222x the price** | Sketchbook → two identical answer cards → cost bar graphic |
| 1:00–2:00 | Bridge + V012 callback | Sketchbook — the Phase-2 box chain |
| 2:00–3:30 | The reframe: models are trade-off bundles | Sketchbook full-screen |
| 3:30–7:00 | The two tiers: closed frontier vs open-weight | Sketchbook + family logos |
| 7:00–11:30 | **The 4 levers (HERO)** | Sketchbook — draw the 4-axis diagram live |
| 11:30–13:30 | Mapping levers to real use cases | Sketchbook — 3 worked examples |
| 13:30–15:00 | When it matters vs when it doesn't | Sketchbook — two-column split |
| 15:00–16:00 | Cheat sheet + decision rule | Sketchbook full-screen (screenshot moment) |
| 16:00–16:45 | Cliffhanger to V014 + outro | Face cam |

## Title + Thumbnail Brief (skill 06)

```
- Title formula: question-hook + family names for SEO
- Final title: Which AI Model Should You Actually Use? GPT, Claude, Gemini, Llama & More (2026)
- Char count: 73
- A/B title: When Your AI Model Choice Matters (And When It Doesn't) — 2026 (60 chars)
- Subject pose: Confident, mid-gesture as if weighing two options in both hands
- Outfit: Brown bomber jacket + black zip-up (Phase-2 series identity, pairs with V010/V011/V012)
- Background: Black + circuit overlay
  Center: a balance scale — left pan stacked with model logos (GPT/Claude/Gemini),
  right pan with open-weight logos (Llama/Mistral/DeepSeek/Qwen)
- Primary text (white, Anton ALL CAPS, top):
    WHICH MODEL?
- Highlight text (yellow + brush band, center BIG):
    222x
- Smaller text under it:
    same answer, different price
- Telugu badge (red, bottom-right):
    "ఇది చాలా మందికి తెలియదు"
    (translation: "Most people don't know this")
- Social-proof badge (top-left):
    "8+ YEARS IN AI"
- Note: ONE yellow element only (222x). Continues the series' single-yellow-word system
  (V011 "WHICH WINS?", V012 "LIE").
```

---

## HOOK FACTORY — 5 drafts (skill 07), recommended pick locked below

```
HOOK A — Personal Story
"For years I picked tools the way most people pick an AI model today — grab the biggest
name and assume it's the right call. On a mainframe that mistake cost me three years.
With models it can cost you a two-hundred-x bill for an answer you could've had for free.
Today: how to never overpay for a model again."
[Visual: sketchbook — "BIGGEST NAME" with a red X, then "RIGHT TOOL" with a green check]

HOOK B — Production Incident
"A team I know ran every request through the most expensive frontier model — top of the
board. Their task? Summarizing support tickets. They burned thousands a month on
something a free open model did identically. The model wasn't wrong. The choice was."
[Visual: an invoice with a big number → cut to two identical summaries side by side]

HOOK C — Live Demo First / Reveal (RECOMMENDED)
"Same question. Two different AI models. Same answer — word for word. But this one costs
two hundred and twenty-two times more than this one. Same task, 222x the price, and you
genuinely can't tell the outputs apart. In the next 16 minutes: the four levers that
explain that gap, and how to pick the right model in seconds — for any model that drops next."
[Visual: two identical answer cards side by side → a bar chart snaps in: $2.70 vs $600/mo, "222x" stamped between]

HOOK D — Comment Callback
"After the benchmarks video, the same question kept coming: 'Okay, I can read a leaderboard
now — but which one do I actually USE? GPT? Claude? Gemini? Llama?' That's the right
question. And most channels answer it with a spec sheet that's dead in two months.
Today you get the framework instead — the one that never expires."
[Visual: composite comment "but which model do I pick??" → V012 thumbnail lower-third]

HOOK E — Shock Statistic
"The same task can cost you two dollars a month — or six hundred. Same input, same output,
a 222x difference, and most of the time you can't tell the answers apart. That gap hides
four levers nobody explains: cost, quality, speed, context. Learn them and you'll pick
the right model in seconds."
[Visual: bar chart — $2.70 bar beside a $600 bar, "222x" stamped between]
```

**PICK: HOOK C (Reveal).** Why: it opens on a concrete, defensible number (222x, sourced from our own cost table), creates an instant knowledge gap ("how can the same answer cost 222x?"), and sets up the 4-lever payoff directly. V012 used Hook B (incident), so C keeps the rotation fresh. The 222x figure is a *visual* (two answer cards + a bar chart), not a live coding segment — keeps this a theory video. Fallback: Hook E (same number, pure chart) if the side-by-side answer cards aren't designed in time.

---

## FINAL HOOK — Same Answer, 222x the Price (LOCKED)

> *[Open on two clean cards, side by side, each showing the identical one-sentence summary of the same prompt. A beat. Then a bar chart slides up underneath: a tiny $2.70 bar next to a towering $600 bar. A yellow "222x" stamps between them.]*
>
> **Spoken:**
>
> "Look at these two answers. Same question. Two different AI models. And the answer is — word for word — basically identical.
>
> Now look at the price. This one costs two dollars a month to run at scale. This one? Six hundred. **Same answer. Two hundred and twenty-two times the cost.**
>
> **[Cut to face cam.]**
>
> So here's the uncomfortable truth: most of the time, the model everyone tells you to use is the wrong one — you're overpaying for quality you can't even see. But *sometimes* picking the cheap one will wreck your product.
>
> Today I'm going to give you the one mental model that tells the difference. Four levers — cost, quality, speed, context. Learn them once, and you'll pick the right model in seconds, for GPT, Claude, Gemini, Llama — and whatever drops next month. No spec sheets. No black box."

---

## SCENE 1 — HOOK + STAKES (0:00 – 1:00)

**On screen:** Two answer cards → cost bar chart (222x) → face cam (as above).

**Retention beat:** A shocking, concrete number in the first 5 seconds (222x), a contrarian claim ("the model everyone recommends is usually wrong"), and a promise (4 levers, any future model). Three reasons to stay before 1:00.

---

## SCENE 2 — BRIDGE + V012 CALLBACK (1:00 – 2:00)

**On screen:** Sketchbook. Phase-2 box chain: `API → Tokens → Trained → 3 Dials (V010) → Reasoning vs Base (V011) → Read Benchmarks (V012) → [TODAY: PICK ONE]`. CapCut lower-third: V012 thumbnail.

**Spoken:**

> Quick context. Last video — *AI Benchmarks, What Nobody Tells You* — you learned to read a leaderboard without getting tricked, and to build a tiny eval on your own task. You can now *judge* whether a model is good.
>
> But a lot of you replied with the obvious next question: *"Okay — I can judge a model. But which one do I actually pick? GPT? Claude? Gemini? One of the open ones like Llama or DeepSeek?"*
>
> That's today. And I'm not going to hand you a ranking — rankings die in two months. I'm going to hand you a **lens** that works on every model, forever. By the end, a new model could drop tomorrow with a name you've never heard, and you'll know exactly where it fits and whether you should care.

---

## SCENE 3 — THE REFRAME: "WHICH IS BEST?" IS THE WRONG QUESTION (2:00 – 3:30) | L3 name the frame

**On screen:** Sketchbook full-screen. Write the question **"Which model is best?"** at the top — then draw a big red X through it. Underneath, write: **"Best at WHAT, for WHICH constraint?"** Then draw a single box and label it **"a model = a bundle of trade-offs."**

**Spoken:**

> Before any model names, get this one reframe — it's the whole video.
>
> When a beginner asks *"which model is best?"*, they're imagining there's a single winner — like one phone is the best phone. There isn't. Asking "which model is best" is like asking "what's the best vehicle." Best for *what*? A bicycle, a truck, and an ambulance are all "best" — for completely different jobs.
>
> So cross that question out. A model is not a score on a chart. **A model is a bundle of trade-offs.** Every model on earth is making a deal between four things — and no model wins all four. The moment you can *name* those four, you stop asking "which is best" and start asking "best for my constraint" — which is a question that actually has an answer.
>
> *Honesty marker:* yes, some models are just better than others on raw quality. But raw quality is only one of the four, and it's the one you pay the most for. Most real decisions are won or lost on the other three.

**[CapCut sticker: `"Which model is best?" → wrong question. A model = a bundle of trade-offs. Ask: best for WHICH constraint?`]**

---

## SCENE 4 — THE FAMILIES IN TWO TIERS (3:30 – 7:00) | L1 fast, grouped by who they're for

**On screen:** Sketchbook. Draw a horizontal line splitting the page. Top half: **CLOSED FRONTIER** (logos: GPT, Claude, Gemini). Bottom half: **OPEN-WEIGHT** (logos: Llama, Mistral, DeepSeek, Qwen). Drop each name in as you say it.

**Spoken:**

> You don't need to memorize seven companies. You need *two tiers* — because the split between them is itself the first big decision.
>
> **Tier one — closed frontier. You rent it through an API. It just works.**
> - **GPT family (OpenAI)** — the all-rounder. Massive ecosystem, the most tools and integrations, strong at coding and agents. The "nobody got fired for picking it" option. Comes in sizes — nano, mini, full, pro — that span cheap-and-fast to slow-and-brilliant.
> - **Claude family (Anthropic)** — the one engineers reach for to *write and reason about code*, and for long, careful, steerable answers. Sizes: Haiku (cheap/fast), Sonnet (the workhorse), Opus (the heavy hitter). Huge context.
> - **Gemini (Google)** — multimodal-native: text, images, audio, video in one model. The **biggest context window** of the bunch, and a free tier that's genuinely useful. Deep Google-ecosystem ties.
>
> One sentence to remember the tier: *closed frontier = maximum convenience and top-end quality, but you pay per token and your data leaves your machine.*
>
> **Tier two — open-weight. You can download the weights and run them yourself.**
> - **Llama (Meta)** — the open default. Biggest community, the model everyone fine-tunes and builds on first.
> - **Mistral (France)** — small models that punch far above their size. Efficient, EU-based — the privacy-and-compliance pick.
> - **DeepSeek (China)** — frontier-level *reasoning and coding* at a fraction of the price, open weights, and a huge context window. The one that keeps detonating the cost floor.
> - **Qwen (Alibaba)** — strongest multilingual family, excellent at coding and math, and it ships in *every* size from tiny to massive — so there's a Qwen for a Raspberry Pi and a Qwen for a server farm.
>
> One sentence for this tier: *open-weight = control, privacy, and near-zero marginal cost — but you (or your provider) own the running of it.*
>
> Notice I didn't rank them. I grouped them by **who they're for.** Because the closed-vs-open split already decides one of your four levers before you even compare numbers — control and privacy. That's lever zero. Now let's name the four that decide the rest.

**[CapCut sticker: `CLOSED FRONTIER (rent it): GPT · Claude · Gemini  |  OPEN-WEIGHT (own it): Llama · Mistral · DeepSeek · Qwen`]**

---

## SCENE 5 — THE 4 LEVERS (7:00 – 11:30) | THE HERO | L3 name → L4 one step deeper

**On screen:** Sketchbook. Draw a square. Label the four corners one at a time: **COST**, **QUALITY**, **SPEED**, **CONTEXT**. As each is explained, draw a small slider/dial next to it. End the scene by drawing arrows showing you can't push all four to max — pulling one up drags others down.

**Spoken (intro):**

> Here's the engine of the whole video. Every model is a setting of **four levers.** You cannot max all four — push one up and at least one other drops. Learn these four and you can read *any* model, ever.

**Lever 1 — COST.** *(Draw the dial.)*

> Lever one — **cost.** Measured in dollars per million tokens, and here's the part beginners miss: input and output are priced *separately*, and output is usually three-to-five times more expensive than input. A frontier model can be a hundred times pricier than a small open model for the *exact same task*. Remember the opening — 222x. That gap is almost pure cost lever. Cost is the lever that doesn't matter at all when you're testing with ten requests, and the *only* lever that matters when you're running ten million.

**Lever 2 — QUALITY.** *(Draw the dial.)*

> Lever two — **quality.** The reasoning and coding ceiling — can it solve the genuinely hard, multi-step problem? This is the lever everyone fixates on and the one you overpay for. Here's the nuance from last video: on *easy* tasks every model is basically maxed out — quality is flat, so paying for it is pure waste. Quality only separates the models when the task is *hard*. So the real question isn't "is this model smart" — it's "is my task hard enough to need the smart one."

**Lever 3 — SPEED.** *(Draw the dial.)*

> Lever three — **speed.** Two parts: how fast the first word appears, and how many tokens per second after that. This is invisible in a demo and brutal in production. If a user is staring at a loading spinner, speed is everything. If an agent makes twenty model calls in a loop, a slow model multiplies that delay twenty times. Providers like Groq exist *entirely* to crank this one lever — same open model, several times faster.

**Lever 4 — CONTEXT LENGTH.** *(Draw the dial.)*

> Lever four — **context length.** How much you can stuff into a single request — the model's short-term memory. A small context fits a paragraph; the big ones — Gemini, Claude, DeepSeek — fit entire books or codebases. You need this lever the moment you're doing long documents, whole-repo code questions, or RAG. And a caveat I'll fully unpack in Phase 7: a *bigger* context window doesn't mean the model actually *uses* all of it well — quality can sag in the middle. So context length is a ceiling, not a guarantee.

**The tension (the key beat).** *(Draw the arrows: pulling COST down drags QUALITY or SPEED.)*

> Now the whole point. **These four fight each other.** The cheapest, fastest models give up quality. The highest-quality models cost the most and run the slowest. The giant-context models cost more to feed. There is no model with max quality, min cost, max speed, and max context — if there were, it'd be the only model and this video wouldn't exist.
>
> So choosing a model is not "find the best." It's *"decide which lever I care about most for THIS task, then take the cheapest model that's good enough on the others."* That sentence is the entire skill.

**[CapCut sticker: `THE 4 LEVERS: Cost · Quality · Speed · Context. You can't max all four. Pick the one your task needs, then take the cheapest model that's good enough on the rest.`]**

**[Optional B-roll: drop in the cost bar chart rendered from `V013_model_comparison.ipynb` here — the $2.70 vs $600 spread — as proof of the cost lever. Static image, not a code walkthrough.]**

---

## SCENE 6 — MAPPING LEVERS TO REAL USE CASES (11:30 – 13:30) | L4 worked examples

**On screen:** Sketchbook. Three rows, each: a TASK on the left → which LEVER dominates → which TIER of model wins. Draw them one at a time.

**Spoken:**

> Let's make this concrete with three real jobs. Watch which lever wins each time — and notice the "best" model changes every row.
>
> **Job one — classify or extract from a million support tickets a day.** The task is easy, the volume is enormous. Which lever? **Cost**, by a mile. Quality is already maxed on an easy task, so paying frontier prices here is lighting money on fire. Winner: a small open-weight model — a tiny Llama, Mistral Small, DeepSeek Flash. Cheap and fast wins.
>
> **Job two — answer questions over a 300-page contract, or your entire codebase.** Which lever? **Context**, then quality. A cheap model with a small window literally cannot hold the document. Winner: a big-context model — Gemini, Claude, or DeepSeek. You pay more per call, but no cheaper model can even do the job.
>
> **Job three — a coding agent that plans, edits files, and loops twenty times.** Which levers? **Quality and speed, together** — it has to be right *and* it runs many calls back-to-back. Cost matters but comes third. Winner: a strong-but-fast tier — Claude Sonnet, a mid GPT, or DeepSeek for the budget version. You accept a higher bill to avoid a dumb agent burning loops.
>
> Three jobs. Three different winners. Same four levers. *That* is why "what's the best model" has no answer — and "what's the best model *for this constraint*" always does.

**[CapCut sticker: `High-volume easy → COST → small open. Long docs/code → CONTEXT → big-window. Agent loop → QUALITY+SPEED → strong-fast tier.`]**

---

## SCENE 7 — WHEN IT MATTERS vs WHEN IT DOESN'T (13:30 – 15:00) | the punchline | L5 honest

**On screen:** Sketchbook. Vertical split. Left header (green): **DOESN'T MATTER — relax.** Right header (red): **MATTERS A LOT — choose carefully.** Fill each column live.

**Spoken:**

> Now the most freeing thing I can tell a beginner. Most of the time — **the choice doesn't matter, and you're wasting energy agonizing over it.**
>
> **It doesn't matter when:** the task is easy — summarizing, basic Q&A, simple formatting. You're prototyping and just want it to work. The volume is low — a few hundred calls. In all of these, grab whatever's cheapest or whatever has a free tier — a Gemini Flash, a small open model — and move on. The differences are rounding errors.
>
> **It matters a lot when one of these is true:**
> - **Scale** — millions of calls. Now the cost lever dominates and a wrong pick is a five-figure bill. *(Callback: the $50k bill from V011.)*
> - **Latency** — a user is waiting, or an agent loops many times. Speed lever.
> - **Long inputs** — big documents, whole codebases, RAG. Context lever.
> - **Privacy or compliance** — the data can't leave your servers. Now you're forced into open-weight, self-hosted — Llama, Mistral, Qwen on your own box. This single constraint can override all three other levers.
> - **Genuinely hard reasoning or coding** — the frontier quality ceiling actually pays for itself.
>
> So the honest rule: *don't optimize the model until you're in the right-hand column.* If you're on the left, pick cheap and ship. If you're on the right, that's when you pull out the lens — and your own eval from last video — and choose deliberately.

**[CapCut sticker: `Doesn't matter: easy task · prototyping · low volume → pick cheap, ship. Matters: scale · latency · long context · privacy · hard reasoning → choose with the levers.`]**

---

## SCENE 8 — CHEAT SHEET + DECISION RULE (15:00 – 16:00) | screenshot moment

**On screen:** Sketchbook full-screen, clean, held long enough to screenshot.

```
HOW TO PICK AN AI MODEL (without overthinking it)

STEP 0 — Closed or open?
   Data can't leave your servers? → open-weight, self-host (Llama/Mistral/Qwen). Done.
   Otherwise → closed frontier is fine to start.

STEP 1 — Which ONE lever does this task care about most?
   COST     → high volume, easy task        → small open (Llama/Mistral/DeepSeek-Flash)
   QUALITY  → hard reasoning / coding        → frontier (GPT / Claude Opus / DeepSeek Pro)
   SPEED    → real-time UX / agent loops     → Groq-hosted open, or Flash/Haiku tiers
   CONTEXT  → long docs / whole codebase     → Gemini / Claude / DeepSeek (big window)

STEP 2 — Take the CHEAPEST model that's good enough on the other three.

STEP 3 — Prove it on YOUR task (your 20-example micro-eval from last video).
         Only move up a tier when the eval — not the vibes — tells you to.

RULE: don't pick the "best" model. Pick the right lever, then the cheapest model
      that clears your bar. Names change every month. The 4 levers don't.
```

**Spoken:**

> Screenshot this. This is the entire video on one page — closed-or-open first, then the one lever your task cares about, then the cheapest model that's good enough, then prove it on your own data.
>
> And notice the rule at the bottom: you are *never* picking the best model. You're picking the right *lever*, then the cheapest model that clears your bar. Do that, and the next time a shiny new model launches with a breathless headline, you won't panic — you'll just ask "which lever did it move, and do I care?" Ninety percent of the time, the answer is "not for what I'm building."

---

## SCENE 9 — CLIFFHANGER TO PHASE 3 + OUTRO (16:00 – 16:45)

**On screen:** Face cam.

**Spoken:**

> That's Phase 2 fully closed. You now have the complete mental model of an LLM — how it thinks, the three dials, reasoning versus base, how to read benchmarks, and now how to *choose* a model like an engineer instead of a fan.
>
> But here's the gap. Everything so far, you've done by *chatting* — typing into a box and reading a reply. Real products don't run in a chat window. They run through the **API** — code talking to the model, no human in the loop. And that jump, from the chat UI to the API, is the exact moment most beginners freeze.
>
> That's Monday — Phase 3 opens. *UI vs API — the hinge moment most people miss.* Subscribe so it reaches you at 7 PM.
>
> And tell me in the comments — **what's your current daily-driver model, and which of the four levers actually drove that choice?** Be honest if the answer is "I just used the popular one." I read every comment. Out.

---

## Production Beat Sheet

| Time | Beat | Reason |
|---|---|---|
| 0:00 | "Same answer, 222x the price" | Strongest concrete 5-sec stake |
| 2:00 | Reframe: model = trade-off bundle | The frame the whole video hangs on |
| 7:00 | The 4 levers drawn live | The hero teaching moment |
| 9:30 | "These four fight each other" tension | The insight that makes it click |
| 11:30 | 3 use cases, 3 different winners | Proof the thesis is real |
| 13:30 | "Most of the time it doesn't matter" | Contrarian, freeing, shareable |
| 15:00 | Cheat sheet | Screenshot moment |
| 16:00 | Phase 3 cliffhanger | Next-video retention |

## Skills used

| Skill | Application |
|---|---|
| 01 voice | Senior-but-honest; "I'm simplifying here" (Scene 3), "no black box" once (Hook) |
| 02 story-bank | STORY_INFOSYS available as Hook A fallback — not used as opener (Hook C locked), so no cooldown spent |
| 04 roadmap-source | Phase 2 / 2.5; prereqs V010–V012; closes Phase 2; teases Phase 3 (UI vs API) |
| 06 title+thumbnail | Question formula; ONE yellow element (222x); Phase-2 series visual continuity |
| 07 hook-factory | 5 hooks generated; Hook C (reveal) locked, E as fallback |
| 09 monetization | Phase 1/early — no pitch. Soft WhatsApp link in pinned comment only |
| 10 description | Run skill 10 on the SRT after recording — keyword: "which AI model to use 2026" |

## What I deliberately cut (and where it goes)

| Cut | Why | Where it goes |
|---|---|---|
| Live coding / API walkthrough | This is a mental-model video; code would dilute it | Notebook stays as a companion + cost-chart source only |
| "Lost in the middle" long-context degradation | Owns Phase 7 (Context Engineering) | Phase 7 |
| Fine-tuning open models to close a quality gap | Phase 8 territory | Phase 8 |
| Specific current rankings / which model is #1 today | Ages in 60 days; not the channel's edge | Off-roadmap "Industry Pulse" only if a drop justifies it |
| Self-hosting mechanics (vLLM, Ollama, GPU sizing) | Setup/tools territory | "Setup & Tools" bonus video |

## Pre-Record Checklist

- [ ] Two identical-answer cards designed for the hook (same prompt, two models) — else fall back to Hook E (chart only)
- [ ] Cost bar chart rendered from `youtube/notebooks/V013_model_comparison.ipynb` ($2.70 vs $600, 222x) — **re-run the morning of; prices move**
- [ ] Confirm the 222x figure matches the rendered chart and the spoken number
- [ ] Sketchbook drawn in advance: reframe, two tiers, the 4-lever square, 3 use cases, matters/doesn't split, cheat sheet
- [ ] Family logos as CapCut stickers: GPT, Claude, Gemini, Llama, Mistral, DeepSeek, Qwen
- [ ] V012 thumbnail ready for the Scene 2 lower-third
- [ ] Voice rules: no "guys", direct address, English jargon preserved (skill 01)
- [ ] Phase-1 monetization respected: no pitch; WhatsApp link in pinned comment only
- [ ] Final cut ≤ 18:00 — if long, trim Scene 4 family elaboration first (keep the tier split, cut per-model detail)

## Post-Record Checklist

- [ ] Length 16–18 min
- [ ] ≥3 medium switches (sketchbook / cost-chart graphic / face cam)
- [ ] Burned captions, yellow on keywords ("4 levers", "222x", "trade-off bundle", lever names)
- [ ] English subtitles file uploaded
- [ ] Cheat-sheet frame held long enough to screenshot
- [ ] End screen → Phase 3 opener + Phase 2 playlist
- [ ] No story used as opener → nothing to log in STORIES.md

---

## Description (for YouTube upload — or regenerate with skill 10 after recording)

```
Same question, two AI models, the same answer — and a 222x difference in price. "Which model is best?" is the wrong question. Here's the mental model that actually tells you which AI model to use: the four levers — cost, quality, speed, and context — and when your model choice matters vs when it truly doesn't.

In this video:
• Why "which model is best?" is the wrong question — a model is a bundle of trade-offs
• The families in two tiers — closed frontier (GPT, Claude, Gemini) vs open-weight (Llama, Mistral, DeepSeek, Qwen)
• The 4 levers that decide every model choice: cost · quality · speed · context — and why you can't max all four
• 3 real jobs, 3 different "best" models — mapping levers to use cases
• When model choice doesn't matter (and you're overthinking it) vs when it really does
• The one-page cheat sheet to pick a model in seconds — for any model that launches next

🗺️ Where this fits in the Roadmap:
Phase 2 — Mental Model of an LLM
Section: 2.5 (Comparing the major model families)
Prerequisite videos: V011 (Reasoning vs Base), V012 (Reading Benchmarks)
Next video: UI vs API — The Hinge Moment Most Beginners Miss (Phase 3 opener)
Full Roadmap: https://ch-balaji.github.io/ai-engineer-roadmap/

⏱️ Timestamps:
0:00 — Same answer, 222x the price
1:00 — Why this matters (V012 callback)
2:00 — "Which model is best?" is the wrong question
3:30 — The families in two tiers
7:00 — The 4 levers (cost, quality, speed, context)
11:30 — 3 jobs, 3 different winners
13:30 — When it matters vs when it doesn't
15:00 — The cheat sheet
16:00 — Phase 3 starts Monday

📚 Resources:
Free AI Engineer Roadmap 2026 — https://ch-balaji.github.io/ai-engineer-roadmap/
Agentic AI Playlist — https://youtube.com/playlist?list=PL8qeqP57-QAa048dYOZSvGwdAGqEMFMkc

📬 Connect:
Join the WhatsApp Community — https://chat.whatsapp.com/GASHZYf7wBA23nQvb39lIP
LinkedIn — https://www.linkedin.com/in/balaji-chippada-0317/
Instagram — https://www.instagram.com/balajichippada

If this helped, subscribe so the next free lesson reaches you.

#AI #AIEngineer #AIRoadmap2026
```

(Pinned comment idea): "The 4 levers I check before picking any model: cost · quality · speed · context — then the cheapest one that clears my bar on MY task. What's your daily-driver model, and which lever actually drove that choice? 👇"





