#!/usr/bin/env python3
"""Create snapshots, verify conservative invariants, and roll back SKILL.md edits."""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path


BACKUP_DIRNAME = ".biosafety-safe-rewrite-backups"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter_name(text: str) -> str | None:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, flags=re.DOTALL)
    if not match:
        return None
    name = re.search(r"(?m)^name:\s*([^\r\n#]+?)\s*$", match.group(1))
    return name.group(1).strip().strip('"\'') if name else None


def headings(text: str) -> list[str]:
    return re.findall(r"(?m)^(#{1,6}\s+.+?)\s*$", text)


def manifest_path(snapshot: Path) -> Path:
    return snapshot.with_suffix(snapshot.suffix + ".json")


def load_manifest(snapshot: Path) -> dict:
    path = manifest_path(snapshot)
    if not path.is_file():
        raise ValueError(f"Missing backup manifest: {path}")
    return json.loads(read_text(path))


def create_snapshot(target: Path) -> int:
    target = target.resolve()
    if not target.is_file():
        raise ValueError(f"Target does not exist: {target}")
    original = read_text(target)
    backup_dir = target.parent / BACKUP_DIRNAME
    backup_dir.mkdir(exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    digest = sha256(target)[:12]
    snapshot = backup_dir / f"{target.stem}.{stamp}.{digest}{target.suffix}"
    shutil.copy2(target, snapshot)
    manifest = {
        "target": str(target),
        "original_sha256": sha256(target),
        "original_name": frontmatter_name(original),
        "original_headings": headings(original),
        "created_utc": stamp,
    }
    manifest_path(snapshot).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"snapshot": str(snapshot), "manifest": str(manifest_path(snapshot))}))
    return 0


def verify(target: Path, snapshot: Path, show_diff: bool) -> int:
    target = target.resolve()
    snapshot = snapshot.resolve()
    manifest = load_manifest(snapshot)
    if str(target) != manifest["target"]:
        raise ValueError("Snapshot does not belong to this target.")
    original = read_text(snapshot)
    current = read_text(target)
    errors: list[str] = []
    warnings: list[str] = []
    if frontmatter_name(current) != manifest["original_name"]:
        errors.append("Frontmatter name changed.")
    if current.count("TODO") > original.count("TODO"):
        errors.append("TODO placeholder introduced.")
    if not headings(current):
        errors.append("No Markdown headings remain.")
    missing_headings = [h for h in manifest["original_headings"] if h not in headings(current)]
    if missing_headings:
        errors.append("Existing headings were removed: " + "; ".join(missing_headings))
    diff = list(difflib.unified_diff(
        original.splitlines(), current.splitlines(),
        fromfile=str(snapshot), tofile=str(target), lineterm=""
    ))
    if not diff:
        warnings.append("No content changes detected.")
    result = {
        "status": "pass" if not errors else "fail",
        "snapshot": str(snapshot),
        "target": str(target),
        "changed_diff_lines": len(diff),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, indent=2))
    if show_diff and diff:
        print("\n".join(diff))
    return 0 if not errors else 2


def rollback(target: Path, snapshot: Path) -> int:
    target = target.resolve()
    snapshot = snapshot.resolve()
    manifest = load_manifest(snapshot)
    if str(target) != manifest["target"]:
        raise ValueError("Snapshot does not belong to this target.")
    shutil.copy2(snapshot, target)
    if sha256(target) != manifest["original_sha256"]:
        raise RuntimeError("Rollback verification failed: restored hash differs from snapshot.")
    print(json.dumps({"status": "rolled_back", "target": str(target), "snapshot": str(snapshot)}))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("snapshot", "verify", "rollback"):
        cmd = sub.add_parser(name)
        cmd.add_argument("target", type=Path)
        cmd.add_argument("snapshot", type=Path, nargs="?")
    sub.choices["verify"].add_argument("--show-diff", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "snapshot":
            return create_snapshot(args.target)
        if args.snapshot is None:
            parser.error(f"{args.command} requires a snapshot path")
        if args.command == "verify":
            return verify(args.target, args.snapshot, args.show_diff)
        return rollback(args.target, args.snapshot)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
