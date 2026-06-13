# Host Capability Matrix

Use this reference before packaging a connector for a real AI host. MCP support is not uniform across hosts; verify transport, auth, tool filtering, output limits, and refresh behavior in the target host.

| Host | Local stdio | Remote HTTP `/mcp` | Auth baseline | Tool controls | Evidence required |
|---|---|---|---|---|---|
| Codex | yes, via MCP config | yes, when configured | local env/keychain for stdio; OAuth for remote where supported | `enabled_tools` / disabled tools, approvals, timeouts | config loaded, discovery visible, one read smoke |
| Claude Code | yes, project/user scope | yes; SSE only compatibility where documented | local env for stdio; OAuth for remote | scope in `.mcp.json` / settings, timeouts, permissions | `tools/list`, read smoke, restart recovery |
| Claude Cowork / remote | no direct desktop local assumption | yes, cloud reaches public/reachable connector | remote connector auth; bridge required for local desktop apps | plugin/connector permissions, sub-agent verifier | reachable server, bridge live, host smoke |
| ChatGPT Apps | no | yes, public HTTPS | app auth / OAuth as supported by Apps SDK | tool descriptors, `_meta`, write confirmation, widget state | Developer Mode/API Playground test, client UX check |
| Gemini CLI | yes | yes | env/ADC/service account/OAuth as documented | `includeTools`, `excludeTools`, `trust`, name sanitization | settings loaded, name mapping, smoke |
| Antigravity | to live-verify | `serverUrl` documented but host behavior must be verified | ADC/OAuth/custom headers where documented | permission rules such as `mcp(server/tool)` | `research/live-verify` until tested |

## Rules

- Choose one primary host in Sprint 1.
- Do not call a host pack ready because a config snippet exists.
- Record exact config path, command, env, transport, auth, and tool filters in `PROJECT-KNOWLEDGE.md`.
- Host smoke must run in the real host, not only in Inspector.
- If the host is remote and the app is desktop/local, design bridge local + broker remote from the start.
## OneMaster Draft Addendum

Track experimental, promoted, and blocked host states separately. A connector can be active in one
host lane while another host is package-lagging, source-only, or experimental. The release claim
must name the exact host lanes included.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atom OMD-M-29; tags BRIDGE / G1 /
G6 / G7 / LAB; claim limit: method/spec evidence only.
