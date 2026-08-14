# P5.3g3 RERUN1 — predregistrácia neutrínového `l=2` z návratového `qn`

**Skript:** `scripts/254_script_KMPC_017_P5_3g3_standard_neutrino_l2_qn_rerun1.py`  
**Nadväzuje na:** PF-044 a P5.3g3a RERUN1.  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE a bez skóre.

Skript 251 použil pomocnú `tn`; tento nástupca používa až vrátené
`qn=4 tn/(3k)` z 84. Z BR2 `l=2` rovnice a CDM synchronnej kontinuity opäť
odvodí regulárne `F2` a prvý `F3` pre AD, CDI, BI, NID, NIV.

## Očakávané rozhodnutie

Pre každý mód: `F2(0)=0`, kladný leading exponent, `F3` o vyšší rád a nulové
truncované `l=2` rezíduum. Navyše NIV musí mať presný leading člen
`F2=2y/(4 fnu+5)+...`; po `sigma=F2/2` je to nezávisle už uložený CAMB
vzťah zo skriptu 106. PASS je stále iba formula/series kandidát, nie P5.4.
