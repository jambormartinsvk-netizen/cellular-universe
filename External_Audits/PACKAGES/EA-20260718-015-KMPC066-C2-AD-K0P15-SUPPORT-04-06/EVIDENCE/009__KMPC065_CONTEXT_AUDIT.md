# KMPC-064/065 — C2 AD/k=.15 nominal: výsledok a audit

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C2 → AD/k=.15/nominal`  
**Autoritatívny stav:** `REVIEW_C2_AD_K0p15_SUPPORT_04_06_REQUIRED`  
**Skóre:** bez zmeny, K4 `60/100`, P5 `3.5/6`

## Technická vetva

KMPC-064 compile/help prešiel, ale smoke odhalil PF-080: restricted
atomový názov bol aktívny počas parent 10-name fixture. Nevznikol raw ani
fyzika; runner 308 je `DO_NOT_RUN`. KMPC-065 oddelil matrix-wide smoke od
atom-local overlaya bez zmeny rovníc, supportu alebo prahov. Jeho
compile/help/smoke prešiel vrátane hash ownera a obnovy ownerov.

## Immutable výsledok

`scripts/results/k_mpc_005/RUN_KMPC_065_P5_3G7_C2_AD_K0p15_NOMINAL.json`  
SHA-256 `987E467EA2F36EA8F061F665A33AE1F6DC9AB6E2EFE9FB710E23CE0C50171636`.

M1 depth 5 mal rank `76/76`, driver `2.29081e-14` a holdout
`8.17635e-15`; prešiel. Core, S-C0, common a background prešli. Common
maximum bolo F0 `4.37116e-15`, M3 `1.07526e-13`; background maximum
`3.45586e-16`.

| Vetva | `z=1e-4` | `z=.01` | Prah | Stav |
|---|---:|---:|---:|---|
| F0 tail `3,4` | `9.36649e-6` | `9.45894e-4` | `1e-6` | FAIL |
| M3 tail `3,4` | `1.09234e-5` | `1.09425e-3` | `1e-6` | FAIL |

Najhoršie relatívne stavy boli `delta_f` pre F0 a `eta` pre M3. Tail
zlyhal už na `z=1e-4`, nie iba na väčšej ploche. Candidate support `[0,2]`
preto nie je adequate pre AD/k=.15. Je oprávnený iba nový atom-local krok
`[0,4]→[0,6]`, M1 depth 6, common `0…4`, tail `5,6`.

Nie je to STOP: lineárne rovnice, M1, core/common ani background nezlyhali.
Výsledok nepotvrdzuje ďalšie módy, varianty, C3, S-M, hierarchy, ODE ani
dáta. Release, Zenodo a prediction-table trigger: `NONE`.
