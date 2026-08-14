# A2-K11 — numerický výstup skriptu 54

**Dátum:** 2026-07-13  
**Testovaný skript 45 SHA-256:**
`973905D79CBECBFD2DE55F13D3D3713D66C18B068BA74C7CAB566001A7312AEB`  
**Verdikt 54:** `FAIL_CLAIMS`

## Reprodukované behy

| Beh | Transfer | max. abs. rezíduum | max. bodové relatívne rezíduum na aktívnych bodoch |
|---|---:|---:|---:|
| amplitúda `1`, krok `1.25e-4` | `1.9928160639550857e-13` | `8.254964047496885e-10` | `1.0` |
| amplitúda `1`, krok `6.25e-5` | `1.9928603330433126e-13` | `8.255147706140903e-10` | `1.0` |
| amplitúda `1e12`, krok `6.25e-5` | `1.9928521556302077e-13` | `825.5147706084562` | `1.0` |

```text
step_log_transfer_relative_difference = 7.596109900001958e-7
amplitude_log_transfer_relative_difference = 1.4031451722414333e-7

step_converged_without_damping_bypass = true
amplitude_scaling_1e12 = true
pointwise_constraint_active = false
scaled_pointwise_constraint_active = false
verdict = FAIL_CLAIMS
```

## Bod maxima pri jednotkovej amplitúde

```text
index = 10
x = -6.994133327444566
a = 0.0009172474016952193
max_abs_state_at_point = 3.797893872691155e-5
terms = [
  3.31533651864446e-26,
  8.247609732449503e-10,
  7.537973691400696e-13
]
term_norm = 8.255147706140903e-10
absolute_residual = 8.255147706140903e-10
pointwise_relative_residual = 1.0
```

## Rovnaký bod pri amplitúde `1e12`

```text
terms = [
  3.315336518618644e-14,
  824.760973239322,
  0.7537973691341978
]
term_norm = 825.5147706084562
absolute_residual = 825.5147706084562
pointwise_relative_residual = 1.0
```

Absolútne rezíduum nie je numerická podlaha; škáluje sa lineárne s
amplitúdou. Kroková a amplitúdová numerika prešli, constraint nie.

