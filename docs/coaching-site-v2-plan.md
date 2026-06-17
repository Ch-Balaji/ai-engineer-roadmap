# Coaching Site V2 — Comprehensive Conversion & Product Plan

> **Site:** [coaching-site-gowtam-2026.web.app](https://coaching-site-gowtam-2026.web.app/)  
> **Author:** Balaji Chippada · The Agent Engineer  
> **Audience:** ~17K YouTube subscribers · 110K-view roadmap video · Indian engineering audience  
> **Goal:** Convert roadmap traffic into paid live masterclasses (₹499–₹1,499) with a professional, frictionless purchase experience  
> **Status:** Plan mode — implementation roadmap  
> **Last updated:** May 25, 2026

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Current State Audit](#2-current-state-audit)
3. [North Star Metrics](#3-north-star-metrics)
4. [Phase 0 — Critical Fixes (Day 1)](#4-phase-0--critical-fixes-day-1)
5. [Phase 1 — Hero & CTA Overhaul (Days 2–3)](#5-phase-1--hero--cta-overhaul-days-23)
6. [Phase 2 — Booking Funnel Redesign (Days 4–7)](#6-phase-2--booking-funnel-redesign-days-47)
7. [Phase 3 — Student Dashboard (Week 2)](#7-phase-3--student-dashboard-week-2)
8. [Phase 4 — Pricing & Product Packaging (Week 2)](#8-phase-4--pricing--product-packaging-week-2)
9. [Phase 5 — Roadmap as Lead Magnet (Week 2–3)](#9-phase-5--roadmap-as-lead-magnet-week-23)
10. [Phase 6 — Trust & Social Proof (Week 3)](#10-phase-6--trust--social-proof-week-3)
11. [Phase 7 — Mobile & WhatsApp (Week 3)](#11-phase-7--mobile--whatsapp-week-3)
12. [Phase 8 — Post-Purchase Lifecycle (Week 3–4)](#12-phase-8--post-purchase-lifecycle-week-34)
13. [Phase 9 — Analytics & A/B Testing (Week 4)](#13-phase-9--analytics--ab-testing-week-4)
14. [Phase 10 — Production Hardening (Week 4–5)](#14-phase-10--production-hardening-week-45)
15. [Recommended Page Structure](#15-recommended-page-structure)
16. [Firestore Data Model](#16-firestore-data-model)
17. [Copy Bank — CTAs, Headlines, Microcopy](#17-copy-bank--ctas-headlines-microcopy)
18. [Legal & Compliance Checklist](#18-legal--compliance-checklist)
19. [Implementation Checklist (Master)](#19-implementation-checklist-master)
20. [Success Criteria — Definition of Done](#20-success-criteria--definition-of-done)

---

## 1. Executive Summary

You have three rare assets most coaches never get:

| Asset | Value |
|---|---|
| **17K YouTube subscribers** | Warm, topic-aligned audience |
| **110K-view roadmap video** | Proof of demand + SEO/social proof |
| **Embedded 26-week roadmap** | Free value that naturally upsells to live teaching |

The website (V1) already has strong bones: premium design, Firebase auth, Firestore masterclasses, Razorpay integration, admin dashboard, and the full roadmap embedded. What it lacks is **conversion architecture** — the funnel from "I trust Balaji" to "I paid, I'm in, I know what happens next."

### The 5 highest-leverage changes

| Priority | Change | Expected impact |
|---|---|---|
| P0 | Fix JS error banner on first paint | Stop losing 30–50% of visitors instantly |
| P0 | Replace generic hero CTA with specific cohort CTA | +20–40% click-through to booking |
| P1 | Login-gated booking + post-payment confirmation screen | Makes product feel real, not prototype |
| P1 | Student dashboard (My Masterclasses tab) | Retention, referrals, repeat purchases |
| P2 | Roadmap woven into homepage with contextual CTAs | Converts your biggest traffic source |

### Product vision (V2)

> A visitor lands from YouTube → sees the next live masterclass with date and seats left → signs in with Google in one tap → pays via Razorpay → lands in a dashboard with calendar invite, Zoom link, prep material, and WhatsApp group → gets reminders → attends live → receives recording + upsell to next class.

---

## 2. Current State Audit

### 2.1 What works well (keep)

- **Visual design** — Dark theme, Instrument Serif + Inter Tight, animated hero, premium feel
- **Roadmap content** — 9 phases, 62 modules, 3 capstones — genuinely world-class free asset
- **Tech stack** — React + Firebase + Razorpay is the right stack for Indian payments
- **Admin dashboard** — AI masterclass generator (Gemini → Firestore syllabus) is a differentiator
- **Masterclass cards** — Split-pane syllabus UI is excellent for showing depth
- **Testimonial marquee + section** — Good pattern, needs real data

### 2.2 What's broken or hurting conversion

| Issue | Severity | Location | User impact |
|---|---|---|---|
| `JS Error undefined` banner on load | 🔴 Critical | `index.html` error handler | Immediate distrust |
| Canonical/OG URLs point to GitHub Pages | 🔴 Critical | `index.html` meta tags | Wrong SEO indexing |
| Hero CTA is generic ("Browse masterclasses") | 🟠 High | `app.jsx` coaching-home hero | No urgency, no specificity |
| Post-payment uses `alert()` | 🟠 High | `app.jsx` ~line 3217 | Feels amateur |
| No student dashboard after purchase | 🟠 High | Missing tab/route | User has nowhere to go |
| Booking doesn't require login first | 🟠 High | Booking modal | Can't tie payment to account |
| Strikethrough discount pricing (₹500 → ₹200) | 🟡 Medium | MasterclassCard, ClosingCTA | Devalues product |
| Fake/generic testimonials | 🟡 Medium | TestimonialMarquee | Reduces trust if spotted |
| Roadmap hidden in separate tab | 🟡 Medium | Tab navigation | Misses 110K-video funnel |
| No FAQ, refund policy, legal pages | 🟡 Medium | Footer | Purchase hesitation |
| No analytics | 🟡 Medium | — | Can't optimize |
| Babel-in-browser for production | 🟡 Medium | `index.html` | Slow TTI on mobile |
| Admin emails hardcoded in UI | 🟢 Low | Dashboard | Minor security UX issue |
| "3k+ Engineers Trained" in hero flank | 🟢 Low | Hero decorative | Inconsistent with "400+ students" stat |

### 2.3 Current user journey (as-is)

```
YouTube video → coaching-site-gowtam-2026.web.app
  → Home tab loads (maybe JS error flash)
  → Hero: "Browse masterclasses →" (scrolls down)
  → Masterclass cards with syllabus
  → Click "Book my seat — ₹X"
  → Modal: Name, Email, Phone (no login required)
  → Razorpay checkout
  → alert("Seat booked successfully!")
  → User closes alert → back on homepage → ??? 
```

**Drop-off points:** JS error → generic CTA → no login → alert() → no dashboard.

### 2.4 Current user journey (target)

```
YouTube / Community post → coaching-site-gowtam-2026.web.app
  → Clean load, no errors
  → Hero: "Reserve seat — Claude Code Masterclass · Sat 7 Jun · ₹499"
  → Click → Google sign-in (one tap) → confirm details → Razorpay
  → Success screen: calendar download, WhatsApp group, prep PDF
  → Redirect to "My Masterclasses" dashboard
  → T-24h email + WhatsApp reminder
  → T-15min "Join Live" button activates
  → Post-class: recording, slides, certificate, next-class coupon
```

---

## 3. North Star Metrics

Track these from Day 1 (even before full V2 ships):

| Metric | Definition | Target (Month 1) |
|---|---|---|
| **Visit → CTA click rate** | % of unique visitors who click any "Reserve/Book" button | > 8% |
| **CTA click → checkout start** | % who open booking modal and submit form | > 60% |
| **Checkout start → payment success** | Razorpay completion rate | > 70% |
| **Overall conversion rate** | Visits → paid bookings | > 3% |
| **Repeat purchase rate** | Users who buy 2+ masterclasses within 90 days | > 15% |
| **NPS post-class** | Net Promoter Score from Day+3 survey | > 50 |
| **Email capture rate** | Roadmap PDF downloads / visits | > 12% |

### Funnel events to instrument

```
page_view
hero_cta_click
masterclass_card_cta_click
booking_modal_open
login_success
booking_form_submit
razorpay_checkout_open
payment_success
payment_failure
dashboard_view
calendar_download
whatsapp_group_click
recording_view
```

---

## 4. Phase 0 — Critical Fixes (Day 1)

> **Goal:** Stop bleeding visitors before any feature work.

### 4.1 Fix JS error banner

**Problem:** Global error handler in `index.html` fires on benign events and shows red error box.

**Fix options (pick one):**

**Option A — Guard the handler:**
```javascript
window.addEventListener('error', function(e) {
  if (!e.message || e.message === 'undefined') return; // ignore benign
  // ... show error UI only for real errors
}, true);
```

**Option B — Remove error catcher in production:**
Only show loading spinner; log errors to console + Sentry.

**Acceptance criteria:**
- [ ] No red error box on fresh page load (desktop + mobile)
- [ ] Real JS errors still logged (Sentry or console)

### 4.2 Fix SEO meta tags

**Current:** `canonical`, `og:url`, `og:image` point to `ch-balaji.github.io/ai-engineer-roadmap/`

**Update to:**
```html
<link rel="canonical" href="https://coaching-site-gowtam-2026.web.app/" />
<meta property="og:url" content="https://coaching-site-gowtam-2026.web.app/" />
<meta property="og:image" content="https://coaching-site-gowtam-2026.web.app/uploads/og.png" />
```

**Also add:**
- Custom domain when ready (e.g. `agentengineer.in` or `balajichippada.com`)
- `og:site_name`: "The Agent Engineer"
- Structured data (JSON-LD) for `Course` / `Event`

**Acceptance criteria:**
- [ ] All meta URLs point to live Firebase hosting URL
- [ ] Facebook/Twitter card debugger shows correct preview

### 4.3 Remove "Test Mode" / dev artifacts

Audit for any visible test/sandbox UI in production:
- [ ] Simulated Razorpay sandbox only in dev environment
- [ ] No admin emails visible to non-admin users
- [ ] No "Test Mode" badge anywhere

### 4.4 Unify social proof numbers

Pick ONE consistent set and use everywhere:

| Stat | Recommended value | Rationale |
|---|---|---|
| YouTube subscribers | 17,000+ | Real, verifiable |
| Roadmap video views | 110,000+ | Real, your biggest proof |
| Students trained (live) | Start honest (e.g. 50+) | Don't inflate; grows with each cohort |
| Average rating | Only show when you have real post-class surveys | Don't show 4.9★ without data |

**Acceptance criteria:**
- [ ] No conflicting numbers across hero, flanks, stats bar, testimonials

---

## 5. Phase 1 — Hero & CTA Overhaul (Days 2–3)

> **Goal:** First 5 seconds answer: *What is this? Why should I trust it? What do I do next?*

### 5.1 New hero structure

```
┌─────────────────────────────────────────────────────────┐
│  EYEBROW: "As seen by 110,000+ engineers on YouTube"  │
│                                                         │
│  TITLE: Master the art of Agentic AI.                   │
│  SUB: Live masterclasses from the engineer behind       │
│       the 26-week 2026 AI Engineer Roadmap.             │
│                                                         │
│  [Reserve seat — Claude Code MC · Sat 7 Jun · ₹499]    │  ← PRIMARY
│  [See the full 26-week roadmap →]                       │  ← SECONDARY
│                                                         │
│  🟢 14 of 50 seats left · Cohort closes Friday          │
│                                                         │
│  YouTube 17K · 110K roadmap views · Razorpay secure   │
└─────────────────────────────────────────────────────────┘
```

### 5.2 Hero CTA rules

| Rule | Detail |
|---|---|
| **Specific** | Name the masterclass, date, and price in the button |
| **Action-oriented** | "Reserve seat" > "Browse" > "Learn more" |
| **One primary action** | Only one orange/primary button above the fold |
| **Scarcity (honest)** | Real seat count from Firestore; hide when sold out |
| **Dynamic** | Pull next upcoming masterclass from Firestore, not hardcoded |

### 5.3 Implementation tasks

- [ ] Create `getNextUpcomingMasterclass()` helper — queries Firestore `masterclasses` ordered by `dateTime asc`, filters future dates
- [ ] Replace hero primary button onClick: open booking modal directly (not scroll)
- [ ] Add scarcity line component: reads `seatsTotal - seatsBooked` from Firestore
- [ ] Add trust strip below CTAs
- [ ] Optional: embed 60–90s YouTube intro video (modal or inline)

### 5.4 Stats bar redesign

Replace current stats bar with verifiable metrics:

```
17K+ YouTube  |  110K+ roadmap views  |  Live cohorts  |  From ₹499
```

Remove fake "4.9★" until you have real survey data.

### 5.5 Closing CTA section

Currently hardcoded to "Claude Code Masterclass" at ₹200. Change to:
- Dynamic: same `getNextUpcomingMasterclass()` as hero
- Add countdown timer to cohort close date
- Button text: "Reserve my seat — ₹{price} →"

**Acceptance criteria:**
- [ ] Hero CTA opens booking modal for specific masterclass
- [ ] Date and price are dynamic from Firestore
- [ ] Scarcity line shows real remaining seats
- [ ] No strikethrough discount badges in hero

---

## 6. Phase 2 — Booking Funnel Redesign (Days 4–7)

> **Goal:** 3-step checkout that feels like buying from a real platform, not a prototype.

### 6.1 New booking flow (3 steps)

```
Step 1: SIGN IN
├── Google one-tap (primary)
├── Phone OTP via Firebase (secondary, for non-Google users)
└── No password forms for buyers

Step 2: CONFIRM DETAILS
├── Pre-filled: name, email (from Google)
├── Ask only: phone number (for WhatsApp updates)
├── Order summary:
│   ├── Masterclass title
│   ├── Date & time (auto-detect timezone, show IST + local)
│   ├── Price
│   └── What's included (bullet list)
└── Tier selector (if multi-tier pricing enabled)

Step 3: PAY
├── Razorpay overlay (UPI / card / netbanking)
└── On success → Confirmation screen (NOT alert())
```

### 6.2 Booking modal UI spec

**Step indicator:** `① Sign in  →  ② Details  →  ③ Pay`

**Step 1 — Sign in:**
```
┌──────────────────────────────────────┐
│  Book your seat                      │
│  Claude Code Masterclass · ₹499      │
│                                      │
│  [🔵 Continue with Google]           │
│                                      │
│  ── or ──                            │
│                                      │
│  Phone: [+91 ___________] [Send OTP] │
└──────────────────────────────────────┘
```

**Step 2 — Confirm:**
```
┌──────────────────────────────────────┐
│  Almost there!                       │
│                                      │
│  Name:  Balaji Chippada  (from Google)│
│  Email: balaji@...       (from Google)│
│  Phone: [+91 ___________] *required  │
│                                      │
│  ── Order Summary ──                 │
│  Claude Code Masterclass             │
│  Sat, 7 Jun 2026 · 10:00 AM IST      │
│  ₹499                                │
│                                      │
│  ✓ Live 3-hour session               │
│  ✓ Slides & GitHub repo              │
│  ✓ 30-day recording access           │
│                                      │
│  [Pay ₹499 securely →]               │
│  🔒 Secured by Razorpay              │
└──────────────────────────────────────┘
```

**Step 3 — Success:**
```
┌──────────────────────────────────────┐
│  ✅ You're in!                       │
│                                      │
│  Claude Code Masterclass             │
│  Sat, 7 Jun 2026 · 10:00 AM IST      │
│                                      │
│  [📅 Add to Google Calendar]         │
│  [📅 Add to Apple Calendar]          │
│  [💬 Join WhatsApp Group]            │
│  [📧 Check your email for prep PDF]  │
│                                      │
│  [Go to My Dashboard →]              │
└──────────────────────────────────────┘
```

### 6.3 Code changes required

| File | Change |
|---|---|
| `app.jsx` | Replace single-step booking modal with 3-step wizard component |
| `app.jsx` | Gate Step 2 behind `user !== null` |
| `app.jsx` | Remove `alert()` on payment success; render Step 3 confirmation |
| `app.jsx` | Add `.ics` calendar file generator (client-side) |
| Cloud Function | On `payment.captured` webhook: write booking to `users/{uid}/bookings/{bookingId}` |
| Cloud Function | Increment `seatsBooked` on masterclass doc |
| Cloud Function | Trigger confirmation email |

### 6.4 Calendar invite generation

Generate `.ics` file client-side on success:

```javascript
function generateICS({ title, startDate, endDate, description, location, organizerEmail }) {
  // Standard iCalendar format
  // Trigger browser download as "{title}.ics"
}
```

Fields:
- `SUMMARY`: Masterclass title
- `DTSTART` / `DTEND`: Session start/end (include 3-hour default if no end time)
- `DESCRIPTION`: Zoom link + prep instructions
- `LOCATION`: Zoom URL (or "Online")
- `ORGANIZER`: balaji@yourdomain.com

### 6.5 Login modal separation

**Current problem:** Login modal mixes admin registration + buyer sign-in.

**Fix:** Two distinct flows:
- **Buyer login:** Google only, no "Register account" toggle, no admin messaging
- **Admin login:** Separate route or hidden behind `/admin` or staff-only nav tab

**Acceptance criteria:**
- [ ] Booking requires Google sign-in before payment
- [ ] Phone number collected in Step 2
- [ ] Payment success shows confirmation screen (no alert)
- [ ] Calendar download works on iOS + Android + desktop
- [ ] Booking written to Firestore under user ID
- [ ] Seat count decrements on successful payment

---

## 7. Phase 3 — Student Dashboard (Week 2)

> **Goal:** Every paying customer has a home base — schedule, links, resources, support.

### 7.1 New navigation tab: "My Masterclasses"

Add to main nav (visible when `user && !isAdmin`):

```
Home  |  Full Roadmap  |  My Masterclasses  |  [Profile avatar]
```

Route: `activeMainTab === 'mybookings'`

### 7.2 Dashboard sections

#### A. Upcoming Sessions
```
┌─────────────────────────────────────────────────┐
│  🔴 LIVE IN 2 HOURS                             │
│  Claude Code Masterclass                        │
│  Sat, 7 Jun · 10:00 AM IST                      │
│                                                 │
│  [Join Live →]  [Add to Calendar]  [Prep Guide] │
└─────────────────────────────────────────────────┘
```

- "Join Live" button activates 15 minutes before start time
- Links to Zoom/Google Meet URL stored in Firestore masterclass doc
- Countdown timer when < 24 hours away

#### B. Past Sessions
```
┌─────────────────────────────────────────────────┐
│  Production RAG Masterclass · 15 May 2026       │
│  [Watch Recording]  [Download Slides]  [Notes]  │
└─────────────────────────────────────────────────┘
```

#### C. Resources
- Pre-class prep checklist (PDF link per masterclass)
- GitHub repo links
- Community links (WhatsApp / Discord)

#### D. Profile & Inquiries
```
Name: Balaji Chippada
Email: balaji@example.com
Phone: +91 98765 43210
[Edit Profile]

── My Inquiries ──
[Submit a question for upcoming session]
[View past Q&A responses]
```

#### E. Receipts
```
Claude Code Masterclass · ₹499 · 1 Jun 2026
[Download Invoice]
```

### 7.3 Firestore queries

```javascript
// User's bookings
db.collection('users').doc(uid).collection('bookings')
  .where('status', '==', 'confirmed')
  .orderBy('sessionDate', 'desc')

// Upcoming only
  .where('sessionDate', '>=', new Date())
  .orderBy('sessionDate', 'asc')
```

### 7.4 Implementation tasks

- [ ] Add `mybookings` tab to nav (conditional on auth)
- [ ] Build `StudentDashboard` component with 5 sections above
- [ ] Firestore security rules: users can only read their own bookings
- [ ] Admin can attach Zoom link, recording URL, slides URL to masterclass doc
- [ ] "Join Live" button time-gated (15 min before → 30 min after session end)
- [ ] Profile edit (name, phone) with Firestore `users/{uid}` doc
- [ ] Inquiry form: writes to `inquiries` collection with userId + masterclassId

**Acceptance criteria:**
- [ ] Logged-in user sees "My Masterclasses" tab
- [ ] Upcoming sessions show countdown + Join Live button
- [ ] Past sessions show recording/slides links
- [ ] User can edit profile and submit inquiries
- [ ] Invoice downloadable as PDF

---

## 8. Phase 4 — Pricing & Product Packaging (Week 2)

> **Goal:** Price for value, not for volume. Structure tiers to maximize revenue per student.

### 8.1 Recommended tier structure

| Tier | Price | Includes | Target buyer |
|---|---|---|---|
| **Live Drop-In** | ₹499 | Live attendance only, no recording | Curious, low commitment |
| **Standard** ⭐ | ₹1,499 | Live + 30-day recording + slides + GitHub repo | Most buyers (70%+) |
| **Pro** | ₹3,999 | Standard + 15-min 1:1 doubt session + private WhatsApp + 50% off next class | Serious engineers |

### 8.2 Pricing psychology rules

| Do | Don't |
|---|---|
| "Cohort 1 intro pricing — goes up after 50 seats" | "₹500 ~~₹500~~ 60% OFF" |
| Show Standard as recommended (highlighted card) | Show only one price with fake discount |
| Anchor Pro tier to make Standard feel reasonable | Price below ₹399 (signals low quality to engineers) |
| Offer payment plans for Pro (2 × ₹2,000) | Hide price until checkout |

### 8.3 Masterclass lineup (suggested)

Based on your roadmap phases and YouTube audience demand:

| Masterclass | Roadmap Phase | Duration | Suggested price (Standard) |
|---|---|---|---|
| **Claude Code Masterclass** | Phase 5 (Tools) | 3 hours | ₹1,499 |
| **Production RAG Masterclass** | Phase 4 (RAG) | 4 hours | ₹1,999 |
| **Multi-Agent Orchestration** | Phase 7 | 3 hours | ₹1,999 |
| **Guardrails & LLMOps** | Phase 8 | 2 hours | ₹1,499 |
| **Cloud Deployment for Agents** | Phase 9 | 3 hours | ₹1,499 |

Launch with **one** masterclass first (Claude Code — highest demand, clearest outcome). Add others monthly.

### 8.4 "What you'll build" deliverables (per masterclass)

People buy outcomes, not topics. Each masterclass card must answer: *"What will I have at the end?"*

**Claude Code Masterclass:**
> By the end of this 3-hour live session, you'll have a Claude Code agent that autonomously reviews PRs in your GitHub repo — with TDD workflow, multi-file refactoring, and security audit capabilities.

**Production RAG Masterclass:**
> You'll deploy a hybrid retrieval pipeline (vector + BM25 + reranking) with a golden eval dataset — and know exactly why your RAG is wrong when it fails.

### 8.5 Implementation tasks

- [ ] Add `tiers` array to Firestore masterclass schema
- [ ] Tier selector in booking modal Step 2
- [ ] Pass selected tier to Razorpay order amount
- [ ] Store tier in booking record
- [ ] Gate recording access by tier in dashboard
- [ ] Remove all strikethrough discount UI
- [ ] Add "What's included" bullet list per tier on masterclass card

**Acceptance criteria:**
- [ ] 3 tiers displayed on masterclass card with Standard highlighted
- [ ] Razorpay charges correct tier amount
- [ ] Dashboard shows tier-specific resources (recording only for Standard+)

---

## 9. Phase 5 — Roadmap as Lead Magnet (Week 2–3)

> **Goal:** Turn your 110K-view roadmap from a separate tab into the #1 conversion engine.

### 9.1 Homepage roadmap teaser

Add section below hero (before masterclass cards):

```
┌─────────────────────────────────────────────────┐
│  THE ROADMAP THAT 110,000 ENGINEERS USED        │
│                                                 │
│  [Phase 1 preview] [Phase 4 preview] [Phase 7]│
│  26 weeks · 9 phases · 62 modules · 3 capstones │
│                                                 │
│  [Explore the full roadmap →]                   │
│  [Get roadmap PDF + Notion template — free]   │  ← email capture
└─────────────────────────────────────────────────┘
```

### 9.2 Email capture for roadmap PDF

- Modal: "Enter email → we'll send the roadmap PDF + Notion template"
- Store in Firestore `leads` collection: `{ email, source: 'roadmap_pdf', createdAt }`
- Send via Firebase Extension (Trigger Email) or Mailchimp/ConvertKit
- Follow-up sequence: Day 0 (PDF) → Day 2 (masterclass invite) → Day 5 (testimonial + scarcity)

### 9.3 Contextual CTAs inside roadmap

Within each phase section in the Roadmap tab, add a contextual banner:

```
┌─────────────────────────────────────────────────┐
│  🎯 Want to master this live?                   │
│  Phase 5: Tools, MCP & Single Agents            │
│  → Claude Code Masterclass · Sat 7 Jun · ₹499  │
│  [Reserve seat →]                               │
└─────────────────────────────────────────────────┘
```

Mapping:

| Roadmap Phase | Masterclass CTA |
|---|---|
| Phase 4 — RAG + Evaluation | Production RAG Masterclass |
| Phase 5 — Tools, MCP & Single Agents | Claude Code Masterclass |
| Phase 7 — Multi-Agent Orchestration | Multi-Agent Masterclass |
| Phase 8 — Guardrails & LLMOps | Guardrails Masterclass |
| Phase 9 — Cloud + Deployment | Cloud Deployment Masterclass |

### 9.4 YouTube video embed

- Sticky bottom-right thumbnail: "▶ Watch the 1-hour roadmap walkthrough"
- Opens modal with embedded YouTube player
- Below video: "Ready to go deeper? Reserve your seat →"

### 9.5 OUT_OF_SCOPE and NEXT_STEPS sections

Your `data.js` already has beautifully written `OUT_OF_SCOPE` and `NEXT_STEPS` content. Use them:

- **OUT_OF_SCOPE:** "These topics aren't in the free roadmap — but we cover them live in our masterclasses."
- **NEXT_STEPS:** "You've seen the roadmap. Now ship it with live guidance."

### 9.6 Implementation tasks

- [ ] Homepage roadmap teaser section with 3 phase preview cards
- [ ] Email capture modal + Firestore `leads` collection
- [ ] Automated PDF email (Firebase Extension or external)
- [ ] Contextual CTA banners in RoadmapView per phase
- [ ] YouTube embed modal (sticky trigger)
- [ ] Map phases to masterclasses in Firestore (phaseId field on masterclass doc)

**Acceptance criteria:**
- [ ] Roadmap visible on homepage (not just separate tab)
- [ ] Email capture works and stores leads
- [ ] At least 3 phase sections have contextual masterclass CTAs
- [ ] YouTube video embeddable from homepage

---

## 10. Phase 6 — Trust & Social Proof (Week 3)

> **Goal:** Remove every reason a skeptical engineer wouldn't pay.

### 10.1 Instructor bio block

```
┌─────────────────────────────────────────────────┐
│  [Photo]  Balaji Chippada                       │
│           AI Engineer · The Agent Engineer      │
│           17K+ YouTube · 110K roadmap views     │
│           [LinkedIn →]  [YouTube →]             │
│                                                 │
│  "I build production agentic AI systems and     │
│   teach engineers to ship them — not demo them."│
└─────────────────────────────────────────────────┘
```

Requirements:
- Professional headshot (not avatar)
- LinkedIn profile link (verifiable)
- YouTube channel link
- 2–3 line bio focused on production experience, not credentials

### 10.2 Real testimonials (minimum 5)

Each testimonial must have:

| Field | Example |
|---|---|
| Full name | Vikram Reddy |
| Role + company | Senior Engineer · Razorpay |
| Photo | Headshot or LinkedIn avatar |
| LinkedIn URL | Optional but powerful |
| Specific outcome | "Shipped my first agentic feature in 3 days after the Claude Code session" |

**Do NOT use:** "Vikram R., Dev" or "Suresh P., Dev" — these read as fabricated.

**Sources for real testimonials:**
- YouTube comments on roadmap video (screenshot + quote)
- Post-class NPS survey (Phase 8)
- LinkedIn posts from attendees
- WhatsApp group messages (with permission)

### 10.3 FAQ section

Add before footer on homepage:

**Q: I'm a beginner — is this too advanced?**
A: The Claude Code masterclass assumes you can write Python and use a terminal. If you've completed Phase 1 of the free roadmap, you're ready.

**Q: What if I miss the live session?**
A: Standard and Pro tiers include 30-day recording access. Drop-In tier is live-only.

**Q: Do I get a certificate?**
A: Yes — all tiers receive a certificate of completion after attending (live or via recording).

**Q: What's the refund policy?**
A: 100% refund within 24 hours of purchase, no questions asked. See our [Refund Policy].

**Q: What language is the session in?**
A: English, with Indian context and examples. Q&A accommodates Hindi questions.

**Q: What do I need to prepare?**
A: A laptop with Python 3.10+, VS Code, and a Claude Pro subscription (free trial works). Full prep checklist sent after booking.

**Q: How is this different from free YouTube content?**
A: YouTube teaches concepts. Masterclasses are live, hands-on build sessions where you ship a working system with real-time debugging and Q&A.

### 10.4 "Who this is for / NOT for"

**This is for you if:**
- You're an engineer who wants to ship agentic AI in production, not just demo it
- You've watched the roadmap video and want hands-on guidance on specific phases
- You learn best by building alongside someone who's done it

**This is NOT for you if:**
- You're looking for a passive lecture with no coding
- You expect a job guarantee or placement
- You haven't written Python before

### 10.5 Implementation tasks

- [ ] Redesign InstructorBio with photo, LinkedIn, YouTube links
- [ ] Replace all generic testimonials with 5+ real ones
- [ ] Add FAQ accordion section (8+ questions)
- [ ] Add "Who this is for / NOT for" block
- [ ] Add YouTube comments screenshot section
- [ ] Add refund policy page

**Acceptance criteria:**
- [ ] Instructor photo and LinkedIn visible
- [ ] 5+ testimonials with full names and companies
- [ ] FAQ covers top 8 objections
- [ ] Refund policy linked from FAQ and footer

---

## 11. Phase 7 — Mobile & WhatsApp (Week 3)

> **Goal:** Most YouTube traffic is mobile. Optimize for thumb-reach and Indian communication norms.

### 11.1 Mobile sticky bottom bar

Always visible on mobile (< 768px):

```
┌─────────────────────────────────────────────────┐
│  Claude Code MC · Sat 7 Jun    [Reserve ₹499 →] │
└─────────────────────────────────────────────────┘
```

- Fixed to bottom, above safe area
- Shows next masterclass name + price
- Tap → opens booking modal directly

### 11.2 WhatsApp floating button

Bottom-right (above sticky bar on mobile):

```
[💬 Questions? WhatsApp us]
```

- Links to WhatsApp Business number
- Pre-filled message: "Hi, I have a question about the Claude Code Masterclass"
- Use WhatsApp Business API for automated responses to common questions

### 11.3 Mobile nav redesign

Current tab nav doesn't work well on mobile. Change to:

```
[☰ Menu]  The Agent Engineer  [Reserve →]
```

Hamburger menu:
- Home
- Full Roadmap
- Masterclasses
- My Masterclasses (if logged in)
- Sign In / Profile

### 11.4 Masterclass card mobile layout

- Split-pane syllabus collapses to accordion on mobile
- "Book my seat" button: full-width, min-height 48px (thumb-friendly)
- Price visible without scrolling

### 11.5 Implementation tasks

- [ ] Sticky bottom CTA bar (mobile only, CSS media query)
- [ ] WhatsApp floating button with pre-filled message
- [ ] Mobile hamburger nav with Reserve button in header
- [ ] Masterclass card responsive accordion
- [ ] Test on iPhone SE (375px) and common Android (360px)

**Acceptance criteria:**
- [ ] Sticky bar visible on all mobile pages
- [ ] WhatsApp button opens chat with pre-filled message
- [ ] All CTAs are 48px+ touch targets
- [ ] No horizontal scroll on 375px viewport

---

## 12. Phase 8 — Post-Purchase Lifecycle (Week 3–4)

> **Goal:** Turn a ₹499 transaction into a ₹4,999 repeat customer through automated nurture.

### 12.1 Email lifecycle

| Trigger | Timing | Subject | Content |
|---|---|---|---|
| Booking confirmed | Instant | "You're in! Claude Code Masterclass · Sat 7 Jun" | Receipt, calendar link, prep PDF, WhatsApp group link |
| Prep reminder | T-48h | "2 days until Claude Code Masterclass — prep checklist" | What to install, what to read, what to expect |
| Live reminder | T-24h | "Tomorrow: Claude Code Masterclass at 10 AM IST" | Zoom link, last-minute prep, "Join Live" button |
| We're live | T-15min | "We're live! Join now →" | Direct Zoom link |
| Post-class | T+1h | "Recording, slides, and your certificate" | Recording URL, slides, certificate PDF, next-class coupon |
| Upsell | T+3d | "50% off: Production RAG Masterclass" | Coupon code, scarcity, testimonial from first class |
| NPS survey | T+3d | "How was the masterclass? (30 seconds)" | 1–10 rating + optional text testimonial request |

### 12.2 WhatsApp lifecycle

Same triggers as email, via WhatsApp Business API (Gupshup / WATI / Interakt):

| Message | Template |
|---|---|
| Booking confirmed | "Hi {name}! Your seat for {masterclass} on {date} is confirmed. Prep guide: {link}. WhatsApp group: {link}" |
| T-24h reminder | "Reminder: {masterclass} is tomorrow at {time}. Zoom link will be sent 15 min before." |
| T-15min live | "We're live! Join here: {zoom_link}" |
| Post-class | "Thanks for attending! Recording: {link}. Slides: {link}. Next class 50% off: {coupon}" |

### 12.3 Technical implementation

```
Payment success (Razorpay webhook)
  → Cloud Function: onPaymentCaptured
    → Write booking to Firestore
    → Increment seatsBooked
    → Trigger email (Firebase Extension: Trigger Email + SendGrid)
    → Trigger WhatsApp (Cloud Function → Gupshup API)
    → Schedule reminder jobs (Cloud Scheduler or Firestore-triggered functions)
```

### 12.4 Certificate generation

Auto-generate PDF certificate on attendance confirmation:

```
┌─────────────────────────────────────────────────┐
│           CERTIFICATE OF COMPLETION             │
│                                                 │
│  This certifies that                            │
│  BALAJI CHIPPADA                                │
│  has successfully completed                     │
│  Claude Code Masterclass                        │
│  7 June 2026                                    │
│                                                 │
│  Balaji Chippada · The Agent Engineer           │
└─────────────────────────────────────────────────┘
```

Generate via Cloud Function + PDF library (pdfkit or puppeteer). Store URL in booking doc. Available in dashboard.

### 12.5 Implementation tasks

- [ ] Set up SendGrid or Postmark for transactional email
- [ ] Firebase Extension: Trigger Email on booking creation
- [ ] WhatsApp Business API integration (Gupshup/WATI)
- [ ] Cloud Scheduler jobs for T-48h, T-24h, T-15min reminders
- [ ] Post-class email with recording + slides + coupon
- [ ] NPS survey (Google Form or Typeform, linked from email)
- [ ] Certificate PDF generator Cloud Function
- [ ] Coupon code system (Firestore `coupons` collection, validated at checkout)

**Acceptance criteria:**
- [ ] Confirmation email sent within 60 seconds of payment
- [ ] WhatsApp confirmation sent within 60 seconds
- [ ] T-24h reminder sent automatically
- [ ] Post-class email with recording link sent within 1 hour of session end
- [ ] Certificate downloadable from dashboard after attendance

---

## 13. Phase 9 — Analytics & A/B Testing (Week 4)

> **Goal:** Measure everything. Optimize what works.

### 13.1 Analytics stack

| Tool | Purpose | Priority |
|---|---|---|
| **Google Analytics 4** | Page views, funnel, traffic sources | P0 |
| **PostHog** (or Mixpanel) | Event-level funnel, session replay | P1 |
| **Meta Pixel** | Retargeting YouTube/Instagram visitors | P1 |
| **Google Search Console** | SEO performance for roadmap keywords | P2 |

### 13.2 GA4 setup

```javascript
// In index.html or app.jsx init
gtag('config', 'G-XXXXXXXXXX');
gtag('event', 'page_view', { page_title: activeMainTab });
```

Custom events (see Section 3 funnel events).

### 13.3 Conversion funnel dashboard

Build a simple admin view (or use PostHog dashboard):

```
Visits:           1,000
Hero CTA clicks:    120  (12%)
Booking modal:       80  (67% of clicks)
Login completed:     70  (88%)
Payment started:     55  (79%)
Payment success:     42  (76%)
Overall CR:        4.2%
```

### 13.4 A/B tests to run (Month 1–2)

| Test | Variant A | Variant B | Metric |
|---|---|---|---|
| Hero CTA text | "Browse masterclasses" | "Reserve seat — Claude Code MC · ₹499" | CTA click rate |
| Hero video | No video | 60s intro video embedded | Time on page + CTA click |
| Pricing display | Single price ₹499 | 3 tiers with Standard highlighted | Revenue per visitor |
| Scarcity | No scarcity line | "14 of 50 seats left" | Checkout start rate |
| Post-payment | alert() | Confirmation screen + calendar | Return visit rate |

### 13.5 YouTube → site attribution

Add UTM parameters to all YouTube links:

```
https://coaching-site-gowtam-2026.web.app/?utm_source=youtube&utm_medium=video&utm_campaign=roadmap_110k
```

Track in GA4 which videos drive the most conversions.

### 13.6 Implementation tasks

- [ ] Install GA4 with custom events
- [ ] Install PostHog (or equivalent) for funnel analysis
- [ ] Install Meta Pixel for retargeting
- [ ] Add UTM parameters to all YouTube description links
- [ ] Build conversion funnel report (weekly review)
- [ ] Set up first A/B test (hero CTA text)

**Acceptance criteria:**
- [ ] All 12 funnel events tracked in GA4
- [ ] Weekly funnel report accessible
- [ ] UTM links in YouTube video descriptions
- [ ] At least 1 A/B test running

---

## 14. Phase 10 — Production Hardening (Week 4–5)

> **Goal:** Move from prototype to production-grade deployment.

### 14.1 Build pipeline

**Current:** Babel Standalone compiles JSX in browser (~400KB overhead).

**Target:** Pre-built bundle deployed to Firebase Hosting.

```
npm run build  →  dist/app.js (minified)
firebase deploy --only hosting
```

Steps:
- [ ] Set up esbuild or Vite build step
- [ ] Remove Babel Standalone from production HTML
- [ ] Remove CDN React (bundle includes it)
- [ ] Enable Firebase Hosting cache headers
- [ ] Target Lighthouse Performance score > 85

### 14.2 Custom domain

Register and configure:
- Primary: `agentengineer.in` or `balajichippada.com` or `theagentengineer.com`
- Redirect Firebase default URL to custom domain
- Update all canonical/OG tags

### 14.3 Firestore security rules

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Masterclasses: public read, admin write
    match /masterclasses/{id} {
      allow read: if true;
      allow write: if request.auth != null
        && request.auth.token.email in ['balaji@...', 'gowtam@...'];
    }
    // User bookings: owner read only
    match /users/{userId}/bookings/{bookingId} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow write: if false; // only Cloud Functions write
    }
    // Leads: anyone can create, admin read
    match /leads/{id} {
      allow create: if true;
      allow read: if request.auth != null && request.auth.token.admin == true;
    }
    // Inquiries: authenticated users create, admin read
    match /inquiries/{id} {
      allow create: if request.auth != null;
      allow read: if request.auth != null
        && (request.auth.uid == resource.data.userId
            || request.auth.token.admin == true);
    }
  }
}
```

### 14.4 Error monitoring

- [ ] Add Sentry for JS error tracking
- [ ] Cloud Function error alerts (Firebase Alerts → email/Slack)
- [ ] Razorpay webhook failure alerts

### 14.5 Performance

- [ ] Lazy-load Three.js / GSAP / Lenis (only on roadmap tab)
- [ ] Image optimization (WebP, lazy loading)
- [ ] Preload critical fonts
- [ ] Service worker for offline roadmap access

### 14.6 Implementation tasks

- [ ] esbuild/Vite build pipeline
- [ ] Custom domain setup
- [ ] Firestore security rules deployed
- [ ] Sentry integration
- [ ] Lazy-load heavy animation libraries
- [ ] Lighthouse audit > 85 performance

**Acceptance criteria:**
- [ ] No Babel Standalone in production
- [ ] Custom domain live with SSL
- [ ] Firestore rules prevent unauthorized access
- [ ] Sentry catching production errors
- [ ] Lighthouse Performance > 85

---

## 15. Recommended Page Structure

Final homepage layout (top to bottom):

```
┌─────────────────────────────────────────────────┐
│  STICKY NAV                                     │
│  Logo · Home · Roadmap · Masterclasses · Sign In│
├─────────────────────────────────────────────────┤
│  1. HERO                                        │
│     Eyebrow (110K social proof)                 │
│     Title + sub                                 │
│     Primary CTA (specific cohort)               │
│     Secondary CTA (roadmap)                     │
│     Scarcity line                               │
│     Trust strip                                 │
│     [Optional: 60s intro video]                 │
├─────────────────────────────────────────────────┤
│  2. NEXT COHORT CARD (large, prominent)         │
│     Date · time · seats left · single CTA       │
├─────────────────────────────────────────────────┤
│  3. WHAT YOU'LL BUILD                           │
│     Concrete deliverables, not curriculum       │
├─────────────────────────────────────────────────┤
│  4. MASTERCLASS SCHEDULE                        │
│     Split-pane cards with syllabus              │
│     Tier pricing on each card                   │
├─────────────────────────────────────────────────┤
│  5. ROADMAP TEASER                              │
│     "110K engineers used this roadmap"          │
│     3 phase previews + email capture            │
├─────────────────────────────────────────────────┤
│  6. INSTRUCTOR BIO                              │
│     Photo · LinkedIn · YouTube · credibility    │
├─────────────────────────────────────────────────┤
│  7. TESTIMONIALS                                │
│     Real names · photos · companies · outcomes  │
├─────────────────────────────────────────────────┤
│  8. YOUTUBE COMMENTS                            │
│     Screenshot grid from 110K-view video          │
├─────────────────────────────────────────────────┤
│  9. PRICING TIERS                               │
│     Drop-In / Standard ⭐ / Pro                   │
├─────────────────────────────────────────────────┤
│  10. FAQ                                        │
│      8+ questions with accordion                │
├─────────────────────────────────────────────────┤
│  11. WHO THIS IS FOR / NOT FOR                  │
├─────────────────────────────────────────────────┤
│  12. CLOSING CTA                                │
│      Countdown + "Reserve my seat"              │
├─────────────────────────────────────────────────┤
│  13. FOOTER                                     │
│      Legal · Contact · WhatsApp · Social        │
├─────────────────────────────────────────────────┤
│  MOBILE: Sticky bottom bar "Reserve ₹499 →"     │
│  FLOATING: WhatsApp button                      │
└─────────────────────────────────────────────────┘
```

---

## 16. Firestore Data Model

### 16.1 Collections

```
masterclasses/{masterclassId}
├── title: string
├── description: string
├── instructor: string
├── dateTime: timestamp
├── duration: number (minutes)
├── price: number (base/Drop-In price)
├── tiers: [
│     { name: "Drop-In", price: 499, includes: [...] },
│     { name: "Standard", price: 1499, includes: [...], recommended: true },
│     { name: "Pro", price: 3999, includes: [...] }
│   ]
├── seatsTotal: number
├── seatsBooked: number
├── syllabus: [{ n, title, items[] }]
├── rawSyllabus: string
├── phaseId: number (links to roadmap phase)
├── zoomLink: string
├── recordingUrl: string (post-class)
├── slidesUrl: string
├── prepPdfUrl: string
├── whatsappGroupLink: string
├── status: "published" | "draft" | "completed"
├── createdAt: timestamp

users/{userId}
├── name: string
├── email: string
├── phone: string
├── createdAt: timestamp
├── bookings/{bookingId}
│   ├── masterclassId: string
│   ├── masterclassTitle: string
│   ├── tier: string
│   ├── amount: number
│   ├── status: "confirmed" | "refunded" | "cancelled"
│   ├── razorpayPaymentId: string
│   ├── razorpayOrderId: string
│   ├── sessionDate: timestamp
│   ├── bookedAt: timestamp
│   ├── attended: boolean
│   └── certificateUrl: string (post-attendance)

leads/{leadId}
├── email: string
├── source: "roadmap_pdf" | "exit_intent" | "newsletter"
├── createdAt: timestamp

inquiries/{inquiryId}
├── userId: string
├── masterclassId: string
├── question: string
├── answer: string (admin response)
├── status: "open" | "answered"
├── createdAt: timestamp

coupons/{couponId}
├── code: string
├── discountPercent: number
├── validUntil: timestamp
├── maxUses: number
├── usedCount: number
├── applicableMasterclassIds: string[]
```

### 16.2 Cloud Functions

| Function | Trigger | Action |
|---|---|---|
| `createRazorpayOrder` | HTTPS callable | Create Razorpay order, return orderId |
| `razorpayWebhook` | HTTPS endpoint | Verify signature, write booking, increment seats, trigger emails |
| `sendBookingConfirmation` | Firestore onCreate (bookings) | Send email + WhatsApp |
| `sendReminder` | Cloud Scheduler | T-48h, T-24h, T-15min reminders |
| `sendPostClassEmail` | Cloud Scheduler (manual trigger) | Recording, slides, certificate, upsell |
| `generateCertificate` | HTTPS callable | Generate PDF, store URL |
| `validateCoupon` | HTTPS callable | Check coupon validity, return discount |

---

## 17. Copy Bank — CTAs, Headlines, Microcopy

### 17.1 Hero headlines (A/B test candidates)

| Variant | Headline | Sub |
|---|---|---|
| A (recommended) | Master the art of **Agentic AI.** | Live masterclasses from the engineer behind the 26-week 2026 AI Engineer Roadmap. |
| B | Ship **production-grade AI agents.** | Not demos. Not tutorials. Live build sessions with Balaji Chippada. |
| C | From roadmap to **production.** | The live masterclasses that turn the 110K-view roadmap into shipped code. |

### 17.2 Primary CTA buttons

| Context | Button text |
|---|---|
| Hero | Reserve seat — Claude Code MC · Sat 7 Jun · ₹499 |
| Masterclass card | Book my seat — ₹1,499 |
| Closing CTA | Reserve my seat — ₹499 → |
| Mobile sticky bar | Reserve ₹499 → |
| Roadmap phase banner | Master this live → Reserve seat |
| Post-video embed | Ready to build this? Reserve your seat → |

### 17.3 Secondary CTAs

| Context | Button text |
|---|---|
| Hero | See the full 26-week roadmap → |
| Roadmap teaser | Get roadmap PDF + Notion template — free |
| Post-class email | 50% off next masterclass → |

### 17.4 Scarcity lines

| Context | Text |
|---|---|
| Hero | 🟢 14 of 50 seats left · Cohort closes Friday |
| Masterclass card | 🔴 Only 6 seats remaining |
| Sold out | ⏳ Sold out — join waitlist for next cohort |
| Closing CTA | ⏰ Price increases to ₹1,999 after first 50 seats |

### 17.5 Trust microcopy

| Location | Text |
|---|---|
| Below pay button | 🔒 Secured by Razorpay · 100% refund within 24 hours |
| Footer | Trusted by 17,000+ YouTube subscribers |
| Booking modal | Your data is encrypted and never shared |

### 17.6 Email subject lines

| Email | Subject |
|---|---|
| Confirmation | You're in! {masterclass} · {date} |
| T-48h | 2 days until {masterclass} — here's your prep checklist |
| T-24h | Tomorrow: {masterclass} at {time} IST |
| T-15min | We're live! Join {masterclass} now → |
| Post-class | Your recording, slides, and certificate are ready |
| Upsell | 50% off: {next_masterclass} — exclusive for attendees |
| NPS | How was {masterclass}? (30 seconds) |

---

## 18. Legal & Compliance Checklist

Required for Razorpay live mode and Indian consumer trust:

- [ ] **Privacy Policy** — what data you collect, how you use it, GDPR/data protection
- [ ] **Terms of Service** — usage terms, intellectual property, liability limits
- [ ] **Refund Policy** — "100% refund within 24 hours of purchase, no questions asked"
- [ ] **Contact page** — email, WhatsApp, response time commitment
- [ ] **GST compliance** — if revenue exceeds ₹20L/year, register for GST; show GSTIN on invoices
- [ ] **Razorpay KYC** — complete merchant verification for live payments
- [ ] **Cookie consent** — if using analytics (GA4, PostHog, Meta Pixel)

Suggested footer links:
```
Privacy Policy · Terms of Service · Refund Policy · Contact · WhatsApp
© 2026 The Agent Engineer · Balaji Chippada
```

---

## 19. Implementation Checklist (Master)

### Week 1 — Stop the bleeding + core funnel

- [ ] Fix JS error banner
- [ ] Fix canonical/OG URLs
- [ ] Unify social proof numbers
- [ ] Dynamic hero CTA with specific masterclass
- [ ] Add scarcity line (real seat count)
- [ ] 3-step booking modal (sign in → details → pay)
- [ ] Replace alert() with confirmation screen
- [ ] Calendar .ics download on success
- [ ] Write booking to Firestore under user ID

### Week 2 — Dashboard + pricing + roadmap

- [ ] Student dashboard tab (My Masterclasses)
- [ ] Upcoming/past sessions, Join Live button
- [ ] Profile edit + inquiry form
- [ ] 3-tier pricing on masterclass cards
- [ ] Remove strikethrough discount UI
- [ ] Homepage roadmap teaser + email capture
- [ ] Contextual CTAs in roadmap phases
- [ ] Instructor bio with photo + LinkedIn

### Week 3 — Trust + mobile + lifecycle

- [ ] 5+ real testimonials with photos
- [ ] FAQ section (8+ questions)
- [ ] Who this is for / NOT for block
- [ ] Refund policy page
- [ ] Mobile sticky bottom bar
- [ ] WhatsApp floating button
- [ ] Confirmation email (SendGrid)
- [ ] WhatsApp confirmation (Gupshup/WATI)
- [ ] T-24h reminder automation
- [ ] Post-class email with recording

### Week 4 — Analytics + hardening

- [ ] GA4 + custom events
- [ ] PostHog funnel dashboard
- [ ] Meta Pixel for retargeting
- [ ] UTM links in YouTube descriptions
- [ ] First A/B test (hero CTA)
- [ ] esbuild/Vite build pipeline
- [ ] Firestore security rules
- [ ] Sentry error monitoring
- [ ] Custom domain setup
- [ ] Certificate PDF generator

### Week 5 — Growth loops

- [ ] NPS survey post-class
- [ ] Coupon system for upsells
- [ ] Exit-intent email capture
- [ ] YouTube video embed on homepage
- [ ] Launch second masterclass (Production RAG)
- [ ] Weekly funnel review process

---

## 20. Success Criteria — Definition of Done

The site is "V2 ready" when ALL of these are true:

### Conversion
- [ ] A new visitor from YouTube can go from landing → paid → dashboard in under 3 minutes
- [ ] No JS errors on page load (desktop + mobile)
- [ ] Overall conversion rate > 3% (visits → paid bookings)
- [ ] Zero `alert()` dialogs anywhere in the flow

### Product feel
- [ ] Paying customer sees confirmation screen with calendar download
- [ ] Customer can log in and see upcoming sessions in dashboard
- [ ] "Join Live" button works 15 min before session
- [ ] Post-class recording accessible from dashboard
- [ ] Certificate downloadable after attendance

### Trust
- [ ] Real instructor photo + LinkedIn visible
- [ ] 5+ real testimonials with full names
- [ ] FAQ + refund policy accessible
- [ ] All social proof numbers are verifiable and consistent

### Operations
- [ ] Confirmation email sent within 60 seconds of payment
- [ ] T-24h reminder sent automatically
- [ ] Admin can publish masterclass, attach Zoom link, upload recording
- [ ] Razorpay live mode active with proper KYC

### Technical
- [ ] Lighthouse Performance > 85
- [ ] Custom domain live
- [ ] Firestore security rules deployed
- [ ] Analytics tracking all funnel events
- [ ] No Babel Standalone in production

---

## Appendix A — Competitive Reference

Sites to study for UX patterns:

| Platform | What to steal |
|---|---|
| [Maven.com](https://maven.com) | Cohort-based course pages, instructor credibility, tier pricing |
| [Topmate.io](https://topmate.io) | 1:1 booking flow, Google sign-in, clean checkout |
| [GrowthSchool.io](https://growthschool.io) | Indian market pricing, WhatsApp integration, urgency |
| [Codedamn](https://codedamn.com) | Developer audience targeting, project-based outcomes |
| [Scaler Academy](https://scaler.com) | Tier pricing psychology, "who this is for" blocks |

## Appendix B — YouTube → Site Integration Playbook

| Touchpoint | Action |
|---|---|
| Video description | Link with UTM: `?utm_source=youtube&utm_medium=description&utm_campaign=roadmap` |
| Pinned comment | "Full roadmap + live masterclasses → [link]" |
| End screen | Card linking to coaching site |
| Community post | "Next Claude Code masterclass: Sat 7 Jun · 14 seats left → [link]" |
| Video chapter | At end of roadmap walkthrough: "Want to build this live? Link in description" |
| Shorts | 30s clip + "Link in bio" to coaching site |

## Appendix C — Revenue Projections (Conservative)

| Scenario | Visitors/mo | CR | Avg ticket | Monthly revenue |
|---|---|---|---|---|
| Month 1 (launch) | 2,000 | 2% | ₹999 | ₹39,960 |
| Month 3 (optimized) | 5,000 | 4% | ₹1,499 | ₹2,99,800 |
| Month 6 (2 classes/mo) | 8,000 | 5% | ₹1,499 | ₹5,99,600 |
| Month 12 (cohort model) | 10,000 | 6% | ₹2,999 | ₹17,99,400 |

Assumes: 17K YouTube subs generating ~5K site visits/month at maturity, plus roadmap SEO + community posts.

---

*This plan is a living document. Update after each cohort with real conversion data, testimonial quotes, and pricing learnings.*
