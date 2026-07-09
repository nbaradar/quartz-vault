---
title: Windsurf
tags:
  - lab
  - ai/ml
  - windsurf
draft:
created: 2025-08-15

modified: 2025-08-29
published: 2025-08-15

---
>[!info]- Relevant Links 
> [Website](https://windsurf.com/)
> [Dev Docs](https://docs.windsurf.com/windsurf/getting-started)
> [July 2025: Windsurf Acquires Cognition](https://windsurf.com/blog/windsurfs-next-chapter)

Windsurf is an entire IDE solution that can use many different LLM models to accomplish different software development tasks. Windsurf includes the [Editor](https://windsurf.com/editor) itself and [plugins](https://windsurf.com/plugins) for other IDEs if you would rather not use their Editor. 

The editor is designed to be self-contained, and is based on VSCode. Because of this, you can use VSX registered extensions. [Here's a curated community list](https://docs.windsurf.com/windsurf/recommended-plugins) of the most used extensions so you can replicate a familiar dev experience. 

---
## Core Features
### [Tab](https://docs.windsurf.com/tab/overview)
A powerful next-intent prediction experience routed to a single keystroke.
### [Cascade](https://docs.windsurf.com/windsurf/cascade/cascade)
This is Windsurfs AI-agentic coder. It's features include 
- [Web Search](https://docs.windsurf.com/windsurf/cascade/web-search): Search the web for live and updated info to be referenced in Cascade suggestions
- [Memories/Rules](https://docs.windsurf.com/windsurf/cascade/memories): Help customize and standardize codebase behaviors
- [MCP](https://docs.windsurf.com/windsurf/cascade/mcp): Model Context Protocol compatible
- [Terminal](https://docs.windsurf.com/windsurf/terminal): An upgraded CLI experience (Like GeminiCLI or ClaudeCLI)
- [Planning Mode](https://docs.windsurf.com/plugins/cascade/planning-mode#planning-mode): Improves performance for longer tasks

---
## Test Project with Windsurf
I'm going to create a quick [[Wikipedia Graph View POC]] application using Windsurf to test it out. 