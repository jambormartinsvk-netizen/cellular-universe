# EA-043 — B6b-1 analytické obálky a B6b-2 perturbation/search/S8 passport

**Stav:** `SEALED_READY_FOR_AUDIT`  
**Target tier:** `T1_PRIMARY_FORMULA / ANALYTIC_ENVELOPE_PERTURBATION_SEARCH_DATA_PASSPORT_AUDIT_ONLY`  
**Autorita:** živé dokumenty 245–247; externý auditor iba odporúča  
**Autor teórie:** Martin Jambor  
**Formalizácia a procesný orchestrátor:** `/root`  
**TASK_ID:** `A2K4-EA043-PACKAGE-CURATION-20260723-66`  
**PACKAGE_CURATOR_TASK_ID:** `/root/ea043_package_curator`  
**ARTIFACT_AUTHOR_TASK_ID:** `/root`  
**INTERNAL_AUDITOR_TASK_ID:** `/root/b6b2_physics_auditor`  
**EXTERNAL_AUDITOR_TASK_ID:** `/root/ea043_external_auditor`  
**INDEPENDENT_PACKAGE_REVIEWER_TASK_ID:** `/root/b6b1_documentation_steward`  
**SEPARATION_OF_DUTIES_CHECK:** `PASS(/root/ea043_package_curator != /root; /root != /root/b6b2_physics_auditor; /root/ea043_package_curator != /root/ea043_external_auditor; /root/b6b2_physics_auditor != /root/ea043_external_auditor)`  
**AUDITOR_ROLE_CONFIG_SHA256:** `6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14`  
**PACKAGE_CURATOR_ROLE_CONFIG_SHA256:** `26CAB7693DBB372C4FAEEFBACF9101CD2C1BA3F40E628CB20E6514EA8A906AE1`  
**RUN_AUTHORIZED:** `false`
**SEAL_AUTHORITY_TASK_ID:** `/root` (`A2K4-EA043-SEAL-20260723-69`)  
**INDEPENDENT_PACKAGE_REVIEW:** `READY_TO_SEAL_EA043 / 96_OF_96_PASS / 15_OF_15_SOURCE_COPY_PARITY / ZERO_FINDINGS`

## R6 súborové počítadlá

Package-curation atóm:

```text
LIVE_SCIENTIFIC_ARTIFACTS=0
LIVE_CENTRAL_REGISTERS_UPDATED=1
LIVE_FILES_CHANGED_TOTAL=1
AUDIT_PACKAGE_COPIES=22 (15 evidence + 7 controls)
RESPONSE_TEMPLATE_FILES=1
NEW_PACKAGE_AND_RESPONSE_FILES_TOTAL=23
```

Podkladový vedecký closure, ktorý balík iba kopíruje a nemení:

```text
UNDERLYING_LIVE_SCIENTIFIC_ARTIFACTS=1
UNDERLYING_LIVE_CENTRAL_REGISTERS_UPDATED=4
UNDERLYING_LIVE_FILES_CHANGED_TOTAL=5
```

## AUDITOR_RULESET_PATHS_AND_SHA256

```text
EVIDENCE/011__AGENTS.md=226710D6467FE923D6F2CBAFF02CE9235F1B48C07C4A9DACD95C6B06486B2B29
EVIDENCE/012__PROJECT_OPERATING_SYSTEM.md=519BDCBAE2CD9BF62351586E357DE3C9A28E60AD79CDB653661DD2821D65B6E7
EVIDENCE/013__AUDITOR_PACKAGE_PROTOCOL_R6.md=4330FFD3D22C27CC60A3693E9B4694B601903FC6490A4DB7F56B56B1C4FD5272
EVIDENCE/014__EXTERNAL_AUDITOR_ROLE.toml=6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14
EVIDENCE/015__AGENT_ROLE_MANIFEST.md=9E3746AA282EA7A3A54564C6B0B2CEB73BE049EAC358232215318E89DE9C9EE4
```

## Scope markery

```text
B6B1=PASS_B6B1_ANALYTIC_ENVELOPE_CONTRACT
B6B2=PASS_B6B2_PASSPORT_SCHEMA
B6B2_PHYSICAL_CONTENT=REVIEW_BLOCKED_D03_D11
E3_S8_OUTER_SEARCH_ENVELOPE=[0.777,0.831]
E3_MAPPING=E2_FLAT_LAMBDACDM_ONLY
DESI=UNCERTIFIED_QUASI_HOLDOUT_NO_RANKING
MF1_MF2_MF3_MF4=OPEN
NEXT=D04+D08+D10_NON_EXECUTABLE_AUTHOR_INPUT_SUBPACKAGE
REPRO=0
RUNTIME_ROWS=0
NO_PYTHON
NO_COMPUTED_RESULT
NO_PHYSICAL_KERNEL_OR_SEARCH
```

## Presná otázka

1. Sú spoločné a rodinné momentové inequalities B6b-1 pre MF1–MF4
   konzistentné, rovnako hlboké a bez tvrdenia životaschopnosti alebo
   prázdnosti rodiny?
2. Je B6b-2 kovariantný passport `P0–P8` úplný vzhľadom na znamienka,
   source-off limity a rodinné linear-response identity?
3. Sú immutable search record, coverage, no-mutation a ranking guardy
   dostatočné na zabránenie leakage a skrytému fitu?
4. Je rozlíšenie E3 intervalu od E2 mapovania a
   calibration/comparator/quasi-holdout logika v projektových dokumentoch
   konzistentná s deklarovanou dôkazovou triedou?
5. Je split stavu korektný a je `D04+D08+D10` najmenší neexekvovateľný
   successor pri zachovaní závislostí D03/D05–D09/D11?

## Povinné obmedzenie S8 zdrojov

Cited DES/KiDS/HSC hodnoty sú iba project-contained citations. Balík
neobsahuje primárne survey likelihoody ani dátové vektory. Auditor ich musí
označiť `INFERRED_FROM_PROJECT_DOCS`; smie auditovať internú klasifikáciu a
použitie, ale nesmie tvrdiť nezávislé overenie primárnej publikácie.

## Poradie čítania

1. `01_MANIFEST_SHA256.tsv` a izolovaný bootstrap
   `EVIDENCE/011` až `015`;
2. tento scope, `02_AUDITOR_INSTRUCTIONS.md` a
   `03_REPRODUCTION_AND_EXPECTATIONS.md`;
3. `EVIDENCE/001` — primárne B6b-1 analytické obálky;
4. `EVIDENCE/002` — primárny B6b-2 perturbation/search/S8 passport;
5. `EVIDENCE/003` — rodičovský D03–D11 a MF1–MF4 contract;
6. `EVIDENCE/006` až `009` — Q22a, metodika a feasibility dôkazové triedy;
7. `EVIDENCE/004` a `005` — release lineage teórie;
8. `EVIDENCE/010` — autoritatívny stav, blocker a successor;
9. `04_RUNTIME_DEPENDENCY_MAP.tsv` a `05_PACKAGE_HISTORY.md`.

Externý auditor nesmie kvôli bootstrapu ani auditu čítať live projekt mimo
tohto balíka.

## Predregistrované hodnotenie externého posudku

- `AGREE_IN_SCOPE` — deklarovaný T1 formula/passport scope je konzistentný;
- `AGREE_WITH_LIMITATION` — jadro sedí, ale chýba presne pomenovaná
  inequality, identity, guard, klasifikácia alebo dependency;
- `DISAGREE` — materiálny formula/passport/search-split defect;
- `CANNOT_AUDIT` — chýba primárna formula, pravidlo alebo source lineage.

## Nonclaims

Balík neobsahuje executable physical kernel/search, výber kandidáta alebo
rodiny, S8 predikciu, certified holdout, closure D03–D11, computed result,
P5.4/G8/G9 ani zmenu K4/P5. Neudeľuje observačný PASS/STOP a nemení skóre
ani hĺbku. `PASS_B6B1_ANALYTIC_ENVELOPE_CONTRACT` a
`PASS_B6B2_PASSPORT_SCHEMA` sú scoped projektové stavy, nie dôkaz pravdivosti
teórie.

## Autorita a lifecycle

Externý posudok je neautoritatívne odporúčanie. Balík zostáva
`DRAFT_NOT_DELIVERED` aj po preflighte, kým ho neoverí nezávislý package
reviewer a hlavný orchestrátor ho výslovne nezapečatí.
