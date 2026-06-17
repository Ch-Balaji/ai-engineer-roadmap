# Video Script — For Review

| | |
|---|---|
| **Working title** | I Built an AI Agent That Runs My Life (On My Own Server) — 2026 |
| **Creator** | Balaji Chippada |
| **Channel** | AI Engineer Roadmap 2026 |
| **Format** | Tutorial-style build-along (not a feature overview) |
| **Target length** | 30–33 minutes |
| **Sponsor** | Hostinger — Hermes Agent (one-click Docker VPS) |
| **Coupon code** | `BALAJI` *(pending confirmation)* |
| **Tracking link** | *(pending — to be added to description after title approval)* |

---

## Summary

A senior AI engineer builds a self-hosted Hermes agent from scratch — deploy on Hostinger, connect to Telegram, and run three real jobs: a daily AI news brief, a Google Calendar day planner, and automatic prep for a freelance teaching class. The video opens with the finished result (three Telegram messages the agent sent overnight), then walks the viewer through the full setup step by step. Sponsorship is disclosed verbally in the first 30 seconds and flagged as paid promotion on YouTube.

---

## Sponsor Integration

| Moment | What happens |
|---|---|
| **0:00–1:10** | Hook demo + verbal sponsorship disclosure + coupon tease |
| **3:00–5:30** | Hermes vs alternatives; why self-hosting needs a VPS; Hostinger one-click template removes Docker/SSL friction |
| **5:30–6:45** | Live walkthrough of the Hermes Agent landing page on Hostinger |
| **6:15–9:30** | Pricing (KVM2 recommended, longer term = better value) + checkout with coupon code entered on screen |
| **9:30–12:00** | One-click deploy time-lapse (~6 min, zero terminal commands) |
| **12:00–28:00** | Full practical setup and three live demos on the deployed server |
| **29:30–31:00** | Recap + tracking link + coupon repeated verbally; both pinned at top of description |

**Disclosure:** Verbal in hook · YouTube "Includes paid promotion" toggle ON · Sponsor link + coupon in first lines of description

---

## Script

### HOOK — 0:00

*[On screen: phone screen recording. Three Telegram messages arrive in sequence.]*

1. "Good morning Balaji. Top 3 AI stories today: …"
2. "Your day: 2 meetings. Freelance class at 6 PM — topic: Python OOP."
3. "I drafted your OOP lesson outline + 3 examples. Want me to send it?"

*[Cut to face cam.]*

I did not write any of these messages. An AI agent did — this morning, while I was asleep.

It read the news. It read my calendar. And it saw I have a freelance class at 6 PM on Python OOP — so it went and prepared the lesson for me.

This is not ChatGPT in a browser tab. This agent runs 24/7 on my own server. It remembers everything I teach it. And in the next 30 minutes, step by step, I'm going to build the whole thing with you — start to finish, almost no code.

And full honesty before we start — this video is sponsored by Hostinger, who make the deploy part take six minutes instead of an afternoon. I'll show you exactly how, and there's a coupon at the end. Let's build.

---

### THE PROBLEM — 1:10

Be honest. The AI you use today has three problems.

One — it forgets. Every new chat, you re-explain who you are, what you do, your style. It has no memory of you.

Two — it can't run on its own. Close the tab and it's dead. It can't wake up at 7 AM and do something for you.

Three — it lives on someone else's computer. Your prompts, your data, your context — all on their servers.

Today we fix all three. We're going to run an agent that remembers, that works while you sleep, and that lives on a server you control. The agent is called Hermes — open source, built by Nous Research. By the end you'll have your own.

---

### WHAT IS HERMES — 3:00

Before we build, one minute on what Hermes actually is — because it is not ChatGPT, and that difference is the whole point.

ChatGPT, Claude — you open them, you ask, they answer, you close them. They react. They mostly forget you. And they run on someone else's computer.

Claude Code, Codex — those are coding agents. They write code in your terminal when you call them. Brilliant at that — but they're not a personal assistant that lives on your phone and runs your day.

n8n — that's automation. You drag boxes and wire every step yourself. Powerful, but you are the brain. Hermes can even trigger n8n, but it's a different thing.

The closest one to Hermes is OpenClaw — also self-hosted, also on your messaging apps. Genuinely a good option, same Hostinger one-click. The difference is one word: learning. Hermes is a self-improving agent — it builds its own skills from experience and keeps a memory that grows. OpenClaw is more "assistant on your channels." Hermes is "an agent that gets better the more you use it."

So Hermes is the only one that's all four at once: it remembers you, it works on its own, it improves itself, and it lives on your server. That last part matters — an agent that runs 24/7 can't live on your laptop, because your laptop sleeps. It needs a small always-on computer in the cloud. That's a VPS.

And setting up a VPS for an agent normally means Docker, Nginx, SSL, a wall of terminal commands — which is where most people quit. Hostinger removed that wall with a one-click Hermes template: click deploy, six minutes, done. That's the only reason I can teach this in 30 minutes instead of three hours. Let me show you.

---

### LANDING PAGE — 5:30

*[On screen: hostinger.com/vps/docker/hermes-agent]*

Don't take my word for the comparison — it's on the page. This is the Hermes Agent page on Hostinger. Read it: self-improving, creates its own skills from experience, persistent memory. That's the row that beats ChatGPT.

It connects to Telegram, WhatsApp, Discord, Slack — so you talk to it from your phone. And everything stays on your server.

Why here and not the other hosts? Two reasons. One — this one-click template barely exists anywhere else; you'd build it by hand. Two — it's the cheapest honest way to get an always-on agent with dedicated RAM. I tested it. It works.

---

### PRICING — 6:15

*[On screen: pricing table. Cursor lands on KVM2. Term selector shown.]*

Pricing. Don't grab the cheapest one — Hermes needs memory. The agent wants around 8 GB of RAM, so the plan you want is KVM2. That's the sweet spot — enough to run the agent plus a Telegram gateway without choking.

One real tip that saves you money: look at the term. The longer the period you pick, the lower the monthly price — the 24-month plan is far cheaper per month than monthly billing. If you're going to run an always-on agent, you'll want it for more than a month anyway, so the longer term is genuinely the better deal. I'm picking KVM2 on the longer term.

---

### CHECKOUT + COUPON — 8:00

*[On screen: checkout page. Coupon field highlighted. Code entered. Total drops.]*

Checkout. Right here — this is the part most sponsored videos rush, and it's the part that saves you money. There's a coupon box. Type BALAJI right here, and you get an extra 10% off on top of the plan price. Watch the total drop.

Same code, same link in the description — I'll repeat it at the end so you don't have to scrub back. Complete the purchase, and during checkout the Hermes Agent app is already pre-selected for one-click install. That's the magic part — coming up next.

---

### ONE-CLICK DEPLOY — 9:30

*[On screen: hPanel → Docker Manager → Catalog → Hermes Agent → Deploy. Time-lapse ~6 minutes.]*

Now the part I promised. We're inside Hostinger's dashboard. Docker Manager, Catalog, search Hermes Agent, Select.

It asks for one thing — an API key for your LLM. This is the brain of your agent. You can use OpenRouter, Anthropic, or OpenAI. I'll use OpenRouter — it gives you access to many models with one key. Paste it. Deploy.

That's it. Hostinger is now building the whole server — Docker, the Hermes container, and HTTPS through Traefik — automatically. About six minutes. Count the terminal commands I typed: zero. This is the wall that used to stop people, and it's just… gone.

---

### SETUP WIZARD — 12:00

*[On screen: browser terminal. Three commands run. Setup wizard completes.]*

```
cd /docker/hermes-agent-xxxx/
docker compose exec -it hermes-agent /bin/bash
hermes setup
```

Server's up. One small setup step — and this is the only place we touch a terminal, and Hostinger gives us a browser terminal so there's nothing to install.

Three lines. Go into the project folder. Step into the container. Then — hermes setup. That starts a wizard.

It asks which provider — I pick OpenRouter. Then which model. For an agent that plans and writes, I'll pick a solid general model — I'll tell you exactly which in the description so you can copy me. Confirm, and Hermes is alive.

---

### CONNECT TELEGRAM — 14:00

*[On screen: @BotFather → new bot → token pasted → gateway started → first reply on phone.]*

Now let's get it on your phone. Open Telegram, message @BotFather, create a new bot, copy the token. Give that token to Hermes, start the gateway.

Watch. "Hey, who are you?" — agent replies on screen. There it is. My agent. On my phone. Running on my own server. This already feels different from a browser tab.

And here's the move most people miss — "Remember: I'm Balaji. I teach freelance Python and AI classes in the evenings. My style is no-jargon, example-first." It just saved that to memory. Hold that thought — it pays off in demo three.

---

### DEMO 1 — MORNING AI NEWS — 16:00

*[On screen: Telegram. Agent researches and summarizes. Cron schedule confirmed.]*

First real job. "Every morning at 7 AM, search the web for the top 3 AI news stories, summarize each in two lines, and message me here."

Watch it work — it goes out, browses the web, comes back with a clean digest. That alone is useful. But the magic is the next word: schedule. It just set up a recurring job — a cron — on the server.

So tomorrow at 7 AM, without me opening anything, this lands on my phone. The agent works while I sleep. That's the whole promise of this video, demo one done.

---

### DEMO 2 — GOOGLE CALENDAR — 19:30

*[On screen: Google Cloud Console on a test account. Calendar API enabled. JSON credentials created and connected.]*

Demo two is the one I'm most excited about, and it's a real engineering skill, not a toy. I want the agent to read my calendar. For that, it needs permission from Google — properly, the way you'd do it in production.

I'm doing this on a throwaway test Google account — never wire your real calendar on camera, and you shouldn't either until you trust the setup.

Step by step. In Google Cloud Console, I create a project, and enable the Google Calendar API. Then I create credentials — I download a JSON key file. This file is the agent's ID card to Google.

I give that JSON to Hermes as a skill, authorize once — that's the OAuth token — and now the agent can read the calendar. "Read today's events and plan my day into a task list, then message me." — plan lands on phone.

This is the fragile part — if your JSON scope is wrong, it fails. I'll put the exact steps and scopes in the description so yours works first try.

---

### DEMO 3 — CLASS PREP — 24:30

*[On screen: calendar event "6 PM — Freelance class: Python OOP". Agent drafts lesson outline. Message opens on phone.]*

Now everything connects. Remember earlier I told the agent who I am and that I teach. And it can read my calendar. So watch what happens when those two combine.

There's a class on my calendar tonight — topic, Python OOP. "Look at my calendar, find today's class, and using my teaching style, prepare a lesson outline with three beginner examples."

Look at this. It pulled the topic from my calendar, used the style from its memory, and wrote a lesson plan I can actually teach. It didn't just answer a question — it did my prep work. This is the difference between a chatbot and an agent. It remembers, it has access, and it does the job.

---

### COST + SAFETY — 28:00

*[On screen: Hermes usage tracking + Hostinger billing.]*

Two fair questions. What does it cost? Two parts — the server, which is the Hostinger plan we picked, and the model usage, which Hermes tracks right here. For this kind of personal use it's small — I'll show you my actual numbers.

Is it safe? Your keys and data sit on your server, not a third party. Keep your API keys and tokens private, never paste them in a public place. That's the trade — a little setup, full control.

---

### CLOSE — 29:30

*[On screen: recap cards. Coupon code + link on screen.]*

Let's recap what you just built. An agent that — one, sends you the morning news. Two, reads your calendar and plans your day. Three, prepares your actual work for you. All on your own server, all from your phone, almost no code.

If you want to build this yourself, the link is in the description, and the coupon BALAJI gives you an extra 10% off — both are pinned at the top of the description. Use the longer plan, it's cheaper per month.

Tell me in the comments — what's the first job you'd give your agent? I read every comment. If this unlocked something, subscribe so the next build reaches you. See you in the next one.

---

## Title Options (pending approval)

1. **I Built an AI Agent That Runs My Life (On My Own Server) — 2026** *(recommended)*
2. This AI Agent Reads My Calendar and Does My Work — Self-Hosted in 2026
3. I Gave an AI Agent a Job (and It Never Sleeps) — Hermes Setup 2026
4. Stop Using ChatGPT in a Tab — Build a 24/7 AI Agent on Your Own Server
5. My AI Agent Wakes Up Before Me — Hermes + Hostinger Step by Step (2026)

---

*Prepared for sponsor review. Full production script with scene notes, compliance map, and record-day checklist available on request.*
