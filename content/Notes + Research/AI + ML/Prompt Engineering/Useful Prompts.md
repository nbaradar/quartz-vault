---
title: Useful ML Prompts
description: A collection of useful and productive prompts that are designed to improve and increase the quality and reasoning in your LLM workflow. These prompts are designed to maximize performance. Some I found online, others I created myself.
draft: false
tags:
  - prompt-engineering
  - ai/ml
  - "#reference"
date: 2025-06-12
created: 2025-06-17

modified: 2025-06-29

published: 2025-06-17

---
# Troubleshooting
```txt
I’m having a persistent problem with [x] despite having taken all the necessary countermeasures I could think of. Ask me enough questions about the problem to find a new approach. Ask me for all the context you need to work through this one question at a time, allowing me to respond.
```

PASTE THIS AT THE END OF YOUR QUESTION:
```txt
Interpret. Contrast. Justify. Then conclude.
```

---
# Coding
```txt
Reflect on 5-7 different possible sources of the problem, distill those down to 1-2 most likely sources, and then add logs to validate your assumptions before we move onto implementing the actual code fix
```

---
# System Manipulation
## Memory Management
```txt
Give me a complete inventory of my current memory. Include the following: 

- Total number of memory entries 
- A categorized breakdown (e.g. work, personal growth, relationships, health, hobbies, etc.) 
- Number of entries per category, and an informational graphic that shows the breakdown. 
- A list of the largest and smallest entries by character or word count 
- A high-level summary of what proportion of my memory is focused on each life domain 
- Any redundancies or overlaps you detect - Anything that looks outdated, vague, or could be consolidated 
- Format the output cleanly with headers and bullet points for easy reference.
```

## Prompt Engineering
```txt
Act as an expert prompt engineer. Your task is to take my simple prompt/goal and transform it into a detailed, optimized prompt that will yield a superior result.

First, analyze my request below and identify any ambiguities or missing information.

Then, construct a new, comprehensive prompt that:
1.  **Assigns a clear Role/Persona** to the AI (e.g., "Act as a senior financial analyst...").
2.  **Provides Essential Context** that the AI would need to know.
3.  **Specifies the exact Format** for the output (e.g., Markdown table, JSON, bulleted list).
4.  **Includes Concrete Examples** of the desired output style or content.
5.  **Adds Constraints** to prevent common errors or unwanted content (e.g., "Do not use jargon," "Ensure the tone is encouraging").

Here is my original request:
[Your original goal or prompt]

Now, provide only the new, optimized prompt.
```