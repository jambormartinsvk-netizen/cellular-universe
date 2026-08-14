# KMPC-039 — M1 order-7 numerical boundary closure: výsledok a audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / M1_ORDER7`  
**Autoritatívny rozsudok:**
`PASS_M1_ORDER7_PROVENANCE_NUMERICAL_BOUNDARY_CLOSED_SAME_MATRIX_ONLY`  
**K4:** `LIVE / 60/100`; skóre bez zmeny  
**Dôsledok:** CDI support step 3 je `UNBLOCKED_FOR_SEPARATE_PREREGISTRATION`,
nie vykonaný ani prejdený

## Dôkazový artefakt

Canonical JSON:
`scripts/results/k_mpc_005/RUN_KMPC_039_P5_3G7_M1_ORDER7_CONTEXT_OWNER.json`  
SHA-256:
`BDF3317235FEDEA23EDF8C23563423014F2E98A461C6E638C474DF94471CE016`.

Identita ostala `CDI / k=0.05 Mpc^-1 / nominal / order=7`, full matica
`121×99`, reduced `121×98`, rank `98/98`, hard anchor `h[1]`.

## Rozhodujúce výsledky

| Brána | Výsledok | Dôkaz |
|---|---|---|
| V0 immutable regresia | PASS | presne reprodukovala pôvodné tri KMPC-036 otvorené riadky |
| V1 residual invariants | PASS | driver/initial aj holdout invariants |
| V2 jediný float64 refinement | PASS | `max|delta_x|=2.11114386969413e-15 < 1e-14` |
| V2 driver/initial | PASS | `121/121`, žiadny otvorený riadok |
| V2 holdout/lower/anchor | PASS | `18/18`, lower `-1..5` a exact anchor zachované |
| V3 jediný 80-dps same-matrix QR | PASS | `121/121` driver/initial a `18/18` holdout |
| V3 rozdiel od KMPC-036 stavu | PASS | `2.108084046016267...e-15 < 1e-14` |
| V3 spätná float64 projekcia | PASS | `121/121` a `18/18`, lower regresia PASS |

Najhoršia V2 driver metrika bola `1.42737e-16`, najhoršia V3 high-precision
metrika `4.51395e-17` a najhoršia spätná float64 projekcia `1.23866e-16`;
všetky sú hlboko pod nezmeneným relatívnym prahom `1e-10`.

## Interpretácia

Tri historické KMPC-036 power-7 odchýlky boli platné výsledky pôvodného
jednoprechodového float64 solve. KMPC-039 však na tej istej už zostavenej
float64 matici, bez zmeny rovníc či prahov, ukázal, že:

1. jediná korekcia veľkosti približne `2.1e-15` ich všetky uzavrie;
2. nezávislý 80-dps Householder QR dá rovnaký záver;
3. lower koeficienty, anchor a nezávislé Einsteinove holdouty sa nerozpadnú.

Preto nejde o invariantný rozpor order-7 recurrence ani o dôvod pre native
high-precision rebuild. V rozsahu provenance je príčina uzavretá ako
float64 solver/rounding floor.

## Technická história bez prepisovania

Podrobná predregistrácia a execution história všetkých troch pokusov je
zlúčená v dokumente 68.

- KMPC-037/PF-072: mpmath QR zlyhal na zero-diagonal Householder tie;
- KMPC-038/PF-073: prvý overlay cielil exportný modul namiesto `mpmath.mp`;
- KMPC-039: owner guard, zero-diagonal fixture, callable restore a nonzero
  parity prešli; jediná formulačná zmena bola štandardná orientácia `+1` pri
  `sign(0)`.

KMPC-037 a KMPC-038 failure JSON ostávajú immutable. Nie sú fyzikálnymi
REVIEW/STOP udalosťami.

## Ďalší predregistrovaný krok

Samostatne predregistrovať `GLOBAL_C1 / CDI_SUPPORT_STEP_3` podľa dokumentu
62: immutable regresia `[0,3]` a `[0,5]`, candidate `[0,5]`, audit `[0,7]`,
F0 počty `12/16`, M3 `78/104`, common bridge `0..5` a tail obálka iba powers
`6,7` voči baseline `1..5` na pôvodných plochách a prahoch.

KMPC-039 tento krok nespustil. Ak step 3 zlyhá, `[0,9]` nevznikne automaticky;
nasleduje audit rastu koeficientov/pomeru/polomeru konvergencie.

## Nonclaims a triggery

Bez CDI step-3 výsledku, BI/NID/NIV, iných `k`/variantov, S-M, full hierarchy,
ODE, G8/G9, CLASS/CMB/BBN/S8/H0 a bez zmeny teórie.
`SCORE_EFFECT=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`RELEASE_TRIGGER=NONE`, `ZENODO_TRIGGER=NONE`.
