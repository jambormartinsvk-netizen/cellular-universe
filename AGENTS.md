# Projektové pravidlá pre agentov — Teória

Tento súbor je záväzný pre hlavného agenta aj všetky projektové roly. Chat,
kompresný súhrn ani počet vytvorených dokumentov nie sú autoritatívny stav.

## 1. Autorita

- Martin Jambor je autor teórie a jediný rozhoduje o nových fyzikálnych
  vstupoch, o povolení ďalšej desaťchybovej dávky a o tom, či závažný
  auditný nález vedie k oprave tej istej koľaje, novej koľaji alebo jej
  ukončeniu.
- Hlavný orchestrátor je jediný projektový zapisovateľ autoritatívneho
  `PASS/REVIEW/STOP`, skóre, hĺbky a povolenia official runu.
- Špecializovaná rola vydáva iba odporúčanie vo svojom rozsahu.
- Autor release-candidate artefaktu nesmie byť jeho jediným auditorom.
- Kurátor externého balíka nesmie auditovať vlastný balík.
- Paralelne môžu pracovať najviac traja špecialisti bez prekrývajúcich sa
  write scopes.

## 2. Povinný jadrový bootstrap

Po otvorení novej úlohy, po kompresii a pred prvým zápisom načítaj:

1. `tracks/00_PROJECT_OPERATING_SYSTEM.md`;
2. `tracks/00_CURRENT_EXECUTION_PLAN.md`;
3. `tracks/00_READ_FIRST.md`;
4. najnižší route-local work plan a aktívny handoff kapsul;
5. `tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md`.

Ak chýba povinný súbor, nesedí zmrazený hash alebo nie je jednoznačný
`ALLOWED_NEXT_ACTION`, stav je `HANDOFF_OR_RULESET_DRIFT_REVIEW`: nič
nespúšťaj a nič neinterpretuj ako vedecký výsledok.

### 2.1 Fázovo primerané Python/compute čítanie

Pred tvorbou alebo DEV testom artefaktu načítaj iba:

1. exact názov kandidáta v `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md`;
2. `scripts/00_KNOWN_PYTHON_ERROR_PATTERNS.md`;
3. `scripts/00_EXECUTION_TIME_LIMITS.md`;
4. príslušný route-local error-batch stav;
5. pri base module aj `scripts/baseScripts/00_MODULE_OWNERSHIP_REGISTER.md`
   a `scripts/baseScripts/00_VERSION_REGISTER.md`.

Celý `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` je historický forenzný
register. DEV autor ani RC auditor ho nečíta celý. Vyhľadá iba záznamy
relevantné k menenému mechanizmu, knižnici, formátu alebo chybovej triede.
Tým sa zachová prevencia bez opakovanej analýzy desiatok nesúvisiacich chýb.

Pred official runom sa navyše overí exact celý názov RC v živom DNR,
zmrazené hashe contract/source/input a relevantné PF záznamy. Historický
checker s `NOT_IN_QUARANTINE` nie je povolenie spustiť artefakt.

Pred prípravou alebo auditom externého balíka načítaj
`External_Audits/00_AUDITOR_PACKAGE_PROTOCOL_SK.md`.

Výnimka nezávislosti: `external_auditor` číta iba sealed package a pravidlá
pribalené v ňom. Chýbajúci ruleset označí ako package-closure blocker.

## 3. Dvojfázový výpočtový workflow

Písanie zdroja nie je povolenie official runu. Workflow má dve oddelené
zóny:

```text
VEDECKÝ CONTRACT/DRAFT
  -> DEV_SANDBOX
     edit rovnakého pracovného súboru
     py_compile/help/synthetic unit/selftest
     bez reálnych vedeckých vstupov, siete, official outputu a verdiktu
  -> DEV_TESTS_PASS
  -> RC_FREEZE
     finálny vedecký contract + source/input SHA + absent-output guard
  -> INDEPENDENT_STATIC_MATH_AUDIT
  -> OFFICIAL_RUN_PRESNE_RAZ
  -> INTERNAL_SCIENCE_AUDIT
  -> ORCHESTRATOR_DECISION
  -> MILESTONE_PROGRESS_REVIEW
  -> EXTERNAL_T2/T3 iba pri ucelenom vedeckom míľniku
```

### 3.1 DEV_SANDBOX

- DEV používa jeden stabilný pracovný base/runner. Bežná oprava nevytvára
  nový prereg, successor, audit, DNR záznam ani Markdown dokument.
- Povolené sú iba offline technické testy nad syntetickými fixtures.
- DEV výstup nesmie byť citovaný ako fyzikálny dôkaz a nesmie zapisovať do
  official cieľov.
- Autor môže v explicitnom capsule spustiť povolené DEV testy s timeoutom;
  nesmie vykonať official vetvu ani auditovať vlastný RC.
- Po každej oprave sa pridá alebo zachová regresný test pre danú chybu.

### 3.2 RC a official

- RC vzniká až po technicky čistom DEV suite; presný source hash sa zmrazí.
- Nezávislý `math_script_auditor` kontroluje exact RC, rovnice, znamienka,
  jednotky, stavové poradie, guardy, provenienciu a rozhodovacie vetvy.
- Po auditnom PASS odporúčaní hlavný orchestrátor môže povoliť bounded
  official run. Official výstup sa publikuje presne raz do neprítomného
  cieľa; kolízia alebo zlyhanie je fail-closed.
- Technická chyba nie je fyzikálny výsledok. Fyzikálny záver vzniká až z
  kompletného rawu a nezávislého interného vedeckého auditu.

## 3.3 Stanica A0 je upstream od každého vedeckého atómu

Od 2026-08-14 platí: **žiadny nový vedecký atóm v `A2` ani `A3` sa neotvára,
kým nie je rozhodnutá stanica `A0`** (`tracks/A0/00_STATION.md`).

Dôvod je fyzikálny, nie procesný. Externý audit 2 (13. 8. 2026, Časť III.5)
ukazuje, že jednosmyčková radiačná korekcia generuje na Poisson–Delaunay sieti
dim-4 narušenie Lorentza 14–22 rádov nad experimentálnymi limitmi. Ak to
platí, sú `A2-K4` aj všetkých päť backupov bezpredmetné. Mapa staníc túto
otázku doteraz neobsahovala.

Povolené počas zmrazenia `A2`:

- práca na koľajach `A0-K1..K5`;
- read-only čítanie a citovanie existujúcich `A2` artefaktov;
- operácie bez contractu podľa §10;
- oprava procesných a release nálezov auditu (git tag, README, preklasifikácia
  predikcií, zaokrúhlenie falošnej precíznosti).

Zakázané počas zmrazenia `A2`:

- nový task, prereg, RC, official run ani podkoľaj v `A2`;
- zjemnenie špecifikácie `P5.3` blockeru v akejkoľvek forme;
- akékoľvek nové CMB-normalizované číslo.

## 4. Chybový rozpočet — patrí fyzikálnej otázke, nie podkoľaji

**Zmena 2026-08-14 (audit 2, V.5).** Pôvodné pravidlo viazalo rozpočet
`0..10` na implementačnú líniu. Dôsledok bol nezamýšľaný a mechanický:
rozpočet sa obnovoval tým, že sa problém rozdelil. Sedemnásť podkoľají
`D2SW0…D2SW16` znamenalo až 170 chybových slotov na jednu otázku. Pravidlo,
ktoré malo terminovať, umožňovalo neterminovať.

Od tejto revízie platí:

```text
QUESTION_ID                    fyzikalna otazka, nie podkolaj
QUESTION_ERROR_BUDGET = 30     spolocny pre VSETKY podkolaje otazky
QUESTION_ERRORS_USED  = 0..30
QUESTION_STATUS       = OPEN | RESOLVED | NO_GO_BY_EXHAUSTION
```

1. **Delenie problému rozpočet nezvyšuje.** Nová podkoľaj, nový adresár, nový
   task counter ani nová implementačná línia neotvárajú nový batch. Dedia
   `QUESTION_ID` rodiča a čerpajú z jeho rozpočtu.
2. Vnútri otázky sa naďalej vedie desaťchybová dávka ako operatívna brána
   (§4.2). Pri `10/10` vzniká `TECHNICAL_PERMISSION_GATE` a čaká sa na
   Martina — ale povolenie ďalšej dávky čerpá z `QUESTION_ERROR_BUDGET`.
3. Pri `QUESTION_ERRORS_USED = 30` sa otázka uzavrie ako
   **`NO_GO_BY_EXHAUSTION`** s presným zoznamom toho, čo sa skúšalo, aké boli
   spoločné príčiny a čo zostáva neoverené. **To je legitímny vedecký výsledok
   a je publikovateľný**, nie zlyhanie.
4. Otázka sa smie znovu otvoriť iba s novým fyzikálnym vstupom od Martina —
   nie s novou implementáciou tej istej veci.

Aktívne registrované otázky a ich rozpočty žijú v
`tracks/00_CURRENT_EXECUTION_PLAN.md`, jeden riadok na otázku.

### 4.1 HRUBÝ_KANDIDÁT_FIRST

**Zavedené 2026-08-14 (audit 2, V.4).** Diagnóza: cez 55 taskov migroval
blocker cez deväť úrovní, z ktorých každá bola **presnejší opis toho, čo
chýba** — nie pokus to vyrobiť. Špecifikáciu neprítomného objektu možno
zjemňovať bez konca a každé zjemnenie vyzerá ako pokrok, pretože je to nový,
korektne auditovaný artefakt.

Pravidlo:

> **Zjemnenie špecifikácie chýbajúceho objektu nie je povolený ďalší krok.**
> Ak je blocker tvaru „chýba X", povolený ďalší krok je postaviť najhrubšieho
> možného explicitného kandidáta na X — aj vymysleného, aj zlého — a prehnať
> ho cez všetky mantinely. Zlyhanie povie, ktoré mantinely sú aktívne.

- Zjemnenie špecifikácie **nespotrebuje chybu**, ale ani **nevytvorí artefakt,
  event ledger záznam, nový task ani novú podkoľaj**. Je to poznámka.
- Zlyhaný explicitný kandidát **spotrebuje jednu chybu z rozpočtu otázky** a
  **vytvorí jeden kompaktný riadok** so zoznamom mantinelov, ktoré ho zabili.
- Rozdiel, na ktorom všetko závisí: zlyhaný kandidát učí, ktorý mantinel
  kúše. Zjemnená špecifikácia neučí nič.

### 4.2 Desaťchybová dávka vnútri otázky

Každá implementačná problémová línia vedie:

```text
ERROR_BATCH_INDEX
ERRORS_USED_IN_CURRENT_BATCH = 0..10
CUMULATIVE_TECHNICAL_ERRORS
LAST_FAILED_CANDIDATE_SHA256
```

Pravidlá počítania:

1. Jeden distinct candidate/build/test, ktorý zlyhá a vyžaduje opravu
   zdroja, konfigurácie, závislosti alebo runtime kontraktu, spotrebuje jednu
   chybu. Viac fixtures s jednou koreňovou príčinou je jedna chyba.
2. Rovnaký candidate SHA sa nesmie bez zmeny znovu spustiť. Zakázané
   opakovanie nevytvorí nový dokument ani nový pokus.
3. Úspešný DEV test nevynuluje spotrebované chyby dávky. Dávku uzavrie iba
   prijatý official/scientific výsledok alebo explicitné ukončenie línie.
4. Premenovanie súboru, nový suffix, agent alebo task counter nevynuluje.
5. Pri `10/10` vznikne `TECHNICAL_PERMISSION_GATE`. Povolená je už len
   stručná read-only diagnóza; ďalší edit, DEV test aj official run sa
   zastavia.
6. Pokusy `11–20` sa otvoria iba po výslovnom povolení Martina Jambora.
   Povolenie zvýši `ERROR_BATCH_INDEX` a otvorí nových najviac desať chýb;
   kumulatívna história sa zachová.
7. `TECHNICAL_PERMISSION_GATE` nie je fyzikálny STOP a nezabíja rodičovskú
   koľaj.

Bežná chyba dostane iba jeden kompaktný route-local riadok:

```text
timestamp | batch/error | candidate_sha | failing_test | root_cause_class |
fix_or_next | scientific_effect=NONE
```

Samostatný error audit/dokument vzniká iba ak chyba mohla ovplyvniť už
publikovaný vedecký raw alebo patrí do rovníc, jednotiek, gauge, stavového
poradia, prahov, proveniencie či rozhodovacej logiky. Reusable prevencia sa
pridá do known-pattern checklistu iba raz.

## 5. Progress review bez procesného spamu

`progress_goal_reviewer` sa spúšťa iba po:

- uzavretí vedeckej brány alebo zmene autoritatívneho blockeru/route;
- official výsledku, ktorý mení dôkaz;
- dosiahnutí `TECHNICAL_PERMISSION_GATE 10/10`;
- explicitnom podozrení na goal drift alebo neprimeraný súborový/auditný
  churn.

Nespúšťa sa po bežnej DEV chybe, oprave, kompilácii, smoke teste, statickom
medzikroku ani po vytvorení package control súboru. Počet dokumentov,
skriptov, testov alebo auditov nie je vedecký progres.

## 6. Auditný nález, karanténa tvrdenia a rozhodnutie o koľaji

Interný alebo externý auditor klasifikuje každý materiálny nález presne do
jednej triedy:

```text
P0_PACKAGE_PROCESS_ONLY
T1_TECHNICAL_NO_CLAIM_REACH
S1_LOCAL_CORRECTABLE_SAME_TRACK
S2_TRACK_IDENTITY_AT_RISK
S3_FATAL_IN_SCOPE
S4_PARENT_THEORY_IMPACT
```

- §P0§ znamená chybu package control vrstvy bez zmeny vedeckých evidence
  hashov. Opraví sa iba package revision, znovu sa zapečatí a požiada sa o
  nový audit. DEV, RC, official ani interný science audit sa neopakujú.
- §T1§ sa vracia do DEV na najskorší technický bod, ktorý mohol chybu
  odstrániť. Vedecký raw sa zneplatní iba ak je chyba k nemu dosiahnuteľná.
- §S1–S4§ okamžite vytvoria §CLAIM_QUARANTINE§. Dotknutý checkpoint a všetci
  jeho závislí potomkovia sa nesmú používať ako prijatý dôkaz, kým hlavný
  orchestrátor neprijme rozhodnutie.

Pri §S1–S4§ vznikne jeden spoločný §AUDIT_FINDING_DECISION_RECORD§, nie
reťazec samostatných auditov. Obsahuje:

1. presný finding a jeho reprodukciu;
2. earliest invalid checkpoint a zoznam závislých záverov;
3. matematický/logický dosah;
4. fyzikálny dosah: covariance, conservation, gauge, causality, stability,
   jednotky, limity a observables;
5. filozoficko-identitný dosah: súlad s bunkovou ontológiou, kauzálnou
   architektúrou, vysvetľovacím cieľom teórie a zákaz ad-hoc záchrany dátami;
6. §TRACK_IDENTITY_GATE = SAME_TRACK_CONFIRMED / NEW_TRACK_REQUIRED /
   UNRESOLVED_AUTHOR_DECISION§;
7. tri možnosti pre Martina: opraviť a vrátiť workflow na exact bod, založiť
   novú koľaj, alebo koľaj v presnom scope ukončiť.

Návratový bod sa volí podľa príčiny, nie podľa pohodlia:

- chyba interpretácie -> §INTERNAL_SCIENCE_AUDIT§;
- chyba official vstupu/execution -> §OFFICIAL_RUN_AUTHORIZED§ po oprave
  upstream príčiny;
- chyba prepisu/kódu -> §DEV_SANDBOX§ a nový RC;
- chyba contractu/rovnice pri zachovanej identite -> §CONTRACT_DRAFT§;
- zmena mechanizmu, stavového priestoru, interakčnej topológie, kauzality
  alebo ontológie -> bez autorovho rozhodnutia sa nesmie označiť ako tá istá
  koľaj.

§S3/S4§ môže odporučiť STOP, ale autoritatívne ukončenie alebo otvorenie novej
koľaje zapíše až hlavný orchestrátor po rozhodnutí Martina.

## 7. Opakovateľné checkpointy a viacerí externí auditori

Každý externe auditovateľný vedecký míľnik má:

```text
CHECKPOINT_ID
PARENT_CHECKPOINT_IDS
ROUTE_AND_GATE
ACCEPTED_STATE
CONTRACT_RC_INPUT_RAW_AUDIT_SHA256
CANONICAL_PACKAGE_ID
CANONICAL_PACKAGE_MANIFEST_SHA256
CHECKPOINT_STATUS
```

Vzťahy sa zapisujú do jediného append-only registra
§External_Audits/HISTORY/00_CHECKPOINT_AND_AUDIT_SUBMISSION_REGISTER.tsv§.
Tak možno audit začať v ľubovoľnom prijatom bode, overiť jeho rodičovské
predpoklady a pokračovať po závislostiach bez prepisovania histórie.

Jeden sealed canonical package možno poslať viacerým nezávislým auditorom
bez zmeny jeho bajtov. Každé odovzdanie má vlastný §AUDIT_SUBMISSION_ID§,
audítora a unikátnu response cestu. Nový auditor štandardne nečíta odpovede
predchádzajúcich auditorov. Rozporné posudky sa neriešia hlasovaním; otvoria
§AUDIT_DISCREPANCY_REVIEW§ nad presnou metódou a evidence.

### 7.1 Povinná položka FRAME_CHALLENGE

**Zavedené 2026-08-14 (audit 2, VI.5–VI.7).** Zistenie auditu: agentová
audítorská vrstva je efektívna na **lokálnu správnosť** a štrukturálne
neschopná zachytiť **kategoriálnu** chybu, pretože kategoriálna chyba je
definovaná relatívne k rámcu a všetci agenti zdieľajú rámec, ktorý im zadá
autor. Doklad: za 222 taskov, 44 runnerov, štyri zapečatené balíky a desiatky
dual-auditov bolo kategoriálnych nálezov **nula**.

Z toho vyplýva prevádzkové pravidlo: **kategoriálny nález nikdy nepríde ako
odpoveď na otázku z balíka; príde iba ako odmietnutie tej otázky.** Dnes taký
kanál v procese neexistuje. Preto každý auditný balík (interný aj externý)
povinne obsahuje:

```text
FRAME_CHALLENGE:
  Je otazka tohto balika spravne polozena?
  Ak nie: ktory UPSTREAM vypocet ju robi bezpredmetnou?
  Ak ano: preco - jednou vetou, nie predvolene.
```

Odpoveď `otázka je správne položená` bez zdôvodnenia je neúplný audit.

### 7.2 Menovanie audítorskej vrstvy

Slovo **„externý"** sa v release, README ani §13 nesmie použiť pre audit,
ktorý vykonal jazykový model. Povolený tvar je
`independent LLM agent audit (model, revízia, mode)`. Do §13 patrí veta:
*„Žiadny audit v tomto korpuse nebol vykonaný človekom mimo projektu."*

Dôvod: metadáta sú v artefaktoch úplne priznané, ale čitateľ prečíta
*„external T2 audit"* a *„independent audits recommended PASS"* ako recenziu
človekom. To je materiálna dezinformácia konotáciou, aj keď podkladový
artefakt hovorí pravdu. Vlastná tabuľka T-úrovní už hovorí, že žiadny
výsledok nedosiahol `T3_INDEPENDENT_IMPLEMENTATION`.

Sekcia dokazujúca bit-identitu a rád konvergencie sa volá
**`Computational reproducibility`**, nie vedecká validácia.

## 8. Dokumentácia a súborový rozpočet

- Dokumentuje sa vývoj teórie: vstupný contract, rovnice a ich pôvod,
  rozhodovacie kritériá, immutable raw, vedecká interpretácia, aktuálny stav
  a najbližší krok.
- Bežné technické chyby sa nedokumentujú naratívne. Ich jediným trvalým
  výstupom je kompaktný error riadok, regresný test a prípadne jeden nový
  reusable known pattern.
- Dynamický globálny stav žije iba v
  `tracks/00_CURRENT_EXECUTION_PLAN.md`; `00_READ_FIRST.md` je navigácia.
- Route stav žije v najnižšom work plane. História patrí do `HISTORY/` a
  nesmie sa kopírovať späť do živých plánov.
- Bežný atóm má najviac päť live vedeckých artefaktov. Centrálne registre sa
  menia jedným batchom až pri skutočnej zmene stavu alebo míľniku.
- Externý balík sa nevytvára pre DEV chybu ani každý support krok.
- Závažný auditný finding vytvára jeden decision record a checkpoint
  invalidation delta; nie nový dokument pre každý komentár auditora.
- Pred editáciou oznám presný zoznam/count súborov; po editácii vykáž
  `LIVE_SCIENTIFIC_ARTIFACTS`, `LIVE_CENTRAL_REGISTERS_UPDATED`, total a
  `AUDIT_PACKAGE_COPIES` osobitne.
- `theory/` je release/historická vrstva. Pracovné zmeny patria do `tracks/`.
- Historický vedecký dôkaz sa nemaže. Odstrániť možno iba preukázanú
  byte-identickú kópiu, superseded navigáciu alebo nevedecký procesný text,
  ak jeho odstránenie neporuší hashovanú dôkazovú reťaz.

## 9. Kompresne odolný handoff

Každá delegácia nesie aspoň:

```text
TASK_ID
ROLE
ROLE_CONFIG_SHA256
ASSIGNED_AGENT_TASK_ID
ARTIFACT_AUTHOR_TASK_ID
STATIC_AUDITOR_TASK_ID
INTERNAL_AUDITOR_TASK_ID
PACKAGE_CURATOR_TASK_ID
EXTERNAL_AUDITOR_TASK_ID
SEPARATION_OF_DUTIES_CHECK
ROUTE
CURRENT_PHASE
ALLOWED_NEXT_ACTION
ALLOWED_READS
ALLOWED_WRITES
FORBIDDEN_ACTIONS
IMMUTABLE_INPUT_PATHS_AND_SHA256
PREREG_SHA256
RUN_AUTHORIZED
OUTPUT_PATHS
ERROR_BATCH_INDEX
ERRORS_USED_IN_CURRENT_BATCH
CUMULATIVE_TECHNICAL_ERRORS
FINDING_ID
FINDING_CLASS
EARLIEST_INVALID_CHECKPOINT_ID
TRACK_IDENTITY_GATE
CHECKPOINT_ID
PARENT_CHECKPOINT_IDS
AUDIT_SUBMISSION_ID
DONE_WHEN
NEXT_ROLE
```

Kapsul sa vloží do existujúcej preregistrácie alebo append-only route
ledgera. Samostatný súbor vznikne iba pre fyzikálne nezávislú úlohu.
Pridelená rola overí actual config SHA proti kapsulu a
`.codex/agents/00_MANIFEST.md`. Zlyhanie identity alebo oddelenia rolí je
`SEPARATION_OF_DUTIES_FAILURE / NO_RUN`.

## 10. Trieda operácií bez contractu

**Zavedené 2026-08-14 (audit 2, V.11).** Doklad problému: úloha Q1R1-V3 mala
zistiť, či jeden externý paper môže byť svedkom pre brány G0–G3. Vygenerovala
preregistráciu, PowerShell akvizičný skript, tar archív, terminálny operačný
journal, autoritatívny výsledok, tabuľku štyroch brán a kanonický živý stav —
a jej fyzikálny obsah bol jeden odstavec poznámok z čítania. Source closure
zostala `UNRESOLVED` kvôli BibTeX štýlovému súboru.

Preregistrácia rešeršného downloadu nie je riadenie rizika; je to premiestnená
práca.

**Contract začína tam, kde vzniká nárok.** Nasledujúce operácie sú
`NO_CONTRACT_CLASS`:

| Operácia | Výstup |
|---|---|
| čítanie literatúry, stiahnutie zdroja, extrakcia čísel z cudzieho papera | poznámka |
| prieskumný výpočet **bez nároku** — orientačný rád, sanity check, sken parametra | poznámka + skript v `tmp/` |
| reprodukcia cudzieho publikovaného výsledku pre kalibráciu vlastného nástroja | poznámka |
| zjemnenie špecifikácie blockeru (§4.1) | poznámka |
| navigačná alebo formátovacia zmena bez zmeny čísla | žiadny |

Pre `NO_CONTRACT_CLASS` platí:

- **nevzniká** prereg, RC, DNR záznam, brána, checkpoint, event ledger riadok,
  package ani skóre;
- **nespotrebuje** chybu z rozpočtu otázky;
- výsledok **sa nesmie citovať ako dôkaz** a nesmie vstúpiť do žiadneho
  official vstupu;
- ak sa z poznámky stane nárok, **vtedy** sa otvorí contract a poznámka sa
  stane jeho vstupom s vlastným hashom.

Rozlišovací test má jednu otázku: *tvrdím niečo o svete, alebo si niečo
zisťujem?* Druhé je poznámka.

## 11. Finitnosť hľadaného priestoru

**Zavedené 2026-08-14 (audit 2, V.7).** Podmienka smrti rodiča v
`00_CONSTRAINT_FEASIBILITY_LEDGER.md` §8 bod 6 (*„rodič zomrie iba po
`EMPTY_CERTIFIED_SCOPE` pre celý vopred definovaný priestor `X_K`"*) je
formálne nesplniteľná, keď je `X_K` priestor funkcií. Zabíjanie podtried po
jednej nekonečnodimenzionálny priestor nikdy nevyčerpá. Doklad: K7 má päť
zabitých podtried a je `UNDETERMINED_REVIEW`; K11 má štyri a je
`UNDETERMINED_REVIEW`.

Pravidlo:

> **Otázka existencie sa nesmie otvoriť nad priestorom, ktorý nemá deklarovaný
> konečnorozmerný rez.**

Pred otvorením contractu na hľadanie objektu v `X_K` sa povinne deklaruje:

```text
DERIVATION_ORDER = n            zafixovany derivacny rad
COEFFICIENT_SPACE               konecnorozmerny priestor koeficientov
DECISION_METHOD = SOS | CAD     rozhodovacia metoda pre prazdnost
ESCALATION                      ak prazdno: rad n+1; ak prazdno dvakrat
                                po sebe -> obhajitelny NO_GO
```

Keď je priestor konečný, „konštruovať" a „vylúčiť" sú tá istá operácia a nedá
sa medzi nimi driftovať. Tým sa naraz odstráni príčina §4.1 aj §4.
