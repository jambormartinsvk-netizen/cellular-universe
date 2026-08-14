# Auditný skript 21 — barotropická uzávera paliva

**Skript:** `21_script_A2_barotropic_fuel_gradient_instability.py`  
**Dátum behu:** 2026-07-13  
**Návratový kód:** `0`  
**Verdikt hypotézy:** `MRTVA_BAROTROPIC_CLOSURE`

## Účel

Skript kvantifikuje analytickú gradientovú nestabilitu striktne barotropického paliva pri

`w_f=c_s,f^2=-1+delta=-0.97703`.

Nie je to solver úplného perturbačného systému. Smrť koľaje vyplýva zo znamienka hlavného `c_s^2 k^2` člena; skript ukazuje veľkosť rastovej miery na reprezentatívnych škálach.

## Reprodukčný príkaz

```powershell
python -m py_compile scripts/21_script_A2_barotropic_fuel_gradient_instability.py
python scripts/21_script_A2_barotropic_fuel_gradient_instability.py
```

## Zachovaný výstup

```text
A2 BAROTROPIC FUEL GRADIENT DIAGNOSTIC
delta=0.02297000
w_f=-0.97703000
c_s^2(barotropic)=-0.97703000
|c_s|=0.98844828
H0/c=2.213864899830e-04 1/Mpc

k[h/Mpc] | k[1/Mpc] | mu/H0 | one e-fold time [H0^-1]
   0.010 | 0.006637 |    29.633 |     3.374624e-02
   0.100 | 0.066370 |   296.329 |     3.374624e-03
   1.000 | 0.663700 |  2963.293 |     3.374624e-04

principal_equation: delta_k'' + c_s^2 k^2 delta_k = 0
negative_cs2_solution: delta_k proportional exp(|c_s| k eta)
kill_condition_negative_cs2_subhorizon=TRUE
VERDICT=MRTVA_BAROTROPIC_CLOSURE
```

## Rozsah verdiktu

Skript zabíja iba uzáveru `c_s,f^2=w_f<0`. Nehodnotí A2-K1 s `c_s,f^2=1`, superhorizontovú stabilitu, gauge konzistenciu, CLASS/CAMB ani dáta.

## Pravidlo uchovania

Skript a tento výstup sa nemažú. Ak sa nájde chyba, vznikne nový očíslovaný skript a Markdown erratum.

