# Command-Schema Discovery

Use this reference when a command exists but the real input/output schema is unknown, stale, contradictory, or only partially documented.

This is a procedure, not a hard gate. The gate is: promote a command to `verified` only after a working payload and readback.

## Sequence

1. Start from primary docs, official repo, installed files, and live version.
2. Confirm command existence with `command-availability-matrix.md`.
3. Use read-only or dry-run calls in a sandbox.
4. Send the smallest valid-looking payload.
5. Read typed errors as schema evidence.
6. Add one field at a time.
7. Record failed useful payloads and the first working payload.
8. Promote only after live readback proves the operation.

## Safety Limits

- Never use destructive writes to learn a schema.
- Do not error-mine without authorization.
- Do not expose a generic/raw command gateway as a user-facing stable tool.
- If a wrapper serializer is wrong, document the lower-level fallback and keep it quarantined until tested.

## Evidence

Record in `WORKING_PAYLOADS.md`:

- failed payloads that revealed required fields;
- final working payload;
- expected output shape;
- readback transcript;
- remaining limits.

## Failure Rule

Documentation, examples, and memory are hypotheses. Working payload plus readback is evidence.
