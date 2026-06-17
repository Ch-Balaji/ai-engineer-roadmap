# Thumbnail Production Rules

Step-by-step instructions to recreate the locked thumbnail style for every video. Tools assumed: CapCut (your editor), Photoshop / Photopea / Canva (any of them), or AI image tools (ChatGPT image, Midjourney) for the background.

## Canonical reference: `media/thumbnails/thumbnail2.jpeg`

Study this thumbnail before producing a new one. Match these elements exactly unless the video type calls for the alternates below.

## Asset checklist (gather before starting)

- [ ] Subject photo of Balaji in **brown bomber jacket + black zip-up** (canal-style key shot exists; reuse or shoot variants in the same outfit)
- [ ] Background: dark with subtle circuit-board / neural-net pattern overlay
- [ ] Tech-stack logos relevant to the video (Python, LangGraph, OpenAI, Claude, AWS, LangChain, Pinecone, etc.) — keep a folder `media/thumbnails/_assets/logos/`
- [ ] Yellow brush-stroke PNG (transparent) for highlight bands — keep in `media/thumbnails/_assets/brushes/`
- [ ] Telugu text in installed font (Lohit Telugu / Noto Sans Telugu — bold weight)

## Step 1 — Background

1. Start with a 1920×1080 canvas.
2. Fill with `#0A0A0A` (near-black).
3. Add circuit-board / neural-net texture overlay at 10–15% opacity. Lean toward warm orange-tinted glow on the subject's side, blue-tinted on the opposite side, for cinematic lighting.
4. (Alternate for "warm-desk" trailer thumbnails: warm dark room, table lamp, books, plant — see `ChatGPT Image May 3, 2026` reference.)

## Step 2 — Subject placement

1. Cutout Balaji from his reference photo. Use Photoshop "Select Subject" or Photopea equivalent.
2. Add a 4–8 px white outer glow / stroke around the subject (this is the "sticker pop" look — see canonical thumbnail2.jpeg).
3. Place subject:
   - **Right third** of canvas if the title text is 4+ words and dominates the left.
   - **Center** if the title is short (3 words) and subject is the main story (e.g., "FREE AI COURSE NOT FOR EVERYONE").
4. Match the lighting: warm rim light from upper-right makes the subject pop on dark backgrounds.

## Step 3 — Primary title text

1. Font: **Anton** (default) or **Bebas Neue** or **Tungsten**. Bold condensed sans-serif. ALL CAPS.
2. Size: largest word at ~150–200px on a 1920×1080 canvas.
3. Stack the title across 2–3 lines maximum.
4. Color: `#FFFFFF` white for most words.
5. Pick **one** word to highlight in yellow `#FFD60A`. This is usually the noun the curiosity hangs on (`AGENTIC AI`, `FREE`, `BROKEN`, `PRODUCTION`).
6. Behind the highlighted word, place a yellow brush-stroke band PNG. Slightly rotated (-2 to -5 degrees), with rough edges visible.
7. Add a 2–3 px black outline to ALL text for mobile readability.

## Step 4 — Telugu accent badge

1. Font: **Noto Sans Telugu Bold** or **Lohit Telugu Bold**.
2. Short Telugu phrase: 2–4 words. Examples:
   - "అవ్వడం ఎలా?" (How to become?)
   - "తెలుగులో FULL GUIDE" (Full guide in Telugu)
   - "ఇంకా టైం ఉంది" (There is still time)
   - "ఇది అందరికీ కాదు" (This is not for everyone)
3. Place in a **red `#E63946`** rounded badge (bottom-right corner is default).
4. Yellow text on red, OR white text on red. White on red is more readable on mobile.
5. Small size: ~50–70 px tall — accent, not headline.

## Step 5 — Social-proof badge (when honest)

1. Top-left or top-right corner.
2. Red badge `#E63946` or dark `#1A1A1A` badge.
3. Text examples (only use what's TRUE):
   - "50K+ VIEWS" — once a video crosses 50k
   - "8+ YEARS IN AI & ML" — fine for evergreen authority videos
   - "3000+ STUDENTS MENTORED" — only if accurate
4. Never inflate numbers. The audience checks. (`no-clickbait` non-negotiable)

## Step 6 — Tech-stack icon row (tutorial videos only)

1. Bottom strip — 4 to 6 logos relevant to the video.
2. Each logo on its own dark rounded card with the logo name underneath in small caps.
3. Logos at consistent height, evenly spaced.
4. Skip this row for: motivational videos, hot-take videos, trailer-style videos.

## Step 7 — Final polish

- Add a subtle vignette (darker corners) to focus the eye on subject + title.
- Bump global contrast slightly so text doesn't get muddy on small mobile displays.
- Run the **mobile readability test**: scale the export to 320×180 and check that the highlight word is still legible.
- Export as PNG (master) and JPG (~80% quality) for upload.

## Quick decision tree per video type

```
Is this a tutorial / roadmap-phase video?
└─ YES → Full template: bg + subject + title + Telugu badge + social-proof + tech-stack row
└─ NO ↓

Is this a hot-take / motivational / job-market video?
└─ YES → Drop the tech-stack row. Give the title more space. Subject more central.
└─ NO ↓

Is this a channel trailer / about / quarterly hero?
└─ YES → Switch to warm-desk-lamp aesthetic (May 3 reference): hand-drawn arrows, sticker callouts ("PRODUCTION AI PROJECTS", "8+ YEARS IN AI & ML").
└─ NO ↓

Is this a Sunday live (replay)?
└─ YES → Add red "LIVE" badge. Otherwise normal template, but with a question on the thumbnail (e.g., "MY RAG IS BROKEN — HELP").
```

## Anti-patterns

- ❌ Wearing a different outfit. Channel signature outfit is brown bomber jacket + black zip-up.
- ❌ More than 5 words in the title.
- ❌ More than 1 yellow highlight word.
- ❌ Pure white background.
- ❌ Tiny text that fails the 320×180 mobile test.
- ❌ Cluttered: subject + 2 logos + 5 badges + 8 lines of text. Pick one focal point.
- ❌ Generic stock-photo subject. Always use Balaji's actual photo (consistency builds face recognition).
