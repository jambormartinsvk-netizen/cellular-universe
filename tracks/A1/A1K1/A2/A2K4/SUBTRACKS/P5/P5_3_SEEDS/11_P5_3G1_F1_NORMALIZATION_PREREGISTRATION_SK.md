# P5.3g1 — predregistrácia: normalizácia neutrínového dipólu

**Skript:** `scripts/248_script_KMPC_011_P5_3g1_f1_normalization_provenance_audit.py`  
**Limit:** 5 s interný / 10 s vonkajší; bez ODE a bez skóre.

## Ľudský účel

BR2 vloží hodnotu `seed[5]` priamo do premennej `F_1` collisionless hierarchy.
Skript 84 však svoj šiesty výstup slovne opisuje ako `q_nu=4 theta_nu/(3k)`.
Pred odvodením `F_2` treba dokázať, či BR2 používa presne túto normalizáciu
pre `F_1`, alebo či chýba faktor či znamienko.

## Očakávanie a rozhodnutie

- **PASS_MAPY:** zdroje obsahujú explicitnú rovnosť `F_1=q_nu` (alebo
  ekvivalentnú obojstrannú definíciu) v tej istej synchronnej konvencii.
  Potom P5.3g2 smie odvodiť multipóly `l>=2` z BR2 hierarchy.
- **REVIEW_BLOCKED:** reťazec len priraďuje hodnotu, ale nevysloví normalizáciu.
  Nejde o smrť K4; chýba formula-provenance uzáver a nesmie sa odvodiť koeficient
  z neoverenej premennej.

Tento krok netestuje evolúciu ani fyzikálnu stabilitu.
