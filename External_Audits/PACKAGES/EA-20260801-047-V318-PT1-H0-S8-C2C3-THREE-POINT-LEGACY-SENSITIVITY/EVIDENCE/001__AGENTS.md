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

## 4. Desaťchybová dávka a povinná používateľská brána

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
