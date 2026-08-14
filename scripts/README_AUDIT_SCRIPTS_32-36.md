# Reprodukcia A2-K5/K1 — skripty 32 až 36

**Dátum:** 2026-07-13  
**Python:** vyžaduje `numpy`; používa validovaný background skriptu 13

## Poradie

1. `32_script_A2_K5_K1_canonical_scalar_reconstruction.py` — rekonštrukcia
   `V(phi)`, `A(phi)`, `beta`, zdroja a hmotností;
2. `35_script_A2_K5_K1_mass_stability_crosscheck.py` — samostatný výpis miním
   `m_phi^2` a `m_eff^2` s krokovou konvergenciou;
3. `33_script_A2_K5_K1_quasistatic_growth_gate.py` — prvý kvázistatický
   CDM+baryónový rastový test;
4. `34_script_A2_K5_K1_weighted_matter_growth_and_S8_projection.py` — pôvodný
   vážený rast a diagnostická projekcia;
5. `36_script_A2_K5_K1_weighted_matter_growth_and_S8_projection_corrected_labels.py`
   — superseduje iba názvy asymetrických chýb skriptu 34.

## Spustenie

```powershell
python scripts\32_script_A2_K5_K1_canonical_scalar_reconstruction.py
python scripts\35_script_A2_K5_K1_mass_stability_crosscheck.py
python scripts\33_script_A2_K5_K1_quasistatic_growth_gate.py
python scripts\34_script_A2_K5_K1_weighted_matter_growth_and_S8_projection.py
python scripts\36_script_A2_K5_K1_weighted_matter_growth_and_S8_projection_corrected_labels.py
```

Všetkých päť behov musí skončiť kódom `0`. Skript 33 hlási
`PASS_NUMERICS_GROWTH_RISK_CONFIRMED`: slovo `PASS` označuje numerickú
konvergenciu a reprodukovateľnosť alarmu, nie fyzikálne schválenie koľaje.

## Rozsah

Skripty 33, 34 a 36 sú subhorizontové diagnostiky. Neobsahujú fotónové a
neutrínové perturbácie, úplné Einsteinove constrainty, superhorizontový mód
ani CMB normalizáciu. Nesmú sa vydávať za CLASS/CAMB likelihood.

Oprava označenia skriptu 34 je zachovaná v
`scripts/ERRATUM_34_36_A2_K5_K1_KIDS_ASYMMETRIC_LABELS.md`; pôvodný skript sa
nemaže.
