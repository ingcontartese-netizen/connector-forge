# CLAUDE.md — Claude Code host pack

## Regole operative

- Usa questo file come istruzione persistente di progetto.
- Usa skill solo quando pertinente al task.
- Esegui discovery MCP prima di invocare tool esterni.
- Per comandi shell usa argomenti separati e non concatenare input non fidato.
- Non esporre write finché non esistono dry-run, approval e recovery.

## Percorso minimo

1. `doctor` / `health`.
2. Discovery app-side e MCP-side.
3. Read tool.
4. Export/preview.
5. Dry-run / prepare.
6. Write controllata.
7. Smoke transcript.
