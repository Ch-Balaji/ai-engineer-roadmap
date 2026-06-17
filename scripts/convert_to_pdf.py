"""
Markdown → PDF converter using the weasyprint pipeline.

Pipeline:
  1. Read .md file
  2. markdown lib → HTML (with fenced_code, codehilite, tables, etc.)
  3. Wrap in styled HTML template with CSS
  4. weasyprint → pixel-perfect PDF

Usage:
  python scripts/convert_to_pdf.py                          # converts all files in the list
  python scripts/convert_to_pdf.py "path/to/file.md"        # converts a single file
"""

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import sys, os, pathlib, re

# ── Configuration ────────────────────────────────────────────────────────────

DEFAULT_FILES = []

OUTPUT_DIR = None  # Auto-detect: places PDF in _PDF/ folder next to the source file

# ── Markdown extensions ──────────────────────────────────────────────────────

EXTENSIONS = [
    "fenced_code",
    "codehilite",
    "tables",
    "toc",
    "sane_lists",
    "nl2br",
    "attr_list",
    "def_list",
    "smarty",
]

EXTENSION_CONFIGS = {
    "codehilite": {
        "guess_lang": True,
        "use_pygments": True,
        "noclasses": True,
        "pygments_style": "friendly",
    },
}

# ── CSS ──────────────────────────────────────────────────────────────────────

CSS_STYLE = """
@page {
    size: A4;
    margin: 20mm 18mm 22mm 18mm;
    @bottom-center {
        content: counter(page) " of " counter(pages);
        font-size: 8pt;
        color: #888;
    }
}

body {
    font-family: "Helvetica Neue", "Arial Unicode MS", "Apple Color Emoji", "Segoe UI Emoji", Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.65;
    color: #1a1a1a;
}

h1 {
    font-size: 20pt; font-weight: 700; color: #0d47a1;
    border-bottom: 2.5px solid #0d47a1;
    padding-bottom: 4px; margin-top: 0; margin-bottom: 14px;
}
h2 {
    font-size: 14pt; font-weight: 700; color: #1565c0;
    border-bottom: 1.5px solid #90caf9;
    padding-bottom: 3px; margin-top: 22px; margin-bottom: 8px;
    page-break-after: avoid;
}
h3 {
    font-size: 11.5pt; font-weight: 700; color: #1976d2;
    margin-top: 16px; margin-bottom: 6px;
    page-break-after: avoid;
}
h4 {
    font-size: 10.5pt; font-weight: 700; color: #333;
    margin-top: 12px; margin-bottom: 4px;
}

p { margin: 0 0 9px 0; }

div.codehilite, .highlight {
    background: #f3f4f6;
    border: 1px solid #d1d5db;
    border-left: 4px solid #1565c0;
    border-radius: 4px;
    padding: 10px 14px;
    margin: 10px 0 14px 0;
    overflow-x: auto;
    page-break-inside: avoid;
}
div.codehilite pre, .highlight pre {
    margin: 0;
    font-family: Menlo, "Courier New", monospace;
    font-size: 8.5pt; line-height: 1.5;
    white-space: pre-wrap; word-break: break-all;
}

pre {
    background: #f3f4f6;
    border: 1px solid #d1d5db;
    border-left: 4px solid #1565c0;
    border-radius: 4px;
    padding: 10px 14px;
    margin: 10px 0 14px 0;
    font-family: Menlo, "Courier New", monospace;
    font-size: 8.5pt; line-height: 1.5;
    white-space: pre-wrap; word-break: break-all;
    page-break-inside: avoid;
}

code {
    font-family: Menlo, "Courier New", monospace;
    font-size: 8.5pt;
    background: #e8eaf6; border: 1px solid #c5cae9;
    border-radius: 3px; padding: 1px 4px; color: #1a237e;
}
pre code {
    background: none; border: none; padding: 0; color: inherit;
}

table {
    border-collapse: collapse; width: 100%;
    margin: 14px 0; font-size: 9pt;
    page-break-inside: avoid;
}
th {
    background: #1565c0; color: #fff; font-weight: 700;
    padding: 7px 10px; text-align: left; border: 1px solid #1565c0;
}
td {
    padding: 6px 10px; border: 1px solid #cbd5e1; vertical-align: top;
}
tr:nth-child(even) td { background: #f0f4ff; }
tr:nth-child(odd)  td { background: #ffffff; }

ul, ol { margin: 6px 0 10px 0; padding-left: 22px; }
li { margin-bottom: 4px; }
li > ul, li > ol { margin-top: 3px; margin-bottom: 3px; }

hr { border: none; border-top: 1.5px solid #e2e8f0; margin: 18px 0; }

blockquote {
    border-left: 4px solid #90caf9; background: #f0f7ff;
    margin: 10px 0; padding: 8px 14px;
    color: #444; font-style: italic;
}

a { color: #1565c0; text-decoration: none; }

strong { font-weight: 700; color: #111; }
em { font-style: italic; }

details { margin: 8px 0; }
summary { font-weight: 700; color: #1565c0; }
"""


def sanitize_code_blocks_in_md(md_text: str) -> str:
    replacements = {
        '₹': 'Rs.',
        '×': 'x',
        '→': '->',
        '←': '<-',
        '▼': 'v',
        '▲': '^',
        '►': '>',
        '◄': '<',
        '─': '-',
        '│': '|',
        '┌': '+',
        '┐': '+',
        '└': '+',
        '┘': '+',
        '├': '+',
        '┤': '+',
        '┬': '+',
        '┴': '+',
        '┼': '+',
        '╔': '+',
        '╗': '+',
        '╚': '+',
        '╝': '+',
        '║': '|',
        '═': '=',
        '—': '--',
        '\ufe0f': '',
    }

    emoji_pattern = re.compile(r'[\U0001F300-\U0001FAFF\u2600-\u27BF\u2705\u274C\u26A0]')

    def _replace_block(m):
        fence_open = m.group(1)
        content = m.group(2)
        fence_close = m.group(3)
        for char, repl in replacements.items():
            content = content.replace(char, repl)
        content = emoji_pattern.sub('', content)
        return fence_open + content + fence_close

    pattern = re.compile(r'(```[^\n]*\n)(.*?)(```)', re.DOTALL)
    return pattern.sub(_replace_block, md_text)


def expand_details_blocks(md_text: str) -> str:
    def _replace(m):
        summary = m.group(1).strip()
        inner = m.group(2).strip()
        return f"**{summary}**\n\n{inner}"

    pattern = re.compile(
        r'<details>\s*<summary>(.*?)</summary>(.*?)</details>',
        re.DOTALL,
    )
    return pattern.sub(_replace, md_text)


def convert_md_to_pdf(md_path: str, output_dir: str = None) -> str:
    src = pathlib.Path(md_path)
    md_text = src.read_text(encoding="utf-8")

    if output_dir is None:
        output_dir = str(src.parent / "_PDF")

    md_text = expand_details_blocks(md_text)
    md_text = sanitize_code_blocks_in_md(md_text)

    md = markdown.Markdown(
        extensions=EXTENSIONS,
        extension_configs=EXTENSION_CONFIGS,
    )
    body_html = md.convert(md_text)

    title = src.stem.replace("_", " ").title()
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"/><title>{title}</title></head>
<body>
{body_html}
</body>
</html>"""

    os.makedirs(output_dir, exist_ok=True)
    out_name = src.stem + ".pdf"
    out_path = os.path.join(output_dir, out_name)

    font_config = FontConfiguration()
    HTML(string=full_html).write_pdf(
        out_path,
        stylesheets=[CSS(string=CSS_STYLE, font_config=font_config)],
        font_config=font_config,
    )
    return out_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = [sys.argv[1]]
    else:
        files = DEFAULT_FILES

    for md_file in files:
        if not os.path.exists(md_file):
            print(f"Skipped (not found): {md_file}")
            continue
        out = convert_md_to_pdf(md_file)
        print(f"OK: {md_file} -> {out}")

    print("Done!")
