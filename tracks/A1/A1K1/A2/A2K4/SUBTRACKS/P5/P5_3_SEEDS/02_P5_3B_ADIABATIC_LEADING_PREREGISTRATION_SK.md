# P5.3b — predregistrácia: adiabatický vedúci Puiseux seed

**Koľaj:** `A1-K1 → A2-K4 → P5 → P5.3b`  
**Skript:** `scripts/243_script_KMPC_006_P5_3b_adiabatic_leading_seed_ledger.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE.

## Predpoklady presne obmedzeného výpočtu

V najskoršej radiačnej ére pre adiabatický mód platí `h_x=H a^2+...`,
`h_c=-1+...`, `gamma~a^2`, `X_f/X_c~a^(3-3 delta)` a
`beta~delta X_f/X_c`. Homogénny divergentný palivový density mód sa zahodí
ako nepravidelný. Nejde o plný seed ani o isokurvatúrne módy.

## Očakávané vedúce členy

Z palivovej kontinuity a Eulerovej rovnice sa očakáva

```text
U_f = A H a^2,          delta_f = delta A H a^2,
A = -1/(52-24 delta).
```

Energy-frame CDM hybnosť sa očakáva až v ráde
`a^(10-6 delta)` s koeficientom úmerným `delta gamma_2 r_0^2 A H`, preto
v limite `gamma→0` zaniká. Staré konečné nuly 89/90 sú teda len približný
seed; tento ledger ich nenahrádza v ODE.

## PASS a STOP

PASS vyžaduje presné nuly vedúcich palivových rovníc, regularitu a nulový
limit transferu. STOP je nenulový zvyšok alebo divergentný nútený mód.
PASS neoveruje ďalšie módy, vyššie rády, gauge transformáciu ani dvojštart.

## Korekcia po prvom behu

Prvý beh skončil PF-042 pred JSON výstupom: všeobecná symbolická nerovnosť
`8-6 delta>0` nemá bez rozsahu `delta` pravdivostnú hodnotu. Algebraické
identity ostávajú všeobecné; jediná porovnávacia nerovnosť sa vyhodnotí na
zmrazenom A1-K1 vstupe `delta=0.02297`. Nejde o fit ani zmenu fyziky.
