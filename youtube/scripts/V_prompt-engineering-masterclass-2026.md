# Prompt Engineering Masterclass — 5 Upgrades, 25 Minutes, One Real Prompt

**Full scene-by-scene script** — applies skills 01 (voice), 06 (title+thumbnail), 07 (hook-factory), 10 (description). Standalone beginner-to-intermediate masterclass. **One unified running example throughout** — a cold email to HR at OpenAI for the Senior AI Engineer role. The hook reveals the *destination* (the finished master prompt + a tight STAR-form email reply). Techniques 1–5 then **build that exact prompt block-by-block in front of the viewer** — Technique 1 adds ROLE+CONTEXT+REFERENCES+TASK+FORMAT+LENGTH, Technique 2 adds CONSTRAINTS, Technique 3 adds EXAMPLES, Technique 4 layers in decomposition, Technique 5 adds PROCESS (interview-style) + QUALITY CHECK. By 23:00 the prompt the viewer sees at 0:30 has been fully reconstructed in front of them. Bonus mini-demo inside Technique 3 (Balaji's own past video hooks as few-shot) is the only non-email moment — kept deliberately, to show the few-shot technique transferring to a second use case. **Why single-example:** promise-payoff loop closes cleanly, no cognitive switching cost, real WBD project = authentic credibility anchor.

> **Teaching style:** Hybrid crossover. Speak as a senior AI engineer ("I'm the one who writes 50+ prompts a day in production"), but the example and final master prompt are universal so any viewer benefits — student, fresher, IT pro, content creator.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V013 |
| Slug | `prompt-engineering-masterclass-2026` |
| Playlist | Phase 3 — Prompt Engineering |
| Target length | 24–25 min tight (hard cap 26) — extended from 22 min to accommodate the new "Why this matters: UI vs API" section |
| Slot | Mon 7 PM IST |
| Previous video | V012 — *Async AI Agent* |
| Next video | *Context Engineering — The Skill That Replaced Prompt Engineering* (tease at end) |

## Roadmap Mapping

```
- Phase: 3 — Prompt Engineering
- Sections covered: 3.1 (the 5-part skeleton + reference grounding),
                    3.2 (constraints), 3.3 (few-shot vs references),
                    3.4 (decomposition + chain-of-thought as tactical),
                    3.5 (interview-style prompting)
- Prerequisites: API basics, Tokens, How LLMs Are Built
- Capstone contribution: yes — the master prompt template is reused in Phase 5 (agents)
- End state: viewer can build any prompt from scratch using a 5-block skeleton,
            knows the difference between references and examples,
            and knows when to let AI interview them instead of guessing the context.
```

## Why this video (now)

| Reality (June 2026) | Script implication |
|---|---|
| Most YouTube "prompt engineering" content still over-focuses on "act as an expert" | Position as a script that drops the act-as nonsense and teaches structure |
| Reasoning models do CoT internally — "let's think step by step" is now redundant on o-series / Claude Thinking / GPT-5 reasoning | Technique 4 leads with **decomposition**, demotes CoT to a tactical line for non-reasoning models |
| Interview-style prompting is the most underused power move in 2026 — almost nobody on YouTube teaches it | Save it for Technique 5 (climactic reveal) — biggest "I'm sharing this video" moment |
| Most viewers in our audience send cold emails to recruiters/companies and get generic ChatGPT output that doesn't earn a reply | The entire script uses one unified example: a cold email to HR at OpenAI for the Senior AI Engineer role, using Balaji's real WBD RAG project as the showcase. The hook reveals the finished prompt; Techniques 1–5 build it block-by-block in front of the viewer. By the end, the viewer has watched the prompt from the hook get assembled from scratch. |
| Beginners constantly confuse "few-shot examples" with "reference material" | Dedicated mini-section in Technique 3 makes the distinction crystal clear |
| Three audience segments are watching (ChatGPT-only users, API devs, agent builders) and the 22-min cut only really served the middle one | New "Why this matters — UI vs API" beat (1:15–3:45) widens the tent: shows ChatGPT-only users that the UI is secretly assembling prompts for them, and shows API/agent builders why the stakes go up the moment that scaffolding disappears |

## Playlist Callback Map (4 references, ~30 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 0:50 | Backward bridge | V009 (How LLMs Are Built) | "LLMs predict next token — so context shapes the output" |
| 2 | 2:30 | Backward bridge | V011 (APIs Explained with a ChatGPT Project) | "Remember when we built that simple chatbot? That `messages` array — every line of it is YOUR prompt now" |
| 3 | 17:00 | Lean-in | V010 (How to Control ChatGPT) | Reasoning vs chat tier — when CoT helps and when it doesn't |
| 4 | 24:00 | Cliffhanger | V014 (Context Engineering — coming next) | "Remember when I said the UI hides all that scaffolding from you? Managing it yourself = context engineering" |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–0:45 | **Hook — bad prompt → master prompt reveal, live in ChatGPT** | Split screen: ChatGPT window + face cam; master prompt scrolls on screen |
| 0:45–1:15 | Promise + 5-upgrade preview (named list) | Face cam → animated list |
| 1:15–3:45 | **Why this matters — UI vs API, what's hiding in the backend** (NEW: chat-UI prompt assembly reveal → Python API code → cost & agent stakes → 5 upgrades apply to both) | Face cam → ChatGPT UI annotation → Python code on screen → diagram |
| 3:45–7:30 | **Technique 1 — The 5-Part Skeleton (incl. reference grounding)** | ChatGPT live + sketch overlay |
| 7:30–10:15 | **Technique 2 — Constraints & Negatives** | ChatGPT live + red-circle overlays |
| 10:15–15:00 | **Technique 3 — Few-Shot Examples** (add 'Hi Maya' email example to the prompt → bonus video-hook mini-demo → Few-shot vs References mini-section) | ChatGPT live + sketch |
| 15:00–18:00 | **Technique 4 — Decomposition (chain) first, CoT second as tactical** | ChatGPT live + flowchart |
| 18:00–21:30 | **Technique 5 — Interview-Style Prompting** (the climactic reveal) | ChatGPT live, multi-turn |
| 21:30–23:00 | Master prompt template (with PROCESS + QUALITY CHECK blocks) + API mapping callback | Sketchbook full-screen → face cam |
| 23:00–23:20 | Honest scope-setting — multimodal aside | Face cam, direct address |
| 23:20–24:30 | CTA (comment "PROMPT") + context-engineering tease (with one-line nod to V016 prompt injection) | Face cam → end screen |

---

## 5 HOOKS (skill 07 — pick one on record day)

### HOOK A — Live Demo First + Show the Final Prompt (RECOMMENDED)
> *"Watch this. I'm applying to OpenAI today. I ask ChatGPT to write the email to HR — the way most people would. [Type into ChatGPT: 'Write an email to HR at OpenAI about the Senior AI Engineer job opening. I want to apply.' Output is a 5-paragraph 'I hope this email finds you well... esteemed team... kind consideration' wall of text.] This is what most people send. No one at OpenAI is replying to this — they get a thousand a week. Now watch what happens when I paste THIS prompt instead. [Screen fills with the full master prompt — ROLE, CONTEXT with the actual job description as REFERENCES, TASK, FORMAT, LENGTH, CONSTRAINTS banning every cliché, one EXAMPLE of the style. Run it. Output is a 4-sentence email with a specific JD callback and one clear ask.] Same model. Same task. One is going to the trash. The other is getting a reply. In the next twenty-five minutes, I'll show you exactly how this prompt is built — five upgrades, one prompt, plus the two minutes you actually need to understand why this matters whether you use ChatGPT or build with the API."*
> [Visual: Split screen — ChatGPT on left, face cam on right. Bad output stays on screen 4–5 seconds (long enough for viewers to read the clichés). Master prompt scrolls on screen for ~6 seconds. Good output holds for 3 seconds. The visible structural diff — wall of text vs. tight 4-sentence email — is the retention payload.]

### HOOK B — Quality Contrast (opinion-framed)
> *"The same model can give you a useless answer or a great answer — depending on how much task, context, format, and examples you put into the prompt. Most people put one. In the next twenty-five minutes, I'll show you the five upgrades that take the same prompt from a two-out-of-ten to a nine-out-of-ten — on a real example you'll use tomorrow."*
> [Visual: Face cam → power-meter graphic 2/10 vs 9/10]

### HOOK C — Production Incident
> *"Last week our agent in production gave a customer the wrong answer. I checked the logs. The prompt was 200 words long, polite, with 'please' and 'thank you' — and it still failed. The fix was rewriting it as five blocks. Today I'll teach you those five upgrades, **step by step**, on a real example."*
> [Visual: Face cam → terminal showing the bad log → fix]

### HOOK D — Comment Callback
> *"After my last video, this comment came in: 'Bro, how do I actually write prompts that don't give generic answers?' Today is the answer. Five upgrades. One real example we build from scratch — a cold email to HR at OpenAI that actually earns a reply, using a real production AI project as the showcase. Twenty-five minutes. By the end you'll have a prompt template you can use for the rest of your career."*
> [Visual: Screenshot of the comment → face cam]

### HOOK E — Personal Story
> *"Three years ago I was the guy typing 'act as an expert' before every ChatGPT question. The outputs were mediocre and I blamed the model. Today I write 50 to 100 prompts a day in production and the outputs are predictable. The difference isn't the model. It's five upgrades nobody taught me. I'm teaching them to you now, in twenty-five minutes."*
> [Visual: Face cam, direct address]

**Recommended:** HOOK A — Live Demo First. Highest cliffhanger value, immediately fulfills the title/thumbnail promise (BAD PROMPT → PRO PROMPT), and the visible quality jump — a 5-paragraph cliché email vs. a 4-sentence specific email — is binary and instantly readable. The cold-email-to-OpenAI angle gives the hook universal emotional stakes (every viewer has either sent or received this email), and the bad output is a phrase-for-phrase reproduction of what every junior writes, so viewers will recognize themselves in it. This is the strongest retention move available for this topic.

---

## TITLE + THUMBNAIL (skill 06)

### Title options (ranked by CTR bet)
1. **Learn 80% of Prompt Engineering in 25 Minutes** *(primary — Pareto-framed promise, specific time commitment, no clickbait; matches the "five upgrades cover 80%" claim of the script)*
2. **I Fixed One Bad ChatGPT Prompt 5 Times — Now It Sounds Professional** *(backup: concrete action verb + curiosity gap; "ChatGPT" is more searchable than "prompt")*
3. **Stop Writing Bad Prompts — 5 Upgrades I Use Every Day As An AI Engineer**
4. **Prompt Engineering Masterclass — 5 Upgrades, 25 Minutes, One Real Prompt**

### Thumbnail
- **Left side:** Face slightly confused, looking at a phone showing the bad cold email — `Subject: Application for Senior AI Engineer Position. Dear Hiring Manager, I hope this email finds you well...` (the body just trails off into ".....") with a red strike-through or trash-can icon
- **Right side:** Face confident, holding a phone showing the new sharp email — `Subject: Long-horizon agents → 25M-chunk RAG at WBD → OpenAI Senior AI role. Hi Archana — Saw the post...` with a green "REPLY" badge or notification
- **Big text overlay (English, large):** **BAD EMAIL → REPLY-WORTHY**
- **Telugu subtitle text (smaller, below the English):** **ప్రాంప్ట్ ఇంజినీరింగ్ మాస్టర్‌క్లాస్** *(transliteration of "Prompt Engineering Masterclass" — signals the video is for the Telugu-speaking AI audience while keeping the English hook for broader CTR. If a more native phrasing is preferred, swap for: ప్రాంప్ట్ ఇంజినీరింగ్ — పూర్తి శిక్షణ)*
- **Top-right badge:** **5 UPGRADES · 25 MIN**
- **Tone:** Photo-real face shots (not cartoon), high contrast between the "before" and "after" sides, phone screens are legible at 320×180 thumbnail size (i.e., only the subject line + first 1 line of body actually need to be readable on each side — the rest is visual texture).

---

# FULL SCRIPT

Visual notation:
- **[VISUAL: ...]** — what's on screen
- **[CLIFFHANGER]** — the line that forces the viewer into the next section
- **[B-ROLL: ...]** — supplementary footage

---

## 0:00 – 0:45 · HOOK (Live Demo First + Show The Final Prompt)

**[VISUAL: Split screen. Left: ChatGPT window. Right: face cam.]**

> *Watch this. I'm applying to OpenAI today. I need to email their HR. So I ask ChatGPT for help — the way most people would.*

**[VISUAL: Type into ChatGPT: `Write an email to HR at OpenAI about the Senior AI Engineer job opening. I want to apply.` Output appears — keep it on screen for 4–5 seconds so viewers can actually read it.]**

```
Subject: Application for Senior AI Engineer Position

Dear Hiring Manager,

I hope this email finds you well. My name is [Your Name], and I am
writing to express my keen interest in the Senior AI Engineer
position at OpenAI as advertised on your careers page.

With over 5 years of experience in the field of artificial
intelligence and a strong background in machine learning, I am
confident that I would be a valuable addition to your esteemed team.
I have a proven track record of delivering innovative solutions...

[continues for 3 more paragraphs of generic qualifications]

Please find my resume attached for your kind consideration. I would
welcome the opportunity to discuss how my skills and experience
align with your needs.

Thank you for your time and consideration. I look forward to
hearing from you soon.

Best regards,
[Your Name]
```

> *This is what most people send. Five paragraphs. "I hope this email finds you well." "Esteemed team." "Kind consideration." It reads like a 2010 cover letter. No one at OpenAI is replying to this. They get a thousand a week.*

> *Now watch what happens when I paste THIS prompt instead.*

**[VISUAL: Clear the ChatGPT window. The full master prompt fills the screen — slowly scrolls from top to bottom over ~6 seconds. Viewer doesn't need to read every word — they need to see it has structure, blocks, examples.]**

```
ROLE: You are an AI engineer with 5 years of production experience,
writing a cold email to a recruiter — confident, specific, not desperate.

CONTEXT:
Audience — a senior recruiter at OpenAI who reads 200+ emails per day
My background — built async multi-agent systems in production and
                scaled them to millions of monthly users
Goal — get a 15-minute screening call, not a generic "thanks we'll review"
Stakes — this email is one of hundreds in their inbox today

REFERENCES:

The job post I'm applying for:
"""
Senior AI Engineer — OpenAI
We're looking for engineers who have shipped agentic AI systems
to production. You'll work on long-horizon agents, tool use, and
reliability at scale. Strong Python + experience with LLM APIs
required. Bonus: experience with async, retrieval, or evals.
"""

My flagship project (the one to showcase in this email):
"""
Built a production-grade RAG-based Content Intelligence Platform
for Warner Bros. Discovery, indexing 25M+ chunks from scripts,
subtitles, PDFs, and metadata across 40K+ media assets — enabling
semantic search and source-grounded Q&A at scale.
Improved retrieval accuracy to 92% using hybrid search, metadata
filters, reranking, and evaluation pipelines; reduced average
response latency by 45% through async APIs, caching, and optimized
vector search.
Enabled content, marketing, and analytics teams to reduce manual
research effort by 60–70%, supporting 1M+ monthly semantic searches
across franchise and catalog intelligence use cases.
"""

TASK: Write a cold email to the HR recruiter for this role.

FORMAT:
- Subject line (under 15 words, specific, no clichés)
- Greeting (use "Hi Archana" — not "Dear Hiring Manager")
- Body: short and crisp, showcase the project in STAR form
        (Situation → Task → Action → Result)
- One clear ask (15-minute screening call)
- Sign-off

LENGTH: Under 300 words total.

CONSTRAINTS:
- No "I hope this email finds you well"
- No "I am writing to express my interest"
- No "esteemed team", "valuable addition", "proven track record"
- No listing of generic qualifications — pick ONE specific match
- No "please find my resume attached" — link is in signature
- Confident tone, not begging tone

EXAMPLES of the style I want:

Subject: Async agents → OpenAI Senior AI role
"Hi Maya — I saw the Senior AI Engineer post. The 'long-horizon
agents' line is exactly what I've been shipping for two years at
[company] — including an async refactor that cut latency by 3x.
15 minutes this week to walk you through it? Resume + agent demo
in signature."

QUALITY CHECK:
Before finalizing, verify: under 300 words, no banned phrases,
one specific match to the JD, one clear ask in STAR form.
If anything fails, rewrite it.
```

**[VISUAL: Run it. Output appears — a tight, confident, STAR-form email that names a specific JD bullet (long-horizon agents → my RAG platform with retrieval reliability at scale), has one clear ask, no clichés. Hold for 4 seconds so viewers can read it.]**

```
Subject: Long-horizon agents → 25M-chunk RAG at WBD → OpenAI Senior AI role

Hi Archana —

Saw the Senior AI Engineer post. The line about "long-horizon agents,
tool use, and reliability at scale" is exactly the problem I've been
shipping for the last two years.

(Situation) Warner Bros. Discovery needed semantic search across 40K+
media assets — scripts, subtitles, PDFs, metadata — but generic
retrieval was 60% accurate, latency was painful, and source-grounding
was inconsistent for any "answer the question" use case.
(Task) Build a production-grade RAG Content Intelligence Platform
that 5 teams could trust as a single source of truth.
(Action) Indexed 25M+ chunks, layered hybrid search + metadata
filters + reranking + an evals pipeline, and rewrote the hot path
async with aggressive caching.
(Result) Retrieval accuracy → 92%. Latency → -45%. Manual research
effort across content, marketing, and analytics → down 60–70%.
1M+ monthly semantic searches today.

15 minutes this week to walk you through the agentic-retrieval
architecture and where I'd take it next?

Resume + a 90-second platform demo are in my signature.

— Ravi
```

> *Same model. Same task. One is going to the trash. The other is getting a reply. The difference is everything you just saw on the screen.*

> *Here's the deal for the next twenty-five minutes — we're going to **build this exact prompt together, from scratch**. Five upgrades. Skeleton. Constraints. Examples. Decomposition. And one final move most beginners don't know. By the end, you'll have written — with me — the prompt I just pasted. Same template works for cold emails, LinkedIn posts, code reviews, cover letters, agents. One prompt, infinite uses. Plus a quick two-minute reality check on why this matters whether you use ChatGPT or call the API yourself.*

**[CLIFFHANGER]**
> *And the last upgrade — the one almost nobody on YouTube is talking about — that's the move that separates a beginner from someone who actually knows what they're doing. I'm saving the full explanation for the end. Stick around.*

---

## 0:45 – 1:15 · PROMISE & POSITIONING

**[VISUAL: On-screen text: "5 Upgrades · 1 Real Prompt · 25 Minutes"]**

> *I'm Balaji. AI engineer for a Swiss telecom, write fifty to a hundred prompts a day in production. We're building that prompt you just saw together — **step by step**, no theory dumps, no "act as a world-class expert" nonsense. Five upgrades, one prompt, twenty-five minutes.*

**[VISUAL: On-screen list, items revealed as you say them]**
1. The 5-part skeleton
2. Constraints
3. Few-shot examples
4. Decomposition
5. *(blurred / hidden)* The secret one

**[CLIFFHANGER]**
> *But before we touch the first upgrade — I want to answer a question you might be having right now. "I just type into ChatGPT. Why do I need to engineer anything?" Stick with me for two minutes. Because by the end of this next section, you'll see prompt engineering is happening every single time you press send — you just haven't noticed it yet. And the moment you build your own chatbot? You're the one writing every block. Let me show you.*

---

## 1:15 – 3:45 · WHY THIS MATTERS — UI vs API, AND WHAT'S HIDING IN THE BACKEND

**[VISUAL: Title card: "Why You Need This — In The UI AND In The API"]**

### Beat 1 — Even in ChatGPT, prompt engineering is already happening (you're just not seeing it)

**[VISUAL: Face cam, direct address. Then cut to a ChatGPT window.]**

> *Quick truth before we go in. You might be thinking — "I just type into ChatGPT. I'm not building anything. Why do I need to engineer prompts?"*

> *Here's the thing. Every time you press send in ChatGPT, you're not the only one writing the prompt. The UI is silently stitching together a much bigger prompt in the background. You just don't see it.*

**[VISUAL: Annotated diagram of what gets sent on every ChatGPT request. Build it on screen, layer by layer:]**
```
                  WHAT YOU TYPE
                        ↓
  ┌─────────────────────────────────────────────┐
  │  Hidden system prompt (OpenAI's defaults)   │
  │  + Your custom instructions                 │
  │  + Memory ("what ChatGPT remembers")        │
  │  + Last 10–20 messages in this chat         │
  │  + Any attached files / images              │
  │  + YOUR actual question                     │
  └─────────────────────────────────────────────┘
                        ↓
              THE REAL PROMPT
              the model sees
```

> *That entire stack gets sent to the model. Every. Single. Time. The UI is doing prompt engineering FOR you, in the background, before your message ever reaches GPT.*

> *This is why two people typing the exact same question can get totally different answers. Their hidden context is different. Their memory is different. Their custom instructions are different.*

> *So even if you never write a line of code — knowing what's in that hidden stack lets you control YOUR side of it. Better custom instructions. Smarter use of memory. Cleaner conversation history. That's prompt engineering in the UI.*

### Beat 2 — Now you build your own chatbot. The UI is gone. You're the UI.

**[VISUAL: Hard cut. Face cam.]**

> *Now imagine you stop typing into ChatGPT, and instead you build your own chatbot. Maybe a customer support bot for your company. Maybe an AI tutor. Maybe an agent that reads your emails. The moment you do that — everything changes.*

**[VISUAL: Real Python API code fills the screen. Highlight the empty fields in red as you talk.]**

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "???"},   # ← YOU write this
        {"role": "user",   "content": "???"},   # ← YOU manage this
    ],
)
```

> *This is what a real API call looks like. Look at those two empty strings. Look at them. **You** are now writing every word that used to be hidden.*

**[VISUAL: Cycle through 4 captions on screen as you list them — each appears next to a red X over the corresponding part of the API "hidden stack" from Beat 1.]**

> *Four things change the moment you go from the UI to the API:*

> *One. **No hidden system prompt.** ChatGPT's safety net is gone. If you don't write "answer only questions about our product, refuse everything else" — your support bot will happily help users debug their JavaScript. Bad system prompt = bad chatbot, on every single conversation.*

> *Two. **No memory. No conversation history.** Every API call is amnesia. Your user says "my name is Ravi" in message one. Message two they say "what's my name?" The model has no idea — unless YOU sent the previous turn back in the messages array. You manage the entire history.*

> *Three. **No safe defaults.** If you don't say "don't make up facts about our pricing", it will. If you don't say "respond in Hindi if the user writes in Hindi", it won't. Every behavior you took for granted in ChatGPT — gone. You write it back in.*

> *Four. **Cost per token.** Every wasted word in your prompt costs real money, multiplied by every user, every message. A bad 500-token prompt that should have been 200 tokens — that's 2.5x your bill, forever.*

**[VISUAL: Cut to a quick visual of an agent in a loop — same prompt firing 50 times, dollar signs ticking up.]**

> *And if you're building **agents** — like the async agent video I did last week — that bad prompt doesn't run once. It runs in a loop. Fifty times per task. A 470x cost mistake compounds fast.*

> *This is where prompt engineering stops being a nice-to-have. It becomes the difference between a chatbot people use and one they uninstall. Between an agent that ships and one that bankrupts you in API bills.*

### Beat 3 — Same 5 upgrades. Both worlds. Higher stakes when you're the builder.

**[VISUAL: Face cam. On-screen split: left "ChatGPT UI", right "Your API code". Five upgrade icons appear in the middle, arrows pointing both ways.]**

> *Here's the good news. The five upgrades I'm about to teach you — they work in **both** worlds.*

> *In the UI, they sharpen YOUR side of the conversation — your custom instructions, your questions, your follow-ups. You become the user who consistently gets great answers while everyone else gets generic slop.*

> *In the API, they ARE the conversation. The whole system prompt, the whole user message, the whole structure — you build it block by block.*

> *Same skill. Same five upgrades. Just much higher stakes when you're the one assembling the prompt instead of letting the UI do it for you.*

**[CLIFFHANGER]**
> *Okay. Now you know why this matters whether you type into ChatGPT or write Python that calls it. Let's build the first upgrade — the skeleton that fixes 80% of bad prompts on day one.*

---

## 3:45 – 7:30 · TECHNIQUE 1 — THE 5-PART SKELETON

**[VISUAL: Title card: "Upgrade 1 · The 5-Part Skeleton"]**

> *Here's a question I want you to think about: when you give AI a task, what does AI actually know about you?*

> *Nothing. Zero. It doesn't know who you are, who's reading the output, how long it should be, or what format you want. So it guesses. And when AI guesses, you get generic.*

> *The fix is a skeleton. Every prompt that works has five parts.*

**[VISUAL: Build the skeleton on screen, one part at a time]**
```
1. ROLE     → who AI should act as
2. CONTEXT  → who the output is for + any reference material
3. TASK     → what to do
4. FORMAT   → how the output should look
5. LENGTH   → how long
```

> *Quick note on CONTEXT, because this is where most people miss something big. Context isn't just "who the output is for." It's also where you paste any **reference material** — your README, a job description, a transcript, a code file, anything AI should base its answer on. If you want AI to write a cold email about a job, paste the actual JD. If you want AI to showcase your project, paste the actual project description. Don't summarize — paste it.*

> *Let's apply this to the bad prompt from the hook.*

**[VISUAL: Original bad prompt re-appears: `Write an email to HR at OpenAI about the Senior AI Engineer job opening. I want to apply.`]**

> *Watch what happens when we add all five parts. I'm going to build this prompt block by block — and by the end of this video, it'll be the exact prompt you saw at the start.*

**[VISUAL: Empty editor on the right side of the screen. Title above it: "OUR PROMPT (building...)". Type out each block slowly, with each new block appearing one at a time on screen.]**
```
ROLE: You are an AI engineer with 5 years of production experience,
writing a cold email to a recruiter — confident, specific,
not desperate.

CONTEXT:
Audience — a senior recruiter at OpenAI who reads 200+ emails per day
My background — built async multi-agent systems in production and
                scaled them to millions of monthly users
Goal — get a 15-minute screening call, not a generic "thanks we'll review"
Stakes — this email is one of hundreds in their inbox today

REFERENCES:

The job post I'm applying for:
"""
Senior AI Engineer — OpenAI
We're looking for engineers who have shipped agentic AI systems
to production. You'll work on long-horizon agents, tool use, and
reliability at scale. Strong Python + experience with LLM APIs
required. Bonus: experience with async, retrieval, or evals.
"""

My flagship project (the one to showcase in this email):
"""
Built a production-grade RAG-based Content Intelligence Platform
for Warner Bros. Discovery, indexing 25M+ chunks across 40K+ media
assets. Hybrid search + reranking + evals took retrieval accuracy
to 92%. Async + caching cut latency 45%. Serves 1M+ monthly
semantic searches across content, marketing, and analytics teams.
"""

TASK: Write a cold email to the HR recruiter for this role.

FORMAT:
- Subject line (under 15 words, specific, no clichés)
- Greeting (use "Hi Archana" — not "Dear Hiring Manager")
- Body: short and crisp, showcase the project in STAR form
        (Situation → Task → Action → Result)
- One clear ask (15-minute screening call)
- Sign-off

LENGTH: Under 300 words total.
```

> *See what I did? I didn't describe the JD in my own words. I didn't describe my project in my own words. I pasted both inside the REFERENCES block. Now ChatGPT has the actual source material on both sides — it can pull the exact JD phrasing and the exact project numbers without me re-typing them. That's reference grounding. Free quality boost.*

> *And notice — the audience for this email isn't "a hiring manager". It's "a senior recruiter at OpenAI who reads 200+ emails per day". That one detail tells ChatGPT to write something that survives a 5-second skim. Specificity in CONTEXT is what specificity in OUTPUT comes from.*

**[VISUAL: Run it in ChatGPT. Show the visibly better output — a structured STAR-form email that names a specific JD bullet and uses the real project numbers. Side-by-side with the bad output from the hook for contrast.]**

> *Same model. Same task. Just five parts. The output is already 5x better than what we started with — it actually mentions the JD, actually shows the project, actually has a structure.*

**[VISUAL: Prompt Power Meter graphic: Bad prompt = 2/10 → 5-part skeleton = 6/10]**

> *This is the floor. From here, every upgrade only makes it better.*

**[CLIFFHANGER]**
> *But there's still something missing. The output is good. It's not great. Because right now, ChatGPT is doing everything you asked — but also a bunch of things you didn't want. Watch what happens when we tell it what NOT to do.*

---

## 7:30 – 10:15 · TECHNIQUE 2 — CONSTRAINTS & NEGATIVES

**[VISUAL: Title card: "Upgrade 2 · Constraints — Tell AI What NOT to Do"]**

> *Look at the email ChatGPT generated. The 5-part skeleton fixed the structure — but watch the language.*

**[VISUAL: Highlight the generated email. Circle problems in red, one at a time as you read each:]**
- "I am writing to express my keen interest..."
- "I would be a valuable addition to your esteemed team"
- "proven track record of delivering innovative solutions"
- "Please find my resume attached"
- "I look forward to hearing from you soon"

> *This is where most people give up. They blame AI. But AI isn't reading your mind. If you don't say "no 'I hope this email finds you well'", ChatGPT assumes that's fine — because that's how 90% of the cold emails on the internet start, and that's what the model learned from. If you don't say "no esteemed team", you're getting esteemed team.*

> *Constraints are the second skeleton. And they're often more powerful than the positive instructions, because they cancel out everything the model defaults to.*

**[VISUAL: Add a new CONSTRAINTS block to the prompt being built on screen:]**
```
CONSTRAINTS:
- No "I hope this email finds you well"
- No "I am writing to express my interest"
- No "esteemed team", "valuable addition", "proven track record"
- No listing of generic qualifications — pick ONE specific match
- No "please find my resume attached" — link is in signature
- Confident tone, not begging tone
```

**[VISUAL: Re-run the prompt. Show the cleaner output side by side with the previous one. Highlight in green every constraint that was respected.]**

> *Look at that. Every banned phrase is gone. The tone shifted from "please notice me" to "here's what I built, want to talk?". That's a different person writing.*

**[VISUAL: Prompt Power Meter: 6/10 → 7.5/10]**

> *And here's the small trick most people miss — **"do not"** is more powerful than "please avoid". Be direct. AI is a tool, not your colleague. You don't have to be polite.*

**[VISUAL: Side-by-side: "Please try to avoid corporate clichés" vs "No 'I hope this email finds you well'. No 'esteemed team'. No 'proven track record'."]**

> *One more thing about constraints, in production. The reason "pick ONE specific match" is in there — without it, the model lists everything. Five years of experience, Python, async, retrieval, evals... A recruiter who reads 200 emails a day skips a list. They stop on one specific match. Constraints turn AI from a shotgun into a sniper.*

**[CLIFFHANGER]**
> *Okay. The skeleton works. The constraints work. But AI still doesn't know what "good cold email writing" actually looks like — for you. The next upgrade is how you show it. And it's the single biggest jump in quality you'll see today.*

---

## 10:15 – 15:00 · TECHNIQUE 3 — FEW-SHOT EXAMPLES

**[VISUAL: Title card: "Upgrade 3 · Few-Shot — Show, Don't Tell"]**

> *Imagine I hire you as a writer. I say: "write in my style." What's the first thing you'd ask?*

> *You'd ask: "show me your old writing." Because words can't describe a style. Examples can.*

> *AI is the same. The fastest way to make AI sound like you is to give it 2 or 3 examples of writing you actually like.*

> *This technique is called **few-shot prompting**. Works on every model — ChatGPT, Claude, Gemini, all of them.*

**[VISUAL: Add an EXAMPLES block to the prompt being built on screen:]**
```
EXAMPLES of the style I want:

Subject: Async agents → OpenAI Senior AI role
"Hi Maya — I saw the Senior AI Engineer post. The 'long-horizon
agents' line is exactly what I've been shipping for two years at
[company] — including an async refactor that cut latency by 3x.
15 minutes this week to walk you through it? Resume + agent demo
in signature."
```

> *One example. That's all it takes for ChatGPT to lock onto the voice. Notice what this example does — it leads with a JD callback ("the 'long-horizon agents' line"), names one specific result ("cut latency by 3x"), and asks for one specific thing ("15 minutes this week"). It models the entire shape of a great cold email in five sentences.*

**[VISUAL: Re-run the prompt. Show the dramatically more on-style output. Highlight the same shape in the new output: JD callback → STAR-form proof → 15-minute ask.]**

> *See what happened? The rhythm changed. The opening changed. Even the dash punctuation changed. Without me explaining anything about "tone". The model just copied the pattern.*

**[VISUAL: Prompt Power Meter: 7.5/10 → 9/10]**

> *Two or three examples is the sweet spot — I used one here because the format is tight enough that one is enough. More than five is wasted tokens. And the examples don't have to be perfect — they just have to **show the pattern**.*

### Bonus mini-demo — "How I actually use this" (fast cut, ~75 sec)

**[VISUAL: Hard cut to a second ChatGPT session. Fast-cut montage with captions on screen.]**

> *Quick sidebar — let me show you the second place I use this every week, just so you see the technique isn't email-specific. Every Monday I generate hooks for my next video. I never start from scratch.*

**[VISUAL: Fast montage — paste 3 past hooks (Async AI Agent, How LLMs Are Built, How to Control ChatGPT) → ask AI to learn the pattern → request 3 hooks for new topics. Cut tight, captions only.]**

```
HOOK 1 (Async AI Agent): "Two chatbots. Same prompt. Same model. Same
code — almost. The slow one took thirty-three seconds. The fast one —
twelve. Twenty-one seconds saved on a single question."

HOOK 2 (How LLMs Are Built): "$100 million. That's how much it costs
to train one large language model. Not to run it. Just to build it
— once."

HOOK 3 (How to Control ChatGPT): "Watch this. I'm going to type one
sentence into ChatGPT. The response comes in 2 seconds. But behind
those 2 seconds? 300 billion words of training data."

→ Generate 3 hooks in this style for:
1. Why your AI agent hallucinates in production
2. The one Cursor shortcut that saved me 2 hours a day
3. Switching from manual testing to TDD
```

**[VISUAL: 3 generated hooks appear, each held on screen ~3 sec.]**

> *Three of my past hooks pasted in. AI learned the pattern. Three new hooks — they sound like me. Same technique, different use case.*

> *You can do this with emails, pull requests, commit messages, anything you've written before. Show AI two or three examples — it copies the pattern.*

### Mini-section: Few-shot vs References — don't confuse these

**[VISUAL: Title card: "Few-shot vs References — Different Jobs"]**

> *Quick clarification before we move on. Something that confused me for the first six months I used these tools — and confuses almost every beginner.*

> *Look at our prompt now. We have TWO different kinds of "content" pasted into it.*

**[VISUAL: Side-by-side split on screen, pointing to the actual blocks in the prompt we've built:]**
```
LEFT — REFERENCES                  RIGHT — EXAMPLES
(inside REFERENCES block)          (inside EXAMPLES block)

The OpenAI JD                      The "Hi Maya — async agents"
+ my WBD project description.      sample email.

Source material AI bases its       Style guide AI copies the
answer ON.                         voice OF.

Tells AI WHAT to write about.      Teaches AI HOW to write it.
```

> *They look similar — both are "stuff I pasted into the prompt." But they do completely different jobs.*

> *References tell AI **what** to write about. The JD is what I'm applying for. The project description is what I'm showcasing. AI extracts facts from both.*

> *Examples teach AI **how** to write it. The "Hi Maya" sample email is the voice — AI copies the rhythm, the dash punctuation, the 5-sentence shape, the "Resume + demo in signature" closer.*

> *Mix them up and your output gets confused. Paste the JD inside your EXAMPLES block, and AI thinks you want bullet-pointed corporate-speak (because that's how JDs are written). Paste the "Hi Maya" sample inside your REFERENCES block, and AI writes you an email *about* the Maya email — not in its style.*

> *Rule: **References = source. Examples = style.** Different blocks. Different jobs. Both matter.*

**[CLIFFHANGER]**
> *Three upgrades in. The output is already 90% there. But what about when the task is too big for one prompt? Like — "write the whole blog post, with the title, intro, body, and CTA." That's where most prompts fall apart. And there's a fix for it that's so simple, you'll wonder why you weren't doing it already.*

---

## 15:00 – 18:00 · TECHNIQUE 4 — DECOMPOSITION: ONE PROMPT, ONE JOB

**[VISUAL: Title card: "Upgrade 4 · Decomposition — Don't Ask AI to Do 5 Jobs"]**

> *Here's a rule I follow in production: if a prompt has more than one job, it will fail at one of them.*

> *AI is good at one thing at a time. Give it five things — pick the strongest JD bullet, draft the email, tighten it to 300 words, check for banned phrases, polish the subject line — and at least one gets dropped, rushed, or hallucinated.*

> *The fix is **decomposition**. Break the work into stages. Two ways to do it.*

### Flavor 1 — Chain the prompts (the cleaner version)

**[VISUAL: On-screen text: "Flavor 1: Chain the prompts"]**

> *Don't try to do everything in one prompt. Use three prompts in sequence — even for a 300-word email. Sounds like overkill. It isn't.*

**[VISUAL: Diagram — 3 boxes, output of one feeding into the next:]**
```
Prompt 1: Read the JD + my project. Which ONE bullet from the JD
          is the strongest match for my WBD work? Quote the line.
   ↓
Prompt 2: Draft a STAR-form email body around that one match.
          Lead with the JD callback.
   ↓
Prompt 3: Polish — under 300 words, no banned phrases, one
          specific ask, one strong subject line.
```

> *Each prompt has one job. Each output is reviewable. If step 1 picks the wrong JD bullet, you fix step 1 — you don't waste time rewriting the whole email. This is how I write production prompts. **No black box.***

> *Use this for: anything important enough that you'd notice if it failed. Cold emails to your dream company. Long-form content. Multi-step coding tasks. Anything where the output has multiple distinct parts.*

### Flavor 2 — Plan inside one prompt (the tactical version)

**[VISUAL: On-screen text: "Flavor 2: Plan inside one prompt"]**

> *If you don't want to manage three separate prompts, you can ask AI to plan first, then write — all inside one prompt.*

**[VISUAL: Add a planning block to the running prompt:]**
```
Before writing the email, plan it first:
1. Which ONE bullet from the JD is the strongest match for my WBD
   project? Quote the line.
2. What's the Situation → Task → Action → Result for that match,
   in one sentence each?
3. What's the subject line that earns the open in a 200-email inbox?
4. Now write the email.
```

> *This used to be called "chain-of-thought" — telling AI to think step by step. It still works on plain chat models like GPT-4o-mini, Gemini Flash, or older open-source models.*

> *Honest note — **I'm simplifying**. On modern reasoning models like GPT-5 or Claude Opus with thinking mode, you don't need to say "think step by step" — they already do it internally. I covered the reasoning-vs-chat split in the "How to Control ChatGPT" video. The point isn't the magic phrase. The point is: **break the work into stages**. Whether you do that across three prompts or inside one — same idea.*

**[VISUAL: Prompt Power Meter: 9/10 → 9.5/10]**

**[CLIFFHANGER]**
> *Four upgrades. You already know more than 95% of ChatGPT users. But the fifth one — the one I promised at the start — this is the one that changed how I write prompts forever. And once you see it, you can never go back.*

---

## 18:00 – 21:30 · TECHNIQUE 5 — INTERVIEW-STYLE PROMPTING (THE BIG REVEAL)

**[VISUAL: Title card: "Upgrade 5 · Let AI Interview YOU"]**

> *Here's the problem with everything I just taught you.*

> *You still have to know what to include in the prompt. Role. Context. References. Constraints. Examples. That's a lot for a beginner. And even for me — for new tasks — I don't always know what context AI needs.*

> *So I let AI ask me.*

**[VISUAL: Pause for effect. Then show what would have happened if I'd skipped Techniques 1–4 and just used Technique 5 directly — back to the original one-line prompt, plus the interview move bolted on:]**
```
I want to write a cold email to HR at OpenAI about the
Senior AI Engineer job opening. I want to apply.

Before you write anything, interview me. Ask me one question
at a time about anything you need — the JD, my background,
my best project, audience, tone, format, constraints, examples.
After each answer, ask the next question. When you have enough
to write something great, say "I have enough" and write the email.
```

**[VISUAL: Run it. Show ChatGPT asking the first question.]**

> *ChatGPT:* "Got it. First question — could you paste the job description, or share the link? I'd like to anchor the email on a specific line from the post, not generic interest."

> *Me:* "[pastes the OpenAI Senior AI Engineer JD]"

> *ChatGPT:* "Perfect. Second question — out of the things this JD asks for (long-horizon agents, tool use, reliability at scale, async, retrieval, evals), which one have you shipped the most of? Tell me about that project."

> *Me:* "Reliability at scale and retrieval. I built a 25-million-chunk RAG platform at WBD."

> *ChatGPT:* "Got it. Third question — what's the recruiter's name? And do you know if they're more technical or HR-focused?"

> *Me:* "Archana. HR-focused, but she screens AI roles, so she knows the terms."

**[VISUAL: Continue 2–3 more questions in a fast cut. AI gradually extracts the JD, the project, the tone, the ask, the banned phrases. It builds the same prompt we built in Techniques 1–4 — but it's extracting the answers from me instead of me having to know the structure.]**

> *Look at what's happening. AI is pulling **the right context out of me** — context I'd otherwise have to remember to type into ROLE, CONTEXT, REFERENCES, CONSTRAINTS. By the time it writes the email, it has reconstructed every single block we built across the last four techniques.*

**[VISUAL: Final output. Show the email — it should look almost identical to the one we built manually, because the underlying prompt blocks ended up the same.]**

**[VISUAL: Prompt Power Meter: 9.5/10 → 10/10. Confetti animation.]**

> *This is the technique that separates beginners from pros. Beginners try to write the perfect prompt. Pros let AI extract the perfect prompt from them.*

> *I use this for: cold emails to people I really want to reach. Planning videos. Designing system architecture. Anything where I don't know what AI needs to know — or where I don't want to forget a block.*

> *And here's the honest part — **I'm simplifying**. In production, with API access, you'd structure this differently. But for ChatGPT or Claude in the browser? This one line — "interview me one question at a time" — is the most valuable prompt move I've learned in three years.*

**[CLIFFHANGER]**
> *Now let me show you the final master prompt that combines all five upgrades. You can copy it. Adapt it. Use it for the rest of your career.*

---

## 21:30 – 23:00 · MASTER PROMPT TEMPLATE (+ API MAPPING CALLBACK)

**[VISUAL: Title card: "Your Master Prompt — Copy This"]**

> *Remember the prompt I showed you at the very start of this video? The one that turned a generic OpenAI cold email into something a recruiter would actually reply to? Here it is in full — every block we've built together over the last twenty minutes, in one place. This is the prompt I promised. We just built it together.*

**[VISUAL: Full filled-in master prompt on screen. Stays up for ~25 seconds so viewers can pause and screenshot. Highlight each block label in a different color as the camera pans down.]**

```
ROLE: You are an AI engineer with 5 years of production experience,
writing a cold email to a recruiter — confident, specific,
not desperate.

CONTEXT:
Audience — a senior recruiter at OpenAI who reads 200+ emails per day
My background — built async multi-agent systems in production and
                scaled them to millions of monthly users
Goal — get a 15-minute screening call, not a generic "thanks we'll review"
Stakes — this email is one of hundreds in their inbox today

REFERENCES:

The job post I'm applying for:
"""
Senior AI Engineer — OpenAI
We're looking for engineers who have shipped agentic AI systems
to production. You'll work on long-horizon agents, tool use, and
reliability at scale. Strong Python + experience with LLM APIs
required. Bonus: experience with async, retrieval, or evals.
"""

My flagship project (the one to showcase in this email):
"""
Built a production-grade RAG-based Content Intelligence Platform
for Warner Bros. Discovery, indexing 25M+ chunks across 40K+ media
assets. Hybrid search + reranking + evals took retrieval accuracy
to 92%. Async + caching cut latency 45%. Serves 1M+ monthly
semantic searches across content, marketing, and analytics teams.
"""

TASK: Write a cold email to the HR recruiter for this role.

FORMAT:
- Subject line (under 15 words, specific, no clichés)
- Greeting (use "Hi Archana" — not "Dear Hiring Manager")
- Body: short and crisp, showcase the project in STAR form
        (Situation → Task → Action → Result)
- One clear ask (15-minute screening call)
- Sign-off

LENGTH: Under 300 words total.

CONSTRAINTS:
- No "I hope this email finds you well"
- No "I am writing to express my interest"
- No "esteemed team", "valuable addition", "proven track record"
- No listing of generic qualifications — pick ONE specific match
- No "please find my resume attached" — link is in signature
- Confident tone, not begging tone

EXAMPLES of the style I want:

Subject: Async agents → OpenAI Senior AI role
"Hi Maya — I saw the Senior AI Engineer post. The 'long-horizon
agents' line is exactly what I've been shipping for two years at
[company] — including an async refactor that cut latency by 3x.
15 minutes this week to walk you through it? Resume + agent demo
in signature."

PROCESS:
Before writing, ask me one question at a time if any important
context is missing — recruiter name, specific JD bullet to anchor
on, anything else. When you have enough, say "I have enough"
and think step by step before writing.

QUALITY CHECK:
Before finalizing, verify: under 300 words, no banned phrases,
one specific match to the JD, one clear ask in STAR form.
If anything fails, rewrite it.
```

> *That's it. That's the whole thing. Every block we built in the last twenty minutes — ROLE, CONTEXT, REFERENCES with the JD AND the project, TASK, FORMAT, LENGTH, CONSTRAINTS, EXAMPLES, PROCESS, QUALITY CHECK — assembled into one prompt that does the job.*

### And here's the generic template — copy this, swap the contents, reuse forever

**[VISUAL: The filled-in prompt fades. The same prompt re-appears with the contents wiped — only the block labels and placeholder brackets remain. Stays on screen ~15 seconds for pause-and-screenshot.]**

```
ROLE: You are a [specific role].

CONTEXT:
Audience — [who will read or use this]
My background — [who I am, in one line]
Goal — [what I want to achieve]
Stakes — [why this output has to be good]

REFERENCES (paste source material — keep """ delimiters):
"""
[JD / README / code / transcript / data — the thing AI grounds on]
"""
"""
[Your project / second source if needed]
"""

TASK: [What to do, in one sentence.]

FORMAT: [Structure — bullets, paragraphs, sections, JSON, etc.]

LENGTH: [Specific number — words, sentences, bullets.]

CONSTRAINTS:
- No [banned phrase 1]
- No [banned phrase 2]
- [Tone direction]
- [Format thing to avoid]

EXAMPLES of the style I want (few-shot — show, don't tell):
[1-3 examples of writing in the voice you want]

PROCESS:
Before generating, ask me one question at a time if any important
context is missing. When you have enough, say "I have enough"
and think step by step before writing.

QUALITY CHECK:
Before finalizing, verify the output matches TASK, LENGTH,
FORMAT, and CONSTRAINTS. Fix anything that doesn't fit.
```

> *Two things to call out. **REFERENCES** is where you paste source material — JD, README, code, transcript, project description. **EXAMPLES** is your style guide — past writing in the voice you want. Different blocks, different jobs. References = source. Examples = style.*

> *And the last two blocks — **PROCESS** and **QUALITY CHECK** — make AI plan before writing and review after writing. Two safety nets. They cost almost nothing and they cut bad outputs in half.*

**[VISUAL: Quick split-screen callback — left: the master prompt template. Right: the Python API code from earlier. Lines connect ROLE → `system` role, everything else → `user` role.]**

> *Quick callback for the builders. Remember the API code I showed you at the start? Here's how this template maps to it. **ROLE** goes in your `system` message — that's the persistent identity for every turn. **CONTEXT, REFERENCES, TASK, FORMAT, LENGTH, CONSTRAINTS, EXAMPLES, PROCESS, QUALITY CHECK** — all of that goes in the `user` message, or split across system and user depending on how reusable each piece is. Same blocks. Different envelope. The skill is identical.*

> *One more thing. The biggest mistake people make? They write one prompt, get a bad output, and blame AI. Don't. **Refine.** "Make it shorter." "More technical." "Cut the third paragraph." "Lead with the JD callback instead of the project." AI is a conversation, not a vending machine.*

---

## 23:00 – 23:20 · HONEST SCOPE-SETTING (MULTIMODAL ASIDE)

**[VISUAL: Face cam, direct address]**

> *One quick honest note before we wrap. Today we used **text references** — pasting a README, a JD, a transcript. That's the most common form of grounding. But images and screenshots are a special kind of reference, and they need their own techniques. Pointing to regions in an image. Describing what to look for **before** pasting a screenshot. Screenshot-to-code. Combining text + visuals without confusing the model. That's a dedicated video — dropping it next.*

---

## 23:20 – 24:30 · CTA + NEXT-VIDEO TEASE

**[VISUAL: Face cam, direct address]**

> *If this video saved you time, drop the word **PROMPT** in the comments and I'll pin a link to this exact template — formatted, downloadable, free.*

> *And the next video in this Phase 3 series — remember at the start when I showed you all that hidden scaffolding ChatGPT's UI was assembling for you behind the scenes? System prompt, memory, conversation history, attached files? When you're the one building the chatbot or the agent, **you** manage all of that yourself. That whole job has a name — it's called **context engineering**. In 2026, prompt engineering is being absorbed into it. That's the skill that separates people building agents in 2026 from people still typing into ChatGPT. After that, I'm covering how to stop prompt injection attacks on your agents — that's becoming a real problem in production. Subscribe so you don't miss either.*

**[VISUAL: End screen with next video thumbnail + subscribe button]**

---

# APPENDIX

## Retention Devices Used (skill 01 + skill 07)

| Device | Where | Purpose |
|---|---|---|
| Live demo first hook | 0:00–0:45 | Fulfill thumbnail promise in <45s |
| Show the final prompt in the hook | 0:30 | Set the destination — viewer wants to know "how do I build that?" |
| Numbered promise ("5 upgrades, 25 min") | 0:45–1:15 | Commitment + scannable |
| **"Why this matters — UI vs API" widening beat** | 1:15–3:45 | Tells every audience segment (ChatGPT-only users, devs, agent builders) this video is for them; reveals the hidden prompt-building in the UI; raises stakes for API/agent builders; sets up the V014 context-engineering tease |
| Cliffhanger at every section break | 6x | Force into next section |
| Prompt Power Meter (2/10 → 10/10) | Throughout | Visible cumulative progress |
| Hidden 5th upgrade tease | 0:30, 1:13, 15:00 | Sustain curiosity to the end |
| Bonus mini-demo with real hooks (skill 07 callback) | Technique 3 (75-sec fast cut) | Authenticity + viewers see his real workflow |
| Few-shot vs References mini-section | Technique 3 close | Removes the single biggest confusion beginners have |
| Honesty markers ("I'm simplifying") | Technique 4, Technique 5 | Trust |
| Quotable repeatable line | "Step by step", "no black box" | Brand reinforcement |
| Emotional unified example ("cold email to OpenAI HR — applying to my dream job, using my real WBD project") | Hook + Techniques 1–5 + Master Prompt (entire script) | Highest possible career stakes → instant identification; viewer projects themselves into the example in <5 seconds; promise-payoff loop is closed by 23:00 when the prompt shown at 0:30 has been built block-by-block in front of them |
| **Block-by-block prompt construction** (visible "prompt growing" left panel) | Techniques 1→5 | Strongest tutorial retention pattern — viewer literally watches their destination (the hook prompt) get assembled on screen, brick by brick. Removes the "I see the result but don't know how to get there" gap that kills most tutorials |
| Authenticity anchor (real WBD RAG platform project used as the showcase content) | REFERENCES block in Techniques 1, 3, 5 + Master Prompt | "He's not making up a fake example — he's actually applying to OpenAI with HIS real project." Credibility multiplier; signals the technique works on real things |
| Comment-bait CTA ("comment PROMPT") | 23:30 | Algorithm + community |
| Next-video teases (context engineering + prompt injection nod) | 23:50 | Series binge |

## Signature Phrases Used (skill 01 — one per video rule)

- **"Step by step"** — used in promise (0:50) and Technique 4 narration. Earned, not opened with.
- **"No black box"** — used once in Technique 4 / Flavor 1 (13:30). Anchors the "real engineer" identity.
- ~~"In real time, in production"~~ — NOT used. Save for a production-grade follow-up.

## Anti-Pattern Blocklist (skill 01) — confirmed clean

- [x] No "hey guys", no "welcome to my channel"
- [x] No "in this video we'll cover"
- [x] All technical terms in English (`prompt`, `temperature`, `few-shot`, `chain-of-thought`)
- [x] No passive voice in spoken lines
- [x] No paid product pitch in first 2 minutes
- [x] No toy-only example without production note (Flavor 1 + honesty marker in Technique 5 cover this)
- [x] No hidden errors — bad outputs shown explicitly, then fixed
- [x] **No unsupported stats** — removed "OpenAI's data shows" from HOOK B; removed "90% of YouTube videos" from Why-this-video table

## Topics to swap if the cold-email-to-OpenAI example doesn't fit

The 5-upgrade structure is example-agnostic. The script currently uses **one unified example** throughout: a cold email to HR at OpenAI for the Senior AI Engineer role, using Balaji's real WBD RAG platform as the showcase. The same scaffold works for any other "important written output" example — you just swap the contents.

### Drop-in replacements (one example must work end-to-end across the whole script)

A good replacement needs all four of these properties:

1. **Binary, instantly-readable diff in the hook** (bad output vs. good output difference is visible in <2 seconds)
2. **Real emotional stakes** (the viewer cares whether the output is good)
3. **Decomposable into the 5 prompt blocks** (ROLE + CONTEXT + REFERENCES + TASK + FORMAT + LENGTH + CONSTRAINTS + EXAMPLES make sense for it)
4. **Universal applicability** (most viewers can imagine running this task themselves the same day)

### Candidate replacements

| Replacement | Why it works | What it costs |
|---|---|---|
| **Cover letter for a specific JD** (closest alternative) | Same career stakes, same JD as REFERENCES, similar STAR-form output | Less universal than cold email — fewer people are job-hunting right now |
| **PR description for a non-trivial change** (developer angle) | Diff between "Updated stuff" and a proper PR description is binary; CONSTRAINTS map to your team's PR style guide | Only works for developer audience — non-devs check out |
| **Customer support reply to an angry user** | High-stakes, binary "is this going to escalate?" diff, CONSTRAINTS naturally restrict tone | Less common audience need; harder to ship a viewer's "I'll use this tomorrow" moment |
| **Sales/outreach DM to a podcast host** | Similar to cold email but with creator-economy framing | Risks feeling samey if you've done other outreach content |
| **Bug report from a vague user complaint** | Strong before/after; PROCESS step (interview-style) shines because users always under-report context | Lower emotional stakes than a job email |

The 5 upgrades + 5 cliffhangers + master prompt template stay identical. Only the contents of the REFERENCES, EXAMPLES, and CONSTRAINTS blocks change.

## Suggested next videos (Phase 3 series)

1. **V014 — Context Engineering: The Skill That Replaced Prompt Engineering** (primary tease in this video's outro)
2. **V015 — Multimodal Prompting: Images, Screenshots & Audio in 2026** (secondary tease in the honest-scope beat at 23:00) — covers image region pointing, "describe-before-paste", screenshot-to-code, prompt design for image generation, and combining text + visuals without confusing the model
3. **V016 — Prompt Injection: How Attackers Hijack Your AI Agent (and How to Stop Them)** (nod in this video's CTA — "after that, how to stop prompt injection")
4. **V017 — DSPy in 15 Minutes: Stop Writing Prompts, Start Compiling Them**
