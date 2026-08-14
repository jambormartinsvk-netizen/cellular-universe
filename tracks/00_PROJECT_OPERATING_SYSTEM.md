# Operačný systém projektu — roly, prechody a lifecycle

**Revízia:** 2026-08-11 / R3.1  
**Autorita:** hlavný orchestrátor v medziach autorstva Martina Jambora  
**Cieľ:** auditovateľný vedecký výpočet bez toho, aby bežné technické chyby
vytvárali nové preregistrácie, audity a dokumenty.

## 1. Autoritatívne poradie

Pri rozpore rozhoduje:

0. **stanica `A0`** ('tracks/A0/00_STATION.md') — od 2026-08-14 je upstream od
   všetkého nižšie. Kým nie je rozhodnutá, `A2` aj `A3` sú `FROZEN_PENDING_A0`
   a neotvára sa v nich žiadny nový vedecký atóm;
1. explicitné aktuálne rozhodnutie Martina Jambora o fyzikálnom vstupe alebo
   povolení ďalšej desaťchybovej dávky;
2. 'AGENTS.md';
3. tento operačný systém;
4. 'tracks/00_CURRENT_EXECUTION_PLAN.md';
5. najnižší route-local work plan a aktívny handoff;
6. zmrazený vedecký contract/prereg, exact RC source/input hashe a immutable
   raw;
7. prijaté rozhodnutie hlavného orchestrátora nad nezávislým auditom.

Starší README, auditný súhrn ani chat nemôže obnoviť prekonaný živý stav.

## 2. Roly a ich jediné užitočné prechody

| Rola | Vstup | Zodpovednosť | Výstup / prechod |
|---|---|---|---|
| Martin Jambor | otvorená fyzikálna voľba, gate '10/10' alebo závažný auditný finding | zvoliť fyzikálny vstup; povoliť ďalších 10 chýb; rozhodnúť same-track opravu, novú koľaj alebo ukončenie | author decision |
| hlavný orchestrátor | current plan + route capsule | zmraziť scope, otvoriť DEV/RC/official, karantenizovať sporné checkpointy, prijať audity a zapísať stav | kapsul pre presne jednu ďalšiu rolu alebo decision dossier pre Martina |
| 'python_script_author' | contract draft + DEV capsule | implementovať a technicky stabilizovať jeden pracovný base/runner; spúšťať iba allowlisted offline DEV testy | 'DEV_TESTS_PASS' + candidate SHA alebo error event |
| 'math_script_auditor' | exact RC po DEV PASS alebo material audit finding | auditovať matematiku/logiku/provenance; pri findingu určiť claim reach a earliest invalid checkpoint | RC odporúčanie alebo math-impact časť decision recordu |
| 'manual_analytic_result_auditor' | exact hashovo zmrazený non-RC manuálny analytický výsledok s už spotrebovanou autorizáciou a zákazom opakovania | read-only audit rovníc, proof-status, proveniencie, rozhodovacích vetiev a claim reach bez opakovania výpočtu | odporúčanie prijať výsledok alebo jeden exact blocker pre orchestrátora |
| hlavný orchestrátor / executor | auditovaný RC + frozen contract + absent output | jediný bounded official run | immutable raw + execution receipt |
| 'physics_track_auditor' | official raw alebo material audit finding | posúdiť fyziku aj súlad opravy s ontológiou, kauzalitou a identitou koľaje | science/identity časť decision recordu |
| 'progress_goal_reviewer' | ucelený míľnik alebo gate '10/10' | zhodnotiť informačný zisk, goal drift a najmenší successor | jedna stručná milestone assessment |
| 'documentation_release_steward' | doc/release/checkpoint batch | overiť hashe, linky, checkpoint DAG, submission identity a duplicity | jeden correction manifest |
| 'external_package_curator' | prijatý míľnik alebo P0 package repair charter | vytvoriť canonical package alebo control-only repair revision bez zmeny evidence | sealed handoff |
| 'external_auditor' | sealed canonical package + unique submission ID | T1/T2/T3 audit; klasifikovať finding a claim reach | unikátna response pre orchestrátora |

Zakázané prechody:

- 'DEV_FAIL -> independent audit -> progress review -> successor doc';
- 'DEV_PASS -> fyzikálny verdict';
- 'author -> jediný auditor vlastného RC';
- 'technical error -> external package';
- 'package curator -> external auditor toho istého balíka'.
- 'material audit finding -> tichá lokálna oprava bez checkpoint invalidácie';
- 'track-defining correction -> pokračovanie pod starým track ID bez Martina'.

## 3. Stavový automat jedného výpočtového atómu

~~~text
CONTRACT_DRAFT
  |
  v
DEV_SANDBOX  <-----------------------------+
  | DEV fail: edit same working source      |
  | + regression + one compact error row ---+
  |
  | DEV suite pass
  v
RC_FREEZE
  |
  v
INDEPENDENT_STATIC_MATH_AUDIT
  | blocker -> DEV_SANDBOX, ak batch < 10
  | pass
  v
OFFICIAL_RUN_AUTHORIZED
  |
  v
IMMUTABLE_RAW
  |
  v
INTERNAL_SCIENCE_AUDIT
  |
  +-- material finding --> CLAIM_QUARANTINE
  |                        -> FINDING_IMPACT_REVIEW
  |                        -> MARTIN_DECISION_GATE
  |                        -> exact workflow return/new track/STOP
  |
  v
ORCHESTRATOR_DECISION
  |
  v
MILESTONE_PROGRESS_REVIEW
  |
  +--> ďalší vedecký atóm
  '--> voliteľný ucelený EXTERNAL_T2/T3
~~~

Pri desiatej chybe z ľubovoľného DEV/RC/official technického prechodu:

~~~text
ERRORS_USED_IN_CURRENT_BATCH = 10/10
  -> TECHNICAL_PERMISSION_GATE
  -> read-only stručná diagnóza
  -> WAIT_FOR_MARTIN
  -> explicitné povolenie otvorí ďalší batch 0/10
~~~

### 3.1 Manuálny analytický výsledok bez official runu

Ak capsule výslovne povoľuje iba bounded ručný symbolický/analytický krok bez
projektového kódu, Pythonu, siete, RC, official outputu a observable claimu,
po jedinom vykonaní sa jeho telo a vstupné hashe zmrazia. Autor nesmie krok
opakovať ani auditovať vlastný výsledok. Odlišný
'manual_analytic_result_auditor' smie iba read-only overiť rovnice,
proof-status, provenienciu, fail-closed vetvy a claim reach exact nezmeneného
tela. Jeho odporúčanie prijíma alebo odmieta hlavný orchestrátor.

Tento prechod nenahrádza DEV/RC/official workflow pre kód, numerické rawy,
observable predikcie alebo fyzikálny verdict a sám neautorizuje Python, sieť,
official run, checkpoint ani externý audit.

## 4. Fáza CONTRACT_DRAFT

Contract obsahuje iba vedecky potrebné informácie:

- otázku a 'DONE_WHEN';
- rovnice, source lineage, znamienka, jednotky, gauge a stavové poradie;
- vstupy, prahy, holdouty, nulové/negatívne kontroly;
- PASS/REVIEW/STOP vetvenie a nonclaims;
- official output path a collision guard.

Contract sa nemusí prepisovať pri každej technickej oprave. Pred RC freeze
musí byť obsahovo konečný. Od RC freeze sa nemení; zmena fyziky otvára nový
vedecký atóm, nie technický successor.

## 5. Fáza DEV_SANDBOX

DEV je technická dielňa, nie dôkazová vrstva.

Povolené:

- 'py_compile', '--help', parser/CLI, synthetic unit test, offline SelfTest;
- lokálne mock/fixture vstupy bez reálnych vedeckých dát a siete;
- editácia rovnakého pracovného base/runnera;
- dočasný výstup iba v capsule allowliste s cleanup guardom.

Zakázané:

- official vstupy a official output path;
- sieť, publikácia, scoring a fyzikálny verdict;
- nový prereg, auditný dokument, DNR entry alebo versioned successor pre
  obyčajnú implementačnú chybu;
- opätovný beh identického failed candidate SHA.

Každý DEV fail vytvorí presne jednu počítanú error udalosť na distinct
candidate. Viac fixture failures s jednou príčinou je jedna udalosť.
Povinné minimum je candidate SHA, failing test, root-cause class, oprava a
'scientific_effect=NONE'. Detailné stack trace ostáva v raw termináli alebo
krátkom machine receipt, nie v novom Markdown dokumente.

## 6. Desaťchybová brána vnútri rozpočtu fyzikálnej otázky

**Revízia 2026-08-14 (externý audit 2, V.5).** Nadradený rozpočet už nepatrí
implementačnej línii, ale **fyzikálnej otázke**; autoritatívne pravidlo je
`AGENTS.md` §4. Táto sekcia opisuje už len operatívnu bránu vnútri otázky.

Dôvod zmeny: pôvodné pravidlo *„nový vedecký atóm začne vlastný batch 0/10"*
malo mechanický nezamýšľaný dôsledok — **rozpočet sa obnovoval tým, že sa
problém rozdelil**. Sedemnásť podkoľají `D2SW0…D2SW16` znamenalo až 170
chybových slotov na jednu otázku. Pravidlo, ktoré malo terminovať, umožňovalo
neterminovať.

Route-local stav vedie:

~~~text
QUESTION_ID                      nadradeny; AGENTS.md §4
QUESTION_ERROR_BUDGET = 30
QUESTION_ERRORS_USED
ERROR_BATCH_INDEX
ERRORS_USED_IN_CURRENT_BATCH
CUMULATIVE_TECHNICAL_ERRORS
LAST_FAILED_CANDIDATE_SHA256
BATCH_AUTHORIZED_BY
BATCH_AUTHORIZATION_DATE
~~~

- Nová podkoľaj, adresár, task counter ani implementačná línia **neotvárajú
  nový rozpočet**. Dedia `QUESTION_ID` a čerpajú z rozpočtu otázky.
- Pri `QUESTION_ERRORS_USED = 30` sa otázka uzavrie ako
  `NO_GO_BY_EXHAUSTION` s presným zoznamom skúšaného. To je publikovateľný
  vedecký výsledok.
- Zjemnenie špecifikácie chýbajúceho objektu **nie je povolený ďalší krok**
  (`AGENTS.md` §4.1, `HRUBÝ_KANDIDÁT_FIRST`).
- Otázka existencie sa **neotvára nad priestorom bez konečného rezu**
  (`AGENTS.md` §11, `FS-C13`).

- Každá distinct technická chyba spotrebuje '1/10'.
- DEV úspech counter nevynuluje; zabraňuje sa tým nekonečnému cyklu
  fail/pass/fail.
- Official/scientific closure ukončí implementačnú líniu. Nový vedecký atóm
  začne vlastný batch '0/10'.
- Pri '10/10' orchestrátor nesmie otvoriť ďalší edit, test ani run. Vytvorí
  iba jednu stručnú gate summary: čo sa skúšalo, spoločné príčiny, čo je
  stále neoverené a návrh pokračovať/zmeniť architektúru/zastaviť.
- Pokusy '11–20', '21–30', ... vyžadujú vždy nové explicitné povolenie
  Martina Jambora. Povolenie je jeden riadok v current/route stave, nie nový
  dokument.

## 7. RC freeze a nezávislý statický audit

RC freeze je jediný bod, kde sa zaznamenáva:

- finálny contract SHA;
- exact source/base/runner/input hashe;
- neprítomnosť official outputu;
- runtime dependency map;
- official príkaz a timeout;
- RC author a odlišný static auditor.

'math_script_auditor' číta exact RC a iba relevantné PF/known-pattern
záznamy. Kontroluje rovnice, znamienka, units/gauge, formula provenance,
stav/RHS/registry parity, generated-versus-executed path, scalar/key
canonicalization, rank/conditioning/scaling/convergence, guard reachability,
runtime closure, deadline headroom a independent holdouty. Nevykonáva
project Python a nevydáva projektový verdict.

Blocker sa vracia do rovnakého DEV source a spotrebuje jednu error udalosť,
ak vyžaduje opravu kandidáta. Nevytvára samostatný auditný súbor; odporúčanie
ostáva v handoff odpovedi alebo existujúcom route ledgeri.

## 8. Official run a vedecký audit

Official je povolený iba ak:

1. contract aj RC hashe sedia;
2. exact RC nie je v DNR;
3. static auditor je odlišný od autora a odporučil PASS;
4. output cieľ neexistuje;
5. 'RUN_AUTHORIZED=true' je zapísané mimo frozen contractu;
6. príkaz má interný aj externý timeout a fail-closed publish.

Official sa publikuje presne raz. Crash, timeout, chýbajúci dependency alebo
schema fail je technická chyba a spotrebuje error udalosť; nie je fyzikálny
výsledok. Immutable raw sa interpretuje až po kontrole hashov.

'physics_track_auditor' overí fyzikálne rovnice a význam, covariance,
conservation, gauge, signs, units, causality, regularity, stability,
holdouty, convergence, null limits a scope. Nesmie dopĺňať autorovu fyziku
ani meniť raw.

## 9. Audit finding triage a claim quarantine

Každý materiálny finding dostane 'FINDING_ID' a jednu triedu:

| Trieda | Claim reach | Povinný prechod |
|---|---|---|
| 'P0_PACKAGE_PROCESS_ONLY' | evidence a vedecký claim nedotknuté | package-repair revision a nový audit submission |
| 'T1_TECHNICAL_NO_CLAIM_REACH' | official claim nedosiahnuteľný chybou | návrat do DEV; invalidovať iba skutočne dotknuté technické outputs |
| 'S1_LOCAL_CORRECTABLE_SAME_TRACK' | claim dotknutý, definujúca fyzika zachovaná | quarantine checkpointu/potomkov, math+physics+philosophy review, návrat na exact bod |
| 'S2_TRACK_IDENTITY_AT_RISK' | oprava môže meniť definujúci mechanizmus | STOP ďalšieho výpočtu a Martin decision gate |
| 'S3_FATAL_IN_SCOPE' | invariantný rozpor v zmrazenom scope | odporúčanie ukončiť scope alebo otvoriť novú koľaj |
| 'S4_PARENT_THEORY_IMPACT' | nález zasahuje rodičovské axiómy/viac koľají | quarantine všetkých dosiahnuteľných potomkov a parent-level decision |

'CLAIM_QUARANTINE' nemení historický raw. Mení jeho použiteľnosť: checkpoint
je 'QUARANTINED_BY_FINDING' a potomkovia 'SUSPENDED_DEPENDENCY'. Žiadny nový
výpočet nesmie používať sporný claim ako prijatý vstup.

### 9.1 Jeden decision record

Pre 'S1–S4' orchestrátor vytvorí alebo aktualizuje jeden route-local
'AUDIT_FINDING_DECISION_RECORD'. Math auditor dodá matematickú/logickú
reachability mapu; physics auditor fyzikálnu a filozoficko-identitnú mapu.
Record obsahuje:

- exact finding, reprodukciu a dôkazový tag;
- earliest invalid checkpoint a transitive downstream set;
- čo ostáva platné;
- matematické, fyzikálne a filozofické riziká opravy;
- 'TRACK_IDENTITY_GATE';
- najmenší bezpečný návratový stav;
- dôsledky troch autorových možností: same-track oprava / new track / STOP.

Filozofický rozmer nie je voľný komentár. Kontroluje sa, či oprava zachováva
bunkovú ontológiu, smer kauzality, lokálnosť/emergenciu, vysvetľovací cieľ a
či nepridáva ad-hoc mechanizmus iba na záchranu dát.

### 9.2 Track identity gate

'SAME_TRACK_CONFIRMED' je možné iba ak sa nemení definujúci mechanizmus,
stavový priestor, interaction topology, causal graph ani ontologický význam
objektov; zmena numerickej metódy, implementácie alebo odvodeného parametra
zvyčajne ostáva v tej istej koľaji.

Zmena definujúcej rovnice/operatora, druhov stavov, conservation closure,
kauzálneho smeru alebo základnej interpretácie vyžaduje
'NEW_TRACK_REQUIRED' alebo 'UNRESOLVED_AUTHOR_DECISION'. Rozhoduje Martin;
auditori iba predložia dôsledky.

### 9.3 Návrat na najskorší chybný bod

| Príčina | Návrat |
|---|---|
| iba chybná interpretácia platného rawu | 'INTERNAL_SCIENCE_AUDIT' |
| official command/input/publication | 'OFFICIAL_RUN_AUTHORIZED' po upstream oprave a guard audite |
| source/prepis/formula implementation | 'DEV_SANDBOX -> nový RC' |
| chybný contract pri potvrdenej same-track identite | 'CONTRACT_DRAFT' |
| track-defining alebo fatal finding | žiadny automatický návrat; Martin decision gate |

Po oprave sa znovu vykonajú iba dotknutý bod a jeho potomkovia. Nezávislé
upstream checkpointy s neporušenými hashmi sa neopakujú.

## 10. Opakovateľný auditný checkpoint a multi-auditor submission

Každý prijatý externe auditovateľný míľnik dostane 'CHECKPOINT_ID', parent
checkpoint IDs, route/gate, accepted state, contract/RC/input/raw/audit hashe,
canonical package ID/manifest hash a status. Register je:

'External_Audits/HISTORY/00_CHECKPOINT_AND_AUDIT_SUBMISSION_REGISTER.tsv'.

Canonical sealed package je immutable auditný snapshot. Rovnaké bajty možno
poslať ľubovoľnému počtu nezávislých auditorov. Každé odovzdanie má unikátny
'AUDIT_SUBMISSION_ID', auditor identity, audit mode, response path/hash a
assessment state. Auditor pred vlastným odovzdaním štandardne nečíta sibling
responses.

Checkpoint package obsahuje '06_CHECKPOINT_PROVENANCE.tsv' s parent IDs,
parent package/manifest hashes a explicitným zoznamom trusted upstream
claims. Auditor môže:

1. auditovať iba vybraný checkpoint s upstream ako hash-bound assumptions;
2. vyžiadať parent packages a prejsť DAG dozadu;
3. pokračovať po registrovaných potomkoch dopredu.

Tak sa dá teória opakovane kontrolovať od ľubovoľného prijatého progress alebo
STOP bodu. Starý checkpoint sa pri findingu nemaže; zmení status a corrected
checkpoint naň odkáže cez 'SUPERSEDES_CHECKPOINT_ID'.

Rozporné externé posudky otvoria 'AUDIT_DISCREPANCY_REVIEW'. Porovná sa
metóda, evidence tagy a reprodukcia; väčšina hlasov sama nerozhoduje.

## 11. Progress a externý audit

Progress review patrí až po ucelenom míľniku, zmene vedeckého blockeru,
official výsledku, goal-drift podozrení alebo gate '10/10'. Bežné DEV
chyby, opravy a RC blocker sa nereviewujú samostatne.

Externý audit sa pripravuje iba ak existuje koherentné tvrdenie:

- uzavretá vedecká brána alebo celý mód;
- autoritatívny fyzikálny STOP;
- významný blocker meniaci route;
- release-critical formula alebo computed result.

Viac blízkych atómov sa spojí do jedného balíka. Technický fail bez rawu
nemá samostatný balík. T2 vyžaduje reprodukovateľný RC, runtime closure,
contract, raw, prahy a príkaz; T3 nezávislú implementáciu.

## 12. Dokumentačný closure

Ucelený vedecký atóm má štandardne najviac:

1. jeden contract/prereg;
2. jeden pracovný base a jeden thin runner, ak ich treba;
3. jeden immutable raw/receipt;
4. jeden výsledkový a interný auditný dokument.

Bežná chyba nevytvára žiadny z týchto dokumentov navyše. Živé plány
obsahujú iba current state, blocker, batch counter a next action. Podrobná
história ostáva v 'HISTORY/' a nevracia sa do current plánu.

Závažný auditný finding smie pridať iba jeden decision record a registry
delta bez ohľadu na počet auditorových komentárov. 'P0' nepridáva vedecký
decision record; iba package repair receipt a nový submission row.

## 13. Handoff capsule

Každý prechod medzi rolami obsahuje:

~~~text
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
INVALIDATED_DESCENDANT_CHECKPOINT_IDS
TRACK_IDENTITY_GATE
CHECKPOINT_ID
PARENT_CHECKPOINT_IDS
CANONICAL_PACKAGE_ID
AUDIT_SUBMISSION_ID
DONE_WHEN
NEXT_ROLE
~~~

Rola vo výstupe zopakuje task ID, prečítané zdroje, zmenené súbory,
vykonané procesy, nonclaims a odporúčaný prechod. Neúplný kapsul, hash drift
alebo porušenie oddelenia rolí znamená 'NO_RUN'.

## 14. Povinný výstup každej zapisujúcej roly

~~~text
TASK_ID
FILES_READ
FILES_CHANGED
PROCESSES_EXECUTED
AUTHORITATIVE_STATE_CHANGE: none|proposed|accepted_by_orchestrator
ERROR_BATCH_INDEX
ERRORS_USED_IN_CURRENT_BATCH
FINDING_CLASS
CHECKPOINT_STATUS
TRACK_IDENTITY_GATE
LIVE_SCIENTIFIC_ARTIFACTS
LIVE_CENTRAL_REGISTERS_UPDATED
LIVE_FILES_CHANGED_TOTAL
AUDIT_PACKAGE_COPIES
NONCLAIMS
RECOMMENDED_NEXT_ROLE
~~~
