# P5.3g2 — výsledok: uzavretý most `F1=qnu`

**Skript:** `scripts/250_script_KMPC_013_P5_3g2_f1_qnu_bridge_ledger.py`  
**Strojový záznam:** `scripts/results/k_mpc_005/RUN_KMPC_013_P5_3G2_F1_QNU_NORMALIZATION_BRIDGE.json`  
**Čas:** 0.047 s; limit 5 s interný / 10 s vonkajší  
**Verdikt:** `PASS_P5_3G2_F1_QNU_NORMALIZATION_BRIDGE`.

BR2 definuje `q=k/H0` a z hierarchy berie `U_nu = 3 (aE) F1 / (4q)`.
CAMB konvencia je `qnu=4 theta_nu/(3k)` a `U_nu = 3 Hconf qnu/(4k)`.
Po dosadení `Hconf=H0 aE`, `k=H0 q` je rozdiel presne
`3 aE (F1-qnu)/(4q)`. Nulový rozdiel má pre nenulové `a,E,q` jediný
výsledok `F1=qnu`.

## Rozsah a limit

Je to **formula PASS iba pre normalizáciu neutrínového dipólu** v BR2
bezrozmernej konvencii. Neodvodzuje `F2`, neuzatvára počiatok celej hierarchy,
neotvára P5.4 ani G8. Nasleduje P5.3g3: regulárny `l=2` koeficient z BR2
rovnice a nezávislé constraintové rezíduum.
