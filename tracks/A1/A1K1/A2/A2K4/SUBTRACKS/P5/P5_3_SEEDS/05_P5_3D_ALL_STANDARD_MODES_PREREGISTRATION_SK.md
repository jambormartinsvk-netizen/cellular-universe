# P5.3d — predregistrácia vedúcich seedov všetkých štandardných módov

**Skript:** `scripts/245_script_KMPC_008_P5_3d_all_standard_modes_seed_ledger.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE.

## Rozšírenie

Pre všeobecný štandardný synchronous metric zdroj `h_x=H a^n+...` sa
odvodí palivový seed pre exponenty `n=(2,1,1,3,2)` módu AD, CDI, BI, NID,
NIV. Očakáva sa

```text
U_f/H = -1/[2((n-1)(n+6-3 delta)+9(2-delta))],
delta_f = delta (n-1) U_f,
U_c ~ a^(n+8-6 delta).
```

PASS vyžaduje presné vedúce nuly, regularitu každého módu a `gamma→0`
limit `U_c`. Neoveruje amplitúdy CLASS/CAMB, vyššie rády, interné
neutrínovo-parné módy, gauge úplnosť ani ODE.
