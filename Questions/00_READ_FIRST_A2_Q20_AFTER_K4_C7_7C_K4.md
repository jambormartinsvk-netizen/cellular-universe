# Čítaj ako prvé — A2/Q20 po C7.7c-K4

## Aktuálny stav

- A2-K4: **živá, technicky pozastavená**
- jemná hĺbka: **66,5/100**
- posledná úplná hlavná brána: **G6**
- G7: otvorená
- C7.7a: PASS
- C7.7b: PASS
- C7.7c: neuzavretá po troch časovo ohraničených numerických variantoch

## Prečo teraz nepokračovať štvrtou optimalizáciou K4

K2, K3 aj K4 narazili na prakticky rovnakú výpočtovú stenu. Ďalší pokus už nie je lacná fyzikálna kontrola, ale samostatná úloha profilovania a návrhu stuhnutého solvera. Pred jej otvorením je informačne výhodnejšie zistiť, či nezačaté A2-K8 alebo A2-K9 neprežijú lacné skoré brány.

## Nasledujúci krok

1. Rekonštruovať fyzikálnu definíciu A2-K8 zo súhrnu a zdrojových dokumentov.
2. Zapísať jednovetový mechanizmus, odlišnosť od K1–K7, povinné zákony a rýchle smrtiace testy.
3. Vykonať iba lacnú bránu G0–G2 s časovými limitmi.
4. Ak K8 zomrie, uchovať dôvod aj skripty a pokračovať K9.
5. Po K8/K9 porovnať živé koľaje a rozhodnúť medzi návratom ku K4, re-entry K7/K11/K12 alebo ďalšou koľajou A1.

## Dôležité obmedzenie

K4 nie je mŕtva. Timeout sa nesmie v budúcnosti citovať ako fyzikálna eliminácia.

