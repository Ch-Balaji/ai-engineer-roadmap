# Slide Deck — Context Engineering (V014)

**Companion deck for** [`V_context-engineering-2026.md`](V_context-engineering-2026.md). Slide-by-slide content + build + design notes. Flow tracks the script beat-for-beat so you can glance at the slide and know where you are in the talk.

> **Condensed 10-slide cut.** All the info from the full outline is preserved — just grouped onto fewer, denser slides. Each slide now uses **progressive builds** (reveal one bullet/region at a time) so it stays "one idea on screen at a time" even though the slide holds more. Never read the slide aloud; the slide is the anchor, your voice is the teaching.

---

## Design System (System A — Editorial, from skill 03)

Apply to **every** slide. This is the in-video deck look, NOT the loud yellow thumbnail style.

| Token | Value | Use |
|---|---|---|
| Background | `#F5EFE6` cream | Every slide bg |
| Card / callout bg | `#FAF6EE` lighter cream | Boxes, the context-window container |
| Accent primary | `#C2562F` rust | Italic serif keywords, the ONE highlight per slide, arrows |
| Heading / structure | `#0F4C4A` teal-deep | Slide titles, the 6-box outlines |
| Callout / warning | `#D6A04A` mustard | "the trap", pricing hint |
| Highlight (sparingly) | `#E4577A` pink | Only the single climactic word ("DEAD", "absorbed") |
| Text primary | `#1A1A1A` | Body |
| Text muted | `#6E665C` | Labels, slide numbers |

**Type:** Display = Inter Tight / Geist Bold (near-black). Accent italic word = Playfair / EB Garamond Italic in rust. Mono labels = JetBrains Mono small-caps (`01`, `02`). **No drop shadows, no gradients, flat editorial.** Slide-number `NN` mono, bottom-right, muted grey.

**Signature treatment:** bold sans headline with **one or two words swapped to rust serif italic** (e.g., "Prompt engineering isn't *dead* — it got *absorbed*").

**Build discipline:** Slides 03 (six boxes) and 06–09 (the four levers) reuse persistent layouts — animate the new piece, don't redraw. The viewer should feel the picture accumulating.

---

## SLIDE 01 — Provocation + the honest turn
**Script:** Hook + promise (0:00–1:15) · **Build in 3 beats**

- **Beat 1 (headline):** PROMPT ENGINEERING IS *DEAD* — "PROMPT ENGINEERING" near-black with red strike-through; **DEAD** in pink serif italic.
- **Beat 2 (the turn):** Not gone. *Absorbed.*
  - Writing a good prompt still matters — it just stopped being *the job.*
  - The prompt is ~**10%** of what the model reads.
  - *(small pie: one thin rust slice = "prompt", rest greyed = "the other 90%")*
- **Beat 3 (agenda):** today → **Part 1:** the 6 things in a context window · **Part 2:** the 4 levers to engineer it.
- **Note:** the "absorbed, not gone" beat MUST land here (by ~0:45) — it's the anti-clickbait guardrail. Mono tag `V014 · PHASE 3 → 6`.

---

## SLIDE 02 — LLM reminder + the running example
**Script:** LLM reference + Part 1 intro (1:15–1:45) · **Build in 2 beats**

- **Beat 1 — stateless box:** `tokens in → [ LLM ] → likely tokens out`. Struck-through below: "❌ remembers you ❌ knows your business". Line: "Everything it needs, *you* place inside — every call." *(callback to V009, keep fast)*
- **Beat 2 — the example we use all video:** WBD Content Intelligence agent. User asks:
  > *"Which scripts mention the Marauder's Map — and summarise how it's described?"*
  - Question on slide: **"What has to fit inside the box for a good answer?"**
  - Show the empty cream **CONTEXT WINDOW** container (teal outline, 6 faint regions).

---

## SLIDE 03 — The 6 things inside a context window
**Script:** Part 1, all six components + growth warning (1:45–6:30) · **Build: 6 regions light up one at a time, then the growth badges**

Persistent box; reveal each region as you narrate it:

1. **USER MESSAGE** — the thing you type. "The only box most people know." `1 of 6`
2. **SYSTEM PROMPT** — always there (even in ChatGPT, unseen). Personality + rules. Chip: *"Cite the asset ID. Never invent a title."*
3. **TOOLS** — descriptions + schemas the model reads to decide what to call. Chips: `search_scripts` · `query_catalog` · `send_result`
4. **RESOURCES** *(draw largest)* — your private data, retrieved for this one call. "The model has never seen WBD's scripts." Tag: ⬆ usually biggest.
5. **ASSISTANT HISTORY** — the model's past replies, fed back.
6. **TOOL-CALL HISTORY** — each search → chunks back → search again; piles up.

- **Closing beat:** **GROWS ↑** badges on Resources, Assistant history, Tool history → "Three of six *grow* as the agent runs."
- **Callback (rust):** *"That whole prompt you built last week lives in ONE box — the system prompt. That's what 'absorbed' means."* (V013 payoff)

---

## SLIDE 04 — The trap: a bigger window won't save you
**Script:** Trap, reasons 1 (6:30–7:00) · **Build: table → fill meter**

- **Headline:** "So just use a million-token model." — *not that simple.*
- **Model table (verify versions on record day):**

| Model (2026) | Advertised window |
|---|---|
| Gemini 2.5 / 3.x Pro | ~1M (up to 2M / 10M) |
| GPT-5.x | ~1M |
| Claude Opus 4.x | 1M |
| Claude Sonnet / Haiku | 200K |
| GPT-5 mini / older | 128K |
| Llama 4 Scout | 10M (advertised) |

- **Reason 1:** the models you actually deploy on are smaller — Sonnet, Haiku, mini = **200K / 128K**. Six boxes, three growing → fills fast (fill meter climbing).
- **Footer (mustard):** ⚠️ pattern matters, not the leaderboard.

---

## SLIDE 05 — The trap: more is *not* better
**Script:** Trap, reason 2 + pricing (7:00–7:30) · **Build: curve → pricing → punchline**

- **Headline:** *Lost in the middle*
- **Visual:** accuracy-vs-fill curve — rises, **peaks ~60–70%**, drops (peak marked rust).
- **Bullets:**
  - Multi-fact retrieval degrades well before the limit — often past **256K–512K**, even on 1M models.
  - Attention favours the **start + end**; the middle gets neglected.
  - Even the bill is a hint: some providers charge **~2×** above 200K. "Don't live up there."
- **Punchline (pink):** More context is *not* better context. → so we **engineer** what goes in. Four levers.

---

## SLIDE 06 — Lever 1: Engineer the system prompt
**Script:** Lever 1 (7:30–8:30) · **Build: dial → 3 bullets**

- **Visual:** dial — **TOO VAGUE** ——●—— **TOO PRESCRIPTIVE**, sweet spot center (rust).
- **Bullets:**
  - ❌ "Do a good job" — too vague.
  - ❌ if-this-then-that flowcharts — too prescriptive (the *engineer's* mistake).
  - ✅ Define **outcomes** + broad approach; let the model find the path.
- **Tag (rust):** "Yes, this is prompt engineering. It didn't die — it became *Lever 1.*"

---

## SLIDE 07 — Lever 2: Describe your tools well
**Script:** Lever 2 (8:30–9:45) · **Build: tool card → 2 rules**

- **Lead:** The model picks tools by *reading their descriptions.* Vague description → wrong call or no call.
- **Tool card:** name / one-line desc / input schema / output schema.
  - `search_scripts: semantic search over WBD script chunks; returns top-k passages with asset IDs.`
- **Two rules:**
  - Specific, **not long.**
  - Always include the **schema** (in + out) — one tool's output is the next step's input.

---

## SLIDE 08 — Lever 3: Retrieve data intelligently (RAG → MCP)
**Script:** Lever 3 (9:45–11:30) · **Build: RAG side → MCP side → pointer trick**

- **Old way — RAG (dump & hope):** vector DB → retrieve anything similar → stuffed context (overflow warning). Fine for a search chatbot; keep it if it's in your stack — but it's *imprecise*, and stuffing hurts (callback to Slide 05).
- **Upgrade — *why MCP exists* (describe → ask → fetch):**
  1. Resources are **described** (cheap, few tokens)
  2. Ask the model: "which do you need?"
  3. Fetch **only those** into the next call
- **Pointer trick:** long record? pass a **user ID** + a tool that expands it — model asks for the full record only if needed. `user_id: 48213 → (tool) → full record`.

---

## SLIDE 09 — Lever 4: Surviving long-horizon agents
**Script:** Lever 4 (11:30–13:30) · **Build: the 3 growing boxes → compaction → memory → sub-agents**

- **Problem:** the three **GROWS ↑** boxes (resources, assistant, tool history) are the enemy on long runs.
- **Compaction:** 50K-token doc → one LLM call → "summarise in 500 words" → carry the summary forward. *(big block ⟶ small block)*
- **Memory:** key-value store beside the agent (`plan → {…}` · `draft → {…}`). Stash out of the window; pull back by key only when needed. Window stays lean.
- **Sub-agents (one line):** heavy retrieval/ranking step → its own sub-agent that returns a clean summary. **Decompose, return less.** *(no microservice tangent)*

---

## SLIDE 10 — Recap + CTA + what's next
**Script:** Recap → CTA → cliffhanger (13:30–15:15) · **Build: recap → "Lever 1" → CTA → next**

- **Recap (split):** left = the 6-box schema (full); right = the 4 levers:
  1. System prompt — outcomes, not flowcharts
  2. Tools — specific + schemas
  3. Retrieval — MCP describe-then-fetch > RAG dump
  4. Long-horizon — compact + memory
- **Title resolved (rust ring on lever 1):** "Prompt engineering didn't die. It became *Lever 1.*" `← V013 lives here`
- **CTA:** Comment **CONTEXT** — building something long-running? Tell me what's eating your window; I'll cover real cases on the live.
- **Cliffhanger / end screen:** **Next: *Memory*** — what to remember, what to forget, recalling you 3 sessions later. Next-video thumb (left) + subscribe (right). Mono `V015`. Small "step by step" in rust.

---

## Flow Logic (why this order)

1. **Slide 01** — hook the V013 crowd, defuse clickbait in 45s, show the map. (was 3 slides)
2. **Slide 02** — minimal LLM reminder + the concrete WBD question that frames everything. (was 2)
3. **Slide 03** — the persistent box fills with all six components + the "your prompt is 1 of 6" payoff. (was 8)
4. **Slides 04–05** — the trap: real model numbers, then the reversal (lost-in-the-middle + pricing). Strongest minute-7 re-engagement. (was 4)
5. **Slides 06–09** — the actionable core, one lever per slide; lever 3 carries the "why MCP" payoff; lever 4 stays tight per your cut. (was 9)
6. **Slide 10** — close the title loop, then push to memory. (was 4)

## Build / Production Checklist
- [ ] Every slide uses **progressive reveal** — don't show all bullets at once (keeps "one idea on screen")
- [ ] Slide 03 box layout is reused/echoed on Slide 09 (the growing boxes) and Slide 10 (recap)
- [ ] Only System A palette — no thumbnail yellow on slides
- [ ] One highlight per slide (rust); reserve pink for "DEAD" / "absorbed" / final punchline only
- [ ] Model table (Slide 04) figures verified on record day
- [ ] Lower-third stays cream + rust per skill 03
- [ ] Export: `slides/V014_context-engineering-2026.key` → `.pdf`
