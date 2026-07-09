---
title: Claude Code
tags:
  - lab
  - claude
  - anthropic
  - ai/ml
draft:
created: 2025-06-29

modified: 2026-06-14

published: 2025-06-29

---
>[!important]- **You** must **have a** **pro account**
>[Pricing](https://www.anthropic.com/pricing) 
>- `$17/month` if billed annually
>- `$20/month` if billed monthly.
>
>Also comes with more usage and more models. 

>[!info]- Addtional Resources
>- https://www.reddit.com/r/ClaudeAI/comments/1ljv2kz/tips_for_developing_large_projects_with_claude/
>- https://www.reddit.com/r/ClaudeAI/comments/1lquetd/the_claude_code_divide_those_who_know_vs_those/
>- https://github.com/hesreallyhim/awesome-claude-code
>- https://github.com/wong2/awesome-mcp-servers
>- https://github.com/punkpeye/awesome-mcp-servers
>- [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
>- [Code execution with MCP: Building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp)

An agentic IDE/CLI provided by [[Anthropic]].

It seems like the most important thing when it comes to "vibe-coding" is setting up your context and tooling correctly. 
So your `CLAUDE.md` file, slash commands, and the newly added "hooks" feature.

As of updating this on June 19, 2025 Claude Code is still considered the best code assist tool when it comes to the quality of it's output. 

NOTE: 
- **Pro ($20/month)**: Average users can send approximately 45 messages with Claude every 5 hours, OR send approximately 10-40 prompts with Claude Code every 5 hours.
	- **Model access**: Pro plan subscribers can access Sonnet 4, but won’t be able to use Opus 4 with Claude Code.

- **Max 5x Pro ($100/month)**: Average users can send approximately 225 messages with Claude every 5 hours, OR send approximately 50-200 prompts with Claude Code every 5 hours.
- **Max 20x Pro ($200/month)**: Average users can send approximately 900 messages with Claude every 5 hours, OR send approximately 200-800 prompts with Claude Code every 5 hours.
	- **Model access**: Max plan subscribers can use Sonnet or Opus 4 on Claude Code (switch between them using the `/model` command).

---
# [[Claude Code Install|Installation]]

# Configuration
>[!info] [CLI Config Documentation](https://docs.anthropic.com/en/docs/claude-code/settings)

You can change a variety of offered settings by running the /config command when using the interactive REPL (Read-Evaluate-Print Loop)

|Command|What it does|Example|
|---|---|---|
|`claude`|Start interactive mode|`claude`|
|`claude "task"`|Run a one-time task|`claude "fix the build error"`|
|`claude -p "query"`|Run one-off query, then exit|`claude -p "explain this function"`|
|`claude -c`|Continue most recent conversation|`claude -c`|
|`claude -r`|Resume a previous conversation|`claude -r`|
|`claude commit`|Create a Git commit|`claude commit`|
|`/clear`|Clear conversation history|`> /clear`|
|`/help`|Show available commands|`> /help`|
|`exit` or Ctrl+C|Exit Claude Code|`> exit`|

---
# ClaudeCode on the Web
> [!info] References
> [Official Documentation](https://code.claude.com/docs/en/claude-code-on-the-web)
> [Announcement](https://www.claude.com/blog/claude-code-on-the-web#:~:text=Claude%20Code%20on%20the%20web%20lets%20you%20kick%20off%20coding,and%20Claude%20handles%20the%20implementation.)

ClaudeCode on the Web allows you to delegate coding tasks from your browser or mobile Claude app instead of having to use the CLI.

**IMPORTANT:** For this tool to work, you must first install the [Claude Github Tool](https://github.com/apps/claude)

> [!note]- [ClaudeCode on the Web | Free Credits](https://support.claude.com/en/articles/12690958-claude-code-promotion)  (Nov 4 - Nov 18, 2025)
> 1. Navigate to [claude.ai/code](https://claude.ai/code) to access Claude Code on the web.
>2. Your promotional credits will be automatically applied when you use Claude Code.
>3. Track your remaining promotional credit balance in the credit tracker panel on the Claude Code web interface.
>4. Continue using Claude Code as you normally would—the promotional credits will be used before your regular usage limits.

---
# Additional Tips/Tricks

### Auto-Dream Mode
https://www.reddit.com/r/ClaudeCode/comments/1rzt8fv/what_is_this_autodream_feature/
> Based on context around this feature flag in the binary, it seems to perform periodic background memory consolidation. When enabled, it occasionally spawns a background Claude agent instance that does a "reflective pass" over your memory files, synthesizing what you've learned across recent sessions into consolidated, organized memories.
>
> Per the binary, here is the actual prompt the background Claude instance receives: "You are performing a dream — a reflective pass over your memory files. Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly. Update [MEMORY.md](http://memory.md/) so it stays under [line limit] lines. It's an index, not a dump — link to memory files with one-line descriptions. Never write memory content directly into it. Return a brief summary of what you consolidated, updated, or pruned. If nothing changed (memories are already tight), say so."
### Tracking Usage
If you want to track your remaining usage credit, there are a couple open source tools that help you do so through JSONL files 
Look at [CCUsage](https://ccusage.com/) 

And if you want to know [how it's working in the background](https://deepwiki.com/ryoppippi/ccusage/5.2-data-loading-system): Basically, ClaudeCode generates JSONL files (JSONL is JSON where each new line is a valid JSON object) that track usage data. CCUsage has a Data Processing Pipeline that looks for these files and any modifications to them and tracks them in real time. You can also learn more about how [ClaudeCode implemented OpenTelemetry for Monitoring here](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage).
### Let Claude Explore First
Before making changes, let Claude understand your code:
```txt
> analyze the database schema
```

```txt
> build a dashboard showing products that are most frequently returned by our UK customers
```
### [Output Styles](https://docs.anthropic.com/en/docs/claude-code/output-styles)
>[!info] [For more detail on how to create your own Output styles](https://docs.anthropic.com/en/docs/claude-code/output-styles#create-a-custom-output-style)

There are two additional built-in output styles focused on teaching you the codebase and how Claude operates:
- **Explanatory**: Provides educational “Insights” in between helping you complete software engineering tasks. 
- **Learning**: Collaborative, learn-by-doing mode where Claude will ask you to contribute small, strategic pieces of code yourself. Claude Code will add `TODO(human)` markers in your code for you to implement.

To change output style, Run `/output-style` to access the menu or run `/output-style [style]` to specify
### [Claude Code Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)
User-defined shell commands that execute at various points in Claude Code’s lifecycle. Hooks provide deterministic control over Claude Code’s behavior, ensuring certain actions always happen rather than relying on the LLM to choose to run them.
### [Terminal Configs](https://docs.anthropic.com/en/docs/claude-code/terminal-config)
For line breaks in the terminal...
1. **Quick escape**: Type `\` followed by Enter to create a newline
2. Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter.

Enable Alert sounds when tasks complete:
```sh
claude config set --global preferredNotifChannel terminal_bell
```
**For macOS users**: Don’t forget to enable notification permissions in System Settings → Notifications → [Your Terminal App].
### [Memory Management](https://docs.anthropic.com/en/docs/claude-code/memory)
Claude offers 4 memory locations in hierarchical structure, each serving a different purpose. 

| Memory Type                | Location                                                                                                                                                | Purpose                                             | Use Case Examples                                                    | Shared With                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------- |
| **Enterprise policy**      | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`  <br>Linux: `/etc/claude-code/CLAUDE.md`  <br>Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | Company coding standards, security policies, compliance requirements | All users in organization       |
| **Project memory**         | `./CLAUDE.md`                                                                                                                                           | Team-shared instructions for the project            | Project architecture, coding standards, common workflows             | Team members via source control |
| **User memory**            | `~/.claude/CLAUDE.md`                                                                                                                                   | Personal preferences for all projects               | Code styling preferences, personal tooling shortcuts                 | Just you (all projects)         |
| **Project memory (local)** | `./CLAUDE.local.md`                                                                                                                                     | Personal project-specific preferences               | _(Deprecated, see below)_ Your sandbox URLs, preferred test data     | Just you (current project)      |

All memory files are automatically loaded into Claude Code’s context when launched. 

>[!important]- REMEMBER TO USE CLAUDE.MD, IT'S BASICALLY USER MEMORY
>Bootstrap a CLAUDE.md for your codebase with the following command: `/init`
>
>Tips:
>
>- Include frequently used commands (build, test, lint) to avoid repeated searches
>- Document code style preferences and naming conventions
>- Add important architectural patterns specific to your project
>- **Use structure to organize**: Format each individual memory as a bullet point and group related memories under descriptive markdown headings.
>- CLAUDE.md memories can be used for both instructions shared with your team and for your individual preferences.

### Claude Agent Skills 
>[!info] [Announcement Blog](https://www.anthropic.com/news/skills)

>[!info] [Dev Docs](https://docs.claude.com/en/docs/claude-code/skills)


### Using Claude Code w/ [[Gemini CLI]]s Larger Context Window
Here's how you can [use Gemini CLIs HUGE ContextWindow within Claude Code](https://www.reddit.com/r/ChatGPTCoding/comments/1lm3fxq/gemini_cli_is_awesome_but_only_when_you_make/):

>I just added instructions to CLAUDE.md to have Claude use the Gemini CLI in non-interactive mode (passing the -p param with a prompt to just get a response back from the CLI) when it needs to gather information about a large part of the codebase.
>
>That way you get the best of both worlds, Claude doesn't waste context and Gemini doesn't waste your time.

>[!example]- Example CLAUDE.md
>```
>> # Using Gemini CLI for Large Codebase Analysis
> 
> When analyzing large codebases or multiple files that might exceed context limits, use the Gemini CLI with its massive
> context window. Use `gemini -p` to leverage Google Gemini's large context capacity.
> 
> ## File and Directory Inclusion Syntax
> 
> Use the `@` syntax to include files and directories in your Gemini prompts. The paths should be relative to WHERE you run the
>  gemini command:
> 
> ### Examples:
> 
> **Single file analysis:**
> 
> gemini -p "@src/main.py Explain this file's purpose and structure"
> 
> Multiple files:
> gemini -p "@package.json @src/index.js Analyze the dependencies used in the code"
> 
> Entire directory:
> gemini -p "@src/ Summarize the architecture of this codebase"
> 
> Multiple directories:
> gemini -p "@src/ @tests/ Analyze test coverage for the source code"
> 
> Current directory and subdirectories:
> gemini -p "@./ Give me an overview of this entire project"
> 
> # Or use --all_files flag:
> gemini --all_files -p "Analyze the project structure and dependencies"
> 
> Implementation Verification Examples
> 
> Check if a feature is implemented:
> gemini -p "@src/ @lib/ Has dark mode been implemented in this codebase? Show me the relevant files and functions"
> 
> Verify authentication implementation:
> gemini -p "@src/ @middleware/ Is JWT authentication implemented? List all auth-related endpoints and middleware"
> 
> Check for specific patterns:
> gemini -p "@src/ Are there any React hooks that handle WebSocket connections? List them with file paths"
> 
> Verify error handling:
> gemini -p "@src/ @api/ Is proper error handling implemented for all API endpoints? Show examples of try-catch blocks"
> 
> Check for rate limiting:
> gemini -p "@backend/ @middleware/ Is rate limiting implemented for the API? Show the implementation details"
> 
> Verify caching strategy:
> gemini -p "@src/ @lib/ @services/ Is Redis caching implemented? List all cache-related functions and their usage"
> 
> Check for specific security measures:
> gemini -p "@src/ @api/ Are SQL injection protections implemented? Show how user inputs are sanitized"
> 
> Verify test coverage for features:
> gemini -p "@src/payment/ @tests/ Is the payment processing module fully tested? List all test cases"
> 
> When to Use Gemini CLI
> 
> Use gemini -p when:
> - Analyzing entire codebases or large directories
> - Comparing multiple large files
> - Need to understand project-wide patterns or architecture
> - Current context window is insufficient for the task
> - Working with files totaling more than 100KB
> - Verifying if specific features, patterns, or security measures are implemented
> - Checking for the presence of certain coding patterns across the entire codebase
> 
> Important Notes
> 
> - Paths in @ syntax are relative to your current working directory when invoking gemini
> - The CLI will include file contents directly in the context
> - No need for --yolo flag for read-only analysis
> - Gemini's context window can handle entire codebases that would overflow Claude's context
> - When checking implementations, be specific about what you're looking for to get accurate results
>```

---
# Use Cases
[Check this excellent documentation](https://docs.anthropic.com/en/docs/claude-code/common-workflows) for a set of common workflows and how they work in Claude Code. Anthropic writes the best dev docs by far. 


