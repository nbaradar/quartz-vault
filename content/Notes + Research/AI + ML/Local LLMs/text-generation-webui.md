---
title: text-generation-webui
tags:
  - reference
  - ai/ml
  - local_llm
created: 2025-07-14

modified: 2025-07-14

published: 2025-07-14

---
>[!important] [GitHub Repo](https://github.com/oobabooga/text-generation-webui)
# Overview
A Python based project that Loads and Runs [[Large Language Model]] locally. It also provides a full-featured web-interface to interact with models. 

It supports **GPU (CUDA), CPU, and Apple Silicon** and even has support for [[LoRA]] adapters, [[Quantization|Quantized]] models, and multi-user chat. 

While `text-generation-webui` IS a python library, it is not used like [[transformers library]]. It's a self-contained app, not something you `pip install` and call from a script.

---
# Do I Have to Use Its Web UI?
**By default, yes**, it’s built around its custom Web UI.
But:
### You _can_ use other interfaces via:
- **API Mode**: It exposes a local REST API (`http://localhost:5000/api/...`)  
    → You can use **OpenUI**, custom scripts, or any LLM frontend that supports OpenAI-style APIs.
- **OpenAI API Emulation**: Turn this on to use tools like **LM Studio**, **LangChain**, or **anything expecting OpenAI-style APIs.**
- **KoboldAI / TavernAI mode**: Supports game-based UIs or character chat frontends

⚠️ However, OpenUI may need some tweaking — `text-generation-webui` is **not built to serve models headlessly by default**, but you can disable the UI and only use the API.

---
# Architecture 

+---------------------+
|    Web UI (Flask)   |
|  - Chat window      |
|  - LoRA control     |
|  - Prompt editing   |
+----------+----------+
           |
           v
+---------------------+
|   Backend Server    |
| - Loads models      |
| - Handles inference |
| - Exposes API       |
+----------+----------+
           |
           v
+---------------------+
|   CUDA / CPU / GGUF |
+---------------------+

---
# Key Features

|Feature|Support|
|---|---|
|GGUF Models (llama.cpp)|✅|
|PyTorch (safetensors, .bin)|✅|
|LoRA adapters|✅|
|OpenAI-style API|✅|
|Streaming output|✅|
|Multi-user chat|✅|
|Prompt formatting templates|✅|
|Embeddings|✅ (basic)|
|Fine-tuning|❌ (not built-in)|