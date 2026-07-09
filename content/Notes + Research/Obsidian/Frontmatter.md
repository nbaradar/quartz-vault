---
title: Frontmatter
tags:
  - frontmatter
  - obsidian
  - markdown
  - reference
draft:
created: 2025-10-27

modified: 2025-10-27

published: 2025-10-27

---
**Frontmatter** is **metadata** that sits at the top of a Markdown file, usually wrapped in triple dashes (`---`). It's written in YAML, and tells site generators (like Quartz) how to render or handle the page.

Sample:
```yaml
---
title: "My First Note"
tags:
  - personal
  - ideas
draft: false
date: 2025-10-26
---
```

Quartz expects frontmatter so it can:
- Display the correct **title** in the UI and metadata.
- Organize pages into **tags** and **collections**.
- Generate slugs, sidebars, and navigation.
- Determine visibility (e.g., skipping drafts).
- Control special rendering behaviors.

