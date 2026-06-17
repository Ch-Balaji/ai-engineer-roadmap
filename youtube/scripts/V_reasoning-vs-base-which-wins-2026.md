# Reasoning vs Base Models — Which Wins When? (2026)

**Full scene-by-scene video script** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway), 10 (description). Follows *How to Control LLM Output* in the Phase 2 playlist.

> **Teaching style locked (from V010):** L1 analogy → L2 plain story → L3 name the term → L4 one step deeper → L5 honest "saved for later".
> **V011 twist:** the framework is DERIVED from examples in front of the viewer, not asserted. Examples first → pick + reasoning → pattern reveal → apply. Senior-engineer mode.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V011 |
| Slug | `reasoning-vs-base-which-wins-2026` |
| Playlist | Phase 2 — LLM Mental Model |
| Target length | 14–15 min (hard cap 16) |
| Slot | Wed 7 PM IST |
| Previous video | How to Control LLM Output (V010, the 470× video) |
| Next video | Reading Benchmarks Without Getting Tricked + Daily Driver (V012) |

## Roadmap Mapping

```
- Phase: 2 — Mental Model of an LLM
- Section covered: 2.3 (Reasoning vs base — when each wins)
- Prerequisites: V009 (How ChatGPT Is Trained), V010 (Three dials)
- Capstone contribution: no
- End state: viewer can pick the right CLASS of model for any task,
  with a 2x2 framework that survives future model releases.
```

## Why this video (now)

| Reality (June 2026) | What it means for the script |
|---|---|
| V010 shipped — viewers know `reasoning.effort` exists but don't know WHEN to use it | This video gives them the decision, not more theory |
| Most YouTube content is "GPT-5 vs Claude vs Gemini" benchmark recital — ages in 60 days | Frame by **task class**, not by model name. Framework outlasts any model. |
| Production agent builders are quietly burning money on reasoning models in routing loops | The agent-loop senior insight (~10:00) is the differentiator nobody else teaches |
| Viewer just absorbed 21 min of cost-heavy content in V010 | Lighter touch, more decision-density, faster pace |

## Playlist Callback Map (4 references, ~30 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 0:50 | Backward bridge | V010 — *How to Control LLM Output* | Continuity from 3 dials |
| 2 | 4:30 | Lean-in | V010 reasoning.effort | Reuse the "hidden tokens" mental model |
| 3 | 11:00 | Forward reference | Phase 5 — Agent Loop | Agent-loop insight sets up Phase 5 |
| 4 | 13:45 | Cliffhanger | V012 — *Benchmarks + Daily Driver* | Validation hook |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–1:00 | **Hook — the $50K/month agent that died of reasoning** | Sketchbook → terminal screenshot |
| 1:00–1:30 | Bridge + V010 callback | Sketchbook — series boxes |
| 1:30–3:00 | Example 1: Spam classification | Jupyter side-by-side |
| 3:00–4:30 | Example 2: Customer tone rewrite | Jupyter |
| 4:30–6:00 | Example 3: Python bug debug | Jupyter — base says "looks fine," reasoning catches it |
| 6:00–7:30 | Example 4: "I was wrong" — contract field extraction | Jupyter — looks complex, isn't |
| 7:30–9:30 | **Framework reveal — the 2×2** | Sketchbook full-screen, drawn live |
| 9:30–11:00 | The agent-loop senior insight | Sketchbook agent loop diagram |
| 11:00–13:00 | Apply — 3 quick questions on screen | Sketchbook + voiceover |
| 13:00–13:45 | Cheat sheet — decision tree | Sketchbook — screenshot moment |
| 13:45–14:30 | Cliffhanger to V012 | Face cam |
| 14:30–15:00 | Subscribe / outro | Face cam |

## Title + Thumbnail Brief (skill 06)

```
- Title formula: T6 (X vs Y — Which Wins in 2026)
- Final title: Reasoning vs Base Models — Which Wins When? (2026)
- Char count: 50
- A/B title: Stop Defaulting to GPT-5 — When Base Models Win (2026) (54 chars)
- Subject pose: Standing center, palms up in "depends" shrug-smirk, head slight tilt
- Outfit: Brown bomber jacket + black zip-up (locked)
- Background: Black + circuit overlay
  Left half: cool purple/blue glow + a brain icon labeled REASONING
  Right half: warm orange/green glow + a lightning icon labeled BASE
- Primary text (white, Anton ALL CAPS, top):
    REASONING vs BASE
- Highlight text (yellow + brush band, center BIG):
    WHICH WINS?
- Smaller text under it:
    (it's not what you think)
- Telugu badge (red, bottom-right):
    "ఏ model ఎప్పుడు?"
    (translation: "Which model, when?")
- Tech-stack icons (bottom):
    GPT-5 · GPT-4o-mini · Claude 4.8 · Gemini · Reasoning Models
- Composition pairs with V010's red/green 470× thumbnail → starts a recognizable Phase-2 series visual identity
```

---

## FINAL HOOK — The $50K Agent That Died of Reasoning (LOCKED)

> *[Open on sketchbook. Three boxes drawn: USER → AGENT → ANSWER. Each box labeled "GPT-5, reasoning.effort=high". Above: "$50,000 / month". Below: "8 second latency / message". Red X drawn over the whole thing.]*
>
> **Spoken:**
>
> "Last quarter, a startup shipped a customer support agent. They picked the best model on every step — GPT-5, reasoning effort high. Because someone said *use the best.*
>
> Forty-five days later — the bill was fifty thousand dollars a month. Average response time — **eight seconds**. Users started churning. And the founder asked the engineer one question: *why is our cheapest competitor faster and better than us?*
>
> **[Cut to face cam.]**
>
> Because the engineer made the senior mistake. Not the junior one — *the senior one*. He knew how to control the model. He just didn't know **which model to pick for which step**.
>
> Today — four questions, my actual picks for each, and the two-by-two that makes those picks obvious. Stick around — there's a fourth example where **I would have picked wrong last year**. The day I unlearned that mistake is the day I stopped burning money on reasoning models."

---

## SCENE 1 — HOOK + STAKES (0:00 – 1:00)

**On screen:** Sketchbook → face cam (as above).

**Retention beat:** Viewer has a fear ($50K), a promise (4 examples + framework), and a teaser (one wrong pick). 3 reasons to stay.

---

## SCENE 2 — BRIDGE + V010 CALLBACK (1:00 – 1:30)

**On screen:** Sketchbook with 4 boxes: `API → Tokens → Trained → Controls (V010) → [TODAY: PICK]`. CapCut lower-third: V010 thumbnail.

**Spoken:**

> Quick context. Last video — *How to Control LLM Output* — we learned the **three dials**: creativity, effort, layout. We saw how the junior burns 470 times the cost of the senior on the same answer.
>
> But there was a question I didn't answer last time: **which model do you even reach for in the first place?** Today — that exact decision. Four real questions. My pick on each. And by the end you'll see a pattern that lets you pick for *any* model — including the ones that haven't launched yet.

---

## SCENE 3 — EXAMPLE 1: SPAM CLASSIFICATION (1:30 – 3:00) | L1 obvious case

**On screen:** Jupyter, two cells side by side. Same prompt: *"Is the following email spam? Answer yes or no.\n\n{email}"*

- Cell A: `model="gpt-4o-mini", temperature=0`
- Cell B: `model="gpt-5", reasoning={"effort": "high"}`

**Choreography:**
- Run both. Both say `no`.
- On-screen sticker: Cell A cost = `$0.000006`, latency `0.4s`. Cell B = `$0.0028`, latency `4.7s`.

**Spoken:**

> Task one. *Classify this email as spam — yes or no.*
>
> Both models say `no`. Same answer. But look at the numbers — base model: half a second, six millionths of a dollar. Reasoning model: nearly five seconds, four hundred seventy times the cost.
>
> **My pick: GPT-4o-mini, temperature zero.** Why? Because *there is no chain of thought here*. The answer is one word. Paying for hidden reasoning tokens on a yes/no question is — and we saw this in V010 — lighting money on fire.
>
> **Rule we just discovered: deterministic + simple = base model, temperature zero.**

**[CapCut sticker (3 sec): `Rule 1 — deterministic + simple → BASE`]**

---

## SCENE 4 — EXAMPLE 2: CUSTOMER SUPPORT TONE REWRITE (3:00 – 4:30) | L1 creative side

**On screen:** Jupyter. Prompt: *"Rewrite this angry customer email in a calm, empathetic tone:\n\n{angry email}"*

- Cell A: `model="gpt-4o-mini", temperature=0.7`
- Cell B: `model="gpt-5", reasoning={"effort": "low"}`

**Choreography:**
- Run both. Both produce a calm rewrite. Reasoning model is slightly more verbose, more "corporate."
- Cost stickers: Cell A `$0.000040`, Cell B `$0.0011`.

**Spoken:**

> Task two. Rewrite an angry customer email — calmer, empathetic. Done a thousand times a day in any support agent.
>
> Both work. But look at the outputs — the reasoning model is *over-polished*. It sounds like a legal department wrote it. The base model with temperature point seven sounds like a human. And it cost twenty-five times less.
>
> **My pick: GPT-4o-mini, temperature 0.7.**
>
> Reasoning models *second-guess* creative tasks. They add hedge words. They sound robotic. When you want *one of many valid answers* — like rephrasing, naming things, generating ideas — you want a base model with the temperature open.
>
> **Rule two: creative + simple = base model, temperature point seven to one.**

**[CapCut sticker: `Rule 2 — creative + simple → BASE + temp 0.7–1.0`]**

---

## SCENE 5 — EXAMPLE 3: PYTHON BUG DEBUG (4:30 – 6:00) | L4 reasoning shines

**On screen:** Jupyter. A 25-line Python function with a subtle off-by-one bug + a wrong base case in recursion.

Prompt: *"Find every bug in this function. Explain why each bug matters. Rewrite correctly."*

- Cell A: `model="gpt-4o-mini", temperature=0`
- Cell B: `model="gpt-5", reasoning={"effort": "low"}`

**Choreography:**
- Run Cell A. Output: confidently lists *one* obvious bug, misses the off-by-one entirely, says "looks correct otherwise." **Highlight this with a red box.**
- Run Cell B. Output: finds both bugs, explains the off-by-one, fixes the recursion base case. **Green box.**
- Stickers: A `$0.00009`, B `$0.0044`. A is wrong; B is right.

**Spoken:**

> Task three. Find the bugs in this function.
>
> Base model — confident, fast, and *wrong*. It misses the off-by-one. It says *"otherwise looks correct."* That's a production incident waiting to happen.
>
> Reasoning model — fifty times the cost. But it caught *both* bugs and explained why each one matters.
>
> **My pick: GPT-5, reasoning effort low.** Not high — *low*. Because the moment you have a **multi-step chain of dependencies** — bug A affects line 12, which affects the recursion — base models silently fail. You need internal thinking tokens to track that chain.
>
> Notice — I didn't go to *high* effort. Low was enough. **Always start at low and only escalate if the answer is wrong.** That's a habit that saves 80% of your reasoning cost.
>
> **Rule three: multi-step + dependencies = reasoning, START at low effort.**

**[CapCut sticker: `Rule 3 — multi-step + dependencies → REASONING, start at low`]**

---

## SCENE 6 — EXAMPLE 4: THE CURVEBALL — CONTRACT FIELD EXTRACTION (6:00 – 7:30) | L5 the senior unlearn moment

**On screen:** Jupyter. A 3-page legal contract pasted in.

Prompt: *"Extract these 6 fields: party A, party B, effective date, termination date, payment terms, governing law."*

- Cell A: `model="gpt-4o-mini", temperature=0` (legal-looking long input)
- Cell B: `model="gpt-5", reasoning={"effort": "medium"}`

**Choreography:**
- Run both. Both return identical JSON with the 6 fields.
- Stickers: A `$0.00014`, B `$0.018`. ~130× difference.
- Face cam cut.

**Spoken:**

> Task four. This one fooled me last year.
>
> Three-page legal contract. Extract six fields. Looks complex, right? Legal language, long document. **Year-ago me would have picked GPT-5 reasoning medium without thinking.**
>
> Look at the output. Both models — *identical JSON*. Same six fields. But the reasoning model cost a hundred and thirty times more.
>
> Here's what I had to unlearn: **long input is not the same as complex reasoning**. This task looks complex on the surface — it's a legal document — but the *operation* is pattern matching. Find a label, copy the value next to it. No chain of thought. No multi-step.
>
> **My pick today: GPT-4o-mini, temperature zero.**
>
> The lesson — and this is the senior-engineer move: **judge the task by the operation, not by the input size or the topic.** A 100-page medical paper summary is *not* reasoning. A 5-line algorithm puzzle *is* reasoning.

**[CapCut sticker: `Rule 4 — long input ≠ complex reasoning. Judge the operation, not the topic.`]**

---

## SCENE 7 — FRAMEWORK REVEAL: THE 2×2 (7:30 – 9:30) | L3 name the pattern

**On screen:** Sketchbook full-screen. Draw the 2×2 live. Place each of the 4 examples into the right quadrant as you go.

```
                 SIMPLE                      COMPLEX
              (1-step,                    (multi-step,
               pattern match)              dependencies)
        ┌─────────────────────────┬─────────────────────────┐
DETER-  │  BASE, temp=0           │  REASONING, low effort  │
MINISTIC│  Examples 1, 4          │  Example 3              │
        │  spam, extraction       │  bug debugging          │
        ├─────────────────────────┼─────────────────────────┤
CREATIVE│  BASE, temp=0.7–1.0     │  REASONING, high effort │
        │  Example 2              │  research, planning,    │
        │  tone rewrite           │  agent final synthesis  │
        └─────────────────────────┴─────────────────────────┘
```

**Spoken:**

> Now look back at the four picks. Three of them ended up on **base**. Only one on **reasoning**. And both came from a pattern.
>
> Two questions decide everything.
>
> One — **is the task simple or complex?** Simple means one step, pattern matching. Complex means multiple steps that depend on each other.
>
> Two — **is the output deterministic or creative?** Deterministic means one right answer. Creative means many valid answers.
>
> Two questions, four quadrants. Three of them — base model. Only one — the upper right and the lower right — needs reasoning. And the lower right needs high effort. The upper right starts at low.
>
> **This is the frame.** Memorize the two questions, not the model names. GPT-5 will become GPT-6. Claude 4.8 will become Claude 5. The questions don't change.

---

## SCENE 8 — THE AGENT-LOOP SENIOR INSIGHT (9:30 – 11:00) | L4 production reality

**On screen:** Sketchbook agent loop — a circle with 4 nodes: ROUTE → TOOL → OBSERVE → SYNTHESIZE. First three labeled "BASE." Last one labeled "REASONING."

**Spoken:**

> Now here's the part nobody on YouTube tells you. Because they're not building agents in production.
>
> When you're building an agent — a real one, with tool calls — your model gets called **eight, ten, twelve times** in a single conversation. Routing the user's question to the right tool, parsing the tool's output, deciding what to do next, finally answering.
>
> If you put a reasoning model on **every step** — that's the fifty-thousand-dollar bill I opened with. Eight seconds latency times ten steps equals an eighty-second response. *Nobody waits eighty seconds.*
>
> The senior pattern: **base model for routing, tool selection, intermediate parsing. Reasoning model only for the final synthesis — the one step where being wrong is a production incident.**
>
> Eighty percent of your agent steps don't need reasoning. They need *speed and determinism*. That's a base model with temperature zero.
>
> This single insight — base for the loop, reasoning for the answer — is what separates an agent that runs in production from a science project.

**[Forward reference: "We'll go deep on agent loops in Phase 5. For today — remember the principle."]**

---

## SCENE 9 — APPLY: 3 QUICK QUESTIONS (11:00 – 13:00) | viewer activation

**On screen:** Sketchbook. For each question: show the question for 5 seconds, viewer thinks, then reveal pick + 1-line reason.

**Question 1 (on screen 5 sec):** *"Summarize this 3-paragraph email into 2 sentences."*

**Spoken pick:** "Simple, deterministic — **base model, temperature zero.** Compression is pattern matching."

**Question 2:** *"Plan a 4-week marketing campaign with budget allocation per channel."*

**Spoken pick:** "Multi-step with dependencies between weeks and budgets — **reasoning, low effort.** Try medium only if low misses something."

**Question 3:** *"Translate this paragraph from English to Hindi, keep technical terms in English."*

**Spoken pick:** "Looks complex because it's bilingual. But the *operation* is one-to-one translation. **Base model, temperature zero.** Remember rule four — judge the operation, not the topic."

**[CapCut sticker: `Three for three? Framework works. Two out of three? Re-watch the 2x2.`]**

---

## SCENE 10 — CHEAT SHEET (13:00 – 13:45) | screenshot moment

**On screen:** Sketchbook full-screen, clean decision tree.

```
THE PICK-A-MODEL DECISION TREE

Q1. Multi-step with dependencies between steps?
├─ YES → REASONING MODEL
│        ├─ Critical / agentic / production? → effort = high
│        └─ Routine / known pattern?         → effort = low
└─ NO  → BASE MODEL
         ├─ One right answer? → temperature = 0
         └─ Many valid answers? → temperature = 0.7–1.0

AGENT-LOOP RULE
80% of agent steps = routing/parsing = BASE
Only the FINAL synthesis = REASONING

THE SENIOR UNLEARN
Long input ≠ complex reasoning.
Judge the OPERATION, not the topic.
```

**Spoken:**

> Screenshot this. Pause if you need to. This is the entire video — the decision tree, the agent-loop rule, and the unlearn moment. Tape it to your monitor.

---

## SCENE 11 — CLIFFHANGER TO V012 (13:45 – 14:30)

**On screen:** Face cam.

**Spoken:**

> One honest gap I haven't filled — I told you reasoning wins for code debugging. But *how do I know I'm not biased*? What if Claude 4.8 beats GPT-5 on that exact task? Or Gemini 3 beats both?
>
> That's Friday's video. **Reading benchmarks without getting tricked.** The MMLU trap, the three numbers I actually check before betting on a model in production, and how to update this 2×2 the moment a new model drops.
>
> Subscribe so it reaches you Friday at 7 PM.

---

## SCENE 12 — OUTRO (14:30 – 15:00)

**On screen:** Face cam.

**Spoken:**

> If this changed how you'll write your next agent — drop a comment with **which quadrant you've been over-spending on**. I read every one.
>
> Same time Friday. Out.

---

## Production Beat Sheet

| Time | Beat | Reason |
|---|---|---|
| 0:00 | Money + latency horror story | Strongest 1-second hook for AI engineer audience |
| 1:30 | Demo 1 starts | Pacing — viewer should see code before 2:00 |
| 6:00 | "I was wrong" curveball | Trust multiplier — biggest retention spike |
| 7:30 | 2x2 reveal | Screenshot moment #1 |
| 9:30 | Agent-loop insight | Senior differentiation — share button moment |
| 11:00 | Apply section | Active engagement — comments spike here |
| 13:00 | Cheat sheet | Screenshot moment #2 |
| 13:45 | V012 cliffhanger | Next-video retention |

## Skills used

| Skill | Application |
|---|---|
| 01 voice | "Senior who's been wrong" tone — confident but humble at example 4 |
| 02 story-bank | $50K agent story used as cold open (replace with a real one from your network if possible) |
| 04 roadmap-source | Phase 2 / 2.3 mapped; prereqs V009, V010 cited; cliffhanger to V012 (2.4–2.5) |
| 06 title+thumbnail | T6 formula locked above. Pair with V010's red/green for series visual identity. |
| 07 hook-factory | Stakes (money) + curiosity (one wrong pick) + promise (4 examples + framework) in first 60 sec |
| 09 monetization | Phase 1 — no paid pitch. Soft community link only in pinned comment after upload. |
| 10 description | Run skill 10 on the SRT after recording — keyword: "which AI model to use 2026" |

## What I deliberately cut (and where it goes)

| Cut | Why | Where it goes |
|---|---|---|
| Full benchmark scores (MMLU, HumanEval, ARC-AGI) | Owns V012 | V012 |
| Vendor comparison (OpenAI vs Anthropic vs Google) | Ages too fast; not the channel's edge | Off-roadmap "Industry Pulse" video if a model drop justifies it |
| Reasoning model failure modes deep dive | Would push past 15 min | Future Phase 2 bonus or Sunday live |
| Fine-tuning / custom models | Phase 8 territory | Phase 8 |
| Latency/throughput optimization | Phase 9 (Production) | Phase 9 |

## Pre-record checklist

- [ ] All 4 example notebooks tested end-to-end with live API on record day
- [ ] Cost numbers re-fetched from API (don't trust last-week numbers)
- [ ] 2x2 drawn cleanly on sketchbook in advance (warm up the marker)
- [ ] Agent-loop diagram drawn in advance
- [ ] Decision tree cheat sheet drawn full-page, clean
- [ ] Thumbnail brief sent to designer / ChatGPT image prompt run with V011 prompt
- [ ] V012 hook ready in head (or fully written) so the cliffhanger sounds natural
- [ ] Final length cut to ≤15:00 — if longer, trim Example 4 narration first (keep the pick, cut the elaboration)
