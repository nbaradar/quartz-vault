---
title: MacOS Local LLMs
tags:
  - local_llm
  - ai/ml
  - guide
draft:
created: 2025-06-17

modified: 2025-07-14

published: 2025-06-17

---
# Quickstart
>![note]- Specs
>16GB Ram
>M3 Processor

installed ollama through brew. To run the ollama service:
`brew services start ollama`

The first model you ran: https://huggingface.co/meta-llama/Llama-2-7b
`ollama run llama2`
Even more specifically: https://ollama.com/library/llama2:latest

More info about your specific model:
```txt
>>> /show info
  Model
    architecture        llama    
    parameters          6.7B     
    context length      4096     
    embedding length    4096     
    quantization        Q4_0     

  Capabilities
    completion    

  Parameters
    stop    "[INST]"      
    stop    "[/INST]"     
    stop    "<<SYS>>"     
    stop    "<</SYS>>"    

  License
    LLAMA 2 COMMUNITY LICENSE AGREEMENT            
    Llama 2 Version Release Date: July 18, 2023
```

# What is Llama.cpp?
This is a C++ implementation of the LLaMA model inference engine that runs **ENTIRELY ON CPU** with optional GPU acceleration (like Metal on macOS)
**This is the GO-TO tool for running models on a laptop.** 
	Wiki Link: https://en.wikipedia.org/wiki/Llama.cpp
	GitHub Link: https://github.com/ggml-org/llama.cpp
	Random Blog Guide: https://blog.steelph0enix.dev/posts/llama-cpp-guide/

```bash
# Clone it
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# Build it with Metal (Apple GPU acceleration)
make LLAMA_METAL=1

# Download a GGUF model (e.g. LLaMA 2 7B Q4_0 from Hugging Face)
# Example: llama-2-7b.Q4_0.gguf

# Run it
./main -m ./llama-2-7b.Q4_0.gguf -p "What is the meaning of life?"
```
# MPS: Metal Performance Shaders
Apple’s framework for GPU-accelerated computations, like matrix multiplications and convolutions—basically, all the heavy lifting involved in running neural networks.
Ollama supports MPS on macOS by default if your system has a compatible GPU, which yours does (Apple M3 Silicone)

