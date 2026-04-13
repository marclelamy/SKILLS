#!/usr/bin/env bash
# One-liner wrapper; edit scripts/upstream-sources.json to add sources.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$ROOT/scripts/sync_upstream_skills.py" "$@"
