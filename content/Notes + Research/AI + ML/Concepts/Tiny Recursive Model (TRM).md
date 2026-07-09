---
title: Tiny Recursive Model (TRM)
tags:
  - concept
  - ai/ml
draft:
created: 2025-10-22

modified: 2025-10-22
published: 2025-10-22

---
>[!note]- Resources
> https://arxiv.org/abs/2510.04871
> https://github.com/SamsungSAILMontreal/TinyRecursiveModels

Developed by [[Samsung]], The model is just 7M parameters and can out perform [[Deepseek]] at certain complex tasks. 
> Tiny Recursive Model (TRM), a much simpler recursive reasoning approach that achieves significantly higher generalization than HRM, while using a single tiny network with only 2 layers. With only 7M parameters, TRM obtains 45% test-accuracy on ARC-AGI-1 and 8% on ARC-AGI-2, higher than most LLMs (e.g., Deepseek R1, o3-mini, Gemini 2.5 Pro) with less than 0.01% of the parameters.

The key to it's performance is **Recursive Hierarchical Reasoning**:
> Recursive hierarchical reasoning consists of recursing multiple times through two small networks (fL at high frequency and fH at low frequency) to predict the answer. Each network generates a different latent feature: fL outputs zH and fH outputs zL. Both features (zL,zH) are used as input to the two networks. The authors provide some biological arguments in favor of recursing at different hierarchies based on the different temporal frequencies at which the brains operate and hierarchical processing of sensory inputs.

Although we simplified and improved on deep recursion, the question of why recursion helps so much compared to using a larger and deeper network remains to be explained; we suspect it has to do with overfitting, but we have no theory to back this explanation.

![[Pasted image 20251022110039.png|400]]