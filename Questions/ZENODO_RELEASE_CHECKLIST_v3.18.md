# Zenodo release checklist — v3.18

**Stav:** `NO-GO — pracovný checklist`  
**Cieľový prvý release:** `R3.18-DOC`  
**PHYS/PREDICTION:** samostatný neskorší kandidát

## A. Identita a rozsah

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-A1 | Release trieda je explicitne `DOC`, `ERRATUM`, `PHYS` alebo `PREDICTION`. | `PASS — plánované DOC` |
| ZR-A2 | Verzia je správne klasifikovaná ako `3.18`, nie `4.0`. | `PASS — fundament sa zatiaľ nemení` |
| ZR-A3 | Je uvedený predchádzajúci verziový DOI aj concept/all-versions DOI. | `OPEN` |
| ZR-A4 | Scope statement presne hovorí, čo vydanie tvrdí a čo netvrdí. | `OPEN` |
| ZR-A5 | Existuje zoznam verejných tvrdení a ich dôkazových úrovní. | `OPEN` |

## B. Vedecká a auditná konzistencia

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-B1 | Jediný aktuálny `READ_FIRST` ukazuje na všetky autoritatívne stavové dokumenty. | `OPEN — vznikli nové A2 dodatky` |
| ZR-B2 | Staršie rozpory sú zachované, ale označené ako historické/obmedzené. | `PARTIAL` |
| ZR-B3 | Každá mŕtva koľaj má dôvod, rozsah, skript/výpočet a podmienku znovuotvorenia. | `PARTIAL — priebežne vedené` |
| ZR-B4 | Žiadna otvorená hypotéza nie je označená ako predikcia alebo potvrdenie. | `REQUIRES FINAL AUDIT` |
| ZR-B5 | Predikčné tabuľky zachovávajú historické čísla alebo ich menia iba cez changelog a príslušnú bránu. | `OPEN` |
| ZR-B6 | SK register je autoritatívny a EN zrkadlo má rovnaké ID a význam. | `PARTIAL — treba celkový cross-check` |

## C. Changelog a erratá

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-C1 | Changelog v3.17 -> v3.18 je úplný. | `OPEN` |
| ZR-C2 | Každá materiálna zmena má `OLD -> NEW -> REASON -> EVIDENCE`. | `OPEN` |
| ZR-C3 | Zmenené/odvolané verejné čísla a tvrdenia sú viditeľné v samostatnej sekcii. | `OPEN` |
| ZR-C4 | Metadata changelog je oddelený od vedeckého changelogu. | `OPEN` |

## D. Reprodukovateľnosť

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-D1 | Každý použitý výpočet má zachovaný skript alebo `NOT REQUIRED` analytický dôkaz. | `PARTIAL/PRECHÁDZA PRIEBEŽNE` |
| ZR-D2 | Skripty majú limity, vstupy, jednotky, tolerancie a prostredie. | `PARTIAL` |
| ZR-D3 | Výstupy sú zmrazené a prepojené s auditnými verdiktmi. | `PARTIAL` |
| ZR-D4 | Celý release balík má manifest ciest, veľkostí a SHA-256. | `OPEN` |
| ZR-D5 | Reprodukčné príkazy boli spustené z čistého release checkoutu. | `OPEN` |

## E. Dokumentácia a balenie

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-E1 | Dokumenty sú rozdelené do schválenej logickej adresárovej štruktúry. | `OPEN` |
| ZR-E2 | Existuje mapa stará cesta -> nová cesta a kontrola odkazov. | `OPEN` |
| ZR-E3 | V balíku nie sú `__pycache__`, `.pyc`, tajomstvá, lokálne závislosti ani dočasné výstupy. | `OPEN` |
| ZR-E4 | README, citácia, licencia a BibTeX sú konzistentné. | `OPEN` |
| ZR-E5 | Archív sa rozbalí a základné odkazy/skripty fungujú. | `OPEN` |

## F. GitHub release candidate

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-F1 | Kanonický GitHub repozitár je zosúladený a pracovný strom release vetvy je čistý. | `OPEN` |
| ZR-F2 | Existuje reviewed commit pre presný release obsah. | `OPEN` |
| ZR-F3 | Existuje nemenný release tag, napr. `v3.18`. | `OPEN` |
| ZR-F4 | Manifest obsahuje commit SHA a tag. | `OPEN` |
| ZR-F5 | CI alebo lokálna release validácia je PASS. | `OPEN` |

## G. Nezávislý release audit

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-G1 | Zmrazený release candidate dostal audit bez následnej tichej zmeny. | `OPEN` |
| ZR-G2 | DOC auditor overil rozsah, rozpory, changelog, odkazy a reprodukčnú stopu. | `OPEN` |
| ZR-G3 | Pri PHYS/PREDICTION auditor nezávisle reprodukoval rozhodujúce výpočty. | `N/A PRE DOC; POVINNÉ PRE PHYS/PREDICTION` |
| ZR-G4 | Každá oprava po audite vytvorila nový RC manifest a opakovaný audit. | `OPEN` |

Určeným auditorom môže byť Fable 5 alebo iný vopred pomenovaný nezávislý auditor. Samotné meno auditora nenahrádza jeho podpísaný zoznam kontrol a verdikt.

## H. Zenodo draft a post-publish kontrola

| ID | Kritérium | Aktuálny stav |
|---|---|---|
| ZR-H1 | Zenodo draft importuje presne súbory z release tagu. | `OPEN` |
| ZR-H2 | Verzia, názov, autori, ORCID, licencia, jazyky a related identifiers sú správne. | `OPEN` |
| ZR-H3 | Popis obsahuje scope, otvorené brány, changelog a Git commit/tag. | `OPEN` |
| ZR-H4 | Pred publikovaním bol skontrolovaný Zenodo preview. | `OPEN` |
| ZR-H5 | Po publikovaní sa stiahnuté súbory znovu hashujú a zhodujú s manifestom. | `OPEN` |
| ZR-H6 | Verziový DOI aj all-versions DOI fungujú a README/BibTeX sa aktualizujú. | `OPEN` |
| ZR-H7 | Publikovaný stav sa označí `FROZEN`; ďalšie zmeny patria novej verzii. | `OPEN` |

## GO pravidlo

`R3.18-DOC = GO` až keď všetky položky A–H relevantné pre DOC sú `PASS` alebo zdôvodnené `N/A`.

Otvorené fyzikálne otázky nie sú automatický NO-GO pre DOC, ak sú jasne priznané. Sú však NO-GO pre tvrdenia a predikcie, ktoré od ich uzavretia závisia.

