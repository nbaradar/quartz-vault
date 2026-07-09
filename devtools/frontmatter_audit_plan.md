# Frontmatter Audit Plan

## Goal

Create a reusable Python tool that audits Markdown files under `content/` and ensures each file has populated `created`, `modified`, and `published` frontmatter fields.

The script should be portable across checkouts of this vault by resolving paths relative to the repository root, not by using absolute local paths.

## Metadata Sources

The default metadata source should be Git history, because filesystem dates can be reset by iCloud sync, restore operations, or checking out the vault on another system.

With `--source git`:

- `created`: use the first Git commit where the file was added.
- `modified`: use the latest Git commit that touched the file.
- `published`: default to the same value as `created`, unless already present in frontmatter.

With `--source filesystem`:

- `created`: prefer macOS Finder `Date Added` metadata (`kMDItemDateAdded` via `mdls`), then fall back to filesystem birth time when available, then filesystem ctime.
- `modified`: use filesystem modified time.
- `published`: default to the same value as `created`, unless already present in frontmatter.

If Git has no usable date for a file, the script should fall back to filesystem metadata.

Dates should be written as `YYYY-MM-DD`.

## First Pass Behavior

For every Markdown file under `content/`:

- If a target field is missing or blank, add or populate it using metadata.
- If a target field already has a value, do not overwrite it during the first pass.
- If an existing frontmatter value differs from the metadata-derived value, record a conflict.
- Log what happened for each file.

## Conflict Resolution

After the first pass, show a numbered list of conflicts:

```text
1. content/example.md
   field: created
   frontmatter: 2025-10-01
   metadata:    2026-06-30
```

Then prompt:

```text
Enter conflict numbers to overwrite with metadata values, comma or space separated, A for all, or N to skip:
```

Accepted inputs:

- `1 3 4`
- `1,3,4`
- `1, 3, 4`
- `A`
- `a`
- `N`
- `n`

Only selected conflicts should be overwritten.

## Summary Report

At the end, print:

- Files scanned
- Files updated in the first pass
- Fields added or populated
- Conflicts found
- Conflicts resolved
- Conflicts skipped
- Errors

## Extensibility Requirements

The script should be structured so future frontmatter functionality can be added without a major refactor.

Use small rule classes or similar units for field-specific logic, so later rules can be added for:

- tags
- aliases
- note type
- status
- summaries
- source URLs
- project metadata

The script should support selecting fields from the command line, for example:

```bash
python devtools/frontmatter_audit.py --fields created modified
```

## Initial CLI

Planned commands:

```bash
python devtools/frontmatter_audit.py
python devtools/frontmatter_audit.py --dry-run
python devtools/frontmatter_audit.py --source git
python devtools/frontmatter_audit.py --source filesystem
python devtools/frontmatter_audit.py --fields created modified
python devtools/frontmatter_audit.py --content-dir content
```
