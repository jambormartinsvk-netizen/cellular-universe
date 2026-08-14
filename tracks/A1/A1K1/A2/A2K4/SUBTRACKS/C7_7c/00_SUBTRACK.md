# A2-K4 / C7.7c — index numerických formulácií

C7.7c overuje evolučnú aktivitu a úplnosť registrovaných species/módov.
K1 až K7 sú alternatívne numerické formulácie tej istej C7.7c brány, nie
fyzikálne koľaje A2 a nie povinné a/b/c etapy každej formulácie.

| Formulácia | Aktuálny stav | Stručný dôvod |
|---|---|---|
| K1 | STOP numerického dôkazu | 28 activity kontrol pod uniformným `atol` floorom |
| K2 | TIMEOUT_UNCLOSED | DOP853 bez výsledného JSON |
| K3 | STOP technickej formulácie | Radau timeout a zle podmienený numerický Jacobián |
| K4 | TIMEOUT_UNCLOSED | analytická obálka PASS, evolúcia timeout |
| K5 | STOP numerickej formulácie | prvý segment 0/1 a zmenený error budget |
| K6 | STOP numerickej formulácie | požadovaný `atol_i` pod float64 podlahou |
| K7 | REVIEW / aktívna | K7a/K7b PASS; K7c P3b krok PASS, celý G5 PARTIAL PASS/REVIEW; K7d nedosiahnutá |

Aktuálny udržiavaný plán a konečný register všetkých siedmich formulácií:
`tracks/A1/A1K1/A2/A2K4/00_WORK_PLAN.md`.

Podrobná lineage matica:
`Audit/A2_K4_C7_7C_K1_K7_LINEAGE_GATE_COVERAGE_AND_WEIGHT_AUDIT_2026-07-15.md`.

