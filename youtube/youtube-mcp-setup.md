# YouTube MCP Setup — Complete Guide (Cursor + @balajichippada)

This document records **every step** to connect Cursor to your YouTube channel via the community [`youtube-studio-mcp`](https://github.com/pauling-ai/youtube-mcp-server) server. It uses Google's official YouTube APIs under the hood — there is **no official Google YouTube MCP** as of May 2026.

**Channel:** [@balajichippada](https://www.youtube.com/@balajichippada)  
**Config level:** User-level (applies to all Cursor projects on this machine)  
**Last verified:** May 29, 2026 on macOS (Homebrew Python 3.14)

---

## Table of contents

1. [What you get](#1-what-you-get)
2. [Prerequisites](#2-prerequisites)
3. [Google Cloud — create project](#3-google-cloud--create-project)
4. [Google Cloud — enable APIs](#4-google-cloud--enable-apis)
5. [Google Cloud — OAuth consent screen](#5-google-cloud--oauth-consent-screen)
6. [Google Cloud — add test users](#6-google-cloud--add-test-users)
7. [Google Cloud — create OAuth credentials & download JSON](#7-google-cloud--create-oauth-credentials--download-json)
8. [Install youtube-studio-mcp locally](#8-install-youtube-studio-mcp-locally)
9. [Configure Cursor MCP (user-level)](#9-configure-cursor-mcp-user-level)
10. [Copy credentials & run first login](#10-copy-credentials--run-first-login)
11. [Restart Cursor & verify MCP is connected](#11-restart-cursor--verify-mcp-is-connected)
12. [Verify channel access from terminal](#12-verify-channel-access-from-terminal)
13. [What you can ask Cursor to do](#13-what-you-can-ask-cursor-to-do)
14. [YouTube policy reminders (do not skip)](#14-youtube-policy-reminders-do-not-skip)
15. [Troubleshooting](#15-troubleshooting)
16. [Security & file locations](#16-security--file-locations)
17. [Re-auth, update, or uninstall](#17-re-auth-update-or-uninstall)

---

## 1. What you get

The MCP exposes **40 tools** including:

| Category | Examples |
|----------|----------|
| **Analytics** | Channel overview, top videos, retention, traffic sources, demographics |
| **Comments** | List comments, draft/post replies (approve before posting) |
| **Metadata** | Update titles, descriptions, tags |
| **Playlists** | Create playlists, add/remove videos |
| **SEO** | Search suggestions, trending (search costs quota) |
| **Reporting** | Bulk CSV exports via YouTube Reporting API |

**Not available via API** (still manual in YouTube Studio): end screens, cards, pin comments, community tab posts, real-time analytics.

---

## 2. Prerequisites

- **Cursor** installed
- **Python 3.11+** (check with `python3 --version`)
- **Google account that OWNS the YouTube channel** — not a channel manager. Analytics API requires the owner account.
- **Google Cloud project** (free tier is fine; API quota is 10,000 units/day by default)
- ~20 minutes for one-time setup

---

## 3. Google Cloud — create project

1. Open [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with the Google account that **owns** `@balajichippada`
3. Click the project dropdown (top bar) → **New Project**
4. Name it e.g. `roadmap-2026-youtube-mcp`
5. Click **Create**
6. Make sure this project is **selected** in the top bar before continuing

---

## 4. Google Cloud — enable APIs

With your project selected, enable **all three** APIs. For each link, click **Enable**:

| API | Direct link |
|-----|-------------|
| YouTube Data API v3 | https://console.cloud.google.com/apis/library/youtube.googleapis.com |
| YouTube Analytics API | https://console.cloud.google.com/apis/library/youtubeanalytics.googleapis.com |
| YouTube Reporting API | https://console.cloud.google.com/apis/library/youtubereporting.googleapis.com |

**Verify:** Go to **APIs & Services → Enabled APIs & services** — all three should appear.

---

## 5. Google Cloud — OAuth consent screen

Google moved this to **Google Auth Platform**. Navigation:

1. Open **APIs & Services → OAuth consent screen**, or go to [Google Auth Platform](https://console.cloud.google.com/auth/overview)
2. Select your project (`roadmap-2026-youtube-mcp`)

### Branding (if prompted)

1. Left sidebar → **Branding**
2. Fill required fields:
   - **App name:** `Roadmap 2026 YouTube MCP` (or any name you recognize)
   - **User support email:** your email
   - **Developer contact email:** your email
3. Save

### Audience / publishing status

1. Left sidebar → **Audience**
2. **User type:** External
3. **Publishing status:** should be **Testing** (correct for personal use — no Google verification needed)

---

## 6. Google Cloud — add test users

While the app is in **Testing** mode, **only listed test users** can sign in. If you skip this, you get:

> `Error 403: access_denied` — app has not completed Google verification process

### Steps

1. Left sidebar → **Audience**
2. Scroll to **Test users**
3. Click **Add users**
4. Add the **exact** Google email that owns the channel, e.g.:
   ```
   balajirokzzz1234@gmail.com
   ```
5. Save
6. Wait 1–2 minutes before retrying login

**Direct link (replace project ID if different):**

https://console.cloud.google.com/auth/audience?project=roadmap-2026-youtube-mcp

---

## 7. Google Cloud — create OAuth credentials & download JSON

You need the **full JSON file** — the client ID string alone is **not enough** (the file also contains `client_secret`).

### Steps

1. Go to [Credentials](https://console.cloud.google.com/apis/credentials)
2. Click **+ Create Credentials → OAuth client ID**
3. If prompted to configure consent screen first, complete [Section 5](#5-google-cloud--oauth-consent-screen)
4. **Application type:** `Desktop app` (important — not "Web application")
5. **Name:** e.g. `Cursor YouTube MCP`
6. Click **Create**
7. Click **Download JSON** (download icon)
8. The file will look like:
   ```
   client_secret_XXXXX-YYYY.apps.googleusercontent.com.json
   ```

### What the JSON contains (do not share publicly)

```json
{
  "installed": {
    "client_id": "809094573307-....apps.googleusercontent.com",
    "client_secret": "GOCSPX-....",
    "project_id": "roadmap-2026-youtube-mcp",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    ...
  }
}
```

---

## 8. Install youtube-studio-mcp locally

On macOS with Homebrew Python, **do not** `pip install` globally (PEP 668 blocks it). Use a dedicated venv in your home directory.

### 8.1 Create directories

```bash
mkdir -p ~/.youtube-mcp
```

### 8.2 Create virtual environment and install

```bash
python3 -m venv ~/.youtube-mcp/venv
~/.youtube-mcp/venv/bin/pip install --upgrade pip
~/.youtube-mcp/venv/bin/pip install youtube-studio-mcp
```

### 8.3 Verify binary exists

```bash
ls -la ~/.youtube-mcp/venv/bin/youtube-studio-mcp
```

Expected: executable file at that path.

### 8.4 (Optional) Alternative install with pipx

If you prefer a global CLI tool manager:

```bash
brew install pipx
pipx ensurepath
pipx install youtube-studio-mcp
```

Then use `which youtube-studio-mcp` for the path in Cursor config instead of the venv path.

---

## 9. Configure Cursor MCP (user-level)

Cursor reads MCP servers from **`~/.cursor/mcp.json`** (user-level = all projects).

### 9.1 Edit the file

Open or create `~/.cursor/mcp.json`:

```bash
open ~/.cursor/mcp.json
# or: nano ~/.cursor/mcp.json
```

### 9.2 Add this configuration

Replace `taachba5` with your macOS username if different:

```json
{
  "mcpServers": {
    "youtube-studio": {
      "type": "stdio",
      "command": "/Users/taachba5/.youtube-mcp/run-mcp.sh",
      "env": {
        "YOUTUBE_MCP_CLIENT_SECRET": "/Users/taachba5/.youtube-mcp/client_secret.json",
        "YOUTUBE_MCP_CONFIG_DIR": "/Users/taachba5/.youtube-mcp"
      }
    }
  }
}
```

> **Important:** Cursor requires `"type": "stdio"` for local MCP servers. Without it, the server may show red/error immediately after restart.

Create the launcher script once:

```bash
cat > ~/.youtube-mcp/run-mcp.sh << 'EOF'
#!/bin/bash
export YOUTUBE_MCP_CLIENT_SECRET="/Users/taachba5/.youtube-mcp/client_secret.json"
export YOUTUBE_MCP_CONFIG_DIR="/Users/taachba5/.youtube-mcp"
exec /Users/taachba5/.youtube-mcp/venv/bin/python -m youtube_mcp.server
EOF
chmod +x ~/.youtube-mcp/run-mcp.sh
```

### 9.3 User-level vs project-level

| Location | Scope |
|----------|-------|
| `~/.cursor/mcp.json` | **All Cursor workspaces** (what we use) |
| `<project>/.cursor/mcp.json` | **Single project only** |

To scope YouTube MCP to one repo only, move the `youtube` block to that project's `.cursor/mcp.json` and remove it from `~/.cursor/mcp.json`.

---

## 10. Copy credentials & run first login

### 10.1 Copy OAuth JSON to the MCP config directory

**Never leave the JSON in your git repo.** Copy it to the home config folder:

```bash
cp ~/Downloads/client_secret_*.json ~/.youtube-mcp/client_secret.json
```

If you downloaded to the project folder instead:

```bash
cp "/Users/taachba5/Documents/Roadmap 2026/client_secret_"*.json ~/.youtube-mcp/client_secret.json
```

### 10.2 Validate JSON structure (optional)

```bash
python3 -c "
import json
p = '$HOME/.youtube-mcp/client_secret.json'
d = json.load(open(p))
k = 'installed' if 'installed' in d else 'web'
print('OK:', k, 'client, project:', d[k].get('project_id'))
"
```

Expected: `OK: installed client, project: roadmap-2026-youtube-mcp`

### 10.3 Create the one-time auth helper script

Save as `~/.youtube-mcp/authenticate.py`:

```python
#!/usr/bin/env python3
"""One-time OAuth setup for youtube-studio-mcp."""

import sys
from pathlib import Path

from youtube_mcp.auth import AuthError, YouTubeAuth

HOME = Path.home()
CONFIG = HOME / ".youtube-mcp"


def main() -> int:
    auth = YouTubeAuth(
        client_secret_path=CONFIG / "client_secret.json",
        config_dir=CONFIG,
    )
    try:
        auth.authenticate()
    except AuthError as exc:
        print(f"Auth failed: {exc}", file=sys.stderr)
        return 1

    status = auth.status()
    print("Authenticated successfully.")
    print(f"Token saved to: {status.get('token_path')}")
    print(f"Scopes: {', '.join(status.get('scopes', []))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### 10.4 Run login

```bash
~/.youtube-mcp/venv/bin/python ~/.youtube-mcp/authenticate.py
```

### 10.5 What happens in the browser

1. Browser opens (or a URL is printed — open it manually)
2. Sign in with the **test user email** you added in [Section 6](#6-google-cloud--add-test-users)
3. You may see: **"Google hasn't verified this app"**
   - Click **Advanced**
   - Click **Go to Roadmap 2026 YouTube MCP (unsafe)** — normal for personal OAuth apps
4. Click **Allow** for all requested permissions
5. Terminal should print:

   ```
   Authenticated successfully.
   Token saved to: /Users/taachba5/.youtube-mcp/token.json
   Scopes: https://www.googleapis.com/auth/youtube.readonly, ...
   ```

### 10.6 Scopes granted

The MCP requests these OAuth scopes:

- `youtube.readonly` — read public/private channel data
- `youtube` — manage channel (metadata, playlists, comments)
- `youtube.upload` — upload videos
- `yt-analytics.readonly` — analytics reports
- `yt-analytics-monetary.readonly` — revenue data (if in YPP)

---

## 11. Restart Cursor & verify MCP is connected

MCP config is loaded at startup.

1. **Quit Cursor completely** — Cmd+Q (not just close the window)
2. Reopen Cursor
3. Go to **Cursor Settings → MCP** (or **Features → MCP**)
4. Find server named **`youtube`**
5. Status should be **green / connected**
6. If red, click refresh and check [Troubleshooting](#15-troubleshooting)

---

## 12. Verify channel access from terminal

Run this **without opening Cursor** to confirm the token works:

```bash
~/.youtube-mcp/venv/bin/python -c "
from youtube_mcp.auth import YouTubeAuth
from pathlib import Path

auth = YouTubeAuth(
    client_secret_path=Path.home() / '.youtube-mcp/client_secret.json',
    config_dir=Path.home() / '.youtube-mcp',
)
yt = auth.build_youtube_service()
resp = yt.channels().list(part='snippet,statistics', mine=True).execute()
ch = resp['items'][0]
s, st = ch['snippet'], ch['statistics']
print('Channel:', s['title'])
print('Handle:', s.get('customUrl', 'N/A'))
print('Subscribers:', st.get('subscriberCount'))
print('Videos:', st.get('videoCount'))
print('Views:', st.get('viewCount'))
"
```

Expected output (numbers will change over time):

```
Channel: Balaji Chippada
Handle: @balajichippada
Subscribers: 18400
Videos: 95
Views: 319212
```

### Verify auth status only

In a new Cursor chat (after MCP restart), ask:

> Use the YouTube MCP tool `youtube_auth_status` and show me the result.

---

## 13. What you can ask Cursor to do

Once MCP is connected, example prompts:

### Analytics

```
Pull my YouTube channel analytics for the last 30 days.
Compare CTR and watch time against the targets in youtube/video-metadata-tracker.md.
Tell me which videos need title/thumbnail fixes per skill 06.
```

### Comment mining (Saturday live prep)

```
List comments from my last 7 days of uploads.
Cluster them by topic for Sunday live prep (skill 08).
Draft replies in Balaji voice (skill 01) — do NOT post without my approval.
```

### Playlists

```
Create a playlist "Phase 1 — Python Foundations" and add my Phase 1 videos in order.
Use youtube/CONTENT_CALENDAR.md as the source of truth.
```

### Title / description updates

```
For video [URL or ID], update the title to the final title from skill 06 brief.
Show me the diff before applying.
```

### Safe workflow for writes

Always use: **draft → you review → apply one action at a time**. Never auto-post bulk identical comment replies.

---

## 14. YouTube policy reminders (do not skip)

| Rule | Why |
|------|-----|
| **Title must match video content** | Misleading metadata = policy strike ([Spam policy](https://support.google.com/youtube/answer/2801973)) |
| **No auto-posting comments without review** | [YouTube API Developer Policies](https://developers.google.com/youtube/terms/developer-policies) require explicit consent per automated action |
| **No identical spam replies** | Comment spam policy |
| **You are responsible for all posted content** | Including AI-generated replies |
| **Use channel owner account** | Managers often cannot access Analytics API |

Your existing skills already align with policy:

- `youtube/skills/06-thumbnail-title-system/` — "Never clickbait"
- `youtube/skills/08-live-doubt-session/` — comment mining, human-led live answers

---

## 15. Troubleshooting

### `Error 403: access_denied` — app not verified

**Cause:** Your email is not a test user, or you signed in with a different Google account.

**Fix:**

1. Google Auth Platform → **Audience** → **Test users**
2. Add your exact email
3. Retry auth in an incognito window with that email only

---

### `client_secret.json not found`

**Cause:** JSON not at the path in `~/.cursor/mcp.json`.

**Fix:**

```bash
ls -la ~/.youtube-mcp/client_secret.json
```

Re-copy from Downloads if missing.

---

### Client ID only — no JSON downloaded

**Cause:** The client ID string (`809094573307-....apps.googleusercontent.com`) is not enough.

**Fix:** Credentials page → click your Desktop OAuth client → **Download JSON**.

---

### `redirect_uri_mismatch`

**Cause:** OAuth client created as **Web application** instead of **Desktop app**.

**Fix:** Create a new OAuth client ID with type **Desktop app**.

---

### Analytics empty or permission errors

**Cause:** Signed in with a **channel manager** account, not the owner.

**Fix:** Re-auth with the Google account that **owns** `@balajichippada`.

---

### MCP shows red in Cursor after restart

**Most common cause:** missing `"type": "stdio"` in `~/.cursor/mcp.json`. Cursor logs show `user-youtube none → error` with no other detail.

**Fix:** use the config from [Section 9](#9-configure-cursor-mcp-user-level) with `"type": "stdio"` and the `run-mcp.sh` launcher.

**Other fixes:**

1. Quit and restart Cursor (Cmd+Q) — not just Reload Window
2. Verify launcher works in terminal:
   ```bash
   printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}\n' | ~/.youtube-mcp/run-mcp.sh | head -1
   ```
   Expected: JSON with `"serverInfo":{"name":"YouTube MCP Server"`
3. Verify OAuth token still valid:
   ```bash
   ~/.youtube-mcp/venv/bin/python ~/.youtube-mcp/authenticate.py
   ```
4. Check `~/.cursor/mcp.json` is valid JSON (no trailing commas)
5. In Cursor: **Settings → MCP → youtube-studio** — click refresh/restart server

---

### `externally-managed-environment` on pip install

**Cause:** Homebrew Python blocks global pip installs.

**Fix:** Use the venv approach in [Section 8](#8-install-youtube-studio-mcp-locally).

---

### Quota exceeded (10,000 units/day)

| Operation | Cost |
|-----------|------|
| Most reads | 1 unit |
| Search | 100 units |
| Writes (update title, comment) | 50 units |
| Video upload | 1,600 units |

**Fix:** Wait until quota resets (midnight Pacific Time). Use `youtube_auth_status` to check usage.

---

### Token expired

The MCP auto-refreshes using `token.json`. If refresh fails:

```bash
rm ~/.youtube-mcp/token.json
~/.youtube-mcp/venv/bin/python ~/.youtube-mcp/authenticate.py
```

---

## 16. Security & file locations

### Files on disk

| File | Purpose | In git? |
|------|---------|---------|
| `~/.youtube-mcp/client_secret.json` | OAuth app credentials | **Never** |
| `~/.youtube-mcp/token.json` | Your access/refresh tokens | **Never** |
| `~/.youtube-mcp/venv/` | Python packages | No |
| `~/.youtube-mcp/authenticate.py` | One-time login helper | No |
| `~/.cursor/mcp.json` | Cursor MCP config | No |

### Repo `.gitignore` entries (already added)

```
client_secret*.json
token.json
```

### Rules

- Do **not** commit OAuth JSON or tokens to GitHub
- Do **not** paste `client_secret` or token contents in chat
- Delete any `client_secret_*.json` copies from project folders after copying to `~/.youtube-mcp/`

---

## 17. Re-auth, update, or uninstall

### Re-authenticate

```bash
rm ~/.youtube-mcp/token.json
~/.youtube-mcp/venv/bin/python ~/.youtube-mcp/authenticate.py
```

### Update youtube-studio-mcp

```bash
~/.youtube-mcp/venv/bin/pip install --upgrade youtube-studio-mcp
```

### Uninstall

```bash
rm -rf ~/.youtube-mcp
```

Remove the `"youtube"` block from `~/.cursor/mcp.json`, then restart Cursor.

---

## Quick reference — copy-paste command block

Full setup from scratch (after Google Cloud JSON is downloaded to `~/Downloads/`):

```bash
# Directories + install
mkdir -p ~/.youtube-mcp
python3 -m venv ~/.youtube-mcp/venv
~/.youtube-mcp/venv/bin/pip install --upgrade pip
~/.youtube-mcp/venv/bin/pip install youtube-studio-mcp

# Copy OAuth JSON (adjust source path if needed)
cp ~/Downloads/client_secret_*.json ~/.youtube-mcp/client_secret.json

# Login (browser opens)
~/.youtube-mcp/venv/bin/python ~/.youtube-mcp/authenticate.py

# Verify channel
~/.youtube-mcp/venv/bin/python -c "
from youtube_mcp.auth import YouTubeAuth
from pathlib import Path
auth = YouTubeAuth(config_dir=Path.home()/'.youtube-mcp')
yt = auth.build_youtube_service()
ch = yt.channels().list(part='snippet,statistics', mine=True).execute()['items'][0]
print(ch['snippet']['title'], ch['snippet'].get('customUrl'))
"
```

Then edit `~/.cursor/mcp.json` ([Section 9](#9-configure-cursor-mcp-user-level)) and restart Cursor.

---

## Related repo files

| File | Role |
|------|------|
| `youtube/CONTENT_CALENDAR.md` | Video schedule & phase mapping |
| `youtube/video-metadata-tracker.md` | Performance log & targets |
| `youtube/skills/06-thumbnail-title-system/` | Title + thumbnail rules |
| `youtube/skills/08-live-doubt-session/` | Comment mining for Sunday live |
| `youtube/skills/10-description-generator/` | Upload package generator |

---

*Setup documented after live install for @balajichippada / Roadmap 2026 channel.*
