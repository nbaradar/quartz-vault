---
draft: null
tags:
- projects
- contentengine
- project
title: ContentEngine
created: 2025-06-18

modified: 2025-11-01

published: 2025-06-18

---

Can we create an AI agent that posts topical memes to twitter daily? Have it automatically generate 2-3 a day? Python, just make it a service that runs. 

What are the components?
- **X Hashtag Scraper:** Makes request for topical hashtags
- **Prompt Generator(ChatGPT Or GROK):** Tokenize hashtags and send query to generate a funny prompt using hashtags. Can also pull from a “ideabank” or “wordbank”
- **Image Generator(DALL-E Or GROK):** Take the generated prompt and create image from it
- **(OPTIONAL) Caption/Overlay Generator:** Use PIL (Python Imaging Library) to add captions/watermarks that you generate through ChatGPT or GROK
- **X Image Poster:** Post the image onto X
- **Post Scheduler:** Use ‘schedule’ library to post at specific times

[https://www.figma.com/board/5snsbPamP5JzqKpWAoLtoO/TrendingContentBot?node-id=2-851&t=jNFPfIe96jXfEzeM-0](https://www.figma.com/board/5snsbPamP5JzqKpWAoLtoO/TrendingContentBot?node-id=2-851&t=jNFPfIe96jXfEzeM-0)

[https://replit.com/@niclog2010/Trending-Content-Machine-Bot#main.ps1](https://replit.com/@niclog2010/Trending-Content-Machine-Bot#main.ps1)