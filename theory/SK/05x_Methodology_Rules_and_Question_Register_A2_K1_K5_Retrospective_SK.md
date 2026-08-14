# REGISTER 05 — SK dodatok po retrospektíve A2-K1 až A2-K5

**Dátum:** 2026-07-13  
**Status:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR18 už určuje, že max. hĺbka je najhlbší vykonaný test a nepromuje rodiča.
AR3 a pravidlá errát určujú zachovanie mŕtvych koľají a chybných rozsudkov.
Žiadne existujúce pravidlo však explicitne neoddeľuje absolútny transfer od
pomeru k dynamicky zanikajúcej nulovej referencii. AR25 preto nie je
duplicitné.

## AR25 — Absolútny transfer a zisk voči referencii sú odlišné brány

Pri teste módu sa musia osobitne vykázať

```text
T_abs=|y_final/y_initial|,
T_null,
G=T_abs/T_null.
```

Ak `T_null` silno zaniká, veľké `G` samo nedokazuje veľký absolútny rast.
Konečný kill rozsudok sa nesmie opierať iba o `G>e`, ak neexistuje vopred
odvodená fyzikálna väzba medzi týmto pomerom a divergenciou, stratou
linearity alebo observačným limitom. Okamžitý eigenvalue podbloku sa tiež
nesmie zameniť za globálny exponent úplnej časovo závislej sústavy.

## Q51 — Sú hĺbky a rozsudky A2-K1 až A2-K5 po retrospektíve správne?

**Stav:** `ČIASTOČNE.`

- K1 `45/100`, K2 `25/100`, K3 `45/100` a K5 `75/100` sa potvrdzujú.
- K4 si ponecháva max. hĺbku `50/100`, ale M-011 sa pozastavuje.
- K4 nie je vyhlásená za preživšiu; čaká úplnú K4.1 bázu módov.

### Obmedzenie starších formulácií

Staršie tvrdenie „K4 má 11.5901 e-foldov nestability“ sa smie čítať iba
ako `ln(T_K4/T_null)=11.5901`. Absolútne platí
`ln(T_K4)=0.4620`. Historický M-011 záznam a skripty sa zachovávajú s
erratom.

