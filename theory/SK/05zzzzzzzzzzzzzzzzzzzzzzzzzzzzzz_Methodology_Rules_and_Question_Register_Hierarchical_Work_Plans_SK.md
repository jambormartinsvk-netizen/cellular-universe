# Dodatok k 05 — hierarchické živé plány a ohraničené vyhľadávanie (SK)

**Dátum:** 2026-07-15  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia  
**Nové pravidlo:** AR66

## Kontrola duplicity

K-ZROD už určuje, kedy smie vzniknúť fyzikálne nová koľaj. AR30 a C7-W1
oddeľujú sekvenčnú hĺbku od váhy dôkazov. Pravidlá predbehových očakávaní,
timeoutov, error ledgeru a karantény skriptov zostávajú platné.

Chýbalo pravidlo, ktoré určuje malý počet udržiavaných navigačných oporných
bodov, frekvenciu ich aktualizácie a spôsob, ako zabrániť nekonečnému
zakladaniu numerických podvetiev. AR66 vypĺňa túto medzeru bez zmeny
starších pravidiel.

## AR66 — Tri úrovne živého plánu a bounded-search kontrakt

Pre každú aktívnu route cestu sa udržiavajú najviac tri živé pracovné
oporné body:

1. plán rodičovskej fyzikálnej vetvy, ktorý uvádza živé/mŕtve koľaje,
   aktívnu koľaj a stopping kritérium;
2. plán aktívnej fyzikálnej koľaje, ktorý uvádza povinné brány, hĺbku,
   support, pracovný progress a konečný zoznam formulácií;
3. plán aktuálnej implementácie alebo podkoľaje, ktorý obsahuje konkrétne
   najbližšie výpočty, očakávania a rozhodovanie.

Najhlbší plán sa aktualizuje po rozhodujúcom balíku. Rodič sa aktualizuje
iba pri zmene celej brány, skóre, aktívneho dieťaťa alebo verdiktu. Horný
plán sa aktualizuje iba pri zmene fyzikálnej koľaje, stanice alebo release
snapshotu. Pomocný parser fix, log alebo technický rerun neopravňuje
prepisovať všetky tri dokumenty.

Každý plán musí obsahovať:

- úplnú route cestu a ľudský opis problému;
- aktuálny stav, aktívne dieťa a tri odlíšené ukazovatele, ak existujú:
  sekvenčnú hĺbku, vedeckú podporu a pracovný progress;
- čo je hotové, čo chýba a čo znamená PASS alebo STOP;
- tabuľku živých, mŕtvych, čakajúcich a aktívnych detí s dôvodmi;
- autoritatívne odkazy na audity, skripty, výstupy a HISTORY;
- pravidlo, pri akej udalosti sa má plán znovu aktualizovať;
- release snapshot informáciu potrebnú pre changelog a manifest.

## Bounded search namiesto milióna názvov

Pred začiatkom numerického hľadania sa vypíše konečný zoznam diskrétnych
formulácií, ktoré už existujú. Nová formulácia vznikne iba ak odstraňuje
konkrétny zdokumentovaný dôvod zlyhania a matematicky sa líši
reprezentáciou alebo operátorom. Zmena tolerancie, solvera, parametra,
parsera alebo JSON serializácie nie je nová koľaj.

Ak je priestor možností spojitý alebo veľký:

1. použije sa jeden verziovaný runner a konfiguračná matica;
2. prvý beh je lacný široký screen s vopred určeným rozpočtom;
3. ďalšie body sa vyberajú coarse-to-fine iba v regiónoch, ktoré prežili;
4. každý screen má predregistrovaný cieľ, PASS/STOP kritérium a maximálny
   počet iterácií;
5. nový názov podkoľaje vznikne až po identifikovaní fyzikálne alebo
   matematicky novej príčiny, nie po každom výsledku.

Na jeden vedecký balík je dovolená prvá implementácia a najviac dve
technické opravy. Potom nasleduje PASS, fyzikálny STOP alebo
`REVIEW_BLOCKED` s architektonickým rozhodnutím.

## Pravidlo času a dohľadu

Každý Python výpočet musí mať interný deadline aj externý timeout. Pred
spustením sa ľudsky zapíše očakávaný výsledok a rozhodovanie pre výsledok v
očakávanom rozsahu aj mimo neho. Beh nad päť minút vyžaduje osobitné
odôvodnenie, checkpoint/resume a výslovný súhlas používateľa. Jednotlivé
prípady sa spúšťajú oddelene, aby jeden timeout nezablokoval celý balík.

## Release použitie

Tri živé plány sú povinné release oporné body. Pred vydaním sa kontroluje ich
vzájomná zhoda, dátum aktualizácie, aktívna cesta, skóre/hĺbka, otvorené
obmedzenia, zmeny tabuľky predpovedí a odkazy na changelog a SHA-256
manifest. Staré audity sa spätne neprepisujú; živé plány na ne odkazujú a
uvedú, ktorý neskorší audit ich obmedzil.

## AR66.1 — záväzný kontrakt aktuálnej koľaje

AR66 určuje počet živých plánov. AR66.1 dopĺňa vykonávaciu hranicu: pred
každým novým výpočtom sa musí určiť jeden autoritatívny kontrakt aktuálnej
koľaje. Musí obsahovať povinný stavový priestor, konečné brány v poradí,
PASS/STOP/REVIEW, zakázané redukcie, aktuálny stav a rozsah, ktorý ešte
neprešiel. Predregistrácia behu uvedie identifikátor brány a nesmie testovať
inú sústavu bez zmeny kontraktu alebo založenia fyzikálne novej koľaje.

Historický numerický PASS sa nesmie preniesť do nového kontraktu iba podľa
názvu koľaje. Ak neskorší audit nájde chýbajúci stav alebo inú formuláciu,
živý kontrakt musí dostať viditeľnú korekciu a starý plán ostáva iba
históriou s odkazom na obmedzujúci audit. Šablóna je
`tracks/00_TRACK_CONTRACT_STANDARD_SK.md`.

## AR66.2 — formula-provenance uzáver pred auditným PASS

Pred auditným PASS nižšieho zadania alebo skriptu nestačí, že obsahuje
správne názvy premenných, prejde solver alebo dá malé interné rezíduum.
Každý povinný vzorec musí mať v kontrakte koľaje formula-provenance ledger:

1. rodičovskú kovariantnú alebo kanonickú rovnicu a jednoznačnú konvenciu
   pre čas, gauge, Fourierov znak a normalizáciu rýchlosti;
2. odvodený nižší tvar s každým znamienkom, koeficientom a aproximáciou;
3. mapu každý člen rodiča → konkrétny člen implementácie alebo explicitne
   zdokumentované vylúčenie s rozsahom platnosti;
4. aspoň jeden nezávislý algebraický alebo invariantný reziduálny test,
   ktorý nie je iba opakovaním definície tej istej premennej;
5. nulové limity a rozmerovú kontrolu pre každý nový coupling alebo
   fractional exponent.

Textový/AST audit smie dať iba `PASS_MAPY` alebo `PASS_SCOPE`; fyzikálny
formula PASS vyžaduje body 1–5. Ak sa po PASS nájde nepresný vzorec v
nižšom zadaní, starý výsledok sa zachová, ale dostane viditeľné obmedzenie;
odvodené numerické brány sa vrátia do `REVIEW_BLOCKED`, kým nový ledger
neprejde. Pred pokračovaním sa chyba zapíše do error ledgeru a kontraktu.
