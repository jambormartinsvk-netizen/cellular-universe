# P5.3d — výsledok vedúcich seedov štandardných módov

**Výstup:** `scripts/results/k_mpc_005/RUN_KMPC_008_P5_3D_STANDARD_MODE_LEADING_SEEDS.json`  
**Čas / limit:** 0.562 s / 5 s  
**Verdikt:** `PASS_P5_3D_STANDARD_MODE_LEADING_SEEDS`

Všetkých 35 kontrol pre AD, CDI, BI, NID a NIV prešlo. Pre každý mód sú
palivové členy regulárne a `U_c` je vyšší rád, ktorý zaniká v `gamma→0`.

Podstatné: CDI a BI majú vedúce `delta_f=0`, ale majú nenulové `U_f`.
Starý štart, ktorý dával nulu aj `U_f`, preto nie je plný regular seed.
Výsledok ešte nepokrýva interné neutrínovo-parné módy, vyššie rády, gauge
triedenie a dvojštartovú validáciu.
