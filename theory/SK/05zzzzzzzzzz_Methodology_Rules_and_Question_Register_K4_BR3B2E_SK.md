# 05 — Dodatok metodiky a registra: K4/BR3B-2e (SK)

Dátum: 2026-07-14

Tento dodatok nemení existujúce pravidlá.

## AR39 — PASS neauditovanej premennej sa nesmie dediť

Cross-check implementácií platí iba pre premenné explicitne zahrnuté v porovnávanom vektore. Ak neskorší výpočet potrebuje vynechaný stress, šmyk alebo multipól, jeho koeficient musí dostať vlastný Euler/Boltzmann/Einstein audit. PASS hustôt, rýchlostí a metriky sa na vynechaný šmyk automaticky neprenáša.

Ak primárne backendy uvádzajú rozdielne koeficienty, uprednostní sa koeficient, ktorý súčasne prejde dynamickou rovnicou, Einsteinovým constraintom a nezávislým numerickým backendom. Staršia formulácia sa nemaže; jej rozsah sa explicitne obmedzí.

## Q66 — Sú skoršie NID/NIV šmykové sektory regulárne?

**Stav: ÁNO PRE PRVÉ DVA SEKTORY; CELÉ G7 OTVORENÉ.**

Najskoršie relatívne rýchlostné sektory sú presne kompenzované a metrické nulové módy. Prvé šmykové sektory NID 5.93109 a NIV 4.93109 majú hodnosť 7, presné Bianchiho rezíduá `0,0`, konečné riešenia a škálované rezíduá pod `6e-15`. Pre NIV bol faktor `1/(4Rnu+5)` potvrdený CAMB 1.6.6 a Eulerovou rovnicou. K4 ostáva živá na 60/100; spoločný fuel sektor a neskoršia `l>=3` rekurzia zostávajú otvorené.

