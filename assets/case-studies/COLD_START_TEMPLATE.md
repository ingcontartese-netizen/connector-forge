# Cold-Start Acceptance Test

Purpose: prove that connector-forge can guide an agent on an app that was not pre-studied in the current project.

Until this test passes, use `field-tested`, not `deployment-ready`.

## Anti-Cheating Rules

- Do not use Archicad or ValuAziende as the cold-start target.
- Do not start from a prebuilt bridge or prepared schema unless that is the discovered authorized surface.
- The human may provide access and approvals, but should not choose the technical path for the agent.
- The agent must show that decisions came from Gate 0, Source Registry, Surface Map, and Capability Ledger.

## Minimum Chain

```text
Gate 0 -> Source Registry -> Surface Map -> Capability Ledger -> first verified read -> governed write/dry-run/readback/rollback if in scope
```

## Evidence Table

| Step | Evidence path / transcript | Status | Notes |
|---|---|---|---|
| Gate 0 doubt-list | | | |
| Source Registry | | | |
| Surface Map / Ladder | | | |
| Capability Ledger | | | |
| First live read | | | |
| Stop-rule or recovery case | | | |
| First write dry-run / governed proposal | | | |
| Readback and rollback scope | | | |

## Verdict

- `deployment-ready`: full chain passed and method guided decisions.
- `field-tested`: known cases passed but cold-start is incomplete.
- `HOLD`: missing access, auth, test environment, or approval.
- `BLOCKED`: no authorized/verifiable surface.

## Declared Limits

Record what the skill did not guide well. These limits become `declared_limits` in the Capability Ledger and release notes.
