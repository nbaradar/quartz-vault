---
title: QKV (Query, Key, and Value)
tags:
  - concept
  - ai/ml
  - transformer
draft:
created: 2025-12-23

modified: 2025-12-23
published: 2025-12-23

---
QKV are vectors in the [[Transformer]] architecture. These are all part of the Transformers self-attention mechanism/module.

- **Query Vector:** 
	- This represents the processed information of the current word. It’s a matrix that helps in the scoring process to see how relevant other words are to the current word.
- **Key Vector:** 
	- This represents the processed information of all the words in the sentence, including the current word. It’s used to compute a score that represents the relationship between different parts of the sentence.
- **Value Vector**
	- This represents the raw information of all words in the sentence. Once the scores between different parts of the sentence are computed, they are used to weight the Value matrix, which in turn gives an aggregated representation of the words in context.

>[!info] Metaphor for Intuition
> - In a Google Search you enter a term to look for something. This term, in our attention mechanism, would be the “Query”.  
> - When you enter this term, Google presents possible options that answer your question. These would be our “Keys”.  
> - And then you pick one of Google’s suggestions and open the content. This would be the “Value”.

![[Pasted image 20251223121225.png|600]]