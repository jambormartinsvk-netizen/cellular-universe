# KMPC-054 — GLOBAL_C1 NIV primary/extended: výsledok a autoritatívny audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NIV`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny stav:** `REVIEW_NIV_C1_SUPPORT_EXTENSION_REQUIRED`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; triggery `NONE`

## Výsledok

KMPC-054 technicky a numericky platne porovnal samostatný NIV primary
support `[-1,2]` s extended supportom `[-1,4]` pri `k=0.05 Mpc^-1`,
nominal variante. Skriptový kandidát je
`REVIEW_NIV_C1_SUPPORT_EXTENSION_REQUIRED`; autoritatívny audit ho prijíma
v presne tomto scope.

| Brána | Výsledok |
|---|---:|
| M1 order-5 | PASS, rank `76/76`, driver `2.8033e-15`, holdout `3.0986e-15` |
| NIV combined-`R_fs` | PASS, velocity residual `4.4409e-16` |
| primary M3 `[-1,2]` | PASS, rank `52/52`, holdout max relative `2.7183e-14` |
| extended M3 `[-1,4]` | PASS, rank `78/78`, holdout max relative `7.5323e-13` |
| F0 common `-1…2` | PASS, max relative `9.5870e-15` |
| M3 common `-1…2` | PASS, max relative `6.3935e-11 < 1e-8` |
| čistý tail `3,4` | **FAIL** |

Cancellation-safe tail výsledky:

| Rodina | `z=1e-4` | `z=1e-2` |
|---|---:|---:|
| F0 | `4.00308e-4`, `U_f`, FAIL | `8.23797e-2`, `delta_f`, FAIL |
| M3 | `6.51243e-4`, `delta_c`, FAIL | `5.62676e-2`, `U_f`, FAIL |

Prahová hodnota bola pred behom zmrazená na `1e-6`. Zlyhania sú o stovky
až desaťtisíce násobkov nad prahom, preto ich nemožno vysvetliť iba
float64 roundingom. Zároveň všetky rank, driver, holdout, forbidden-layer,
production, S-C0 a common-coefficient brány prešli. Dôkaz preto ukazuje na
nedostatočný truncation support, nie na rozpad rovníc ani fyzikálny STOP.

## Autoritatívne rozhodnutie

`[-1,2]` nie je pre NIV pri tomto bode preukázaný ako postačujúci support.
NIV zostáva `REVIEW` a jeho ďalší predregistrovaný krok je support step 2:

```text
[-1,4] primary → [-1,6] extended,
common -1…4, čistý tail 5,6,
M1 depth 6, pretože extended high=6.
```

M1 depth sa rozšíri súčasne so supportom, aby sa nezopakovala NID chyba,
pri ktorej bol vyšší M3 support napájaný plytším M1 stavom. Prahy, plochy,
rovnice a parameter `k` sa nemenia. Ak step 2 zlyhá v core alebo common
koeficientoch, najprv sa vykoná provenance/numerical audit; ak zlyhá iba
tail, ďalší support vyžaduje novú predregistráciu.

## Proveniencia

- base SHA-256:
  `B222554E8F6E664DAC674E394FED02A02ECBEE432ADEDC9A9682DFA6BB746E9D`;
- runner SHA-256:
  `75CDF108C4FA11A97E10F555FD47B0B5005551EC4513438A4B5C223985A0C66B`;
- raw JSON:
  `scripts/results/k_mpc_005/RUN_KMPC_054_P5_3G7_NIV_C1_PRIMARY_EXTENDED_COVERAGE.json`;
- raw SHA-256:
  `0CF322A7BA5964B78BBF9180B29FA8BBBE43A646ECEB05D444B6250568ECFB1E`.

## Nonclaims

Výsledok neuzatvára NIV support adequacy, iné `k`/varianty, S-M, full
hierarchy, finite opacity, ODE/P5.4 ani kanonickú G8/G9 bránu. Nemení skóre,
predikčnú tabuľku, release ani Zenodo stav. NID koeficienty, korekcia a
support verdict neboli prenesené.

