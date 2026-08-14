# P5.3g1 — výsledok: formátovo korektná mapa `F1`

**Skripty:** 248 (historický prvý beh), 249 (RERUN1)  
**Autoritatívny záznam:** `scripts/results/k_mpc_005/RUN_KMPC_012_P5_3G1_F1_NORMALIZATION_PROVENANCE_RERUN1.json`  
**Verdikt:** `REVIEW_BLOCKED_F1_NORMALIZATION_UNPROVEN` — neskôr uzavretý P5.3g2.

Prvý beh 248 mal formálne falošné negatívum pre BR2-90, pretože očakával
zápis `2.0*f[2]`; zdroj používa algebraicky rovnaké `2*f[2]`. PF-043 tento
dôvod a starý JSON zachováva. RERUN1 (249) potvrdil všetky priradenia:
`seed[5]` ide do hierarchy `l=1` a obidva BR2 zdroje majú správnu `l=1`
rovnicu. Vtedy však ešte nebola explicitná rovnosť `F1=qnu` v jednom súbore.

Táto medzera sa nesmela prekryť menom premennej; uzavrel ju až samostatný
algebraický most P5.3g2. RERUN1 preto nie je fyzikálny FAIL ani sám osebe
formula PASS.
