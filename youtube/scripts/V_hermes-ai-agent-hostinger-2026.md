# I Built an AI Agent That Runs My Life on My Own Server (Hostinger Hermes, No Black Box)

**Full scene-by-scene script** — SPONSORED integration with Hostinger (Hermes Agent VPS). Dedicated tutorial-style video. ~30 min. One running story: *"I gave an AI agent a real job — running my mornings, my calendar, and my freelance teaching prep."* Three escalating demos, all built live, all on my own self-hosted server.

> **Teaching style:** Senior AI engineer building in real time. Demo-first. Direct address to one viewer. English technical terms preserved, Telugu delivery. The agent is the hero; Hostinger is the thing that removes the friction so anyone can follow.

> **⚠️ SPONSORSHIP:** This is a paid partnership with Hostinger. Disclosure is verbal (Scene 1) + YouTube "paid promotion" toggle + first line of the description. Coupon + tracking link spoken in Scene 1 teaser callout AND in the close, and pinned at the top of the description. Title must be sent to Caio for approval BEFORE recording. Final cut delivered ≥ 2 business days before publish.

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0XX (sponsored special — confirm next number against `video-metadata-tracker.md`) |
| Slug | `hermes-ai-agent-hostinger-2026` |
| Sponsor | Hostinger — product: **Hermes Agent** (one-click Docker, VPS) |
| Deal | $2,000 fixed + 40% affiliate commission + personalized 10% coupon |
| Playlist | AI Engineer Roadmap 2026 (Phase 5 — Agents, applied) |
| Target length | 30–33 min (hard cap 34) |
| Slot | confirm with Hostinger; deliver final ≥ 2 business days before publish |
| Coupon code | `BALAJI` (placeholder — confirm exact code with Caio) |
| Tracking link | (placeholder — Caio sends after title approval) |

## Roadmap Mapping

- **Phase 5 — Agents (applied):** what an autonomous agent actually is, memory, skills, tool-calling, scheduled (cron) autonomy
- **Prerequisites:** *What are AI Agents*, *Working with API*, basic comfort with the idea of an LLM
- **End state:** viewer can deploy a self-hosted, always-on AI agent on their own server, connect it to Telegram + Google Calendar, and have it do real recurring work — with zero local install and (almost) no code

## Why this video, now

| Reality (verified June 2026) | Script implication |
|---|---|
| Hermes Agent (Nous Research) crossed 100k+ GitHub stars in weeks — self-improving, builds its own skills, persistent memory | Lead the hook on "it remembers and improves" — the one thing ChatGPT can't do for you |
| Hostinger is the only major host with a one-click Hermes Docker template (~6 min, no terminal commands to deploy) | This is the "removes friction" story Hostinger's brief asks for — show the time-lapse |
| Hermes connects to Telegram / WhatsApp / Discord in gateway mode | Mobile-first payoff — huge for the audience; "control your agent from your phone" |
| KVM2 (8 GB RAM) is the practical minimum for Hermes | Pricing scene recommends KVM2 + longer term honestly, not the cheapest plan |
| Hermes can browse the web, run code, schedule cron jobs | Enables all three demos without external glue for demos 1 & 3 |
| Google Calendar needs a real API connection (service-account JSON / OAuth) | Featured "real engineer" segment — done on a throwaway test Google account for safety |

## Hostinger Brief Compliance Map (DO NOT SKIP ANY)

| Brief requirement | Where it lands in this script |
|---|---|
| 1. Hook: why audience needs this + why Hostinger | Scene 1 (demo) + Scene 3 (what Hermes is / why self-host / why Hostinger) |
| 2. Show product landing page + why over alternatives | Scene 3 (comparison table vs ChatGPT/Claude/Codex/n8n/OpenClaw) + Scene 4 (landing page proof) |
| 3. Pricing section, pick plan, recommend longer period | Scene 5 |
| 4. Purchase process + where to enter coupon | Scene 6 |
| 5. Practical steps of using the product | Scenes 7–13 (the whole build) |
| Tutorial-style, not feature overview | Entire structure is build-along |
| Promote agreed product (Hermes) | Hermes is the product the whole video |
| Coupon + tracking link spoken verbally + top of description | Scene 1 callout + Scene 14 close + description |

---

## FINAL HOOK — The "It Did This While I Slept" Cold Open (LOCKED draft — needs your approval)

**On screen:** Phone screen recording, Telegram. Three messages land one after another, ~1 sec apart, with the notification buzz:

1. 🔔 *"Good morning Balaji. Top 3 AI stories today: …"*
2. 🔔 *"Your day: 2 meetings. Freelance class at 6 PM — topic: Python OOP."*
3. 🔔 *"I drafted your OOP lesson outline + 3 examples. Want me to send it?"*

Then cut to face cam.

**Spoken (face cam, calm, slightly amused):**

> I did not write any of these messages. An AI agent did — this morning, while I was asleep.
>
> It read the news. It read my calendar. And it saw I have a freelance class at 6 PM on Python OOP — so it went and prepared the lesson for me.
>
> This is not ChatGPT in a browser tab. This agent runs 24/7 on **my own server**. It remembers everything I teach it. And in the next 30 minutes, **step by step**, I'm going to build the whole thing with you — start to finish, almost no code.
>
> *(beat)* And full honesty before we start — this video is sponsored by Hostinger, who make the deploy part take six minutes instead of an afternoon. I'll show you exactly how, and there's a coupon at the end. Let's build.

**[Disclosure done in <30s, demo-first, no greeting, no "in this video we'll cover". Brief hook requirement satisfied honestly.]**

---

## SCENE 1 — HOOK (0:00 – 1:10)

Locked above. Real phone, real Telegram, three real messages from the agent you'll build. Disclosure + coupon tease folded in.

---

## SCENE 2 — THE PROBLEM WITH YOUR CURRENT AI (1:10 – 3:00)

**On screen:** Split — left, ChatGPT window; right, three problem cards drawn/animated as you say them.

**Spoken:**

> Be honest. The AI you use today has three problems.
>
> **One — it forgets.** Every new chat, you re-explain who you are, what you do, your style. It has no memory of you.
>
> **Two — it can't run on its own.** Close the tab and it's dead. It can't wake up at 7 AM and do something for you.
>
> **Three — it lives on someone else's computer.** Your prompts, your data, your context — all on their servers.
>
> Today we fix all three. We're going to run an agent that **remembers**, that **works while you sleep**, and that lives on a server **you** control. The agent is called **Hermes** — open source, built by Nous Research. By the end you'll have your own.

---

## SCENE 3 — WHAT IS HERMES, AND HOW IS IT DIFFERENT? (3:00 – 5:30) | the understanding scene

**On screen:** Build this comparison table row-by-row as you speak (one column lights up at a time). Keep it on screen the whole scene.

| Tool | What it really is | Remembers you? | Runs 24/7 on its own? | Lives on |
|---|---|---|---|---|
| ChatGPT / Claude (app) | A chat assistant you open and ask | Barely (limited memory) | No — you must open it | Their servers |
| Claude Code / Codex | A coding agent in your terminal | Per-project only | No — runs when you call it | Their cloud + your machine |
| n8n | Visual workflow automation | No — you wire every step | Yes, but **you** are the brain | Your server |
| OpenClaw | Self-hosted assistant on your messaging apps | Some | Yes (messaging) | Your server |
| **Hermes** | **Self-improving autonomous agent** | **Yes — persistent memory** | **Yes — schedules itself** | **Your server** |

**Spoken:**

> Before we build, one minute on what Hermes actually is — because it is **not** ChatGPT, and that difference is the whole point.
>
> **ChatGPT, Claude** — you open them, you ask, they answer, you close them. They react. They mostly forget you. And they run on someone else's computer.
>
> **Claude Code, Codex** — those are coding agents. They write code in your terminal when you call them. Brilliant at that — but they're not a personal assistant that lives on your phone and runs your day.
>
> **n8n** — that's automation. You drag boxes and wire every step yourself. Powerful, but *you* are the brain. Hermes can even trigger n8n, but it's a different thing.
>
> The closest one to Hermes is **OpenClaw** — also self-hosted, also on your messaging apps. Genuinely a good option, same Hostinger one-click. The difference is one word: **learning**. Hermes is a self-improving agent — it builds its own skills from experience and keeps a memory that grows. OpenClaw is more "assistant on your channels." Hermes is "an agent that gets *better* the more you use it."
>
> So Hermes is the only one that's all four at once: it **remembers you**, it **works on its own**, it **improves itself**, and it **lives on your server**. That last part matters — an agent that runs 24/7 can't live on your laptop, because your laptop sleeps. It needs a small always-on computer in the cloud. That's a **VPS**.
>
> And setting up a VPS for an agent normally means Docker, Nginx, SSL, a wall of terminal commands — which is where most people quit. Hostinger removed that wall with a **one-click Hermes template**: click deploy, six minutes, done. That's the only reason I can teach this in 30 minutes instead of three hours. Let me show you.

**[Honesty markers: credit OpenClaw fairly (not a strawman), and name the real friction — Docker/Nginx/SSL — before crediting Hostinger for removing it. Keep the table on screen; talk fast over it.]**

---

## SCENE 4 — LANDING PAGE: SEE IT FOR YOURSELF (5:30 – 6:45) | Brief #2

**On screen:** Live on `hostinger.com/vps/docker/hermes-agent`. Scroll slowly. Highlight the exact words that prove the table from Scene 3: "self-improving", "builds skills", "persistent memory", "Telegram/Discord/Slack/WhatsApp", "your own infrastructure".

**Spoken:**

> Don't take my word for the comparison — it's on the page. This is the Hermes Agent page on Hostinger. Read it: **self-improving**, creates its own **skills** from experience, **persistent memory**. That's the row that beats ChatGPT.
>
> It connects to Telegram, WhatsApp, Discord, Slack — so you talk to it from your phone. And everything stays on **your** server.
>
> Why here and not the other hosts? Two reasons. One — this one-click template barely exists anywhere else; you'd build it by hand. Two — it's the cheapest honest way to get an always-on agent with dedicated RAM. I tested it. It works.

---

## SCENE 5 — PRICING: PICK THE PLAN (6:15 – 8:00) | Brief #3

**On screen:** Pricing table on the page. Cursor hovers each plan. Land on **KVM2**. Then show the term selector (1 / 12 / 24 months) and the per-month price dropping.

**Spoken:**

> Pricing. Don't grab the cheapest one — Hermes needs memory. The agent wants around **8 GB of RAM**, so the plan you want is **KVM2**. That's the sweet spot — enough to run the agent plus a Telegram gateway without choking.
>
> One real tip that saves you money: look at the term. The **longer the period you pick, the lower the monthly price** — the 24-month plan is far cheaper per month than monthly billing. If you're going to run an always-on agent, you'll want it for more than a month anyway, so the longer term is genuinely the better deal. I'm picking KVM2 on the longer term.

**[Brief: must recommend longer periods. Done — framed as honest value, not pressure.]**

---

## SCENE 6 — CHECKOUT + COUPON (8:00 – 9:30) | Brief #4

**On screen:** Checkout page. Zoom hard on the **coupon / promo code field**. Type the code. Show the total drop by 10%.

**Spoken:**

> Checkout. Right here — this is the part most sponsored videos rush, and it's the part that saves you money. There's a coupon box. Type **`BALAJI`** *(confirm code)* right here, and you get an **extra 10% off** on top of the plan price. Watch the total drop. *(it drops)*
>
> Same code, same link in the description — I'll repeat it at the end so you don't have to scrub back. Complete the purchase, and during checkout the **Hermes Agent app is already pre-selected** for one-click install. That's the magic part — coming up next.

---

## SCENE 7 — ONE-CLICK DEPLOY (9:30 – 12:00)

**On screen:** hPanel → VPS dashboard → Docker Manager → Catalog → search "Hermes Agent" → Select. Show the deploy form: it asks for an **LLM API key** (OpenRouter / Anthropic / OpenAI). Paste key. Click **Deploy**. **Time-lapse** the ~6-minute build (progress bar → "running"). Lower-third counts: "0 terminal commands so far."

**Spoken:**

> Now the part I promised. We're inside Hostinger's dashboard. Docker Manager, Catalog, search **Hermes Agent**, Select.
>
> It asks for one thing — an **API key** for your LLM. This is the brain of your agent. You can use OpenRouter, Anthropic, or OpenAI. I'll use OpenRouter — it gives you access to many models with one key. Paste it. Deploy.
>
> *(time-lapse)* That's it. Hostinger is now building the whole server — Docker, the Hermes container, and HTTPS through Traefik — automatically. About six minutes. Count the terminal commands I typed: **zero.** This is the wall that used to stop people, and it's just… gone.

**[On-screen overlay when done: ✅ Server live · HTTPS auto · 0 commands typed]**

---

## SCENE 8 — FIRST CONTACT: SETUP WIZARD (12:00 – 14:00) | start of "practical steps" (Brief #5)

**On screen:** VPS dashboard → **Browser Terminal**. Run the three setup lines on screen (read them out, they're in English):

```
cd /docker/hermes-agent-xxxx/
docker compose exec -it hermes-agent /bin/bash
hermes setup
```

Then the wizard: pick provider (OpenRouter) → pick model.

**Spoken:**

> Server's up. One small setup step — and this is the only place we touch a terminal, and Hostinger gives us a **browser terminal** so there's nothing to install.
>
> Three lines. Go into the project folder. Step into the container. Then — `hermes setup`. That starts a wizard.
>
> It asks which provider — I pick **OpenRouter**. Then which model. For an agent that plans and writes, I'll pick a solid general model — I'll tell you exactly which in the description so you can copy me. Confirm, and Hermes is alive.

**[Honesty: don't hide the terminal — frame it as 3 lines, in-browser, copy-paste. Anti-pattern blocklist: no happy-path lie.]**

---

## SCENE 9 — CONNECT TELEGRAM (14:00 – 16:00)

**On screen:** Telegram → @BotFather → /newbot → copy token. Back in Hermes, enable gateway / paste token. Start the gateway. Send first message from phone → agent replies. Show the phone.

**Spoken:**

> Now let's get it on your phone. Open Telegram, message **@BotFather**, create a new bot, copy the token. Give that token to Hermes, start the **gateway**.
>
> Watch. *(types on phone)* "Hey, who are you?" *(agent replies on screen)* There it is. My agent. On my phone. Running on my own server. This already feels different from a browser tab.
>
> And here's the move most people miss — *(types)* "Remember: I'm Balaji. I teach freelance Python and AI classes in the evenings. My style is no-jargon, example-first." It just **saved that to memory.** Hold that thought — it pays off in demo three.

**[Plants the memory thread. Callback in Scene 12.]**

---

## SCENE 10 — DEMO 1: MORNING AI NEWS BRIEF (16:00 – 19:30)

**On screen:** Phone/Telegram. Ask the agent to research today's AI news and summarize. Show it browsing (or the result). Then schedule it daily (cron). Show the schedule confirmation.

**Spoken:**

> First real job. *(types)* "Every morning at 7 AM, search the web for the top 3 AI news stories, summarize each in two lines, and message me here."
>
> Watch it work — it goes out, **browses the web**, comes back with a clean digest. That alone is useful. But the magic is the next word: **schedule.** It just set up a recurring job — a cron — on the server.
>
> So tomorrow at 7 AM, without me opening anything, this lands on my phone. The agent works while I sleep. That's the whole promise of this video, demo one done.

**[Demo 1 = web browse + cron. Rock-solid, no external auth. Good confidence builder before the harder demo.]**

---

## SCENE 11 — DEMO 2: GIVE IT YOUR CALENDAR (Google API, JSON + OAuth) (19:30 – 24:30) | FEATURED ENGINEER SEGMENT

**On screen:** Google Cloud Console on a **TEST Google account** (clearly labeled "test account — not my real data"). Steps, shown cleanly:
1. Create project → enable **Google Calendar API**
2. Create credentials → **OAuth consent (test user)** + download **`credentials.json`** (or a **service account** + JSON key, shared to the test calendar)
3. Upload the JSON to the agent / give it the key as a Hermes skill
4. Authorize once (OAuth token) → agent reads the test calendar

Then: ask the agent to read today's events and plan the day → it messages a plan to Telegram.

**Spoken:**

> Demo two is the one I'm most excited about, and it's a real engineering skill, not a toy. I want the agent to read my **calendar**. For that, it needs permission from Google — properly, the way you'd do it in production.
>
> I'm doing this on a **throwaway test Google account** — never wire your real calendar on camera, and you shouldn't either until you trust the setup.
>
> Step by step. In Google Cloud Console, I create a project, and enable the **Google Calendar API**. Then I create credentials — I download a **JSON key** file. This file is the agent's ID card to Google.
>
> I give that JSON to Hermes as a skill, authorize once — that's the **OAuth token** — and now the agent can read the calendar. *(types)* "Read today's events and plan my day into a task list, then message me." *(plan lands on phone)*
>
> *(honesty marker)* This is the fragile part — if your JSON scope is wrong, it fails. I'll put the exact steps and scopes in the description so yours works first try. This is "**no black box**" — you now know how an agent actually connects to the outside world.

**[⚠️ HIGHEST RISK ON CAMERA. Must be fully rehearsed. Keep the JSON key off-screen / blurred. Use test account only. Have a recorded backup take of the working result in case live auth misbehaves.]**

---

## SCENE 12 — DEMO 3: IT PREPS MY FREELANCE CLASS (24:30 – 28:00) | THE CLIMAX

**On screen:** A calendar event on the test calendar: "6 PM — Freelance class: Python OOP". The agent notices the topic, pulls from the memory/skill you taught it in Scene 9, and drafts a teaching outline + examples. Message lands. Open it — show a genuinely usable lesson outline.

**Spoken:**

> Now everything connects. Remember in scene… I told the agent who I am and that I teach. And it can read my calendar. So watch what happens when those two combine.
>
> There's a class on my calendar tonight — topic, **Python OOP**. *(types)* "Look at my calendar, find today's class, and using my teaching style, prepare a lesson outline with three beginner examples."
>
> *(message lands — open it)* Look at this. It pulled the topic **from my calendar**, used the style **from its memory**, and wrote a lesson plan I can actually teach. It didn't just answer a question — it **did my prep work**. This is the difference between a chatbot and an agent. It remembers, it has access, and it does the job.

**[Payoff of the memory thread + the calendar connection. This is the "share this video" moment.]**

---

## SCENE 13 — COST + IS IT SAFE (28:00 – 29:30)

**On screen:** Hermes cost/usage tracking + Hostinger billing. Show real, small numbers.

**Spoken:**

> Two fair questions. **What does it cost?** Two parts — the server, which is the Hostinger plan we picked, and the model usage, which Hermes tracks right here. For this kind of personal use it's small — I'll show you my actual numbers.
>
> **Is it safe?** Your keys and data sit on **your** server, not a third party. Keep your API keys and tokens private, never paste them in a public place. That's the trade — a little setup, full control.

---

## SCENE 14 — RECAP + CTA + COUPON (29:30 – 31:00) | Brief: verbal link + coupon

**On screen:** Three-up recap cards (News / Calendar plan / Lesson prep). Then description-link card + coupon code big on screen + WhatsApp QR.

**Spoken:**

> Let's recap what you just built. An agent that — one, sends you the morning news. Two, reads your calendar and plans your day. Three, prepares your actual work for you. All on your own server, all from your phone, almost no code.
>
> If you want to build this yourself, the link is in the description, and the coupon **`BALAJI`** *(confirm)* gives you an **extra 10% off** — both are pinned at the top of the description. Use the longer plan, it's cheaper per month.
>
> Tell me in the comments — what's the **first job** you'd give your agent? I read every comment. If this unlocked something, subscribe so the next build reaches you. See you in the next one.

---

## RETENTION MAP (planning lens)

| Time | Beat | Why it holds |
|---|---|---|
| 0:00–1:10 | 3 real messages from the agent + disclosure | Payoff before tutorial; honesty buys trust |
| 1:10–3:00 | The 3 problems with your current AI | Names the viewer's pain |
| 3:00–5:30 | **What is Hermes** vs ChatGPT/Claude/Codex/n8n/OpenClaw + why self-host | The understanding scene — "now I get what this is" |
| 5:30–6:45 | Landing page proves the comparison | Product = the differentiator |
| 6:15–9:30 | Plan pick + coupon + checkout | Brief-required, kept short |
| 9:30–12:00 | One-click deploy time-lapse, "0 commands" | The friction-removed wow |
| 12:00–16:00 | Setup + Telegram + plant memory | Mobile payoff + sets up climax |
| 16:00–19:30 | Demo 1: morning news + cron | First "works while I sleep" win |
| 19:30–24:30 | Demo 2: Google Calendar via JSON/OAuth | Real engineering depth — credibility |
| 24:30–28:00 | Demo 3: preps the class (climax) | Memory + calendar payoff — share moment |
| 28:00–29:30 | Cost + safety | Removes the last objection |
| 29:30–31:00 | Recap + coupon + comment CTA | Close + algorithm fuel |

**Highest-risk drop-off:** Scenes 6–8 (checkout + terminal). Mitigation — keep checkout under 90s, frame the terminal as "3 copy-paste lines in the browser," cut fast to the first Telegram reply.

**Highest-risk on camera:** Scene 11 (Google OAuth/JSON). Mitigation — full rehearsal on the test account, exact scopes in description, recorded backup take of the working result.

---

## TITLE OPTIONS (⚠️ SEND TO CAIO FOR APPROVAL BEFORE RECORDING)

1. **I Built an AI Agent That Runs My Life (On My Own Server) — 2026** ⭐ recommended
2. This AI Agent Reads My Calendar and Does My Work — Self-Hosted in 2026
3. I Gave an AI Agent a Job (and It Never Sleeps) — Hermes Setup 2026
4. Stop Using ChatGPT in a Tab — Build a 24/7 AI Agent on Your Own Server
5. My AI Agent Wakes Up Before Me — Hermes + Hostinger Step by Step (2026)

**Final pick:** #1 — but Hostinger approves the title before any work starts (their requirement).

---

## THUMBNAIL BRIEF

**Layout:** 60/40 split, you on the right (chest-up, looking at the phone with a "wait, it did that?" reaction).

**Left side — phone mockup** with two stacked Telegram bubbles:
- TOP bubble (green): *"Top 3 AI news today…"*
- BOTTOM bubble (green): *"Prepared your 6 PM class ✅"*

**Center badge:** glowing **24/7** ring + small **"ON YOUR OWN SERVER"** chip.

**Title text bar (2 lines max):**
> MY AI AGENT
> **RUNS MY LIFE**

**Color rules:** follow `youtube/skills/03-visual-identity/THUMBNAIL_RULES.md`. Keep Hostinger logo OFF the thumbnail unless Caio requires it (cleaner CTR; confirm in brief).

---

## SHORTS HOOKS (3 candidates, ≤45s each — cut from the long video)

1. **"It prepped my class while I slept"** — open on the 3 Telegram messages, end on the lesson outline. "Built on my own server, link below."
2. **"ChatGPT forgets. This doesn't."** — the 3 problems, then the memory line. Provocative, 1 idea.
3. **"6 minutes, 0 commands"** — the one-click deploy time-lapse with the "0 commands typed" counter.
4. **"ChatGPT vs Claude Code vs Hermes — what's the difference?"** — the Scene 3 comparison table, one row at a time, end on "Hermes is the only one that remembers, runs itself, and improves." Strong search-intent Short.

---

## RECORD-DAY CHECKLIST (assets + pre-tests)

**Accounts / access (from Hostinger):**
- [ ] Hostinger VPS access with Hermes plan provisioned (request from Caio)
- [ ] Personalized **coupon code** confirmed (replace `BALAJI` placeholder everywhere)
- [ ] **Tracking link** received (Caio sends after title approval) — put in description
- [ ] Title approved by Caio in writing

**The agent:**
- [ ] OpenRouter (or chosen) API key ready; note exact model name for description
- [ ] Telegram bot created via @BotFather; token ready; gateway tested
- [ ] Memory line pre-tested ("Remember: I'm Balaji, I teach…")
- [ ] Demo 1 (news + cron) verified end-to-end
- [ ] Cron schedule confirmation visible on screen

**Google Calendar segment (HIGH RISK — rehearse twice):**
- [ ] **Throwaway test Google account** created (no real data)
- [ ] Google Cloud project + **Calendar API enabled**
- [ ] Credentials: OAuth consent (test user) OR service account + **JSON key** downloaded
- [ ] Correct **scopes** noted (read calendar) — write them into the description
- [ ] JSON given to Hermes as a skill; OAuth authorized once; read verified
- [ ] Test calendar seeded with today's events + a **"6 PM Freelance class: Python OOP"** event
- [ ] **Backup recorded take** of the working calendar read (insurance if live auth fails)
- [ ] JSON key / tokens kept OFF-SCREEN or blurred in edit

**Edit:**
- [ ] Sponsorship disclosure on screen (Scene 1) + YouTube "paid promotion" toggle ON
- [ ] Coupon + link on-screen lower-third in Scene 6 and Scene 14
- [ ] Time-lapse the 6-min deploy
- [ ] Blur any API keys, tokens, IPs, JSON contents

---

## DESCRIPTION + TAGS + PINNED COMMENT

Generate after recording via `youtube/skills/10-description-generator/SKILL.md`, using the published transcript. **Hard requirements (Hostinger brief):** tracking link + coupon must be in the **first lines** of the description. Pull WhatsApp/roadmap links from `links.config.md`.

---

## NOTES TO SELF (from prep)

- This is the **first sponsorship** — over-deliver on the brief, send the script to Caio (he said he likely won't request changes if he sees the script first), and deliver the final cut ≥ 2 business days early.
- Keep the voice honest: name the real friction (Docker/SSL) before crediting Hostinger for removing it. Audience trusts earned praise, not ad-read praise.
- The Google Calendar JSON/OAuth segment is the credibility centerpiece for the AI-engineer audience — but it's also the thing most likely to break live. Rehearse it cold, twice, and keep the backup take.
- Don't say "no black box" AND "step by step" in the first 5 seconds — earn them. "Step by step" is used in Scene 1, "no black box" in Scene 11. One each, deliberately.
- Confirm the exact model and exact coupon before locking the description.
- Adding the Scene 3 explainer pushes total to ~31–33 min. If you need to recover time, trim Scene 6 (checkout) and Scene 13 (cost) — both can lose 20–30s without hurting the brief. Don't cut the explainer; understanding what Hermes is drives the whole video.
- Keep the OpenClaw comparison fair on camera — viewers respect honest "this alternative is also good, here's the difference" more than fake superiority, and Hostinger sells OpenClaw too.
