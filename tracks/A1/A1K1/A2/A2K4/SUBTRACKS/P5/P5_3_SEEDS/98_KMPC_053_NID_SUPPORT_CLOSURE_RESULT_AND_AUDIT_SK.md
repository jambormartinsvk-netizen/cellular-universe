# KMPC-053 — výsledok NID support closure

**Dátum:** 2026-07-18  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Autoritatívny rozsudok:** `PASS_NID_SUPPORT_05_ADEQUATE_AT_K005_NOMINAL`  
**K4/P5:** `LIVE 60/100 / 3.5/6`; score a triggery `NONE`

Raw `RUN_KMPC_053_P5_3G7_NID_SUPPORT_CLOSURE.json`, SHA
`625AC2FAF4BD114D4907ABF83BFF059B50741642E7FB198FA3D7FBCB1BF3B4BD`.

## Výsledok brán

- immutable KMPC-048 regresia `[0,3]/[0,5]`: PASS;
- KMPC-052 V0/V2/V3 parity: PASS;
- hard-anchored M1 depth 7, supporty 03/05 a refined 07 core: PASS;
- combined-`R_fs` a S-C0: PASS;
- common F0/M3 `0…5`: PASS; maxima `4.13e-15` a `1.11e-10` proti `1e-8`;
- tail powers `6,7`: PASS;
- refined driver maximum `1.62e-16`, holdout maximum `2.62e-11`.

Na najhlbšej ploche `z=.01` je F0 tail maximum `3.14e-9` na `U_f` a M3
tail maximum `1.68e-7` na `h`; oboje pod zmrazeným `1e-6`. Candidate
support `[0,5]` je preto pre NID pri `.05/nominal` dostatočný. `[0,9]` sa
nevyžaduje.

## Význam a hranica

NID vetva bola uzavretá až po oprave skutočnej depth mismatch: M3 order 7
musí používať M1 depth 7. Zostávajúca float64 hranica bola nezávisle
uzavretá KMPC-052. Tento výsledok neplatí automaticky pre iné `k`, varianty
ani NIV a nemení celú P5.3 bránu.

Ďalší predregistrovaný mód je NIV. Keďže NIV má leading `j=-1`, jeho
primary/extended support a tail interval sa musia odvodiť z kontraktu 51;
NID support ani correction vector sa naň nesmú preniesť.
