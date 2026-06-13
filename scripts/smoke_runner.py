#!/usr/bin/env python3
"""Smoke runner generico per CLI agent-native.
Esegue comandi read-only e registra output. Non esegue write.

Esempi:
  python smoke_runner.py "python app_cli.py"
  python smoke_runner.py shop-agent --test "doctor --format json" --test "auth status" --timeout 20
"""
import argparse, subprocess, json, time, shlex
from pathlib import Path

DEFAULT_TESTS = ["doctor --format json", "--help"]

def run(base, test, timeout):
    cmd = base + shlex.split(test)
    t0 = time.time()
    try:
        p = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
        return {"cmd": cmd, "returncode": p.returncode,
                "latency_ms": int((time.time()-t0)*1000),
                "stdout": p.stdout[:4000], "stderr": p.stderr[:2000]}
    except Exception as e:
        return {"cmd": cmd, "error": type(e).__name__, "message": str(e),
                "latency_ms": int((time.time()-t0)*1000)}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tool", help="comando base, anche multi-parte tra virgolette (es. 'python app_cli.py')")
    ap.add_argument("--test", action="append", default=None, help="sottocomando ripetibile (read-only)")
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--output", default=None, help="scrivi risultati JSON su file")
    args = ap.parse_args()
    base = shlex.split(args.tool)
    tests = args.test if args.test else DEFAULT_TESTS
    results = [run(base, t, args.timeout) for t in tests]
    payload = {"base": base, "results": results}
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)
