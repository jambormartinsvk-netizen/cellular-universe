# READ FIRST — navigácia, nie stavový register

**Aktualizované:** 2026-07-29  
**Stav:** 'NAVIGATION_ONLY'  
**Jediný globálny živý stav:** 'tracks/00_CURRENT_EXECUTION_PLAN.md'

Tento súbor zámerne neopakuje blocker, skóre, error counter ani next action.

## Jadro každej úlohy

1. 'AGENTS.md';
2. 'tracks/00_PROJECT_OPERATING_SYSTEM.md';
3. 'tracks/00_CURRENT_EXECUTION_PLAN.md';
4. najnižší route-local work plan;
5. aktívny handoff kapsul;
6. 'tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md'.

Pre aktívnu cestu P5:

1. 'tracks/A1/A1K1/A2/A2K4/00_WORK_PLAN.md';
2. 'tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_WORK_PLAN.md';
3. current plánom označený prereg/source/raw;
4. iba exact potrebný úsek
   'tracks/A1/A1K1/A2/A2K4/HISTORY/00_EVENT_LEDGER.md'.

Nečíta sa rekurzívne celý route strom ani celá história, ak kapsul uvádza
exact delta artefakty.

## Fázové bezpečnostné čítanie

### DEV tvorba/test

- exact candidate name v 'scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md';
- 'scripts/00_KNOWN_PYTHON_ERROR_PATTERNS.md';
- 'scripts/00_EXECUTION_TIME_LIMITS.md';
- route-local error batch;
- base ownership/version registre iba ak sa mení base module.

Celý formal error ledger sa v DEV nečíta. Používa sa cielené vyhľadanie
relevantnej error triedy.

### RC audit/official

Navyše frozen contract, RC source/input hashe, absent-output guard, relevantné
PF záznamy a exact DNR check. External package sa riadi
'External_Audits/00_AUDITOR_PACKAGE_PROTOCOL_SK.md'.

## Orientačné registre

- všetky routes: 'tracks/00_ROUTE_REGISTER.md';
- A2 koľaje: 'tracks/A1/A1K1/A2/00_TRACK_REGISTER.md';
- layout: 'tracks/00_ROUTE_AND_ARTIFACT_LAYOUT_SK.md';
- skratky: 'Questions/00_ABBREVIATION_AND_IDENTIFIER_REGISTER_SK.md';
- constraint feasibility:
  'tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md';
- script index: 'scripts/00_ROUTE_SCRIPT_INDEX.md'.

Historické hĺbky ani verdicty sa neobnovujú zo staršieho README. Rozhoduje
current plán, route plán a ich exact dôkazová reťaz.
