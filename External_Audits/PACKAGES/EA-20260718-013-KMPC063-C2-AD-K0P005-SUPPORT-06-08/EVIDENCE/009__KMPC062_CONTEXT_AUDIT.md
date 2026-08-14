# KMPC-062 — C2 AD/k=.005 support `[0,4]→[0,6]`: výsledok a audit

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny stav:** `REVIEW_C2_AD_K0p005_SUPPORT_06_08_REQUIRED`  
**Skóre:** K4 `60/100`, P5 `3.5/6`; bez zmeny

Immutable raw:
`scripts/results/k_mpc_005/RUN_KMPC_062_P5_3G7_C2_AD_K0p005_SUPPORT_04_06.json`  
SHA-256 `640057CB6AC3F059988D6BD6C0CBE65ABAC1712F18961A2FEAFA5E1341EA6760`

| Brána | Výsledok |
|---|---:|
| M1 rank | `87/87`, PASS |
| M1 driver / holdout | `5.34531e-14 / 1.05223e-13`, PASS |
| candidate `[0,4]`, audit `[0,6]`, S-C0 | PASS |
| common F0 / M3 | `7.52810e-15 / 2.64950e-12`, PASS |
| background worst relative | `1.15195e-16`, PASS |
| F0 tail `5,6`, `z=1e-4 / 1e-2` | `7.86847e-12` PASS / `8.21011e-6` FAIL |
| M3 tail `5,6`, `z=1e-4 / 1e-2` | `1.48998e-11` PASS / `1.56680e-5` FAIL |

Support rozšírenie znížilo tail z percentovej úrovne na `10^-5` pri
`z=.01` a na `10^-11` pri `z=1e-4`, no frozen prah `1e-6` stále neprešlo.
Najhoršie stavy zostávajú `delta_f` (F0) a `eta` (M3). Ide o systematickú
konvergenciu, nie o background leak alebo roundoff.

Ďalší minimálny predregistrovaný krok je candidate `[0,6]` voči auditu
`[0,8]` s M1 depth 8. Ak M1 raw narazí iba na numerical boundary, nesmie sa
automaticky korigovať; dostane vlastný same-matrix audit. `[0,10]` sa zatiaľ
nespúšťa. Zvyšných deväť C2 atómov ostáva NOT_RUN.
