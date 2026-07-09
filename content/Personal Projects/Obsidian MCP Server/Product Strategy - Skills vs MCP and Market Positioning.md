---
date: 2025-10-27
status: active
tags:
  - mcp
  - lab
  - ai/ml
  - projects
  - obsidian-mcp-server
  - product-strategy
  - project
title: "Product Strategy: Skills vs MCP and Market Positioning"
draft: true
created: 2025-10-27

modified: 2025-11-10
published: 2025-10-27

---

# Product Strategy: Skills vs MCP and Market Positioning

**Date:** October 27, 2025  
**Context:** Strategic discussion about Obsidian MCP Server architecture, Skills integration, and market positioning

---

## Key Insights

### 1. Skills Cannot Replace MCP Servers

**Core Distinction:**
- **MCP Servers:** Execute code, access filesystem, return dynamic data, maintain state
- **Skills:** Read-only documentation that Claude reads at runtime to improve tool usage

**Skills with executable code exist** (using `bash_tool`), but converting our tools would be strictly worse:
- ❌ Lose security sandboxing (path traversal protection)
- ❌ Lose stateful sessions (active vault tracking)
- ❌ Lose type safety (parameters become string parsing)
- ❌ Lose structured errors (get Python tracebacks instead)
- ❌ Lose UI integration (tools hidden in markdown)

**Verdict:** Keep all 22 MCP tools as-is. They're core infrastructure, not utilities.

---

## What Skills Should Provide

Skills complement MCP servers by providing **workflow patterns and best practices** without bloating the context window.

### Recommended Skill Structure

```markdown
# /mnt/skills/user/obsidian-vault/SKILL.md

## Core Workflow Patterns

### Pattern 1: Discovery Before Retrieval
✅ search_obsidian_notes → verify → retrieve
❌ retrieve directly → FileNotFoundError

### Pattern 2: Token-Efficient Content Search
✅ search_obsidian_content (snippets) → selective retrieval
❌ list_all → retrieve_all (burns tokens)

### Pattern 3: Structured Edits
✅ append_to_section_obsidian_note
❌ retrieve → modify → replace (expensive)
```

**What Skills add:**
- 📚 Multi-step workflow examples
- 📚 Token efficiency patterns
- 📚 Vault-specific conventions
- 📚 Error recovery strategies
- 🔧 Specialized utility scripts (backlink analysis, etc.)

**What Skills don't replace:**
- Core CRUD operations
- Security validation
- Session state management
- Type-safe parameters

---

## Market Positioning Strategy

### The Rebrand Question

**Decision: Keep "Obsidian MCP Server"**

**Why?**
1. **SEO & Discoverability:** "Obsidian MCP" has high search volume
2. **Marketing > Technical Accuracy:** Obsidian has 1M+ users as distribution channel
3. **Code is already universal:** Works with any markdown folder (Logseq, Foam, Dendron, plain folders)
4. **"PKM" is niche:** Most people don't know the abbreviation
5. **Positioning:** "Obsidian-compatible" rather than "Obsidian-exclusive"

**Strategy:**
- Keep the Obsidian brand for discoverability
- Clarify in README that it works with any markdown system
- Use "vault" terminology (clearer than "workspace" or "folder")
- Position as "Built for Obsidian, works universally"

---

## Competitive Analysis

### What Actually Exists

**Generic Filesystem Servers:**
- Basic CRUD (read_file, write_file, list_directory)
- ❌ No markdown awareness
- ❌ No structural operations

**Obsidian Local REST API Servers:**
- Requires Obsidian running
- ❌ No heading-based operations
- ❌ Limited functionality

**Other Markdown Servers:**
- Basic CRUD only
- ❌ No vault concept
- ❌ No multi-vault sessions
- ❌ No frontmatter tools

### Our Unique Value Proposition

**Only server with:**
1. ✅ Heading-based structural editing (semantic, not line-based)
2. ✅ Token-efficient snippet search (preview before full retrieval)
3. ✅ Multi-vault session management (stateful context)
4. ✅ Frontmatter as first-class citizen (YAML manipulation)
5. ✅ Backlink updating on move/rename
6. ✅ Works without Obsidian running
7. ✅ Security built-in (path traversal protection, vault sandboxing)

**Key Differentiator:** Markdown-native operations vs. treating .md files like .txt

---

## Token Economics

### Current Tool Definition Cost
- 22 tools × ~400 tokens/tool = ~8,800 tokens
- Loaded **once per session** and cached
- This is **negligible** compared to:
  - Conversation history: ~20K tokens
  - Single note retrieval: ~5K tokens
  - Claude's system prompt: ~50K tokens

**Conclusion:** Tool definitions aren't the bottleneck. Skills optimize supplementary documentation, not core tool defs.

### Token Efficiency by Design

**Example: Content Search**
- Full retrieval of 10 notes: **~50,000 tokens** 💸
- Snippet search with our server: **~1,500 tokens** ✅

**Pattern:**
```python
search_obsidian_content("machine learning")  # Returns snippets
# Review snippets, identify best 1-2 matches
retrieve_obsidian_note("AI/ML Notes")  # Full content only for relevant notes
```

---

## Updated README Strategy

### New Tagline
```markdown
# 🧠 Obsidian MCP Server
**Structure-aware markdown operations for Claude Desktop**

> Built for Obsidian, works with any markdown folder. The only MCP server with 
> heading-based editing, token-efficient search, and frontmatter as a first-class citizen.
```

### Key Sections to Add

#### 1. "Why This Server?"
Comparison table showing:
- Generic server: Replace entire file
- This server: `insert_after_heading` (semantic)

#### 2. "What Makes This Different"
Five unique capabilities:
1. Heading-based navigation (stable semantic anchors)
2. Token-efficient by design (snippet search)
3. Multi-vault sessions (stateful context)
4. Frontmatter as first-class (YAML manipulation)
5. Security from day one (sandboxing, validation)

#### 3. "Comparison with Other Solutions"
- vs. Obsidian Local REST API
- vs. Generic Filesystem Servers
- vs. Other Markdown Servers

#### 4. "Who Should Use This"
- ✅ Obsidian, Logseq, Foam, Dendron users
- ✅ Anyone with markdown notes
- ✅ Developers building PKM automations
- ❌ Not for: Binary files, real-time collaboration

#### 5. "Compatibility"
Examples showing vaults.yaml config for:
- Obsidian vaults
- Logseq graphs
- Foam workspaces
- Plain markdown folders

---

## Distribution Strategy

### Current Situation
- ✅ Great product built
- ✅ Genuinely unique features
- ✅ Solves real problems
- ❌ **Bottleneck: Awareness**

### Action Plan

**1. Update README** (use new positioning)

**2. Create Demo Assets**
- GIF showing heading-based insert in action
- Before/after comparison with generic server
- Token savings visualization

**3. Community Outreach**
- Obsidian Forum: "MCP Server for Structure-Aware Vault Operations"
- r/ObsidianMD: "I built an MCP server with heading-aware operations"
- Twitter/X thread: Technical breakdown with examples
- MCP Discord: Announce new server
- Anthropic's MCP servers list: Submit for inclusion

**4. GitHub Optimization**
```
Topics: obsidian, mcp, claude, markdown, pkm, knowledge-management,
        note-taking, obsidian-md, anthropic, fastmcp
```

**5. Content Strategy**
- Blog post: "Building a Markdown-Native MCP Server"
- Use cases: Daily journaling, research notes, vault reorganization
- Technical deep-dive: Why heading-based > line-based
- Respond to "automate Obsidian" posts with link

---

## Real-World Workflow Examples

### Daily Journaling
```
User: "Add today's gratitude entry"
→ append_to_section_obsidian_note(
    "Daily/2025-10-27",
    heading="Gratitude",
    content="- Morning productivity"
  )
```

### Research Note Management
```
User: "Find notes about transformer architecture"
→ search_obsidian_content("transformer")
→ Review snippets
→ retrieve_obsidian_note("AI/ML Fundamentals")  # Only relevant match
```

### Vault Reorganization
```
User: "Move 'Old Project' to Archive"
→ move_obsidian_note(
    "Projects/Old Project",
    "Archive/Old Project",
    update_links=True  # Updates backlinks automatically
  )
```

---

## Implementation Decisions

### ✅ Keep as "Obsidian MCP Server"
- Better SEO and discoverability
- Obsidian community as distribution channel
- Code already works universally
- Just clarify compatibility in docs

### ✅ All 22 Tools Stay in MCP
- They're core infrastructure, not utilities
- Security, state, type safety all depend on MCP
- Token cost is negligible (~9K, cached)
- Converting would be strictly worse

### ✅ Add Skills for Workflow Patterns
- Multi-step workflow examples
- Token efficiency best practices
- Vault-specific conventions
- Specialized utility scripts (optional)

### ✅ Focus on Distribution
- Product is great, awareness is the gap
- Multi-channel outreach (forum, Reddit, Twitter)
- Demo assets to show the magic moment
- Position uniqueness clearly

---

## Next Steps

1. **[ ] Update README** with new positioning and comparison table
2. **[ ] Create demo GIF** showing heading-based insert
3. **[ ] Write Obsidian forum post** (technical audience loves this)
4. **[ ] Post to r/ObsidianMD** with demo
5. **[ ] Create Skills file** with workflow patterns
6. **[ ] Submit to Anthropic MCP list**
7. **[ ] Twitter thread** announcing features
8. **[ ] Blog post** on development journey

---

## Updated README Draft

```markdown
# 🧠 Obsidian MCP Server

**Structure-aware markdown operations for Claude Desktop**

> Built for Obsidian, works with any markdown folder. The only MCP server with 
> heading-based editing, token-efficient search, and frontmatter as a first-class citizen.

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-latest-green.svg)](https://gofastmcp.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **📚 Technical Deep Dive:** [Read the full development journey](https://nbaradar.github.io/the-latent-space/Personal-Projects/Obsidian-MCP-Server/Obsidian-MCP-Server)

---

## Why This Server?

**Generic filesystem servers** treat markdown like text files.  
**This server** understands markdown structure.

| Operation | Generic Server | This Server |
|-----------|---------------|-------------|
| Add content | Replace entire file | `insert_after_heading` |
| Find notes | Full-text search | Snippet preview → selective retrieval |
| Update metadata | Parse YAML manually | `update_obsidian_frontmatter` |
| Rename notes | Just move file | Move + update all backlinks |

**Result:** 10× fewer tokens, semantic operations, no fragile line-number edits.

---

## What Makes This Different

### 1. 🎯 **Heading-Based Navigation** (Unique)
Traditional editors use line numbers—they break when content changes.  
This server uses **semantic anchors** (headings) that remain stable.

```markdown
## Meeting Notes
Content here

### Action Items
- Task 1
```

**With this server:**
```python
append_to_section_obsidian_note(
    title="2025-10-27",
    heading="Action Items",
    content="- New task"
)
```
**→ Adds task in the right place, no line counting**

### 2. 💰 **Token-Efficient by Design** (Unique)
Searching 10 notes with full retrieval: **~50,000 tokens** 💸  
Searching with this server: **~1,500 tokens** ✅

```python
search_obsidian_content("machine learning")
# Returns snippets with context, not full files
# Then retrieve only the 1-2 relevant notes
```

### 3. 🔄 **Multi-Vault Sessions** (Unique)
```python
set_active_vault("work")
# All subsequent operations use work vault
# No need to repeat vault parameter
```
**→ Stateful context that persists**

### 4. 📋 **Frontmatter as First-Class** (Rare)
```python
update_obsidian_frontmatter("note", {"draft": false})
# Merges into existing frontmatter
# Preserves other fields
# Validates YAML structure
```

### 5. 🔒 **Security from Day One** (Critical)
- Path traversal protection
- Vault sandboxing
- No arbitrary filesystem access
- All operations logged

---

## Comparison with Other Solutions

### vs. Obsidian Local REST API
**Their approach:** Requires Obsidian running, limited operations  
**This server:** Works offline, full structural editing

### vs. Generic Filesystem Servers
**Their approach:** Treat .md files like .txt  
**This server:** Markdown-native, structure-aware

### vs. Other Markdown Servers
**Their approach:** Basic CRUD, no vault concept  
**This server:** Multi-vault sessions, heading navigation, token efficiency

---

## 🔄 Compatibility

This server works with any markdown-based system:

### Obsidian
```yaml
vaults:
  my-vault:
    path: "/Users/you/Documents/ObsidianVault"
    description: "Primary personal vault"
```

### Logseq
```yaml
vaults:
  logseq-graph:
    path: "/Users/you/Documents/logseq"
    description: "Logseq daily notes"
    # Logseq uses journals/ and pages/ - works fine!
```

### Foam (VS Code)
```yaml
vaults:
  foam-workspace:
    path: "/Users/you/Documents/foam-workspace"
    description: "Foam workspace"
```

### Plain Markdown
```yaml
vaults:
  notes:
    path: "/Users/you/Documents/notes"
    description: "Any folder with .md files works"
```

---

## Who Should Use This

✅ **Obsidian users** who want Claude to manage their vaults  
✅ **Logseq users** who work with markdown files  
✅ **Foam/Dendron users** with VS Code workspaces  
✅ **Anyone** with a folder of markdown notes  
✅ **Developers** building PKM automations  

❌ **Not for:** Binary files, non-markdown content, real-time collaboration

---

## 🎬 Real-World Workflows

### Daily Journaling
```
User: "Add today's gratitude entry"
Claude: append_to_section_obsidian_note(
    "Daily/2025-10-27", 
    heading="Gratitude",
    content="- Grateful for productive morning"
)
```

### Research Note Management
```
User: "Find all notes mentioning 'transformer architecture'"
Claude: search_obsidian_content("transformer")
# Reviews snippets, identifies 2 relevant notes
# Retrieves only those 2, not all matches
```

### Vault Reorganization
```
User: "Move 'Old Project' to Archive folder"
Claude: move_obsidian_note(
    "Projects/Old Project",
    "Archive/Old Project",
    update_links=True  # Updates all backlinks across vault
)
```

---

## ✨ Key Features

[Keep your existing features section]

---

## 🚀 Quick Start

[Keep your existing installation section]

---

## 🛠️ Available Tools

### **Management**
| Tool | Purpose |
|------|---------|
| `list_vaults` | Discover configured vaults and current session state |
| `set_active_vault` | Switch active vault for subsequent operations |

### **Core Operations**
[Keep your existing tools table]

---

## 🏗️ Design Principles

### 1. **Token Efficiency First**
Every tool is designed to minimize context window usage:
- Snippet-based search over full-content retrieval
- Heading-based navigation over full-file reads
- Combined operations over multiple tool calls

### 2. **Markdown-Native Operations**
Traditional editors use line numbers. This breaks with note edits. **Semantic anchors** (headings) remain stable as content changes.

### 3. **Session-Aware Context**
Claude can switch between vaults mid-conversation without losing state.

*"Update my work vault... actually, check my personal vault first"* — just works.

---

## 📚 Documentation

[Keep your existing documentation links]

---

## 🤝 Contributing

This project is in active development. Contributions, issues, and feature requests are welcome!

**Particularly interested in:**
- Testing on Windows/Linux (currently Mac-focused)
- Additional vault sources (Logseq, Roam integration examples)
- Performance optimization for large vaults (10k+ notes)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Built with:
- [FastMCP](https://gofastmcp.com/) by Anthropic
- [Model Context Protocol](https://modelcontextprotocol.io/) specification
- Inspiration from the Obsidian community's API work

---

## 📬 Contact

**Nader Baradar**
- GitHub: [@nbaradar](https://github.com/nbaradar)
- Blog: [The Latent Space](https://nbaradar.github.io/the-latent-space/)

---

<p align="center">
  <i>Built because context matters, and markdown has structure.</i>
</p>
```

---

## Conclusion

**Strategic Summary:**
1. Keep "Obsidian MCP Server" name for SEO and distribution
2. All 22 tools stay in MCP (they're core infrastructure)
3. Add Skills for workflow patterns and best practices
4. Focus on distribution: product is great, awareness is the gap
5. Position as unique: no other server has heading-ops + snippets + sessions

**Unique Value:** Markdown-native operations that understand structure, not just text.

**Next Focus:** Distribution and community outreach to reach the 1M+ Obsidian users who could benefit from this.

---

*This note synthesizes a strategic planning session on October 27, 2025, covering Skills vs MCP architecture, competitive positioning, and go-to-market strategy for the Obsidian MCP Server project.*