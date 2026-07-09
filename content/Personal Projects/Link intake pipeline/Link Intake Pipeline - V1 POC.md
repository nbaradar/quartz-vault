---
date: 2026-06-14
title: Link Intake Pipeline - V1 POC
tags:
  - project
  - python
  - rookiepy
  - discord
  - reddit
enableToc: true
draft: false
created: 2026-06-14

modified: 2026-06-14
published: 2026-06-14

---
> [!success] POC complete
> [[Link Intake|Link to Intake Page]] 
# Goal
Reduce cognitive overhead from saved links by automatically collecting links from Reddit and Discord into a single markdown-based intake page for future review.

---
## Problem Statement
I've spent the last four months accumulating links that I found interesting or wanted to discuss on my blog. But I have not had the time to update my blog with these hundreds of accumulated links. I realized the accumulation itself was creating mental overhead. My first instinct was to build a sophisticated system. Instead I'm forcing myself to build the smallest possible intake pipeline. This is a proof of concept only, and in exercise in not over-engineering everything I want to build.

Currently links are saved in multiple locations:
- Reddit saved posts
- Personal Discord intake channel

These links accumulate over time and create open loops:
- "I should post that."
- "I should remember that."
- "I should add that to the blog."

---
## Scope

### Included
- Reddit API retrieval
- Discord API retrieval
- Markdown generation
- Single output file
### Explicitly Excluded
- MCP servers
- Databases
- LLM summarization
- Metadata extraction
- Embeddings
- Search
- Categorization
- Tag generation
- Automated publishing workflows
- Multi-user support
- Frontend UI

---
## Output Format

Example:
```markdown
# Intake
## 2026-06-14
### Reddit
- [Interesting Post Title](https://example.com)
- Saved: 2026-06-14

### Discord
- [Interesting Link](https://example.com)
- Posted: 2026-06-12
```

---
## Technical Design
### Reddit Source
Input:
- Authenticated Reddit account (must be logged into Reddit in Chrome)
- Saved posts via Reddit's JSON API
  
Retrieval method:
- `rookiepy` reads Reddit session cookies directly from Chrome's local cookie database
- macOS will prompt for Keychain access once (Chrome encrypts cookies with it)
- Cookies are passed to `requests` which calls `reddit.com/user/me/saved.json`
- Reddit's server sees it as a normal authenticated browser session
- No Reddit API app registration, no Playwright, no bot detection issues
- If Reddit returns 403, cookies have expired — just log into Reddit in Chrome again

Output:
- Title
- URL
- Timestamp

---
### Discord Source
Input:
- Configured Discord channel

Source info:
- Channel ID: 1063541461452337212
- Server ID: 155427339524767744
- Bot Application ID: 1515835274570104873

Credentials:
- Requires a Discord bot token (set as `DISCORD_BOT_TOKEN` in `.env`)
- Get the token from: Discord Developer Portal → your app → Bot → Token
- The bot must be added to the server with Read Messages + Read Message History permissions on the intake channel

Output:
- Message content
- URLs
- Timestamp

---
### Aggregation

Merge both sources into a common markdown structure.
Sort by date if convenient.
No additional processing required.

---
## Setup & Usage

### First-time setup
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
cp .env.example .env
# Edit .env and add your DISCORD_BOT_TOKEN
```
### Running the script
```bash
# Collect links from the last 4 months (default)
.venv/bin/python3 intake.py

# Collect links from a specific date onward
.venv/bin/python3 intake.py --since 2026-02-01
```

### First Reddit run
On the first run, a Chromium browser window will open. Log in to Reddit manually. The session is saved to `session.json` and reused on all future runs. You only need to log in again if the session expires.
### Output
Links are written to `content/intake.md`, grouped by date (newest first) and split by source.

---
## Configuration
### Environment variables (`.env`)
| Variable            | Required | Description                                                      |
| ------------------- | -------- | ---------------------------------------------------------------- |
| `DISCORD_BOT_TOKEN` | Yes      | Bot token from Discord Developer Portal → your app → Bot → Token |
### Hardcoded config (edit in source if needed)
| Value          | File                 | Description                                                |
| -------------- | -------------------- | ---------------------------------------------------------- |
| `CHANNEL_ID`   | `discord_fetcher.py` | Discord channel to read from (`1063541461452337212`)       |
| `OUTPUT_FILE`  | `intake.py`          | Output path (`content/intake.md`)                          |
| `SESSION_FILE` | `reddit_scraper.py`  | Where Playwright saves the Reddit session (`session.json`) |
### Files that must not be committed
- `.env` — contains the real bot token
- `session.json` — contains your Reddit browser session
- Both are listed in `.gitignore`

---
## Future Versions (Not V1)

### V1.1
- Incremental updates
- Deduplication
### V2
- Draft generation
- Personal notes
### V3
- LLM-assisted enrichment
- Summaries
- Metadata extraction
### V4+ ???
- Knowledge graph
- MCP integration
- Advanced workflows
  
---