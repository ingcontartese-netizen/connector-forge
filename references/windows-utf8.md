# Windows UTF-8 Guardrail

Use this reference when a connector runs on Windows, emits user-facing text, handles comments/notes, or logs non-ASCII data.

Problem: a valid read can fail during reporting because the console uses a legacy code page such as cp1252. This is a deployment problem, not a data problem.

## Host environment

For Python bridges and CLI wrappers on Windows, prefer:

```powershell
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
python -X utf8 server.py
```

In host pack config, set:

```json
{
  "env": {
    "PYTHONIOENCODING": "utf-8",
    "PYTHONUTF8": "1"
  }
}
```

## File and log I/O

- Open text files with `encoding="utf-8"`.
- For JSON, use `ensure_ascii=False` only when the receiving channel is UTF-8 safe; otherwise keep escaped JSON or write an artifact file.
- Prefer artifact files for long comments, rich text, and large reports.
- Keep stdout machine-readable and small; use stderr or lifecycle log files for diagnostics.

## Acceptance

Verify with at least one payload containing accented text and one non-BMP or symbol character. If console output fails but file/artifact output works, keep the connector usable by returning artifact path plus summary.
