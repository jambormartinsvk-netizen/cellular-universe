# P5.3g7 M1 order-7 provenance — technický attempt ledger

**historical_packages_total:** `4`  
**consecutive_technical_failures:** `0/10`  
**Fyzikálny stav:** `PASS_M1_ORDER7_PROVENANCE_NUMERICAL_BOUNDARY_CLOSED_SAME_MATRIX_ONLY`; K4 `LIVE / 60/100`

| Balík | Run | Stav | Vecný výsledok | Active counter |
|---:|---|---|---|---:|
| 1 | KMPC-036 | `AUTHORITATIVE SCOPED PASS+REVIEW` | regression/shape/rank/anchor/condition/holdout PASS; tri power-7 precision-floor driver REVIEW; doc65 | `0/10` (reset vecným výsledkom) |
| 2 | KMPC-037 | `TECHNICAL_FAILURE / PF-072` | mpmath non-pivoted Householder vyhlásil maticu za numericky singulárnu; bez výsledného payloadu | `1/10` |
| 3 | KMPC-038 | `SMOKE_TECHNICAL_FAILURE / PF-073` | overlay cielil modul `mpmath` namiesto runtime contextu `mpmath.mp`; full audit NOT_RUN | `2/10` |
| 4 | KMPC-039 | `AUTHORITATIVE PASS` | jediný refinement aj jediný 80-dps same-matrix QR uzavreli 121+18 bez lower/anchor regresie; doc74 | `0/10` (reset vecným výsledkom) |

Syntax/import/timeout/sandbox/serializácia/hash mismatch sú technické chyby.
Vecný interpretovateľný výsledok bez pádu resetuje counter na `0/10`;
compile/help/smoke ho neresetujú. Po 10 po sebe idúcich technických zlyhaniach
sa zastaví iba táto implementačná línia s presným dôvodom, nie fyzika K4.

## Externý R3 audit — technický dlh, nie nový pokus

Opakovaný externý audit R3 prešiel end-to-end; active counter zostáva
`0/10`. Dodatočná immutability sonda auditora odhalila stale `.tmp-…json`
po publish kolízii. Kanonický súbor ostal nedotknutý a guard bol fail-closed.
Nález sa preto eviduje ako `TECHNICAL_DEBT_TMP_CLEANUP_AND_FAIL_EARLY`, nie
ako fyzikálny neúspech ani ako ďalší implementačný pokus.

Budúci nový runner má bezpečne upratať iba vlastný temp súbor, urobiť
fail-early kontrolu cieľa a zapísať Python/NumPy/BLAS metadata. Runner 280
a jeho immutable výsledok sa retroaktívne nemenia.
