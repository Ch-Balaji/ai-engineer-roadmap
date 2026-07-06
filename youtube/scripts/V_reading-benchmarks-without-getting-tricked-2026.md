# Reading Benchmarks Without Getting Tricked + Picking Your Daily Driver (2026)

**Full scene-by-scene video script** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway), 10 (description). Closes Phase 2. Follows *Reasoning vs Base Models* (V011) and bridges into Phase 3.

> **Teaching style locked (from V010/V011):** L1 obvious case → L2 plain story → L3 name the term → L4 one step deeper → L5 honest "saved for later". Framework is DERIVED in front of the viewer, not asserted.
> **V012 spine (NEW):** the whole video lives on one distinction — **model evals (today) vs application evals (the promise)**. Benchmarks/leaderboards are model evals. The micro-eval is the hinge. Application evals are the cliffhanger into Phase 4.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V012 |
| Slug | `reading-benchmarks-without-getting-tricked-2026` |
| Playlist | Phase 2 — LLM Mental Model |
| Target length | 20 min (hard cap 21) |
| Slot | Fri 7 PM IST |
| Previous video | Reasoning vs Base Models — Which Wins When? (V011) |
| Next video | UI vs API — The Hinge Moment Most Beginners Miss (V013, Phase 3 opener) |

## Roadmap Mapping (skill 04)

```
- Phase: 2 — Mental Model of an LLM
- Sections covered: 2.4 (Reading benchmarks / leaderboards), 2.5 (Picking your daily driver model + your own micro-eval)
- Prerequisites needed: 2.1–2.2 (How an LLM thinks), 2.3 (Reasoning vs base)
- Prerequisite videos: V010, V011
- Capstone contribution: no (but seeds Phase 4 / 4.9 RAG-eval and the "application eval" mindset)
- End state: viewer can read ANY leaderboard skeptically, knows the 3 numbers to check,
  and can build a 20-example micro-eval to pick a model for THEIR task — a skill that
  survives every future model release.
- This video CLOSES Phase 2. It must tease Phase 3 (next video) AND plant the
  application-eval open loop that pays off in Phase 4.
```

## Why this video (now)

| Reality (June 2026) | What it means for the script |
|---|---|
| V011 ended on a literal promise: "the MMLU trap, the three numbers I actually check, how to update the 2×2 when a model drops" | This video MUST deliver those three things by name, or the cliffhanger lied |
| Every other channel does "GPT-5.2 vs Gemini 3 vs Claude Opus 4.5" recital — dead in 60 days | Teach the **method** and the **distinction**, never the rankings. Method is evergreen. |
| Beginners pick models by overall leaderboard rank, then act shocked when it fails their task | The micro-eval is the antidote and the channel's edge — make it the hero |
| Leaderboards changed names (Chatbot Arena → LMArena), HF Open LLM board deprioritized | Showing this churn ON SCREEN is itself the lesson: names change, method doesn't |

## Playlist Callback Map (4 references, ~30 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 1:00 | Backward bridge | V011 — *Reasoning vs Base* | "I told you reasoning wins for debugging — how do I know I'm not biased?" (V011's exact cliffhanger) |
| 2 | 11:00 | Lean-in | V011 2×2 | "Update the 2×2 the moment a new model drops" — the promised payoff |
| 3 | 16:30 | Forward reference | Phase 4 / 4.9 — *RAG Evaluation* | The application-eval open loop pays off here (Ragas, RAG Triad) |
| 4 | 19:30 | Cliffhanger | V013 — *UI vs API* (Phase 3) | Continuity: "you can pick a model — now learn to actually talk to it" |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–1:00 | **Hook — the model that won the leaderboard and lost my task** | Sketchbook → leaderboard screenshot → red X |
| 1:00–2:00 | Bridge + V011 callback + the eval-split frame | Sketchbook — draw the split |
| 2:00–3:30 | Two kinds of eval: model vs application | Sketchbook full-screen |
| 3:30–7:00 | The benchmark zoo in 3 buckets | Sketchbook + benchmark logos |
| 7:00–10:30 | Why benchmarks lie | Sketchbook → live leaderboard → LiveBench/SEAL |
| 10:30–13:30 | Read a leaderboard skeptically + the 3 numbers | **Live screen-record** of 4 leaderboards |
| 13:30–17:30 | **Build your own micro-eval (HERO)** | Jupyter, full screen, face PiP |
| 17:30–19:00 | Common mistakes (one real error live) | Jupyter |
| 19:00–20:00 | Cheat sheet + bridge to application evals | Sketchbook full-screen |
| 20:00–20:45 | Cliffhanger to V013 + outro | Face cam |

## Title + Thumbnail Brief (skill 06)

```
- Title formula: T1 (Topic — What Nobody Tells You)
- Final title: AI Benchmarks — What Nobody Tells You (2026)
- Char count: 44
- A/B title: How to Read AI Leaderboards Without Getting Tricked (2026) (57 chars)
- Subject pose: Confident, slight knowing smirk, one eyebrow up, arms relaxed
- Outfit: Brown bomber jacket + black zip-up (locked)
- Background: Black + circuit overlay (Phase-2 series identity, pairs with V010/V011)
  Center: a faux leaderboard table (rows blurred) with a big red rubber-stamp "RIGGED?" over it
- Primary text (white, Anton ALL CAPS, top):
    AI BENCHMARKS
- Highlight text (yellow + brush band, center BIG):
    LIE
- Smaller text under it:
    (here's how to read them right)
- Telugu badge (red, bottom-right):
    "ఇది అందరికీ తెలియదు"
    (translation: "Most people don't know this")
- Social-proof badge (top-left):
    "8+ YEARS IN AI"
- Tech-stack / source icon row (bottom):
    LMArena · Artificial Analysis · Aider · SWE-bench · LiveBench
- Note: ONE yellow word only (LIE). Pairs with V011's "WHICH WINS?" yellow for series continuity.
```

---

## HOOK FACTORY — 5 drafts (skill 07), recommended pick locked below

```
HOOK A — Personal Story
"In 2018 I picked my tech stack the way most people pick a model today — I trusted
the rankings. Everyone said mainframes were stable, so I joined. Three years later I
was stuck on a dying stack. Picking a model by a leaderboard is the same mistake,
just faster. Today I'll show you how to never make it again."
[Visual: sketchbook — "LEADERBOARD #1" with a red X, then "MY TASK" with a green check]

HOOK B — Production Incident (RECOMMENDED)
"Last year a team shipped the number-one model on the leaderboard. Top of LMArena,
top of MMLU. Two weeks in production, it was wrong on their actual task forty percent
of the time. The model didn't fail. The benchmark did. Today — why benchmarks lie,
and the one eval that doesn't."
[Visual: leaderboard screenshot, that model circled #1 → cut to a terminal showing 40% wrong on their task → red X over the leaderboard]

HOOK C — Live Demo First
"Watch this. Same prompt, same task, two models. The one that's higher on every
leaderboard — gets it wrong. The lower one gets it right. In the next 20 minutes
I'll show you why that happens, and how to build the 20-line eval that would've
caught it. No black box."
[Visual: Jupyter, two cells running side by side, leaderboard-leader fails, underdog passes]

HOOK D — Comment Callback
"After the last video a lot of you asked the same thing: 'Okay, reasoning wins for
debugging — but how do YOU know? What if Claude beats GPT on that exact task?'
That's the most important question on this channel so far. Today is the full answer."
[Visual: screenshot of a (composite) comment asking exactly this]

HOOK E — Shock Statistic
"A model can score ninety percent on a benchmark it has already seen the answers to.
It's called contamination, and it's in more leaderboards than you think. If you're
picking models by a public score, you're being gamed. Here's how to stop."
[Visual: a benchmark bar at 90% → a second bar (contamination-controlled) collapses to 60%]
```

**PICK: HOOK B (Production Incident).** Why: tutorial purpose defaults to B/C; B carries the highest stakes for the AI-engineer audience, names concrete sources (LMArena, MMLU), and sets up BOTH the "benchmarks lie" body and the micro-eval payoff. Hook D is the strongest *secondary* and is folded into Scene 2 as the V011 callback. (Hook C needs a working demo on record day — keep as fallback if B's screenshot isn't ready.)

---

## FINAL HOOK — The #1 Model That Lost the Task (LOCKED)

> *[Open on a real leaderboard screenshot. The top model circled in red. Cut to a sketchbook: a bar labeled "BENCHMARK 92%" next to a bar labeled "MY TASK 60%". Draw a red X over the leaderboard.]*
>
> **Spoken:**
>
> "Last year a team shipped the number-one model on the leaderboard. Top of LMArena. Top of MMLU. The best on paper.
>
> Two weeks into production, it was wrong on their *actual* task — forty percent of the time. They almost fired the engineer who picked it.
>
> Here's the twist. The model didn't fail. **The benchmark did.** It measured something — just not the thing that team needed.
>
> **[Cut to face cam.]**
>
> Today — three things. Why benchmarks lie, even the famous ones. How I read a leaderboard in sixty seconds without getting tricked — the *three* numbers I actually check. And then we build the one eval that would have saved that team: twenty lines, your own task, no black box. Stick around for the end — there's a number I check that *nobody* on YouTube talks about, because they're not shipping models in production."

---

## SCENE 1 — HOOK + STAKES (0:00 – 1:00)

**On screen:** Leaderboard screenshot → sketchbook bars → face cam (as above).

**Retention beat:** Fear (40% wrong / almost fired), promise (3 things), teaser (a number nobody talks about). Three reasons to stay before 1:00.

---

## SCENE 2 — BRIDGE + V011 CALLBACK (1:00 – 2:00)

**On screen:** Sketchbook. Phase-2 boxes: `API → Tokens → Trained (V009) → 3 Dials (V010) → Pick a Model (V011) → [TODAY: TRUST a Model]`. CapCut lower-third: V011 thumbnail.

**Spoken:**

> Quick context. Last video — *Reasoning vs Base* — we built a 2×2 to pick the right *class* of model for any task. And I made a claim: reasoning wins for code debugging.
>
> A lot of you pushed back in the comments — and you were right to. *"How do you know? What if Claude beats GPT on that exact task? What if Gemini beats both?"*
>
> That's the most important question we've hit so far. Because a framework is only as good as your ability to **check** it. Today I give you the check. By the end you'll be able to update that 2×2 yourself — the day any new model drops, no matter what it's called.

---

## SCENE 3 — THE ONE DISTINCTION: MODEL EVAL vs APPLICATION EVAL (2:00 – 3:30) | L3 name the frame

**On screen:** Sketchbook full-screen. Draw a vertical line splitting the page. Left header: **MODEL EVAL**. Right header: **APPLICATION EVAL**.

```
        MODEL EVAL                 |        APPLICATION EVAL
   "Is THIS MODEL good?"           |   "Is MY SYSTEM good? Did my
                                   |    last change make it better
   - benchmarks (MMLU, SWE-bench)  |    or worse?"
   - leaderboards (LMArena, AA)    |   - retrieval metrics
   - YOUR micro-eval (daily driver)|   - faithfulness / groundedness
                                   |   - task success rate
   >>> TODAY <<<                   |   - LLM-as-judge, regression suites
                                   |   >>> PHASE 4 (the promise) <<<
```

**Spoken:**

> Before any benchmark, get this one distinction. It's the whole video.
>
> There are **two** kinds of evaluation, and people mix them up constantly.
>
> One — **model eval.** *Is this model good?* That's what every benchmark and every leaderboard measures. MMLU, SWE-bench, LMArena — all model evals. This is what we do today, and it ends with you building your own.
>
> Two — **application eval.** *Is my system good?* Not the model — your RAG pipeline, your agent, the thing you actually shipped. Did your last change make it better or worse? That's retrieval scores, faithfulness, task success, LLM-as-judge.
>
> Here's the trap: **a great model does not guarantee a great application.** You can wire the best model on earth into a broken pipeline and ship garbage.
>
> Today is the left side — model eval. The right side — application eval — is a whole phase on its own. I'll show you the door to it at the end. For now: *which model do I even trust?*

**[Open loop planted: "the door to application evals at the end" — resolved at 16:30.]**

---

## SCENE 4 — THE BENCHMARK ZOO, IN 3 BUCKETS (3:30 – 7:00) | L1 fast, no recital

**On screen:** Sketchbook. Three boxes drawn live: **KNOWLEDGE**, **CODE/MATH**, **AGENTIC**. Drop each benchmark in as you name it. Logos appear in CapCut as stickers.

**Spoken:**

> You don't need to memorize twenty benchmarks. You need three buckets and the *one trap* in each.
>
> **Bucket one — knowledge and reasoning.**
> - `MMLU` — multiple-choice across 57 subjects. The old default. Its trap: it's *saturated and contaminated* — every model has basically seen it, so scores are bunched at the top and mean little now.
> - `GPQA` — "Google-proof" PhD-level science questions. Harder, cleaner. Its trap: it's narrow — it tells you nothing about your support-ticket task.
> - `MMMU` — same idea but *multimodal*: images, charts, diagrams. Check this only if your task has images.
>
> **Bucket two — code and math.**
> - `GSM8K` — grade-school math word problems. Basically solved. Ignore it in 2026.
> - `HumanEval` — write a function to pass unit tests. Useful, but tiny and heavily contaminated.
> - `SWE-bench` — and specifically **SWE-bench Verified** — fix *real GitHub issues* in *real repos*. This is the one that actually correlates with "can it code in production." If you build coding agents, this is your bucket-two number.
>
> **Bucket three — agentic / tool use.**
> - `BFCL` — Berkeley Function-Calling Leaderboard. Can the model pick the right tool, with the right arguments, in the right order? If you're building agents — and on this channel, you are — this matters more than MMLU ever will.
>
> **The meta-rule, write this down:** a benchmark is only useful if its task *resembles your task*. A 90 on MMLU means nothing for function calling. Match the bucket to what you're building.

**[CapCut sticker (4 sec): `Knowledge: MMLU·GPQA·MMMU | Code: HumanEval·SWE-bench | Agents: BFCL — match the bucket to YOUR task`]**

---

## SCENE 5 — WHY BENCHMARKS LIE (7:00 – 10:30) | L4 "this breaks in production"

**On screen:** Sketchbook three-column list drawn live: **CONTAMINATION**, **PROMPT SENSITIVITY**, **EVAL GAMING**. Then cut to a live leaderboard, then to LiveBench/SEAL.

**Spoken:**

> So why did that team's number-one model fail? Three reasons benchmarks lie. Not "are wrong sometimes" — *lie*, structurally.
>
> **One — contamination.** Benchmarks are public. They end up in the next model's training data. So the model isn't *reasoning* the answer — it *memorized* it. It's an open-book exam where the model already saw the answer key. A 92 can be a 92 of memory, not skill.
>
> *Honesty marker:* I'm simplifying — labs do try to filter this. But you can't fully un-leak a public test set. Assume some contamination always.
>
> **Two — prompt sensitivity.** The *same model* on the *same benchmark* can swing ten, fifteen points just by reformatting the prompt — different few-shot examples, different phrasing. So when you see "Model A: 88, Model B: 86" — that two-point gap is noise. It's within the margin of how the question was *asked*.
>
> **Three — eval gaming.** Labs know exactly which benchmarks the headlines quote. So they optimize for them. Train on similar data, tune the format. The benchmark stops measuring *capability* and starts measuring *how hard they targeted the benchmark.* Goodhart's law: when a measure becomes a target, it stops being a good measure.
>
> **[Cut to live screen-record.]** This is why a whole class of benchmarks exists *specifically to fight this*:
> - **LiveBench** — refreshes its questions *every month*, so models can't have seen them. Contamination-resistant by design.
> - **Scale SEAL** — private, held-out test sets the labs never get. Expert-graded.
>
> **The skeptic's move:** if a model is a hero on MMLU but *drops* on LiveBench or SEAL — that gap is your contamination smell test. Trust the board the model *couldn't* have memorized.

**[CapCut sticker: `Benchmarks lie 3 ways: contamination · prompt sensitivity · gaming. Antidote → contamination-resistant boards (LiveBench, SEAL)`]**

---

## SCENE 6 — READ A LEADERBOARD SKEPTICALLY: THE 3 NUMBERS (10:30 – 13:30) | the V011 payoff

**On screen:** **Live screen-record on record day** — visible date in the corner. Tab through 4 sites. Do the divergence demo.

**Choreography:**
1. **LMArena** (say once: "formerly Chatbot Arena"). Open the *category* dropdown — show coding / vision sub-arenas, not just overall.
2. **Artificial Analysis** — point at the cost + speed columns ($/M tokens, tokens/sec, TTFT).
3. **Aider Polyglot** or **SWE-bench Verified** — the task-specific board.
4. **The divergence demo:** find ONE model that is top-3 on LMArena but mid-pack on Aider (or vice versa). Circle both. This single shot proves the thesis.

**Spoken:**

> Now the part I promised last video — the three numbers I actually check. Not twenty. Three. And I check them in this order.
>
> **Number one — Arena Elo, but in the *category* that matches my task.** This is LMArena, formerly Chatbot Arena — blind human votes, converted to an Elo rating like chess. But *never* read the overall ranking. Open the category dropdown — coding, vision, whatever you're building. The overall board is a popularity contest. The category board is a signal.
>
> **Number two — cost and speed, together.** I go to **Artificial Analysis** because it puts intelligence, *price per million tokens*, and *speed* on one screen. A model that's two points smarter but five times the cost and three times slower is the wrong pick for a high-volume agent. Remember the fifty-thousand-dollar bill from V011? This column is where you prevent it.
>
> **Number three — a task-specific board.** For code, that's **Aider Polyglot** or **SWE-bench Verified** — does the code actually compile and pass tests. For agents, BFCL. Match the board to the bucket.
>
> **Now watch this.** *[Circle the divergence.]* This model is top three on the human-preference arena. Same model — middle of the pack on the coding board. **One model. Two boards. Opposite verdicts.** That is the entire reason "what's the best model" is the wrong question. The right question is "best at *what*, measured *how*."
>
> And the honest line — *[point at the date in the corner]* — this is the board as of today's date. By the time you watch this, the model names will have changed. The three numbers I check will not.

**[CapCut sticker: `The 3 numbers: 1) Arena Elo in YOUR category  2) cost + speed (Artificial Analysis)  3) a task-specific board (Aider/SWE-bench/BFCL)`]**

---

## SCENE 7 — BUILD YOUR OWN MICRO-EVAL (13:30 – 17:30) | THE HERO | L5 "no black box"

**On screen:** Jupyter, full screen, face PiP bottom-right. Reuse the **contract field-extraction** task from V011 for continuity.

**Spoken (intro):**

> Here's the truth none of those leaderboards can give you: **none of them ran your task.** The only number that matters is the one on *your* data. So we build it. Twenty lines. No black box.
>
> Four steps. Watch.

**Step 1 — 15–20 real examples with gold answers.** *(On screen: a small list.)*

> Step one — collect fifteen to twenty *real* examples from your task, each with the *correct* answer. Gold labels. This is the whole game — not a thousand, not a toy. Twenty real ones beat any public benchmark for *your* decision.

```python
# eval_set.py — your task, your gold answers (15-20 rows)
EVAL_SET = [
    {
        "contract": open("contracts/01.txt").read(),
        "gold": {"party_a": "Acme Inc", "party_b": "Globex LLC",
                 "effective_date": "2025-03-01", "termination_date": "2027-03-01",
                 "payment_terms": "Net 30", "governing_law": "Delaware"},
    },
    # ... 14-19 more, drawn from REAL contracts you actually process ...
]
```

**Step 2 — a scorer (the honest part).** *(On screen.)*

> Step two — a scorer. For extraction, it's field-by-field exact match. No vibes, no "looks good." A number. *This* is what separates an engineer from someone guessing.

```python
def score(predicted: dict, gold: dict) -> float:
    hits = sum(1 for k in gold if predicted.get(k) == gold[k])
    return hits / len(gold)            # 0.0 to 1.0, per example
```

**Step 3 — run the candidates.** *(On screen: two models.)*

> Step three — run your two candidates over all twenty. Capture three things every time: **accuracy, cost, latency.** Not just accuracy — the same triad from the leaderboard, now on *your* data.

```python
import time, json
from openai import OpenAI
client = OpenAI()

PROMPT = "Extract these 6 fields as JSON: party_a, party_b, effective_date, " \
         "termination_date, payment_terms, governing_law.\n\nCONTRACT:\n{c}"

def run(model: str):
    scores, cost, latency = [], 0.0, 0.0
    for row in EVAL_SET:
        t0 = time.time()
        r = client.chat.completions.create(
            model=model, temperature=0,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": PROMPT.format(c=row["contract"])}],
        )
        latency += time.time() - t0
        pred = json.loads(r.choices[0].message.content)
        scores.append(score(pred, row["gold"]))
        cost += estimate_cost(model, r.usage)   # your price table
    n = len(EVAL_SET)
    return {"acc": sum(scores)/n, "cost": cost, "latency": latency/n}

print("mini :", run("gpt-4o-mini"))
print("flash:", run("gemini-2.5-flash"))   # via your provider/router
```

**Step 4 — pick: cheapest that clears your bar.** *(On screen: a 2-row result table.)*

> Step four — the decision rule. Not "highest accuracy." **The cheapest model that clears your bar.** Set the bar first — say, ninety-five percent field accuracy. Then take the cheapest, fastest model that passes it. *That's* your daily driver. Tape that rule to your monitor.

```
model         acc     cost($/run)   latency(s)
gpt-4o-mini   0.96      0.00014        0.7      <- clears 0.95 bar, 130x cheaper -> WINNER
gemini-flash  0.97      0.00011        0.6      <- also clears, even cheaper -> recheck
big-reasoner  0.98      0.018          4.7      <- +2% for 130x cost -> NO
```

**Payoff line:**

> See? **No black box.** Twenty examples, a ten-line scorer, three numbers on *your* task. That's the eval that would have saved the team from the opening — they'd have caught the forty percent *before* shipping, in an afternoon. This single file is worth more than every leaderboard combined, because it's the only one that ran *your* job.

---

## SCENE 8 — COMMON MISTAKES (17:30 – 19:00) | one real error, live

**On screen:** Jupyter. Trigger mistake #3 as a real, visible flip.

| # | Mistake | Why wrong | Fix |
|---|---|---|---|
| 1 | Picking by **overall** leaderboard rank | Overall = popularity; your task ≠ the average task | Use the matching *category* + your micro-eval |
| 2 | Trusting **one** benchmark / one board | Contamination + gaming inflate single scores | Cross-check a contamination-resistant board (LiveBench/SEAL) |
| 3 | Micro-eval with **too few / unrepresentative** examples or **vibe grading** | Tiny n is noise; vibes aren't a number | 15–20 *real* examples + a coded scorer with gold labels |

**Live error to show (mistake #3):**

> Let me show you the trap I see most. Watch what happens if I run this eval on *three* examples instead of twenty.
>
> *[Run with `EVAL_SET[:3]`.]* gpt-4o-mini: sixty-seven percent. Gemini: a hundred. Looks decisive — pick Gemini, done.
>
> *[Run again on a different 3.]* Now it flips — mini's ahead. **Same models. Different three rows. Opposite winner.** That's not a result, that's noise. Three examples can't tell you anything.
>
> *[Run full 20.]* Twenty rows — they settle within one point of each other, and *cost* becomes the tiebreaker. **That's** a decision. The fix is boring and it's everything: enough real examples, graded by code, not by feeling.

---

## SCENE 9 — RECAP + BRIDGE TO APPLICATION EVALS (19:00 – 20:00) | screenshot moment + open-loop payoff

**On screen:** Sketchbook full-screen, clean.

```
HOW TO TRUST A MODEL (without getting tricked)

1. Match the BUCKET to your task
   knowledge · code · agentic — a 90 on the wrong bucket = 0 signal

2. Assume benchmarks lie 3 ways
   contamination · prompt sensitivity · gaming
   -> cross-check a contamination-resistant board (LiveBench / SEAL)

3. The 3 numbers (in order)
   (a) Arena Elo in YOUR category
   (b) cost + speed (Artificial Analysis)
   (c) a task-specific board (Aider / SWE-bench / BFCL)

4. The only number that's really yours
   a 20-example micro-eval -> cheapest model that clears your bar

RULE: never read rankings, read the LENS. Names change, method doesn't.
```

**Spoken:**

> Screenshot this. This is the whole video — the buckets, the three lies, the three numbers, and the micro-eval.
>
> Now — that door I promised at minute two. *[Cut back to the model-eval vs application-eval split.]* Everything today answered *"is this model good?"* — model eval.
>
> But your micro-eval just quietly did something bigger. The moment you scored a model on *your own data with your own gold answers* — you stopped doing model eval and started doing **application eval**. You evaluated a *system on a task*, not a model on a benchmark.
>
> And that's the entire discipline waiting for you in Phase 4. When we build RAG, "is the model good" isn't enough — we'll ask *did retrieval find the right chunk? is the answer grounded in the source, or hallucinated? did my last change make the system better or worse?* That's Ragas, faithfulness, the RAG triad. Same micro-eval mindset — scaled to a pipeline.

---

## SCENE 10 — CLIFFHANGER TO V013 + OUTRO (20:00 – 20:45)

**On screen:** Face cam.

**Spoken:**

> That closes Phase 2. You now have the full mental model of an LLM — how it thinks, the three dials, which class to pick, and how to *prove* your pick on your own data. That's more than most working engineers can do.
>
> But here's the gap. Everything so far, you've mostly done in ChatGPT's box. Production doesn't run in a chat window — it runs through the **API**. And the jump from the UI to the API is the exact moment most beginners get stuck.
>
> That's Monday — Phase 3 opens. *UI vs API — the hinge moment most people miss.* Subscribe so it reaches you at 7 PM.
>
> And tell me in the comments — **which model is your current daily driver, and have you ever actually eval'd it on your own task?** Be honest. I read every one. Out.

---

## Production Beat Sheet

| Time | Beat | Reason |
|---|---|---|
| 0:00 | "#1 model, 40% wrong, almost fired" | Strongest 1-sec stake for AI-engineer audience |
| 2:00 | Model-eval vs application-eval split | The frame the whole video hangs on; plant the open loop |
| 7:00 | "Benchmarks lie" — 3 structural reasons | Trust + retention spike (contrarian truth) |
| 10:30 | The 3 numbers (live leaderboards) | Delivers V011's promise; screenshot moment #1 |
| 11:45 | Divergence demo (one model, two boards) | Single strongest visual proof — share moment |
| 13:30 | Micro-eval build starts | The hero; "no black box" payoff |
| 17:30 | n=3 noise flip (live error) | Trust multiplier; honesty marker |
| 19:00 | Cheat sheet | Screenshot moment #2 |
| 19:30 | Open-loop payoff → application evals | Sets up Phase 4 without breaking Phase 3 continuity |
| 20:00 | V013 cliffhanger | Next-video retention |

## Skills used

| Skill | Application |
|---|---|
| 01 voice | Senior-but-honest tone; "I'm simplifying here", "no black box" used once (Scene 7) |
| 02 story-bank | None as opener (Hook B is a production incident, not a canon story). STORY_INFOSYS available as Hook A fallback — not used, so no cooldown spent. |
| 04 roadmap-source | Phase 2 / 2.4–2.5; prereqs V010, V011; closes Phase 2; teases Phase 3 (V013) + forward-refs Phase 4/4.9 |
| 06 title+thumbnail | T1 formula locked; ONE yellow word (LIE); Phase-2 series visual continuity |
| 07 hook-factory | 5 hooks generated; Hook B (incident) locked, C as fallback |
| 09 monetization | Phase 1/early — no pitch. Soft WhatsApp community link in pinned comment only. |
| 10 description | Run skill 10 on the SRT after recording — keyword: "how to read AI benchmarks 2026" |

## What I deliberately cut (and where it goes)

| Cut | Why | Where it goes |
|---|---|---|
| Application-eval deep dive (Ragas, RAG triad, faithfulness) | Owns Phase 4 / 4.9 (V030) | V030 |
| LLM-as-judge mechanics + judge bias | Application-eval territory; would blow the runtime | V030 / Phase 5 agent eval |
| Specific current rankings / model names | Ages in 60 days; not the channel's edge | Off-roadmap "Industry Pulse" only if a drop justifies it |
| Statistical significance / confidence intervals on evals | Too deep for Phase 2 | Sunday live or a Phase 4 bonus |
| Fine-tuning to beat a benchmark | Phase 8 territory | Phase 8 |

## Pre-Record Checklist

- [ ] Hook B screenshot ready (a real leaderboard with #1 circled) — else fall back to Hook C demo
- [ ] Live leaderboard tabs pre-opened on record day: LMArena (category view), Artificial Analysis, Aider/SWE-bench, LiveBench/SEAL
- [ ] **Divergence example found same-day** (one model top-3 on Arena, mid-pack on coding) — re-find on record day, it moves
- [ ] Date overlay enabled on the screen-record (honesty marker)
- [ ] Micro-eval notebook runs end-to-end with live API; contract examples reuse V011's contract for continuity
- [ ] n=3 vs n=20 flip rehearsed so the live error lands cleanly
- [ ] Cost numbers re-fetched from API (don't trust last-week numbers)
- [ ] Sketchbook drawn in advance: eval-split, 3 buckets, 3 lies, cheat sheet
- [ ] Thumbnail brief run (T1, ONE yellow word "LIE")
- [ ] Final cut ≤ 21:00 — if long, trim Scene 4 narration first (keep buckets, cut elaboration)
- [ ] Voice rules: no "guys", direct address, English jargon preserved (skill 01)
- [ ] Phase-1 monetization respected: no pitch; WhatsApp link in pinned comment only

## Post-Record Checklist

- [ ] Length 20–21 min
- [ ] ≥3 medium switches (sketchbook / live leaderboard / Jupyter / face cam) — easily met
- [ ] Burned captions, yellow on keywords (benchmark names, "3 numbers", "no black box")
- [ ] English subtitles file uploaded
- [ ] Code on screen ≥16pt
- [ ] Cheat-sheet frame held long enough to screenshot
- [ ] End screen → V013 + Phase 2 playlist
- [ ] No story used as opener → nothing to log in STORIES.md

---

## Description (for YouTube upload)

```
The #1 model on the leaderboard was wrong 40% of the time in production. The model didn't fail — the benchmark did. Here's how to read AI benchmarks without getting tricked, and how to pick your daily-driver model the right way.

In this video:
• The benchmark zoo in 3 buckets — MMLU, GPQA, MMMU (knowledge), HumanEval, SWE-bench (code), BFCL (agents) — and the one trap in each
• Why benchmarks lie: contamination, prompt sensitivity, and eval gaming
• How to read a leaderboard skeptically — the 3 numbers I actually check (LMArena, Artificial Analysis, Aider/SWE-bench) + contamination-resistant boards (LiveBench, SEAL)
• Build your own 20-line micro-eval to pick a model for YOUR task — no black box
• Model eval vs application eval — and where Phase 4 picks it up

🗺️ Where this fits in the Roadmap:
Phase 2 — Mental Model of an LLM
Section(s): 2.4 (Reading benchmarks), 2.5 (Picking your daily driver)
Prerequisite videos: V010 (3 Dials), V011 (Reasoning vs Base)
Next video: V013 — UI vs API (Phase 3 opener)
Full Roadmap: https://ch-balaji.github.io/ai-engineer-roadmap/

📂 Code:
GitHub (micro-eval starter): {per-video repo link}

⏱️ Timestamps:
0:00 — The #1 model that lost the task
1:00 — Why this matters (V011 callback)
2:00 — Model eval vs application eval
3:30 — The benchmark zoo in 3 buckets
7:00 — Why benchmarks lie
10:30 — Read a leaderboard skeptically (the 3 numbers)
13:30 — Build your own micro-eval (no black box)
17:30 — Common mistakes
19:00 — Recap + what's next
20:00 — Phase 3 starts Monday

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
```
(Pinned comment idea): "The 3 numbers I check: (1) Arena Elo in YOUR category (2) cost+speed on Artificial Analysis (3) a task-specific board — then my own 20-example micro-eval. What's your daily-driver model, and have you ever eval'd it on your own task? 👇"
```
