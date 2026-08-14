# P5.3e — predregistrácia interných kompenzovaných módov

**Skript:** `scripts/246_script_KMPC_009_P5_3e_internal_modes_regularity.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE.

Pre kompenzované interné neutrínovo-parné módy je vedúci metric zdroj nulový.
Overí sa homogénny palivový 2x2 systém. Ak jeho korene majú zápornú reálnu
časť pri zmrazenom `delta`, nenulový homogénny seed diverguje k `a→0` a
nulový `delta_f,U_f,U_c` je regularita pre tento seed, nie gauge voľba.
PASS nepokrýva vyššie rády ani ODE.
