# Protokol aktualizácie tabuľky predpovedí a Zenodo vydania

**Dátum účinnosti:** 2026-07-14  
**Nadväzuje na:** AR5, AR9 a AR48  
**Hlavná zásada:** preukázateľne chybná publikovaná predpoveď nesmie zostať bez verejného upozornenia iba preto, že jej náhrada ešte nie je hotová

## 1. Tabuľka predpovedí je release-critical artefakt

Publikovaná tabuľka predpovedí nie je bežný pracovný súbor. Čitatelia ju môžu citovať alebo použiť na porovnanie s dátami. Materiálna zmena ľubovoľného riadku preto vstupuje priamo do rozhodnutia o novom Zenodo vydaní.

Zmena tabuľky má prednosť pred snahou čakať na veľké súhrnné vydanie, ak by čakanie ponechalo verejne aktívne číslo, o ktorom už audit preukázal, že je chybné alebo má užší rozsah.

## 2. Dva oddelené spúšťače

### PT1 — odvolanie alebo obmedzenie starej predpovede

PT1 vznikne, keď uzavretý audit preukáže aspoň jedno:

- chyba rovnice, znamienka, jednotiek, dát alebo skriptu mení výsledok;
- použitý mechanizmus alebo koľaj zomrela v rozsahu potrebnom pre predpoveď;
- číslo bolo v skutočnosti fit, toy sensitivity alebo backgroundový odhad, nie predikcia;
- stará neistota alebo interval nezahŕňali známy dominantný zdroj chyby;
- tvrdenie bolo podmienené bránou, ktorá neskôr zlyhala;
- zmenil sa rozsah tak, že starý riadok môže čitateľa materiálne zavádzať.

Pri PT1 sa **nečaká na novú hodnotu**. Vydá sa úzke `ERRATUM` alebo `DOC` vydanie, v ktorom sa stará hodnota označí:

```text
WITHDRAWN — nesmie sa používať ako aktuálna predpoveď
```

alebo

```text
SUPERSEDED IN SCOPE — platí iba v presne uvedenom historickom modeli
```

Stará verzia a jej DOI zostanú zachované. Nová verzia uvedie dôvod, audit a stav náhrady `NOT YET AVAILABLE`, ak náhrada ešte neprešla vlastnými bránami.

### PT2 — validovaná náhradná alebo nová predpoveď

PT2 vznikne, keď nová hodnota alebo interval prejde minimálne:

1. presným odvodením a deklarovaným rozsahom;
2. reprodukovateľným skriptom/výpočtom;
3. nulovým a konvergenčným testom primeraným výsledku;
4. príslušnými fyzikálnymi bránami koľaje;
5. nezávislým auditom rozhodujúceho výpočtu;
6. kontrolou, či hodnota nevznikla ladením na dáta, voči ktorým sa nazýva predikciou.

PT2 vyžaduje nové Zenodo vydanie s aktualizovanou tabuľkou. Ak ostatný veľký release nie je pripravený, vydá sa úzky `PREDICTION-TABLE UPDATE` balík s úplným changelogom a reprodukčnou stopou.

## 3. Čo je materiálna zmena riadku

Zmena je materiálna, ak nastane aspoň jedna podmienka:

1. zmení sa stav `PREDICTION`, `CONDITIONAL ESTIMATE`, `POST-DATA FIT`, `HISTORICAL` alebo `WITHDRAWN`;
2. zmení sa centrálna hodnota viac než

   `max(deklarovaná numerická tolerancia, polovica jednotky poslednej publikovanej číslice)`;

3. zmení sa interval, neistota, horný/dolný limit alebo falsifikačný prah;
4. zmení sa znamienko, poradie, kvalitatívny trend alebo kategória zhody/napätia;
5. zmení sa použitý mechanizmus, koľaj, dataset, likelihood alebo kalibrácia;
6. riadok sa pridá alebo odstráni zo zoznamu verejných predpovedí;
7. zmena môže ovplyvniť vedeckú interpretáciu alebo spôsob citovania.

Ak nebola publikovaná numerická tolerancia, každá zmena zobrazenej číslice sa považuje za materiálnu, kým audit nedokáže, že ide iba o formátovanie.

Čistá oprava medzery, fontu alebo formátu pri identickej hodnote, jednotke, statuse a význame nie je materiálna; môže čakať na patch alebo najbližší balík.

## 4. Povinné stavy každého riadku

Každý riadok budúcej tabuľky musí obsahovať alebo jednoznačne odkazovať na:

| Pole | Význam |
|---|---|
| `observable` | presne definovaná veličina |
| `value_or_interval` | hodnota, interval alebo `NOT YET AVAILABLE` |
| `status` | `PREDICTION/CONDITIONAL ESTIMATE/POST-DATA FIT/HISTORICAL/WITHDRAWN` |
| `scope` | model, koľaj, epochy a aproximácie |
| `derivation_gate` | najvyššia brána oprávňujúca dané tvrdenie |
| `frozen_inputs` | parametre, priory a verzie dát/kódu |
| `uncertainty_type` | numerická, modelová, štatistická alebo chýbajúca |
| `evidence` | audit, skript a manifest |
| `valid_from_version` | prvá verzia obsahujúca tento stav |
| `supersedes` | starý riadok/verzia, ak existuje |
| `data_exposure` | či boli rozhodujúce dáta známe pred zmrazením |

## 5. Predikcia verzus post-data výsledok

Ak sa hodnota upravila po pozretí na cieľové dáta, smie byť publikovaná, ale nie pod statusom `PREDICTION`. Dostane status `POST-DATA FIT` alebo `CONDITIONAL ESTIMATE` a presne uvedie použité dáta.

Novou predikciou sa môže stať až hodnota zmrazená pred nezávislou budúcou dátovou skúškou alebo hodnota odvodená bez ladenia na porovnávaný dataset.

Toto pravidlo umožňuje rýchlo zverejniť opravený najlepší odhad bez jeho nesprávneho vydávania za predikciu.

## 6. Časový protokol proti zbytočnému odkladu

### Po PT1 — chyba starej predpovede

- do 3 pracovných dní: založiť verejný pracovný erratum záznam v kanonickom Git repozitári a označiť riadok `WITHDRAWAL PENDING RELEASE`;
- bez zbytočného odkladu, cieľ najneskôr do 14 kalendárnych dní: publikovať úzke Zenodo erratum alebo novú DOC verziu;
- ak technická release brána do 14 dní neprejde, doplniť na starý Zenodo záznam verejnú metadata poznámku odkazujúcu na audit a pripravovanú opravu; poznámka sa zapíše do metadata changelogu;
- úplná náhradná hodnota môže prísť neskôr cez PT2.

### Po PT2 — validovaná nová hodnota

- okamžite zaradiť riadok do zmrazeného release candidate;
- cieľ najneskôr do 30 kalendárnych dní od finálneho auditného PASS publikovať nové Zenodo vydanie;
- ak veľký balík nie je pripravený, vytvoriť úzky prediction-table update namiesto čakania.

Tieto lehoty sú operačné ciele, nie povolenie obísť manifest, Git tag, changelog alebo audit. Nesplnenie cieľa sa označí `OVERDUE` s verejne zapísaným dôvodom.

## 7. Verzia pri zmene tabuľky

- materiálna zmena predikčnej tabuľky nikdy nie je patch `3.x.y`;
- pri nezmenenom fundamente dostane novú minor verziu `3.x`;
- ak nová predpoveď vyžaduje zmenu fundamentu, patrí do `4.0`;
- čisto typografická oprava bez zmeny hodnoty a významu môže byť patch alebo súčasť nasledujúceho vydania.

## 8. Povinný changelog riadku

Každá materiálna zmena musí uviesť:

```text
OLD VALUE/STATUS
NEW VALUE/STATUS
WHY IT CHANGED
WHICH AUDIT PROVED THE CHANGE
WHETHER TARGET DATA WERE ALREADY KNOWN
WHICH VERSION/DOI SUPERSEDES THE OLD ROW
```

Historické hodnoty sa nemažú. V novej tabuľke môžu byť presunuté do historickej sekcie s odkazom na pôvodný verziový DOI.

## 9. Aplikácia na v3.18

Pred `R3.18-DOC` sa musí vykonať riadkový audit celej publikovanej tabuľky v3.17:

1. `STILL CURRENT` — hodnota a dôkazový status zostávajú;
2. `SCOPE NARROWED` — číslo zostáva iba historickým/conditional odhadom;
3. `WITHDRAWN` — audit ukázal, že sa nesmie používať;
4. `REPLACEMENT VALIDATED` — existuje nová auditovaná hodnota;
5. `RECALCULATION OPEN` — stará hodnota je odvolaná, nová ešte nie je hotová.

R3.18-DOC nesmie automaticky kopírovať starú predikčnú tabuľku bez tohto riadkového rozsudku.

