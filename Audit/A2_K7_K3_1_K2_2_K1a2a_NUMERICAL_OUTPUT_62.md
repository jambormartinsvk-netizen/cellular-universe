# A2-K7.1a-K3.1-K2.2-K1a2a — numerický výstup skriptu 62

**Dátum behu:** 2026-07-13  
**Exit code:** `1` — očakávaný kill výstup  
**Verdikt:** `DEAD_M014d1b_INCOHERENT_KMS_GRAVITON_TRANSITION`  
**Max. hĺbka:** `42/100`

| eps/delta | `Gamma_KMS,max/H` rec | dnes | potrebné zosilnenie rec | dnes | `omega_req` rec [MeV] | dnes [MeV] | `omega/T` rec | dnes | Stav | Max. hĺbka |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 0.01 | 3.109e-30 | 5.650e-35 | 2.186e26 | 2.666e33 | 51.249 | 10.814 | 6.024e8 | 1.387e11 | FAIL | `42/100` |
| 0.05 | 3.109e-30 | 5.650e-35 | 1.085e27 | 2.711e33 | 87.416 | 10.874 | 1.028e9 | 1.394e11 | FAIL | `42/100` |
| 0.10 | 3.109e-30 | 5.650e-35 | 2.168e27 | 2.768e33 | 110.103 | 10.950 | 1.294e9 | 1.404e11 | FAIL | `42/100` |
| 0.25 | 3.109e-30 | 5.650e-35 | 5.416e27 | 2.937e33 | 149.404 | 11.169 | 1.756e9 | 1.432e11 | FAIL | `42/100` |
| 0.50 | 3.109e-30 | 5.650e-35 | 1.083e28 | 3.220e33 | 188.225 | 11.516 | 2.212e9 | 1.477e11 | FAIL | `42/100` |
| 0.90 | 3.109e-30 | 5.650e-35 | 1.949e28 | 3.672e33 | 228.958 | 12.032 | 2.691e9 | 1.543e11 | FAIL | `42/100` |

```text
optimistic_incoherent_rate_meets_K7_with_omega_le_T = false
required_high_frequency_transition_has_unsuppressed_reverse_absorption = false
collective_coherent_channel_tested = false
fuel_mediator_transition_spectrum_derived = false
```

Skript zámerne vracia exit 1 pri smrti listovej podkoľaje. Pôvodné
thermal-scattering čísla skriptov 60/61 zostávajú oddelené.

