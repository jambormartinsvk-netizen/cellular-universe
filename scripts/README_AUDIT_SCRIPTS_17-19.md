# Katalóg auditných skriptov 17–19: S8–H0

**Dátum:** 2026-07-13

| Skript | Účel | Stav |
|---|---|---|
| `17_script_S8_H0_drag_curvature_grid_audit.py` | Nezávislá reprodukcia gridov trenia a FLRW krivosti, audit `χ²_3front` a citlivosti na kovarianciu | PASS; autoritatívny reprodukčný skript |
| `18_script_S8_H0_combined_drag_curvature_point.py` | Overenie príkladu `ΩK=0,002`, `γ=0,015` | PASS; príklad nedosiahol deklarovaný cieľ |
| `19_script_S8_H0_toy_target_calibration.py` | Nájdenie toy bodu, ktorý po dátach trafí `H0=68`, `S8=0,82` | PASS; kalibrácia bez prediktívnej váhy |

## Referenčné výsledky

Skript 17:

- základ: `H0=66,36575`, `S8=0,874649`;
- `γ=0,03`: `S8=0,810779`;
- `ΩK=0,005`: `H0=68,70603`, `S8=0,830343`.

Skript 18:

- `ΩK=0,002`, `γ=0,015`: `H0=67,26723`, `S8=0,825146`.

Skript 19:

- post-data bod `ΩK=0,0035564`, `γ=0,0110529` dá `H0=68,00001`, `S8=0,820000`.

## Interpretácia návratového kódu

Kód `0` znamená, že numerický výpočet prešiel vlastnými kontrolami. Neznamená platnú kozmologickú likelihood ani potvrdenie mikrofyziky.

