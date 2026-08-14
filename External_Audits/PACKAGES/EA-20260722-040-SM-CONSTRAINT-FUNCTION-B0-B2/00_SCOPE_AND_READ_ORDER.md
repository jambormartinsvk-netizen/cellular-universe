# EA-040 — S–M constraint-first funkcia, screeny B0–B2

**Stav:** `SEALED_READY_FOR_AUDIT`  
**Target tier:** `T1_PRIMARY_FORMULA / ANALYTIC_CONDITIONAL_SCREEN_ONLY`  
**Autorita:** živý dokument 245; externý auditor iba odporúča  
**Autor teórie:** Martin Jambor  
**Formalizácia rovníc a procesný orchestrátor:** Codex (OpenAI)  
**PACKAGE_CURATOR_TASK_ID:** `/root`  
**EXTERNAL_AUDITOR_TASK_ID:** `/root/ea040_external_audit`  
**CURATION_REVIEWER_TASK_ID:** `/root/ea038_external_audit`  
**SEPARATION_OF_DUTIES_CHECK:** `PASS(curator != external auditor)`  
**AUDITOR_ROLE_CONFIG_SHA256:** `6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14`  
**PACKAGE_CURATOR_ROLE_CONFIG_SHA256:** `26CAB7693DBB372C4FAEEFBACF9101CD2C1BA3F40E628CB20E6514EA8A906AE1`  
**PACKAGE_CURATOR_CONFIG_BINDING:** `REFERENCE_ONLY_MAIN_ORCHESTRATOR_CURATOR`  
**RUN_AUTHORIZED:** `false`  
**LIVE_SCIENTIFIC_ARTIFACTS:** `1` — živý dokument 245  
**LIVE_CENTRAL_REGISTERS_UPDATED:** `4` — tri plány a event ledger  
**LIVE_FILES_CHANGED_TOTAL:** `5`  
**AUDIT_PROCESS_TOOL_UPDATED:** `1` — všeobecný R6 no-runtime preflight guard  
**AUDIT_PACKAGE_COPIES:** `15` manifestových kópií + `7` controls = `22`;
response `1`; spolu `23 < 40`.

## AUDITOR_RULESET_PATHS_AND_SHA256

```text
EVIDENCE/009__AGENTS.md=BD64D6AC1C583194A67B3ABC5423467AF3F5F292F0293AF68F02AA3BBC503EE5
EVIDENCE/010__PROJECT_OPERATING_SYSTEM.md=F4F0C3610CBE5BDF05DEC7EE606534682222DBF959F439686CF89FA7B0F7E543
EVIDENCE/011__AUDITOR_PACKAGE_PROTOCOL_R6.md=4330FFD3D22C27CC60A3693E9B4694B601903FC6490A4DB7F56B56B1C4FD5272
EVIDENCE/012__EXTERNAL_AUDITOR_ROLE.toml=6B1AF6C55E725E7A2332F30F0337713F1A7E254402E7F8A5A64BB689569C9A14
EVIDENCE/013__AGENT_ROLE_MANIFEST.md=76921D8F2FA0FB02C70F511AFB4396C4148F052938DA21C33B91D1594C20061E
```

## Scope markery

```text
LIFECYCLE_RESULT=PASS_MAPY
INTERNAL_REVIEWER_RESULT=PASS_MAP
B0_RESULT=PASS_SCREEN
B0_SCOPE=ANALYTIC_CONDITIONAL_SCREEN
B1_RESULT=CONDITIONAL_FUNCTION_FAIL
B1_SCOPE=SHARED_1280_EFOLD_BACKGROUND_ENERGY_MAP
B2_STATUS=EVENT_FACTORIZATION_REQUIRED_FOR_B2_DISCRETE_EVENT_BRANCH
RESULT_CLASS=PRECHECK_EXCLUDED_SCOPE
D03=SOLE_ACTIVE
D04_D11=BLOCKED
K4=60/100_UNCHANGED
P5=3.5/6_UNCHANGED
T2_NOT_CLAIMED
T3_NOT_CLAIMED
NO_RUNTIME
NO_PYTHON
NO_COMPUTED_VERDICT
```

## Presná otázka

1. Je constraint-first mapa v oddieloch 8.1–8.9 primárneho dokumentu
   lokálna, rozmerovo konzistentná a zlučiteľná so zachovaním energie?
2. Je správne oddeliť pri diskrétnej bunkovej udalosti mieru udalostí
   `R_J` od energie jednej udalosti `E_J`, pričom pozadie identifikuje iba
   súčin `Q_D=R_J E_J`?
3. Je prompt parný kandidát
   `r_s=(2/g_*) epsilon_J^2`, `beta_s=r_s/(1+r_s)` správne označený iba
   ako rekonštruovaná hypotéza na intervale `0<=epsilon_J<=1`, bez
   dvojitého použitia faktora `2/g_*`?
4. Podporujú B0 a B1 iba deklarovaný podmienený záver, že mapovanie pary
   priamo z priemernej backgroundovej energie `y_e` je pri spoločnej
   1280-e-foldovej vetve silno potlačené, nie všeobecný STOP pary?
5. Je B2 dostatočný na otvorenie ďalšieho analytického kroku: konečnej,
   vopred odôvodnenej množiny kandidátov pre `R_J(Y)` a `E_J(Y)`?

## Poradie čítania

1. `EVIDENCE/014` — primárny dokument, najmä oddiely 3, 7 a 8;
2. `EVIDENCE/001` — predchádzajúca STOP/brána a pôvod otvoreného vstupu;
3. `EVIDENCE/002` až `005` — odvodenie z mantinelov, skorá para a poradie
   produktov;
4. `EVIDENCE/006` a `007` — filozofia teórie, A12/A13 a metodické
   obmedzenia Q18/Q22;
5. `EVIDENCE/008` — aktuálny autoritatívny stav;
6. `EVIDENCE/015` — presný AR66.2 formula-provenance checklist;
7. manifest, prázdna no-runtime mapa a pravidlá `EVIDENCE/009` až `013`.

## Predregistrované hodnotenie externého posudku

- `AGREE_IN_SCOPE`: rovnice, scope a klasifikácie B0–B2 sú konzistentné;
- `AGREE_WITH_LIMITATION`: mapa je použiteľná, ale auditor presne označí
  chýbajúci invariant, doménu alebo nonclaim pred tvorbou kandidátov;
- `DISAGREE`: auditor nájde porušenie zachovania energie, rozmerov,
  kruhovú definíciu alebo záver silnejší než dodané predpoklady;
- `CANNOT_AUDIT`: primárna formula alebo jej autoritatívny pôvod v balíku
  chýba.

## Tier hranica

Balík je statický T1 formula audit. Neobsahuje výpočtový skript, generated
JSON ani transitive runtime closure. Auditor nesmie vydávať ručný výpočet
alebo vlastný nový model za T2 reprodukciu.

## Nonclaims

- Balík nevyberá konkrétne `R_J`, `E_J`, `Gamma_D`, clock ani mikrofyziku.
- Dokument 244 je iba `HISTORICAL_CONTEXT`, nie aktuálny live STOP.
- `phi_e` je iba efektívna bunková kolektívna súradnica, nie nový
  fundamentálny inflatón.
- `y_e` je diagnostický lokálny stav, nie uzavretý globálny clock.
- B0 je iba `ANALYTIC_CONDITIONAL_SCREEN`; B1 iba
  `CONDITIONAL_FUNCTION_FAIL` v spoločnom 1280-e-foldovom background scope.
- B1 nevylučuje celú S–M vetvu. Vylučuje iba testované
  `beta_s proportional y_e^2` pri štyroch uvedených predpokladoch a pri
  identifikácii energie slabej udalosti s priemernou bunkovou energiou.
- B2 nedokazuje existenciu vzácnych Planckovských udalostí a nepovoľuje
  nastaviť `epsilon_J=1` bez odvodenia.
- `R_J`, `E_J`, `Gamma_D`, `Gamma_C`, `beta_s` ani `V1-T1` nie sú
  odvodené alebo vybrané zákony.
- `T_freeze` z A13 nie je `T_exit`; `Delta N_eff=0.0535`, `0.90 K` a
  `53 GHz` nie sú cieľové hodnoty ani aktuálne predikcie.
- B2 nepreukazuje Poissonovský šum ani vyššie korelácie udalostí.
- K4 ostáva `60/100`, P5 `3.5/6`, P5.4 `NOT RUN`; G8/G9, fit, Python a
  zmena prediction table zostávajú blokované.

## Autorita a oddelenie rolí

Kurátor balíka a plánovaný externý auditor sú rozdielne identity. Interné
read-only kontroly nie sú externým posudkom. Externý audit nemení projektový
verdikt ani skóre; jeho odpoveď spracuje hlavný orchestrátor v novom
autoritatívnom assessment súbore.
