# KMPC-047 — GLOBAL_C1 NID primary/extended: výsledok a audit

**Dátum:** 2026-07-18  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → GLOBAL_C1 / NID`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny rozsudok:** `REVIEW_NID_C1_SUPPORT_EXTENSION_REQUIRED`  
**K4:** `LIVE / 60/100`; **P5:** `3.5/6`; skóre bez zmeny

## Dôkaz

| Artefakt | SHA-256 |
|---|---|
| base `nid_c1_coverage.py` | `EEEE74848B6F4413914F0CC60230CC824982C7E485A38C77C4495F807975A2CD` |
| runner 291 | `EF217D9AD729CFA0B112018B5D4C385E983564F185A1543F3BC245F812FEAF95` |
| raw JSON | `EED63396DB99C0818306C581413572BE647630CFD0433A8F05A1DCE704DC696A` |

Canonical JSON:
`scripts/results/k_mpc_005/RUN_KMPC_047_P5_3G7_NID_C1_PRIMARY_EXTENDED_COVERAGE.json`.
Jediný official audit skončil exitom `0`, internal runtime `1.485 s`.
Failure ani temp artefakt nevznikol.

## Rozhodujúce brány

| Brána | Výsledok | Najdôležitejší údaj |
|---|---|---|
| support/count | PASS | `[0,3]→[0,5]`, F0 `8→12`, M3 `52→78` |
| R-A/B1/TCA0/M1/core | PASS | žiadny false core check |
| combined `R_fs` NID kompenzácia | PASS | density residual `4.44e-16`, velocity residual `1.11e-16` |
| actual S-C0 coefficient guard | PASS | primary aj extended lower moments |
| common F0 powers `0…3` | PASS | worst relative `5.42e-16 < 1e-8` |
| common M3 powers `0…3` | PASS | worst relative `5.61e-12 < 1e-8` |
| tail F0 powers `4,5`, `z=1e-4` | PASS | worst relative `0` |
| tail M3 powers `4,5`, `z=1e-4` | PASS | worst relative `6.81e-10 < 1e-6` |
| tail F0 powers `4,5`, `z=.01` | **FAIL** | `1.86927e-2`, `U_f` |
| tail M3 powers `4,5`, `z=.01` | **FAIL** | `4.39219e-2`, `U_f` |

NID primary a extended solve teda zdieľajú stabilné common koeficienty a
všetky invariantné/core kontroly prešli. Zlyhanie pochádza iba z veľkosti
nového tailu na plytšej zmrazenej ploche. Je približne `1.87e4` až `4.39e4`
krát nad prahom, takže `[0,3]` nemožno označiť za dostatočný support.

## Interpretácia

Výsledok neukazuje chybu combined-`R_fs` kompenzácie ani rozpad rovníc.
Ukazuje, že NID má na `z=.01` významné subleading členy `j=4,5`; primary
support `[0,3]` je príliš krátky pre požadovanú presnosť. Toto je
`REVIEW_SUPPORT_EXTENSION_REQUIRED`, nie fyzikálny STOP A2-K4.

## Ďalší krok

Samostatne predregistrovať NID support step 2:

```text
immutable regresia: [0,3] a [0,5] voči KMPC-047
candidate:           [0,5]
audit:               [0,7]
common:              0…5
new tail:            6,7
```

Prahy, plochy, rovnice, combined-`R_fs`, core a S-C0 guard ostávajú bez
zmeny. `[0,9]` sa nespustí automaticky. NIV zostáva blokovaný, kým sa NID
fail-fast vetva nerozhodne.

## Nonclaims a triggery

Bez NID support `[0,5]` adequacy, NIV, iných `k`/variantov, S-M, full
hierarchy, ODE/P5.4, G8/G9, CLASS/CMB/BBN/S8/H0 a bez potvrdenia celej
teórie. `SCORE_EFFECT=NONE`, `RELEASE_TRIGGER=NONE`,
`PREDICTION_TABLE_EFFECT=NONE`, `ZENODO_TRIGGER=NONE`.

