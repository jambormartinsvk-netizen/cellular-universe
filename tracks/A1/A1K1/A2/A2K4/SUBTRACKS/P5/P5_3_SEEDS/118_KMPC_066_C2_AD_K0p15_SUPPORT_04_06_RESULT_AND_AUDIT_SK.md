# KMPC-066 — C2 AD/k=.15 support `[0,4]→[0,6]`: výsledok a audit

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny stav:** `PASS_C2_AD_K0p15_SUPPORT_04_ADEQUATE_CANDIDATE_ONLY`  
**Coverage:** C2 `2/10 PASS`; skóre K4 `60/100`, P5 `3.5/6` bez zmeny

Immutable raw `scripts/results/k_mpc_005/RUN_KMPC_066_P5_3G7_C2_AD_K0p15_SUPPORT_04_06.json`,
SHA-256 `81370874BCF25123565FBB117EDFEB4D51F12560CCC04BDC8CCDFC0DF8FDE816`.

M1 depth 6 prešiel s rankom `87/87`, driverom `3.32013e-14` a holdoutom
`1.30109e-14`. Core, S-C0, common a background prešli; common F0
`1.07275e-14`, M3 `1.88594e-12`, background `3.45586e-16`.

| Vetva | `z=1e-4` | `z=.01` | Prah | Stav |
|---|---:|---:|---:|---|
| F0 tail `5,6` | `9.11385e-15` | `9.14145e-9` | `1e-6` | PASS |
| M3 tail `5,6` | `1.51510e-14` | `1.51953e-8` | `1e-6` | PASS |

Najhoršie stavy na `.01` boli `delta_f` a `sigma_fs`. Candidate `[0,4]`
je adequate iba pre AD/k=.15/nominal. Spolu s KMPC-063 sú oba AD k-body
uzavreté. Ďalší frozen C2 atóm je CDI/k=.005/nominal s jeho uzavretým C1
supportom `[0,5]→[0,7]`, M1 depth 7; bez prenosu korekcie.

Nie je to plný P5/K4 verdikt. Osem C2 atómov, C3, S-M, hierarchy, ODE a
dáta ostávajú otvorené. Trigger release/Zenodo/prediction: `NONE`.
