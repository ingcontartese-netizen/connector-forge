#!/usr/bin/env bash
# connector-forge -> GitHub push, with full logging so Claude can verify the result.
# Credentials stay with you: when Git asks to authenticate, complete it yourself.

cd "/c/Users/conta/Documents/Per skill CLI/REAL_CASES/VALUAZIENDE_CONNECTOR_FORGE_LAB/connector-forge-pub" || { echo "ERROR: cd failed"; exit 1; }

# Mirror all output to a log file that Claude can read, while still showing it to you.
exec > >(tee "push_log.txt") 2>&1

echo "=== START $(date) ==="
echo "PWD: $(pwd)"
echo "git version: $(git --version)"

git init
git config user.name  "Giuseppe"
git config user.email "ing.contartese@gmail.com"
git add -A
git -c commit.gpgsign=false commit -m "fix: complete README (full ValuAziende row + body, MCP+CLI, credits, license)" || echo "(no new commit / already committed)"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/ingcontartese-netizen/connector-forge.git

echo "=== files staged ==="
git ls-files | wc -l

echo "=== pushing... (complete the GitHub sign-in window if it appears) ==="
git push -u origin main

echo "=== PUSH EXIT CODE: $? ==="
echo "=== END $(date) ==="
