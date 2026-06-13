# Write Intent Proof

Use this reference before any connector write that changes app state, creates native objects, edits business data, or changes files/projects the user cares about.

Gate 13 exists because a technically successful write can still fail the user intent. A wall can have the right length but the wrong position. A proposal can be stored but bypass the governed approval path. A UI note can be created while the requested native object was not created.

## Required Chain

Every write must pass this chain before it is called successful:

```text
intent contract -> command availability -> dry-run -> approval -> apply -> readback -> intent proof -> rollback scope -> user-facing confirmation
```

## Intent Contract

Capture the user intent before applying:

- original user request;
- target object or record;
- operation risk class: `read`, `safe`, `write-safe`, `write-governed`, `write`, `write-destructive`, or `open-world`;
- native/proxy class: `native_verified`, `native_hypothesis`, `visual_proxy`, `metadata_only`, `unsafe_generic`, or `forbidden_proxy_for_native_request`;
- expected object type and required fields;
- units and conversion;
- anchor/reference object;
- direction/orientation/position when visual or geometric intent matters;
- parent/context/layer/story/project/document that must already exist;
- expected side effects;
- allowed ambiguity and required clarification;
- dry-run plan;
- rollback scope.

## Command Availability

Before dry-run, prove the operation is not just documented:

- source or docs say the command exists;
- installed version contains the command or equivalent;
- live app/add-on/SDK says the command is available;
- bridge/host catalog exposes it with stable schema;
- dry-run or schema-only call works;
- apply is allowed only in sandbox or approved environment.

Use `command-availability-matrix.md` for the detailed table.

## Dry-Run

The dry-run must produce a plan the user or verifier can inspect:

- operation name;
- target IDs or creation scope;
- payload summary;
- expected created/modified/deleted objects;
- side effects;
- risk class;
- rollback scope;
- whether approval is required.

Dry-run without the ability to predict affected objects is not enough for write readiness.

## Apply

Apply only after approval and only within the declared scope.

For create operations, capture the created object IDs. For modify operations, capture a before snapshot or enough fields to perform an inverse modify. For governed domains, apply usually means creating a proposal, not mutating the domain object directly.

## Readback

Read back from the app, not from local memory or the request payload.

Minimum readback:

- object ID/GUID or stable ID;
- object type/class;
- fields that prove the requested change;
- mode/live proof when applicable;
- source of readback;
- timestamp or transcript path.

## Intent Proof

Compare expected vs actual.

For CAD/BIM/visual/geometric writes:

- length/size;
- start/end or bounding geometry;
- orientation/direction;
- anchor/reference relationship;
- layer/story/context;
- native object class;
- visual confirmation or equivalent render/check when the user intent was visual.

For business/data writes:

- record ID;
- changed fields;
- unchanged protected fields;
- approval/proposal state when governed;
- calculation engine untouched unless explicitly authorized;
- audit event.

For files/projects:

- output path;
- checksum or diff;
- no overwrite outside the intended path;
- recoverable backup if modified in place.

## Rollback Scope

Declare rollback before success:

- created IDs can be deleted or archived;
- modified IDs have before snapshot or inverse payload;
- governed proposals can be rejected/withdrawn;
- manual rollback is a documented recovery, not an automatic pass.

## Failure Rule

If measurement passes but placement, native class, governed flow, parent relation, or protected fields fail, the write is not successful. Report partial success, keep evidence, and either rollback or ask for approval before correction.
## OneMaster Draft Addendum

For high-value app writes, bind approval to a concrete dry-run artifact: operation, target identity,
expected changeset, challenge token, dry-run hash, and runtime fingerprint. A token alone is not
enough if the payload or runtime changed after approval.

Evidence provenance: ValuAziende OneMaster Draft, 2026-06-03; atoms OMD-M-17, OMD-M-20; tags
APP / BRIDGE / G1 / G6 / G7 / LAB; claim limit: method/spec evidence only.
