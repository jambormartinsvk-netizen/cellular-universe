# REGISTER 05 — SK dodatok k programu A1-K1/A2

**Dátum:** 2026-07-14  
**Status:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

Pravidlá koľají už chránia mŕtve vetvy, maximálnu hĺbku a vznik fyzikálne
odlišných dcér. Chýbalo však explicitné pravidlo, kedy smrť A2 dcéry možno
preniesť na backgroundového rodiča A1-K1 a kedy je priestor mechanizmov
dostatočne vyčerpaný. AR27 preto nie je duplicitné.

## AR27 — Smrť A2 dcéry sa neprenáša automaticky na A1 rodiča

A1-K1 zostáva `OTVORENÁ A PODMIENENÁ` dovtedy, kým:

- aspoň jedna fyzikálne odlišná A2 koľaj ostáva otvorená; alebo
- neexistuje všeobecný no-go dôkaz pokrývajúci všetky A2 uzávery A1-K1.

A1-K1 sa smie opustiť po všeobecnom no-go dôkaze alebo po zdokumentovanom
vyčerpaní všetkých registrovaných tried K4, K7, K8, K9, K11 a K12. Každá
smrť musí mať zachovaný rozsah, dôkaz, skript/výpočet a krížovú kontrolu.
Nová koľaj musí odstrániť konkrétny dôvod smrti novou fyzikou; premenovanie
alebo post-data parameter sa nepočíta ako nevyčerpaná možnosť.

## Q53 — Je A1-K1 už slepá vetva?

**Stav:** `NIE; A2 PROGRAM JE OTVORENÝ.`

- K1–K3, K5 a K6 sú mŕtve iba vo svojom presnom rozsahu.
- K4 prešla K4.1 a prežíva na `55/100`; K4.2 zostáva otvorená.
- K7, K8, K9, K11 a K12 ešte obsahujú otvorené mechanizmy.
- K10 mení background a nepočíta sa ako záchrana A1-K1.

Bezprostredný krok je K4.2; po jeho prípadnej smrti nasleduje K8.1.

### Obmedzenie starších formulácií

Staršie skratky, ktoré zo smrti konkrétnej A2 koľaje vyvodzovali smrť
backgroundu A1-K1, sú obmedzené AR27. Platí iba smrť presne testovaného
uzáveru, pokiaľ dokument výslovne nedokazuje všeobecný no-go.

## Kontrola duplicity AR28

Existujúce pravidlá vyžadujú Einsteinove constrainty a regulárnosť, ale
výslovne nerozlišovali medzi vektorom skonštruovaným v konečnom čase a
úplným priestorom regulárnych primordiálnych Frobeniových módov. AR28 preto
nie je duplicitné.

## AR28 — Primordiálny kill test musí patriť do úplnej regulárnej bázy

Vektor, ktorý v konečnom čase spĺňa Einsteinove constrainty, nie je tým
automaticky prípustným primordiálnym módom. Kill test založený na počiatočných
poruchách musí:

1. odvodiť úplnú Frobeniovu/indiciálnu bázu pri `a -> 0`;
2. vyradiť divergujúce módy s `Re(p)<0`, ak mikrofyzika výslovne nedokáže
   iné prípustné počiatočné rozhranie;
3. ukázať, že testovaný vektor leží v regulárnom constraintovom priestore;
4. osobitne hlásiť absolútny transfer a pomer k nulovej referencii;
5. zachovať aj neplatný historický seed a vysvetlenie jeho obmedzenia.

Smrť vyvolaná vektorom mimo regulárneho primordiálneho priestoru sa nesmie
preniesť na celú koľaj.

## Q54 — Prešla A2-K4 úplnou regulárnou superhorizontovou bránou?

**Stav:** `ÁNO V ROZSAHU K4.1; K4 PREŽÍVA 55/100.`

Indiciálny audit našiel presne tri regulárne módy a hlavný aj nezávislý
integrátor prešli. Historický velocity seed M-011 neleží v ich priestore.
Výsledok neobsahuje high-k, úplnú Boltzmannovu hierarchiu ani CMB-normalizovaný
rast. Bezprostredný krok je K4.2.

### Obmedzenie staršej formulácie M-011

M-011 sa zachováva ako historický riadok, ale jeho zámenu `ln(T/T0)` za
absolútny `ln(T)` a použitie neregulárneho primordiálneho seedu obmedzil audit
K4.1. Prípadná budúca smrť K4 musí mať nový dôvod.

## Kontrola duplicity AR29

Existujúce pravidlá určujú zachovanie výpočtov, dôkazov a mŕtvych koľají,
ale neurčujú povinný časový limit spúšťaných procesov. Kontrola registrov
nenašla staršie pravidlo s rovnakým obsahom. AR29 preto nie je duplicitné.

## AR29 — Každé spustenie skriptu musí mať explicitný časový limit

Každý nový aj historický skript sa smie spustiť iba s explicitným externým
časovým limitom.

- čítanie, vyhľadávanie, hashovanie a krátke kontroly: predvolene `15 s`;
- bežný numerický alebo symbolický beh: najviac `60 s`;
- dlhší výpočet: rozdeliť na úseky najviac `60 s` s checkpointmi;
- stav bežiaceho procesu kontrolovať najneskôr po `10 s` intervaloch;
- po timeoute proces ukončiť, zapísať `TIMEOUT` do MD a opakovať iba s novým
  explicitným limitom;
- limit sa nesmie ticho odstrániť ani zmeniť na neobmedzené čakanie.

Timeout nie je fyzikálny FAIL. Koľaj zostáva bez rozsudku, kým neexistuje
úplný výsledok. Nové dlhšie skripty majú podľa možnosti aj interný runtime
limit a checkpoint, ale externý limit zostáva povinný.

Podrobný prevádzkový zápis je v `scripts/00_EXECUTION_TIME_LIMITS.md`.
