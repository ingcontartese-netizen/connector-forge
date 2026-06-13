# WINDOWS_UTF8_GUARDRAIL

Project:
Connector:
Host:
Environment:
Date:
Owner:

## Runtime Settings

- Host OS:
- Python version:
- Console/code page observed:
- `PYTHONIOENCODING=utf-8` set:
- `PYTHONUTF8=1` or `python -X utf8` set:
- File/log writes use `encoding="utf-8"`:

## Output Channels

| Channel | Policy | Evidence |
|---|---|---|
| stdout | machine-readable, small, protocol-safe | |
| stderr | diagnostics only, no secrets | |
| lifecycle log | UTF-8 JSONL | |
| artifact file | UTF-8, used for long/rich text | |

## Test Payloads

| Payload | Expected behavior | Evidence |
|---|---|---|
| accented text | no `UnicodeEncodeError`; preserved in file/artifact or escaped JSON | |
| symbol / non-ASCII comment | no console crash; summary or artifact path returned | |
| long comment/report | summary in chat/log, full content in artifact | |

## Decision

- UTF-8 guardrail status: verified / HOLD / BLOCKED / N/A with reason
- Blocking gaps:
- Next action:
