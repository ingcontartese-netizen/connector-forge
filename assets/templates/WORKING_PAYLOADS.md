# WORKING_PAYLOADS

Project:
Connector:
Host:
Environment:
Date:

## Known-Good Read Payloads
| Operation | Input | Expected shape | Bounded-output proof | Evidence |
|---|---|---|---|---|
| health / doctor | | | N/A | |
| context / status | | | N/A or summary | |
| list / search | default `page_size=25`; probe `page_size=3` | bounded page + `result_count` | `has_more`/`next_cursor` or total metadata | |
| get / read one | stable object ID | one object only | N/A | |
| export / preview | | artifact path + checksum | no large raw dump | |

## Known-Good Dry-Run / Simulate Payloads
| Operation | Input | Expected shape | Safety note | Evidence |
|---|---|---|---|---|
| simulate | default `page_size=25`; probe `page_size=3`; include `limit`/`fields` when output can grow | bounded result, summary, cursor, or artifact path | no large raw payload dump | |
| action_prepare | | | | |
| propose | | | | |

## Known-Good Write Intent Payloads
| Operation | Intent contract | Dry-run input | Apply input | Readback expected shape | Intent proof evidence |
|---|---|---|---|---|---|
| create/update | `INTENT_CONTRACT.md` path | includes risk, native/proxy class, target, rollback scope | includes approval/idempotency key when required | stable ID + fields proving expected-vs-actual | readback transcript + comparison |

## Known Errors And Recovery
| Scenario | Expected error | Recovery instruction | Evidence |
|---|---|---|---|
| backend unavailable | | | |
| auth missing / expired | | | |
| permission denied | | | |
| object not found | | | |
| timeout / long-running task | | | |
| Windows non-ASCII console output | no crash; summary/artifact path or UTF-8-safe output | set UTF-8 env or write artifact | |
| lifecycle logger write failure | bridge continues; diagnostic warning only | fix log path/permissions | |
| command documented but not live available | typed unavailable/version error | update dependency, choose another surface, or keep capability hypothesis | |
| HOST_BUSY / app not idle | typed busy/lock/conflict error | bounded retry, ask user to finish input/Esc, then re-run readback | |
| intent proof mismatch | partial/fail with expected-vs-actual fields | rollback or ask for correction approval | |

## Output Limits
- Maximum payload size before summarizing or writing an artifact:
- Canonical default page size: 25
- Acceptance probe size: 3
- Default fields:
- Simulate/report limit policy:
- Cursor / has_more / total metadata policy:
- Redaction rules:
- Filesystem output path policy:

## Lifecycle / Encoding Payloads
- Health/version payload includes `version`, `build_stamp`, `built_at`, `mode`:
- Lifecycle log sample path:
- Lifecycle events verified:
- UTF-8 payload tested:
- Artifact fallback path for rich text:

## Promotion Notes
- Payloads verified on live app:
- Payloads still mock/stub:
- Payloads forbidden:
- Write payloads with readback + intent proof:
- Payloads failed but useful for schema/error discovery:
