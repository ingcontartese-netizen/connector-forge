#!/usr/bin/env bash
# connector-forge OneMaster V1 -> GitHub push helper.
# Credentials stay with the operator. This script never stores tokens/passwords.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

exec > >(tee "push_log.txt") 2>&1

echo "=== START $(date) ==="
echo "PWD: $(pwd)"
echo "git version: $(git --version)"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: this folder is not a Git working tree."
  exit 1
fi

remote_url="$(git remote get-url origin 2>/dev/null || true)"
if [ "$remote_url" != "https://github.com/ingcontartese-netizen/connector-forge.git" ]; then
  echo "ERROR: unexpected origin remote: ${remote_url:-<none>}"
  exit 1
fi

legacy_name="mcp-"connector-"builder"
if grep -R -n --exclude-dir=.git "$legacy_name" . >/tmp/connector_forge_residue.txt; then
  echo "ERROR: retired external MCP specialist skill-name residue found:"
  cat /tmp/connector_forge_residue.txt
  exit 1
fi

ref_count="$(find references -maxdepth 1 -type f -name '*.md' | wc -l | tr -d ' ')"
if [ "$ref_count" != "78" ]; then
  echo "ERROR: expected 78 integrated references, found $ref_count"
  exit 1
fi

for required in \
  references/mcp-procedure-track.md \
  references/mcp-artifact-matrix.md \
  references/mcp-inspector-lab.md \
  references/mcp-remote-first-baseline.md \
  references/carrier-parity-matrix.md \
  references/mcp-2026-07-28-watchlist.md \
  references/mcp-field-lessons.md; do
  if [ ! -f "$required" ]; then
    echo "ERROR: missing required MCP core file: $required"
    exit 1
  fi
done

if [ -f LICENSE.PLACEHOLDER.md ]; then
  echo "ERROR: LICENSE.PLACEHOLDER.md must not be published."
  exit 1
fi

echo "=== status before commit ==="
git status --short

git add -A
git -c commit.gpgsign=false commit -m "OneMaster V1: internalize MCP in connector-forge" || echo "(no new commit / already committed)"

echo "=== latest commit ==="
git --no-pager log -1 --oneline

echo "=== pushing... complete GitHub sign-in if prompted ==="
git push origin main

echo "=== END $(date) ==="
