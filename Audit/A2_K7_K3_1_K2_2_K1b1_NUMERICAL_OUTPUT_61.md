# A2-K7.1a-K3.1-K2.2-K1b1 — numerický výstup opraveného skriptu 61

**Dátum behu:** 2026-07-13  
**Exit code:** `1` — očakávaný kill výstup  
**Verdikt:** `DEAD_M014d2a_ENHANCED_LEADING_SOFT_SPIN2_COUPLING`  
**Max. hĺbka:** `41/100`

| eps/delta | `M_eff,max` rec [eV] | `M_eff,max` dnes [eV] | min. zosilnenie coupling | min. `G_eff/G_N` | diagnostické `g_nonspin2` rec | dnes | Stav | Max. hĺbka |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 0.01 | 3.743e6 | 1917.77 | 1.270e24 | 1.612e48 | 2.273e-8 | 4.067e-8 | FAIL | `41/100` |
| 0.05 | 2.508e6 | 1909.72 | 1.275e24 | 1.626e48 | 3.392e-8 | 4.084e-8 | FAIL | `41/100` |
| 0.10 | 2.109e6 | 1899.89 | 1.282e24 | 1.643e48 | 4.033e-8 | 4.105e-8 | FAIL | `41/100` |
| 0.25 | 1.678e6 | 1871.86 | 1.301e24 | 1.692e48 | 5.071e-8 | 4.166e-8 | FAIL | `41/100` |
| 0.50 | 1.411e6 | 1829.35 | 1.331e24 | 1.772e48 | 6.030e-8 | 4.263e-8 | FAIL | `41/100` |
| 0.90 | 1.218e6 | 1770.23 | 1.376e24 | 1.892e48 | 6.984e-8 | 4.405e-8 | FAIL | `41/100` |

```text
leading_hmunu_Tmunu_coupling_only = true
higher_derivative_curvature_operators_excluded_by_this_test = false
universal_leading_scale_compatible_with_measured_Mpl = false
species_dependent_leading_massless_spin2_coupling_allowed_by_soft_theorem = false
```

Pôvodný preširoký beh je zachovaný v
`scripts/61_script_A2_K7_K3_1_K2_2_K1b_spin2_coupling_scale_gate_PRE_ERRATUM_OVERBROAD.py`.

