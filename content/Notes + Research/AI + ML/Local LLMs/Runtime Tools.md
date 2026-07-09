---
title: Runtime Tools
tags:
  - reference
  - local_llm
  - ai/ml
created: 2025-07-14

modified: 2025-07-14

published: 2025-07-14

---
### Common Runtime Tools in 2025

| Tool                          | Best For                                  | Runs on                     | Supports Quantized?     | Interface          | Notes                                                               |
| ----------------------------- | ----------------------------------------- | --------------------------- | ----------------------- | ------------------ | ------------------------------------------------------------------- |
| **[[Ollama Notes\|Ollama]]**  | Plug-and-play local LLMs                  | CPU/GPU (cross-platform)    | ✅ Yes (.gguf)           | CLI, REST API      | Simplest tool. Great user experience. Limited customization.        |
| **[[llama.cpp]]**             | Fast, portable inference                  | CPU/GPU (CUDA, Metal, ROCm) | ✅ Yes (.gguf)           | CLI, API           | Super efficient, no Python needed, often used as backend.           |
| **[[text-generation-webui]]** | Maximum flexibility & features            | GPU (CUDA), CPU             | ✅ Yes (.gguf, .pth)     | Web UI, API        | Hugely popular. Supports multiple models, LoRA, streaming, plugins. |
| **vLLM**                      | High-throughput, OpenAI-style inference   | GPU                         | ❌ (full precision only) | API (OpenAI-style) | Blazing fast for multi-user apps. Not for quantized models.         |
| **TGI (Text Gen Inference)**  | Production-grade model hosting            | GPU                         | ❌ (full models only)    | API                | From Hugging Face. For scalable, fast deployment.                   |
| **LM Studio**                 | GUI-based local model runner              | GPU/CPU (Windows/macOS)     | ✅ Yes (.gguf)           | Desktop GUI        | Great for beginners. Drag-and-drop style model loading.             |
| **llamafile**                 | Self-contained binaries (model + runtime) | CPU/GPU                     | ✅ Yes (.gguf)           | CLI, API           | Like a portable .exe for models. No install needed.                 |
| **AutoGPTQ**                  | Quantized model inference (GPTQ format)   | GPU                         | ✅ GPTQ only             | Python scripts     | For developers using GPTQ quantization.                             |

---
### Comparison Summary

| Feature                  | Ollama | llama.cpp    | text-gen-webui | vLLM                 | LM Studio   |
| ------------------------ | ------ | ------------ | -------------- | -------------------- | ----------- |
| Ease of Use              | ⭐⭐⭐⭐⭐  | ⭐⭐           | ⭐⭐⭐            | ⭐⭐⭐⭐                 | ⭐⭐⭐⭐        |
| Quantization Support     | ✅      | ✅            | ✅              | ❌                    | ✅           |
| GPU Acceleration         | ✅      | ✅            | ✅              | ✅                    | ✅           |
| LoRA / Fine-tune Plugins | ❌      | ⚠️ (partial) | ✅              | ❌                    | ❌           |
| Multi-Model Switching    | ❌      | ⚠️ (manual)  | ✅              | ⚠️ (restarts needed) | ⚠️ (manual) |
| API Exposure             | ✅      | ✅            | ✅              | ✅                    | ❌           |
| Local-Only Privacy       | ✅      | ✅            | ✅              | ✅                    | ✅           |

---
### File Formats by Runtime

| Format         | Used By                      | Description                                       |
| -------------- | ---------------------------- | ------------------------------------------------- |
| `.gguf`        | llama.cpp, Ollama, LM Studio | Quantized models (efficient for CPU/GPU)          |
| `.safetensors` | Hugging Face, text-gen-webui | Full-precision PyTorch weights                    |
| `.bin`         | Legacy models                | Older format, being phased out                    |
| `.ggml`        | llama.cpp (older)            | Predecessor to `.gguf`, still seen in some models |
| `.pt/.pth`     | PyTorch                      | Full-precision, often used before quantization    |
| `.ggqt`        | AutoGPTQ                     | Specialized GPTQ quantized weights                |

---
### When to Use What
|Use Case|Recommended Tool|
|---|---|
|Just want to run a model quickly|**Ollama** or **LM Studio**|
|Want web UI + LoRA support|**text-generation-webui**|
|Maximum performance, CLI use|**llama.cpp**|
|High-performance web app backend|**vLLM**|
|Self-contained model (portable .exe)|**llamafile**|
