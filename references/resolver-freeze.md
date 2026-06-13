# Resolver Freeze and Identity Keys

Use this when user-facing labels must be resolved to app-native IDs, especially before writes, readback, or audit.

## Problem

Users use names, visible codes, or descriptions. Apps use GUIDs, ObjectIds, database IDs, composite keys, natural keys, or versioned IDs. If preview resolves one object and apply resolves again later, the connector can touch the wrong object.

## Rule

Every capability declares the canonical identity key. Before apply, freeze the resolver output and reuse it for preview, apply, readback, rollback, and audit.

Minimum identity map:

- `human_label`;
- `canonical_id`;
- `secondary_keys`;
- `domain_class`;
- `resolver_query`;
- `resolver_timestamp`;
- `confidence`;
- `ambiguity_policy`;
- `freeze_scope`.

## Examples

- CAD/BIM: modify by GUID, not "the wall on the left".
- Scheduling: use internal ObjectId for writes, keep Activity ID for UX.
- Finance/CRM: ticker, company id, and database id are not automatically equivalent.

## Test

Readback must cite the same `canonical_id` that preview/apply used. Ambiguity must block apply or request user selection.
