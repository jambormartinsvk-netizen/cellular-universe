# KMPC-048 — GLOBAL_C1 NID support step 2: výsledok a audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID_SUPPORT_STEP_2`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny rozsudok:** `REVIEW_NID_SUPPORT_STEP_2_ORDER7_CORE_BOUNDARY`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; skóre bez zmeny

## Dôkaz

| Artefakt | SHA-256 |
|---|---|
| base `nid_support_step2.py` | `7AFA5AD9022FA3EB8BDFB5F77D573939D60B2312A0FA29493D6505695958EE5B` |
| runner 292 | `9FA55116BB7CFD911CCB2D8D741280C3A5AF99C9741BA2FC5AA61A5DC2068002` |
| raw JSON | `B4F320F5D850DCF78FD9EC2A5BDDEBDA87D590DA2988CF505FA7D5B25B49BF32` |

Canonical JSON:
`scripts/results/k_mpc_005/RUN_KMPC_048_P5_3G7_NID_SUPPORT_STEP_2_05_07.json`.
Jediný official audit skončil exitom `0`, internal `3.531 s`. Failure ani
temp artefakt nevznikol.

## Výsledky brán

| Brána | Výsledok | Údaj |
|---|---|---|
| immutable KMPC-047 regresia | PASS | `[0,3]` aj `[0,5]`, F0/M3 |
| support/count/registry restore | PASS | `[0,3]/[0,5]/[0,7]`, `8/12/16` a `52/78/104` |
| R-A/B1/TCA0/M1 | PASS | bez contract driftu |
| combined `R_fs` | PASS | bez zmeny NID kompenzácie |
| S-C0 actual coefficient `05↔07` | PASS | lower moments |
| common F0 `0…5` | PASS | worst relative `1.80e-15 < 1e-8` |
| common M3 `0…5` | PASS | worst relative `9.35e-11 < 1e-8` |
| tail F0 `6,7`, `z=.01` | PASS | `3.45e-8 < 1e-6`, `U_f` |
| tail M3 `6,7`, `z=.01` | PASS | `1.63e-7 < 1e-6`, `h` |
| support `[0,7]` rank | PASS | `104/104`, equilibrated ratio `0.276` |
| support `[0,7]` M3 driver | **FAIL** | worst relative `1.26305e-10`, `fuel_continuity[7]`, limit `1e-10` |
| support `[0,7]` holdout | **FAIL** | worst relative `0.229987`, `Einstein_00[7]`; abs-fallback max `2.77e-15` |

Support `[0,3]` a `[0,5]` core prešli. Jediné core zlyhanie je order-7 M3
blok. Tail samotný je už pod prahom, takže výsledok nie je dôkaz potreby
`[0,9]`. Zároveň nemožno udeliť adequacy PASS, kým sa nevysvetlí driver a
nezávislý holdout na ráde 7.

## Interpretácia a ďalší krok

Veľký relatívny holdout pri absolútnom zvyšku rádovo `1e-15` môže byť
normalizačná/precision hranica, ale to sa nesmie predpokladať. Nasleduje
samostatný no-new-physics NID order-7 provenance audit:

1. presná identita row/column a scaling vetvy;
2. raw a equilibrated rank/condition;
3. rezíduá všetkých driver[7] a holdout[7] riadkov v absolútnej aj
   relatívnej vetve;
4. coefficient perturbation/backward-error diagnostika;
5. rozhodnutie, či je povolený same-matrix high-precision boundary audit.

Žiadna zmena rovníc, supportu, plôch alebo prahov. `[0,9]` a NIV sa zatiaľ
nespúšťajú.

## Nonclaims a triggery

Bez uzavretia NID order-7 core, support adequacy, NIV, iných `k`/variantov,
S-M, full hierarchy, ODE/P5.4, G8/G9, CLASS/CMB/BBN/S8/H0.
`SCORE_EFFECT=NONE`, `RELEASE_TRIGGER=NONE`, `PREDICTION_TABLE_EFFECT=NONE`,
`ZENODO_TRIGGER=NONE`.

