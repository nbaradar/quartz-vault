---
title: GGUF
tags:
  - local_llm
  - reference
  - ai/ml
created: 2025-07-14

modified: 2025-07-14

published: 2025-07-14

---
**GGUF (GPTQ GPU Unified Format)** is the evolved file format used in llama.cpp.

It is a binary file format optimized for efficiently loading and saving [[Large Language Model|Large Language Models]] and other machine learning models using [[Quantization]], particularly for [[Inferencing]].

It stores **compressed versions of LLMs** by reducing the precision of weights from:  
> **FP16** or **FP32** → **INT4** / **INT5** / **INT8**, etc.

---
# GGUF Quant Levels (Simplified Table)

|Quant Level|Bits|Precision Type|Size|Speed|Quality|Typical Use|
|---|---|---|---|---|---|---|
|`Q2_K`|2-bit|VERY low precision|🔻 Smallest|🚀 Fastest|❌ Poor|Experiments, small devices|
|`Q3_K`|3-bit|Low precision|🔻 Small|🚀 Fast|⚠️ Low|Small devices, toy use|
|`Q4_0`|4-bit|Basic INT4 (old)|🔻 Small|🚀 Fast|⚠️ Noticeable loss|Older models, testing|
|`Q4_K_M`|4-bit|Modern INT4 + mul mat|⚖️ Medium|⚡ Fast|✅ Good (~95%)|✅ Best Q4-level compromise|
|`Q5_0`|5-bit|Basic INT5|⚖️ Medium|⚡ Fast|✅+ Very good|Good balance for general use|
|`Q5_K_M`|5-bit|Optimized 5-bit|📈 Larger|✅ Fast|✅✅ Excellent|Near-FP16 quality|
|`Q6_K`|6-bit|Almost INT8-level|📈 Big|✅ Fast|✅✅✅ Very close to FP|Ideal if you have VRAM room|
|`Q8_0`|8-bit|Full INT8|📈📈 Large|⚠️ Slower|✅✅✅✅ Excellent|Very close to full precision|

The **community favorite** right now is:
> 🔥 `Q4_K_M` → Great speed & quality on mid-range GPUs like your **3080 Ti**.

---
GGML and GGUF refer to the same concept, with GGUF being the newer version that incorporates additional data about the model.

For more info: [What is GGUF and GGML?](https://medium.com/@phillipgimmi/what-is-gguf-and-ggml-e364834d241c)

---

![[Pasted image 20250714155249.png]]