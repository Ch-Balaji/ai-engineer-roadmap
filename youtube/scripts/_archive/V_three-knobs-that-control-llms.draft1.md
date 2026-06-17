# Same Prompt, Different Answer — 3 Hidden Knobs That Control Every LLM

**Full scene-by-scene script — TIGHT 12–14 MIN VERSION** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway).

> **Why this video exists:** *How ChatGPT Is Trained* already covered tokens, embeddings, transformer, attention, knowledge cutoff, hallucinations, and behavior mapping. This video is **NOT a recap**. It is the **control surface**: the knobs you set every time you call the API. Demo-first. Tight. Actionable.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V010 |
| Slug | `three-knobs-that-control-llms` |
| Old slug (replaced) | `brain-in-windowless-room` (too broad, overlapped trained video) |
| Playlist | Phase 2 — LLM Mental Model |
| Target length | 12–14 min (hard cap 15) |
| Slot | Mon 7 PM IST |
| Previous video | How ChatGPT Is Trained |
| Next video | Reasoning Models vs Base Models — When Each Wins in 2026 (Wed) |

## Roadmap Mapping

```
- Phase: 2 — Mental Model of an LLM
- Section covered: 2.2 (How an LLM thinks) — sampling parameters subset
- Prerequisites: API access, Tokens, How ChatGPT Is Trained
- Capstone contribution: no
- End state: viewer can set temperature / top_p / seed correctly per use case;
             can read logprobs to debug; knows the lost-in-the-middle rule
```

## Promise vs Trained-Video — what is NEW today

| Already taught (training video) | NEW in this video |
|---|---|
| Probabilistic generation (concept) | The **knobs** that control the probability — temperature, top_p, top_k |
| Tokens, embeddings, attention | `logprobs=True` — see the actual probability list |
| Knowledge cutoff, hallucinations | `seed` parameter and the determinism trap |
| Behavior table | Lost-in-the-middle U-curve (production rule) |
| Inference token-by-token | Production defaults cheat sheet you can copy today |

**Re-teach budget: 30 seconds total.** Everything else is new.

---

## Playlist Callback Map (kept tight — 5 references, ~30 sec total)

| # | Time | Type | Target video | Why |
|---|---|---|---|---|
| 1 | 0:30 | Backward bridge | *How ChatGPT Is Trained* | Sets context, names the playlist |
| 2 | 4:10 | Lean-in | *Tokens in LLM* | Justifies why this video is short |
| 3 | 8:30 | Forward reference | Phase 4 — RAG | Anticipation for upcoming phase |
| 4 | 11:00 | Sibling reference | All Phase 2 videos | Binge-watch nudge |
| 5 | 11:45 | Cliffhanger | V011 — *Reasoning Models vs Base Models* | Next-video pull |

**Visual rule:** Each backward callback gets a 3-second lower-third sticker (CapCut) showing the prior video's thumbnail. No verbal interruption.

## Visual / Production Plan

| Time | Segment | Medium |
|---|---|---|
| 0:00–0:30 | Hook — same prompt, different output (live) | Mac terminal full-screen |
| 0:30–1:00 | 30-sec callback (no rehash) | Sketchbook — one box |
| 1:00–4:00 | Knob 1 — temperature | Mac — side by side runs |
| 4:00–6:00 | logprobs peek — see the probabilities | Mac — terminal scroll |
| 6:00–8:00 | Knob 2 — top_p (and top_k briefly) | Mac + sketchbook overlay |
| 8:00–10:00 | Knob 3 — context shape (lost in the middle) | Sketchbook U-curve |
| 10:00–11:30 | Production defaults cheat sheet | Sketchbook full-screen |
| 11:30–12:30 | Cliffhanger → reasoning models | Face cam |

---

## Title + Thumbnail Brief (skill 06)

```
- Title formula: T1 (What Nobody Tells) blended with T9 (X Things)
- Final title: Same Prompt, Different Answer — Why? (3 Knobs)
- Char count: 50
- Alt A/B titles:
    1. 3 Hidden Knobs That Control ChatGPT (Live Demo)
    2. temperature, top_p, seed — When to Use Which
    3. Stop Calling LLMs Random — Here Is the Actual Math
- Subject pose: Confident, slight smirk, finger pointing at split-screen
- Outfit: Brown bomber jacket + black zip-up (locked)
- Background: Black + circuit overlay + warm rim light upper-right
- Primary text (white, Anton ALL CAPS):
    SAME PROMPT
    DIFFERENT ANSWER
- Highlight text (yellow + brush band):
    WHY?
- Telugu badge (red, bottom-right):
    "ఇది అందరికీ తెలియదు"
- Social-proof badge (top-left, if true):
    "110K+ ROADMAP VIEWS"
- Tech-stack icons (bottom):
    OpenAI · Anthropic · Python · logprobs
```

---

## 5 HOOKS (skill 07)

### HOOK A — Live Demo First (RECOMMENDED)
> "Watch this. Same prompt. Same model. Same temperature. I run it twice. *[two visibly different outputs print]* If the brain is the same — why two different answers? After 12 minutes you will know exactly which knob controls this, and I will show you the actual probability list the model is sampling from. No black box."
> [Visual: Mac terminal full-screen, two API calls execute live, outputs appear side by side]

### HOOK B — Comment Callback
> "After the training video, the most repeated comment was: 'Balaji, I set temperature to zero. The output is still different. Why?' Today — the answer. With code. With proof."
> [Visual: Screenshot of YouTube comment → terminal demo]

### HOOK C — Mistake Reveal
> "If you are setting `temperature=0` and expecting deterministic output, you have a bug in production right now. You just have not noticed. Today I show you why and the one parameter that fixes it."
> [Visual: Sketchbook — write `temperature=0 ≠ deterministic` and circle it]

### HOOK D — Money Hook
> "There are three knobs on every LLM call. Most engineers touch one — temperature. Get the other two right, and you can cut hallucinations in half on the same model."
> [Visual: Sketchbook — three dial icons drawn live]

### HOOK E — Senior Engineer Frame
> "In every interview I take for a senior AI engineer role, I ask one question: 'temperature is 0.7 and top_p is 0.9 — which one decides what gets sampled?' Most candidates fail. Twelve minutes from now, you will not."
> [Visual: Face cam direct address → sketchbook with two knobs]

**Recommended:** HOOK A — demo-first matches your channel pattern, creates an immediate gap ("why two answers?"), and the payoff is the entire video. Strongest CTR + retention combo.

---

## SCENE 1 — HOOK (0:00 – 0:30)

**On screen:** Mac terminal full-screen. Pre-loaded `repro_same_prompt.py`. Run it live.

**Spoken:**

> Watch this.
>
> **[Run script — two outputs print]**
>
> Same prompt. Same model — `gpt-4o-mini`. Same temperature — `0.7`. I ran it twice.
>
> Two different answers. Different wording. Slightly different facts.
>
> If the brain is the same — why two different answers?
>
> By the end of this video, you will know exactly which knob to turn — and I will show you the **actual probability list** the model is sampling from. Not magic. No black box.

**[0:28 — gap planted: "which knob? show me the probabilities."]**

---

## SCENE 2 — 30-SECOND BRIDGE (0:30 – 1:00) — playlist callback

**On screen:** Sketchbook — three small boxes drawn left to right: `API → Tokens → Trained → [TODAY]`. Lower-third overlay (3 sec) showing the *How ChatGPT Is Trained* thumbnail.

**Spoken:**

> Quick context. This video sits inside Phase 2 of the AI Engineer Roadmap — the mental model series.
>
> Last video — *How ChatGPT Is Trained* — we covered the four stages, why hallucinations happen, why every model has its own personality. If you skipped it, pause this, watch that, come back. Link in description and end card.
>
> Today is different. Today is the **control surface**. Three knobs you set every time you call the API. Twelve minutes. Mostly demos.

**[Bridge ends fast — no re-teaching. Straight into Knob 1.]**

> **Playlist tactic (skill notes):**
> - Verbal callback names the prior video by title — earns trust, kills the ambiguity of "go watch my other video".
> - Visual lower-third (CapCut sticker) shows the actual thumbnail for 3 seconds. Boosts CTR to that video.
> - Phrase "pause this, watch that, come back" — directly tells the loyal viewer it's safe to leave; YouTube counts the round trip as session watch time.

---

## SCENE 3 — KNOB 1: TEMPERATURE (1:00 – 4:00)

**On screen:** Mac — `sampling_demo.py`. Two terminal panes side by side.

**Spoken:**

> Knob one — `temperature`.
>
> One sentence: temperature controls how spiky or flat the probability distribution is at every token step.
>
> Translation — at every step, the model has a list of likely next tokens with probabilities. `temperature=0` says: pick the top one almost always. `temperature=0.9` says: flatten the list, give the lower-ranked tokens a real chance.
>
> Watch.
>
> ```python
> from openai import OpenAI
> client = OpenAI()
>
> for temp in [0.0, 0.9]:
>     r = client.chat.completions.create(
>         model="gpt-4o-mini",
>         messages=[{"role": "user", "content": "Give me 5 startup ideas for AI in India."}],
>         temperature=temp,
>     )
>     print(f"--- temperature={temp} ---")
>     print(r.choices[0].message.content[:300])
> ```
>
> **[Run.]**
>
> `temperature=0` — same five ideas every time. Boring. Repeatable. Good.
>
> `temperature=0.9` — different ideas every run. Creative. Useful for brainstorming. Bad for compliance text.
>
> **Production rule:**
>
> | Use case | temperature |
> |---|---|
> | Extraction, JSON output, agents | `0` or `0.1` |
> | Summarization | `0.2`–`0.4` |
> | Brainstorming, creative writing | `0.7`–`1.0` |
>
> One knob, one decision. Most engineers stop here. They should not. Knob two changes the game.

---

## SCENE 4 — LOGPROBS PEEK (4:00 – 6:00) — lean-in callback to Tokens video

**On screen:** Mac terminal — `logprobs_demo.py`. Brief lower-third sticker on the Tokens video thumbnail at minute 4:10.

**Spoken:**

> Quick proof — the model genuinely has a probability list. We do not have to trust me. We can ask the API to show its work.
>
> One reminder from the **Tokens** video — the model does not see "Paris", it sees a token ID. So when I say it ranks the top tokens by probability, you already know what a token is. That is why this video is twelve minutes and not thirty.
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
> **[Run — terminal shows token + alternatives + log-probabilities]**
>
> Look at the first token. ` Paris` — top choice. ` Lyon` somewhere in the alternatives. ` the` somewhere else.
>
> That is what the model sees at every step. A ranked list. It picks one. Then it does it again for the next token. Thousands of times for one ChatGPT response.
>
> **temperature** changes how steep that ranking looks. **top_p** changes how many of those candidates the model is allowed to pick from. That is knob two.

---

## SCENE 5 — KNOB 2: TOP_P (6:00 – 8:00)

**On screen:** Sketchbook — draw a probability bar chart, then a cutoff line.

**Spoken:**

> Knob two — `top_p`. Also called nucleus sampling.
>
> **[Sketch: bars from highest to lowest probability]**
>
> top_p says: only sample from the smallest set of tokens whose probabilities **add up to p**. Cut off the long tail of weird tokens.
>
> Example. `top_p=0.9` — keep the top tokens until their combined probability hits 90 percent. Drop the rest. Sample from the survivors.
>
> Why does this matter when you already have temperature? Because temperature alone, set high, can pick a bizarre token from the tail. top_p protects you from that.
>
> Production combo I see most often:
>
> ```python
> temperature=0.7, top_p=0.9
> ```
>
> Mid-randomness. No weird tail. Good for general chat, RAG answers, content generation.
>
> **`top_k` — one line:** older parameter, only consider top k tokens. Most teams use top_p instead. Anthropic exposes both. OpenAI exposes top_p only. Know the name. Move on.
>
> **The seed trap.** Engineers set `temperature=0` and assume deterministic output. It is *more* deterministic — not perfectly. Kernel scheduling, batching, GPU non-determinism — drift creeps in.
>
> ```python
> temperature=0, seed=42
> ```
>
> `seed` improves repeatability. For tests, set both. Then still treat outputs as probabilistic and write evals.

---

## SCENE 6 — KNOB 3: CONTEXT SHAPE / LOST IN THE MIDDLE (8:00 – 10:00)

**On screen:** Sketchbook — draw the U-curve attention chart.

**Spoken:**

> Knob three — and this one is not a parameter. It is a layout decision. **Context shape.**
>
> A paper called *Lost in the Middle* — engineers should know the name.
>
> **[Draw attention curve: HIGH at start, LOW middle, HIGH at end — U-shape]**
>
> When your prompt is long, the model pays more attention to the **start** and the **end**. Things buried in the middle get under-weighted.
>
> You retrieved the right chunk in your RAG pipeline. You placed it in the middle of a forty-page prompt. The model ignored it. Looks like RAG is broken. Often it is context shape that is broken.
>
> **Production rule — say it out loud:**
>
> > Put critical instructions and critical evidence near the **start** or repeat them near the **end**. Do not bury gold in the middle.
>
> One more thing about the slot. `gpt-4o` advertises 128k tokens. That is the size — not the quality. Everything competes for the same slot: your system prompt, retrieved chunks, chat history, the user question. Fill the slot, something gets truncated. Often **silently**. No error. The middle pages just never made it.
>
> **Forward reference (Phase 4 hook):** This U-curve is exactly why naive RAG fails in production. We will fight it head-on in Phase 4 — chunking, reranking, hybrid retrieval. For now, just remember the rule: gold at the edges, never the middle.
>
> **CTA hint (skill 09 — Phase 1, single line, ≤15 sec):**
>
> > If you want structured help on resume or mock interviews, the form is in the description. Back to the cheat sheet.

---

## SCENE 7 — PRODUCTION DEFAULTS CHEAT SHEET (10:00 – 11:30)

**On screen:** Sketchbook full-screen — clean cheat sheet drawn live.

**Spoken:**

> One page. Screenshot this. This is your default config for every common use case.

```
THREE KNOBS — PRODUCTION DEFAULTS

Use case                           temperature   top_p   seed   notes
-----------------------------------------------------------------------
Extraction / JSON / agents          0.0–0.1      1.0     yes    repeatable
Summarization                       0.2–0.4      0.9     yes    safe
RAG answers                         0.0–0.3      0.9     yes    grounded
General chat                        0.5–0.7      0.9     no     balanced
Brainstorming / creative            0.7–1.0      0.95    no     varied
Code generation                     0.0–0.2      1.0     yes    deterministic-ish

CONTEXT-SHAPE RULES
- Put critical instructions at the START
- Repeat the question or constraint at the END
- Do NOT bury retrieved evidence in the MIDDLE
- Long context ≠ reliable context — chunk and prioritize
```

> Three knobs. One layout rule. That is the whole control surface for every LLM call you make this week.
>
> **Sibling reference (binge-watch nudge):** Hallucinations and refusals — those are training-stage problems, covered in *How ChatGPT Is Trained*. Sampling and shape — what we just covered. Reasoning vs base models — Wednesday. Three videos, one playlist, one mental model. Click the playlist link.

---

## SCENE 8 — RECAP + CLIFFHANGER (11:30 – 12:30)

**On screen:** Face cam, direct address.

**Spoken:**

> Quick recap.
>
> Knob one — `temperature`. How spiky the probability distribution is.
> Knob two — `top_p`. How many candidates are allowed in the pool. Plus `seed` for repeatability.
> Knob three — context shape. Where you put information matters as much as what you put.
>
> Now — the next twist for 2026. Until last year, every model worked like this. One forward pass. Predict tokens. Done.
>
> Then a new family arrived — **reasoning models**. `o3`, Claude with extended thinking, Gemini thinking, DeepSeek R1. Same API. But your bill suddenly has a new line called **thinking tokens**. They cost more. They can be 10× slower. Sometimes they are dramatically better. Sometimes they are wasted money on a task `gpt-4o-mini` would solve at temperature zero.
>
> Wednesday — that video. Reasoning Models vs Base Models. When to pay 5× and when not to.
>
> If this clicked — share it with one person who keeps saying "the LLM is random." It is not. It is three knobs.
>
> See you in the next one.

---

## YouTube Description (draft — final pass after edit)

```
Same prompt. Same model. Different answer. This is the video that explains why — and how to control it.

In this video:
• Knob 1 — temperature, with a live side-by-side demo
• logprobs=True — see the actual probability list ChatGPT is sampling from
• Knob 2 — top_p (and the seed trap most engineers fall into)
• Knob 3 — context shape and the Lost in the Middle rule
• Production defaults cheat sheet you can copy today

🗺️ Roadmap: Phase 2 — Mental Model of an LLM (section 2.2 sampling)
Previous: How ChatGPT Is Trained
Next: Reasoning Models vs Base Models (Wednesday)
Full Roadmap: https://ch-balaji.github.io/ai-engineer-roadmap/

📂 Code:
Repo: roadmap-2026-v010-three-knobs
- repro_same_prompt.py
- sampling_demo.py
- logprobs_demo.py

#LLM #AIEngineer #GenerativeAI
```

---

## Companion Code Files (create before record)

### `repro_same_prompt.py`
```python
from openai import OpenAI
client = OpenAI()
prompt = "Explain RAG in exactly 3 bullet points."
for i in range(2):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    print(f"--- Run {i+1} ---")
    print(r.choices[0].message.content)
```

### `sampling_demo.py`
```python
from openai import OpenAI
client = OpenAI()
for temp in [0.0, 0.9]:
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Give me 5 startup ideas for AI in India."}],
        temperature=temp,
    )
    print(f"--- temperature={temp} ---")
    print(r.choices[0].message.content[:300])
```

### `logprobs_demo.py`
```python
from openai import OpenAI
client = OpenAI()
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "The capital of France is"}],
    max_tokens=5,
    logprobs=True,
    top_logprobs=3,
)
for t in r.choices[0].logprobs.content:
    print(t.token, t.top_logprobs)
```

### `requirements.txt`
```
openai>=1.40.0
python-dotenv>=1.0.0
```

---

## Retention Map

| Time | Beat | Why it works |
|---|---|---|
| 0:00 | Live demo split outputs | Stops the scroll, immediate gap |
| 0:28 | "which knob?" promise | Open loop — resolved at 1:00 |
| 1:00 | First payoff (temperature) | Fast — keeps loyal viewers |
| 4:00 | logprobs terminal scroll | "no black box" demo moment |
| 6:00 | top_p sketch + seed trap | Mistake reveal = stickiness |
| 8:00 | Lost in the middle U-curve | Phase 4 foreshadow |
| 10:00 | Cheat sheet | Screenshot moment + share |
| 11:30 | Reasoning models cliffhanger | Next-video pull |

---

## Skill Compliance Audit

| Skill | Compliance |
|---|---|
| 01 voice | No "guys". Direct "you". English terms preserved. One "no black box" at logprobs scene. Short declarative sentences. |
| 02 story-bank | No story used (12-min cap respects pacing — story budget transferred to next video) |
| 04 roadmap-source | Phase 2 / 2.2 sampling subset. Prerequisites cited. Cliffhanger to 2.3 reasoning models. |
| 06 title+thumbnail | T1+T9 blended brief locked above. Thumbnail highlight word `WHY?`. |
| 07 hook-factory | 5 hooks generated; HOOK A (live demo first) recommended. |
| 09 monetization | Phase 1 — single 15-sec description hint, no pitch. |
| Anti-patterns | No welcome / throat-clear, no rehash of training video, no toy-only example, real production defaults table. |

---

## CapCut Edit Cues — Playlist Callbacks

| Time | Cue | Asset |
|---|---|---|
| 0:32 | Lower-third (3 sec) | Thumbnail of *How ChatGPT Is Trained* + small "▶ Watch first" tag |
| 4:10 | Lower-third (3 sec) | Thumbnail of *Tokens in LLM* + "Prereq" tag |
| 8:35 | Floating sticker (4 sec) | Text "Phase 4 — RAG → coming in Week 8" with arrow icon |
| 11:00 | Playlist card (5 sec) | Phase 2 playlist link + sticker "All in one playlist →" |
| 11:50 | End-screen template | Next video (V011) on left, Phase 2 playlist on right |
| Throughout | Pinned comment | Auto-pin: "Roadmap playlist: {link} · Previous video: {link} · Next: {link}" |

## Pre-Record Checklist

- [ ] Hook ≤30s — terminal split clearly visible
- [ ] `repro_same_prompt.py`, `sampling_demo.py`, `logprobs_demo.py` tested with real API key
- [ ] `OPENAI_API_KEY` exported in recording shell
- [ ] Terminal font 16pt+, dark theme, no personal data in shell history
- [ ] Sketchbook ready with U-curve template lightly pencilled
- [ ] Cheat sheet drafted on a separate sketchbook page (record drawing it live)
- [ ] Thumbnail brief sent to designer / ChatGPT image prompt run
- [ ] End screen: V011 Reasoning Models + Phase 2 playlist
- [ ] Final length ≤15:00 — if longer, cut the seed paragraph or trim cheat sheet narration

---

## What this video INTENTIONALLY does not cover (saved for other videos)

| Topic | Where it lives |
|---|---|
| 4 stages of training | Already in *How ChatGPT Is Trained* |
| Tokens, embeddings depth | Already in *Tokens in LLM* + training video |
| Transformer / attention math | Will be its own video later in Phase 2 |
| Knowledge cutoff | Already in training video |
| Hallucination explanation | Already in training video |
| Reasoning models | V011 — Wednesday |
| Benchmarks (MMLU, GSM8K, etc.) | Phase 2 section 2.4 |
| Picking your daily driver model | Phase 2 section 2.5 |
| Prompt engineering techniques | Phase 3 |
| RAG / context engineering deep dive | Phase 4 + Phase 7 |

---

*Tight v1 — record, edit aggressively to stay under 14 min, run `10-description-generator` skill on final SRT for upload package.*
