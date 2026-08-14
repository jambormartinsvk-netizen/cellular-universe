# A2-K7.1a — numerický výstup skriptov 55 a 56

**Dátum:** 2026-07-13  
**Background:** validovaný A1-K1, `z*=1089.92`, `lambda=0.15`,
`delta=0.02297`  
**Grid:** `epsilon/delta={0.01,0.05,0.10,0.25,0.50,0.90}`

## Skript 55 — konštantné on-shell šírky

```text
E(recombination)=23594.351067
constant Gamma_chi reproduces Q2 = true
constant Gamma_phi reproduces Q1 = false for every grid point
verdict = A2-K7.1a-K1 MŔTVA M-014a
```

| `eps/delta` | `epsilon` | `Gamma_chi/H0` | `Gamma_chi/H(rec)` | `Gamma_phi/H0 rec` | `Gamma_phi/H0 dnes` | max/min |
|---:|---:|---:|---:|---:|---:|---:|
| 0.01 | 0.00022970 | 653.025686 | `2.767720e-2` | 16.039051 | 0.150673 | 106.449102 |
| 0.05 | 0.00114850 | 130.605137 | `5.535441e-3` | 79.668332 | 0.153370 | 519.451094 |
| 0.10 | 0.00229700 | 65.302569 | `2.767720e-3` | 159.369739 | 0.156748 | 1016.724431 |
| 0.25 | 0.00574250 | 26.121027 | `1.107088e-3` | 399.578748 | 0.166929 | 2393.704810 |
| 0.50 | 0.01148500 | 13.060514 | `5.535441e-4` | 803.648234 | 0.184055 | 4366.355720 |
| 0.90 | 0.02067300 | 7.255841 | `3.075245e-4` | 1460.015910 | 0.211874 | 6890.978193 |

Nenulový exit code `1` je zámerný strojový rozsudok mŕtvej podkoľaje, nie
pád programu.

## Skript 56 — rekonštrukcia `Upsilon(phi)`

| `eps/delta` | `Delta varphi` | `Upsilon/H0 rec` | `Upsilon/H0 dnes` | `Upsilon/H rec` | `Upsilon/H dnes` | ledger residual |
|---:|---:|---:|---:|---:|---:|---:|
| 0.01 | 0.209281 | 705.151941 | 6.624311 | 0.029886 | 6.624311 | `2.776e-17` |
| 0.05 | 0.205010 | 3646.716927 | 7.020328 | 0.154559 | 7.020328 | `2.776e-17` |
| 0.10 | 0.199542 | 7691.368782 | 7.564851 | 0.325983 | 7.564851 | `2.776e-17` |
| 0.25 | 0.182156 | 23061.045832 | 9.634039 | 0.977397 | 9.634039 | `4.163e-17` |
| 0.50 | 0.148730 | 69170.076983 | 15.841604 | 2.931637 | 15.841604 | `5.551e-17` |
| 0.90 | 0.066514 | 622478.450789 | 90.332379 | 26.382521 | 90.332379 | `5.551e-17` |

```text
positive single-valued reconstruction = true
microphysical derivation = not passed
memory kernel = not derived
noise correlator = not derived
K7.1a-K2 = survives reconstruction only
```

