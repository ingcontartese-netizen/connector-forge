#!/usr/bin/env python3
import argparse, json, sys, time

VERSION = "0.1.0"

def emit(obj, fmt):
    if fmt == "json":
        print(json.dumps(obj, indent=2, ensure_ascii=False))
    else:
        if obj.get("ok"):
            print(obj.get("message", "ok"))
        else:
            print(f"{obj['error']['code']}: {obj['error']['message']}", file=sys.stderr)

def main():
    p = argparse.ArgumentParser(prog="acme")
    p.add_argument("--format", choices=["json","text"], default="text")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("doctor")
    s = sub.add_parser("search"); s.add_argument("--query", required=True); s.add_argument("--limit", type=int, default=5)
    g = sub.add_parser("get"); g.add_argument("--id", required=True)
    e = sub.add_parser("export"); e.add_argument("--id", required=True); e.add_argument("--output", required=True)
    args = p.parse_args()
    if args.cmd == "doctor":
        emit({"ok": True, "version": VERSION, "message": "doctor ok", "meta": {"timestamp": int(time.time())}}, args.format)
    elif args.cmd == "search":
        emit({"ok": True, "data": [{"id": "demo-1", "title": f"Result for {args.query}"}], "meta": {"count": 1}}, args.format)
    elif args.cmd == "get":
        emit({"ok": True, "data": {"id": args.id, "title": "Demo object"}}, args.format)
    elif args.cmd == "export":
        with open(args.output, "w", encoding="utf-8") as f: f.write("Demo export\n")
        emit({"ok": True, "data": {"path": args.output}, "message": f"exported {args.output}"}, args.format)
    else:
        p.print_help(); sys.exit(2)

if __name__ == "__main__":
    main()
