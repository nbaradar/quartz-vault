# Agent Guide: `frontmatter_audit.py`

This file is for future coding agents maintaining `devtools/frontmatter_audit.py`. Keep it concise and update it when script behavior changes.

## Purpose

`frontmatter_audit.py` audits Markdown files in this Quartz vault and populates date frontmatter:

- `created`
- `modified`
- `published`

It is meant to help normalize PKM note metadata without blindly overwriting existing frontmatter.

## Repo Context

- Repo root is the parent of `devtools/`.
- Default content directory is `content/`, resolved relative to repo root.
- Main script: `devtools/frontmatter_audit.py`
- Plan/design notes: `devtools/frontmatter_audit_plan.md`
- This project is a Quartz site. Quartz reads date frontmatter keys such as `created`, `modified`, and `published`.

## Current Behavior

Default command:

```bash
python3 devtools/frontmatter_audit.py
```

Default metadata source is Git:

- `created`: first Git commit where the file was added.
- `modified`: latest Git commit touching the file.
- `published`: same source as `created`.

Fallback source:

```bash
python3 devtools/frontmatter_audit.py --source filesystem
```

Filesystem mode:

- `created`: macOS Finder Date Added via `mdls`, then filesystem birth time, then `ctime`.
- `modified`: filesystem modified time.
- `published`: same source as `created`.

If Git has no date for a file, the script falls back to filesystem metadata.

## Safety Contract

Do not break these guarantees:

- Missing fields may be added.
- Blank target fields may be populated.
- Existing non-blank `created`, `modified`, or `published` values must not be overwritten during the first pass.
- Existing values that differ from metadata must be reported as conflicts.
- Conflicts are only overwritten when selected by the user.
- `--dry-run` must never write files.
- `--no-prompt` must skip conflict resolution.

Conflict selection supports:

- `1 3 4`
- `1,3,4`
- `1, 3, 4`
- `A` or `a` for all conflicts
- `N` or `n` to skip

## Useful Commands

Syntax check:

```bash
python3 -m py_compile devtools/frontmatter_audit.py
```

Help output:

```bash
python3 devtools/frontmatter_audit.py --help
```

Safe full preview:

```bash
python3 devtools/frontmatter_audit.py --dry-run --no-prompt
```

Focused preview:

```bash
python3 devtools/frontmatter_audit.py --dry-run --no-prompt --content-dir content/News
```

Audit only some fields:

```bash
python3 devtools/frontmatter_audit.py --fields created modified
```

## Code Structure

Important classes/functions:

- `FileMetadataProvider`: retrieves Git or filesystem dates.
- `FieldRule`: base class for field-specific logic.
- `CreatedRule`, `ModifiedRule`, `PublishedRule`: current date field rules.
- `FrontmatterDocument`: minimal frontmatter parser/writer.
- `FrontmatterAuditor`: first pass, conflict collection, conflict resolution.
- `parse_selection`: parses conflict prompt input.
- `parse_args`: CLI flags and help text.

Preferred extension path:

1. Add a new `FieldRule` subclass.
2. Register it in `build_rules`.
3. Add the field to CLI choices if it should be selectable.
4. Update `--help`, the plan doc, and this agent guide.
5. Add a dry-run verification command to the final response.

## Editing Notes

- Prefer standard library only unless the user explicitly approves a dependency.
- Preserve existing Markdown body content exactly.
- Be careful with YAML complexity. `FrontmatterDocument` intentionally handles simple top-level `key: value` fields, not full YAML round-tripping.
- If adding richer YAML support later, prefer `ruamel.yaml` for formatting preservation, but document the new dependency.
- Do not revert user content changes in `content/`.
- Avoid hardcoded absolute paths. Resolve from `Path(__file__).resolve().parents[1]`.

## Known Limitations

- Git `created` means "first tracked in this repo," not necessarily true note creation time.
- `--follow` helps with renames but is not perfect for complex file history.
- Files not tracked by Git use filesystem fallback dates.
- The parser does not support complex nested YAML edits.

