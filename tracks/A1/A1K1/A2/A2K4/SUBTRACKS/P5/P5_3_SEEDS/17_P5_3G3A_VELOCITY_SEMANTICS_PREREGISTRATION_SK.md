# P5.3g3a — predregistrácia: sémantika velocity výstupu 84

**Skript:** `scripts/252_script_KMPC_015_P5_3g3a_seed84_velocity_semantics_audit.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE a bez skóre.

## Prečo je tento test nutný

84 opisuje svoj výstup ako `qnu=4 theta_nu/(3k)`. Pri fixnom `y=k tau` a
rovnakej jednotkovej metrike (`eta`) preto nesmie jeho `qnu` dostať ďalší
faktor `k`. No NIV formula 84 začína `0.75*k`. P5.3g2 identifikoval
normalizácie iba za predpokladu, že názov a formula majú rovnaký význam.

## Test a očakávanie

Skript zavolá iba čistú funkciu `class_seed` z 84 pri dvoch `k`, pričom drží
`y=k tau` konštantné, a overí samostatne invariantnosť `eta` a škálovanie
piateho/siedmeho výstupu. 

- **PASS:** `qnu` je pri fixnom `y` invariantné; P5.3g2 sa obnoví a G3
  kandidát pokračuje na nezávislý constraint ledger.
- **REVIEW_BLOCKED:** `eta` ostane invariantné, ale `seed[5]` škáluje s `k`.
  Potom 84 nemôže byť súčasne zdrojom deklarovaného `qnu` a BR2 `F1`; treba
  kanonický seedový zdroj alebo explicitnú konverziu. K4 neumiera, ale P5.4
  a G8 zostanú zavreté.
