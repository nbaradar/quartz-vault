#!/usr/bin/env python3
"""
Audit and populate Markdown frontmatter dates for this Quartz vault.

The script resolves paths relative to the repository root, so it can be run
from another checkout without editing absolute paths.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable


TARGET_FIELDS = ("created", "modified", "published")
DATE_FORMAT = "%Y-%m-%d"
FRONTMATTER_DELIMITER = "---"


@dataclass
class Conflict:
    path: Path
    field_name: str
    frontmatter_value: str
    metadata_value: str


@dataclass
class FileChange:
    path: Path
    added_fields: list[str] = field(default_factory=list)
    populated_fields: list[str] = field(default_factory=list)
    resolved_conflicts: list[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.added_fields or self.populated_fields or self.resolved_conflicts)


@dataclass
class AuditReport:
    scanned: int = 0
    updated_first_pass: int = 0
    updated_second_pass: int = 0
    fields_added: dict[str, int] = field(default_factory=lambda: {name: 0 for name in TARGET_FIELDS})
    fields_populated: dict[str, int] = field(default_factory=lambda: {name: 0 for name in TARGET_FIELDS})
    conflicts: list[Conflict] = field(default_factory=list)
    resolved_conflicts: list[Conflict] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


class FileMetadataProvider:
    def __init__(self, repo_root: Path, source: str, verbose: bool = False) -> None:
        self.repo_root = repo_root
        self.source = source
        self.verbose = verbose

    def date_added(self, path: Path) -> datetime | None:
        if self.source == "git":
            git_date = self._git_first_added(path)
            if git_date is not None:
                return git_date
            if self.verbose:
                print(f"[warn] No Git created date found for {path}; falling back to filesystem")

        return self._filesystem_date_added(path)

    def date_modified(self, path: Path) -> datetime:
        if self.source == "git":
            git_date = self._git_latest_modified(path)
            if git_date is not None:
                return git_date
            if self.verbose:
                print(f"[warn] No Git modified date found for {path}; falling back to filesystem")

        return datetime.fromtimestamp(path.stat().st_mtime)

    def _filesystem_date_added(self, path: Path) -> datetime | None:
        mdls_date = self._macos_date_added(path)
        if mdls_date is not None:
            return mdls_date

        stat = path.stat()
        birth_time = getattr(stat, "st_birthtime", None)
        if birth_time is not None:
            return datetime.fromtimestamp(birth_time)

        return datetime.fromtimestamp(stat.st_ctime)

    def _macos_date_added(self, path: Path) -> datetime | None:
        try:
            result = subprocess.run(
                ["mdls", "-raw", "-name", "kMDItemDateAdded", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
        except FileNotFoundError:
            return None

        if result.returncode != 0:
            return None

        raw = result.stdout.strip()
        if not raw or raw == "(null)":
            return None

        for fmt in ("%Y-%m-%d %H:%M:%S %z", "%Y-%m-%d %H:%M:%S"):
            try:
                return datetime.strptime(raw, fmt)
            except ValueError:
                continue

        if self.verbose:
            print(f"[warn] Could not parse Date Added from mdls for {path}: {raw}")
        return None

    def _git_first_added(self, path: Path) -> datetime | None:
        rel = path.relative_to(self.repo_root)
        lines = self._git_log_dates(
            [
                "log",
                "--follow",
                "--diff-filter=A",
                "--format=%aI",
                "--",
                str(rel),
            ],
        )
        if not lines:
            return None

        return parse_git_date(lines[-1])

    def _git_latest_modified(self, path: Path) -> datetime | None:
        rel = path.relative_to(self.repo_root)
        lines = self._git_log_dates(
            [
                "log",
                "--follow",
                "-1",
                "--format=%aI",
                "--",
                str(rel),
            ],
        )
        if not lines:
            return None

        return parse_git_date(lines[0])

    def _git_log_dates(self, args: list[str]) -> list[str]:
        try:
            result = subprocess.run(
                ["git", *args],
                cwd=self.repo_root,
                check=False,
                capture_output=True,
                text=True,
            )
        except FileNotFoundError:
            return []

        if result.returncode != 0:
            if self.verbose:
                print(f"[warn] Git command failed: {' '.join(args)}")
            return []

        return [line.strip() for line in result.stdout.splitlines() if line.strip()]


class FieldRule:
    name: str

    def desired_value(self, path: Path, metadata: FileMetadataProvider) -> str | None:
        raise NotImplementedError


class CreatedRule(FieldRule):
    name = "created"

    def desired_value(self, path: Path, metadata: FileMetadataProvider) -> str | None:
        date_added = metadata.date_added(path)
        return format_date(date_added) if date_added else None


class ModifiedRule(FieldRule):
    name = "modified"

    def desired_value(self, path: Path, metadata: FileMetadataProvider) -> str | None:
        return format_date(metadata.date_modified(path))


class PublishedRule(FieldRule):
    name = "published"

    def desired_value(self, path: Path, metadata: FileMetadataProvider) -> str | None:
        date_added = metadata.date_added(path)
        return format_date(date_added) if date_added else None


class FrontmatterDocument:
    def __init__(self, path: Path, text: str) -> None:
        self.path = path
        self.lines = text.splitlines(keepends=True)
        self.has_trailing_newline = text.endswith("\n")
        self.has_frontmatter = False
        self.fm_start = 0
        self.fm_end = 0
        self._parse_boundaries()

    def _parse_boundaries(self) -> None:
        if not self.lines or self.lines[0].strip() != FRONTMATTER_DELIMITER:
            return

        for index in range(1, len(self.lines)):
            if self.lines[index].strip() == FRONTMATTER_DELIMITER:
                self.has_frontmatter = True
                self.fm_start = 0
                self.fm_end = index
                return

    def get(self, key: str) -> str | None:
        match = self._find_key_line(key)
        if match is None:
            return None
        _, parsed = match
        return parsed.strip().strip("'\"")

    def set(self, key: str, value: str) -> str:
        if not self.has_frontmatter:
            prefix = [
                f"{FRONTMATTER_DELIMITER}\n",
                f"{key}: {value}\n",
                f"{FRONTMATTER_DELIMITER}\n",
            ]
            if self.lines and self.lines[0].strip():
                prefix.append("\n")
            self.lines = prefix + self.lines
            self.has_frontmatter = True
            self.fm_start = 0
            self.fm_end = 2
            return "added"

        match = self._find_key_line(key)
        if match is not None:
            line_index, existing_value = match
            if existing_value.strip():
                self.lines[line_index] = re.sub(
                    rf"^(\s*{re.escape(key)}\s*:\s*).*$",
                    rf"\g<1>{value}\n",
                    self.lines[line_index],
                )
                return "overwritten"

            self.lines[line_index] = re.sub(
                rf"^(\s*{re.escape(key)}\s*:\s*).*$",
                rf"\g<1>{value}\n",
                self.lines[line_index],
            )
            return "populated"

        insert_at = self.fm_end
        self.lines.insert(insert_at, f"{key}: {value}\n")
        self.fm_end += 1
        return "added"

    def to_text(self) -> str:
        text = "".join(self.lines)
        if self.has_trailing_newline and not text.endswith("\n"):
            return text + "\n"
        return text

    def _find_key_line(self, key: str) -> tuple[int, str] | None:
        if not self.has_frontmatter:
            return None

        key_pattern = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.*?)\s*$")
        for index in range(self.fm_start + 1, self.fm_end):
            match = key_pattern.match(self.lines[index])
            if match:
                return index, match.group(1)

        return None


class FrontmatterAuditor:
    def __init__(
        self,
        repo_root: Path,
        content_dir: Path,
        rules: list[FieldRule],
        source: str,
        dry_run: bool,
        verbose: bool,
    ) -> None:
        self.repo_root = repo_root
        self.content_dir = content_dir
        self.rules = rules
        self.dry_run = dry_run
        self.verbose = verbose
        self.metadata = FileMetadataProvider(repo_root=repo_root, source=source, verbose=verbose)
        self.report = AuditReport()

    def run_first_pass(self) -> AuditReport:
        for path in self.iter_markdown_files():
            self.report.scanned += 1
            try:
                change = self.audit_file(path)
            except Exception as exc:
                rel = self.relative(path)
                message = f"{rel}: {exc}"
                self.report.errors.append(message)
                print(f"[error] {message}")
                continue

            if change.changed:
                self.report.updated_first_pass += 1

        return self.report

    def iter_markdown_files(self) -> Iterable[Path]:
        return sorted(self.content_dir.rglob("*.md"))

    def audit_file(self, path: Path) -> FileChange:
        rel = self.relative(path)
        original = path.read_text(encoding="utf-8")
        document = FrontmatterDocument(path, original)
        change = FileChange(path=path)

        if self.verbose:
            print(f"[scan] {rel}")

        for rule in self.rules:
            desired = rule.desired_value(path, self.metadata)
            if desired is None:
                self.report.errors.append(f"{rel}: no metadata value available for {rule.name}")
                print(f"[warn] {rel}: no metadata value available for {rule.name}")
                continue

            current = document.get(rule.name)
            if current is None:
                document.set(rule.name, desired)
                change.added_fields.append(rule.name)
                self.report.fields_added[rule.name] += 1
                print(f"[add] {rel}: {rule.name}: {desired}")
                continue

            if not current.strip():
                document.set(rule.name, desired)
                change.populated_fields.append(rule.name)
                self.report.fields_populated[rule.name] += 1
                print(f"[populate] {rel}: {rule.name}: {desired}")
                continue

            if normalize_date(current) != normalize_date(desired):
                self.report.conflicts.append(
                    Conflict(
                        path=path,
                        field_name=rule.name,
                        frontmatter_value=current,
                        metadata_value=desired,
                    ),
                )
                print(
                    f"[conflict] {rel}: {rule.name}: frontmatter={current} metadata={desired}",
                )
            elif self.verbose:
                print(f"[ok] {rel}: {rule.name}: {current}")

        if document.to_text() != original:
            if self.dry_run:
                print(f"[dry-run] would update {rel}")
            else:
                path.write_text(document.to_text(), encoding="utf-8")
                print(f"[write] updated {rel}")

        return change

    def resolve_conflicts(self, selected_numbers: set[int]) -> None:
        by_path: dict[Path, list[Conflict]] = {}
        for number in selected_numbers:
            conflict = self.report.conflicts[number - 1]
            by_path.setdefault(conflict.path, []).append(conflict)

        for path, conflicts in by_path.items():
            rel = self.relative(path)
            original = path.read_text(encoding="utf-8")
            document = FrontmatterDocument(path, original)
            changed_fields: list[str] = []

            for conflict in conflicts:
                document.set(conflict.field_name, conflict.metadata_value)
                changed_fields.append(conflict.field_name)
                self.report.resolved_conflicts.append(conflict)
                print(
                    f"[resolve] {rel}: {conflict.field_name}: "
                    f"{conflict.frontmatter_value} -> {conflict.metadata_value}",
                )

            if document.to_text() != original:
                self.report.updated_second_pass += 1
                if self.dry_run:
                    print(f"[dry-run] would update {rel} for conflicts: {', '.join(changed_fields)}")
                else:
                    path.write_text(document.to_text(), encoding="utf-8")
                    print(f"[write] updated {rel} for conflicts: {', '.join(changed_fields)}")

    def relative(self, path: Path) -> Path:
        return path.relative_to(self.repo_root)


def format_date(value: datetime) -> str:
    return value.strftime(DATE_FORMAT)


def parse_git_date(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def normalize_date(value: str) -> str:
    stripped = value.strip().strip("'\"")
    if len(stripped) >= 10 and re.match(r"^\d{4}-\d{2}-\d{2}", stripped):
        return stripped[:10]

    for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(stripped[: len(fmt)], fmt).strftime(DATE_FORMAT)
        except ValueError:
            continue

    return stripped


def parse_selection(raw: str, max_number: int) -> set[int]:
    value = raw.strip()
    if value.lower() == "n":
        return set()
    if value.lower() == "a":
        return set(range(1, max_number + 1))

    if not value:
        raise ValueError("empty input")

    pieces = re.split(r"[\s,]+", value)
    selected: set[int] = set()
    for piece in pieces:
        if not piece:
            continue
        if not piece.isdigit():
            raise ValueError(f"not a number: {piece}")
        number = int(piece)
        if number < 1 or number > max_number:
            raise ValueError(f"number out of range: {number}")
        selected.add(number)

    return selected


def build_rules(field_names: list[str]) -> list[FieldRule]:
    available: dict[str, FieldRule] = {
        "created": CreatedRule(),
        "modified": ModifiedRule(),
        "published": PublishedRule(),
    }
    return [available[name] for name in field_names]


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def print_conflicts(repo_root: Path, conflicts: list[Conflict]) -> None:
    if not conflicts:
        print("\nNo conflicts found.")
        return

    print("\nConflicts found:")
    for index, conflict in enumerate(conflicts, start=1):
        rel = conflict.path.relative_to(repo_root)
        print(f"{index}. {rel}")
        print(f"   field: {conflict.field_name}")
        print(f"   frontmatter: {conflict.frontmatter_value}")
        print(f"   metadata:    {conflict.metadata_value}")


def print_summary(report: AuditReport) -> None:
    skipped = len(report.conflicts) - len(report.resolved_conflicts)
    print("\nSummary")
    print(f"Files scanned: {report.scanned}")
    print(f"Files updated in first pass: {report.updated_first_pass}")
    print(f"Files updated in conflict pass: {report.updated_second_pass}")
    print("Fields added:")
    for name in TARGET_FIELDS:
        print(f"  {name}: {report.fields_added.get(name, 0)}")
    print("Blank fields populated:")
    for name in TARGET_FIELDS:
        print(f"  {name}: {report.fields_populated.get(name, 0)}")
    print(f"Conflicts found: {len(report.conflicts)}")
    print(f"Conflicts resolved: {len(report.resolved_conflicts)}")
    print(f"Conflicts skipped: {skipped}")
    print(f"Errors: {len(report.errors)}")

    if report.errors:
        print("\nErrors:")
        for error in report.errors:
            print(f"- {error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit Markdown files and populate missing frontmatter date fields "
            "from file metadata."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python devtools/frontmatter_audit.py
  python devtools/frontmatter_audit.py --dry-run
  python devtools/frontmatter_audit.py --dry-run --no-prompt
  python devtools/frontmatter_audit.py --fields created modified
  python devtools/frontmatter_audit.py --content-dir content/News
  python devtools/frontmatter_audit.py --source filesystem

Notes:
  --source git is the default because it is usually more stable for synced
  vaults than Finder Date Added or filesystem birth time.

  With --source git:
    created    Uses the first Git commit where the file was added.
    modified   Uses the latest Git commit that touched the file.
    published  Uses the same Git source as created.

  With --source filesystem:
    created    Uses macOS Finder Date Added when available, then filesystem
               birth time, then filesystem ctime as a portability fallback.
    modified   Uses filesystem modified time.
    published  Uses the same filesystem source as created.

  If Git has no date for a file, the script falls back to filesystem metadata.

  Existing non-blank values are never overwritten during the first pass. If an
  existing value differs from metadata, the script reports a conflict and can
  optionally overwrite only the conflicts you select. At the conflict prompt,
  enter A to overwrite all conflicts, N to skip, or a comma/space separated
  list of conflict numbers.
""",
    )
    parser.add_argument(
        "--content-dir",
        default="content",
        help=(
            "Directory to scan, relative to the repo root. "
            "Use this to audit a subsection like 'content/News'. Default: content"
        ),
    )
    parser.add_argument(
        "--fields",
        nargs="+",
        choices=TARGET_FIELDS,
        default=list(TARGET_FIELDS),
        metavar="FIELD",
        help=(
            "Frontmatter fields to audit. Supported fields: created, modified, "
            "published. Default: created modified published"
        ),
    )
    parser.add_argument(
        "--source",
        choices=("git", "filesystem"),
        default="git",
        help=(
            "Metadata source for desired date values. 'git' uses commit history "
            "and falls back to filesystem metadata for untracked files. "
            "'filesystem' uses Finder/filesystem timestamps. Default: git"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the changes that would be made without writing any files.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Also log unchanged field checks, not just updates and conflicts.",
    )
    parser.add_argument(
        "--no-prompt",
        action="store_true",
        help="Skip the interactive conflict-resolution prompt after the first pass.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = repo_root_from_script()
    content_dir = (repo_root / args.content_dir).resolve()

    if not content_dir.exists():
        print(f"[error] content directory does not exist: {content_dir}", file=sys.stderr)
        return 1

    rules = build_rules(args.fields)
    mode = "dry run" if args.dry_run else "write"
    print(f"Frontmatter audit starting in {mode} mode")
    print(f"Repo root: {repo_root}")
    print(f"Content dir: {content_dir.relative_to(repo_root)}")
    print(f"Fields: {', '.join(rule.name for rule in rules)}")
    print(f"Source: {args.source}")

    auditor = FrontmatterAuditor(
        repo_root=repo_root,
        content_dir=content_dir,
        rules=rules,
        source=args.source,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )
    report = auditor.run_first_pass()

    print_conflicts(repo_root, report.conflicts)
    if report.conflicts and not args.no_prompt:
        while True:
            raw = input(
                "\nEnter conflict numbers to overwrite with metadata values, "
                "comma or space separated, A for all, or N to skip: ",
            )
            try:
                selected = parse_selection(raw, len(report.conflicts))
            except ValueError as exc:
                print(f"Invalid selection: {exc}")
                continue
            break

        if selected:
            auditor.resolve_conflicts(selected)
        else:
            print("Skipping conflict resolution.")
    elif report.conflicts and args.no_prompt:
        print("\nSkipping conflict resolution because --no-prompt was provided.")

    print_summary(report)
    return 0 if not report.errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
