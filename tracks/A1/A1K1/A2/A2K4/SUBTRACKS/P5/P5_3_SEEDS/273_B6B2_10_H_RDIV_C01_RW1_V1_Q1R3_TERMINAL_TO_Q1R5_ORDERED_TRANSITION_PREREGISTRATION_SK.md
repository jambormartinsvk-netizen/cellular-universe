# B6b-2.10 — Q1R3 terminál -> Q1R5 ordered-transition preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-TO-Q1R5-TRANSITION-PREREG-20260727-220`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_ORDERED_TRANSITION / NO_SOURCE_OPERATION_YET / NO_PYTHON`

## 1. Jediný cieľ

Cieľom je doplniť chýbajúcu procesnú vetvu frozen dokumentu261 po tom, ako
prvý eligible Q1R3 zostal fyzicky nerozhodnutý a jeho samostatný evidence cap
sa terminálne vyčerpal. Tento dodatok nesmie Q1R3 prekvalifikovať na
neúspešný kandidát. Smie iba povoliť prístupové a eligibility overenie prvého
nasledujúceho neduplikovaného raw ranku bez zmeny pôvodného poradia.

```text
preserved earlier candidate:
  Q1R3 / arXiv 2301.12328
  NOT_ACCEPTED_NOT_EXCLUDED_TERMINAL_SOURCE_CAP_EXHAUSTED
  further Q1R3 source operations = FORBIDDEN
  Q1R3 cap reset = FORBIDDEN

mechanically skipped row:
  Q1R4 = DUPLICATE_OF_Q1R3
  not a physical candidate transition

next inspectable raw rank:
  global rank = 5
  family = F-A
  query = Q1
  query rank = 5
  transition label = Q1R5
  title = Gravitational radiation from first-order phase transitions
          in the presence of a fluid
  arXiv = 1405.4005
  frozen URL = https://arxiv.org/abs/1405.4005
```

Q1R5 ešte nie je `ELIGIBLE_PRIMARY`, complete-W10 kandidát ani fyzikálny
witness. Tento atóm iba rozhodne jeho primary identity, accessibility a
zhodu s frozen F-A eligibility definíciou.

## 2. Immutable vstupy a prijatý stav

```text
frozen source protocol261 SHA256:
  FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B
raw-v2 source ledger264:
  immutable source-order authority for Q1R1-Q4 rows
Q1R3 terminal result272 SHA256:
  7DADCB21EA17040316811015BDC9F941EA84DD575AC5A8FB9A24A6A073153531
Q1R3 terminal receipt271A SHA256:
  20133175CD2B388388110ED1B5D75A4F0016F9A406DC100415EC9B9F77BA694D
current plan SHA256 after task218:
  6FB0B26A034AC49BC3E7AFD004D758C9BB2169B2572FF66FF01CC354BDAFDD63
K4 plan SHA256 after task218:
  82CF80FDD4C70736B283CCD5B7BBC44FBB66BACB6D7CE747B87A73520BC6125E
P5 plan SHA256 after task218:
  37AA6D627312633FA58E61945A9C7E43E1E9FC80E7FE7FC04F4AC3D3D42D7E37
event ledger through task218 SHA256:
  8AB42112E4277763802E8CA094BD62CB824E26C40816048008BF15ADD5E67A14
progress review task219:
  BOUNDARY_OR_BLOCKER_PROGRESS
  ordered-transition protocol required before next-candidate action
```

Autoritatívny stav zostáva K4 `60/100`, P5 `3.5/6`, P4 work atoms `2`,
physical witness attempts `0`, `RUN_AUTHORIZED=false` a blocker
`PHYSICAL_RW1_CARRIER_POWER_THRESHOLD_CONSERVATION_CELL_MEASURE_AND_RESET_NOT_DERIVED`.

## 3. Prečo continuation nie je cherry-picking

Continuation sa riadi výlučne immutable provider poradím. Q1R4 sa preskakuje
iba preto, že už je v raw-v2 ledgeri mechanicky označený ako duplicate Q1R3.
Q1R5 sa nekvalifikuje podľa priaznivého abstraktu ani očakávaného výsledku.

Q1R3 ostáva otvorenou coverage dierou. Preto ani budúci complete W10 z Q1R5
nesmie spätne tvrdiť exhaustive F-A search, fyzické vylúčenie Q1R3 alebo
`REVIEW_NO_COMPLETE_W10...` nad celým frozen poradím. Úspešný neskorší witness
by dokazoval iba existenciu jedného kompletného passportu, čo je deklarovaný
cieľ, nie úplnosť literárneho prehľadu.

## 4. Frozen Q1R5 access/eligibility call

Po nezávislom auditnom PASS, out-of-file SHA freeze a absent-target
preflighte sa vykoná presne jeden batched `web__run/open` call s
`response_length=long`:

```json
{"open":[
  {"ref_id":"https://arxiv.org/abs/1405.4005"},
  {"ref_id":"https://arxiv.org/pdf/1405.4005"}
]}
```

Ide o presne dve Q1R5 internal operations v samostatnom candidate-local
budžete `2/2`. Nie je to reset ani rozšírenie Q1R3 `24/24` lineage. Search,
find, click, iný URL, DOI/publisher fallback, companion, retry, pagination a
ďalšie okno sú v tomto atóme zakázané.

Ak jeden cieľ zlyhá, cache-missne alebo nevráti auditovateľnú same-identity
primary evidenciu, výsledok je iba
`REVIEW_Q1R5_ACCESS_COVERAGE_INCOMPLETE_NO_PHYSICAL_INFERENCE`. Call sa
neopakuje.

## 5. One-call/one-file raw receipt

Exact celý tool return sa v tom istom `functions.exec` publikuje presne raz
do absent cieľa:

`273A_B6B2_10_Q1R5_ACCESS_ELIGIBILITY_RAW.txt`.

Header musí obsahovať exact payload, internal count `2`, candidate-local
budget `2/2`, `BEGIN_EXACT_BATCH_RETURN`, neupravený string alebo
`JSON.stringify(result,null,2)` a `END_EXACT_BATCH_RETURN`. Append, overwrite
a silent repair sú zakázané. Delimiter collision, publication race alebo
neobnoviteľný raw return sú technický fail bez fyzikálnej inferencie.

## 6. Frozen eligibility gate

Výsledok sa publikuje do absent cieľa:

`274_B6B2_10_H_RDIV_C01_RW1_V1_Q1R5_ACCESS_ELIGIBILITY_RESULT_SK.md`.

Povolené vetvy sú úplné:

1. `PASS_Q1R5_ELIGIBLE_PRIMARY_ACCESSIBLE_PENDING_EXPLICIT_S0_S13_SCREEN`,
   iba ak source je pôvodný research paper, same identity, rovnice sú
   čitateľné a samotný model spĺňa frozen F-A vstupnú definíciu: lokálny
   scalar/domain-wall interface model s explicitným fluid/reservoir sektorom
   a relevantným barrier/interface-energy preobrazom;
2. `PRIMARY_OUTSIDE_F_A_REQUIRED_INTERFACE_ACTION`, ak je primárny a
   dostupný, ale source-native model nespĺňa F-A vstupnú definíciu;
3. `SECONDARY_EXCLUDED`, ak nejde o pôvodný research source;
4. `REVIEW_Q1R5_ACCESS_COVERAGE_INCOMPLETE_NO_PHYSICAL_INFERENCE`, ak sa
   identita, equations alebo eligibility nedajú z exact receipt uzavrieť;
5. `REVIEW_Q1R5_ACCESS_TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE` pri
   transportnej/publikačnej/framing chybe.

Eligibility PASS ešte nie je S0–S13 PASS. V tomto atóme sa nesmie vyhlásiť
`SOURCE_EXACT`, `DERIVED_SAME_MODEL`, `E3_MAPPING`, `MISSING`, complete W10,
reference-only výsledok ani candidate-local fyzikálny konflikt. Pri PASS je
ďalším krokom až samostatný source-specific screen prereg; pri inej vetve
nasleduje nezávislý audit a progress review pred ďalším rankom.

## 7. Rozpočet, nonclaims a zákazané kroky

Live vedecké artefakty atómu sú najviac 3: document273, receipt273A a
result274. Opening batch mení iba document273 + existujúci event ledger;
central closure nastane iba po auditovanom prijatí výsledku. Audit package
copies `0`.

Bez ohľadu na vetvu sa v tomto atóme nemenia K4/P5, P4 atoms, witness
attempts, `RUN_AUTHORIZED`, C01 pravda, `A_RW1` emptiness/nonemptiness ani A3.
Python, fit, P5.4, steam/completion, nový ansatz a Q1R3 operation sú zakázané.

## 8. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-TO-Q1R5-TRANSITION-PREREG-AUDIT-20260727-221
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task220
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::task221
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit::RESERVED_DISTINCT_RESULT_AUDIT
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_AUTHOR_PREREG_RESULT_AUDITOR_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R3_TO_Q1R5
CURRENT_PHASE: DRAFT_ORDERED_TRANSITION_BEFORE_ANY_Q1R5_SOURCE_OPERATION
ALLOWED_NEXT_ACTION: independent read-only prereg audit; after PASS, out-of-file SHA freeze and absent-target preflight
ALLOWED_READS: mandatory bootstrap; documents261,264,271-273; receipt271A; result272; ledger tasks209-220; current/K4/P5 plans; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; web/source operation; Python; Q1R3 operation/cap reset; infer Q1R3 fail; choose later rank; physics/passport verdict; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document261=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; result272=7DADCB21EA17040316811015BDC9F941EA84DD575AC5A8FB9A24A6A073153531; receipt271A=20133175CD2B388388110ED1B5D75A4F0016F9A406DC100415EC9B9F77BA694D; current=6FB0B26A034AC49BC3E7AFD004D758C9BB2169B2572FF66FF01CC354BDAFDD63; K4=82CF80FDD4C70736B283CCD5B7BBC44FBB66BACB6D7CE747B87A73520BC6125E; P5=37AA6D627312633FA58E61945A9C7E43E1E9FC80E7FE7FC04F4AC3D3D42D7E37; ledger_through_task218=8AB42112E4277763802E8CA094BD62CB824E26C40816048008BF15ADD5E67A14
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit; after freeze exact receipt273A and result274
DONE_WHEN: Q1R3 terminal preservation, Q1R4 duplicate handling, exact Q1R5 rank/identity, two-operation candidate-local budget, one-call-one-file persistence, eligibility branches, no-cherry-pick nonclaims and three-artifact budget are fail-closed
NEXT_ROLE: main_orchestrator
```

