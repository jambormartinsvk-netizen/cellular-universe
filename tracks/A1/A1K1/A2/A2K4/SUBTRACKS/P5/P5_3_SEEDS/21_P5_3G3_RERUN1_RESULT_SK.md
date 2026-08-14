# P5.3g3 RERUN1 — neutrínový `l=2` z návratového `qn`

**Skript:** `scripts/254_script_KMPC_017_P5_3g3_standard_neutrino_l2_qn_rerun1.py`  
**Strojový záznam:** `scripts/results/k_mpc_005/RUN_KMPC_017_P5_3G3_STANDARD_NEUTRINO_L2_QN_RERUN1.json`  
**Čas:** 2.5 s; limit 5 s interný / 10 s vonkajší  
**Verdikt:** `DERIVATION_PASS_P5_3G3_RERUN1_NEUTRINO_L2_QN`.

Všetkých päť štandardných módov AD, CDI, BI, NID, NIV má regulárny kandidát
`F2`: nulový v počiatku, s kladným vedúcim rádom; prvý `F3` začína vždy o
jeden rád neskôr a dosadený truncovaný `l=2` residual je presne nula.

Najdôležitejšia nezávislá kontrola konvencie je NIV:

```text
F2 = 2 y/(4 fnu + 5) + ...,
sigma_nu = F2/2 = y/(4 fnu + 5) + ... .
```

To presne zodpovedá samostatnému CAMB shear auditu 106. Výsledok nahrádza
nepoužiteľný 251/PF-044; ten zostáva zachovaný v `18_P5_3G3_LIMITATION_SK.md`.

## Čo ešte chýba

Toto je formula/series kandidát, nie plný seedový PASS: potrebuje nezávislý
Einsteinov constraintový ledger, fotónový quadrupól a TCA pravidelný seed,
vyššie multipóly a dvojštart. P5.4 a G8 sú preto stále blokované.
