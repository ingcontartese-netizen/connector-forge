#!/usr/bin/env python3
"""Cautious read-only probe for common web/API surfaces.

No aggressive scanning, no auth bypass. Use only on authorized targets.
"""
import argparse
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_ENDPOINTS = ["/openapi.json", "/docs", "/redoc", "/health", "/version"]


def get(url, timeout, headers):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(4096)
            return {
                "ok": True,
                "status": r.status,
                "content_type": r.headers.get("Content-Type"),
                "sample": body[:500].decode("utf-8", "replace"),
            }
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "error": "HTTPError", "message": str(e)}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__, "message": str(e)}


def classify(results):
    if results.get("/openapi.json", {}).get("ok"):
        return "openapi"
    if results.get("/docs", {}).get("ok") or results.get("/redoc", {}).get("ok"):
        return "docs_only"
    if results.get("/health", {}).get("ok"):
        return "health_only"
    return "unknown"


def markdown_report(base_url, results, surface):
    lines = [
        "# Surface Probe Report",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Base URL: `{base_url}`",
        f"Surface class: `{surface}`",
        "",
        "| Endpoint | OK | Status/Error | Content-Type |",
        "|---|---|---|---|",
    ]
    for path, row in results.items():
        status = row.get("status") or row.get("error")
        lines.append(f"| `{path}` | {row.get('ok')} | {status} | {row.get('content_type', '')} |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Read-only probe only.",
            "- Treat findings as `hypothesis` until live smoke validates operations.",
            "- If OpenAPI is present, run `openapi_contract_stub.py` next.",
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--endpoint", action="append", help="extra endpoint path; repeatable")
    ap.add_argument("--header", action="append", default=[], help="HTTP header as Name: Value; repeatable")
    ap.add_argument("--timeout", type=float, default=5.0)
    ap.add_argument("--out", default="surface_probe.generated")
    args = ap.parse_args()

    headers = {}
    for raw in args.header:
        if ":" not in raw:
            raise SystemExit(f"Invalid header: {raw}")
        name, value = raw.split(":", 1)
        headers[name.strip()] = value.strip()

    endpoints = list(DEFAULT_ENDPOINTS)
    for endpoint in args.endpoint or []:
        endpoints.append(endpoint if endpoint.startswith("/") else "/" + endpoint)

    base = args.base_url.rstrip("/")
    results = {path: get(base + path, args.timeout, headers) for path in endpoints}
    surface = classify(results)
    payload = {"base_url": base, "surface_class": surface, "results": results}

    out_base = Path(args.out)
    json_path = out_base.with_suffix(".json")
    md_path = out_base.with_suffix(".md")
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(markdown_report(base, results, surface), encoding="utf-8")
    print(json.dumps({"surface_class": surface, "json": str(json_path), "md": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
