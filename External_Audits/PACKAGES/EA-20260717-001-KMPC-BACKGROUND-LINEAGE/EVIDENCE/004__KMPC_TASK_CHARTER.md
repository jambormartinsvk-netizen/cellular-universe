# Nezávislý audit: význam `K_MPC = 0.05`

**Stav:** `OPEN / nezávislé od G8 FULL`  
**Rola asistenta:** fyzikálny auditor a partner pri tvorbe hypotéz; nie
autorita, ktorá potichu pridá parameter.  
**Rodičovský problém:** univerzálnosť backgroundu z RUN-FULL-002.

## Cieľ

Z filozofických východísk bunkového priestoru a používateľových návrhov
vytvoriť malý počet jasných predpokladov o význame `K_MPC=0.05`, ktoré možno
fyzikálne auditovať. Nájsť buď jeden životaschopný význam vedúci k
univerzálnemu `H(a)`, alebo poctivo ukázať, že aktuálna formula potrebuje
novú fundamentálnu vetvu.

## Hranice

- táto úloha nemení G8, A2-K4 ani publikované predpovede;
- žiadny návrh sa neprijme len preto, že opraví CLASS adapter;
- každý predpoklad dostane: fyzikálny význam, parameter bookkeeping,
  matematický test k‑nezávislosti, pozorovateľný dôsledok a stav
  `živá/review/mŕtva`;
- mŕtve hypotézy zostávajú v dokumentácii s dôvodom smrti.

## Prvý rozsah práce

1. vysvetliť rozdiel medzi vlnovým módom `k` a globálnym referenčným scale
   `k_*` ľudskou rečou;
2. rozlíšiť, či `0.05 Mpc^-1` je Fourierov mód, konvenčný pivot, alebo
   teóriou odvodená sieťová dĺžka;
3. vytvoriť a auditovať koľaje K-N1 až K-N5 v `02_TRACKS.md`;
4. až po prežití koľaje vrátiť výsledok k bráne
   `FULL_BACKEND/03_K4_BACKGROUND_UNIVERSALITY_GATE.md`.
