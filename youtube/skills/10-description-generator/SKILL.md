---

## name: description-generator
description: Generates a complete, SEO-optimized YouTube upload package (description, topic-shift timestamps, hybrid tag set, 5 title variants, pinned comment, Shorts hooks, hashtags) from an SRT file plus a video title and 1-line topic. Tuned for Roadmap-2026 channel — pulls links and branding from links.config.md so updates happen in one place.

# YouTube Description Generator

Use this skill **after** the video is recorded and the SRT is exported, **before** uploading. It produces everything that goes into the YouTube upload form.

## Required inputs (ask the user if missing — never assume)

1. **SRT file** — full transcript with timestamps (path or pasted content).
2. **Video title** — the final published title.
3. **Topic line** — one sentence describing what the video is about and the target keyword (e.g., *"Beginner-friendly RAG explained without LangChain — keyword: RAG tutorial"*).

If any of the three is missing, **stop and ask**. Do not invent a title or guess the topic from the SRT alone.

## Always-load files

Before generating, read:

- `links.config.md` (same folder) — links block, branding, hashtag pool. **Never hardcode links in output; always pull from this file.** If the user asks to change a link, edit `links.config.md`, not the SKILL.

## Output destination

- **Always write the final output to a single file inside `outputs/` (same folder as this skill).**
- Filename pattern: `outputs/<slugified-title>.md` (lowercase, hyphenated, no special chars). If the file exists, append a short numeric suffix (`-2`, `-3`, ...).
- The file must be **fully copy-paste-ready**: the YouTube paste block goes first inside a fenced code block so the user can copy it cleanly, followed by the supplementary sections (title variants, pinned comment, Shorts hooks).
- After writing, tell the user the absolute path to the file and a 1-line summary (chapter count, tag char count). Do not re-paste the full content into chat.

## Output format (deliver as a single ready-to-paste block)

```
[HASHTAGS — top 3, space-separated, above title in YouTube]

🔗 Join the WhatsApp Community
<URL from config>
<community blurb from config>

📚 Free Resources
• Free AI Engineer Roadmap 2026: <URL>
• Agentic AI Playlist: <URL>          ← always include
• Roadmap Video: <URL>

🌐 Connect with me
• LinkedIn: <URL>
• Instagram: <URL>

[DESCRIPTION INTRO]
3–5 sentences, ~600–800 characters, English only, medium SEO-optimized.
- Sentence 1: Hook tied to the title's promise.
- Sentence 2–3: What the viewer will learn / why it matters.
- Sentence 4–5: Who it's for + soft CTA to keep watching.
- Weave the target keyword in naturally 2–3 times. No stuffing. No emojis unless user requests.
- Note on placement: links live ABOVE the intro because viewers don't scroll. The intro still owns the SEO weight (target keyword appears in its first 1–2 sentences), but the links get the eyeballs.

⏱ Timestamps
00:00 <chapter title>
MM:SS <chapter title>
... (only at clear topic shifts — quality over quantity, even if 4–6 chapters)

🏷 Tags
<comma-separated, hybrid mix, ≤500 chars total — see Tag Strategy below>
```

Then, **below** the paste-ready block, output these as separate clearly-labeled sections:

### 5 Title Variants

Numbered list, each <60 chars, clickable, includes target keyword. Reuse formulas from `06-thumbnail-title-system` if available.

### Pinned Comment Draft

2–4 lines. Open with a question or value-add (not "thanks for watching"). Include WhatsApp link + one resource link. Invite a specific reply.

### 3–5 Shorts Hook Ideas

Pulled directly from the SRT — quote the exact timestamp range and the line that would hook a Shorts viewer in <3 seconds.

## Timestamp generation rules (topic-shifts only)

1. Parse the SRT into segments by **topic shift**, not by time interval. A shift is a clear change in what's being explained — not a sentence break.
2. **First chapter must be `00:00`** (YouTube requirement for chapters to render).
3. **Minimum 3 chapters** (YouTube requirement). If the video genuinely has fewer shifts, expand the most important section into 2 sub-chapters rather than padding with filler.
4. Density guide (soft):
  - <5 min video → 3–4 chapters
  - 5–15 min → 4–7 chapters
  - 15–30 min → 6–10 chapters
  - 30 min+ → 8–14 chapters
5. Chapter title rules:
  - 3–7 words
  - Curiosity or value-forward (`"Why RAG fails in production"` not `"RAG problems"`)
  - No numbering prefix (no `1.`, `Part 1:` etc.)
  - Mirror the viewer's question, not the speaker's outline
6. Each chapter must be **≥10 seconds long** (YouTube requirement) and timestamps must be in ascending order.

## Tag Strategy (hybrid mix, ≤500 chars total)

Build the tag list in this order, stopping at ~480 chars to leave a safety margin:

1. **Branded (3–5 tags):** `Balaji Chippada`, `AI Engineer Roadmap 2026`, `Roadmap 2026`, channel-specific terms.
2. **Topic-core (8–12 tags):** the exact target keyword + tight variants (e.g., `RAG tutorial`, `RAG explained`, `Retrieval Augmented Generation`).
3. **Niche/long-tail (8–12 tags):** specific tools, libraries, sub-concepts mentioned in the SRT (e.g., `vector database`, `embeddings python`, `chunking strategy`).
4. **Broad umbrella (4–6 tags):** `AI`, `Machine Learning`, `Generative AI`, `LLM`, `Artificial Intelligence` — only the ones genuinely relevant.

**Never** include unrelated trending tags. **Never** repeat near-duplicates that only differ in casing.

## Description intro — SEO checklist

Before finalizing the intro, verify:

- Target keyword appears in the **first 1–2 sentences** (above-the-fold for search).
- Total length **600–800 characters** (medium SEO sweet spot).
- No clickbait — every claim is delivered in the video.
- Reads like a human wrote it, not a keyword-stuffer.
- No emojis in the intro paragraph itself (emojis only as section markers below).

## Pinned comment template

```
<One-line value add or question tied to the video's main idea.>
👉 Join the WhatsApp community of serious AI learners: <link>
📘 Full Free Roadmap: <link>
Drop your biggest doubt below — I read every comment.
```

## Workflow

1. Confirm all 3 required inputs are present. If not, ask once and wait.
2. Read `links.config.md`.
3. Parse SRT → identify topic shifts → draft chapters → validate against timestamp rules.
4. Draft description intro → run SEO checklist.
5. Build tag list → verify ≤500 chars.
6. Generate 5 title variants, pinned comment, Shorts hooks, hashtags.
7. Output the paste-ready block first, then the supplementary sections.
8. End with: *"Update `links.config.md` if any link or CTA changed."*

## Don't do this

- Don't hardcode links — always read from `links.config.md`.
- Don't generate timestamps by fixed time intervals; use topic shifts.
- Don't add Telugu phrases unless the user explicitly asks for this video.
- Don't pad the description with filler keywords or hashtag dumps.
- Don't suggest tags for topics not actually covered in the SRT.

