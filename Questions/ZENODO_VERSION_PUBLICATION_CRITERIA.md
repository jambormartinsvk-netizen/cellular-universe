# Kritériá pre aktualizáciu a publikovanie verzií na Zenodo

**Dátum účinnosti:** 2026-07-14  
**Nadväzuje na:** AR5 a AR9  
**Zásada:** vydanie sa riadi vedeckou udalosťou a pripravenosťou, nie kalendárom ani počtom nových súborov

## 1. Kedy novú verziu vydať

Nová verejná verzia je oprávnená iba vtedy, keď platí aspoň jeden spúšťač P1–P5 a súčasne prejde celý príslušný release checklist.

### P1 — kritická oprava publikovaného tvrdenia

Nová verzia je povinná, ak audit zmení alebo odvolá publikované:

- číslo alebo predikciu;
- rovnicu alebo znamienko s fyzikálnym dôsledkom;
- stav `PREŽÍVA/MŔTVA/VYBRANÁ`;
- rozsah platnosti výsledku;
- tvrdenie o fitovaní, predikcii alebo štatistickej významnosti;
- reprodukčný skript, ktorého chyba mení výsledok.

Takáto oprava sa nemá odkladať iba preto, že ostatné časti teórie sú otvorené. Vydá sa úzko ohraničené opravné vydanie s erratom.

### P2 — uzavretý vedecký míľnik

Nová verzia je oprávnená, keď sa zmení kanonický verejný stav hlavnej vetvy, napríklad:

- primárna A1 koľaj prejde alebo definitívne zomrie;
- aspoň jedna A2 koľaj uzavrie G7 a môže prejsť do A3;
- vznikne alebo zomrie predtým verejne preferovaný mikrofyzický mechanizmus;
- uzavrie sa zásadná otázka Q4, Q8, Q18/Q23 alebo iný cieľ deklarovaný pre vydanie;
- dokončí sa nezávisle reprodukovateľný modelový balík.

Samotný intra-gate checkpoint alebo zmena jemnej hĺbky o `0,1–1,0` bodu nie je míľnik na Zenodo.

### P3 — koherentné dokumentačné/auditné vydanie

Nová verzia je oprávnená, ak vznikol stabilný a citovateľný auditný snapshot, ktorý:

- opravuje verejný obraz staršej verzie;
- obsahuje jednotný stav, register otázok, mŕtve koľaje a ich dôvody;
- nemení otvorené hypotézy na predikcie;
- je užitočný ako samostatný citable release.

Toto je plánovaný rozsah `R3.18-DOC`.

### P4 — zmrazenie pred novej externou dátovou skúškou

Pred použitím nového datasetu alebo pred zverejnením dát, voči ktorým sa má tvrdenie považovať za predikciu, sa vydá predregistračný snapshot iba vtedy, keď sú vopred zmrazené:

- rovnice a implementácia;
- parametre a priory;
- dataset/likelihood plán;
- kill thresholds;
- predikčné tabuľky a kontrolné súčty.

Neuzavretá pracovná hypotéza sa nevydáva ako predikcia iba kvôli časovej pečiatke.

### P5 — reprodukčná alebo softvérová zmena meniaca vedecký výsledok

Nová verzia je povinná, ak zmena kódu, knižnice, solvera, dát alebo pipeline mení publikované výstupy nad deklarovanú toleranciu. Čisté zrýchlenie alebo refaktor s bitovo/numericky ekvivalentným výsledkom sa zhromaždí do ďalšieho plánovaného vydania.

## 2. Kedy novú verziu nevydávať

Samostatný Zenodo release nespúšťa:

- nová otvorená otázka bez výsledku;
- vznik pracovnej podkoľaje;
- technický timeout alebo neuzavretý beh;
- jediný smoke test, toy model alebo citlivostný grid;
- desatinný posun hĺbky vnútri otvorenej brány;
- syntaktická oprava skriptu bez zmeny výsledku;
- zrýchlenie interpolácie alebo solvera bez zmeny vedeckého výstupu;
- priebežné pridanie auditného súboru;
- upratanie ciest, kým nie je dokončený celý konzistentný balík.

Tieto zmeny sa zachovajú v Git histórii a pracovnom changelogu a vydajú sa spoločne pri najbližšom platnom spúšťači.

## 3. Typ čísla verzie

### Patch: `3.x.y`

Použiť iba ak sa nemení:

- fyzikálny význam rovníc;
- číselný výsledok;
- stav koľaje;
- rozsah tvrdenia;
- záver alebo predikčná tabuľka.

Príklady: preklep v súbore, nefunkčný interný odkaz, chýbajúci nevedecký súbor v balíku, oprava formátu citácie.

### Nová minor verzia `3.x`

Použiť pri každej materiálnej vedeckej alebo auditnej zmene tej istej fundamentálnej teórie:

- opravená/obmedzená rovnica alebo tvrdenie;
- zmena čísla, rozsudku alebo dôkazovej úrovne;
- nový uzavretý auditný míľnik;
- nový reprodukčný balík;
- nové predikcie po prejdení príslušných brán.

Plánované `v3.18` je minor dokumentačné/auditné vydanie, nie patch v3.17.

### Major verzia `4.0`

Použiť pri zmene fundamentu podľa auditu hranice v4. Nové pomocné pole alebo mediátor automaticky neznamená v4, ak zostáva explicitne efektívnym uzáverom. Verziu 4 vyžaduje jeho prijatie ako nového základného postulátu alebo zmena jadrového zákona teórie.

## 4. Metadáta bez novej verzie

Bez novej verzie možno meniť iba nesémantické metadáta pri nezmenených súboroch, napríklad:

- oprava ORCID/ROR;
- kľúčové slovo;
- nevedecký kontaktný odkaz;
- nastavenie default preview alebo viditeľnosti.

Každá taká zmena sa zapíše do metadata changelogu s dátumom, starou a novou hodnotou.

Zmena názvu, poradia/totožnosti autorov, abstraktu s vedeckými tvrdeniami, verzie, licencie, publikovaného rozsahu alebo citačného významu sa nepovažuje za nesémantickú. Musí byť verejne zdokumentovaná a pri zmene vedeckého významu dostane novú verziu.

## 5. Release triedy

| Trieda | Účel | Povinné fyzikálne brány |
|---|---|---|
| `ERRATUM` | opraviť/odvolať konkrétne staré tvrdenie | iba brány potrebné na preukázanie opravy; ostatné otvorené otázky sa priznajú |
| `DOC` | stabilný auditný a dokumentačný snapshot | konzistencia tvrdení a dôkazových úrovní; nemusí uzavrieť otvorenú fyziku |
| `PHYS` | nové rovnice/mechanizmus v presne obmedzenom rozsahu | všetky fyzikálne brány potrebné pre dané tvrdenie |
| `PREDICTION` | nové alebo zmenené kozmologické predikcie | A2/G7, vlastná A3/G8 a predregistrovaný dátový protokol; pre likelihood aj G9 |
| `MAJOR` | nový fundament | nové brány verzie 4 definované pred výpočtami |

## 6. GO/NO-GO princíp

Release candidate je `GO` iba ak:

1. má platný spúšťač P1–P5;
2. má správne číslo a release triedu;
3. všetky povinné položky checklistu sú `PASS` alebo výslovne `NOT APPLICABLE` s dôvodom;
4. release auditor podpíše zmrazený kandidát;
5. Zenodo balík je bitovo totožný s označeným Git tagom.

Ak sa po vytvorení manifestu zmení ľubovoľný súbor balíka, kandidát sa vracia do `DRAFT`, vytvorí sa nový manifest a opakuje audit.

## 7. Politika frekvencie

Nie je stanovený minimálny ani maximálny počet dní medzi vydaniami. Platí event-driven politika:

- kritické erratum sa vydá bez zbytočného čakania po prejdení opravnej brány;
- normálne malé zmeny sa balia do jedného koherentného vydania;
- verzia sa nevydáva iba preto, že od poslednej uplynul čas;
- verzia sa neodkladá, ak by starý verejný výsledok mohol byť naďalej chybne citovaný.

