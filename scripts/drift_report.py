#!/usr/bin/env python3
"""Drift report. Senza argomenti genera un template; con --expected/--current
confronta due file (hash + primo diff di riga) e segnala il drift."""
import argparse, hashlib, sys
from datetime import datetime, timezone
from pathlib import Path

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def first_diff(a, b):
    la = Path(a).read_text(encoding="utf-8-sig", errors="replace").splitlines()
    lb = Path(b).read_text(encoding="utf-8-sig", errors="replace").splitlines()
    for i, (x, y) in enumerate(zip(la, lb), 1):
        if x != y:
            return {"line": i, "expected": x[:200], "current": y[:200]}
    if len(la) != len(lb):
        return {"line": min(len(la), len(lb))+1, "note": "lunghezze diverse",
                "expected_lines": len(la), "current_lines": len(lb)}
    return None

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--expected")
    ap.add_argument("--current")
    ap.add_argument("--label", default="snapshot")
    ap.add_argument("--output", default="DRIFT_REPORT.generated.md")
    args = ap.parse_args()
    ts = datetime.now(timezone.utc).isoformat()
    if args.expected and args.current:
        he, hc = sha(args.expected), sha(args.current)
        drift = he != hc
        out = [f"# Drift Report", f"", f"Generated: {ts}", f"Label: {args.label}", "",
               f"- expected: `{args.expected}` sha256={he[:16]}",
               f"- current:  `{args.current}` sha256={hc[:16]}",
               f"- **drift: {'YES' if drift else 'no'}**", ""]
        if drift:
            d = first_diff(args.expected, args.current)
            out.append(f"Primo diff: {d}")
        Path(args.output).write_text("\n".join(out), encoding="utf-8")
        print("\n".join(out))
        sys.exit(1 if drift else 0)
    else:
        content = (f"# Drift Report\n\nGenerated: {ts}\n\n"
                   "| Area | Versione prima | Versione dopo | Test | Esito | Azione |\n"
                   "|---|---|---|---|---|---|\n"
                   "| Host AI |  |  |  |  |  |\n| App target |  |  |  |  |  |\n"
                   "| API/SDK |  |  |  |  |  |\n| CLI/MCP |  |  |  |  |  |\n")
        Path(args.output).write_text(content, encoding="utf-8")
        print(f"Wrote {args.output} (template). Usa --expected/--current per il confronto reale.")
