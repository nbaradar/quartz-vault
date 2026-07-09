---
title: Ollama Notes
tags:
  - local_llm
  - ollama
  - ai/ml
  - reference
draft:
created: 2025-06-17

modified: 2025-07-14

published: 2025-06-17

---
# Commands

| Command                                     | Description                                           |
| ------------------------------------------- | ----------------------------------------------------- |
| **SECTION: MODEL MANAGEMENT**               | **======================================**            |
| `ollama list`                               | displays the models you have locally downloaded       |
| `ollama run <model>`                        | Run a model (`llama2:latest`, `deepseek-r1:14b`, etc) |
| `ollama pull <model>`                       | Download a model from Ollama's registry               |
| `ollama show <model>`                       | Show details of a model                               |
| `ollama rm <model>`                         | Remove a model from your system                       |
| **SECTION: MODEL CREATION/CUSTOMIZATION**   | **======================================**            |
| `ollama create <model-name> -f <Modelfile>` | Create a new model using a custom `Modelfile`         |
| `ollama run <model> --system <prompt>`      | Run a model with a system prompt override             |
| `ollama run <model> --template <template>`  | Run a model with a custom prompt template             |
# llama.cpp
This is a C++ implementation of the LLaMA model inference engine that runs **ENTIRELY ON CPU** with optional GPU acceleration (like Metal on macOS)
This is the GO-TO tool for running models on a laptop. More info can be found [[MacOS Local LLMs#What is Llama.cpp?|here]]



# Misc
## What is GGUF?
https://www.reddit.com/r/LocalLLaMA/comments/1ayd4xr/for_those_who_dont_know_what_different_model/
A type of model format. There's GGML, GGUF, previously GPTQ. And there are others as well. 