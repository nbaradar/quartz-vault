---
title: LM Studio
tags:
  - local_llm
  - ai/ml
  - lab
draft:
created: 2025-10-27

modified: 2025-10-27
published: 2025-10-27

---
>[!info] [Documentation](https://lmstudio.ai/docs/app)
## What can I do with LM Studio?
- Download and run local LLMs like gpt-oss or Llama, Qwen
- Use a simple and flexible chat interface
- Connect [[Model Context Protocol]] servers and use them with local models
- Search & download functionality (via [[Hugging Face]] 🤗)
- Serve local models on OpenAI-like endpoints, locally and on the network
- Manage your local models, prompts, and configurations
## How can I use MCP 
https://lmstudio.ai/docs/app/mcp
To add [[Model Context Protocol]] Servers
1. Click on wrench (top right)
2. Click on "Program" tab in the right panel
3. Click the "Install" Dropdown to the right of "🔌 Integrations" 
4. Update your `mcp.json`
![[Pasted image 20251027031405.png]]

## How can I increase Context Size
You can increase [[Context Window]] size for models by going to the "Developer" view (green button on left panel), the going to the "Load" tab on the right panel
![[Pasted image 20251027121834.png]]