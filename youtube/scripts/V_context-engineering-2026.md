# Prompt Engineering Is Dead — Context Engineering Is the Job Now (2026)

**Full scene-by-scene script** — applies skills 01 (voice), 06 (title+thumbnail), 07 (hook-factory), 10 (description). Direct follow-up to V013 (Prompt Engineering Masterclass). **Adapted from a reference structure** (the 6-component context schema + 4 engineering levers) and rebuilt in Balaji's voice, on a real production example — the WBD Content Intelligence agent from V013. **One running example throughout:** a user asks the WBD agent a question, and we watch what has to fit into its context window for it to answer well — then how we engineer that.

> **Teaching style:** Senior-engineer crossover. "I write agents in production." The title is a provocation that pays off in the first 90 seconds — prompt engineering isn't *gone*, it got *absorbed*. The viewer who watched V013 feels the tension ("did he just contradict himself?") and stays for the resolution.

> **Structure (per Balaji's request):** Powerful hook → promise/preview → quick LLM reference (don't re-teach) → topics. **Deliberately cut:** the microservice analogy ramble (sub-agents collapsed to one line) and the repeated resources/"be economical" passes (one clean pass only).

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V014 |
| Slug | `context-engineering-2026` |
| Playlist | Phase 3 → Phase 6 bridge (Prompt Engineering → Memory & Context Engineering) |
| Target length | 15 min tight (hard cap 16) |
| Slot | Mon 7 PM IST |
| Previous video | V013 — *Prompt Engineering Masterclass* |
| Next video | *Memory — How Production Agents Remember Across Sessions* (tease at end) |

## Roadmap Mapping

```
- Phase: 3 (Prompt Engineering) closing out → Phase 6 (Memory & Context Engineering) opening
- Sections covered: 6.1 (context window as working memory),
                    6.2 (SYSTEM / CONTEXT / USER structure),
                    6.3 (short-term / session history),
                    6.6 (context compression / compaction),
                    plus 5.1–5.3 callbacks (tools, schemas, MCP) framed from the context angle
- Prerequisites: V013 (Prompt Engineering), API basics, How LLMs Are Built
- End state: viewer can name the 6 things competing for space in a context window,
            knows why more tokens ≠ better (lost-in-the-middle),
            and can apply 4 levers — system prompt, tool descriptions,
            smart retrieval (RAG → MCP), and long-horizon (compaction + memory) —
            to keep an agent reliable as it runs.
```

## Why this video (now)

| Reality (June 2026) | Script implication |
|---|---|
| Everyone who watched V013 now thinks "prompt = the whole skill." It isn't — the prompt is ~10% of what the model reads. | Title weaponises that gap. The hook pays it off honestly in 90s ("absorbed, not gone"). |
| "Context engineering" is the most-used phrase in agent circles in 2026 but almost no Telugu content explains the *anatomy* of a context window | Lead with the 6-component schema — the teaching diagram nobody in the niche draws |
| Beginners hear "million-token context" and assume space is solved | The 60–70% fill / lost-in-the-middle beat reframes it: more isn't better |
| Viewers asked "why MCP? why not just RAG?" after the agents teasers | Lever 3 answers it directly: RAG dumps, MCP describes-then-fetches |
| The reference video this was modelled on ends on a sponsor and rambles on a microservice analogy | Cut the ramble; replace the sponsor with our own CTA + memory cliffhanger |

## Playlist Callback Map (~25 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 0:15 | Backward bridge | V013 (Prompt Engineering) | "I taught you prompts last week — now the uncomfortable truth" |
| 2 | 1:30 | Backward bridge | V009 (How LLMs Are Built) | "Remember: stateless box, tokens in, tokens out" |
| 3 | 8:30 | Lean-in | V013 WBD email prompt | "That whole prompt you built? It lives in *one* of these six boxes" |
| 4 | 14:20 | Cliffhanger | V015 (Memory) | "Compaction and memory deserve their own video — that's next" |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–0:30 | **Hook — "prompt engineering is dead"** | Face cam, direct address; title word DEAD strikes through "Prompt Engineering" |
| 0:30–1:15 | Promise + preview (the 6 boxes + 4 levers, named) | Face cam → animated list |
| 1:15–1:45 | LLM reference (don't re-teach) — stateless box | Sketchbook: tokens in → box → tokens out |
| 1:45–6:30 | **PART 1 — The 6 things inside a context window** (the schema) | Sketchbook: one big box, 6 labelled regions filling in live |
| 6:30–7:30 | **The trap — more is not better** (model limits table → 60–70% sweet spot → lost-in-the-middle) | Model-limits table → fill meter → accuracy-vs-fill curve |
| 7:30–13:30 | **PART 2 — The 4 levers** (system prompt · tools+schemas · retrieval RAG→MCP · long-horizon compaction+memory) | Sketchbook + on-screen prompt/tool/JSON snippets |
| 13:30–14:25 | Recap — the schema + 4 levers in one frame | Full-screen sketchbook |
| 14:25–15:15 | CTA (comment "CONTEXT") + memory cliffhanger | Face cam → end screen |

## Model Context Limits — reference for the 6:30 on-screen table

> ⚠️ **Verify on record day.** Version numbers move monthly. Keep the spoken line rounded ("about a million," "around 200K") and let the graphic carry exact figures. The teaching point is the *pattern*, not the leaderboard: flagships advertise ~1M, deployable workhorses are smaller, and accuracy degrades well before the advertised ceiling.

| Model (mid-2026) | Advertised context | Note for the video |
|---|---|---|
| Gemini (2.5 / 3.x Pro) | 1M (up to 2M; 10M variants) | Largest advertised; Google tiers pricing ~2× above 200K |
| GPT-5.x | ~1M (some tiers 400K) | Flagship 1M club |
| Claude Opus 4.x | 1M (GA, up from 200K) | Jumped to 1M in 2026 |
| Claude Sonnet / Haiku | 200K | The "workhorse is smaller" point |
| GPT-5 mini / older | 128K | Cheapest tier, smallest window |
| Llama 4 Scout | 10M (advertised) | Headline number; degrades early |

**The defensible caveats (say at least one):**
- Multi-fact retrieval (MRCR-style benchmarks) degrades well before the limit — often past ~256K–512K tokens, even on 1M-token models.
- "Lost in the middle": models attend to the start and end, neglect the middle.
- Sweet spot ≈ 60–70% fill. Some providers charge ~2× above 200K — the pricing itself discourages maxing it out.

---

## 5 HOOKS (skill 07 — pick one on record day)

### HOOK A — Shock + Callback (RECOMMENDED)
> *"Last week I taught you prompt engineering. Five upgrades, one prompt. Now I'm going to say something that sounds like I lied to you. Prompt engineering is dead. [beat] Not gone — dead as the *whole* skill. In 2026 it got absorbed into something bigger. And here's the part that should scare you: that prompt you spent all that time building? It's about ten percent of what the model actually reads. Today I'll show you the other ninety percent — and why agents fail with a two-hundred-thousand-token context window. No black box."*
> [Visual: Face cam. On-screen title "PROMPT ENGINEERING" with a red strike-through, then "CONTEXT ENGINEERING" stamps in. Keep face cam dominant — this is a direct, confident address.]

### HOOK B — Production Incident
> *"This agent had a two-hundred-thousand-token context window. The user asked one normal question. It still gave the wrong answer. I opened the logs — the context was 90% full of junk it didn't need, and the one fact that mattered was buried in the middle where the model ignored it. That failure has a name. It's why prompt engineering alone isn't enough anymore."*
> [Visual: Terminal log scrolling → highlight the buried line → face cam.]

### HOOK C — Shock Statistic
> *"Give a model a hundred-thousand-token context window, fill it to the top, and your accuracy drops. Consistently. The sweet spot is around sixty to seventy percent. Nobody who says 'just use the big context window' tells you that. Today — why, and the four levers that actually control it."*
> [Visual: Accuracy-vs-context-fill curve, peak at ~65%.]

### HOOK D — Comment Callback
> *"After the agents teasers, this comment kept coming: 'Why do I need MCP? Why not just dump everything into RAG?' Today is the answer — and it's the whole reason context engineering replaced prompt engineering."*
> [Visual: Comment screenshot → face cam.]

### HOOK E — Question / Provocation
> *"You can paste a whole book into Gemini's context window now. So why do production agents still fail? Because filling a context window and *engineering* one are two completely different skills. Let me show you the difference."*
> [Visual: Face cam → sketchbook reveal of the empty context box.]

**Recommended:** HOOK A. It directly exploits the V013 → V014 continuity (every viewer who watched last week feels the "wait, did he contradict himself?" tension), lands the provocative title, and creates the strongest knowledge gap ("the other 90%"). The honesty turn — *dead as the whole skill, not gone* — is delivered within the same breath, so it never reads as clickbait.

---

## FULL SCRIPT

### HOOK — 0:00
**[VISUAL: Face cam. "PROMPT ENGINEERING" on screen, red strike-through, "CONTEXT ENGINEERING" stamps in.]**

> *"Last week I taught you prompt engineering. Five upgrades, one prompt. Now I'm going to say something that sounds like I lied to you. Prompt engineering is dead. [beat] Not gone — dead as the* whole *skill. In 2026 it got absorbed into something bigger. And here's the part that should scare you: that prompt you spent all that time building? It's about ten percent of what the model actually reads. Today I'll show you the other ninety percent — and why agents fail even with a two-hundred-thousand-token context window. No black box."*

---

### PROMISE + PREVIEW — 0:30
**[VISUAL: Face cam → animated list builds as he names each item.]**

> *"Let me be precise, because 'prompt engineering is dead' is the kind of line people say for clicks. I'm not saying writing a good prompt stopped mattering. I'm saying it stopped being the* job. *The job now is context engineering — deciding everything that goes into the model's window on every single call. The prompt is one slot inside it.*
>
> *So here's the plan. First, I'll show you the six things fighting for space inside a context window — most people only know about one of them. Then I'll show you why a bigger window does* not *fix this. And then the four levers you actually pull to engineer it: your system prompt, your tool descriptions, how you retrieve data — RAG versus MCP — and how you survive an agent that runs for a long time. Fifteen minutes. Same WBD agent we used last week as the example. Let's go."*

---

### LLM REFERENCE (don't re-teach) — 1:15
**[VISUAL: Sketchbook — `tokens in → [ box ] → tokens out`. Fast.]**

> *"One thing from the LLMs video, thirty seconds, because everything today rests on it. An LLM is a stateless box. Tokens go in, likely tokens come out. That's it. It does not remember your last call. It does not know your business. It only knows what it read on the internet during training.*
>
> *So if I want an agent that knows about WBD's content library and can actually do things — that knowledge has to be* placed *into the box, as tokens, every single time I call it. That pile of tokens I send in — that's the context window. And that is the thing we're going to engineer."*

---

## PART 1 — THE 6 THINGS INSIDE A CONTEXT WINDOW (1:45 – 6:30)

**[VISUAL: Sketchbook. Draw one big box labelled "CONTEXT WINDOW". Six regions get labelled and filled as he speaks.]**

> *"Let's make it concrete. A user opens our WBD Content Intelligence agent and asks: 'Which scripts mention the Marauder's Map, and summarise how it's described.' What has to fit inside the box for the model to answer that well? Six things. I'll fill them in one by one."*

### 1 — User message
> *"First, the obvious one. The user message. 'Which scripts mention the Marauder's Map.' This is the only box most people think about — the thing you type into ChatGPT. It's box number one of six."*

### 2 — System prompt
> *"Second, the system prompt. There is* always *one, even in ChatGPT — you just don't see it. It sets the personality and the rules. For our agent: 'You are a content intelligence assistant for a media company. Cite the asset ID for every claim. Never invent a title that isn't in the retrieved results.' You write this once. It rides along on every call."*

### 3 — Tools
> *"Third, tools. The whole point of an agent is that it can* do *things — search the vector database, query the catalog, send a result. So inside the context we include a* description *of every tool the model is allowed to call, and the schema — what goes in, what comes out. The model reads these descriptions to decide what to call. More on getting these right in a minute."*

### 4 — Resources (the retrieved data)
> *"Fourth — and this is the big one — resources. The model only knows the public internet. It has never seen WBD's private scripts, subtitles, or metadata. So we retrieve the relevant chunks and place them in the context. This is your private data, made visible to the model for this one call. It can be huge. We'll spend real time on this."*

### 5 — Assistant messages (the history)
> *"Fifth, assistant messages. The model's own previous replies. In a back-and-forth, every answer it gave gets fed back in so it knows what it already said. The longer the conversation runs, the more space this eats."*

### 6 — Tool calls + results (the history)
> *"Sixth, the history of tool calls and their results. As the agent works, it might search, get fifty chunks back, search again. Each of those calls and results piles up inside the context too."*

**[VISUAL: All six regions now filled. Three of them — assistant messages, tool history, resources — flagged with a small "GROWS ↑" arrow.]**

> *"Six boxes. And notice — three of them grow as the agent runs: the resources you keep pulling, the assistant replies, the tool results. That prompt I taught you to build last week — the whole ROLE, CONTEXT, REFERENCES masterpiece? It lives inside* one *of these. The system prompt box. That's what I mean when I say it got absorbed. It's one-sixth of the picture."*

---

## THE TRAP — MORE IS NOT BETTER (6:30 – 7:30)

**[VISUAL: Model-limits table fades in (GPT-5 / Claude Opus / Gemini ~1M; Sonnet/Haiku 200K; mini models 128K). Then a fill meter on the box, then an accuracy-vs-fill curve peaking around 65%.]**

> *"Now you're thinking: fine, just use a model with a giant window. In 2026 that's easy — GPT-5, Claude Opus, Gemini all advertise a million tokens. Gemini pushes two million; some variants claim ten. Sounds like space is solved. It isn't. Two reasons.*
>
> *One — the models you'll actually deploy on are often smaller. Claude Sonnet, Haiku, the mini models — a lot of them still sit at two hundred thousand, even a hundred and twenty-eight thousand tokens. Add up six boxes with three of them growing, and that fills fast.*
>
> *Two — and this is the part nobody tells you — filling the window* hurts *you. The benchmarks are consistent: multi-fact retrieval starts breaking down long before the limit, often past two-to-five-hundred-thousand tokens — even on the million-token models. The model attends to the start and the end and gets lazy in the middle. They call it 'lost in the middle.' The sweet spot is roughly sixty to seventy percent full. The providers know it — Google literally charges you about double once you cross two hundred thousand tokens. The pricing is a hint: don't live up there. I'm simplifying, and the version numbers will have moved by the time you watch this — but the direction is rock solid. More context is not better context. That's exactly why we engineer what goes in. Four levers."*

---

## PART 2 — THE 4 LEVERS (7:30 – 13:30)

### LEVER 1 — Engineer the system prompt (7:30)
**[VISUAL: Sketchbook — a dial with "TOO VAGUE" on one end, "TOO PRESCRIPTIVE" on the other, sweet spot in the middle.]**

> *"Lever one — the system prompt. Yes, this is prompt engineering. It didn't die; it moved into this box, and it's still the highest-leverage thing you write once. There's a Goldilocks problem here.*
>
> *Too vague — 'do a good job, get what you need' — useless. Too prescriptive is the mistake* engineers *make. If you find yourself writing if-this-then-that logic in your system prompt — 'if the user asks X, first do Y, then check Z' — stop. That's you doing the model's job. Define the* outcome *and the broad approach, and let the model figure out the path. That's what it's good at. Outcomes, not flowcharts. That's the art."*

### LEVER 2 — Describe your tools well (8:30)
**[VISUAL: A tool definition on screen — name, one-line description, input schema, output schema.]**

> *"Lever two — tools. This answers a question a lot of you asked: why does tool design even matter? Because the model picks tools by* reading their descriptions. *If the description is vague, it calls the wrong one, or doesn't call it at all.*
>
> *Two rules. One — be specific and tight. 'search_scripts: semantic search over WBD script chunks; returns top-k passages with asset IDs.' Not a paragraph. Specific, not long. Two — always include the schema. What goes in, what comes out. The model needs to know it has the right inputs before it'll call the tool, and it needs to know the output shape, because that output is often the* input *to its next step. Specific description, full schema. That's the whole lever."*

### LEVER 3 — Retrieve data intelligently: RAG → MCP (9:45)
**[VISUAL: Left — "RAG: dump matching docs in." Right — "MCP: describe what's available → model asks → fetch only that."]**

> *"Lever three — getting the right data into the resources box. This is where most of your tokens go, so this is where context engineering really lives.*
>
> *The first approach everyone used was RAG. Vector database, index your documents, take the user message, retrieve anything that looks similar, dump it into the context. For a search chatbot, that works — and if it's in your stack, keep it. I'm not calling you old-fashioned. But RAG by itself is* imprecise. *It pulls everything that sounds related, and remember — stuffing the window hurts you.*
>
> *So here's the upgrade, and this is why MCP exists. With the Model Context Protocol, resources are* described, *like tools are — a bit of text, maybe some query parameters. Those descriptions are cheap; they cost few tokens. So on one call, the model just sees what's* available. *Then you ask it: based on this question, which resources do you actually need? It tells you. You go fetch* only those, *and put them in the next call. Describe, then fetch what's needed — instead of dump-everything-and-hope.*
>
> *Same trick for big records. If a user object is long, don't paste it — pass a user ID and a tool that expands it. Let the model ask for the full record only if it needs it. You're trading a cheap pointer for an expensive payload, and only paying when it matters."*

### LEVER 4 — Long-horizon: compaction + memory (11:30)
**[VISUAL: Sketchbook — the three "GROWS ↑" boxes, now with two tools pointed at them: "COMPACT" and "MEMORY (key → value)".]**

> *"Lever four — for agents that run a long time and make many calls. Remember the three boxes that grow — resources, assistant messages, tool results? Over a long run, those are your enemy. Two tools keep them in check.*
>
> *First, compaction. LLMs are incredible at summarising. Say a previous step pulled a fifty-thousand-token document. I don't want all of that riding along in every future call. So I make one separate LLM call — 'summarise this in five hundred words' — and carry the summary forward instead of the raw text. Compact the past, keep moving.*
>
> *Second, memory. This is just a key-value store sitting beside the agent. Some intermediate result — a big chunk of JSON, a long assistant message — I don't need it in the window* right now, *but I'll need it in three steps. So I stash it under a key, out of the context, and pull it back only when the moment comes. The window stays lean; the data waits cheaply on the side. And if a chunk of your agent gets complex enough — like the whole retrieval-and-ranking step — you split it into its own sub-agent that hands back a clean summary. One line: decompose, return less."*

**[VISUAL: Note — keep the sub-agent point to a single sentence. No microservice analogy. No second pass over resources.]**

---

## RECAP (13:30 – 14:25)
**[VISUAL: Full-screen sketchbook — the six-box schema on the left, the four levers listed on the right.]**

> *"That's the whole model. The context window holds six things: the user message, the system prompt, your tools, your resources, the assistant history, and the tool-call history. All of it has to fit — and these windows are not getting much bigger, while three of those boxes keep growing.*
>
> *So you engineer it with four levers. Get the system prompt right — outcomes, not flowcharts. Describe your tools precisely, with schemas. Retrieve data intelligently — describe with MCP, fetch only what's needed, instead of dumping with RAG. And for long runs, compact the past and offload to memory.*
>
> *That's context engineering. The prompt is still in there — it's lever one. It just isn't the whole job anymore."*

---

## CTA + CLIFFHANGER (14:25 – 15:15)
**[VISUAL: Face cam → end screen with next-video thumbnail + subscribe.]**

> *"If this reframed how you think about your agent — comment the word CONTEXT, I read them and I answer. And if you're building something with this, especially something that runs for a long time, tell me what's eating your context window. I'll cover the real cases on the live.*
>
> *One box I rushed today on purpose — memory. I made it sound like a simple key-value store. In production it's a whole skill: what to remember, what to forget, how the agent recalls the right thing three sessions later. Your agent forgetting you between conversations versus remembering you — that's the next video. Subscribe so it reaches you. Step by step. See you there."*

---

## Retention Devices Map

| Device | Time | Purpose |
|---|---|---|
| Provocative title payoff ("dead, not gone") | 0:00–0:45 | Resolve the V013 contradiction tension fast → keep the loyal viewer |
| "The other 90%" open loop | 0:25 | Knowledge gap that only closes at the recap |
| One running example (WBD agent) | throughout | Zero context-switching cost; production credibility anchor |
| Six-box diagram filling live | 1:45–6:30 | Visual progress bar; viewer wants to see all six |
| "More is NOT better" reversal | 6:30 | Counterintuitive beat → re-engages anyone drifting at minute 7 |
| "Why MCP?" comment payoff | 9:45 | Directly answers a known audience question |
| Memory cliffhanger | 14:10 | Binge nudge into V015 |

## Skill Compliance Checklist

- [x] 01 voice — direct "you"/`manam`, English tech terms preserved, one signature phrase ("no black box" in hook, "step by step" in outro — not both early), no "guys", no greeting, short declarative lines
- [x] 06 title+thumbnail — see brief below
- [x] 07 hook-factory — 5 hooks across rotation, recommended pick justified, <30s, knowledge gap, visual specified
- [x] 10 description — to be generated from final SRT after record
- [x] No paid pitch (Confluent plug from source removed entirely)
- [x] Production example, not toy; honesty markers used ("I'm simplifying", "the number will keep moving")
- [x] Cuts applied per request: microservice ramble → one line; resources repetition → single clean pass

## Title + Thumbnail Brief (for skill 06 / tracker)

- **Primary title:** `Prompt Engineering Is Dead. Context Engineering Is the Job Now.`
- **Alt A:** `Why Prompt Engineering Is Already Obsolete (Context Engineering 2026)`
- **Alt B:** `I Taught You Prompts. Now Forget Half of It — Context Engineering`
- **Thumbnail:** "PROMPT ENGINEERING" struck through in red, "CONTEXT ENGINEERING" stamped over it; Balaji pointing at a context-window diagram with the 6 boxes; highlight word **DEAD**.
- **Telugu badge:** కంటెక్స్ట్ ఇంజినీరింగ్
- **Honesty guardrail:** body must land "absorbed, not gone" by 0:45 so title ≠ clickbait.

## Suggested next videos

1. **V015 — Memory: How Production Agents Remember Across Sessions** (primary tease here) — episodic vs long-term, key-value vs vector, mem0/Zep, when memory becomes a privacy problem
2. **V016 — Lost in the Middle: Reranking & Context Ordering That Actually Works**
3. **V017 — Prompt Injection: How Attackers Hijack Your Agent Through the Context Window**
