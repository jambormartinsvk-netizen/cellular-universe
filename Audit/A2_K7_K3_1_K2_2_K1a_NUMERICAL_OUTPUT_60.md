# A2-K7.1a-K3.1-K2.2-K1a — numerický výstup skriptu 60

**Dátum behu:** 2026-07-13  
**Príkaz:** `python scripts/60_script_A2_K7_K3_1_K2_2_K1a_registered_steam_gravity_rate.py`  
**Exit code:** `1` — očakávaný kill výstup  
**Verdikt:** `DEAD_M014d1_REGISTERED_GRAVITON_STEAM_TOO_WEAK`  
**Max. hĺbka:** `40/100`

## Vstupy

```text
T_steam,0 = 0.905 K
Delta N_eff = 0.0535
Mbar_Pl = 2.435e27 eV
optimistic gravity prefactor = 1
H0 = 1.4157515302794188e-33 eV
z_start = 1089.9
```

## Výstup gridu

| eps/delta | `Q1/(H rhoF)` rec | `Q1/(H rhoF)` dnes | `Gamma_g/H` rec | `Gamma_g/H` dnes | najlepší `Gamma_g/(Q1/rhoF)` | min. deficit [rády] | Stav | Max. hĺbka |
|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 0.01 | 6.796e-4 | 0.150639 | 3.795e-87 | 5.796e-98 | 5.584e-84 | 83.253 | FAIL | `40/100` |
| 0.05 | 3.373e-3 | 0.153194 | 3.795e-87 | 5.796e-98 | 1.125e-84 | 83.949 | FAIL | `40/100` |
| 0.10 | 6.739e-3 | 0.156388 | 3.795e-87 | 5.796e-98 | 5.632e-85 | 84.249 | FAIL | `40/100` |
| 0.25 | 1.684e-2 | 0.165970 | 3.795e-87 | 5.796e-98 | 2.254e-85 | 84.647 | FAIL | `40/100` |
| 0.50 | 3.367e-2 | 0.181941 | 3.795e-87 | 5.796e-98 | 1.127e-85 | 84.948 | FAIL | `40/100` |
| 0.90 | 6.060e-2 | 0.207493 | 3.795e-87 | 5.796e-98 | 6.263e-86 | 85.203 | FAIL | `40/100` |

## Kontroly

```text
steam_background_already_registered = true
steam_prediction_is_conditional_in_register_Q18_Q23 = true
microscopic_oscillation_scale_faster_than_H = true
gravity_only_rate_can_supply_K7_Q1 = false
```

Skript zámerne vracia nenulový exit pri smrti koľaje. Nejde o runtime
chybu. Plnú presnosť a všetky konštanty zachováva skript; jeho SHA-256 je v
dôkazovom manifeste.

