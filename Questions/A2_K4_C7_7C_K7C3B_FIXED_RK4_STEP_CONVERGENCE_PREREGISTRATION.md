# A2-K4 / C7.7c / K7c.3b — predregistrácia pevného RK4 a krokovej konvergencie

Dátum: 2026-07-15  
Vstup: DOP853 v 180 narazil na RHS cap; profil 182 vylúčil veľké vlastné číslo

## Nemenná fyzika

- rovnaký NID/deep HP seed zo 178;
- rovnaký 13-zložkový projektovaný RHS a background ako 179/180;
- rovnaký interval `[-25,-24.75]`, envelope škála a closure `L5=0`;
- žiadna zmena rovnice, parametra ani constraint prahu.

## Dve pevné mriežky

- hrubá: RK4, krok `h=0.002` (125 krokov);
- jemná: RK4, krok `h=0.001` (250 krokov);
- žiadny adaptívny error controller a žiadny `atol/rtol`;
- checkpointy začiatok, polovica, koniec;
- maximálne 2 000 RHS volaní vrátane auditu;
- normalizovaný safety cap `1e8` a pevný časový limit.

## Brány

1. obe mriežky dosiahnu koniec a všetky stavy/RHS sú konečné;
2. max normalizovaný rozdiel jemného a hrubého endpointu je `<1e-6`;
3. jemný endpoint sa netriviálne líši od seedu o viac než `1e-12`;
4. density/momentum constraint rezíduá na jemných checkpointoch sú `<5e-12`;
5. žiadny safety cap ani limit RHS volaní sa neprekročí;
6. výsledok reportuje každý z 13 endpointov a rozdiel po komponentoch.

PASS dokazuje iba krátku konvergovanú NID/deep evolúciu a povoľuje rovnakú bránu na NID/shallow. FAIL pri oboch konečných mriežkach môže zabiť K7c.3b; technická chyba ostáva REVIEW. Skóre sa nemení.
