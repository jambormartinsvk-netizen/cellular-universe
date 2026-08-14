# Návrh V2 — stanice, cesty koľají a viac-kolové audity

Dátum: 2026-07-15  
Stav: odporúčaný model na schválenie pred vytvorením a migráciou  
Nahrádza organizačný význam návrhu V1; inventár počtov a závislostí z V1 zostáva platný

## Mentálny model

- `A1`, `A2`, `A3`, ... sú **kontrolné stanice**.
- `A1K1`, `A2K4`, ... sú **koľaje zvolené na konkrétnej stanici**.
- cesta je usporiadaný prefix koľají, napríklad `A1K1 → A2K4 → A3K2`;
- cesta môže zastaviť na ktorejkoľvek stanici;
- stanica prejde iba vtedy, keď aspoň jedna jej koľaj prejde všetkými povinnými bránami danej stanice;
- ak všetky koľaje na stanici zomrú, zomiera príslušný prefix cesty a ďalšia stanica sa nedosiahne;
- podkoľaje ako K7a/K7b/K7c sú vnútorné pokusy koľaje na tej istej stanici, nie nové stanice.

## Primárny strom ciest

```text
tracks/
├── 00_READ_FIRST.md
├── 00_ROUTE_REGISTER.md
├── A1/
│   ├── 00_STATION.md
│   ├── PASS/
│   ├── REVIEW/
│   ├── STOP/
│   ├── AUDIT_THREADS/
│   ├── A1K1/
│   │   ├── 00_TRACK.md
│   │   ├── 00_CURRENT_DECISION.md
│   │   ├── PASS/
│   │   ├── REVIEW/
│   │   ├── STOP/
│   │   ├── HISTORY/
│   │   ├── AUDIT_THREADS/
│   │   ├── ARTIFACTS/
│   │   └── A2/
│   │       ├── 00_STATION.md
│   │       ├── 00_ROUTE_PREFIX.md
│   │       ├── PASS/
│   │       ├── REVIEW/
│   │       ├── STOP/
│   │       ├── AUDIT_THREADS/
│   │       ├── A2K1/
│   │       ├── A2K2/
│   │       ├── A2K3/
│   │       ├── A2K4/
│   │       │   ├── 00_TRACK.md
│   │       │   ├── 00_CURRENT_DECISION.md
│   │       │   ├── PASS/ REVIEW/ STOP/ HISTORY/
│   │       │   ├── AUDIT_THREADS/
│   │       │   ├── ARTIFACTS/
│   │       │   ├── SUBTRACKS/
│   │       │   └── A3/               # vznikne až po PASS stanice A2
│   │       ├── A2K5/
│   │       ├── ...
│   │       ├── A2K12/
│   │       └── CROSS_ROUTE_LINKS/
│   └── A1K2/
│       └── A2/
│           └── A2K10/
└── STATION_CATALOG/
    ├── A1/
    ├── A2/
    ├── A3/
    └── ...
```

Primárna auditovateľná cesta je fyzicky vnorená: `A1/A1K1/A2/A2K4/...`. `STATION_CATALOG` obsahuje iba všeobecné definície brán a mechanizmov použiteľné vo viacerých cestách; výsledky závislé od predchádzajúcej koľaje patria do konkrétneho prefixu cesty.

## Stanica verzus koľaj

### Adresár stanice

`A2/00_STATION.md` definuje brány, ktoré musí na A2 prejsť každá koľaj: povinné rovnice, nulové limity, stabilita, constrainty, konvergencia, observačné brány a stop kritériá. `A2/PASS` obsahuje rozhodnutie, ktorá konkrétna koľaj umožnila pokračovať na A3. `A2/STOP` vznikne iba vtedy, keď sú všetky koľaje pre daný route prefix mŕtve.

### Adresár koľaje

`A2K4/00_TRACK.md` definuje mechanizmus ľudskou rečou, rozdiel od súrodencov, ktoré dôvody smrti starších koľají odstraňuje, aktuálnu maximálnu hĺbku, podkoľaje a dôkazy. Ak A2K4 zomrie, jej `STOP` nemení automaticky stav A2, pokiaľ žije iná A2 koľaj.

### Ďalšia stanica

Adresár `A3/` sa označí ako `REACHED` iba na route prefixe, ktorý prešiel A2. Pri mŕtvej A2K4 sa do A2K4 nevytvára falošný A3 PASS; terminálny dokument uvedie `STOP_AT_STATION: A2`.

## A2-K10 a správny route prefix

Aktuálny audit označuje A2-K10 ako odlišnú backgroundovú vetvu A1-K2. Jej kanonická cesta má byť `A1/A1K2/A2/A2K10`, nie `A1/A1K1/A2/A2K10`. V indexe A1-K1/A2 zostane viditeľný odkaz, ale nie duplicitný artefakt. Ak neskorší audit preukáže, že K10 je platná aj pre A1-K1, vznikne samostatná route-conditioned inštancia s vlastným auditom.

## Vnútorné podkoľaje A2-K4

Podkoľaje zostanú na stanici A2:

```text
A2K4/SUBTRACKS/
├── CORE_SUPERHORIZON/
├── K4_1/
├── K4_2/
├── K4_3a/
├── K4_3b_RG/
│   ├── BR1/
│   ├── BR2/
│   └── BR3/
│       ├── BR3A/
│       ├── BR3B/BR3B1...BR3B2g/
│       └── BR3C/BR3C_a...BR3C_c/
└── C7_7c/
    ├── K1...K6/
    └── K7/
        ├── SHARED_K7B_K7C/
        ├── K7a_PROJECTED_JACOBIAN/
        ├── K7b_CONSTRAINTS/K7b1...K7b3b_P0/
        ├── K7c_EVOLUTION/K7c1...K7c3d_P2/
        └── K7d_FULL_ACTIVITY/
```

Každá podkoľaj má rovnaké `PASS/REVIEW/STOP/HISTORY/AUDIT_THREADS/ARTIFACTS`. Smrť podkoľaje sa nezovšeobecní na rodiča, kým nie sú mŕtve všetky podkoľaje rodičovskej vetvy.

## Viac-kolový auditný dialóg

Jeden audit nemusí byť konečný. Každá nezávislá auditná diskusia dostane vlastný nemenný thread:

```text
AUDIT_THREADS/
└── T001_FABLE5_K7C_P1/
    ├── 00_SCOPE_AND_PARTICIPANTS.md
    ├── 00_CURRENT_THREAD_STATUS.md
    ├── ROUND_01/
    │   ├── 01_AUDIT.md
    │   ├── 02_RESPONSE.md
    │   ├── 03_EVIDENCE_MANIFEST.md
    │   └── 04_OPEN_POINTS.md
    ├── ROUND_02/
    │   ├── 01_REAUDIT.md
    │   ├── 02_RESPONSE.md
    │   ├── 03_EVIDENCE_MANIFEST.md
    │   └── 04_OPEN_POINTS.md
    ├── ROUND_03/
    │   └── ...
    ├── 90_THREAD_SUMMARY.md
    └── 99_THREAD_DECISION.md
```

Pravidlá:

1. Starý audit ani odpoveď sa neprepisujú; ďalší krok je nové číslo kola.
2. Každé tvrdenie auditu má stabilné ID, napríklad `T001-R02-F03`.
3. Odpoveď musí pri každom ID uviesť `ACCEPTED`, `PARTIALLY_ACCEPTED`, `REJECTED_WITH_EVIDENCE` alebo `OPEN`.
4. Každé kolo má manifest skriptov, vstupov, výstupov a SHA-256.
5. `99_THREAD_DECISION.md` môže byť `PASS`, `REVIEW`, `STOP` alebo `CONFLICT`; neprepisuje rozhodnutie celej koľaje bez samostatného rozhodovacieho záznamu.
6. Viac auditorov znamená viac threadov. Konflikt medzi auditmi sa rieši samostatným adjudikačným threadom, nie vymazaním jedného auditu.
7. `00_CURRENT_THREAD_STATUS.md` je navigačný súhrn; nemenné kolá sú autoritatívny dôkaz.

## Rozhodnutia a ich história

Každý uzol má:

```text
00_CURRENT_DECISION.md
PASS/D001_....md
REVIEW/D002_....md
STOP/M009_....md
HISTORY/LIMITATIONS/D001_LIMITED_BY_D003.md
```

Ak neskorší audit obmedzí starý PASS, pôvodný súbor zostane. Nový dokument uvedie presný rozsah obmedzenia, dôvod, nové dôkazy a nový aktuálny verdikt. `00_CURRENT_DECISION.md` odkazuje na najnovšie platné rozhodnutie.

## Artefakty

```text
ARTIFACTS/
├── 00_MANIFEST.md
├── scripts/
├── results/
├── audits/
├── responses/
└── questions/
```

Skript alebo výsledok má jediného vlastníka. Artefakt spoločný viacerým podkoľajam patrí do najbližšieho spoločného `SHARED` uzla. Route-conditioned výsledok sa nesmie zameniť za všeobecný výsledok rovnako pomenovanej koľaje na inom backgrounde.

## Register ciest

`00_ROUTE_REGISTER.md` obsahuje jeden riadok na každý route prefix:

| Route ID | Cesta | Posledná dosiahnutá stanica | Aktuálna koľaj | Stav | Max. hĺbka | Terminálny dôvod | Ďalší krok |
|---|---|---|---|---|---:|---|---|
| `R-A1K1-A2K4` | `A1K1 → A2K4` | A2 | A2K4/K7c | REVIEW | 66.5 | — | P2 `M'` ledger |
| `R-A1K1-A2K1` | `A1K1 → A2K1` | A2 | A2K1 | STOP | 45.0 | M-009 | neotvárať bez nového mechanizmu |

Route ID sa rozšíri až po dosiahnutí ďalšej stanice. Vďaka tomu bude viditeľné, či cesta skončila na A1, A2 alebo neskôr.

## Migračné poradie

1. Zmraziť flat stav SHA-256 a Git baseline commitom.
2. Vytvoriť iba strom, indexy, route register a audit-thread šablóny; nič nepresúvať.
3. Priradiť každý existujúci artefakt práve jednému route/station/subtrack uzlu.
4. Ručne overiť všetky `SHARED` a cross-route položky.
5. Až potom presúvať MD/JSON a aktualizovať odkazy cez `OLD_PATH → NEW_PATH` mapu.
6. Skripty presúvať po závislostných komponentoch; historický obsah nemeníť.
7. Po každom balíku spustiť iba organizačné brány: broken links, dependency graph, SHA, `py_compile`, corpus checker.
8. Fyzikálne regresie spustiť oddelene po predregistrácii.

## Odporúčanie

Ako prvú implementáciu vytvoriť neinvazívny strom pre existujúci route prefix `A1K1 → A2`, všetkých A2 kandidátov a detail A2K4. Naplniť ho manifestmi odkazujúcimi na dnešné ploché cesty. Po ručnom potvrdení, že route a station model zodpovedá zamýšľanej teórii, pokračovať fyzickou migráciou.

## Dodatok V2.1 — povinný HISTORY, váhy výsledkov a spoločné jadro

### Povinný obsah HISTORY

HISTORY nie je odkladisko starých kópií, ale append-only časová os uzla:

~~~text
HISTORY/
├── 00_EVENT_LEDGER.md
├── DECISIONS/
├── SCORE_CHANGES/
├── LIMITATIONS/
├── SUPERSESSIONS/
└── PATH_AND_NAME_CHANGES/
~~~

Každá udalosť má stabilné ID, čas, route/node ID, predchádzajúci a nový stav,
predchádzajúce a nové skóre, spúšťací audit alebo otázku, dôvod, dotknuté
claimy, odkazy a SHA-256 dôkazov. Starý záznam sa neopravuje; oprava je
ďalšia udalosť s väzbou CORRECTS. Aktuálny súhrn sa môže prepisovať ako
navigácia, ale autoritatívne udalosti sú nemenné. Rovnaký HISTORY kontrakt
platí pre stanicu, koľaj, podkoľaj, auditný thread aj verziu spoločného jadra.

### Váhy výsledkov a scorecard

Každý uzol má 00_SCORECARD.md. Pred výpočtom sa výsledok priradí práve jednej
verziovanej gate s váhou. Váhy v jednom scorecarde majú súčet 100 a nesmú sa
meniť po výsledku bez novej verzie a zápisu v HISTORY/SCORE_CHANGES. Viac
korelovaných monitorov toho istého claimu nezískava viacnásobnú váhu.

Scorecard oddelene uvádza validovanú podporu z PASS, blokujúcu evidenciu z
autoritatívneho FAIL, otvorenú alebo technickú váhu a auditované pokrytie
PASS+FAIL. Tieto čísla nie sú pravdepodobnosť pravdivosti a bez crosswalku sa
nesčítajú s historickou jemnou hĺbkou. Pre C7.7c je prvým návrhom C7-W1 v
Audit/A2_K4_C7_7C_K1_K7_LINEAGE_GATE_COVERAGE_AND_WEIGHT_AUDIT_2026-07-15.md.

### Verziované baseScripts a externé audity

Spoločný vykonateľný kód sa postupne extrahuje do nemenných verzií
scripts/baseScripts/vNNN. Konkrétna koľaj volá jadro cez manifest s presnou
verziou a hashmi. Oprava vytvorí novú verziu a nové výsledky; nesmie spätne
meniť historické výpočty. Autoritatívny návrh je
Questions/BASESCRIPTS_VERSIONED_ARCHITECTURE_AND_MIGRATION_2026-07-15.md.

Externé audity používajú route-conditioned export s hashovanými vstupmi,
očakávaniami, kódom, surovými dôkazmi a nemennými viac-kolovými odpoveďami.
Pilot pre K7c P1 je definovaný v
Questions/EXTERNAL_AUDIT_PACKAGE_STANDARD_AND_K7C_RK4_PILOT_2026-07-15.md.

### Doplnené migračné poradie

1. V prvej neinvazívnej fáze vytvoriť aj HISTORY, scorecardy a audit-thread šablóny.
2. Pilotne extrahovať iba K7c P1 do baseScripts/v001 a preukázať paritu so skriptom 197.
3. Fyzikálne regresie spúšťať oddelene po predregistrácii a uložiť ich ako nové historické udalosti.