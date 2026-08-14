# KMPC-095 — HP-M1 column-equilibrated QR successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `2/10`

## Jediná povolená zmena

KMPC-094 skončil po úspešnom smoke v `mpmath.qr_solve` na hlásení
`matrix is numerically singular`. KMPC-095 nahradí iba reduced-solve
funkciu diagonálnou stĺpcovou ekvilibráciou:

`A x = b`, `A' = A D^-1`, `y = D x`, solve `A' y = b`, potom `x = D^-1 y`.

Každý scale je maximum absolútnych hodnôt príslušného stĺpca. Riadky ani
pravá strana sa neškálujú, preto sa nemení pôvodný unweighted least-squares
cieľ. Po solve sa residual znovu vypočíta v pôvodných súradniciach a exportuje
sa minimum, maximum a pomer stĺpcových scale.

Frozen KMPC-093 M1 modul a KMPC-094 owner modul ostávajú byteovo nezmenené.
Nemenia sa rovnice, M1 riadky, background bridge, hard anchor, 80 dps, F0,
fractional background, M3, support, prahy ani non-fit holdout.

## Brány a interpretácia

- compile/help/smoke, source/prerequisite hashe a owner lifecycle prejdú;
- všetkých 98 scales je konečných a kladných, row scaling je false;
- jeden nový M1 solve a pôvodné dva M3 solve; žiadny holdout vo solve;
- fyzikálna interpretácia zostáva presne podľa predregistrácie 156;
- ďalšia `matrix is numerically singular` alebo iný implementačný pád je
  `TECHNICAL_ERROR / NO_PHYSICS_VERDICT`, nie fyzikálny STOP.

## Zmrazená implementácia pred prvým Python behom

- V3 column-equilibrated modul:
  `8C52A465C5417EC65A89AC0484AB201EC3CFB0101D5630EB97844F65E2E19192`;
- runner 339:
  `942D22363F669CA7F2036D267222EBF35A79E6D2C2C3A2A011FCD5C4B4A427A1`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `44/44` source/prerequisite hashov sedelo; všetkých
  `47` dlhých hash literálov malo presne 64 hex znakov.

Po freeze sa V1–V3 ani runner pred official behom nemenia. Úspešný vecný
výpočet resetuje technický counter na `0/10`; autoritatívny C2/K4 stav sa
mení až po internom audite.

## Explicitný pre-run refreeze

Pred prvým Python behom statický review našiel, že iba syntetický scale
fixture nevstupoval do vlastného `80 dps` contextu. Official algoritmus sa
nemenil. Pôvodné, nikdy nespustené hashe boli modul
`1C0CA3C778EFD91F441125E58AF4614851EF461676392F3A8B92AAF247C0B5FC`
a runner `E15B2E4F1A66F663DEE9B7B1020F2EFF6DF2C959C713FF1E88B7FB2576CBE80B`.
Fixture bol ešte pred compile/smoke uzavretý v `mp.workdps(80)` a hore sú
uvedené nové autoritatívne hashe. Nejde o technické zlyhanie ani ďalší pokus.
