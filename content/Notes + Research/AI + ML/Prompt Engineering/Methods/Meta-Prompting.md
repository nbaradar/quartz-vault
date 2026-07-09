---
title: Meta-Prompting
tags:
  - prompt-engineering
  - ai/ml
  - reference
draft:
created: 2025-06-29

modified: 2025-07-05

published: 2025-06-29

---

Meta-prompting is a technique in prompt engineering where prompts are used to generate, modify, or interpret other prompts. This approach involves creating high-level prompts that guide the AI in understanding or creating more specific prompts for various tasks.

I'm thinking this approach could be used in agentic workflows where you may have a prompt "template" that needs to be updated based on information. Or just a cool idea that requires you first generate a prompt in a workflow.

### Example of Meta-prompting
```
Meta-Prompt: "Generate a prompt that will guide an AI to analyze [specific topic]. The prompt should include instructions for:

1. Summarizing key points
2. Identifying main arguments
3. Evaluating evidence
4. Suggesting areas for further researchEnsure the generated prompt is clear, concise, and adaptable to various subjects within [specific topic]."

This meta-prompt instructs the AI to create a more specific prompt for analyzing a given topic, demonstrating how meta-prompting can be used to dynamically generate task-specific prompts.
```

### Resources
- [Meta Prompting Guide by PromptLayer](https://www.promptlayer.com/glossary/meta-prompting#:~:text=Key%20aspects%20of%20Meta%2Dprompting,based%20on%20context%20or%20feedback)
- [Reddit | Axiom prompt engineering system](https://www.reddit.com/r/PromptEngineering/comments/1hhfoxy/ive_developed_an_axiom_prompt_engineering_system/)
	- [Reddit | Axiom Github](https://github.com/codedidit/axiomprompting)
