# Stav spracovania hypotéz trenia, krivosti a kombinácie S8–H0

**Dátum:** 2026-07-13  
**Status:** SPRACOVANÉ AUDITOM; NEVKLADAŤ PÔVODNÉ ZÁVERY BEZ OPRÁV

## Spracované vstupy

- grid `γdrag=0,00–0,06`;
- grid `ΩK=-0,005–+0,005`;
- tvrdenia o optime `γ≈0,03` a `ΩK≈0,005`;
- príklad kombinácie `ΩK=0,002`, `γ=0,015`;
- tvrdenia o zlepšení `χ²` voči ΛCDM.

## Autoritatívne výstupy

- `../Audit/AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md`;
- `../Audit/ERRATUM_predbezny_S8_H0_screening_skript16_2026-07-13.md`;
- `../Questions/S8_H0_K1_K4_K5_autoritativny_stav_a_dalsie_testy.md`;
- `../scripts/17_script_S8_H0_drag_curvature_grid_audit.py`;
- `../scripts/18_script_S8_H0_combined_drag_curvature_point.py`;
- `../scripts/19_script_S8_H0_toy_target_calibration.py`.

## Pokyny pre zapracovanie do v3.18

Povolené:

- tabuľky označené ako sensitivity study zjednodušenej pipeline;
- prežívajúce koľaje K1b, K4a/K4b a K5 so skóre a kill conditions;
- explicitné priznanie, že parametre nie sú odvodené ani plne fitované.

Zakázané:

- „exaktná kalibrácia“;
- „dokonalá štatistická zhoda“;
- „celkové χ² = 8,99/9,50“;
- „zlepšenie o 20–21 bodov“;
- „trenie vyriešilo S8 na 100 %“;
- „ΩK=0,005 vyplýva z topológie siete“;
- kombinovaný kalibrovaný bod ako predikcia.

Pôvodný text hypotéz je týmto považovaný za spracovaný. Ďalšia práca patrí do nových testov K1b-T1 alebo K4b-T1, nie do opakovania týchto gridov.

