#!/usr/bin/env python3
"""
Sync vendored community skills from upstream GitHub repos.

Reads scripts/upstream-sources.json. For each source, shallow-clones the repo and
compares each local skill directory (must contain SKILL.md) to the matching folder
under upstream_skills_path (empty = repo root).

Requires: git, rsync (macOS/Linux).

Usage:
  python3 scripts/sync_upstream_skills.py              # dry-run (rsync -n)
  python3 scripts/sync_upstream_skills.py --apply      # write changes
  python3 scripts/sync_upstream_skills.py --source matt-pocock
  python3 scripts/sync_upstream_skills.py --list
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "scripts" / "upstream-sources.json"


def load_config() -> dict:
    if not CONFIG_PATH.is_file():
        print(f"Missing config: {CONFIG_PATH}", file=sys.stderr)
        sys.exit(1)
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def run(cmd: list[str], *, cwd: Path | None = None) -> None:
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode != 0:
        raise SystemExit(r.returncode)


def rsync_dry_or_apply(
    src: Path, dst: Path, *, apply: bool, label: str
) -> None:
    if not src.exists():
        print(f"  [skip] upstream missing: {label}")
        return
    flags = ["rsync", "-a"]
    if not apply:
        flags.append("-n")
    flags.extend(["--delete", f"{src}/", f"{dst}/"])
    print(f"  {'APPLY' if apply else 'DRY'}: {label}")
    run(flags)


def sync_file(upstream_repo: Path, rel_from: Path, dst_file: Path, *, apply: bool) -> None:
    src = upstream_repo / rel_from
    if not src.is_file():
        print(f"  [skip] upstream file missing: {rel_from}")
        return
    print(f"  {'APPLY' if apply else 'DRY'}: file {rel_from} -> {dst_file.relative_to(REPO_ROOT)}")
    if apply:
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst_file)


def process_source(source: dict, *, apply: bool) -> None:
    sid = source["id"]
    github = source["github"]
    branch = source.get("branch", "main")
    local_rel = source["local_dir"]
    upstream_sub = (source.get("upstream_skills_path") or "").strip().strip("/")
    local_root = REPO_ROOT / local_rel

    if not local_root.is_dir():
        print(f"[{sid}] local_dir does not exist: {local_root}")
        return

    url = f"https://github.com/{github}.git"
    print(f"\n=== {sid} ({github} @ {branch}) ===")

    with tempfile.TemporaryDirectory(prefix=f"skills-upstream-{sid}-") as tmp:
        clone_dir = Path(tmp) / "repo"
        run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "-b",
                branch,
                url,
                str(clone_dir),
            ]
        )
        upstream_skills = clone_dir / upstream_sub if upstream_sub else clone_dir

        if not upstream_skills.is_dir():
            print(f"  [error] upstream path not a directory: {upstream_sub or '.'}")
            return

        for child in sorted(local_root.iterdir()):
            if not child.is_dir():
                continue
            if child.name.startswith("."):
                continue
            if not (child / "SKILL.md").is_file():
                continue
            up = upstream_skills / child.name
            rsync_dry_or_apply(up, child, apply=apply, label=child.name)

        for extra in source.get("extra_files") or []:
            rel = extra["upstream_relative"].lstrip("/")
            loc = extra["local_relative"].lstrip("/")
            sync_file(clone_dir, Path(rel), local_root / loc, apply=apply)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply updates (default is dry-run via rsync -n)",
    )
    parser.add_argument(
        "--source",
        action="append",
        dest="sources",
        metavar="ID",
        help="Limit to one or more source ids (repeatable)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Print configured sources and exit",
    )
    args = parser.parse_args()
    data = load_config()
    sources = data["sources"]

    if args.list:
        for s in sources:
            print(f"{s['id']}\t{s['github']}\t{s.get('local_dir', '')}")
        return

    if args.sources:
        wanted = set(args.sources)
        sources = [s for s in sources if s["id"] in wanted]
        missing = wanted - {s["id"] for s in sources}
        if missing:
            print(f"Unknown source id(s): {sorted(missing)}", file=sys.stderr)
            sys.exit(1)

    if not args.apply:
        print("Dry-run only (no writes). Use --apply to sync from upstream.\n")

    for s in sources:
        process_source(s, apply=args.apply)


if __name__ == "__main__":
    main()
