# Adapter Contract

The adapter is the reusable core. Build it before packaging as CLI, MCP, or Hybrid.

## Required Sections

```yaml
app:
  name:
  version:
  environment:
  owner:
surface:
  type:
  evidence:
auth:
  mode:
  scopes:
  secret_storage:
resources: []
operations: []
errors: []
safety:
  dry_run:
  approval:
  rollback:
evidence: []
```

## Resource Rules

- Use stable IDs from the app, not display names.
- Record canonical read operation before write operation.
- Mark PII, secrets, files, money, legal, or irreversible state.

## Operation Rules

Each operation needs:

- name and intent;
- input schema;
- output schema;
- side effects;
- idempotency;
- auth scope;
- timeout/rate limit expectations;
- error taxonomy;
- evidence and acceptance test.

No operation is `verified` without docs, code, local probe, or a passing fixture.
