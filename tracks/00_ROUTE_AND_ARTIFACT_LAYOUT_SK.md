# Kanonický poriadok koľají, skriptov a dôkazov

**ID:** `ORG-V2-P1-CANONICAL-LAYOUT`  
**Aktualizované:** 2026-07-16  
**Stav:** aktívny organizačný kontrakt; nemení fyziku ani staré verdikty

## Dve vrstvy bez kopírovania

1. `tracks/` je navigačná a rozhodovacia vrstva. Každá koľaj má vlastný
   stav, plán, manifest, históriu a auditné thready.
2. `scripts/`, `scripts/results/`, `Audit/`, `Questions/` a
   `Independent_Audits/` sú kanonické úložiská existujúcich artefaktov.
3. `theory/` je konsolidovaná release/release-candidate vrstva. Nový
   pracovný stav, otázka ani metodické pravidlo sa tam priebežne nezapisujú.

Jeden historický súbor má jednu fyzickú cestu a jedného vlastníka. Koľaj naň
odkazuje plnou cestou; nekopíruje ho do svojho adresára. Dôvodom je najmenej
468 historických väzieb, vrátane `Path(__file__).with_name(...)`, hashov a
auditných citácií.

## Povinný obsah koľaje

```text
TRACK/
├── 00_TRACK.md                 # ľudský mechanizmus a aktuálny stav
├── 00_WORK_PLAN.md             # iba aktívna/REVIEW koľaj
├── 00_CURRENT_DECISION.md      # posledné rozhodnutie a jeho rozsah
├── ARTIFACTS/00_MANIFEST.md    # runner → base → result → audit
├── BASE/00_BASE_DEPENDENCIES.md
├── AUDIT_THREADS/00_REGISTER.md
├── HISTORY/00_EVENT_LEDGER.md
├── PASS/
├── REVIEW/
├── STOP/
└── 05_RULE_AND_QUESTION_CANDIDATES_SK/EN.md  # iba skutočná AR/Q/L delta
```

Prázdny adresár nie je dôkaz. Ak zatiaľ nemá samostatný dokument, manifest
uvedie `NONE` alebo odkaz na centrálny historický audit.

Pri malom alebo mŕtvom uzle môže `00_TRACK.md` niesť aj aktuálne rozhodnutie
a `ARTIFACTS/00_MANIFEST.md` register auditov. Samostatné decision buckets a
`AUDIT_THREADS/` sa vytvoria až pri prvom route-local rozhodnutí alebo
viackolovom audite; nevytvárajú sa desiatky prázdnych README. Aktívny
komplexný uzol A2-K4/P5 ich má oddelené.

Voliteľný lokálny pár `05_RULE_AND_QUESTION_CANDIDATES_*` obsahuje iba
pracovné delty a nevzniká pri každom skripte alebo zmene stavu. Všeobecné
metodické delty patria do `tracks/METHODOLOGY/`. Povýšenie do `theory/`
upravuje AR70.

## Jediný zdroj pravdy

- fyzikálny stav: `00_CURRENT_DECISION.md` a najnovší autoritatívny audit;
- pracovný plán: najnižší aktívny `00_WORK_PLAN.md`;
- kód vzorca: pinovaný base modul alebo historický runner;
- technická použiteľnosť: `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md`;
- výsledok: immutable JSON/MD na pôvodnej ceste;
- história obmedzení: append-only `HISTORY/00_EVENT_LEDGER.md`.

Pri konflikte má fyzikálne odvodenie a novší scope-limiting audit prednosť
pred navigačným súhrnom. Starý súhrn sa nevymaže; HISTORY vysvetlí zmenu.

## Manifest jedného behu

Každý nový beh musí mať jeden riadok s týmito väzbami:

`route/gate → preregistračný MD → runner → base moduly+SHA → vstupy → raw výsledok → audit → stav`.

Číselný prefix skriptu nie je jedinečný; identifikátorom je celý názov a
SHA-256. Stav `PASS_SCRIPT` nesmie nahradiť `PASS_PHYSICS`.

## Base architektúra

Spoločný vzorec patrí do malého modulu s explicitnými vstupmi a bez skrytého
globálneho stavu. Runner obsahuje iba parametre konkrétnej koľaje, limity,
serializáciu a volanie modulu. Oprava nevytvorí mutable `latest`, ale novú
verziu/hash a zoznam všetkých dotknutých manifestov.

## Migračné hranice

Táto fáza nič fyzicky nepresúva. Fyzická migrácia je povolená až po Git
baseline, úplnom `OLD_PATH → NEW_PATH` manifeste, kontrole hashov a všetkých
závislostných komponentov. Dovtedy sú nové adresáre kontrolovateľné indexy.

Metodika: AR59, AR61, AR62, AR66.1, AR66.2 a AR69.
