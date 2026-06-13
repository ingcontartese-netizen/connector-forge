# Operating Knowledge Gate (R3-21)

ID: R3-21
Owner: JOINT
Status: active-v3-candidate / WP12.5 source verified
Class: gate + per-connector artifact
Evidence rows: L56, L61, L63, L77, L78, L82

## 1. Problem

Building a bridge is not the same as operating correctly through it. A connector can know how to click, import, call an endpoint, or write a field while still misunderstanding the domain operation.

Mechanics success is not operational correctness.

## 2. Core Rule

For non-trivial domains, a write or live operation requires an operating knowledge artifact before apply. The artifact does not need to be a full product manual, but it must capture the operational rules that affect the requested command.

If the bridge does not know what the command means in the target domain, it must remain in inspect/export/dry-run mode.

## 3. Required Knowledge

Minimum operating knowledge for a write-capable command:

- domain object class and lifecycle state;
- human-facing labels and technical identifiers;
- command surface: API, CLI, file sheet, UI tab, or control;
- required fields and writable fields;
- protected fields and never-write fields;
- display units, storage units, import units;
- minimal authoritative field to write;
- dependent fields to read, not force;
- side effects and recompute requirements;
- valid host state and selection state;
- rollback or compensation route;
- expert/domain validation notes.

## 4. Minimal Authoritative Write

Prefer writing the smallest authoritative field that the host engine expects, then read dependent fields after the host applies its own rules.

Do not write dependent fields merely because they are visible, unless the operating manual says they are independently writable and required.

## 5. Sheet/Surface Compatibility

If the actuator is a file or spreadsheet import, the sheet/tab and header names are part of the command grammar. A field valid on one sheet may be invalid or dangerous on another.

The bridge must record:

- sheet or surface name;
- accepted column/header labels;
- required rows;
- fields that must be defined elsewhere;
- fields that can be assigned on this surface.

## 6. Evidence From P6

P6 showed the gate clearly:

- duration display/storage/import units can differ;
- task sheet fields differ from resource sheet fields;
- a duration update should write the authoritative duration field, then read remaining/at-complete/dependent values;
- F9/schedule may be required for derived outputs, but a recompute action is distinct from the field write itself.

Giuseppe's domain input was evidence, not a bypass around governance.

## 7. Artifact

Use `OPERATING_MANUAL.md` for the per-connector artifact.

The manual must include, at minimum:

- domain object mapping;
- command schema;
- surface grammar;
- field and unit semantics;
- minimal write / dependent read;
- side effects and recompute;
- protected rules;
- host and actuator assignment;
- pre-apply and post-apply checks;
- expert notes with binding level.

## 8. Stop Rules

Stop if:

- the operation name is understood only as a UI label;
- required/writable fields are unknown;
- units are unknown;
- sheet/surface compatibility is unknown;
- side effects or recompute needs are unknown for a state-changing command;
- the only evidence is "the tool accepted it" without domain readback.

## 9. Status

`active-v3-candidate / WP12.5 source verified`

## 10. WP12.5 Codex Addition

Codex expanded `OPERATING_MANUAL.md` with command schema columns, unit calibration states, recompute states, host/actuator assignment, and example check definitions.

Pending Claude second-read: improve structure/wording, add compact case-study examples, and verify no P6-specific rule leaked into the generic template.
