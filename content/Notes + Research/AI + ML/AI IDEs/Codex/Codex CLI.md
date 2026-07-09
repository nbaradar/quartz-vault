---
title: Codex CLI
tags:
  - openai
  - lab
  - ai/ml
  - chatgpt
draft:
created: 2025-06-30

modified: 2026-02-23

published: 2025-06-30

---
>[!info]- Relevant Links 
>- [Announcement Blog](https://openai.com/index/introducing-codex/)
>- [GitHub Repo](https://github.com/openai/codex)

An agentic CLI provided by [[OpenAI]]. They have an [open source GitHub repo](https://github.com/openai/codex). **Zero setup** - bring your OpenAI API key and it just works!

Providers you can use:
- openai (default)
- openrouter
- azure
- gemini
- ollama
- mistral
- deepseek
- xai
- groq
- arceeai
- any other provider that is compatible with the OpenAI API

---
# [[Codex CLI Install|Installation]]
### Upgrade Codex
You can upgrade Codex with your preferred package manager:
#### Upgrade with npm
```
npm install -g @openai/codex@latest
```
#### Upgrade with Homebrew
```
brew upgrade codex
```
# [[Codex CLI Commands|Commands]]

---
# Configuration
>[!info] [CLI Config Documentation](https://github.com/openai/codex?tab=readme-ov-file#configuration-guide)

---
# Additional Tips and Tricks
>[!error]- Why does `o3` or `o4-mini` not work for me?
>It's possible that your [API account needs to be verified](https://help.openai.com/en/articles/10910291-api-organization-verification) in order to start streaming responses and seeing chain of thought summaries from the API. If you're still running into issues, please let us know!

>[!info]- Which models are supported?
>Any model available with [Responses API](https://platform.openai.com/docs/api-reference/responses). The default is `o4-mini`, but pass `--model gpt-4.1` or set `model: gpt-4.1` in your config file to override.
## [Memory & Project Docs](https://github.com/openai/codex?tab=readme-ov-file#memory--project-docs)
You can give Codex extra instructions and guidance using `AGENTS.md` files. Codex looks for `AGENTS.md` files in the following places, and merges them top-down:

1. `~/.codex/AGENTS.md` - personal global guidance
2. `AGENTS.md` at repo root - shared project notes
3. `AGENTS.md` in the current working directory - sub-folder/feature specifics

Disable loading of these files with `--no-project-doc` or the environment variable `CODEX_DISABLE_PROJECT_DOC=1`.
## Tracing / verbose logging
Setting the environment variable `DEBUG=true` prints full API request and response details:
```shell
DEBUG=true codex
```

---
# Use Cases
Below are a few bite-size examples you can copy-paste. Replace the text in quotes with your own task. See the [prompting guide](https://github.com/openai/codex/blob/main/codex-cli/examples/prompting_guide.md) for more tips and usage patterns.

| ✨   | What you type                                                                   | What happens                                                               |
| --- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 1   | `codex "Refactor the Dashboard component to React Hooks"`                       | Codex rewrites the class component, runs `npm test`, and shows the diff.   |
| 2   | `codex "Generate SQL migrations for adding a users table"`                      | Infers your ORM, creates migration files, and runs them in a sandboxed DB. |
| 3   | `codex "Write unit tests for utils/date.ts"`                                    | Generates tests, executes them, and iterates until they pass.              |
| 4   | `codex "Bulk-rename *.jpeg -> *.jpg with git mv"`                               | Safely renames files and updates imports/usages.                           |
| 5   | `codex "Explain what this regex does: ^(?=.*[A-Z]).{8,}$"`                      | Outputs a step-by-step human explanation.                                  |
| 6   | `codex "Carefully review this repo, and propose 3 high impact well-scoped PRs"` | Suggests impactful PRs in the current codebase.                            |
| 7   | `codex "Look for vulnerabilities and create a security review report"`          | Finds and explains security bugs.                                          |

