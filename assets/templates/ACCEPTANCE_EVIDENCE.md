# ACCEPTANCE_EVIDENCE

Project:
Release:
Primary host:
Environment:
Date:
Owner:

## Evidence Index
| Gate | Status (`pass|fail|n/a`) | Evidence path / transcript | Notes |
|---|---|---|---|
| G0.0 Domain Comprehension | | | required for non-trivial domains |
| G0 Installability | | | |
| G1 Handshake | | | |
| G2 Tool discovery | | | |
| G3 State introspection | | | |
| G3.1 Domain-Semantic Validation | | | required before user-facing answers from technical data |
| G4 Read/export proof | | | |
| G5 Safety proof | | | |
| G6 Host smoke + recovery | | | |
| G10 Host-live states | | | |
| G11 Bounded output | | | |
| G12 Lifecycle observability | | | |
| G13 Write intent proof | | | |
| G14 Cold-start acceptance | | | |

## Host-Live State Chain
| State | Status (`pass|fail|n/a`) | Evidence path / transcript | Notes |
|---|---|---|---|
| `source_validated` | | | contract/source/template checks |
| `fresh_process_validated` | | | restart/reload after source change; cache-bust if needed |
| `host_loaded` | | | host handshake + tools/catalog loaded |
| `host_live_validated` | | | host live read + recovery/error proof |

## Lifecycle Observability
| Check | Status (`pass|fail|n/a`) | Evidence path / transcript | Notes |
|---|---|---|---|
| JSONL lifecycle log exists | | | path such as `logs/mcp_bridge_lifecycle.jsonl` |
| `process_start` event | | | includes version/build_stamp/mode |
| transport start event | | | stdio/HTTP/other |
| tool requested/completed pair | | | includes request_id if available |
| error/recovery event | | | redacted traceback or typed error |
| redaction check | | | no tokens/secrets/full payloads |
| stdout clean | | | protocol/result only |

## Live Evidence
| Capability | Mode (`live|mock|stub`) | Input | Result summary | Evidence |
|---|---|---|---|---|
| doctor / health | | | | |
| context / status | | | | |
| list / read | | | | |
| export / preview | | | | |
| simulate / dry-run | | | | |
| propose / prepare | | | | |

## Pagination / Output Control
- Canonical default page size: 25
- Acceptance probe: `page_size=3` or equivalent small limit
- Probe result count:
- Cursor / next page behavior:
- Total / has_more / next_cursor metadata:
- Fields projection / summary / artifact behavior:
- Large-output handling:
- Redaction / fields projection:
- Maximum raw payload allowed in chat/log before summary/artifact:
- Variable-size operations still unbounded:

## Windows UTF-8 Guardrail
- Applies? yes / no
- `PYTHONIOENCODING=utf-8` / `PYTHONUTF8=1` or equivalent:
- File/log writes use UTF-8:
- Non-ASCII test payload:
- Long/rich text uses summary or artifact path:

## Natural User Questions
| Question | UI_FIELD_MAP checked (`yes|no|n/a`) | Tool/op | Result summary | Evidence |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |

## Domain-Semantic Evidence
| Capability/question | Domain class | False-friend checked | Identity key | Technical read state | Domain semantics state | User answer state | Evidence |
|---|---|---|---|---|---|---|---|
|  |  |  |  | technical_read_verified/hypothesis | domain_semantics_verified/hypothesis | user_answer_verified/hypothesis | |

## Safety Evidence
- Write class:
- Operation risk: `read | safe | write-safe | write-governed | write | write-destructive | open-world`
- Native/proxy class:
- declared_limits checked against README/tool metadata:
- Sandbox identity:
- Command availability evidence:
- Dry-run transcript:
- Approval path:
- Rollback / recovery:
- Audit log evidence:

## Write Intent Proof
- Intent contract path:
- Original request:
- Expected target object/record:
- Expected position / relationship / protected fields:
- Apply transcript:
- Readback source:
- Created/modified object IDs:

| Expected | Actual | Pass/fail | Evidence |
|---|---|---|---|
| object/record ID | | | |
| native/proxy class | | | |
| key fields/properties | | | |
| position/orientation/relationship | | | |
| governed proposal/audit state | | | |

## Cold-Start Evidence
- Required before `deployment-ready` / GitHub-ready claims: yes / no / n/a
- App was not pre-studied in this project: yes / no
- Gate 0 path:
- Source Registry path:
- Surface Map path:
- Capability Ledger path:
- First verified read evidence:
- First governed write/dry-run/readback/rollback evidence:
- Recovery/stop-rule evidence:
- Case-study path:

## Release Decision
Host-live state: `source_validated | fresh_process_validated | host_loaded | host_live_validated | HOLD | BLOCKED`
Release state: `local_validated | host_runnable | go_live | HOLD | BLOCKED`
Blocking gaps:
Next action:
