# The Brain in a Windowless Room — How an LLM Actually Thinks

**Full scene-by-scene video script** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway). Follows *How ChatGPT Is Trained* in the playlist.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V010 |
| Slug | `brain-in-windowless-room` |
| Playlist | Phase 2 — LLM Mental Model |
| Target length | 28–32 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | How ChatGPT Is Trained (How LLMs Are Built) |
| Next video | Reasoning Models vs Base Models — When Each Wins in 2026 |

## Roadmap Mapping

```
- Phase: 2 — Mental Model of an LLM
- Sections covered: 2.1 (What an LLM actually is), 2.2 (How an LLM thinks)
- Prerequisites needed: API access basics, tokens, how LLMs are trained (4 stages)
- Prerequisite videos: Working With API, Tokens in LLM, How ChatGPT Is Trained
- Capstone contribution: no
- End state (from roadmap): Explain to a non-technical PM why ChatGPT made up a fact; know which knob to turn when outputs vary
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:30 Hook | Sketchbook full-screen — draw windowless room + door slot live |
| 0:30–2:30 Bridge | Sketchbook + face-cam PiP; series flow diagram |
| 2:30–5:30 What an LLM is (2.1) | Sketchbook — room analogy deepened |
| 5:30–8:30 Same prompt, different answer | Mac screen — two API runs side by side |
| 8:30–12:00 Probabilistic generation | Sketchbook softmax diagram → screen `logprobs=True` |
| 12:00–14:00 Knowledge cutoff | Sketchbook calendar frozen → face cam |
| 14:00–18:30 Tokens + context window | Sketchbook → screen tiktoken → callback Tokens video |
| 18:30–20:30 Lost in the middle | Sketchbook U-curve attention |
| 20:30–22:30 Transformer + attention (30k ft) | Sketchbook only — no math |
| 22:30–25:30 Sampling live demo | Mac — temperature 0 vs 0.9, top_p |
| 25:30–27:30 Behaviors map + common mistakes | Sketchbook table |
| 27:30–28:30 Roadmap on screen | Browser — roadmap site |
| 28:30–30:00 Recap cheat sheet + cliffhanger | Sketchbook → face cam |

## Title + Thumbnail Brief (skill 06)

```
- Title formula: T10 (Senior Engineer)
- Final title: How an LLM Actually Thinks (Senior Engineer Mental Model)
- Char count: 56
- Alt A/B: The Brain in a Windowless Room — How ChatGPT Works
- Subject pose: Confident, calm, direct eye contact
- Outfit: Brown bomber jacket + black zip-up (locked)
- Background: Black + circuit overlay + warm rim light upper-right
- Primary text (white, Anton ALL CAPS):
    HOW AN LLM
    ACTUALLY
- Highlight text (yellow + brush band):
    THINKS
- Telugu badge (red, bottom-right):
    "ఇది అందరికీ తెలియదు"
- Social-proof badge (top-left, if true at publish):
    "17K+ SUBSCRIBERS" or "110K+ ROADMAP VIEWS"
- Tech-stack icons (bottom):
    OpenAI · Anthropic · tiktoken · Hugging Face
```

---

## 5 HOOKS (skill 07)

### HOOK A — Windowless Room (RECOMMENDED)
> "Imagine a brilliant person locked in a room. No windows. No internet. No phone. The only way in or out is a slot in the door — you slide a question through, they slide an answer back. They have read more books than any human alive. But they do not know what year it is today. They cannot check anything. They cannot remember who asked two minutes ago. That person is an LLM. Everything strange about ChatGPT makes sense once you accept the room."
> [Visual: Sketchbook — hand draws closed room, door, slot, question slip going in, answer slip coming out]

### HOOK B — Comment Callback
> "After the How ChatGPT Is Trained video, hundreds of you asked the same thing: 'Okay, I know pre-training, SFT, RLHF — but when I type a question, what is actually happening inside?' Fair. Today we open the room."
> [Visual: Screenshot of YouTube comments → sketchbook room drawing]

### HOOK C — Live Demo First
> "Watch this. Same prompt. Same model. Same temperature. I will run it twice."
> [Visual: Terminal — two outputs appear, visibly different → freeze → face cam: "If it is the same brain, why two different answers?"]

### HOOK D — Production Incident (Mental Model)
> "A PM asked me: 'Why did ChatGPT invent a legal case that does not exist?' I said: 'It is not lying. It is not searching. It is predicting the next likely token.' She stared at me. That stare is why this video exists."
> [Visual: Face cam → sketchbook: GENERATE not RETRIEVE in large letters]

### HOOK E — Shock Statistic
> "You paste 120,000 tokens into a 128k context model. You assume everything you pasted is 'in memory.' It is not. Research shows accuracy on facts buried in the middle of long prompts can drop by 20% or more. The model did not forget — the room has a shape. Today I show you that shape."
> [Visual: Chart or sketch — high attention at start/end, weak middle]

**Recommended**: HOOK A — this analogy is the title of the video and the mental model for the entire Phase 2 playlist. Draw it live in the first 15 seconds; the viewer stays to see the rest of the room filled in.

---

## SCENE 1 — HOOK (0:00 – 0:30)

**On screen**: Sketchbook full-screen. Hand draws as you speak — no face until the last line.

**Spoken**:

> Imagine a brilliant person locked in a room.
>
> **[Draw a box — the room. No windows.]**
>
> No windows. No internet. No phone.
>
> **[Draw a narrow slot in the door.]**
>
> The only way information gets in or out is through this slot. You slide a question through. They write an answer and slide it back.
>
> **[Draw arrow: question in → answer out]**
>
> They have read more books than any human alive. Patterns from the entire internet — frozen at the day training stopped.
>
> But they do not know what year it is right now. They cannot open Google. They cannot remember the last person who knocked.
>
> **[Write in large letters: THIS IS AN LLM]**
>
> That is an LLM. Not a search engine. Not a database. A brain in a windowless room.
>
> The whole rest of this roadmap — prompts, RAG, tools, agents — makes sense once you accept the room.

**[0:28 — knowledge gap: "what are the rules of this room?"]**

---

## SCENE 2 — CONTEXT BRIDGE (0:30 – 2:30)

**On screen**: Sketchbook + face-cam PiP bottom-right. Draw the series flow.

**Spoken**:

> If you have been following this channel — three videos set up today.
>
> **[Draw boxes connected left to right]**
>
> First — the API video. You learned how to talk to ChatGPT from your own code. Request in, response out.
>
> Second — the tokens video. You learned the model does not eat words. It eats tokens. And every token has a cost.
>
> Third — How ChatGPT Is Trained. Pre-training, SFT, RLHF, inference. The recipe. How $100 million became a model.
>
> **[Circle a new box: "How It THINKS" — write TODAY]**
>
> Today is the missing piece. Not how the model was built — how it behaves when you use it.
>
> This is Phase 2 of the AI Engineer Roadmap — sections 2.1 and 2.2. Mental model of an LLM. Almost no heavy code today. Just clarity.
>
> And I am making you one promise. By the end of this video, when ChatGPT hallucinates, refuses a question, gives a different answer the second time you run it, or silently ignores the middle of your long prompt — you will know which part of the room broke. Not magic. Mechanics.

**[Retention beat: "which part of the room broke" — payoffs in Scene 11.]**

---

## SCENE 3 — WHAT AN LLM ACTUALLY IS (2.1) (2:30 – 5:30)

**On screen**: Sketchbook full-screen.

**Spoken**:

> Section 2.1 — what an LLM actually is. Three facts. Everything else hangs on these.

**Fact 1 — Trained on a fixed snapshot**

> The person in the room finished reading on a specific date. That is the knowledge cutoff.
>
> **[Draw a calendar on the wall inside the room — last date marked TRAINING END]**
>
> Everything after that date? Never entered the room. ChatGPT does not know who won yesterday's cricket match unless you tell it in the prompt or you give it a tool to search — Phase 5.
>
> When someone says "the model is outdated" — they mean the snapshot is old. Not that the model is lazy.

**Fact 2 — Probabilistic generation, not retrieval**

> **[Cross out the word SEARCH. Write GENERATE.]**
>
> The room does not have a filing cabinet. It does not look up "capital of France" and return a card.
>
> It predicts the next token — one piece at a time — based on patterns learned during training.
>
> "Paris" appears because after billions of examples, `capital` + `France` → `Paris` was the highest-probability continuation. Not because someone stored a fact labeled France.

**Fact 3 — Same prompt, different outputs**

> Because each step is probabilistic, the same question can produce slightly different answers.
>
> That is not a bug in your code. That is the design of the room — unless you turn the randomness knobs down. We will open those knobs in Scene 9.

**Analogy lock-in**:

> Quick check. If I ask "what is 2 + 2?" — the room is so confident the next tokens are `4` that every run looks identical.
>
> If I ask "write me a poem about Hyderabad" — many valid continuations exist. Different runs, different poems. Same room. Different probability landscape.

**[Bridge: "Let me prove Fact 3 on screen right now."]**

---

## SCENE 4 — THE PROBLEM: SAME PROMPT, DIFFERENT ANSWER (5:30 – 8:30)

**On screen**: Mac terminal — two panes or sequential runs. `repro_same_prompt.py` in repo.

**Spoken**:

> Watch this. I will call the OpenAI API twice. Same model — `gpt-4o-mini`. Same system prompt. Same user message. Same temperature — `0.7`.
>
> **[Run script — two completions print side by side.]**
>
> ```python
> from openai import OpenAI
> client = OpenAI()
> prompt = "Explain RAG in exactly 3 bullet points."
> for i in range(2):
>     r = client.chat.completions.create(
>         model="gpt-4o-mini",
>         messages=[{"role": "user", "content": prompt}],
>         temperature=0.7,
>     )
>     print(f"--- Run {i+1} ---")
>     print(r.choices[0].message.content)
> ```
>
> Different bullet wording. Maybe different ordering. Maybe a different fourth bullet sneaks in.
>
> I ask engineers in interviews: "Why?" The most common wrong answer: "the model is random." Too vague. Useless in production.
>
> The right answer starts here: **at every token step, the model samples from a probability distribution.** Different sample → different path → different paragraph.
>
> **[Open loop — planted here, resolved Scene 9:]**
>
> In about 17 minutes I will show you the exact two parameters — `temperature` and `top_p` — that control how wild that sampling is. And I will show you `logprobs` so you see the actual probabilities, not just the final text.

---

## SCENE 5 — PROBABILISTIC GENERATION + LOGPROBS (8:30 – 12:00)

**On screen**: Sketchbook → Mac screen.

**Spoken**:

> Let me draw what happens inside the room for one token step.
>
> **[Sketchbook: input tokens → model → output bar chart of top-5 next tokens with %]**
>
> The model outputs a score for every possible next token. Softmax turns scores into probabilities. They must sum to 100%.
>
> Example — the context ends with: "The capital of France is"
>
> Top candidates might look like:
> - ` Paris` — 82%
> - ` Lyon` — 4%
> - ` the` — 3%
> - …
>
> The model **samples** one token from that distribution. Sample again — you might occasionally get a wrong city. That is hallucination at the token level: a low-probability token got picked, or the context was misleading.

**Screen demo — logprobs**:

> Do not take my word for it. Let us ask the API to show its work.
>
> ```python
> r = client.chat.completions.create(
>     model="gpt-4o-mini",
>     messages=[{"role": "user", "content": "The capital of France is"}],
>     max_tokens=5,
>     logprobs=True,
>     top_logprobs=3,
> )
> for t in r.choices[0].logprobs.content:
>     print(t.token, t.top_logprobs)
> ```
>
> **[Scroll terminal output — viewer sees token + probability pairs.]**
>
> See? No black box. Not magic. A ranked list of likely next tokens, chosen one step at a time. The entire answer is thousands of these micro-decisions chained together.

**PM script (say it cleanly)**:

> If your product manager asks "why did it make up a citation?" — your answer:
>
> *"The model does not retrieve facts. It generates text token by token from learned patterns. Sometimes a plausible-sounding but false continuation wins the probability race. We fix that with RAG, tools, or guardrails — not by asking it to try harder."*

**[Bridge: "Generation explains wrong facts. Cutoff explains missing facts. Next — the cutoff."]**

---

## SCENE 6 — KNOWLEDGE CUTOFF (12:00 – 14:00)

**On screen**: Sketchbook — calendar + door slot.

**Spoken**:

> Fact 1 again — the snapshot.
>
> GPT-4o, Claude, Gemini — each has a training cutoff date published by the vendor. Anything after that date was never in the training data.
>
> **[Write on sketchbook: KNOWLEDGE CUTOFF = last day of reading]**
>
> So when the model confidently discusses a 2025 paper that does not exist — it is not lying. It is completing a pattern that *looks like* a paper citation. The room never saw the real paper.
>
> Two production fixes — names only today, depth later:
> - **RAG** (Phase 4) — slide fresh documents through the door slot with the question.
> - **Tools** (Phase 5) — give the room a phone: web search, APIs, databases.
>
> Without those, you are asking a 2023 snapshot to answer a 2026 question. It will try. It will often guess.

---

## SCENE 7 — TOKENS + CONTEXT WINDOW (2.2) (14:00 – 18:30)

**On screen**: Sketchbook → Mac (`tiktoken` REPL) → sketchbook.

**Spoken**:

> Section 2.2 — how an LLM thinks. The room has a second constraint: **the slot has a size limit**, measured in tokens — not words.

**Callback to Tokens video**:

> I made a full video on tokenization. Link in the description. Today — the mental model only.
>
> **[Draw the door slot. Label: MAX TOKENS = context window.]**

**tiktoken demo (2 min)**:

> ```python
> import tiktoken
> enc = tiktoken.encoding_for_model("gpt-4o")
> len(enc.encode("hello"))
> # 1 token
> len(enc.encode("antidisestablishmentarianism"))
> # 6 tokens
> ```
>
> Same language. Wildly different token count. Your API bill counts tokens. Your context window counts tokens. Not pages. Not characters.

**Context window**:

> `gpt-4o` might advertise 128k tokens. That sounds like "paste my entire codebase." Technically you can. Practically — the room degrades.

> Everything you send — system prompt, retrieved chunks, chat history, your question — competes for the same slot. Fill the slot → something gets truncated. Often silently. No error. No warning. The model just never saw the middle pages.

**Mid-video story (skill 02 — STORY_INFOSYS_MAINFRAMES, Framing C "Lost")**:

> Quick personal note. On Infosys mainframes, my worst debugging nights were not when the code was wrong — when I did not understand the system underneath. I would patch one symptom and create three new ones.
>
> Every "my agent is broken" message I get on this channel eventually traces back to two roots: **probabilistic generation** or **context limits**. Skip this video, you will burn months on symptoms.

**CTA hint (skill 09 — Phase 1, 15 sec max)**:

> If you want structured help on resume or mock interviews, there is a form in the description. For now — back to the slot size.

---

## SCENE 8 — LOST IN THE MIDDLE (18:30 – 20:30)

**On screen**: Sketchbook — U-shaped attention curve.

**Spoken**:

> There is a paper — *Lost in the Middle* — engineers should know the name even if they never read it.
>
> **[Draw attention strength: HIGH at start, LOW in middle, HIGH at end — U-shape]**
>
> When your prompt is long, the model pays more attention to the beginning and the end. Facts buried in the middle get missed. Your RAG retrieved the right chunk, placed it in the middle of a 40-page prompt, and the model ignored it. Looks like "RAG is broken." Often it is "context shape is broken."
>
> I am simplifying — attention is more nuanced. But this U-shape is the mental model that saves you in Phase 4.
>
> Rule for production: **put the critical instruction and the critical evidence near the start or repeat them at the end.** Do not bury gold in the middle.

---

## SCENE 9 — TRANSFORMER + ATTENTION (30,000 FEET) (20:30 – 22:30)

**On screen**: Sketchbook only. No equations.

**Spoken**:

> You do not need a PhD to use LLMs. You do need one picture of the architecture.
>
> Inside the room sits a **Transformer** — the neural network architecture from the 2017 paper *Attention Is All You Need*. Every major LLM — GPT, Claude, Gemini, Llama — is a Transformer at the core.
>
> **[Draw: tokens enter → stack of blocks → logits out]**
>
> What does a Transformer block do? Two jobs:
> 1. **Attention** — for each token, decide which other tokens in the slot matter right now.
> 2. **Feed-forward** — transform the representation.
>
> Attention example — no math:
>
> Sentence: "The cat sat on the mat because it was tired."
>
> When the model processes **"it"**, attention links **"it"** → **"cat"** (not "mat"). That is how pronouns work without a grammar rule hard-coded.
>
> **[Draw arrows from "it" to "cat"]**
>
> Positional encoding — separate idea, one line: the model also needs to know token *order*. "Dog bites man" ≠ "Man bites dog." Position is encoded as numbers alongside meaning.
>
> I am deliberately not covering multi-head attention, layer norms, KV-cache — those are implementation details. If you build agents, you need the **attention = relevance wiring** picture. That is enough.

**[Bridge: "Architecture processes tokens. Sampling chooses the next token. Let us turn the knobs."]**

---

## SCENE 10 — THE AHA: TEMPERATURE, TOP-P, TOP-K (22:30 – 25:30)

**On screen**: Mac — side-by-side runs. `sampling_demo.py`.

**Spoken**:

> Open loop payoff. Same prompt, different answer — here are the knobs.
>
> **Temperature** — how sharp or flat the probability distribution is before sampling.
> - `temperature = 0` → almost always pick the highest-probability token. Repeatable. Good for extraction, JSON, tests.
> - `temperature = 0.9` → flatter distribution. More creative. More variation. Good for brainstorming. Bad for compliance text.
>
> **top_p** (nucleus sampling) — only sample from the smallest set of tokens whose cumulative probability reaches p. Cuts off the long tail of weird tokens.
>
> **top_k** — only consider the top k tokens. Older technique. Many teams use top_p instead.
>
> **[Run side by side — same prompt, temp 0 vs 0.9 — show near-identical vs varied outputs.]**
>
> ```python
> for temp in [0.0, 0.9]:
>     r = client.chat.completions.create(
>         model="gpt-4o-mini",
>         messages=[{"role": "user", "content": "Give me 5 startup ideas for AI in India."}],
>         temperature=temp,
>     )
>     print(f"temperature={temp}:", r.choices[0].message.content[:200], "...")
> ```
>
> See? Same room. Different randomness budget.
>
> Production defaults I see:
> - Structured output / agents that must be repeatable → `temperature=0` or `0.1`, plus `seed` where the API supports it.
> - Creative writing → higher temperature, but never ship without evals.
>
> **`seed` note**: `temperature=0` is *more* deterministic, not perfectly deterministic. Kernel scheduling and batching can still introduce tiny drift. For tests, use `seed` when available — and still treat outputs as probabilistic.

---

## SCENE 11 — MAP EVERY WEIRD BEHAVIOR + COMMON MISTAKES (25:30 – 27:30)

**On screen**: Sketchbook — two-column table.

**Spoken**:

> Let us connect every strange behavior to the room.

| Behavior | Room explanation |
|---|---|
| Hallucination | Low-probability token chain that *sounds* right — generation, not retrieval |
| Knowledge cutoff | Snapshot ended — never read events after training date |
| Different answer each run | Sampling — temperature / top_p |
| Ignores middle of long prompt | Lost in the middle + silent truncation |
| Refusals | RLHF training — taught to reject certain patterns (from last video) |
| "Sorry, I cannot help" tone | Different RLHF teams — Claude vs GPT vs Gemini |
| Slow on long prompts | More tokens → more attention compute at inference |

**Common mistakes (show at least one live)**:

| # | Mistake | Fix |
|---|---|---|
| 1 | "temperature=0 means deterministic forever" | Use `seed`; still evaluate probabilistically |
| 2 | "128k context = paste everything" | Chunk + RAG; repeat critical facts at start/end |
| 3 | "Model knows current news" | Tools or RAG with fresh data |
| 4 | "Retry until it works" without diagnosis | Ask: cutoff? truncation? sampling? missing RAG? |

**Terminal mistake demo**:

> **[Run same code twice at temperature=0 without seed — show tiny difference. Then add seed — show match.]**

---

## SCENE 12 — WHERE THIS FITS IN THE ROADMAP (27:30 – 28:30)

**On screen**: Browser — https://ch-balaji.github.io/ai-engineer-roadmap/

**Spoken**:

> Phase 2 — Mental Model of an LLM.
>
> **[Scroll roadmap]**
>
> Today: 2.1 + 2.2 — what the LLM is, how it thinks inside the room.
>
> Next video — 2.3: reasoning models vs base models. When to pay for `o3` / Claude thinking / DeepSeek R1 thinking tokens — and when a cheap model plus a good prompt wins.
>
> Then 2.4–2.5 — benchmarks and picking your daily driver model.
>
> After Phase 2 → Phase 3 prompt engineering. You will finally understand *why* system prompts, few-shot examples, and structured outputs work — because you know what the room can and cannot do.
>
> Roadmap is free. Link in the description. Pin it.

---

## SCENE 13 — RECAP + CLIFFHANGER (28:30 – 30:00)

**On screen**: Sketchbook cheat sheet → face cam.

**Spoken**:

> One page. Screenshot this.

```
THE WINDOWLESS ROOM — CHEAT SHEET
1. LLM = brain in a room. Slot in door = API. No windows = no live world.
2. GENERATE next token — do not RETRIEVE facts.
3. Knowledge CUTOFF = last training day. Not "dumb" — snapshot.
4. TOKENS not words. Slot size = context window. Bills in tokens.
5. LONG context ≠ reliable middle. Lost in the middle. Put gold at start/end.
6. ATTENTION = which tokens matter to which tokens.
7. temperature + top_p = randomness budget. logprobs = proof.
8. Hallucination / variation / cutoff / refusal → all map to room rules.
```

> You now have the mental model.
>
> But the market in 2026 split the room into two types of brains — **base models** and **reasoning models**. Same API. Different price. Different latency. Different "thinking tokens" on your bill.
>
> When should you pay 5× for a reasoning model? When is `gpt-4o-mini` at temperature 0 enough?
>
> That is the next video. Wednesday. Reasoning models vs base models.
>
> If this clicked — share it with someone who still thinks AI is magic. It is not. It is a room with rules.
>
> See you in the next one.

---

## YouTube Description (draft — run skill 10 after final cut)

```
How an LLM actually thinks — the senior engineer mental model behind every ChatGPT behavior.

In this video:
• The brain-in-a-windowless-room analogy (what an LLM really is)
• Why LLMs generate instead of retrieve — with logprobs demo
• Knowledge cutoff explained without hand-waving
• Tokens, context windows, and silent truncation
• Lost in the middle — why long prompts fail
• Transformer + attention in 2 minutes (no math)
• temperature, top_p, and when to use each
• Map hallucinations, refusals, and random outputs to one framework

🗺️ Roadmap: Phase 2 — Mental Model of an LLM (sections 2.1, 2.2)
Previous: How ChatGPT Is Trained
Next: Reasoning Models vs Base Models (2026)
Full Roadmap: https://ch-balaji.github.io/ai-engineer-roadmap/

📂 Code (companion repo — create before record):
`roadmap-2026-v010-llm-mental-model` — repro_same_prompt.py, sampling_demo.py, logprobs_demo.py

#LLM #AIEngineer #GenerativeAI
```

---

## Companion Code Files (create before record)

### `repro_same_prompt.py`
Two runs, same params, print both completions.

### `logprobs_demo.py`
Single-turn with `logprobs=True`, `top_logprobs=3`, print token probabilities.

### `sampling_demo.py`
Loop `temperature` in `[0.0, 0.9]` — same user message.

### `requirements.txt`
```
openai>=1.40.0
tiktoken>=0.7.0
python-dotenv>=1.0.0
```

---

## Technical Terms Introduced

| Term | Analogy first | When named |
|---|---|---|
| Windowless room | Person with only a door slot | Hook |
| Probabilistic generation | Predict next token, not lookup | Scene 3 |
| Knowledge cutoff | Last day of reading | Scene 3 / 6 |
| Context window | Size of door slot | Scene 7 |
| Lost in the middle | U-shaped attention | Scene 8 |
| Attention | "it" looks at "cat" | Scene 9 |
| Transformer | Stack of blocks in the room | Scene 9 |
| temperature / top_p | Randomness knobs | Scene 10 |
| logprobs | Show the probability list | Scene 5 |

---

## Retention Techniques Used

| Timestamp | Technique | Purpose |
|---|---|---|
| 0:00 | Live drawing hook | Visual + curiosity |
| 0:28 | "Rules of the room" gap | Stay for framework |
| 2:00 | Series callback (3 prior videos) | Reward loyal viewers |
| 5:30 | Live API demo — different outputs | Proof before theory |
| 5:30 | Open loop → Scene 10 | Delay knob reveal |
| 8:30 | logprobs terminal output | "No black box" payoff |
| 14:00 | Callback + skip depth on tokens | Respect prior video |
| 16:30 | Infosys story bridge | Emotional stickiness |
| 18:30 | Lost in the middle | Phase 4 foreshadow |
| 22:30 | Side-by-side temperature | Aha moment |
| 25:30 | Behavior mapping table | Everything clicks |
| 28:30 | Cheat sheet | Shareable + rewatch |
| 29:00 | Reasoning models cliffhanger | Next video pull |

---

## Skill Compliance Audit

| Skill | Compliance |
|---|---|
| 01 voice | No "guys". Direct "you". English terms preserved. One "no black box" at logprobs beat. |
| 02 story-bank | STORY_INFOSYS_MAINFRAMES Framing C mid-video — not opener. |
| 04 roadmap-source | Phase 2 / 2.1, 2.2. Prerequisites = API, Tokens, How Trained. Cliffhanger → 2.3. |
| 06 title+thumbnail | T10 brief locked above. |
| 07 hook-factory | 5 hooks; recommended A (windowless room). |
| 09 monetization | Phase 1 — one 15-sec description hint only. |
| Anti-patterns | No welcome throat-clear. No toy-only — production mistakes included. |

---

## Pre-Record Checklist

- [ ] Hook ≤30s — room drawn live
- [ ] `repro_same_prompt.py`, `logprobs_demo.py`, `sampling_demo.py` tested with real API key
- [ ] tiktokenizer or `tiktoken` REPL bookmarked
- [ ] Roadmap site loads on screen recording
- [ ] Thumbnail brief sent to designer / ChatGPT image prompt run
- [ ] End screen: next video + Phase 2 playlist
- [ ] Log story usage in `skills/02-story-bank/STORIES.md` after publish

---

*Draft v1 — record, tighten in edit, run `10-description-generator` on final SRT for upload package.*
