# Erratum A2-K4/P5.3g4 — nezmapovaný metrický shear v TCA drive

**Dátum:** 2026-07-16  
**Dotknutý runner/výstup:** `255_script_KMPC_018_P5_3g4_photon_l2_tca_seed.py` /
`RUN_KMPC_018_P5_3G4_PHOTON_TCA_FIRST_ORDER.json`  
**Stav po RERUN1/021:** `FORMULA_PASS_PHOTON_TCA_WITH_SYNCHRONOUS_GAUGE_BRIDGE`.

## Nález

Runner 255 spojil dve správne, ale odlišne kontextované informácie:

1. `Audit/A2_K4_3B_HIERARCHY_MODE_TAXONOMY_RECOMBINATION_AUDIT.md`, riadky
   54–69, dáva synchronnú Ma–Bertschinger rovnicu
   `F_gamma2' = 8 theta_gamma/15 - 3 k F_gamma3/5 + collision`.
   Pri `q_gamma=4 theta_gamma/(3k)` je jej leading drive presne
   `2 k q_gamma/5`.
2. `scripts/76...` používa CAMB symbol `sigma` v inom symbolickom rozhraní.

Skript 255 bez explicitného gauge/normalizačného mosta pridal k synchronnému
drive ešte `8 k shear/15`. Preto jeho nulový kolízny rezíduum je pravdivá
algebraická identita, ale kombinácia `3 q_gamma+4 shear` **nie je ešte
preukázaný synchronný regular-seed koeficient**.

## Čo ostáva platné

- determinant collision bloku `-3/10`, plná hodnosť a nulová TCA rovnováha;
- riešenie `C X + epsilon D=0` pre ľubovoľný deklarovaný drive;
- skorý opacity limit z P5.3g5.

## Pôvodné obmedzenie

Výstup 018 sa nesmie citovať ako odvodenie plného photon `l=2` seedu. Nemá
žiadny vplyv na hĺbku `60/100`, na P5 score, P5.4 ani G8. Nejde o smrť
A2-K4: ide o `REVIEW_BLOCKED` jednej formulačnej väzby.

## Uzavretie obmedzenia

RERUN1/021 preukázal druhú možnosť priamo na lokálnom CAMB zdroji:
`sigma_syn=(hdot+6 eta_dot)/(2k)` a obidve identity majú rezíduum `0`.
255/018 preto ostávajú nezmenené immutable artefakty, ale ich formulačný
význam sa obnovuje iba s odkazom na 021. Samostatný erratum starého photon
zápisu je `Audit/A2_K4_3B_PHOTON_L2_METRIC_SOURCE_ERRATUM_2026-07-16.md`.
