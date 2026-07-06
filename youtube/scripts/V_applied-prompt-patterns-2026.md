# The 5 Things LLMs Actually Do — Applied Prompt Patterns (2026)

**Full scene-by-scene script** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway), 10 (description). Phase 3 — Prompt Engineering. Follows *Prompt Engineering Masterclass* (the 5-block skeleton). **One unified running dataset throughout** — a pile of ~10 raw customer support tickets (`youtube/notebooks/V014_applied_prompt_patterns/tickets.json`). Every pattern operates on the SAME tickets, in sequence, so by the end the five patterns visibly compose into a tiny agent pipeline.

> **Teaching style locked (V010–V013):** L1 obvious case → L2 plain story → L3 name the term → L4 one step deeper → L5 honest "saved for later". Each pattern is DERIVED on a real ticket in front of the viewer, never asserted.
> **Spine (theory + code crossover):** the reframe is **"prompting isn't one skill — it's five verbs."** Extraction, Classification, Transformation, Generation, Decomposition. Theory map first on the sketchbook (~5 min), then ONE continuous code build where the same ticket pile flows verb → verb. Decomposition is the climax: it's the meta-pattern that orchestrates the other four and quietly becomes an agent — the cliffhanger into Phase 4/5.
> **Prompt location decision (locked):** prompts stay **inline in the code**. We name prompt-versioning as a future topic but do not extract prompts to files in this video.
> **Model decision (locked):** ChatGPT UI for the fast visual beats; **free Groq + Llama** for the Python code so any viewer can follow without paying.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V014 (Phase 3) |
| Slug | `applied-prompt-patterns-2026` |
| Playlist | Phase 3 — Prompt Engineering & API Access |
| Target length | 22 min (hard cap 24) |
| Slot | Mon 7 PM IST |
| Previous video | Prompt Engineering Masterclass — 5 Upgrades (V013) |
| Next video | Context Engineering — The Skill That Replaced Prompt Engineering |
| Medium | **Hybrid.** Sketchbook for the 5-verb map; live ChatGPT UI + Python/Groq for the build. One dataset on screen the whole time. |

## Roadmap Mapping (skill 04)

```
- Phase: 3 — Prompt Engineering & API Access
- Sections covered: 3.6 (Applied prompt patterns: extraction, classification,
                    transformation, generation, decomposition)
- Prerequisites needed: 3.1–3.5 (the 5-block prompt skeleton), API basics, Tokens
- Prerequisite videos: V013 (Prompt Engineering Masterclass), V011 (APIs Explained),
                       V009 (How LLMs Are Built)
- Capstone contribution: indirect — the decomposition pattern is the seed of the
                        Phase 5 agent loop; the extraction/classification prompts
                        get reused in the Phase 4 RAG ingestion video.
- End state: viewer can look at ANY task and instantly name which of the 5 verbs it
            is (or which chain of verbs), then write the right-shaped prompt for it.
```

## Why this video (now)

| Reality (June 2026) | What it means for the script |
|---|---|
| V013 taught *how to structure one prompt*. The obvious next question: "okay, but what do I actually point that prompt at?" | This video answers it — the five task-types every LLM job reduces to. |
| Most "prompt patterns" content is a disconnected listicle (15 prompts you must try!) that ages instantly | We unify all five over ONE dataset and show they COMPOSE. The composition is the evergreen idea, not the list. |
| Beginners write a vague mega-prompt that tries to do everything at once, and get mush | The hook shows exactly that failure on a real ticket, then fixes it by naming the verb. |
| Viewers don't see the line between "prompting" and "building an agent" | Decomposition as the climax draws that line live — five prompts chained = an agent. |

## Playlist Callback Map (3 references, ~30 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 1:00 | Backward bridge | V013 — *Masterclass* | "You can structure a prompt now — here's what to point it at." |
| 2 | 6:00 | Lean-in | V011 — *APIs* | The `messages` array from the API video is where these prompts live. |
| 3 | 20:30 | Cliffhanger | Phase 4/5 — *RAG / Agent loop* | "Five prompts chained is one step from an agent." |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–1:00 | **Hook — one mega-prompt mushes a real ticket** | Split screen: ChatGPT + face cam; bad output held on screen |
| 1:00–2:00 | Bridge + V013 callback + promise (5 verbs) | Face cam → animated 5-item list |
| 2:00–6:30 | **The 5-verb map (theory)** | Sketchbook full-screen — derive each verb from a ticket |
| 6:30–9:00 | Pattern 1 — **Extraction** (live on the tickets) | ChatGPT UI → Python/Groq, JSON out |
| 9:00–11:00 | Pattern 2 — **Classification** (intent + sentiment + routing) | Python/Groq, enum-constrained |
| 11:00–13:00 | Pattern 3 — **Transformation** (summarize + translate the Hindi ticket) | Python/Groq |
| 13:00–15:30 | Pattern 4 — **Generation** (draft reply + generate SQL) | Python/Groq + tiny orders table |
| 15:30–20:00 | Pattern 5 — **Decomposition** (the tangled ticket → chain of the other 4) | Sketchbook flow → Python loop = mini pipeline |
| 20:00–21:30 | The pipeline reveal + "this is almost an agent" | Sketchbook full-screen (screenshot moment) |
| 21:30–22:30 | Cliffhanger to Context Engineering + outro | Face cam |

## Title + Thumbnail Brief (skill 06)

```
- Title formula: number + curiosity + payoff
- Final title: The 5 Things LLMs Actually Do — Applied Prompt Patterns (2026)
- A/B title: Stop Writing One Giant Prompt — Do These 5 Instead (2026)
- Subject pose: Confident, holding up an open hand (five fingers) mid-explanation
- Outfit: Phase-3 series identity (continue from V013)
- Background: Black + circuit overlay
  Center: one messy ticket card on the left with a red "?" → five clean labeled
  cards on the right: EXTRACT · CLASSIFY · TRANSFORM · GENERATE · DECOMPOSE
- Primary text (white, Anton ALL CAPS, top):
    5 PROMPT PATTERNS
- Highlight text (yellow, the single yellow element):
    1 PIPELINE
- Telugu badge (red, bottom-right):
    "ఇవి తెలిస్తే చాలు"  (translation: "Know these and that's enough")
- Social-proof badge (top-left): "8+ YEARS IN AI"
- Note: ONE yellow element only (1 PIPELINE). Continues the single-yellow-word system.
```

---

## HOOK FACTORY — 5 drafts (skill 07), recommended pick locked below

```
HOOK A — Live Demo First / The Mush (RECOMMENDED)
"Watch this. Here's one real customer support ticket — angry, messy, has an order
number buried in it. I'm going to do what most people do: write ONE big prompt that
says 'read this ticket and handle it.' [Run it.] Look at the output. It half-extracts
the order ID, half-guesses the sentiment, writes a reply that invents a refund policy
we don't have, and misses that the customer threatened a chargeback. It's mush. Now
watch what happens when I stop asking for everything at once — and instead name the
FIVE things an LLM actually does, one at a time. By the end, these same five prompts
will run as a pipeline that handles this ticket end to end."
[Visual: split screen — ChatGPT left, face cam right. Bad output held 5 seconds so the
viewer reads the invented refund policy. Then cut to the 5-verb list.]

HOOK B — Contrarian
"Prompt engineering is not one skill. It's five. And once you can name the five, you'll
never stare at a blank prompt again — you'll just ask 'which of the five is this?' and
the prompt writes itself. Today, all five, on one pile of real support tickets."
[Visual: face cam → five fingers → 5-card graphic]

HOOK C — Production Incident
"A support automation I reviewed was sending customers refund amounts that didn't exist.
One prompt was doing extraction, classification, and reply-writing all at once, and when
one part guessed wrong, the whole answer was confidently wrong. The fix was splitting it
into five smaller jobs. Today I'll show you those five — on real tickets."
[Visual: face cam → screenshot of a wrong refund reply → fix]

HOOK D — Comment Callback
"After the prompt masterclass, a lot of you asked the same thing: 'Okay, I can structure
a prompt now — but what do I actually use it FOR?' This is the answer. Every LLM task you
will ever build is one of five patterns. Let me show you all five in 22 minutes."
[Visual: comment screenshot → face cam]

HOOK E — Shock/Stakes
"One vague prompt that does everything will fail silently in production and you won't know
until a customer screenshots it on Twitter. Five small, named prompts won't. Here's the
difference — live, on real support tickets."
[Visual: face cam → a 'silent failure' diagram]
```

**PICK: HOOK A (The Mush).** Why: it opens on the exact mistake the audience makes (one mega-prompt), shows a concrete, embarrassing failure (an invented refund policy) in the first 20 seconds, and the fix is the whole video. The same ticket from the hook returns at the climax fully handled — clean promise/payoff loop. Fallback: Hook D if the live run is risky on record day.

---

## FINAL HOOK — The Mush (LOCKED)

> *[Open on split screen: ChatGPT UI left, face cam right. One ticket (TKT-1001, the cracked headphones / chargeback threat) is pasted into a single prompt: "Read this support ticket and handle it." Run it. The output is a polite wall of text that invents a "30-day no-questions refund policy", states the wrong order number, and never flags the chargeback threat. Hold it on screen for 5 seconds.]*
>
> **Spoken:**
>
> "Look at what just happened. I gave the model one real support ticket and one lazy instruction — 'handle it.' And it *sounds* confident. But it invented a refund policy we don't have. It got the order number wrong. And it completely missed that this customer is about to do a chargeback. In production, this is the answer that ends up in a screenshot.
>
> **[Cut to face cam.]**
>
> Here's the thing nobody tells you: prompting isn't one skill. Every job you'll ever hand an LLM is really one of **five** things — extraction, classification, transformation, generation, and decomposition. Name the right one, and the prompt almost writes itself. Mix them all into one prompt, and you get the mush you just saw.
>
> Today I'll show you all five — on this exact pile of support tickets — and by the end, these five prompts will run as one pipeline that handles this ticket properly, end to end. No black box."

---

## SCENE 2 — BRIDGE + V013 CALLBACK (1:00 – 2:00)

**On screen:** Sketchbook. Phase-3 chain: `API → Tokens → 5-Block Skeleton (V013) → [TODAY: the 5 verbs you point it at]`.

**Spoken:**

> Quick context. Last video — the prompt masterclass — you learned *how to structure* a prompt: role, context, task, format, constraints, examples. That's the skeleton.
>
> But a skeleton needs a job. And a lot of you asked the obvious next question: *"Okay — I can write a clean prompt now. But what do I actually point it at?"*
>
> That's today. We're not learning new prompt structure. We're learning the five *shapes of task* you'll apply that structure to — for the rest of your career. And we're doing all five on something real: a folder of messy customer support tickets, the kind every company drowns in.

---

## SCENE 3 — THE 5-VERB MAP (2:00 – 6:30) | THE THEORY | L3 name → L4 deeper

**On screen:** Sketchbook full-screen. Draw one ticket box on the left. Then draw five arrows out of it, labeling each verb as you derive it from THAT ticket. End with the five stacked as a vertical list.

**Spoken (intro):**

> Here's the whole mental model on one page. Take one ticket. There are exactly five *kinds* of thing I might ask an LLM to do with it. Watch me pull each one out of this single ticket.

**Verb 1 — EXTRACTION.** *(Draw arrow: ticket → {order_id, date, amount}.)*

> One — **extraction.** Pull structured facts out of unstructured text. Order number, date, amount, product name — they're all sitting inside this paragraph as words. Extraction turns that messy paragraph into clean fields a database can use. The signal: *"I need data OUT of text."*

**Verb 2 — CLASSIFICATION.** *(Draw arrow: ticket → [REFUND] [NEGATIVE] [URGENT].)*

> Two — **classification.** Put the text into a box. Is this a refund, a bug, a billing issue, a how-to? Is the sentiment angry or happy? Is it urgent? Classification picks from a *fixed set of labels*. The signal: *"I need to sort this into known buckets."*

**Verb 3 — TRANSFORMATION.** *(Draw arrow: ticket → shorter / another language.)*

> Three — **transformation.** Same meaning, different form. Summarize a long rambling ticket into two lines. Translate a Hindi ticket into English for an agent who doesn't read Hindi. Reformat. The content is the same — the *shape* changes. The signal: *"I have text, I want the same text in a different form."*

**Verb 4 — GENERATION.** *(Draw arrow: ticket → reply / SQL.)*

> Four — **generation.** Create something *new* from the input. Draft the reply to the customer. Or generate the SQL query that looks up their order. This is the verb everyone thinks of first when they hear 'AI' — but notice it's only one of five. The signal: *"I need new content that didn't exist before."*

**Verb 5 — DECOMPOSITION.** *(Draw arrow: big tangled ticket → break into sub-tasks → the other four.)*

> Five — **decomposition.** This one's different — it's the *boss* of the other four. Some tickets aren't one task. [Point to TKT-1009.] 'Tell me if it shipped, cancel one item, refund a fee I didn't agree to, and switch my billing plan.' That's four requests in one message. Decomposition is the verb that *breaks a big request into smaller ones* — and each smaller one is just extraction, classification, transformation, or generation again. The signal: *"This is too big for one prompt."*

**The key beat (L4).** *(Circle decomposition, draw lines from it to the other four.)*

> Here's the part that makes this more than a list. The first four are *atomic* — one prompt, one job. The fifth, decomposition, is how you *chain* the first four together. And the moment you chain prompts where the output of one feeds the next — congratulations, you've basically built an agent. We'll get there at the end.

**[CapCut sticker: `THE 5 VERBS: Extract · Classify · Transform · Generate · Decompose. The first four are atomic. The fifth chains them.`]**

---

## SCENE 4 — PATTERN 1: EXTRACTION (6:30 – 9:00) | live

**On screen:** Show `tickets.json` briefly. Then ChatGPT UI on TKT-1001, then Python with Groq.

**Spoken:**

> Let's build. Here's our data — ten real-shaped support tickets in a JSON file. Notice the order numbers, dates, amounts are all buried *inside* the message text. That's the point — extraction's whole job is digging them out.
>
> Start in the ChatGPT UI so you can see it, then we move to code. *(Callback to V011: this is the same `messages` array, just in Python now.)*

**[On-screen prompt — note: kept INLINE in the code, per our decision.]**

```python
from groq import Groq
import json

client = Groq()  # free tier — key in env, like the APIs video

ticket = tickets[0]["raw_message"]

prompt = f"""Extract the following fields from the support ticket.
Return ONLY valid JSON, no prose.

Fields:
- order_id (string or null)
- date_mentioned (ISO format or null)
- amount (number or null)
- product (string or null)

Ticket:
\"\"\"{ticket}\"\"\""""

resp = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
)
print(resp.choices[0].message.content)
```

> Two things to call out. **Temperature zero** — extraction is not creative, I want the same answer every time. And I'm telling it to return *only* JSON, because the next step in our pipeline is code, and code needs structure, not a friendly paragraph.
>
> *(Run it. Show the clean JSON: order_id ORD-88231, amount 7499, etc.)*
>
> **The failure, honestly:** [Show a ticket with no order ID, e.g. TKT-1005.] When the field genuinely isn't there, a weak prompt will *hallucinate* one. That's why I said `or null` explicitly. Watch — on this ticket it correctly returns null instead of inventing an order. This breaks in production if you don't force the null option.

---

## SCENE 5 — PATTERN 2: CLASSIFICATION (9:00 – 11:00) | live

**On screen:** Python/Groq, looping over a few tickets.

**Spoken:**

> Pattern two — classification. The trick here is *constraining the labels*. If I just say 'what category is this,' the model will invent its own categories and you'll get 'inquiry,' 'general,' 'misc' — useless. I give it the exact enum.

```python
prompt = f"""Classify this support ticket.
Return ONLY JSON with these exact fields and allowed values:
- category: one of ["refund", "bug", "billing", "shipping", "how_to", "cancellation", "feature_request"]
- sentiment: one of ["angry", "neutral", "happy"]
- priority: one of ["low", "medium", "high"]

Ticket:
\"\"\"{ticket}\"\"\""""
```

> *(Run it over TKT-1001, 1004, 1010. Show: refund/angry/high, how_to/happy/low, cancellation/angry/high.)*
>
> See how `priority: high` falls out for the chargeback threat and the cancellation? That's the routing signal. In a real system this JSON decides *which queue the ticket goes to and how fast.* Same idea as the masterclass — constraints aren't optional politeness, they're what makes the output usable by code.
>
> **Honest note — I'm simplifying:** for a million tickets a day, you'd fine-tune a tiny model for this, like we discussed in the model-selection video. For now, a constrained prompt on a cheap model is plenty.

---

## SCENE 6 — PATTERN 3: TRANSFORMATION (11:00 – 13:00) | live

**On screen:** TKT-1005 (the long rambling one) → summary. Then TKT-1006 (Hindi) → English.

**Spoken:**

> Pattern three — transformation. Same meaning, new form. Two flavors back to back.
>
> First, summarize. [TKT-1005 — the three-paragraph SmartScale ramble.] An agent doesn't have time to read this. I want two lines.

```python
prompt = f"""Summarize this ticket in at most 2 sentences,
preserving every distinct issue the customer raised.

Ticket:
\"\"\"{ticket}\"\"\""""
```

> *(Run it. Show: "Customer reports SmartScale sync issues — duplicate readings, delayed app sync, and a stale weight reading. Also notes minor peeling on the band.")*
>
> Notice I said *preserve every distinct issue* — without that, summaries quietly drop information, and in support that's a missed complaint. That constraint is the difference between a useful summary and a dangerous one.
>
> Second flavor — translation. [TKT-1006, the Hindi ticket.] Same content, different language, so a non-Hindi agent can act on it.

```python
prompt = f"""Translate this ticket to English.
Keep order numbers and amounts exactly as written.

Ticket:
\"\"\"{ticket}\"\"\""""
```

> *(Run it. "My order ORD-91540 hasn't arrived yet. I ordered 5 days ago, for 3,299 rupees...")* Same meaning. New shape. That's transformation.

---

## SCENE 7 — PATTERN 4: GENERATION (13:00 – 15:30) | live

**On screen:** Draft a reply, then generate SQL against a tiny `orders` table sketch.

**Spoken:**

> Pattern four — generation. Now we create something new. Two examples, because generation has two faces: *language out* and *code out*.
>
> Face one — the reply. But notice: I'm not going to let it invent a policy like the hook did. I *feed it* the extracted facts and a real policy. This is generation grounded in the earlier steps.

```python
prompt = f"""You are a support agent for a D2C electronics brand.
Write a reply (max 4 sentences, calm, specific).

Known facts (do not contradict these):
- order_id: {extracted['order_id']}
- issue: {classification['category']}
- policy: damaged items are eligible for a full refund within 14 days of delivery.

Customer message:
\"\"\"{ticket}\"\"\""""
```

> *(Run on TKT-1001. Output references the real order, the real 14-day policy, acknowledges the chargeback concern, no invented nonsense.)* Compare this to the hook. Same model. The difference is the model is *generating* on top of clean extracted facts instead of guessing everything at once.
>
> Face two — generating SQL. Say the agent needs to look up the order. The LLM can write the query.

```python
prompt = f"""Generate a single SQL query for this request.
Table: orders(order_id, customer, status, amount, ordered_at, shipped_at)
Return ONLY the SQL.

Request: look up the status and shipped date for order {extracted['order_id']}."""
```

> *(Show the SELECT.)* **Big honesty marker — this breaks in production if you trust it blindly:** never run model-generated SQL straight against your database. You validate it, you use read-only access, you parameterize. Generation is powerful and it's the one you must guardrail the hardest. We'll do that properly in the tools phase.

---

## SCENE 8 — PATTERN 5: DECOMPOSITION (15:30 – 20:00) | THE CLIMAX | L4→L5

**On screen:** Sketchbook flow for TKT-1009 (the tangled four-in-one ticket), then Python that chains the previous four prompts.

**Spoken:**

> Pattern five — decomposition. The boss. Here's the ticket that breaks everything. [TKT-1009.] Read it: *has it shipped? cancel the blue case. refund a priority fee I didn't pick. switch me to monthly billing.* That's four separate jobs hiding in one message.
>
> If I throw this at one 'handle it' prompt — we're back to the mush from the hook. So instead, I decompose. Step one is itself a prompt: *break this into a list of atomic sub-tasks.*

```python
prompt = f"""Break this ticket into a list of atomic sub-tasks.
Return JSON: a list of objects with fields "task" and "type",
where type is one of ["extraction","classification","transformation","generation"].

Ticket:
\"\"\"{ticket}\"\"\""""
```

> *(Run it. Output: 4 sub-tasks, each tagged with one of our four verbs.)*
>
> Look what just happened. The model didn't *solve* the ticket — it *planned* it. And every sub-task it produced is one of the four atomic verbs we already built. So now I just route each sub-task to the right prompt.

```python
for sub in subtasks:
    if sub["type"] == "extraction":
        result = run_extraction(sub["task"], ticket)
    elif sub["type"] == "classification":
        result = run_classification(sub["task"], ticket)
    elif sub["type"] == "generation":
        result = run_generation(sub["task"], ticket, facts)
    # ... transformation likewise
    results.append(result)
```

> *(Run the loop. Show each sub-task resolved: shipped-status extracted, cancellation classified+routed, fee checked, billing-change drafted. Then a final generation step stitches one clean reply.)*
>
> Stop and look at what we just made. A planner prompt that splits the work, then a loop that sends each piece to the right specialist prompt, then a final prompt that assembles the answer. **That is the entire video on one screen** — and it handled the ticket the hook couldn't.

**[CapCut sticker: `DECOMPOSE = plan into sub-tasks → route each to one of the 4 atomic verbs → assemble. That loop is the seed of an agent.`]**

**L5 honest:**

> One honest boundary: real decomposition gets harder when sub-tasks *depend* on each other — task 2 needs the result of task 1. Handling that ordering, with memory and retries, is exactly what the **agent loop** is, and that's a whole phase. Today you've seen the seed. Don't over-build it yet.

---

## SCENE 9 — THE PIPELINE REVEAL (20:00 – 21:30) | screenshot moment

**On screen:** Sketchbook full-screen, clean, held for screenshot.

```
APPLIED PROMPT PATTERNS — THE 5 VERBS

ATOMIC (one prompt, one job):
  1. EXTRACTION      text → structured fields      (temp 0, force null)
  2. CLASSIFICATION  text → fixed labels           (constrain the enum)
  3. TRANSFORMATION  text → same meaning, new form (summarize / translate)
  4. GENERATION      input → new content           (ground it; guardrail SQL)

ORCHESTRATOR:
  5. DECOMPOSITION   big request → plan → route to 1–4 → assemble

RULE: don't write one prompt that does everything. Name the verb,
      write the small prompt, chain them when the task is big.
      Chained prompts where output feeds input = an agent.
```

**Spoken:**

> Screenshot this. Next time you face any LLM task, you don't stare at a blank prompt. You ask one question: *which verb is this?* And if the answer is 'more than one' — you decompose. That single habit is the difference between the mush in the hook and the pipeline you just built.

---

## SCENE 10 — CLIFFHANGER + OUTRO (21:30 – 22:30)

**On screen:** Face cam.

**Spoken:**

> That's applied prompt patterns — the five verbs that cover basically every LLM task you'll ever write. But notice something about our pipeline: every step re-read the *whole* ticket, and we passed facts around by hand. That works for one short ticket. What happens when the input is a 300-page document, or a conversation that's gone for fifty turns? You run out of room, and you have to get deliberate about *what* you feed the model and *when*.
>
> That's the next skill — and in 2026 it's the one that actually replaced prompt engineering: **context engineering.** That's the next video. Subscribe so it reaches you at 7 PM.
>
> The tickets file and all five prompts are in the repo, link in the description. Go run them on your own data — that's how this sticks. See you in the next one.

---

## Production Notes / Code Repo

- Dataset: `youtube/notebooks/V014_applied_prompt_patterns/tickets.json` (10 tickets — includes TKT-1006 Hindi for translation, TKT-1009 four-in-one for decomposition, TKT-1005 long ramble for summarization, TKT-1001 chargeback for the hook/generation).
- Prompts: **inline in the code** (decision locked). Mention prompt-versioning as a future topic; do not extract to files on camera.
- Model: free Groq + `llama-3.3-70b-versatile` for code; ChatGPT UI for the first visual beat only.
- Each pattern: show one success + one honest failure/guardrail (per voice skill — no happy-path-only).

## Description / Tags (hand off to skill 10 after recording)

- Target keyword: `prompt patterns` / `LLM prompt patterns`
- Chapters map 1:1 to the 9 scenes above.
- Title (final): The 5 Things LLMs Actually Do — Applied Prompt Patterns (2026)
