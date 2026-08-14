# Audit medzery v pravidlách publikovania verzií na Zenodo

**Dátum:** 2026-07-14  
**Rozsah:** existujúce AR5, AR9, A0 a vydávacie koľaje R3.18-DOC/R3.18-PHYS  
**Výpočet/skipt:** `NOT REQUIRED — metodický a dokumentový audit`

## Rozsudok

Existujúce pravidlá správne chránia nemennosť publikovaných verzií a určujú technické poradie Git commit/tag -> Zenodo. Chýbali však štyri rozhodnutia:

1. aká zmena je dostatočne významná na novú verejnú verziu;
2. ktoré pracovné zmeny sa majú iba zhromažďovať do budúceho balíka;
3. kedy použiť patch, ďalšiu verziu `3.x` alebo `4.0`;
4. aké presné `GO/NO-GO` brány musí release candidate prejsť.

Túto medzeru uzatvárajú:

- `Questions/ZENODO_VERSION_PUBLICATION_CRITERIA.md`;
- `Questions/ZENODO_RELEASE_CHECKLIST_v3.18.md`;
- AR48 a Q74 v SK/EN registri 05.

## Existujúce pravidlá, ktoré sa nemenia

### AR5

Publikované čísla a súbory sú nemenné. Oprava má novú verziu, changelog, manifest, SHA-256 a odkazy na zmenené verdikty.

### AR9

Zenodo vydaniu musí predchádzať skontrolovaný Git commit a release tag. Presuny dokumentov vyžadujú inventár, mapu ciest a kontrolu odkazov.

### A0

A0 zostáva vybavené ako princíp: stará verzia sa ticho neprepisuje. A0 však samo neznamená, že aktuálny workspace je pripravený na nové vydanie.

## Aktuálne správanie Zenodo a naše prísnejšie pravidlo

Zenodo uvádza, že metadáta publikovaného záznamu možno upravovať, ale nová verzia vytvorí nový záznam s vlastným DOI a väzbou na ostatné verzie. Zenodo odporúča versioning pri významnej zmene súborov. Pozri oficiálne stránky [About records](https://help.zenodo.org/docs/deposit/about-records/), [Manage versions](https://help.zenodo.org/docs/deposit/manage-versions/) a [Manage files](https://help.zenodo.org/docs/deposit/manage-files/).

Projekt prijíma prísnejšie pravidlo:

- po publikovaní sa vedecký obsah súborov neupravuje ani v technicky dostupnom opravnom okne;
- zmena ľubovoľného publikovaného súboru vytvorí novú verziu;
- pri bezpečnostnom, právnom alebo osobnom incidente sa postupuje cez obmedzenie prístupu/podporu Zenodo a verejnú poznámku, nie tichým prepisom;
- nesémantická zmena metadát je prípustná iba s lokálnym a verejným metadata changelogom.

## Dôvod prísnejšieho pravidla

Konkrétny verziový DOI musí označovať reprodukovateľný objekt. Čitateľ citujúci staršiu verziu nesmie neskôr dostať iné rovnice, čísla, skripty alebo verdikty pod rovnakou citáciou.

## Aktuálny stav v3.18

### R3.18-DOC

`NO-GO — ZATIAĽ`.

Dôvodom nie je otvorená fyzika sama osebe. Dokumentačné vydanie môže otvorené fyzikálne brány priznať. Pred publikáciou však ešte chýba:

- dokončené upratanie a kanonická mapa dokumentácie;
- jediný aktuálny verejný stavový dokument bez rozporov so staršími smerovníkmi;
- úplný changelog v3.17 -> v3.18;
- celobalíkový manifest a SHA-256;
- pripravený Git commit/tag;
- release audit zmrazeného kandidáta.

### R3.18-PHYS s novými kozmologickými predikciami

`NO-GO` až do príslušných A2/A3/A8 brán. Aktuálna K4 je živá na 66,5/100, ale G7 nie je uzavretá a CMB-normalizovaný predikčný balík nevznikol.

## Hranica verzie 4

Kým sa nemení fundament, vydanie zostáva v rade `3.x`. Verzia `4.0` je povinná, ak sa zmení jadro teórie tak, že výsledok už nie je iba presnejší uzáver tej istej teórie, napríklad:

- základná ontológia bunky alebo rolí palivo/para/popol/doména I;
- rozmernosť alebo fundamentálna kauzálna štruktúra;
- hlavný zákon delenia/metabolizmu alebo A1 backgroundový zákon;
- fundamentálna akcia/gravitácia, ktorá nahradí doterajšie jadro;
- nový objekt propagovaný z efektívneho pomocného mechanizmu na základný postulát.

Nový efektívny uzáver, nový audit alebo nová mikrofyzická realizácia zostáva `3.x`, ak nemení tieto postuláty a otvorene uvádza svoj efektívny status.

