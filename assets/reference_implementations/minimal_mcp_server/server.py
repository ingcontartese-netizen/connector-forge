"""Minimal FastMCP server with lifecycle logging.

Requires: pip install mcp
Stdio start: python server.py
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
import traceback
import uuid
from datetime import datetime, timezone
from pathlib import Path

from mcp.server.fastmcp import FastMCP

APP_NAME = "connector-forge-demo"
VERSION = "0.1.0"
MODE = os.getenv("CONNECTOR_MODE", "stub")
ROOT = Path(__file__).resolve().parent
LOG_PATH = Path(os.getenv("CONNECTOR_LIFECYCLE_LOG", ROOT / "logs" / "mcp_bridge_lifecycle.jsonl"))


def _build_stamp() -> str:
    try:
        return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16]
    except Exception:
        return "unknown"


BUILD_STAMP = os.getenv("CONNECTOR_BUILD_STAMP", _build_stamp())


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_text(value: object, limit: int = 500) -> str:
    text = str(value)
    for marker in ("token=", "authorization=", "password=", "secret="):
        text = text.replace(marker, f"{marker}[REDACTED]")
    return text[:limit]


def log_event(event: str, **fields: object) -> None:
    """Best-effort JSONL lifecycle log. Never raise from logging."""
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "ts": _now(),
            "event": event,
            "app": APP_NAME,
            "version": VERSION,
            "build_stamp": BUILD_STAMP,
            **fields,
        }
        with LOG_PATH.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
    except Exception:
        pass


mcp = FastMCP(APP_NAME)


@mcp.tool()
def health() -> dict:
    """Verify process identity, build stamp, and live/mock/stub mode."""
    request_id = str(uuid.uuid4())
    started = time.perf_counter()
    log_event("tool_requested", tool="health", request_id=request_id, bounded_args_summary={})
    result = {
        "ok": True,
        "app": APP_NAME,
        "version": VERSION,
        "build_stamp": BUILD_STAMP,
        "built_at": _now(),
        "mode": MODE,
        "log_path": str(LOG_PATH),
    }
    log_event(
        "tool_completed",
        tool="health",
        request_id=request_id,
        elapsed_ms=round((time.perf_counter() - started) * 1000, 2),
        result_count=1,
        has_more=False,
    )
    return result


@mcp.tool()
def get_context() -> dict:
    """Use this when you need the current app context before choosing a connector action."""
    request_id = str(uuid.uuid4())
    started = time.perf_counter()
    log_event("tool_requested", tool="get_context", request_id=request_id, bounded_args_summary={})
    result = {"ok": True, "app": "demo", "document": None, "mode": MODE}
    log_event(
        "tool_completed",
        tool="get_context",
        request_id=request_id,
        elapsed_ms=round((time.perf_counter() - started) * 1000, 2),
        result_count=1,
        has_more=False,
    )
    return result


@mcp.tool()
def export_preview(target_id: str, format: str = "markdown") -> dict:
    """Use this when you need a safe preview artifact for a target object."""
    request_id = str(uuid.uuid4())
    started = time.perf_counter()
    log_event(
        "tool_requested",
        tool="export_preview",
        request_id=request_id,
        bounded_args_summary={"target_id_len": len(target_id), "format": format},
    )
    try:
        result = {"ok": True, "target_id": target_id, "format": format, "path": f"./preview-{target_id}.{format}"}
        log_event(
            "tool_completed",
            tool="export_preview",
            request_id=request_id,
            elapsed_ms=round((time.perf_counter() - started) * 1000, 2),
            result_count=1,
            has_more=False,
        )
        return result
    except Exception as exc:
        log_event(
            "tool_failed",
            tool="export_preview",
            request_id=request_id,
            elapsed_ms=round((time.perf_counter() - started) * 1000, 2),
            error_type=type(exc).__name__,
            traceback_redacted=_safe_text(traceback.format_exc()),
        )
        raise


if __name__ == "__main__":
    started = time.perf_counter()
    log_event(
        "process_start",
        pid=os.getpid(),
        python=sys.version.split()[0],
        cwd=os.getcwd(),
        bridge_root=str(ROOT),
        mode=MODE,
    )
    log_event("transport_start", transport="stdio")
    try:
        mcp.run()
    except Exception as exc:
        log_event("process_error", error_type=type(exc).__name__, traceback_redacted=_safe_text(traceback.format_exc()))
        raise
    finally:
        log_event("process_end", pid=os.getpid(), elapsed_ms=round((time.perf_counter() - started) * 1000, 2), reason="exit")
