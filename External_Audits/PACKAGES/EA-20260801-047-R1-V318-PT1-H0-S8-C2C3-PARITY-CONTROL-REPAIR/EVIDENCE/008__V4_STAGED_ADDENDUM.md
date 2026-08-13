# V4 addendum: staged execution `n8000` legacy citlivosti `H0/S8`

**Task ID:** `V318-PT1-H0-S8-C2-N8000-STAGED-V4-20260731`  
**Route:** `RELEASE/v3.18/PT1_H0/C2`  
**Stav:** `CONTRACT_DRAFT / RUN_AUTHORIZED=false`  
**Rodič:** V3 SHA
`DC6E8CC12172BD9AF4805870722AA9516A5A48F3824A05FD7A0D5956513E54F7`

## Dôvod a identita koľaje

Šesť V3 cells `n2000/n4000` skončilo
`PASS_GRID_CELL_INTRINSIC`. Pozorované runtime `n4000` bolo
`37.094--44.703 s` z interných `45 s`; priame `n8000` preto nebolo
spustené. V4 nemení rovnice, fyzikálne vstupy, `n=8000`, tolerancie,
komparatory, claim ani cross-cell rozhodovanie. Mení iba execution graph:
spoločný výpočet, ktorý V3 opakoval v každom celli, sa uloží raz ako
immutable hashovo viazaná referencia.

`TRACK_IDENTITY_GATE = SAME_TRACK_CONFIRMED`.

## Official execution graph

```text
REFERENCE_N8000
  -> MODEL_NULL_N8000  -> AGGREGATE_NULL_N8000  -> pôvodný V3 cell raw
  -> MODEL_HALF_N8000  -> AGGREGATE_HALF_N8000  -> pôvodný V3 cell raw
  -> MODEL_FULL_N8000  -> AGGREGATE_FULL_N8000  -> pôvodný V3 cell raw
```

### Referenčný stage

Výstup:
`scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_N8000_REFERENCE_STAGE.json`.

Samostatne počíta `theta_reference`, LCDM anchor pri `n=8000` s
`lambda=delta=Delta N_eff=0` a jeho rast. Exportuje úplné rezíduá,
pozitivitu, root/bracket, kvadratúru, frozen input ledger a
`reference_growth_D`. Úspešný verdict je iba
`PASS_N8000_REFERENCE_STAGE_INTRINSIC`.

### Tri modelové stages

Výstupy:

- `.../RUN_V318_PT1_H0_S8_CELL_NULL_N8000_MODEL_STAGE.json`;
- `.../RUN_V318_PT1_H0_S8_CELL_HALF_N8000_MODEL_STAGE.json`;
- `.../RUN_V318_PT1_H0_S8_CELL_FULL_N8000_MODEL_STAGE.json`.

Každý príkaz dostane exact SHA256 referenčného rawu, pred načítaním ho
overí a fail-closed odmietne nezhodu. Modelový stage počíta iba jeden
modelový anchor/rast pre svoj frozen `Delta N_eff`, používa referenčný
`theta_reference` a `reference_growth_D` a exportuje kompletný V3 point.
Úspešný verdict je `PASS_N8000_MODEL_STAGE_INTRINSIC`.

### Tri agregácie

Agregátor dostane exact SHA referenčného aj príslušného modelového rawu,
overí oba súbory, embedded lineage, cell/grid/Delta mapovanie a všetky
intrinsic guardy. Nevykonáva ODE ani anchor solve. Publikuje presne pôvodné
V3 ciele:

- `RUN_V318_PT1_H0_S8_CELL_NULL_N8000.json`;
- `RUN_V318_PT1_H0_S8_CELL_HALF_N8000.json`;
- `RUN_V318_PT1_H0_S8_CELL_FULL_N8000.json`.

Výstupná schéma a verdict ostávajú V3:
`v318_pt1_h0_s8_grid_cell_v3 / PASS_GRID_CELL_INTRINSIC`. Full comparator
`H0=66.37+/-0.05`, `S8=0.8745+/-0.002` sa pridá iba v agregácii
`full-n8000`.

## Predregistrované očakávania a vetvy

- referenčný/modelový stage: finite native JSON, kladný background,
  sign-change root, žiadny floor/clip, matter residual `<=1e-10`, theta
  residual `<=1e-8`, quadrature error `<=1e-8`;
- očakávaný runtime jedného ťažkého stage je pod `45 s`, pretože V3 cell
  s dvoma takými vetvami trval `37--45 s`; nejde o fyzikálne kritérium;
- agregácia musí trvať pod `5 s` a nesmie volať solve/growth;
- hash/schema/lineage/publish chyba je technická, bez fyzikálneho dosahu;
- `REVIEW_INVALID_BACKGROUND_OR_ROOT` alebo
  `REVIEW_NUMERICAL_CONVERGENCE` zachová kompletný stage raw, ale finálny
  sampled výsledok nemôže byť PASS;
- unexpected crash/timeout nevytvára vedu a rovnaký SHA/stage sa neopakuje;
- platí `NO_SIGN_GATE`; žiadny nový číselný interval sa nepridáva.

Každý ťažký stage má interný limit `45 s` a samostatný externý limit
`60 s`; agregátor interný `5 s`, externý `30 s`. Všetky targety musia byť
pred behom neprítomné a publikovanie je exclusive/atomic.

## DEV a RC

Rovnaký base/runner sa upraví bez vytvárania nového Python súboru. DEV smie
iba `py_compile`, `--help` a syntetický self-test nad dočasnými fake rawmi.
Syntetický test musí overiť hash mismatch, schema/lineage mismatch,
správnu agregáciu a zákaz solvera v agregátore. Nepoužije produkčný
`Delta N_eff`, `n=8000` ani official output.

Po DEV PASS sa zmrazí V4/base/runner SHA. Nezávislý
`math_script_auditor` musí exact RC skontrolovať pred akýmkoľvek stage
behom. Po referenčnom raw sa jeho SHA zapíše do route plánu a modelové
príkazy sa autorizujú s týmto exact hashom; analogicky sa pred každou
agregáciou zmrazí modelový SHA.

## Handoff kapsul

```text
TASK_ID: V318-PT1-H0-S8-C2-N8000-STAGED-V4-DEV-20260731
ROLE: main_orchestrator_as_DEV_source_author
ROLE_CONFIG_SHA256: NOT_APPLICABLE_ROOT_ORCHESTRATOR
ASSIGNED_AGENT_TASK_ID: /root
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/h0_s8_math_auditor
INTERNAL_AUDITOR_TASK_ID: /root/h0_s8_physics_auditor
PACKAGE_CURATOR_TASK_ID: NONE
EXTERNAL_AUDITOR_TASK_ID: NONE
SEPARATION_OF_DUTIES_CHECK: PASS(/root != both auditors)
ROUTE: RELEASE/v3.18/PT1_H0/C2
CURRENT_PHASE: CONTRACT_DRAFT / DEV_SOURCE_UPDATE_PENDING
ALLOWED_NEXT_ACTION: update the same base/runner for staged n8000 execution; no scientific run.
ALLOWED_READS: mandatory bootstrap; V1--V4 contracts; exact RC10; six immutable V3 raw hashes; runtime/checklist/base registers.
ALLOWED_WRITES: scripts/baseScripts/release_v318_h0_s8_legacy_sensitivity_dev.py; scripts/393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py
FORBIDDEN_ACTIONS: no production stage/cell, official output, network, theory edit, verdict, score/depth, equation/threshold change or direct V3 n8000 run.
IMMUTABLE_INPUT_PATHS_AND_SHA256: V3=DC6E8CC12172BD9AF4805870722AA9516A5A48F3824A05FD7A0D5956513E54F7; RC10 base=7E81F87FAEF994A0D9823A5FAD9052B7DB19787564551A15426C18618AE0D982; RC10 runner=28BAFD9011B8D56EA7AC9CC0AA37963950D02EC9133D16F44302921F3392A8EE
PREREG_SHA256: PENDING_V4_HASH
RUN_AUTHORIZED: false
OUTPUT_PATHS: same two DEV source paths only
ERROR_BATCH_INDEX: 2
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 10
LAST_FAILED_CANDIDATE_SHA256: AA368719535B8D5FB6501D69F950F6A9EC680AC17A7CB6B1CF98EA6E11CE4818+517B41FE16BAC420A3943523E152C867BDEAF042C9665C81310EE85E5CC06B92
FINDING_ID: NONE; runtime prevention before failure
FINDING_CLASS: T1_TECHNICAL_NO_CLAIM_REACH_PREVENTED
EARLIEST_INVALID_CHECKPOINT_ID: NONE_PRE_OFFICIAL
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED
CHECKPOINT_ID: NOT_CREATED_PRE_OFFICIAL
PARENT_CHECKPOINT_IDS: NONE
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: staged schema/runner and offline synthetic hash/lineage/aggregate regressions pass DEV.
NEXT_ROLE: main RC freeze, then math_script_auditor
```
