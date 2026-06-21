# Package Integrity

Use this reference before publishing or handing off Rev2 packages across Codex and Cowork.

Package integrity is a release gate, not a first-edit blocker. A package can be in build progress, but it cannot be called ready until this check passes.

## Check

| Area | Check |
|---|---|
| Core | `SKILL.md` and the shipped core references agree on funnel, stop rules, risk classes, Gate 0.0 / Domain-Semantic scope, and write-path evidence status |
| References | Codex and Cowork packages expose equivalent method content, even if filenames differ |
| Templates | Required templates exist in each package or are documented as host-specific omissions |
| Scripts | Script behavior matches skill claims and compiles on Windows |
| Host packs | Host examples use carrier states from `carrier-parity-matrix.md`, such as `source_only`, `package_lag`, `package_built`, `installed_needs_smoke`, `host_loaded`, `host_live_validated`, `research_live_verify`, or `blocked` |
| Verifier | Cowork sub-agent, Codex verifier/checklist, or manual verification path is explicit |
| Versioning | README, release notes, changelog, and manifest version agree |
| Historical manifests | Delivered/source manifests are historical evidence after source edits; the current build must use a fresh OneMaster manifest |
| v2.3 Fascia A | Domain references/templates exist; P6 case-study is evidence, not a P6 manual; Fascia B write-path remains `needs-evidence` |

## MCP OneMaster Checks

| Area | Check |
|---|---|
| Core MCP refs | Package includes the self-contained MCP core references: `mcp-procedure-track.md`, `mcp-artifact-matrix.md`, `mcp-inspector-lab.md`, `mcp-remote-first-baseline.md`, `carrier-parity-matrix.md`, and `mcp-2026-07-28-watchlist.md` |
| Runtime dependency | Public package does not require a separate MCP specialist skill to understand ordinary MCP design |
| Host pack parity | Each intended carrier has a declared state from `carrier-parity-matrix.md` |
| Host smoke | Any claim above source/package state points to host-loaded or host-live evidence |
| Remote-first | Broker, endpoint, auth, audit, and bridge assumptions are documented and revalidated when remote hosts are in scope |
| Manifest | Final manifest includes new MCP refs and modified existing refs; old manifests are marked historical |
| Current manifest | `SHA256SUMS_ONEMASTER_V1.txt` lives outside the skill folder and must be regenerated after output edits so it does not become self-referential |
| Lag declaration | If source changed but a carrier package was not rebuilt, installed/reloaded, and smoke-tested, declare package lag |

## Release rule

If any public claim says "ready", "validated", or "go-live", evidence must point to the real host smoke and package matrix row.
## OneMaster Draft Addendum

Package integrity must cover generation identity and carrier parity. A source edit in one host lane
creates drift until the package is rebuilt, checksummed, installed or reloaded, and smoke-tested.
If that is deferred, record `DECLARED_COWORK_LAG` or the equivalent host-lag state.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-12, OMD-M-13,
OMD-M-18, OMD-M-21, OMD-M-29, OMD-M-33; tags BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim
limit: method/spec evidence only.
