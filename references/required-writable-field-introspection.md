# Required And Writable Field Introspection

Status: active-v3-candidate / partial needs-evidence
Class: reference

Use this when required fields, writable fields, or field units are unknown, stale, surface-specific, or discoverable only through live schema, typed errors, exports, UI controls, or import templates.

## Problem

Documentation often tells you that an object or command exists, but not which fields are required or writable for this host, version, data source, object state, and surface.

## Rule

Do not promote a write command until required and writable fields are evidenced for the actual surface.

Evidence can come from:

- official schema or SDK metadata;
- CLI/MCP discovery;
- OpenAPI or typed errors;
- official import/export template headers;
- UI control metadata;
- dry-run validation messages;
- minimal create/update experiments in sandbox.

## Required Field Evidence

For each command, record:

- fields required by the app;
- fields required by the connector contract;
- defaults supplied by the app;
- defaults supplied by the bridge;
- fields defined on another object/sheet/surface;
- fields that are required only in a lifecycle state.

## Writable Field Evidence

For each writable field, record:

- surface where it is writable;
- object class;
- state/lifecycle constraints;
- unit profile;
- validation rule;
- dependent fields;
- protected-field relation;
- readback query.

## Stop Rules

Stop if:

- required fields are unknown;
- writable status is inferred from a label or table column only;
- the field is present in export but not proven import/write-ready;
- a field belongs to another sheet/object/surface;
- a dry-run error shows schema mismatch and the bridge guesses around it.
