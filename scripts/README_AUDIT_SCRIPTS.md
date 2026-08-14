# Auditné a validačné skripty

**Pravidlo od 2026-07-13:** každý nový skript použitý pri fyzikálnom audite, numerickom teste alebo rozhodovaní medzi koľajami sa uloží do priečinka `scripts`. Príslušný Markdown protokol musí uviesť názov skriptu, vstupy, prostredie, očakávaný výstup a stav testu.

## Evidencia

| Skript | Účel | Súvisiaci dokument | Stav |
|---|---|---|---|
| `06_script_Q14_light_cone_front_sharpening.py` | Simulácia zaostrovania svetelného frontu | hlavný fyzikálny audit | existujúci skript, auditovaný |
| `07_script_Q12_dispersion_Lorentz_test.py` | Disperzia a izotropia grafových vĺn | hlavný fyzikálny audit | existujúci skript, auditovaný |
| `08_script_Q7_sound_horizon_H0.py` | Zvukový horizont a znamienko neskorej tvorby CDM | hlavný fyzikálny audit | existujúci skript, auditovaný |
| `09_script_K3_cosmology_pipeline.py` | Backgroundová kozmologická pipeline | hlavný fyzikálny audit | existujúci skript, auditovaný s obmedzeniami |
| `10_script_Q10_Vlinks_dowry_rule.py` | Pravidlo vena V-spojov | hlavný fyzikálny audit | existujúci skript, auditovaný |
| `11_script_A1_K1_cdm_background_audit.py` | A1-K1: rozdelenie baryónov/CDM, kladnosť, zachovanie, limita λ=0 a konvergencia | `../Questions/A1_K1_numericky_protokol_T5_2026-07-13.md` | nový reprodukovateľný auditný skript |

## Spustenie skriptu 11

Predvolený auditovaný bod:

```powershell
python scripts/11_script_A1_K1_cdm_background_audit.py
```

Rýchly beh bez polovičného kroku:

```powershell
python scripts/11_script_A1_K1_cdm_background_audit.py --skip-convergence
```

Skript vypíše JSON a skončí návratovým kódom `0`, iba ak prejdú všetky zapnuté kontroly. Pri zlyhaní aspoň jednej kontroly skončí kódom `1`.

## Pravidlá pre ďalšie skripty

1. Názov musí obsahovať poradové číslo a identifikátor problému alebo koľaje.
2. Predvolené parametre musia zodpovedať testu zapísanému v Markdown protokole.
3. Výstup má byť podľa možnosti JSON alebo CSV, aby sa dal automaticky porovnať.
4. Skript musí mať referenčnú limitu alebo inú internú validáciu.
5. Náhodný výpočet musí zaznamenať seed a pri rozhodujúcom teste použiť viac seedov.
6. Numerický výpočet musí uvádzať toleranciu alebo konvergenčný test.
7. Zmena skriptu po publikovaní patrí do novej verzie a changelogu; publikovaný skript sa spätne neprepisuje.
