# P5.3g7 M1 order-7 provenance — technický attempt ledger

**historical_packages_total:** `1`  
**consecutive_technical_failures:** `0/10`  
**Fyzikálny stav:** `SCOPED PASS / POWER7 DRIVER PRECISION REVIEW`; K4 `LIVE / 60/100`

| Balík | Run | Stav | Vecný výsledok | Active counter |
|---:|---|---|---|---:|
| 1 | KMPC-036 | `AUTHORITATIVE SCOPED PASS+REVIEW` | regression/shape/rank/anchor/condition/holdout PASS; tri power-7 precision-floor driver REVIEW; doc65 | `0/10` (reset vecným výsledkom) |

Syntax/import/timeout/sandbox/serializácia/hash mismatch sú technické chyby.
Vecný interpretovateľný výsledok bez pádu resetuje counter na `0/10`;
compile/help/smoke ho neresetujú. Po 10 po sebe idúcich technických zlyhaniach
sa zastaví iba táto implementačná línia s presným dôvodom, nie fyzika K4.
