# Benchmark Plan

## Obiettivo

Confrontare API diretta, MCP, CLI e CLI + cache/mirror sullo stesso task.

| Scenario | Host | Dataset | Task | Metriche | Note |
|---|---|---|---|---|---|
| API diretta |  |  |  | latenza, token, accuracy, retry |  |
| MCP |  |  |  | latenza, token, tool calls, failure |  |
| CLI |  |  |  | wall-clock, exit code, output size |  |
| CLI + mirror |  |  |  | p50/p95, freshness, privacy |  |

## Regole

- Stesso task e stesso dataset.
- Almeno 10 run per MVP, 30 per report serio.
- Separare cold start e warm run.
- Misurare p50/p95, non solo media.
- Non usare claim assoluti senza benchmark riproducibile.
