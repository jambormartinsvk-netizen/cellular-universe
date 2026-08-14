# P5.3g1 RERUN1 — predregistrácia opravy formálneho markeru

**Skript:** `scripts/249_script_KMPC_012_P5_3g1_f1_normalization_provenance_rerun1.py`  
**Nadväzuje na:** 248 a PF-043.  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE a bez skóre.

Prvý source audit správne zistil chýbajúcu explicitnú rovnosť `F1=qnu`, ale
chybne nenájde BR2-90 rovnicu `l=1`, pretože jej zápis používa `2*f[2]`
namiesto matematicky rovnocenného `2.0*f[2]`. RERUN1 normalizuje zdroj na
významový zápis; nemení súbory 248 ani jeho immutable JSON.

**Očakávanie:** všetky priraďovacie a hierarchy markery prejdú, ale explicitná
rovnosť `F1=qnu` naďalej chýba. Verdikt má preto byť
`REVIEW_BLOCKED_F1_NORMALIZATION_UNPROVEN`, nie fyzikálny FAIL K4.
