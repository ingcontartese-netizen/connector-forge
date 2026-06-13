# Package Integrity

Use this reference before publishing or handing off Rev2 packages across Codex and Cowork.

Package integrity is a release gate, not a first-edit blocker. A package can be in build progress, but it cannot be called ready until this check passes.

## Check

| Area | Check |
|---|---|
| Core | `CONNECTOR_FORGE_CORE.md` and `SKILL.md` agree on funnel, stop rules, risk classes, v2.3 Gate 0.0 / Domain-Semantic scope, and deferred write-path status |
| References | Codex and Cowork packages expose equivalent method content, even if filenames differ |
| Templates | Required templates exist in each package or are documented as host-specific omissions |
| Scripts | Script behavior matches skill claims and compiles on Windows |
| Host packs | Host examples are marked verified, draft, or research/live-verify |
| Verifier | Cowork sub-agent, Codex verifier/checklist, or manual verification path is explicit |
| Versioning | README, release notes, changelog, and manifest version agree |
| v2.3 Fascia A | Domain references/templates exist; P6 case-study is evidence, not a P6 manual; Fascia B write-path remains `needs-evidence` |

## Release rule

If any public claim says "ready", "validated", or "go-live", evidence must point to the real host smoke and package matrix row.
## OneMaster Draft Addendum

Package integrity must cover generation identity and carrier parity. A source edit in one host lane
creates drift until the package is rebuilt, checksummed, installed or reloaded, and smoke-tested.
If that is deferred, record `DECLARED_COWORK_LAG` or the equivalent host-lag state.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-12, OMD-M-13,
OMD-M-18, OMD-M-21, OMD-M-29, OMD-M-33; tags BRIDGE / G1 / G6 / G7 / GIUSEPPE / LAB; claim
limit: method/spec evidence only.
