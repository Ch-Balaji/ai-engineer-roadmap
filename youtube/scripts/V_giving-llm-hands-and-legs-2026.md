# How to Give an LLM Hands and Legs — Tool Calling From Scratch (2026)

**Full scene-by-scene video script** — applies skills 01 (voice), 02 (story-bank), 04 (roadmap-source), 06 (title+thumbnail), 07 (hook-factory), 09 (monetization-runway), 10 (description). Phase 5 opener — the jump from "LLM that talks" to "LLM that acts."

> **Teaching style locked:** L1 analogy → L2 plain story → L3 name the term → L4 one step deeper (code/production) → L5 honest "saved for later". One running story holds the whole video: *we adopt a genius trapped in a jar and, upgrade by upgrade, turn it into an assistant that can actually do things.*

> **Source notebook:** `Masai Pandas/content/Module_3/04_ai_agents/04_ai_agents_fundamentals.ipynb` — this script teaches that notebook end to end. Notebook changes required before record are listed in the **Notebook Changes** section at the bottom.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V036 (Phase 5) — may absorb the V035 Phase-5 opener slot |
| Slug | `giving-llm-hands-and-legs` |
| Playlist | Phase 5 — From Retrieval to Action: Tools & Agents |
| Target length | 30–38 min (capstone-style — full build, one notebook) |
| Slot | Wed/Fri 7 PM IST |
| Previous video | V010 — *The Brain in a Windowless Room* (callback: same brain, new problem) · V008 — *asyncio / retries* (callback: retry + backoff) |
| Next video | Phase 5.2 — *MCP & multi-tool agents* (cliffhanger plan below) |

## Roadmap Mapping

```
- Phase: 5 — From Retrieval to Action (Tools, Function Calling, Single Agents)
- Sections covered: 5.1 (tool / function calling) + agent-loop intro
- Prerequisites: API basics (V_calling-openai), system/user/assistant roles,
                 JSON, retries + backoff (V008)
- Capstone contribution: yes — the agent loop is reused in every later agent video
- End state: viewer can take ANY Python function, describe it as a tool,
            let the LLM decide to call it, run it, feed the result back,
            and wrap the whole thing in a safe autonomous loop.
```

## Why this video (now)

| Reality | What it means for the script |
|---|---|
| Beginners think ChatGPT's web search / code interpreter = "the model can do things" | The #1 misconception to break in Scene 3: those are app features bolted on, not model abilities |
| The raw API gives you ONLY the brain — no tools at all | The "empty jar" demo is the hook payoff that motivates the whole build |
| Every agent framework (LangChain, LangGraph, OpenAI Agents SDK, MCP) is sugar over `messages → tool_calls → run → feed back` | "No black box" — we build the loop by hand once, frameworks make sense forever |
| The LLM never executes anything — it only emits text/JSON asking YOU to run a function | This is THE mental model; everything in the video serves it |

## Playlist Callback Map (4 references, ~30 sec total)

| # | Time | Type | Target | Why |
|---|---|---|---|---|
| 1 | 0:55 | Backward bridge | *The Brain in a Windowless Room* | Same brain — last time it couldn't SEE today, today it can't ACT |
| 2 | 3:30 | Lean-in | *What Are AI Agents* (resume agent demo) | "Remember that agent? This is the engine inside it" |
| 3 | 22:00 | Backward bridge | V008 — asyncio retries + backoff | Safety section reuses exactly that skill |
| 4 | 34:00 | Cliffhanger | Phase 5.2 — MCP / multi-tool agents | Next-video pull |

## Visual / Production Plan

| Time | Scene | Medium |
|---|---|---|
| 0:00–1:30 | **Cold open — the helpless brain (live weather fail)** | Mac + notebook, live API call → wrong/refused answer → face cam |
| 1:30–3:30 | Chatbot vs Agent (talker vs doer) | Sketchbook — two diagrams |
| 3:30–6:30 | **"But ChatGPT already has tools?!"** — product vs raw brain | Split: ChatGPT.com tools vs raw API empty-handed |
| 6:30–13:00 | First hand — `get_weather` + the big secret | Mac + notebook, 4 visible steps, LIVE Open-Meteo |
| 13:00–17:00 | The menu (JSON schema) + second hand (calculator) | Sketchbook (menu card) + notebook |
| 17:00–22:00 | The loop — letting it work unsupervised | Notebook — `run_agent`, 4 test questions |
| 22:00–26:00 | Safety — retry, backoff, hard stop | Sketchbook + notebook, force a failure live |
| 26:00–33:00 | **Finale — CSV Analyst (first real job)** | Notebook — plain-English questions over a dataset |
| 33:00–35:00 | Recap (Brain + Tools + Loop) + cliffhanger | Sketchbook full-screen → face cam |

## Title + Thumbnail Brief (skill 06)

```
- Title formula: T8 (From X to Y) + concrete metaphor
- Final title: How to Give an LLM Hands and Legs (Tool Calling From Scratch, 2026)
- Alt A/B titles:
    1. Your LLM Is a Brain in a Jar — Here's How to Set It Free (2026)
    2. Tool Calling Explained — How an LLM Actually "Does" Things (2026)
    3. From Chatbot to Agent — The One Loop That Changes Everything
    4. The LLM Never Runs Your Code. So How Do Agents Work? (2026)
- Subject pose: holding a glass jar with a glowing "brain", reaching a robotic hand out of it
- Outfit: brown bomber jacket + black zip-up (locked)
- Background: black + circuit overlay + warm rim light upper-right
- Primary text (white, Anton ALL CAPS, left): BRAIN IN A JAR
- Highlight text (yellow + brush band, right, BIG): GIVE IT HANDS
- Telugu badge (red, bottom-right): "LLM ki చేతులు ఇద్దాం"  (translation: "let's give the LLM hands")
- Tech-stack icons (bottom): gpt-4o-mini · Open-Meteo · Python · JSON
```

---

## COLD OPEN — THE HELPLESS BRAIN (LOCKED)

> *[Open on a Jupyter notebook, dark theme, one cell visible. A plain chat call to `gpt-4o-mini` — no tools, nothing special. Code font ≥18pt.]*
>
> **Spoken:**
>
> "Watch this. I'll ask the smartest model in the world one simple question.
>
> **[Run the cell: `What's the weather in Hyderabad right now?` — plain API call, no tools.]**
>
> Look at the answer. It's either making something up, or it's politely telling me it has no idea. This model has read the entire internet. It can write code, pass exams, explain quantum physics. And it **cannot tell me if it's raining outside.**
>
> **[Cut to face cam.]**
>
> Here's the truth nobody says out loud. An LLM is a **genius brain trapped in a sealed jar.** It read everything humanity wrote — but months ago, and then the lid was closed. It has no eyes to see today. No hands to do anything. No phone to call the outside world. It can only *think* and *talk.*
>
> Today, we open the jar. We give this brain **hands and legs** — the ability to actually reach out and do things in the real world. By the end of the next thirty minutes, this exact same brain will check live weather, do real math, and analyze a real dataset — and it will decide, on its own, when to do each. Step by step. No black box. Let's go."

---

## SCENE 1 — CHATBOT vs AGENT: TALKER vs DOER (1:30 – 3:30) | L1 analogy → L3 name

**On screen:** Sketchbook. Draw the two diagrams from the notebook (Part 1) live — fast.

**Spoken:**

> So what do we actually have right now? A **chatbot.** You ask, it thinks, it answers. One shot. Done. It never *does* anything.
>
> **[Draw box 1: You → LLM thinks → LLM answers. Full stop.]**
>
> Think of a friend who gives amazing advice but never lifts a finger. "You should book that ticket." "You should check that file." Great advice. But *you* still have to do everything.
>
> What we want is an **agent.**
>
> **[Draw box 2: You → LLM thinks → LLM picks a tool → tool runs → result goes back → loop until done.]**
>
> An agent is an assistant who actually opens the laptop, runs the thing, reads the result, and comes back with the real answer. Same brain. But now it can *act.*
>
> And an agent is just three parts. Remember these — the whole video hangs on them.
>
> **[Write: 🧠 BRAIN + 🔧 TOOLS + 🔄 LOOP]**
>
> The **brain** — that's the LLM. We already have it. The **tools** — those are the hands; the functions it can call. And the **loop** — that's letting it work on its own until the job is done. We have the brain. Today we build the hands and the loop.

**[Retention beat: "But wait — doesn't ChatGPT already do this? It searches the web. Hold that thought, because the answer is the most important idea in this video."]**

---

## SCENE 2 — "BUT CHATGPT ALREADY HAS TOOLS?!" (3:30 – 6:30) | L2 reframe — the misconception killer

**On screen:** Split. Left: ChatGPT.com running a live web search / code interpreter. Right: a raw API call in the notebook that visibly *can't*.

**Spoken:**

> Let me answer the question you're already shouting at the screen. "Balaji, what are you talking about? I use ChatGPT every day. It **searches the web.** It **browses links.** It **runs Python.** It **makes images.** That brain doesn't sound very trapped."
>
> **[Show ChatGPT.com doing a live web search.]**
>
> You're right that ChatGPT does all of that. But here's what almost nobody realizes. **Those tools are not part of the brain.** OpenAI's engineers *built* them — a web search, a code interpreter, a browser — and **bolted them onto the ChatGPT app.**
>
> So the ChatGPT you use every day isn't just a model. It's already an **agent.** Brain, plus a team of pre-built hands, plus a loop. Someone built those hands for you. You just never saw it happen.
>
> Now watch what you *actually* get when you call the model directly — the way a developer does.
>
> **[Switch to notebook. Run a plain API call: "Search the web and tell me today's top news headline."]**
>
> Nothing. It can't. It refuses, or it invents a headline from months ago. **This is the real LLM. Naked. No web search. No browser. No hands.** ChatGPT was the dressed-up version the whole time.
>
> So why are we building tools by hand? Two reasons. **One** — the raw API gives you nothing, so if you want powers, *you* attach them. **Two, and this is the big one** — you can give it hands ChatGPT will *never* have. ChatGPT can't touch **your** database. **Your** company's internal API. **Your** CSV file. But the assistant *you* build can.
>
> And here is the secret that makes all of this click — say it with me — **a tool is just a function call.** ChatGPT's fancy web search? Underneath, it is literally someone's code calling a search API and handing the result back to the brain. That's it. If you can write a Python function, you can give an LLM hands. Let me prove it — with the simplest hand of all.

**[Retention beat: viewer's biggest misconception is dead; they now NEED to see how a plain function becomes a "hand".]**

---

## SCENE 3 — THE FIRST HAND: `get_weather` + THE BIG SECRET (6:30 – 13:00) | L4 — the heart of the video

**On screen:** Notebook. Build in four visible steps. The weather call is **live** (Open-Meteo, no key).

**Spoken:**

> We're going to give the brain one hand: the ability to check the weather. And I'm going to do it in four steps you can see.
>
> **Step one — write the hand.** A tool is just a normal Python function. Nothing magic.
>
> **[Show `get_weather(city)` — real Open-Meteo call. Run it ourselves.]**
>
> ```python
> get_weather("Hyderabad")
> # → 'Hyderabad, India: 31.2°C, humidity 54%, wind 8.3 km/h.'
> ```
>
> That's live. Real coordinates, real current weather, no API key. When *I* call it, it works. But the LLM can't call Python. So how does the brain use this?
>
> **Here's the secret — the single most important idea in this video.** The LLM **still cannot run anything.** It can only output text. So it doesn't *run* the function — **it just asks YOU to.** It writes a little note, in JSON: "please call `get_weather` with `city='Hyderabad'`." *Your* code is the actual hand that runs it. Then you pass the answer back through the bars of the jar.
>
> **[Sketchbook, 4 boxes:]**
> ```
> LLM writes: call get_weather(city="Hyderabad")   ← it only ASKS
>      ↓
> OUR code runs get_weather("Hyderabad")            ← we are the hands
>      ↓
> we send the result back to the LLM                ← back through the bars
>      ↓
> LLM uses the result to write the final answer     ← now it can talk about today
> ```
>
> **Step two — hand the brain the menu** so it knows this tool exists. (We'll dissect the menu format in a second — for now, just watch.)
>
> **Step three — ask the question, and watch what the LLM does.**
>
> **[Run the single tool-call cell with the weather question. Print `finish_reason`, `content`, `tool_calls`.]**
>
> ```
> finish_reason: tool_calls      ← NOT "stop"
> content:       None            ← it didn't answer...
> tool_calls:    get_weather(city="Hyderabad")   ← ...it asked for a hand
> ```
>
> Look at this. `finish_reason` is **`tool_calls`**, not `stop`. The content is **`None`** — the brain did not answer. Instead it raised its hand and said "I need the weather tool first." This is the brain reaching through the bars.
>
> **Step four — we run the hand and pass the result back.**
>
> **[Run the tool, append the `tool` message with `tool_call_id`, call the LLM again.]**
>
> ```
> 🔧 running get_weather(city='Hyderabad')
> 📤 result: Hyderabad, India: 31.2°C, humidity 54%, wind 8.3 km/h.
> 🤖 final answer: It's currently 31°C in Hyderabad with 54% humidity and a light breeze.
> ```
>
> Now go back to the cold open. Same question. Same brain. The *only* thing we added was one hand — and the jar just touched the real world, **live, on camera.** That is tool calling. Everything else today is just more hands and a loop around this exact dance.

**[CTA hint — skill 09, Phase 1, ≤15 sec, single line, no pitch.]**

> If you want me to look at your code or your resume, the form's in the description. Now — back to that menu I skipped.

---

## SCENE 4 — THE MENU: JSON SCHEMA + A SECOND HAND (13:00 – 17:00) | L3 name + L4 code

**On screen:** Sketchbook (restaurant menu) → notebook (`tools` schema + add `calculate`).

**Spoken:**

> One question I skipped — how did the brain even *know* `get_weather` existed? I never showed it the Python code. I showed it a **menu.**
>
> **[Sketchbook: draw a menu card.]**
>
> The LLM never sees your functions. You hand it a menu — in a format called a **JSON schema.** Each item has a name, a description of what the dish does, and what you need to order it — the parameters.
>
> **[Notebook: show the `tools` schema for `get_weather`.]**
>
> The brain reads this menu, decides which dish it wants, and tells you the order. Our code is the kitchen that actually cooks it. The `description` matters more than beginners think — that sentence is *how* the model decides when to reach for this tool. Write it badly, and the model orders the wrong dish.
>
> Now let's put a **second hand** on the menu — a calculator. Why? Because the brain is a famously bad calculator. Ask it `1547 * 23 + 89` and it'll confidently get it slightly wrong. A tool fixes that — not by making the brain smarter, but by letting it *delegate.*
>
> **[Add `calculate` function + its schema. Two tools now on the menu.]**
>
> So now our assistant has two hands — eyes for the weather, and a calculator for exact math. Which raises the obvious question: if it has two hands, **how does it know which one to use?** And do we really have to run each tool by hand, every time, ourselves? No. That's the loop.

---

## SCENE 5 — THE LOOP: LETTING IT WORK UNSUPERVISED (17:00 – 22:00) | L4 — autonomy

**On screen:** Notebook — build `run_agent`, then run four test questions.

**Spoken:**

> So far, *I* ran the tool by hand — I checked `finish_reason`, I ran the function, I passed the result back. That's babysitting. A real assistant shouldn't need it.
>
> The fix is one small loop. In plain English:
>
> **[Sketchbook:]**
> ```
> while not done:
>     ask the LLM
>     if it says "I'm done"        → return the answer
>     if it says "use a tool"      → run the tool, feed the result back, repeat
> ```
>
> That's the entire engine inside every AI agent on Earth. Let me build it.
>
> **[Show `run_agent` with `max_steps`. Then run four questions.]**
>
> Now watch it *choose.*
>
> - **[Math question]** → it reaches for the calculator.
> - **[Weather question]** → it reaches for the weather tool.
> - **[`"weather in Delhi and Bangalore, which is cooler?"`]** → it calls the weather tool *twice*, then compares — multiple steps, on its own.
> - **[`"What is Python?"`]** → it uses **no tool at all.** It just answers.
>
> *That* decision — when to reach for a hand and when to just talk — is the line between a script and an agent. We didn't write any `if weather: ... elif math: ...`. The brain decides. We just hold the tools.

**[Retention beat: "This works beautifully on the happy path. Now let me show you how it explodes in production — and the three lines that save it."]**

---

## SCENE 6 — SAFETY: RETRY, BACKOFF, HARD STOP (22:00 – 26:00) | L4 production reality

**On screen:** Sketchbook (3 safety nets) → notebook. Force a failure live.

**Spoken:**

> We just told an AI to run code, in a loop, unsupervised. **What could possibly go wrong?**
>
> Three things, all the time, in production. The API rate-limits you. The network blips. Or the model gets stuck calling tools in circles and never stops — and that loop is now spending your money.
>
> Three safety nets. You met two of them back in the asyncio video — same skill, new place.
>
> **[Sketchbook table:]**
> | Net | What it does | Like |
> |---|---|---|
> | **Retry** | try again on failure | redialing a busy phone |
> | **Backoff** | wait longer each time — 1s, 2s, 4s | not hammering a busy line |
> | **Hard stop** | quit after N steps | "can't finish in 5 tries? stop and tell me" |
>
> **[Notebook: show `call_llm_with_retry` with exponential backoff, then `run_safe_agent` with `max_steps`.]**
>
> **[Force a failure live — bad key or rate limit — show the retries firing, the backoff waiting, then succeeding or hard-stopping cleanly.]**
>
> Without the hard stop, a confused agent loops forever and burns your budget at 3 AM. Without retry, one network hiccup kills the whole task. Without backoff, your retries just get you rate-limited faster. Three small ideas. This is the difference between a demo and something you'd actually ship.

---

## SCENE 7 — FINALE: THE CSV ANALYST (FIRST REAL JOB) (26:00 – 33:00) | L4 — the payoff

**On screen:** Notebook — load a dataset, give the agent 3 data tools, ask plain-English questions.

**Spoken:**

> Our assistant has a brain, hands, a loop, and safety rules. Time for its **first real job.**
>
> Here's a dataset — employees, departments, salaries, cities. And here are **three new hands**: one to list the columns, one to get statistics on a column, one to count rows matching a condition.
>
> **[Show the 3 CSV tools + schemas + the `csv_analyst` agent — same loop as before, different menu.]**
>
> Notice — it's the **exact same loop** from Scene 5. Only the menu changed. That's the whole point: once you have the engine, new powers are just new functions.
>
> Now I'm going to talk to a spreadsheet in plain English.
>
> **[Run, narrating each tool call as it appears:]**
> - *"What's the average salary?"* → it calls `get_stats('salary')` → answers.
> - *"How many people work in Engineering, and who are they?"* → `filter_count` → names + count.
> - *"Which department pays more — Engineering or Marketing, and by how much?"* → it plans, calls stats **twice**, subtracts, answers.
>
> Watch the trace — **plan, call a tool, read the result, decide if it needs another, then answer.** No SQL. No pandas. No `if` statements from me. You just *talked to your data.* That's an agent doing a real job.

---

## SCENE 8 — RECAP + CLIFFHANGER (33:00 – 35:00) | L5 + next-video pull

**On screen:** Sketchbook full-screen, then face cam.

**Spoken:**

> Remember the brain in the jar from the start? It couldn't tell us if it was raining. Look at it now. It checks **live weather.** It does **exact math.** It **analyzes a real dataset.** And it decides, by itself, which hand to use for which job.
>
> **[Sketchbook: 🧠 BRAIN + 🔧 TOOLS + 🔄 LOOP = AGENT]**
>
> Brain plus tools plus loop. That's it. That's an agent. Every framework you'll ever hear about — LangChain, LangGraph, the OpenAI Agents SDK, MCP — is just a fancier wrapper around this exact loop you now understand from scratch. No black box.
>
> And remember that resume agent I showed you in the *What Are AI Agents* video? **This** is the engine that was running inside it the whole time.
>
> One last thing. Right now, *we* wrote every tool by hand. But what if tools could be shared — what if your agent could plug into a library of hands someone else already built? Your database, GitHub, your file system, Slack — all as ready-made tools? That's a new standard called **MCP**, and that's the next video. See you in the next one.

---

## YouTube Description (draft — run skill 10 on final SRT)

```
An LLM is a genius brain trapped in a jar. It can't check the weather, do exact math, or touch your data. In this video we give it hands and legs — tool calling, from scratch, no framework.

What you'll learn:
• Why the raw API gives you ONLY the brain — and why ChatGPT's web search isn't part of the model
• The one idea that makes tool calling click: the LLM never runs your code, it just ASKS you to
• Build a real tool (live weather, no API key) and watch the LLM call it
• JSON schemas — the "menu" the model reads to pick a tool
• The agent loop — the engine inside every AI agent
• Safety: retry, exponential backoff, and hard stops
• Finale: an agent that answers plain-English questions about a dataset

🗺️ Roadmap: Phase 5 — From Retrieval to Action
Previous: The Brain in a Windowless Room
Next: MCP & Multi-Tool Agents
Full Roadmap: https://ch-balaji.github.io/ai-engineer-roadmap/

📂 Code:
Repo: roadmap-2026-v036-tool-calling
- 04_ai_agents_fundamentals.ipynb

#AIEngineer #LLM #ToolCalling #AIAgents #2026
```

---

## Companion Code (key cells — full build lives in the notebook)

### The cold-open "helpless brain" cell (no tools)
```python
from openai import OpenAI
client = OpenAI()

r = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's the weather in Hyderabad right now?"}],
)
print(r.choices[0].message.content)
# It either refuses or invents a number — it has no way to know.
```

### The first hand — REAL weather, no API key (Open-Meteo)
```python
import requests

def get_weather(city: str) -> str:
    """Get the CURRENT, LIVE weather for a city. No API key needed."""
    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1}, timeout=10,
    ).json()
    if not geo.get("results"):
        return f"Could not find a city called '{city}'."
    place = geo["results"][0]
    lat, lon = place["latitude"], place["longitude"]
    name = ", ".join(p for p in [place.get("name"), place.get("country")] if p)

    w = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"},
        timeout=10,
    ).json()
    c = w["current"]
    return (f"{name}: {c['temperature_2m']}°C, "
            f"humidity {c['relative_humidity_2m']}%, "
            f"wind {c['wind_speed_10m']} km/h.")

print(get_weather("Hyderabad"))  # live
```

### The single tool-call — watch it ASK (not answer)
```python
import json

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current, live weather for any city. Use whenever the user asks about weather.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "City name, e.g. 'Hyderabad'"}},
            "required": ["city"],
        },
    },
}]

messages = [
    {"role": "system", "content": "You are a helpful assistant. Use tools when needed."},
    {"role": "user", "content": "What's the weather in Hyderabad right now?"},
]

resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)
choice = resp.choices[0]
print("finish_reason:", choice.finish_reason)     # → tool_calls
print("content:      ", choice.message.content)   # → None
print("tool_calls:   ", choice.message.tool_calls)
```

### Run the hand, feed it back, get the live answer
```python
available_tools = {"get_weather": get_weather}

tc = choice.message.tool_calls[0]
args = json.loads(tc.function.arguments)
print(f"🔧 running {tc.function.name}({args})")
result = available_tools[tc.function.name](**args)
print("📤 result:", result)

messages.append(choice.message)                       # the assistant's tool request
messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})

final = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)
print("🤖", final.choices[0].message.content)
```

> The agent loop (`run_agent`), the safety wrapper (`run_safe_agent` with retry + backoff + hard stop), and the CSV-analyst finale are the existing notebook cells (Parts 7, 8, 9) — they run unchanged on top of the code above.

### `requirements.txt`
```
openai>=1.55.0
python-dotenv>=1.0.0
requests>=2.31.0
```

---

## CapCut Edit Cues

| Time | Cue | Asset |
|---|---|---|
| 0:00 | Cold-open cell runs | Zoom-sticker on the refused / made-up weather answer |
| 0:40 | "brain in a sealed jar" | Animated jar graphic over face cam |
| 3:30 | Split screen | ChatGPT.com web search (left) vs raw API empty answer (right) |
| 5:20 | "a tool is just a function call" | Big yellow lower-third — the key line |
| 9:00 | `finish_reason: tool_calls` / `content: None` | Red box around both lines, "it ASKED, it didn't answer" caption |
| 12:30 | Cold-open callback | Side-by-side: same question, before (jar) vs after (live answer) |
| 18:30 | "What is Python? → no tool" | Caption: "it CHOSE not to use a tool" |
| 23:00 | Force a live failure | Red `RETRY` / `BACKOFF 2s` stickers as they fire |
| 31:00 | CSV trace | Highlight each tool call line as it appears |
| 33:30 | Brain + Tools + Loop = Agent | Full-screen equation graphic |
| End screen | Next video | Phase 5.2 MCP + Phase 5 playlist |

---

## Retention Map

| Time | Beat | Purpose |
|---|---|---|
| 0:00 | Smartest model can't tell the weather | Curiosity + relatable fail from frame 1 |
| 0:40 | "brain in a jar" metaphor named | Mental anchor for the whole video |
| 3:30 | "ChatGPT already has tools" reframe | Kills the #1 objection, shareable insight |
| 5:20 | "a tool is just a function call" | The unlock line |
| 9:00 | `tool_calls` / `content: None` reveal | The core mechanism, made visible |
| 12:30 | Cold-open payoff — live weather | Loop closed, dopamine hit |
| 18:00 | Agent CHOOSES tools (incl. none) | "this is what makes it an agent" |
| 23:00 | Live failure + recovery | Production credibility |
| 31:00 | Talk to a spreadsheet in English | Money-shot finale |
| 34:00 | Engine-inside-the-resume-agent callback + MCP tease | Binge nudge |

---

## Skill Compliance Audit

| Skill | Compliance |
|---|---|
| 01 voice | No "guys". Direct "you". English jargon preserved (`tool calling`, `JSON schema`, `finish_reason`, `agent loop`, `backoff`). Signature phrases used sparingly: "no black box" (Scene 2 + recap), "step by step" (cold open). Short declarative sentences. |
| 02 story-bank | No canon career story used (technical tutorial). Running metaphor (brain in a jar) is original to this video, not a STORY_ entry. |
| 04 roadmap-source | Phase 5 / 5.1. Prereqs: API basics, roles, retries. Cliffhanger to 5.2 (MCP). |
| 06 title+thumbnail | T8 (From X to Y) + metaphor. Brief locked above. |
| 07 hook-factory | Live-demo-first hook (tutorial default) fused with the jar metaphor. Lands < 30s. |
| 09 monetization | Phase 1 — single ≤15-sec description hint after Scene 3, no pitch. |
| Anti-patterns | No greeting/throat-clear. Real failure shown live (Scene 6). Build-from-scratch before any framework name. Real (not toy) weather data. |

---

## Pre-Record Checklist

- [ ] Re-run the whole notebook top to bottom (`Restart & Run All`) — confirm every cell succeeds in order
- [ ] `OPENAI_API_KEY` loaded from `.env` (notebook currently reads `os.getenv('openaiapikey')` — confirm the env var name matches your `.env`)
- [ ] **Open-Meteo live** on record day — run `get_weather("Hyderabad")` and 2–3 other cities; confirm real numbers (no key needed, but verify network/firewall)
- [ ] Cold-open cell genuinely fails/refuses on `gpt-4o-mini` — capture the exact output (if the model hedges instead of refusing, tweak the prompt to make the helplessness obvious)
- [ ] Single tool-call cell shows `finish_reason='tool_calls'`, `content=None` clearly on camera
- [ ] Force one real failure for Scene 6 (temporary bad key or low rate limit) and confirm retry/backoff fire visibly, then restore the good key
- [ ] CSV-analyst questions return correct numbers (spot-check `get_stats('salary')` and the Eng-vs-Marketing diff by hand)
- [ ] Notebook font ≥18pt, dark theme, outputs cleared before recording, secrets not visible on screen
- [ ] Sketchbook templates pencilled: chatbot-vs-agent, the 4-box "it only asks" diagram, the menu card, the 3 safety nets, the Brain+Tools+Loop equation
- [ ] Thumbnail brief sent / image prompt run
- [ ] End screen: Phase 5.2 (MCP) + Phase 5 playlist

---

## Notebook Changes Required (before record)

These are the edits to `04_ai_agents_fundamentals.ipynb` that make it match this script. (Do these in the next step after script approval.)

1. **Add a cold-open section** at the very top: a markdown "brain in a jar" cell + a no-tools cell that asks the weather and visibly fails. (New — supports Scene 0/1.)
2. **Make `get_weather` real** via Open-Meteo geocoding + forecast (code above), replacing the hardcoded `fake_weather` dict. The whole metaphor depends on actually reaching the real world. (Edits Part 4 cell.)
3. **Add the "ChatGPT vs raw API" markdown** explaining product-vs-brain + "tools are just calls." (New — supports Scene 2.)
4. **Lead the single-call demo with the weather question**, not math. Keep the math/`calculate` example as the *second* hand introduced right after (Scene 4). (Reorders Part 6.)
5. **Thread one named assistant** through the section headers ("Upgrade 1: give it eyes", "Upgrade 2: …") so the notebook reads as one journey, matching the running story. (Markdown-only edits.)
6. **Reframe Part 9** header as "The assistant's first real job" and add 1–2 callback lines to the cold-open question. (Markdown-only.)
7. Confirm the API-key line (`os.getenv('openaiapikey')`) matches the `.env` convention used elsewhere in the repo.

---

*v1 — 30–38 min target — Phase 5 opener — teaches `04_ai_agents_fundamentals.ipynb` end to end. Record, edit aggressively, run `10-description-generator` on the final SRT for the upload package.*
