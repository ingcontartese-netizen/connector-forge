# Host Packs

Use host packs after the adapter and branch are chosen.

Before writing host-specific files, update `host-capability-matrix.md`.

## Codex

Artifacts:

- `AGENTS.md` for repo-local instructions when useful;
- Codex MCP config block for stdio or HTTP;
- `enabled_tools`/`disabled_tools` for tool exposure control;
- smoke command and rollback notes.

Codex config must not hide unresolved auth or missing environment.

## Claude Code / Cowork

Distinguish:

- Claude Code local MCP/project setup;
- Cowork or Claude remote connector requiring a reachable remote MCP server;
- plugin bundle when skills/connectors/subagents belong together.

Use Claude-owned references or current Anthropic docs before packaging.

## ChatGPT Apps

Needs:

- public HTTPS MCP endpoint, typically `/mcp`;
- app metadata;
- tool descriptions with claim audit;
- write confirmation behavior;
- testing in Developer Mode/API Playground or equivalent.

## Antigravity / Gemini

Needs:

- host-specific MCP config;
- stdio vs remote `serverUrl`;
- headers/OAuth/Google auth model documented;
- project context file such as `GEMINI.md` when relevant.

## Rule

Host packaging is the last mile. It cannot fix an unverified surface or weak adapter.

## Deploy Hardening

For local Python MCP bridges and CLI wrappers, host packs should set:

- `PYTHONDONTWRITEBYTECODE=1` or launch with `python -B`;
- `PYTHONIOENCODING=utf-8` and `PYTHONUTF8=1` on Windows;
- a lightweight `health` or `version` tool returning `version`, `build_stamp`, `built_at`, and `mode`;
- lifecycle log path, usually `logs/mcp_bridge_lifecycle.jsonl`.

Before claiming `host_loaded`, run the host and compare the returned `build_stamp` with the expected release stamp. Before claiming `host_live_validated`, collect a live read plus lifecycle log evidence.

Before release, run the package check in `package-integrity.md`.
## OneMaster Draft Addendum

Host packs should be thin plugs over shared connector logic. Do not let Codex, Cowork, Antigravity,
or another host carry divergent domain behavior. If one host package lags a source update, declare
the lag and block carrier-parity claims until package evidence catches up.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-12, OMD-M-29,
OMD-M-30; tags BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim limit: method/spec evidence only.
