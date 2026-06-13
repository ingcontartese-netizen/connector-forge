# Cowork Plugin Brief

Cowork va trattato come superficie distinta da Claude Code e Claude Desktop locale.

## Pattern consigliato

| Caso | Pattern |
|---|---|
| SaaS/cloud | Remote MCP connector diretto |
| Desktop app con API locale | Plugin + remote MCP broker + site bridge locale |
| Desktop app con SDK profondo | Adapter nativo + bridge + MCP task-level |
| App senza API sufficiente | Computer use solo come fallback |

## Regole

- Non assumere che Cowork possa usare direttamente un server MCP locale.
- Se l'app vive sul desktop, prevedi site bridge locale e broker remoto.
- Usa computer use solo per setup, QA visiva o gap residui.
- Le write devono avere approval server-side o processo umano esterno.
