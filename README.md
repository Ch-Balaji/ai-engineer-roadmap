# AI Engineer Roadmap 2026

An interactive roadmap for becoming a production-ready AI engineer in 2026.

The site covers a 26-week learning path across Python foundations, LLM mental models, prompt engineering, cloud infrastructure, RAG, tools, MCP, single-agent systems, memory, multi-agent orchestration, guardrails, deployment, and capstone projects.

## Live Site

GitHub Pages:

https://ch-balaji.github.io/ai-engineer-roadmap/

## About

This roadmap is created by Balaji Chippada, an AI/ML practitioner and tutor who has worked across traditional machine learning, production-scale agentic AI systems, and AI/data science education.

The curriculum is designed around one idea:

> If I had to start all over again in 2026, this is how I would begin.

## Tech Stack

- Static HTML
- CSS
- React via CDN
- Babel standalone for JSX in the browser
- GitHub Pages for hosting

No build step is required.

## Run Locally

From the `site/` folder:

```bash
cd site
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

> **GitHub Pages:** After moving the site into `site/`, update the repo's Pages settings to publish from the `/site` folder (or copy `site/` contents to the branch root on deploy).

## Project Structure

```text
site/                  # Roadmap website (HTML, CSS, JS)
  index.html
  Roadmap.html
  app.jsx
  data.js
  styles.css
  uploads/
youtube/               # Scripts, skills, channel data
projects/              # Code demos and apps
media/                 # Audio, subtitles, thumbnails
docs/                  # Planning documents
partnerships/          # Partner agreements
```

## Contributing

This project is open source and open to contributions.

Contributions are welcome for:

- Improving the curriculum structure
- Adding better explanations or learning outcomes
- Fixing UI issues
- Improving accessibility and responsiveness
- Suggesting new capstone projects
- Updating tools, frameworks, or platform references

Please open an issue or pull request with a clear description of the change.

## License

No license has been added yet. If you want to reuse or adapt this project, please open an issue first.
