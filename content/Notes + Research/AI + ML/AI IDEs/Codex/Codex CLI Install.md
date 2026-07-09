---
title: Codex CLI Install
tags:
  - guide
  - openai
  - chatgpt
  - ai/ml
draft:
created: 2025-06-30

modified: 2026-02-23

published: 2025-06-30

---
First you need to make sure you meet these requirements:

| Requirement                 | Details                                                         |
| --------------------------- | --------------------------------------------------------------- |
| Operating systems           | macOS 12+, Ubuntu 20.04+/Debian 10+, or Windows 11 **via WSL2** |
| Node.js                     | **22 or newer** (LTS recommended)                               |
| Git (optional, recommended) | 2.23+ for built-in PR helpers                                   |
| RAM                         | 4-GB minimum (8-GB recommended)                                 |
> Never run `sudo npm install -g`; fix npm permissions instead.

---
First all we do is run 
```bash
npm install -g @openai/codex
```

You can run `npm list --global` to validate that it installed correctly. You should see it listed as an installed package:
```txt
/Users/naderbaradar/.nvm/versions/node/v22.16.0/lib
├── @google/gemini-cli@0.1.7
├── @openai/codex@0.1.2505172129
├── corepack@0.32.0
└── npm@10.9.2
```

Next, you need to set your OpenAI API key as an environment variable. 
```bash
export OPENAI_API_KEY="your-api-key-here"
```

To find your API key, log into [The OpenAPI Platform](https://auth.openai.com/log-in)
![[Pasted image 20250630000516.png]]

**Do not share your API key** with others or expose it in the browser or other client-side code.

You can test to make sure your API key was set with this command:
```bash
echo $OPENAI_API_KEY
```

Then finally, simply issue this `codex` command
```bash
codex
```

And that's it! You should see the interface and can begin prompting
![[Pasted image 20250630002126.png]]

