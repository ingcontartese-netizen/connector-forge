---
name: connector-toolsmith
description: Use this skill when building, verifying, or improving a CLI/MCP/API/hybrid connector for a target app.
---

# Connector Toolsmith

## Procedure

1. Run Gate 0.0 Domain Comprehension when the domain is non-trivial.
2. Build Gate 0, Source Registry, Surface Map, and Capability Ledger.
3. Choose CLI, MCP, Hybrid, API, file workflow, browser/UI, computer-use, or STOP through the decision engine.
4. Compile Adapter Contract plus the branch contract (`CLI_CONTRACT.yaml` or `MCP_TOOL_CATALOG.json`).
5. Implement the smallest read-only health/discovery/read/export path first.
6. Add writes only with intent proof, dry-run/simulate, approval, rollback/recovery readiness, and predeclared readback.
7. For non-trivial writes, create `OPERATING_MANUAL.md` and actuator/readback evidence before apply.
8. Run acceptance tests and extended acceptance evidence.
9. Create host pack, package integrity evidence, drift report, and release claim audit only when release is in scope.

## Stop Rules

Stop if any of these is missing:

- authorized surface;
- real environment or sandbox;
- auth/scopes/test account;
- stable target identity;
- field allowlist and protected-field rules for writes;
- unit/semantic operating knowledge for numeric, progress, duration, date, rate, or status writes;
- rollback/recovery route for writes;
- readback scope proportional to operation and actuator risk;
- explicit claim limits.

Direct private datastore writes are forbidden unless the vendor explicitly authorizes that write path for the actual data source.
