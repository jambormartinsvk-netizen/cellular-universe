# P5.3c — predregistrácia konečných adiabatických štartov

**Skript:** `scripts/244_script_KMPC_007_P5_3c_adiabatic_finite_start_audit.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE.

## Cieľ

Vyhodnotiť P5.3b vedúce adiabatické korekcie na `x=-25` a `x=-23` pri
zmrazenom A1-K1 backgrounde a `k=0.05 Mpc^-1` iba ako referenčnom
perturbačnom móde. Overiť konečnosť, očakávané pomery mocnín a limit
`gamma_2=0` pre `U_c`.

## Očakávania

`U_f` a `delta_f` sa medzi plochami škálujú ako `exp(2 Delta x)`;
`U_c` ako `exp((10-6 delta) Delta x)`. Všetky hodnoty majú byť konečné;
`U_c` musí pri `gamma_2=0` presne zmiznúť. Tento beh neurčuje normalizáciu
primordiálneho módu ani nevykonáva evolúciu.
