# A2-K7.1a-K3.1 — výstup skriptu 58

**Dátum:** 2026-07-13  
**Grid:** `epsilon/delta={0.01,0.05,0.10,0.25,0.50,0.90}`  
**Normalizácia:** `ell=1`, `zeta=1.01 alpha^2`, `T=1`

| `eps/delta` | `alpha` | holé vlastné hodnoty | `zeta` | det doplnenej `L` | min. eig doplnenej `L` | stav |
|---:|---:|---|---:|---:|---:|---|
| 0.01 | `2.24423791e-4` | `±2.24423791e-4` | `5.08696983e-8` | `5.03660380e-10` | `5.03660354e-10` | bare FAIL, completed PASS |
| 0.05 | `1.122118955e-3` | `±1.122118955e-3` | `1.27174246e-6` | `1.25915095e-8` | `1.25914936e-8` | bare FAIL, completed PASS |
| 0.10 | `2.24423791e-3` | `±2.24423791e-3` | `5.08696983e-6` | `5.03660380e-8` | `5.03657843e-8` | bare FAIL, completed PASS |
| 0.25 | `5.610594775e-3` | `±5.610594775e-3` | `3.17935615e-5` | `3.14787737e-7` | `3.14777828e-7` | bare FAIL, completed PASS |
| 0.50 | `1.122118955e-2` | `±1.122118955e-2` | `1.27174246e-4` | `1.25915095e-6` | `1.25899242e-6` | bare FAIL, completed PASS |
| 0.90 | `2.019814119e-2` | `±2.019814119e-2` | `4.12044557e-4` | `4.07964908e-6` | `4.07798539e-6` | bare FAIL, completed PASS |

```text
bare_cross_only_operator_fails_every_grid_point = true
positive_onsager_completion_exists_every_grid_point = true
completion_requires_nonzero_diagonal_reaction = true
completion_requires_bulk_viscous_companion = true
local_KMS_completion_requires_noise = true
microphysical_coefficients_derived = false
bath_background_closed = false
```

`completed PASS` znamená iba pozitivitu normalizovanej matice, nie fyzikálny
prechod K7.1.

