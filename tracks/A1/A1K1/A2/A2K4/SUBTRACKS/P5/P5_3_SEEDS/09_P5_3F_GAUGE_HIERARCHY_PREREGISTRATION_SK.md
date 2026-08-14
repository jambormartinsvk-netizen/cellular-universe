# P5.3f — predregistrácia gauge a hierarchy seedového auditu

**Skript:** `scripts/247_script_KMPC_010_P5_3f_gauge_hierarchy_seed_audit.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE.

Audit preverí dve oddelené veci: (1) `U_f-U_c` je invariantná relatívna
rýchlosť pri spoločnom synchronnom velocity shifte, preto `U_c=0` nesmie
odstrániť fyzikálny relatívny mód; (2) ktoré seed zdroje obsahujú plnú
hierarchiu. Očakáva sa, že 80 kryje interný nu-steam hierarchy seed, ale
84/89/90 štandardný seed napĺňa iba `l=0,1`. PASS je iba presná mapa a
zablokuje P5.4 do doplnenia štandardného `l>=2` seedu.
