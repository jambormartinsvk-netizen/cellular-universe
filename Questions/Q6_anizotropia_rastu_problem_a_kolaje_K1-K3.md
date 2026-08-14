# Q6 — anizotropia rastu siete: problém, reprodukcia a koľaje

**Dátum:** 2026-07-13  
**Stav:** ČIASTOČNÁ; PÔVODNÝ NUMERICKÝ VERDIKT TREBA SPRESNIŤ

## 1. Čo sa podarilo reprodukovať

Pomocou `scripts/06_script_Q14_light_cone_front_sharpening.py`:

| Režim | N | Metrika |
|---|---:|---:|
| Poisson | 30 000 | 3,4325 % |
| Poisson | 300 000 | 2,0310 % |
| Grown | 29 988 | 5,2020 % |
| Grown | 299 989 | 3,2635 % |

Tvrdenie `3,4 % → 2,0 %` je teda reprodukovateľné pre Poissonov kontrolný graf. Nie je to výsledok režimu `grown`.

## 2. Čo súčasná metrika meria

Skript meria rozptyl priemerného polomeru BFS frontu medzi oktantmi pri jednej hopovej škrupine. Nemeria priamo uhlové rozdelenie smerov delenia buniek ani tenzorovú anizotropiu rastového jadra.

Ďalšie obmedzenia: jeden seed, neperiodické hranice, prvý vhodný zdroj a vstupne izotropné náhodné smery.

## 3. K1 — izotropné lokálne delenie bez dodatočnej preferencie

### Hypotéza

Smer delenia sa žrebuje z rotačne invariantnej distribúcie a makroskopická anizotropia klesá so zväčšujúcim sa N.

### Stav testov

- existencia klesajúceho trendu v jednom behu: **PASS ako indícia**;
- rozlíšenie Poisson/grown: **pôvodný text neprešiel**;
- viac seedov a interval spoľahlivosti: **NEUROBENÉ**;
- periodické hranice: **NEUROBENÉ**;
- analytický exponent poklesu: **NEODVODENÝ**;
- metrika rastového jadra namiesto BFS frontu: **NEUROBENÉ**.

### Stav

**PREŽÍVA; NA STENE ŠTATISTICKEJ A MERACEJ VALIDÁCIE.**

## 4. K2 — geometricky viazané delenie

### Hypotéza

Lokálna orientácia hrán, napätie alebo tvar Voronoiho bunky ovplyvní smer ďalšieho delenia. Makroskopická izotropia musí vzniknúť coarse-grainingom, nie byť vložená do generátora.

### Testy

- rotačná kovariancia lokálneho pravidla;
- multipóly smerového rozdelenia;
- závislosť od počiatočnej mriežky;
- škálovanie kvadrupólu s N.

### Stav

**PREŽÍVA; ZATIAĽ BEZ IMPLEMENTÁCIE.**

## 5. K3 — delenie plus lokálna relaxácia/retriangulácia

### Hypotéza

Anizotropiu po delení odstraňuje lokálna relaxácia alebo Delaunayova retriangulácia pri zachovaní lokálnosti.

### Riziká

- relaxácia nesmie zaviesť nadsvetelné alebo globálne preusporiadanie;
- musí zachovať účtovníctvo energie a informácie;
- môže meniť kauzálny graf a predchádzajúce predikcie.

### Stav

**PREŽÍVA AKO ZÁLOŽNÁ KOĽAJ; VYSOKÉ RIZIKO ZMENY FUNDAMENTU.**

## 6. Ďalší krok

Pokračovať K1: vytvoriť samostatný multi-seed skript, oddeliť Poissonovu kontrolu od rastového grafu, pridať periodické hranice a merať dipól/kvadrupól priamo v smeroch rastu. Až potom fitovať pokles `A(N) ∝ N^-α` a formulovať makroskopický limit.

