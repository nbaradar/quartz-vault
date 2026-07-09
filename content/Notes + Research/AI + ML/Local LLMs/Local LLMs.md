---
title: Local LLMs
tags:
  - local_llm
  - ai/ml
  - lab
draft:
created: 2025-06-17

modified: 2025-07-14

published: 2025-06-17

---
> [!info] This space will contain any learning/research notes pertaining to running LLMs locally on a machine.
> 
> Quick Start Guides:
> - [[MacOS Local LLMs]]
> - [[Windows Local LLMs]]

---
# Overview
2 different concepts for running LLMs locally:
- Running a Model ([[Inferencing]])
	- Uses a pre-trained model to generate responses
	- Fast (real-time)
	- Requires model weights + runtime
	- `EXAMPLE:` Using LLaMA-3 to chat
- Training a Model ([[Finetuning]])
	- Teaching a model new behavior using labeled data
	- Extremely resource-intensive
	- Requires massive GPU memory + long training times
	- `EXAMPLE:` Teaching LLaMa-3 to answer legal questions using transcripts

Most people just do **Inferencing**

---
## [[Runtime Tools]]
Essentially the engine that loads, serves, and runs inferencing on models. Kind of like a game engine. 

1. Loads a model (from disk, HuggingFace, etc)
2. Quantizes it or runs it in full precision (depending on tool and hardware)
3. Executes inference locally (on GPU/CPU/Both)
4. Exposes an interface to interact with the model (CLI, API, WebUI)

---
## What is [[Hugging Face]]
A platform that hosts models, datasets, and tools.
Provides:
- [[Transformer]]: Python library to load/use models.
- Dataset: Ready-to-use corpora for training or testing
- Spaces: Hosting demos using Gradio/Streamlit

You can **download models** from Hugging Face and run them locally with tools like the [[transformers library]], [[text-generation-webui]], or [[llama.cpp]].

**Datasets** are used for fine-tuning

---
## What is a [[LoRA]]
**LoRA: Low-Rank Adaptation**

Example: You can train a LoRA to make your model talk like a specific character or use a memory bank.

---
## Types of Models
- **Chat Models:** Chatbots and assistants
- **Instruction Tuned:** Follows user instructions
- **Code Models:** Code generation and Debugging
- **Embedding Models:** Vector Search, Semantic Search
- **Multimodal:** Image + Text input

---
## Running Multiple Models
You need enough RAM or VRAM. 

If you have enough, you could run an **embedding model** while also running a **chat model** in two different processes

Look into `text-generation-webui`

---
## Typical Workflow
1. Choose a model on HuggingFace
2. Download it using 
	- [[transformers library]] (Python, for full models)
	- [[llama.cpp]] or `text-generation-webui` (For quantized models like `.gguf`)
3. Launch it locally using
	- Python script with [[transformers library]] (For GPU based Models)
	- [[llama.cpp]]/llamafile (for CPU/GPU Quantized Models)
	- `text-generation-webui` (browser based UI)
4. Interact via API, terminal, or WebUI

---
## GPU vs CPU for Inference
What are the difference between cpu vs gpu for running a model [[Windows PC Specs|for your system]]?

| Factor           | CPU                              | GPU                                    |
| ---------------- | -------------------------------- | -------------------------------------- |
| Cores            | 32 Cores                         | Thousands of CUDA cores                |
| RAM              | 96GB Shared RAM                  | 12GB VRAM (FAST)                       |
| Memory Bandwidth | Slower                           | Extremely Fast (GDDR6X)                |
| Parallelism      | Moderate                         | Massive (ideal for Matrix Ops)         |
| Ideal for        | GGUF/Quantized CPU models        | Large models, full-precision inference |
| Bottlenecks      | Slower matrix math, cache/memory | VRAM limits model size                 |

In your use case, the GPU is still better. VRAM is a constraint though...

|Model Size|Format|VRAM Usage (approx.)|3080 Ti Status|
|---|---|---|---|
|Mistral 7B|GGUF Q4_0|~4.5GB|✅|
|Mistral 7B|FP16|~12–13GB|⚠️ Close! May OOM|
|LLaMA 13B|Q4_0|~8.5–9GB|✅|
|LLaMA 13B|FP16|~24GB|❌ Too big|
But if a model exceeds your GPU VRAM, `text-generation-webui` or `transformers` can **offload layers to RAM**, at the cost of speed.

---
## Full Precision VS Quantized Performance
>**Full precision** = reading the original, uncompressed encyclopedia — accurate, but huge and slow.
>**Quantized** = reading a high-quality summary — 95% of the info, in half the time.

---
# Useful Links
- [VRAM Calculator](https://apxml.com/tools/vram-calculator)
	- Use this to check if your PC can run the model you are interested in depending on parameterization and quantization
- [Uncensored General Intelligence Leaderboard](https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard)
	- Leaderboard for all publicly available uncensored models
- [llama.cpp Guide](https://blog.steelph0enix.dev/posts/llama-cpp-guide/)
	- Guide to running llama.cpp (much more powerful version of [[Ollama Notes|ollama]])
- [HuggingFace Model Catalog](https://huggingface.co/models)
- [Youtube: Running LLMs Locally](https://www.youtube.com/watch?v=XwL_cRuXM2E)
- [OpenOrca FLAN Dataset](https://www.kaggle.com/datasets/thedevastator/open-orca-augmented-flan-dataset)
- [What is GGUF/GGML](https://medium.com/@phillipgimmi/what-is-gguf-and-ggml-e364834d241c)
- [CivitAI (Uncensored)](https://civitai.com/)
	- Online platform and marketplace for generative AI content, primarily focused on AI-generated images and models
- [Local LLM Interfaces (REDDIT)](https://www.reddit.com/r/LocalLLaMA/comments/1jc3jow/openweb_ui_lm_studio_or_which_interface_is_your/)
	- KoboldCpp
	- Open WebUI
	- SillyTavern
	- LM Studio