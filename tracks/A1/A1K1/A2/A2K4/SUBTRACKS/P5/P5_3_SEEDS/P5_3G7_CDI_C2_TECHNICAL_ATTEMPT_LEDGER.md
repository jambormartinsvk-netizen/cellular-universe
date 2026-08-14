# P5.3g7 GLOBAL-C1/CDI-support-step-2 — technický attempt ledger

**historical_packages_total:** `1`  
**consecutive_technical_failures:** `0/10`  
**Fyzikálny stav:** `SCOPED CORE+COMMON PASS / SUPPORT_03 REMAINDER REVIEW`; K4 `LIVE / 60/100`

| Balík | Run | Stav | Vecný výsledok | Active counter po balíku |
|---:|---|---|---|---:|
| 1 | KMPC-035 | `AUTHORITATIVE SCOPED PASS+REVIEW` | regression/core/common/S-C0 PASS; `[0,3]` tail FAIL; nie smrť CDI/K4; doc62 | `0/10` (reset vecným výsledkom) |

Syntax, import, timeout, sandbox, serializácia a hash mismatch sú technické
chyby. Vecný interpretovateľný výsledok bez technického pádu resetuje
active counter na `0/10`; compile/help/smoke ho neresetujú. Po `10`
po sebe idúcich technických zlyhaniach sa zastaví iba implementačná línia
s presným dôvodom, nie fyzika CDI alebo K4.
