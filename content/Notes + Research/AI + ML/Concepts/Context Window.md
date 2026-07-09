---
title: Context Window
tags:
  - concept
  - ai/ml
draft:
created: 2025-10-27

modified: 2025-10-27
published: 2025-10-27

---
>[!note] [Coursera: What is a Context Window](https://www.coursera.org/articles/context-window)

The Context Window (or Context Length) refers to the amount of text, in tokens, that a [[Large Language Model]] can consider or "remember" at any one time. 

An LLM’s context window can be thought of as the equivalent of its working memory. It determines how long of a conversation it can carry out without forgetting details from earlier in the exchange. It also determines the maximum size of documents or code samples that it can process at once.

---
Pros/Cons of increasing context window size

| Pros                                     | Cons                                      |
| ---------------------------------------- | ----------------------------------------- |
| Longer, more coherent conversations      | Increased Costs                           |
| Fewer Hallucinations                     | More opportunities to confuse the AI      |
| Ability to analyze large amounts of data | Doesn't automatically mean better outputx |

![[Pasted image 20251027124850.png]]