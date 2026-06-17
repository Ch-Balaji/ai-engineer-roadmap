---
name: visual-identity
description: Locks the two-system visual brand for Balaji Chippada's channel — the editorial Roadmap-2026 site palette (cream + rust + teal + serif italic) and the high-CTR YouTube thumbnail style (black bg + circuit pattern + yellow knockout text + brown bomber jacket subject + Telugu accent badge). Use when designing slides, lower-thirds, sketchbook pages, brochures, GitHub READMEs, or thumbnails.
---

# Visual Identity

The brand has **two visual systems**, deliberately. They serve different surfaces. Don't merge them.

## System A — Editorial / Curriculum (the Roadmap site)

Used for: the roadmap website (`site/Roadmap.html` + `site/styles.css`), curriculum brochures, slide decks inside videos, GitHub README headers, course PDFs.

**Mood**: Premium, calm, editorial. Like a serious publication, not a coding bootcamp ad.

### Palette (locked)

| Role | Hex | Where it appears |
|---|---|---|
| Background (primary) | `#F5EFE6` cream | Site bg, slide bg, deck bg |
| Background (paper) | `#FAF6EE` lighter cream | Card bg, callout bg |
| Accent (primary) | `#C2562F` rust orange | Italic serif words, key highlights, "Phase" markers |
| Accent (deep) | `#0F4C4A` teal-deep | Phase 1 cards, primary buttons, headings |
| Accent (mid) | `#3A8F8C` teal | Phase 2 cards |
| Accent (warm) | `#D6A04A` mustard | Phase 6, callouts |
| Accent (sweet) | `#E4577A` pink | Capstone projects, highlights |
| Accent (royal) | `#6B4E8A` purple | Phase 3, secondary headings |
| Text (primary) | `#1A1A1A` near-black | Body |
| Text (muted) | `#6E665C` warm grey | Secondary, metadata |

(See repo's `site/data.js` `PHASE_COLORS` and `site/styles.css` for the canonical CSS variables.)

### Typography (System A)

- **Display headings**: Bold sans-serif (Inter Tight Bold / Geist Bold) — black text
- **Italic accent words**: Serif italic (Playfair Display Italic / EB Garamond Italic) — rust `#C2562F`
- **Body**: Inter / system sans, regular, near-black
- **Labels / numbers**: Geist Mono / JetBrains Mono — small caps `01`, `02`, `03`

The signature treatment: a sans bold sentence with **one or two words swapped to serif italic in rust orange** (e.g., "The path from *script kid* to agent engineer"). Use this for hero / phase intros / video opening title cards.

### Layout language

- Phase cards: rounded corners (12–16px), solid color fill, white text, large numeral top-left, week-range bottom-left
- "Difficulty" indicator: 5 circles, filled in the phase's accent color
- Generous whitespace around editorial blocks
- No drop shadows, no gradients, no glassmorphism — flat editorial

---

## System B — YouTube Thumbnails

Used for: YouTube thumbnails only. (And matching YouTube end-screen cards.) Not for slides, not for the website.

**Mood**: Loud, punchy, algorithm-friendly. High contrast. Indian YouTube CTR optimized.

Reference examples in `media/thumbnails/` folder:
- `thumbnail2.jpeg` — "BEST PRODUCTION LEVEL AGENTIC AI ENGINEER IN 2026" — the canonical template
- `ChatGPT Image May 3, 2026, 01_58_34 PM.png` — channel-trailer / about-style thumbnail with handwritten arrows
- `ChatGPT Image May 7, 2026, 11_41_33 PM.png` — "FREE AI COURSE NOT FOR EVERYONE" — provocation style

### Locked thumbnail elements (every video uses these)

| Element | Spec |
|---|---|
| Background | Black `#0A0A0A` to dark navy, with subtle circuit-board / neural-net pattern overlay (10–15% opacity) |
| Subject | Balaji, well-lit (warm rim light), in **brown bomber jacket** + black inner zip-up (the canal-photo outfit) |
| Subject pose | Confident, looking at camera, slight smile or expressive face matching video tone |
| Subject placement | Right third (when text-heavy) or center (when subject-led) |
| Primary text | Bold condensed sans-serif (Anton / Bebas Neue / Tungsten), ALL CAPS, white `#FFFFFF` |
| Highlight text | Same font, bright yellow `#FFD60A`, used for the 1–2 most important words |
| Highlight background | Yellow `#FFD60A` brush-stroke band behind the highlight word (rough edges, hand-painted feel) |
| Telugu accent | Telugu text (e.g., "అవ్వడం ఎలా?", "తెలుగులో FULL GUIDE") in bottom-right or bottom-left badge — red `#E63946` or yellow on dark, readable on mobile |
| Social proof badge | Top-left or top-right corner: "50K+ VIEWS" / "8+ YEARS" / "3000+ STUDENTS" — small, on red or dark badge |
| Tech-stack icon row | Bottom strip showing 4–6 logos relevant to the video (Python, LangGraph, AWS, Claude, etc.) — only on tutorial-type thumbnails |

### Text rules

- 3 to 5 words max in the main hero text
- 1 highlight word (yellow + brush band) per thumbnail
- Telugu accent text is short — 2–4 Telugu words max
- Mobile-readability test: thumbnail must be parseable at 320×180 pixels

### When to break the template

- **Channel-trailer / about-style** (e.g., May 3 thumbnail): hand-drawn arrows + sticker badges + warm desk-lamp lighting. Used once per quarter, not per-video.
- **Pure provocation / hot take** (e.g., "FREE AI COURSE NOT FOR EVERYONE"): drop the tech-stack icon row, give the type more room, keep yellow brush band as the only accent.

Detailed thumbnail production rules (CapCut / Photoshop / Canva instructions): see [THUMBNAIL_RULES.md](THUMBNAIL_RULES.md).

---

## In-Video Visual System (overlays, lower-thirds, sketchbook)

The video itself uses System A's editorial palette, NOT the thumbnail's loud yellow.

| Element | Spec |
|---|---|
| Lower-third (name + topic) | Cream `#F5EFE6` band, near-black text, rust `#C2562F` accent line. ~10% screen height. Bottom-left, 30%–40% width. |
| Section transitions | Phase number large (`PHASE 04`) in rust italic serif, sub-text in sans. 1.5s hold. |
| Code overlays | Dark editor theme (One Dark / Dracula) — but the SLIDE around the code stays cream. Code is the only dark element. |
| Sketchbook (GoodNotes iPad sidecar) | Cream paper background, near-black ink, accent annotations in rust `#C2562F` and teal-deep `#0F4C4A`. Avoid yellow/pink markers (clash with editorial palette). |
| Insta360 webcam PiP | Bottom-right corner, soft rounded mask, ~22% screen width. Subtle 1px cream border. |
| Captions (burned in via CapCut) | White text, bold sans, 1px black outline. Yellow `#FFD60A` highlight on the keyword being emphasized — this is the ONE place yellow appears in-video, deliberately echoing the thumbnail. |

## File / Asset Naming

- Slide deck: `slides/{video_number}_{slug}.key` (Keynote) or `.pdf`
- Sketchbook export: `sketchbook/{video_number}_{slug}.pdf`
- Thumbnail source: `media/thumbnails/{video_number}_{slug}_thumb.png` (1920×1080, exported at 80% JPEG for upload)
- Sketchbook page within: numbered `01`, `02` for sequence

## Quality Pass

Before publishing any visual deliverable:

- [ ] Editorial deliverables: ONLY use System A palette. No yellow, no neon.
- [ ] Thumbnails: USE the brown bomber jacket subject (not a different outfit).
- [ ] Thumbnail title is 3–5 words, with exactly one yellow-highlight word.
- [ ] Telugu accent text on thumbnail is present and short.
- [ ] Lower-third in video is cream + rust, not yellow.
- [ ] Sketchbook page uses rust + teal-deep accents, not pink/yellow markers.
