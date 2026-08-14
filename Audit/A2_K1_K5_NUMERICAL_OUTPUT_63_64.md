# A2-K1 až A2-K5 — zmrazený číselný výstup retrospektívy 63–64

**Dátum:** 2026-07-13  
**Príkazy:**

```powershell
python scripts\63_script_A2_K1_K5_retrospective_depth_equation_verdict_audit.py
python scripts\64_script_A2_K4_retrospective_adiabatic_convergence.py
```

## Súhrn skriptu 63

| Koľaj | Rozhodujúca hodnota | Parita | Max. hĺbka |
|---|---:|---|---:|
| K1 | `exp(12.2131073973)=201411.9108` | rovnice/výpočet PASS | `45/100` |
| K2 | `c_s^2=-0.97703`; `mu/H0=29.6329` pri `0.01 h/Mpc` | PASS | `25/100` |
| K3 | `exp(6.1065536987)=448.7893835` | rovnice/výpočet PASS | `45/100` |
| K4 | `T_abs=1.5873085`, `T/T0=108028.1391` | výpočet PASS, starý rozsudok FAIL | `50/100` |
| K5 | `Delta A_s/A_s=23.0255--26.4477 %` | PASS | `75/100` |

## K4 izokurvatúrny rozklad

```text
absolute transfer                 1.587308465541289
absolute log transfer             0.4620397928781821
null absolute transfer            1.4693472258019427e-5
ratio to decaying null            108028.1391401522
log ratio to decaying null        11.590147019763728
absolute transfer > e             FALSE
ratio to null > e                 TRUE
```

## K4 adiabatický beh skriptu 64

| Kontrola | Výsledok | Prah | Stav |
|---|---:|---:|---|
| všetky behy konečné | `TRUE` | `TRUE` | PASS |
| počiatočné `00` rezíduum | `1.73472e-18` | `<1e-10` | PASS |
| globálne relatívne `00` rezíduum | `5.42109e-12` | `<1e-5` | PASS |
| krokový rozdiel | `2.24352e-7` | `<1e-6` | PASS |
| `k -> k/2` rozdiel | `1.13550e-6` | `<1e-6` | **FAIL tesne** |
| max. relatívny mód / počiatočná spoločná rýchlosť | `1.43903e-6` | `<e` | PASS fyzikálnej neexplózie |

Strojový verdikt skriptu 64 je `REQUIRES_NUMERICAL_REVIEW`, nie `PASS`.
Fyzikálny dôsledok je užší: tento adiabatický mód neexplodoval, ale test
ešte nie je úplnou konvergentnou bázou všetkých módov.

## Reprodukcia starších rozhodujúcich skriptov

V tomto audite boli bez zmeny súborov opätovne spustené skripty
`21,23--27,30--33,35--37,41,42,44--46`. Všetky reprodukovali uložené
rozhodujúce hodnoty. Skript 45 použil Python 3.11.3, CAMB 1.6.6 a lokálny
adresár `.deps/python`.

