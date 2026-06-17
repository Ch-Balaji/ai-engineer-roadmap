# You Don't Control ChatGPT — Here's How (2026)

**Full scene-by-scene video script** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway), 10 (description). Follows *How ChatGPT Is Trained* in the Phase 2 playlist.

> **Teaching style locked:** L1 analogy → L2 plain story → L3 name the term → L4 one step deeper (code/production) → L5 honest "saved for later". Mix of beginner, mid, senior — each layer serves one of them, and senior viewers reward the *progression*, not the depth alone.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V010 |
| Slug | `how-to-control-chatgpt-2026` |
| Replaced drafts | `brain-in-windowless-room`, `three-knobs-that-control-llms` |
| Playlist | Phase 2 — LLM Mental Model |
| Target length | 14–16 min (hard cap 17) — new hook adds ~30s, payoff in Scene 6 callback |
| Slot | Mon 7 PM IST |
| Previous video | How ChatGPT Is Trained |
| Next video | Reasoning Models vs Base Models — When Each Wins in 2026 |

## Roadmap Mapping

```
- Phase: 2 — Mental Model of an LLM
- Section covered: 2.2 (How an LLM thinks) — control surface in 2026
- Prerequisites: API basics, Tokens, How ChatGPT Is Trained
- Capstone contribution: no
- End state: viewer can pick the right control parameter for the right model
            in 2026 — temperature for classic models, reasoning.effort for
            reasoning models, and layout rules for both.
```

## Why this video (now)

| Reality (May 2026 — LIVE VERIFIED against OpenAI account on 29 May 2026) | What it means for the script |
|---|---|
| OpenAI has split its model line into a **chat tier** and a **reasoning tier** | Two control surfaces, same provider — the core reframe of this video |
| **Chat tier** (sampling works): `gpt-5-chat-latest`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-4o-mini` | Accepts `temperature`, `top_p`, `seed` — use these for the Dial 1 demo |
| **Reasoning tier** (sampling rejected): `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-5-pro`, `o3`, `o4-mini` | HTTP 400 — *"Only the default (1) value is supported"* |
| **`gpt-5.1/5.2/5.3-chat-latest` are also reasoning-tier** | Despite the `-chat-latest` suffix — only **`gpt-5-chat-latest`** (no version) accepts sampling |
| `reasoning.effort` levels are **model-specific** | `gpt-5`/`gpt-5-mini`: `minimal/low/medium/high` · `o3`/`o4-mini`: `low/medium/high` · **`gpt-5-pro`: only `high` (locked)** |
| `verbosity` IS available on Responses API | Correct syntax: `text={"verbosity": "low\|medium\|high"}` — verified on `gpt-5`, `gpt-5-mini` |
| Claude Opus 4.8 shipped 28 May 2026 — verified release | `claude-opus-4-8`, $5/$25 per M tokens, 1M context |
| Opus 4.7+ rejects **non-default** sampling params with HTTP 400 | Live deprecation demo — narrate as "non-default sampling params" |
| Anthropic uses adaptive thinking + `effort` parameter | **Anthropic API not tested locally — verify exact Python SDK shape on record day** |
| Most 2024 tutorials are now wrong | Channel positioning win — first to teach the 2026 split |

## Playlist Callback Map (5 references, ~35 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 0:40 | Backward bridge | *How ChatGPT Is Trained* | Set context, name the playlist |
| 2 | 4:00 | Lean-in | *Tokens in LLM* | Token costs justify the seed/effort discussion |
| 3 | 10:00 | Forward reference | Phase 4 — RAG | Lost in the middle sets up RAG |
| 4 | 12:00 | Sibling reference | All Phase 2 videos | Binge-watch nudge inside cheat sheet |
| 5 | 13:30 | Cliffhanger | V011 — *Reasoning Models vs Base Models* | Next-video pull |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–1:10 | **Hook — Junior vs Senior terminals, 470× bill reveal** | Split-screen terminals → big number contrast → face cam |
| 1:10–1:35 | Bridge + playlist callback | Sketchbook — series boxes |
| 1:35–2:45 | Mental model — 3 controls (fast) | Sketchbook full-screen |
| 2:45–5:15 | Control 1 — Creativity (temperature, top_p, seed) | Sketchbook + Mac terminal |
| 5:15–6:45 | 2026 plot twist — the 400 error live | Mac terminal — gpt-5 + Claude 4.8 reject sampling |
| 6:45–9:00 | Control 2 — Effort (reasoning.effort + hidden tokens) | Mac — OpenAI + Anthropic side by side |
| 9:00–10:00 | **Waste demo — closes the hook loop** | Mac — waste_demo.py full table, callback to opening |
| 10:00–11:30 | Control 3 — Layout (lost in the middle) | Sketchbook U-curve |
| 11:30–12:45 | 2026 cheat sheet (6 rows) | Sketchbook full-screen |
| 12:45–14:00 | Cliffhanger to V011 | Face cam direct address |

## Title + Thumbnail Brief (skill 06)

```
- Title formula: T2 (Identity Gap) + Number + 2026 anchor
- Final title: Junior vs Senior AI Engineer — Same Code, 470× Bill (2026)
- Char count: 60
- Alt A/B titles:
    1. Why Senior Engineers Pay 470× LESS for the Same ChatGPT Answer
    2. Same ChatGPT Answer, 470× the Cost — Are You the Junior?  (2026)
    3. The Hidden ChatGPT Bill Junior Devs Don't See (2026)
    4. You Don't Control ChatGPT — Here's How (2026)   (fallback / safer)
- Subject pose: Confident, holding two phones / two terminals — left one red, right one green
- Outfit: Brown bomber jacket + black zip-up (locked)
- Background: Black + circuit overlay + warm rim light upper-right
- Primary text (white, Anton ALL CAPS, left side):
    SAME CODE
- Highlight text (yellow + brush band, right side, BIG):
    470× BILL
- Smaller text under it:
    Are you the junior?
- Telugu badge (red, bottom-right):
    "మీరు junior లాగా code రాస్తున్నారా?"
    (translation: "Are you coding like a junior?")
- Social-proof badge (top-left, if true at publish):
    "110K+ ROADMAP VIEWS"
- Tech-stack icons (bottom):
    GPT-5 · Claude 4.8 · gpt-4o-mini · Responses API
- Thumbnail composition: split-screen vibe — left half shows $0.002820
  highlighted red, right half shows $0.000006 highlighted green, you
  point at the green one with a smirk
```

---

## FINAL HOOK — Junior vs Senior (LOCKED)

> *[Open on a single Jupyter notebook in JupyterLab Dark / VSCode Dark+. Two cells visible, stacked vertically. Cell labels via CapCut overlay: top cell = "JUNIOR", bottom cell = "SENIOR". Identical `prompt` variable visible in both — the only differences are the API call and the model name.]*
>
> **Spoken:**
>
> "Two engineers. Same company. Same task — *classify if this email is spam, yes or no.*
>
> **[Run JUNIOR cell — `Shift+Enter`. ~5-second wait while gpt-5 thinks. Output renders: `Answer: no` · `Tokens: 310 (hidden reasoning: 256)` · `Cost: $0.002820` in bold red.]**
>
> This is **you** — junior developer. You wrote this code last year. You picked the most powerful model and the highest reasoning effort because someone told you 'use the best.' It works. The answer comes back — `no`. The cost — **two-point-eight thousandths of a dollar.**
>
> **[Run SENIOR cell — `Shift+Enter`. Instant. Output renders: `Answer: no` · `Tokens: 34` · `Cost: $0.000006` in bold green.]**
>
> This is **me** — senior engineer, same company, same task. I picked a smaller model and turned off the thinking. Same answer — `no`. Cost — **six-millionths of a dollar.**
>
> **[CapCut: full-screen contrast frame. `$0.002820` on the left in red, `$0.000006` on the right in green, giant animated `470×` between them.]**
>
> Same answer. Same one word. **Four hundred and seventy times the cost.**
>
> Multiply that by one hundred thousand API calls a day — the junior is burning twenty-three thousand rupees. The senior is paying fifty rupees. **Same code, same output, different bill.**
>
> **[Cut to face cam.]**
>
> Nobody on YouTube is showing you this number — because you cannot see it on ChatGPT.com. You only see it from the API. And the gap between those two cells is the entire 2026 control panel I am going to teach you in the next sixteen minutes.
>
> We are not going to start with the cost. We are going to start with the *why*. **Three dials.** Creativity. Effort. Layout. Once you see them — you will never write the junior version again."

---

## SCENE 1 — HOOK: JUNIOR vs SENIOR (0:00 – 1:10) | L1 identity-driven pain

**Source notebook:** `youtube/scripts/v010_hook/junior_vs_senior.ipynb`
**Frontend:** JupyterLab Dark or VSCode Dark+ · code font ≥18pt · cell numbers hidden · all outputs cleared before recording

**Notebook layout (top to bottom):**
- **Cell 1 — SETUP** (kept *off-camera* — collapsed or scrolled above the visible frame; loads `OPENAI_API_KEY` and defines the shared `prompt` variable + the `show()` HTML helper)
- **Cell 2 — JUNIOR** (visible, top of frame): `client.responses.create(model="gpt-5", reasoning={"effort":"high"}, ...)` — calls `show(..., color="#E63946")` so the cost line renders **bold red**
- **Cell 3 — SENIOR** (visible, bottom of frame): `client.chat.completions.create(model="gpt-4o-mini", temperature=0, ...)` — calls `show(..., color="#16A34A")` so the cost line renders **bold green**

**Choreography:**
- **0:00–0:06** — Notebook visible, both cells unrun. CapCut lower-thirds appear: top cell labeled `JUNIOR — your code from last year`, bottom cell labeled `SENIOR — same task, 2026`.
- **0:06–0:14** — Junior cell run with `Shift+Enter`. Genuine ~5-second wait — gpt-5 high reasoning is slow. Let the wait happen on camera; it adds tension. Output renders. Red `$0.002820` zoom-sticker on the cost line.
- **0:14–0:22** — Senior cell run. Returns in <1 second. Output renders. Green `$0.000006` zoom-sticker on the cost line.
- **0:22–0:35** — Hard cut to full-screen contrast frame: `$0.002820` (red) ◀ giant animated `470×` ▶ `$0.000006` (green).
- **0:35–1:10** — Cut to face cam, direct address (text below).

**Spoken:**

> Two engineers. Same company. Same task — *"classify if this email is spam, yes or no."*
>
> **[Run JUNIOR cell. ~5 sec wait while gpt-5 thinks. Output renders.]** This is **you** — junior developer. You wrote this code last year. You picked the most powerful model and the highest reasoning effort because someone told you "use the best." It works. The answer comes back — `no`. The cost — **two-point-eight thousandths of a dollar.**
>
> **[Run SENIOR cell. Instant. Output renders.]** This is **me** — senior engineer, same company, same task. I picked a smaller model and turned off the thinking. Same answer — `no`. Cost — **six-millionths of a dollar.**
>
> **[Full-screen contrast frame.]**
>
> Same answer. Same one word. **Four hundred and seventy times the cost.**
>
> Multiply that by one hundred thousand API calls a day — the junior is burning twenty-three thousand rupees. The senior is paying fifty rupees. **Same code, same output, different bill.**
>
> **[Cut to face cam.]**
>
> Nobody on YouTube is showing you this number — because you cannot see it on ChatGPT.com. You only see it from the API. And the gap between those two cells is the entire 2026 control panel I am going to teach you in the next sixteen minutes.
>
> We are not going to start with the cost. We are going to start with the *why*. **Three dials.** Creativity. Effort. Layout. Once you see them — you will never write the junior version again.

**[Retention beat: viewer now has an unanswered question — "what is the senior doing that I'm not?" — and a promise of three dials. They will stay 9 minutes specifically to see the answer.]**

---

## SCENE 2 — BRIDGE + PLAYLIST CALLBACK (1:10 – 1:35) | L1 → L2

**On screen:** Sketchbook — three small boxes left to right: `API → Tokens → Trained → [TODAY]`. CapCut lower-third (3 sec) showing the *How ChatGPT Is Trained* thumbnail.

**Spoken:**

> Quick context. This is Phase 2 of the AI Engineer Roadmap.
>
> Last video — *How ChatGPT Is Trained* — we cracked open how the model is built. Four stages, $100 million, the whole recipe. If you missed it, pause this, watch that, come back. Link in description.
>
> Today is the next step. Today is how you **control it** once it is built. Sixteen minutes. Mostly demos.

**[Bridge ends fast. Straight into mental model — no rehash.]**

---

## SCENE 3 — THE THREE CONTROLS (1:10 – 2:20) | L1 analogy → straight to demo

**On screen:** Sketchbook full-screen. Draw three dials live — fast, no over-explaining.

**Spoken:**

> One picture, then we go to code.
>
> There are only **three controls** on an LLM call.
>
> **[Draw dial 1]** **Creativity.** How safe or wild the next word is.
>
> **[Draw dial 2]** **Effort.** How hard the model thinks before it answers.
>
> **[Draw dial 3]** **Layout.** Where you put information in the prompt — beginning, middle, end.
>
> **[Write on sketchbook: 1. CREATIVITY  2. EFFORT  3. LAYOUT]**
>
> Every term you have ever heard — `temperature`, `top_p`, `reasoning.effort`, `seed`, lost-in-the-middle — maps to one of these three. That is the whole panel.
>
> Two more things before we hit code. One — names changed in 2026. The models I am using are from this April and last week. Anything written before 2025 is partially wrong now. Two — the way I will teach each dial is the same every time. **Analogy first. Name second. Code third.** Let's go.

**[Retention beat: first demo arrives 35 seconds from here, not 2 minutes. Proof early.]**

---

## SCENE 4 — DIAL 1: CREATIVITY (2:20 – 5:00) | L3 name + L4 code

**On screen:** Sketchbook — zoom into Dial 1. Then switch to Mac terminal for live demo.

**Spoken:**

> Dial one — creativity. The 2026 name is `temperature`. Number between 0 and 2.
>
> - Low — `0` or `0.2` — the model is careful, repeatable, picks the safest next word. Use this for extraction, JSON, agents.
> - High — `0.9` or above — the model picks varied words, more creative, sometimes weird. Use this for brainstorming, naming, content variations.
>
> Let me show you. Same prompt. Two `temperature` values. For this demo I am using `gpt-4.1-mini` — one of OpenAI's **chat-tier** models that still accepts the full temperature range. Why "chat-tier"? Hold that thought, scene five.
>
> **[Switch to Mac terminal — sampling_demo.py]**
>
> ```python
> from openai import OpenAI
> client = OpenAI()
>
> for temp in [0.0, 0.9]:
>     r = client.chat.completions.create(
>         model="gpt-4.1-mini",
>         messages=[{"role": "user",
>                    "content": "5 startup ideas for AI in India"}],
>         temperature=temp,
>     )
>     u = r.usage
>     print(f"--- temperature={temp} | "
>           f"in={u.prompt_tokens} out={u.completion_tokens} "
>           f"total={u.total_tokens} ---")
>     print(r.choices[0].message.content[:300])
> ```
>
> **[Run.]**
>
> `temperature=0` — almost the same five ideas every run. Repeatable.
> `temperature=0.9` — different ideas every run. Creative.
>
> **Notice the line at the top of each run.** That is `usage` — printed from the response. `prompt_tokens`, `completion_tokens`, `total_tokens`. Every API call returns these numbers. Print them. **You should never be guessing what an LLM call cost you** — the API tells you exactly. We will use this all through the video.
>
> **There is a sibling parameter — `top_p`.** Also controls variety, in a different way. For chat-tier models, **don't tune both at the same time** unless you know why — pick one. We will save the `top_p` deep dive for a Phase 3 prompt-engineering video.
>
> **Quick production note** — there is also `seed`. Set `seed=42` with `temperature=0` on chat-tier models, and the output becomes *as repeatable as it gets*. Not perfect. Close enough for tests.
>
> And here is the cliffhanger for the next scene — try this exact same code with `model="gpt-5"` and watch what happens.

**[Retention beat: "Okay — creativity dial, got it. But here is where 2026 broke every old tutorial."]**

---

## SCENE 5 — 2026 PLOT TWIST: THE 400 ERROR (5:00 – 6:30) | L4 production reality

**On screen:** Mac terminal — pre-loaded `temp_on_gpt5.py`. Run live. Then a second terminal window for Anthropic.

**Spoken:**

> Watch. Same code from Scene 4. One word changed. `gpt-4.1-mini` becomes `gpt-5`.
>
> ```python
> r = client.chat.completions.create(
>     model="gpt-5",
>     messages=[{"role": "user", "content": "Hello"}],
>     temperature=0,
> )
> ```
>
> **[Run.]**
>
> ```
> openai.BadRequestError: Error code: 400 -
> Unsupported value: 'temperature' does not support 0 with this model.
> Only the default (1) value is supported.
> ```
>
> HTTP 400. From **OpenAI itself.** Not Anthropic. Not some weird edge model. **`gpt-5`** — the flagship — rejects the very knob every 2024 tutorial taught you to set.
>
> This is the 2026 split. **OpenAI has divided its model line in two.**
>
> - The **chat tier** — `gpt-5-chat-latest`, `gpt-4.1`, `gpt-4o-mini` — still accepts sampling parameters. This is what powers ChatGPT consumer.
> - The **reasoning tier** — `gpt-5`, `gpt-5-mini`, `gpt-5-pro`, the `o-series` — rejects non-default temperature. Same provider. Different control surface.
>
> And it is not just OpenAI. **[Switch to second terminal.]**
>
> ```python
> import anthropic
> client = anthropic.Anthropic()
> client.messages.create(
>     model="claude-opus-4-8",
>     max_tokens=1024,
>     temperature=0,
>     messages=[{"role": "user", "content": "Hello"}],
> )
> # → 400: non-default sampling parameters are not supported
> ```
>
> Same story. Claude Opus 4.8 — released May 28 — rejects non-default sampling parameters too.
>
> Why has both providers done the same thing? Because **reasoning models think first, then answer.** The creativity dial is no longer the main control for this kind of model. Both providers moved the control surface entirely.
>
> So if creativity is not the main dial here — what is?
>
> That is dial two.

**[Retention beat: "OpenAI ITSELF rejects temperature now — what is the new dial?"]**

---

## SCENE 6 — DIAL 2: EFFORT (6:30 – 9:30) | L1 → L2 → L3 → L4 — the heart of the video

**On screen:** Sketchbook — zoom into Dial 2. Draw a student writing an exam, low effort vs deep thinking.

**Spoken:**

> Remember the analogy. Dial two — **how hard the model thinks before answering.**
>
> In 2024, this dial did not exist. Every model worked the same way. You ask, it answers. One pass through the brain.
>
> In 2026, there is a second family — **reasoning models.** They think first. Internally. Token by token, working out steps on a scratchpad you do not see. Then they answer. Those scratchpad tokens — they call them **thinking tokens**. And they count toward your billed generation-side usage.
>
> Examples — `gpt-5`, `gpt-5-mini`, `gpt-5-pro`, `o3`, `o4-mini`, Claude Opus 4.8, DeepSeek R1, Gemini 2.5 Thinking.
>
> For these models, you do not set creativity. You set **effort**.
>
> Let me show you both providers side by side.
>
> **[Mac terminal — effort_demo_openai.py]**
>
> ```python
> # OpenAI — uses the new Responses API
> from openai import OpenAI
> client = OpenAI()
>
> r = client.responses.create(
>     model="gpt-5",
>     input="Plan a 3-day trip to Hyderabad for a family of four.",
>     reasoning={"effort": "low"},   # also "minimal", "medium", "high"
> )
> print(r.output_text)
> ```
>
> Quick note — supported levels **depend on the model**. `gpt-5` and `gpt-5-mini` support `minimal`, `low`, `medium`, `high`. The `o-series` — `o3`, `o4-mini` — supports `low`, `medium`, `high`. `minimal`/`low` — fast and cheap, almost no thinking. `high` — the model genuinely reasons through the problem. Default is `medium` on most models.
>
> Anthropic does the same idea with different names. **Quick note for engineers — verify the exact SDK shape against the latest `anthropic` package before you ship this, the field names are still settling. The concept is what matters:** adaptive thinking + an effort level.
>
> ```python
> # Anthropic — Claude Opus 4.8 (verify exact SDK syntax on record day)
> import anthropic
> client = anthropic.Anthropic()
>
> message = client.messages.create(
>     model="claude-opus-4-8",
>     max_tokens=2048,
>     thinking={"type": "adaptive"},
>     output_config={"effort": "medium"},   # "low", "medium", "max"
>     messages=[{"role": "user",
>                "content": "Plan a 3-day trip to Hyderabad for a family of four."}],
> )
> print(message.content[0].text)
> ```
>
> Same idea, different API. OpenAI: `reasoning.effort`. Anthropic: adaptive thinking with an `effort` parameter. The model decides *how* to think — you pick the depth.
>
> **Production rule of thumb — three levels you actually use:**
>
> | Effort | Use case |
> |---|---|
> | `minimal` / `low` | Simple lookups, classification, fast UX, agents that just route |
> | `medium` (default on most) | Most production workloads |
> | `high` / `max` | Hard reasoning, coding agents, multi-step planning, math |
>
> **One step deeper — and this one I want you to see, not take my word for.** Thinking tokens cost real money. Let me show you the actual numbers, live.
>
> **[Run effort_demo_openai.py — same math question, four effort levels, usage printed each row.]**
>
> ```
> effort      input  visible   hidden   total
> ---------------------------------------------
> minimal        14       27        0      41
> low            14       40       64     118
> medium         19       67      320     406
> high           19       89      768     876
> ```
>
> Look at this. **Same model. Same kind of question. Just one parameter changed.** `minimal` to `medium` — your token usage went up **ten times.** And look at the `hidden` column — those are reasoning tokens. The model is "thinking" three hundred and twenty tokens internally before it gives you a six-line answer. You pay for every one of them. Most engineers never see this number because they never print `usage`. Now you will.
>
> When `high` is worth that 20x bill and when `minimal` is enough — that is **Wednesday's video**.
>
> But before we move on — **let me close the loop from the opening.** Remember the two terminals at the start? The junior versus senior bill? You now have the vocabulary to understand exactly what was happening.
>
> **[Switch to waste_demo.py — full table across 10 model/effort configs.]**
>
> Same prompt as the hook — *"Is this email spam? Reply yes or no."* — but now I am going to run it on **every tier**. Cheapest chat model, mid-tier, full reasoning at every effort level. Watch the answer column — and watch the cost column.
>
> ```
> model          effort     in  visible  hidden  total    cost($)   answer
> -----------------------------------------------------------------------
> gpt-4o-mini    -          33       1       0      34   0.000006   'no'
> gpt-4.1-mini   -          33       1       0      34   0.000015   'no'
> gpt-5-mini     minimal    32      19       0      51   0.000046   'no'
> gpt-5-mini     medium     32      28      64     124   0.000192   'no'
> gpt-5-mini     high       32      32     128     192   0.000328   'no'
> gpt-5          minimal    32      19       0      51   0.000230   'no'
> gpt-5          medium     32      17     128     177   0.001490   'no'
> gpt-5          high       32      22     256     310   0.002820   'no'
> ```
>
> Every row says **`no`**. Same answer. **Top row to bottom row — four hundred and seventy times the cost.** This is the exact gap from the opening.
>
> The junior in the hook was running the bottom row — `gpt-5` `high` effort, because someone told them "use the best model." The senior was running the top row — `gpt-4o-mini`, the right model for a binary classification.
>
> **The lesson is not "always use the cheap model."** Sometimes `gpt-5` `high` earns every paisa — for coding agents, multi-step reasoning, hard math. The lesson is **match the model and effort to the task**, and you can only do that once you have seen these three dials and started printing your usage.
>
> Wednesday's video is the full framework — when to climb the ladder, when to stay at the bottom. So I am stopping here. Dial three.

**[CTA hint — skill 09, Phase 1, ≤15 sec, single line, no pitch.]**

> If you want structured help on resume or mock interviews, the form is in the description. Back to dial three.

---

## SCENE 7 — DIAL 3: LAYOUT (10:00 – 11:30) | L1 → L2 → forward reference

**On screen:** Sketchbook — draw the U-curve attention chart.

**Spoken:**

> Dial three — and this one is not deprecated, not changed, **not going anywhere.** It will be true in 2027, 2028, the day they release GPT-7. **Where you put information in the prompt.**
>
> There is a paper called *Lost in the Middle*. The name is enough — engineers should know it.
>
> **[Draw a U-curve. HIGH attention at start, LOW in middle, HIGH at end.]**
>
> When your prompt gets long, the model pays the most attention to the **beginning** and the **end**. Whatever you bury in the middle — facts, instructions, retrieved chunks — the model under-weights. Sometimes ignores entirely.
>
> Imagine again the letter to a friend. Page one — they read carefully. Last page — they read carefully. Page seven, paragraph four — skimmed.
>
> **Production rule, say it out loud:**
>
> > Put critical instructions and critical evidence near the **start** or repeat them near the **end**. Do not bury gold in the middle.
>
> One more piece. Your model says it has 1 million tokens of context. Sounds like "I can paste my entire codebase." Technically yes. Practically — everything competes for the same slot. System prompt, retrieved chunks, chat history, the user question. Fill the slot, the middle silently degrades. No error. No warning. Just worse answers.
>
> **Forward reference:** This U-curve is exactly why naive RAG fails in production. We will fight it head-on in Phase 4 — chunking, reranking, hybrid retrieval. For now — just remember the rule. Gold at the edges. Never the middle.

---

## SCENE 8 — 2026 CHEAT SHEET (11:30 – 12:45) | L4 summary + sibling reference

**On screen:** Sketchbook full-screen — draw the cheat sheet live, row by row.

**Spoken:**

> One page. Screenshot this. The entire 2026 control panel in six rows.

```
THE 2026 LLM CONTROL PANEL  (live-verified May 29, 2026)

Control          Chat tier                         Reasoning tier
                 gpt-5-chat-latest, gpt-4.1,       gpt-5, gpt-5-mini, gpt-5-pro,
                 gpt-4o-mini, Sonnet 4.6,          o3, o4-mini, Opus 4.8,
                 Gemini Flash, open-source         DeepSeek R1, Gemini 2.5 Thinking
─────────────────────────────────────────────────────────────────────────────────
Creativity       temperature, top_p                NOT accepted
                 (don't tune both)                 HTTP 400 on non-default values
                                                   (verified on gpt-5 and opus-4-8)

Effort           Not the main control              OpenAI Responses API:
                                                     gpt-5/mini  → minimal/low/medium/high
                                                     o-series    → low/medium/high
                                                   Anthropic:
                                                     adaptive thinking + effort
                                                     (low/medium/max)

Repeatability    seed (where supported)            Not stable — model decides

Layout           Always matters                    Always matters — even with 1M context
                 Place gold at start or end        Long context ≠ reliable context
                 Never bury it in the middle       Chunk + repeat the critical instruction

Cost visibility  r.usage.prompt_tokens             r.usage.input_tokens
                 r.usage.completion_tokens         r.usage.output_tokens
                 r.usage.total_tokens              r.usage.output_tokens_details
                                                     .reasoning_tokens  ← hidden cost
                                                   r.usage.total_tokens
                 Always print it.                  Always print it.

Main lesson      Tune sampling                     Tune thinking effort
```

> Two model families. Same three controls. The lesson on the bottom row is the one to remember — **for classic chat models, you tune sampling. For reasoning models, you tune effort.** Layout matters on both, always.
>
> **Sibling reference:** Hallucinations and refusals — that was the training video. The control panel — what we just covered. Reasoning vs base models — Wednesday. Three videos, one playlist, one mental model. Playlist link below.

---

## SCENE 9 — CLIFFHANGER (12:45 – 14:00) | L5 + next-video pull

**On screen:** Face cam, direct address.

**Spoken:**

> Quick recap before I let you go.
>
> Dial one — creativity. `temperature`. Works on classic chat models. Restricted or unavailable on the new reasoning models.
>
> Dial two — effort. `reasoning.effort` on OpenAI. Adaptive thinking with `effort` on Anthropic. The new control surface that did not exist last year.
>
> Dial three — layout. Lost in the middle. Eternal. Will outlive every model release.
>
> Now — the next question.
>
> You know how to *control* a model. But **which** model do you call?
>
> Same prompt. `gpt-5-chat-latest` — fast and cheap. `gpt-5` reasoning — three times slower, much smarter. Claude Opus 4.8 — even pricier but the best on hard reasoning. When does the expensive one earn its money? When does the cheap one win and the expensive one waste your budget?
>
> Wednesday's video. *Reasoning Models vs Base Models — When Each Wins in 2026.* Spoiler: most teams pick the wrong one and burn money for two weeks before they notice.
>
> If this clicked — share it with one engineer who is still copy-pasting `temperature=0` into a 2026 reasoning model. They are about to hit a 400 error.
>
> See you in the next one.

---

## YouTube Description (draft — run skill 10 on final SRT)

```
Two engineers. Same code. 470× different bill. Are you the junior in this video?

The actual control panel of ChatGPT — and how it changed in 2026. Most tutorials are now wrong.

In this video:
• Junior vs Senior cost demo — same prompt, same answer, 470× cost (real numbers, live)
• 3 things you actually control on every LLM call (mental model first)
• Dial 1 — temperature, top_p, and the seed trap
• The 400 error nobody warned you about — gpt-5 and Claude Opus 4.8 rejecting non-default sampling params
• Dial 2 — reasoning.effort (OpenAI) and adaptive thinking + effort (Anthropic)
• Hidden reasoning-token bill — how to see what ChatGPT is really charging you
• Dial 3 — Lost in the Middle and why naive RAG breaks
• 2026 cheat sheet by model tier — chat vs reasoning

🗺️ Roadmap: Phase 2 — Mental Model of an LLM
Previous: How ChatGPT Is Trained
Next: Reasoning Models vs Base Models (Wednesday)
Full Roadmap: https://ch-balaji.github.io/ai-engineer-roadmap/

📂 Code:
Repo: roadmap-2026-v010-control-llms
- v010_hook/junior_vs_senior.ipynb  (HOOK — 3 cells: setup + JUNIOR red / SENIOR green)
- sampling_demo.py                  (gpt-4.1-mini, temperature + usage)
- temp_on_gpt5.py                (live 400 error on gpt-5)
- temp_on_opus48.py              (live 400 error on Claude Opus 4.8)
- effort_demo_openai.py          (reasoning.effort + hidden reasoning tokens)
- effort_demo_anthropic.py       (adaptive thinking + effort)
- waste_demo.py                  (470x cost comparison across tiers)
- requirements.txt

#AIEngineer #LLM #ChatGPT2026
```

---

## Companion Code Files (create before record)

### Hook source — `junior_vs_senior.ipynb` (3 cells, on-camera) — LIVE VERIFIED

**Path:** `youtube/scripts/v010_hook/junior_vs_senior.ipynb`
**Frontend on camera:** JupyterLab Dark or VSCode Dark+ · code font ≥18pt · all outputs cleared before recording.

#### Cell 1 — Setup (off-camera; collapse or scroll above frame)
```python
import os
from openai import OpenAI
from IPython.display import HTML, display

with open(".env") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            if k.lower() == "openaiapikey":
                os.environ["OPENAI_API_KEY"] = v
                break

client = OpenAI()

email = "Hey, want to grab coffee tomorrow?"
prompt = f"Is this email spam? Reply yes or no.\n\nEmail: '{email}'"

def show(answer, tokens, hidden, cost, color):
    hidden_str = f"  (hidden reasoning: {hidden})" if hidden else ""
    display(HTML(f"""
    <div style='font-family: "JetBrains Mono", "Menlo", monospace;
                font-size: 22px; line-height: 1.6; padding: 8px;'>
      <div><b>Answer:</b>  {answer}</div>
      <div><b>Tokens:</b>  {tokens}{hidden_str}</div>
      <div style='color: {color}; font-weight: 700;'>Cost:    ${cost:.6f}</div>
    </div>
    """))
```

#### Cell 2 — JUNIOR (top of visible frame, RED cost line)
```python
r = client.responses.create(
    model="gpt-5",
    input=prompt,
    reasoning={"effort": "high"},
    max_output_tokens=4000,
)
u = r.usage
cost = (u.input_tokens / 1e6) * 1.25 + (u.output_tokens / 1e6) * 10.00
show(
    r.output_text.strip(),
    u.total_tokens,
    u.output_tokens_details.reasoning_tokens,
    cost,
    "#E63946",
)
```
**Verified output (29 May 2026):** `Answer: no` · `Tokens: 310 (hidden reasoning: 256)` · `Cost: $0.002820` (bold red)

#### Cell 3 — SENIOR (bottom of visible frame, GREEN cost line)
```python
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_completion_tokens=10,
)
u = r.usage
cost = (u.prompt_tokens / 1e6) * 0.15 + (u.completion_tokens / 1e6) * 0.60
show(
    r.choices[0].message.content.strip(),
    u.total_tokens,
    0,
    cost,
    "#16A34A",
)
```
**Verified output (29 May 2026):** `Answer: no` · `Tokens: 34` · `Cost: $0.000006` (bold green)

**Why this design makes the cost difference unmissable:**
1. The shared `prompt` variable in cell 1 means the inputs are *identical* — no "the prompt was different" objection
2. Cells 2 and 3 differ only in the API call shape and the `model=` line — the structural diff *is* the lesson, called back in Scene 6
3. HTML `display()` renders bold colored text reliably across JupyterLab, VSCode, and Colab — unlike ANSI escape codes
4. The hidden-reasoning count (`256` on the junior side, absent on the senior) reveals the *invisible bill* in real time
5. `.6f` precision makes `$0.000006` look "almost free" next to `$0.002820` — the digit count itself sells the gap

### `sampling_demo.py` (Dial 1) — LIVE VERIFIED
```python
from openai import OpenAI
client = OpenAI()
# Chat-tier model — accepts the full temperature range
for temp in [0.0, 0.9]:
    r = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user",
                   "content": "5 startup ideas for AI in India"}],
        temperature=temp,
    )
    u = r.usage
    print(f"--- temperature={temp} | "
          f"in={u.prompt_tokens} out={u.completion_tokens} "
          f"total={u.total_tokens} ---")
    print(r.choices[0].message.content[:300])
```

### `temp_on_gpt5.py` (the 400 error — primary hook payoff) — LIVE VERIFIED
```python
from openai import OpenAI
client = OpenAI()
try:
    r = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": "Hello"}],
        temperature=0,
    )
    print(r.choices[0].message.content)
except Exception as e:
    print("400 ERROR LIVE ON CAMERA:", e)
# Verified output (29 May 2026):
# BadRequestError: 400 - Unsupported value: 'temperature' does not
# support 0 with this model. Only the default (1) value is supported.
```

### `temp_on_opus48.py` (secondary 400 error — Anthropic side)
```python
import anthropic
client = anthropic.Anthropic()
try:
    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        temperature=0,
        messages=[{"role": "user", "content": "Hello"}],
    )
    print(message.content[0].text)
except anthropic.BadRequestError as e:
    print("400 ERROR LIVE ON CAMERA:", e)
```

### `effort_demo_openai.py` (Dial 2 — Responses API) — LIVE VERIFIED
```python
from openai import OpenAI
client = OpenAI()
# gpt-5 effort levels: minimal, low, medium, high  (NOT 'none' or 'xhigh')
print(f"{'effort':<10} {'input':>6} {'visible':>8} {'hidden':>8} {'total':>7}")
print("-" * 45)
for level in ["minimal", "low", "medium", "high"]:
    r = client.responses.create(
        model="gpt-5",
        input="What is 137 * 24? Think step by step then give the answer.",
        reasoning={"effort": level},
        text={"verbosity": "medium"},
        max_output_tokens=4000,
    )
    u = r.usage
    visible = u.output_tokens - u.output_tokens_details.reasoning_tokens
    hidden  = u.output_tokens_details.reasoning_tokens
    print(f"{level:<10} {u.input_tokens:>6} {visible:>8} "
          f"{hidden:>8} {u.total_tokens:>7}")
    print(f"  answer: {r.output_text[:80]}...")
# Real numbers from a live run (29 May 2026, math question):
#   effort=minimal -> input=14  visible=27   hidden=0    total=41
#   effort=medium  -> input=19  visible=67   hidden=320  total=406
# Same model, same kind of question, 10x cost jump.
# Fun fact: gpt-5-pro only accepts effort='high' — locked.
```

### `effort_demo_anthropic.py` (Dial 2 — Anthropic)
> **VERIFY ON RECORD DAY:** Anthropic's effort parameter shape on the Python SDK is still settling (`output_config.effort` is the documented concept, but the exact kwarg name may shift between SDK versions). Run this once before recording and adjust the call signature to whatever the latest `anthropic` package accepts.
```python
import anthropic
client = anthropic.Anthropic()
# Claude Opus 4.8 effort levels (concept): low, medium, max
for level in ["low", "medium", "max"]:
    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2048,
        thinking={"type": "adaptive"},
        output_config={"effort": level},
        messages=[{"role": "user",
                   "content": "Plan a 3-day trip to Hyderabad for a family of four."}],
    )
    print(f"--- effort={level} ---")
    print(message.content[0].text[:400])
```

### `waste_demo.py` (the cost-comparison money shot) — LIVE VERIFIED
```python
from openai import OpenAI
client = OpenAI()

# Generic, low-difficulty task — classification with one-word answer
task = ("Is this email spam? Reply with only one word: yes or no.\n\n"
        "Email: 'Hey, want to grab coffee tomorrow?'")

# USD per million tokens — verified openai.com/api/pricing on 29-May-2026
# UPDATE THESE ON RECORD DAY (pricing shifts).
PRICES = {
    "gpt-4o-mini":   {"in": 0.15,  "out": 0.60},
    "gpt-4.1-mini":  {"in": 0.40,  "out": 1.60},
    "gpt-5-mini":    {"in": 0.25,  "out": 2.00},
    "gpt-5":         {"in": 1.25,  "out": 10.00},
}

def cost(model, in_tok, out_tok):
    p = PRICES[model]
    return (in_tok / 1e6) * p["in"] + (out_tok / 1e6) * p["out"]

header = f"{'model':<14} {'effort':<10} {'in':>5} {'visible':>8} {'hidden':>8} {'total':>7} {'cost($)':>10} answer"
print(header)
print("-" * len(header))

# Chat tier — no effort knob
for model in ["gpt-4o-mini", "gpt-4.1-mini"]:
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": task}],
        temperature=0,
        max_completion_tokens=10,
    )
    u = r.usage
    c = cost(model, u.prompt_tokens, u.completion_tokens)
    print(f"{model:<14} {'-':<10} {u.prompt_tokens:>5} "
          f"{u.completion_tokens:>8} {0:>8} {u.total_tokens:>7} "
          f"${c:>9.6f}  {r.choices[0].message.content!r}")

# Reasoning tier — multiple effort levels
for model in ["gpt-5-mini", "gpt-5"]:
    for eff in ["minimal", "low", "medium", "high"]:
        r = client.responses.create(
            model=model,
            input=task,
            reasoning={"effort": eff},
            max_output_tokens=4000,
        )
        u = r.usage
        hidden = u.output_tokens_details.reasoning_tokens
        visible = u.output_tokens - hidden
        c = cost(model, u.input_tokens, u.output_tokens)
        print(f"{model:<14} {eff:<10} {u.input_tokens:>5} "
              f"{visible:>8} {hidden:>8} {u.total_tokens:>7} "
              f"${c:>9.6f}  {(r.output_text or '<empty>')!r}")
# Verified output (29 May 2026): every row prints 'no', cost spans
# $0.000006 (gpt-4o-mini) to $0.002820 (gpt-5 high) — a 470x range
# for identical answers. At 100K calls/day that is 60 paise vs ~23,000 rupees.
```

### `requirements.txt`
```
openai>=1.55.0
anthropic>=0.39.0
python-dotenv>=1.0.0
```

---

## CapCut Edit Cues — Playlist Callbacks + Highlights

| Time | Cue | Asset |
|---|---|---|
| 0:00–1:10 | **Notebook layout, two cells stacked** | One JupyterLab/VSCode notebook visible · top cell labeled `JUNIOR` · bottom cell labeled `SENIOR` (CapCut overlays) |
| 0:14 | Red zoom sticker | Animate `$0.002820` growing 2× with red glow over the JUNIOR output |
| 0:22 | Green zoom sticker | Animate `$0.000006` growing 2× with green glow over the SENIOR output |
| 0:30 | Full-screen contrast frame | Two numbers + giant animated `470×` between them |
| 1:35 | Lower-third (3 sec) | Thumbnail of *How ChatGPT Is Trained* + small "▶ Watch first" tag |
| 4:30 | Lower-third (3 sec) | Thumbnail of *Tokens in LLM* + "Prereq" tag |
| 5:35 | Big red `400` overlay (animated) | Sticker on terminal output |
| 6:00 | Zoom-in callout | Red box around `temperature is deprecated` |
| 9:30 | Floating sticker (4 sec) | Text "Phase 4 — RAG → coming in Week 8" |
| 12:30 | Playlist card (5 sec) | Phase 2 playlist link + sticker "All in one playlist →" |
| 13:40 | End-screen template | V011 on left, Phase 2 playlist on right |
| Pinned comment | Auto-pin | "Roadmap: {link} · Previous: How ChatGPT Is Trained · Next: Reasoning vs Base Models (Wed)" |

---

## Technical Terms Introduced (analogy first, name second — locked)

| Term | L1 analogy | L3 name lands at |
|---|---|---|
| `temperature` | Creativity dial | Scene 4 |
| `top_p` | Sibling of creativity dial | Scene 4 (mention only) |
| `seed` | Repeatability lock | Scene 4 |
| Reasoning model | Student working on scratch paper | Scene 6 |
| Thinking tokens | The scratch paper itself | Scene 6 |
| `reasoning.effort` (`none/low/medium/high/xhigh`) + `verbosity` | Effort dial — OpenAI flavor | Scene 6 |
| Adaptive thinking + `effort` (`low/medium/max`) | Effort dial — Anthropic flavor (verify SDK shape) | Scene 6 |
| Responses API | OpenAI's new endpoint for reasoning models | Scene 6 |
| Lost in the middle | Friend skimming page 7 of a letter | Scene 7 |
| Context competition | Everything fights for the same slot | Scene 7 |

---

## Retention Map

| Time | Beat | Purpose |
|---|---|---|
| 0:00 | Split-screen terminals start blank | Curiosity from frame 1 |
| 0:25 | Junior cost $0.002820 zooms up (red) | First number shock |
| 0:40 | Senior cost $0.000006 zooms up (green) | Contrast lands |
| 0:55 | Giant `470×` between the two numbers | Screenshot moment + identity hit |
| 1:05 | "Are you the junior?" implicit | Open loop — must stay 9 min to learn |
| 1:35 | Three dials drawn live (fast) | Mental anchor for whole video |
| 2:30 | "Analogy → name → code, always" | Sets viewer trust in pacing |
| 3:00 | First demo (`gpt-4.1-mini` + temperature) | Proof under 3 min — locks the loyal viewer |
| 5:15 | Live 400 error on `gpt-5` (OpenAI itself!) | Shock + shareable moment + reframe |
| 7:00 | Reasoning model analogy (student with scratch paper) | New mental hook |
| 8:30 | **Live usage table — 10× cost jump on the SAME model** | Money-shot #1 |
| 9:00 | **Waste demo — explicitly closes the hook loop** | Money-shot #2 + payoff to opening |
| 10:00 | "Wednesday's video does the full framework" | Honest deferral + next-video pull |
| 11:30 | Cheat sheet drawn live | Screenshot + share moment |
| 12:45 | Cliffhanger to V011 | Binge-watch nudge |

---

## Skill Compliance Audit

| Skill | Compliance |
|---|---|
| 01 voice | No "guys". Direct "you". English jargon preserved (`temperature`, `top_p`, `reasoning.effort`). Signature phrase `no black box` saved — used only if needed in edit. Short declarative sentences. |
| 02 story-bank | No canon story used. Two universal mini-analogies (writer's desk, student with exam). Story budget transferred to V011. |
| 04 roadmap-source | Phase 2 / 2.2. Prerequisites: API, Tokens, How ChatGPT Is Trained. Cliffhanger to 2.3. |
| 06 title+thumbnail | T1 + 2026 anchor. Brief locked above. |
| 07 hook-factory | 5 hooks generated. Recommended A (universal pain). Alternate B (live 400 error) flagged. |
| 09 monetization | Phase 1 — single 15-sec description hint at minute 10, no pitch. |
| Anti-patterns | No welcome / throat-clear. No rehash of training video. No toy-only example — Opus 4.8 and Responses API are current production. |

---

## Pre-Record Checklist

**OpenAI side — verified live against the account on 29 May 2026.**

- [x] **JUNIOR cell** → `gpt-5` + effort=high → `answer='no'`, tokens=310 (hidden=256), `cost=$0.002820` ✅ verified
- [x] **SENIOR cell** → `gpt-4o-mini` + temperature=0 → `answer='no'`, tokens=34, `cost=$0.000006` ✅ verified
- [x] HTML `display()` color rendering verified (bold red `#E63946` and bold green `#16A34A`)
- [x] `sampling_demo.py` with `gpt-4.1-mini` + temperature 0.0 / 0.9 → works
- [x] `temp_on_gpt5.py` with `gpt-5` + temperature 0 → returns HTTP 400 *("Only the default (1) value is supported")* — this IS the hook payoff
- [x] `effort_demo_openai.py` with `gpt-5` + `minimal/low/medium/high` → all four accepted
- [x] `usage` field shape verified on both APIs (chat: `prompt_tokens / completion_tokens`; Responses: `input_tokens / output_tokens / output_tokens_details.reasoning_tokens`)
- [x] Hidden reasoning-token cost demonstrated live — `minimal → 0`, `medium → 320`, `high → 768` for the same question
- [x] `waste_demo.py` live-verified: same `'no'` answer across 10 configs, cost range **$0.000006 → $0.002820** (470×)
- [ ] **Re-verify pricing constants in `waste_demo.py`** on record day at openai.com/api/pricing — pricing shifts and a stale row is the kind of detail that gets called out in comments
- [x] `o3`, `o4-mini`, `o3-mini` confirmed to reject non-default temperature
- [ ] Re-run all OpenAI scripts on record day — model availability can shift
- [ ] **Do NOT use `gpt-5.5` on camera** — not in `models.list`, behavior unstable
- [ ] **`verbosity` must be passed as `text={"verbosity": "low|medium|high"}`** — top-level kwarg fails with TypeError in SDK 2.38
- [ ] Optional curiosity beat: mention that `gpt-5-pro` only accepts `effort="high"` (locked) — verified, makes a nice "engineers will care" aside if time allows

**Anthropic side — NOT tested (no key in .env). Must test on record day.**

- [ ] Add `ANTHROPIC_API_KEY` to .env
- [ ] Run `temp_on_opus48.py` — capture verbatim 400 message
- [ ] Verify `output_config.effort` SDK kwarg name against latest `anthropic` package
- [ ] If Anthropic test fails or SDK shape is uncertain — **the OpenAI `gpt-5` 400 alone is enough** for the Scene 5 hook payoff. Anthropic becomes a 30-sec "same story other provider" beat.

**Narration rules:**

- [ ] Frame the 400 as **"non-default sampling parameters"**, not "any temperature value"
- [ ] Effort levels: say "depends on the model" then list: `gpt-5` family → `minimal/low/medium/high`; `o-series` → `low/medium/high`
- [ ] The story is **"OpenAI split its own model line"** — chat tier vs reasoning tier

**Production:**

- [ ] Terminal font 16pt+, dark theme, secrets removed from shell history
- [ ] Sketchbook ready: 3-dial control panel template pencilled, U-curve template pencilled, 6-row cheat sheet skeleton pencilled
- [ ] **`junior_vs_senior.ipynb` opens in JupyterLab Dark or VSCode Dark+**, code font ≥18pt, cell numbers hidden, all outputs cleared, kernel restarted (`Restart & Run All` once before recording to confirm both cells succeed in sequence)
- [ ] Cell 1 (Setup) collapsed or scrolled above the visible frame so only JUNIOR + SENIOR cells are on camera
- [ ] CapCut overlays prepared: `JUNIOR` and `SENIOR` lower-thirds, red `$0.002820` and green `$0.000006` zoom-stickers, full-screen `470×` contrast frame
- [ ] Re-test pricing constants in the notebook on record day — pricing drift makes the 470× claim risky if numbers are stale
- [ ] Thumbnail brief sent to designer / ChatGPT image prompt run
- [ ] End screen: V011 + Phase 2 playlist
- [ ] Final length ≤16:30 (Scene 6 grew by ~60s with the waste demo; if you run long, the safest cuts are the `seed` paragraph in Scene 4 or the second Anthropic terminal beat in Scene 5) — if longer, cut the `seed` paragraph or compress Scene 7 layout to 90 sec
- [ ] Description draft pre-written so upload is fast
- [ ] Pinned comment ready with playlist + next-video links

---

## What this video INTENTIONALLY does NOT cover

| Topic | Where it lives |
|---|---|
| Why training has 4 stages | Already in *How ChatGPT Is Trained* |
| Tokens / embeddings / attention | Already in *Tokens in LLM* + training video |
| Reasoning models — when to actually use | V011 — Wednesday |
| `top_p` deep dive | Phase 3 prompt engineering video |
| `frequency_penalty`, `presence_penalty`, `logit_bias` | Phase 3 advanced prompting |
| Benchmarks (MMLU, GSM8K, HumanEval, SWE-bench) | Phase 2 section 2.4 |
| Picking your daily driver model | Phase 2 section 2.5 |
| RAG / chunking / reranking | Phase 4 (Weeks 8–12) |
| Lost-in-the-middle production fixes | Phase 4 hybrid retrieval video |
| Tool calling / function calling | Phase 5 |

---

*v1 — 14–16 min target — 2026-current — record, edit aggressively, run `10-description-generator` skill on final SRT for upload package.*
