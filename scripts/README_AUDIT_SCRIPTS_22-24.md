# Auditné skripty 22–24 — A2-K1

**Dátum:** 2026-07-13  
**Finálny vedecký verdikt:** `MRTVA_A2_K1`

## Skript 22

`22_script_A2_K1_superhorizon_velocity_instability.py`

- prvý výpočet exponentu na backgrounde skriptu 13;
- `lambda/delta=6.5302568568`;
- exponent od rekombinácie `12.2131075096` na jemnejšom z dvoch behov;
- fyzikálne brány prešli;
- konvergenčný rozdiel `3.6758627e-8` neprešiel prahom `1e-8`;
- návratový kód 1, stav `REQUIRES_FULL_REVIEW`.

Skript zostáva zachovaný ako neúspešný konvergenčný beh.

## Skript 23

`23_script_A2_K1_superhorizon_velocity_instability_converged.py`

- nástupca skriptu 22 bez zmeny fyziky alebo prahu;
- kroky `5e-4` a `2.5e-4`;
- finálny `H0 Delta t(z_star->0)=0.9351169231`;
- finálny exponent `12.2131073973`;
- zosilnenie `201411.9108`;
- relatívny konvergenčný rozdiel `9.1895363e-9 < 1e-8`;
- všetky tri kill checks `true`;
- `VERDICT=MRTVA_A2_K1`, návratový kód 0.

## Skript 24

`24_script_A2_K1_equation_sign_and_null_limit_audit.py`

Symbolicky overil:

1. znamienko kontinuity CDM;
2. znamienko kontinuity paliva;
3. znamienko Eulerovej rovnice paliva;
4. znamienko superhorizontovej miery;
5. tri nulové limity `Gamma->0`;
6. párové zrušenie backgroundového zdroja.

Všetkých osem kontrol: `true`; stav `PASS`.

## Reprodukčné príkazy

```powershell
python scripts/22_script_A2_K1_superhorizon_velocity_instability.py
python scripts/23_script_A2_K1_superhorizon_velocity_instability_converged.py
python scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py
```

## Rozsah

Skripty zabíjajú presne A2-K1. Nezabíjajú background A1-K1 ani koľaje A2-K3 až A2-K5.

