#!/usr/bin/env python3
"""Generate draft Adapter/CLI contracts from a local OpenAPI JSON file.

The output is intentionally conservative: operation risk is a first draft,
not authority. Promote operations only after live smoke evidence.
"""
import argparse
import json
import re
from pathlib import Path

WRITE_METHODS = {"post", "put", "patch", "delete"}
GOVERNED_HINTS = re.compile(r"approve|approval|proposal|propose|portfolio|valuation|financial|govern", re.I)
DESTRUCTIVE_HINTS = re.compile(r"delete|remove|drop|reset|purge|destroy", re.I)


def risk(method, path, operation_id):
    text = f"{method} {path} {operation_id or ''}"
    if method.lower() == "delete" or DESTRUCTIVE_HINTS.search(text):
        return "write-destructive"
    if method.lower() in WRITE_METHODS:
        if GOVERNED_HINTS.search(text):
            return "write-governed"
        return "write"
    if re.search(r"export|preview|download", text, re.I):
        return "safe"
    return "read"


def iter_operations(spec):
    for path, methods in spec.get("paths", {}).items():
        for method, op in (methods or {}).items():
            if method.lower() not in {"get", "post", "put", "patch", "delete"}:
                continue
            op = op or {}
            operation_id = op.get("operationId") or f"{method}_{path}".strip("/").replace("/", "_").replace("{", "").replace("}", "")
            yield {
                "method": method.upper(),
                "path": path,
                "operationId": operation_id,
                "summary": op.get("summary") or op.get("description", "")[:120],
                "risk": risk(method, path, operation_id),
            }


def q(value):
    return json.dumps(value, ensure_ascii=False)


def write_adapter_contract(out_dir, operations, title):
    lines = [
        "adapter:",
        f"  app: {q(title)}",
        "  version: \"0.1.0-draft\"",
        "  source: \"openapi\"",
        "operations:",
    ]
    for op in operations:
        lines.extend(
            [
                f"  - id: {q(op['operationId'])}",
                f"    method: {q(op['method'])}",
                f"    path: {q(op['path'])}",
                f"    risk: {q(op['risk'])}",
                "    status: \"hypothesis\"",
                "    evidence: \"generated from OpenAPI; requires live smoke\"",
                "    auth: \"TODO\"",
                "    errors: []",
            ]
        )
    (out_dir / "ADAPTER_CONTRACT.generated.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_cli_contract(out_dir, operations, title):
    lines = [
        f"cli_name: {q(title.lower().replace(' ', '-'))}",
        "version: \"0.1.0-draft\"",
        "commands:",
        "  doctor:",
        "    risk: \"read\"",
        "    output: \"json\"",
    ]
    for op in operations:
        cmd = op["operationId"].replace("_", "-")
        flags = ["--format", "--timeout"]
        if op["risk"] in {"read", "safe"}:
            flags.extend(["--limit", "--cursor", "--fields"])
        if op["risk"].startswith("write"):
            flags.extend(["--dry-run", "--idempotency-key"])
        lines.extend(
            [
                f"  {cmd}:",
                f"    source_operation: {q(op['operationId'])}",
                f"    risk: {q(op['risk'])}",
                f"    flags: [{', '.join(q(f) for f in flags)}]",
                "    status: \"hypothesis\"",
            ]
        )
    lines.extend(
        [
            "safety:",
            "  dry_run_format: \"json_diff\"",
            "  fail_closed_exit_code: 10",
            "  write_governed_direct_write_forbidden: true",
        ]
    )
    (out_dir / "CLI_CONTRACT.generated.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("openapi_json")
    ap.add_argument("--out-dir", default=".")
    args = ap.parse_args()

    spec = json.loads(Path(args.openapi_json).read_text(encoding="utf-8-sig"))
    title = spec.get("info", {}).get("title", "connector")
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    operations = list(iter_operations(spec))

    (out_dir / "openapi_operations.generated.json").write_text(
        json.dumps(operations, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    write_adapter_contract(out_dir, operations, title)
    write_cli_contract(out_dir, operations, title)
    print(json.dumps({"operations": len(operations), "out_dir": str(out_dir)}, indent=2))


if __name__ == "__main__":
    main()
