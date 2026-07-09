---
title: LLM Memory Usage
tags:
  - reference
  - local_llm
  - ai/ml
created: 2025-07-14

modified: 2025-07-14

published: 2025-07-14

---
> How does memory usage work under the hood of an LLM? 
# Memory Usage = Model Size × Precision × Overhead
The formula:
`Total Memory (bytes) = #Params × Bytes per Param + Overhead`

So for 13 Billion Parameters at Full Precision 16...
`13,000,000,000` parameters ` x 2` bytes per parameter (FP16) = `26GB`

So that's `26GB` of RAW WEIGHT MEMORY, in practice VRAM would use slightly less (24-25gb)

Basic Cheat-sheet: `Memory ≈ (Model Size in B) × (Bytes per param)`
- **13B FP16** → `13 × 2 = ~26GB` ≈ **24GB with real-world optimizations**
- **13B Q4_K_M** → `13 × 0.5 = ~6.5GB` + overhead ≈ **8.5–9GB**

---
# Offloading to RAM
You can offload to RAM, but RAM is not used for [[Inferencing]] as much as it is for Training, so it will be very slow. 

Let's say you want t run a 35B model at FP16. This means you need 70GB VRAM
If you only have 12GB, then you need 58GB of weights in RAM. 

**In theory**, you can run **35B FP16 with offloading**, _if_:
- You're using a backend that **supports offloading** (e.g., `transformers`, `auto_gptq`, `llama.cpp`)
- You have **enough RAM** 
- You accept that it’ll be **much slower** than a model that fits in VRAM

### Performance Difference
| Metric                 | All GPU (Fits VRAM)      | Offloaded to RAM         |
| ---------------------- | ------------------------ | ------------------------ |
| Latency (1st token)    | Low (~100ms–300ms)       | High (~1–3 seconds+)     |
| Token generation speed | Fast (15–60+ tokens/sec) | Slower (1–10 tokens/sec) |
| Interactivity          | Smooth                   | Choppy, noticeable lag   |
| Usability              | Excellent                | Tolerable for testing    |
Offloading is so much slower because PCIe bandwidth (between GPU <-> RAM) is MUCH SLOWER than VRAM speed. RAM also has higher latency and lower parallelism. 

---
# Reference Tables

| Precision | Bytes per Param | 13B Model Use | 7B Model Use |
| --------- | --------------- | ------------- | ------------ |
| FP32      | 4 bytes         | ~52GB+        | ~28GB+       |
| FP16      | 2 bytes         | ~24–26GB      | ~13GB        |
| INT8      | 1 byte          | ~13GB         | ~7GB         |
| INT4 (Q4) | 0.5 byte        | ~7–8GB        | ~4GB         |
NOTE: `FP32` is mainly used for **Training**, not [[Inferencing]]. 

| Quant Level     | VRAM (13B) | VRAM (7B) | Notes                        |
| --------------- | ---------- | --------- | ---------------------------- |
| **FP16 (full)** | ~24GB      | ~13GB     | ❌ Too much for your 3080 Ti  |
| **Q8_0**        | ~16–18GB   | ~9–10GB   | ❌ 13B won’t fit              |
| **Q6_K**        | ~13–14GB   | ~7GB      | ❌ 13B right on the edge      |
| **Q5_K_M**      | ~10–11GB   | ~6GB      | ✅ Fits in 12GB (just barely) |
| **Q4_K_M**      | ~8–9GB     | ~4.5GB    | ✅ Safely fits                |
| **Q4_0**        | ~7–8GB     | ~4GB      | ✅ Easily fits                |

## GGUF Quantization Levels – Compression Reference

|Quant Level|Bits|Bytes per Param|Shrink Ratio (vs FP16)|13B Model Size|7B Model Size|Quality / Notes|
|---|---|---|---|---|---|---|
|**FP16**|16|2.0|1×|~26GB|~14GB|✅ Full precision|
|**Q8_0**|8|1.0|0.50×|~13–14GB|~7GB|✅✅✅ Near FP16, slower, rare|
|**Q6_K**|6|0.75|0.375×|~10–11GB|~6GB|✅✅✅ Great quality, more RAM needed|
|**Q5_K_M**|~5.5|~0.69*|0.35–0.40×|~9.5–10.5GB|~5.5GB|✅✅ Balanced, clean generation|
|**Q5_0**|5|0.625|0.31–0.33×|~9GB|~5GB|✅ Similar to Q5_K_M but older format|
|**Q4_K_M**|~4.5|~0.58*|~0.30–0.35×|~8.5–9GB|~4.5–5GB|✅ Best speed/quality tradeoff|
|**Q4_0**|4|0.5|0.25×|~7–8GB|~4GB|⚠️ Older, more quality loss|
|**Q3_K**|3|0.375|0.19×|~6GB|~3.5GB|⚠️ Very lossy, small systems|
|**Q2_K**|2|0.25|0.125×|~4–5GB|~2.5GB|❌ Poor quality, toy use only|
