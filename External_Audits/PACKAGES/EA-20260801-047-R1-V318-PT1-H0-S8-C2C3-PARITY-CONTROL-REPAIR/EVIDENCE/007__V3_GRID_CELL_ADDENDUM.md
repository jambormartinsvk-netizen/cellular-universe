# V3 addendum: grid-cell execution legacy citlivosti `H0/S8`

**Task ID:** `V318-PT1-H0-S8-C2-GRID-CELL-V3-20260731`  
**Route:** `RELEASE/v3.18/PT1_H0/C2`  
**Stav:** `CONTRACT_DRAFT / RUN_AUTHORIZED=false`  
**Rodičia:** V1 SHA `865033E55783EFC48E8C67A8DF71ACE4798ED0E2DF01172F118894B706D07780`,
V2 SHA `C2AAB58C565530DEA8CFC6FB7719B9B662706341A399FBAB0CC5736FD1D9C768`

## Dôvod a nemenné časti

Combined RC8 aj one-point RC9 `null` prekročili interný limit `45 s` bez
rawu. Martin Jambor 2026-07-31 výslovne povolil technickú dávku 2, pokusy
11–20, na grid-sharded opravu.

V3 nemení rovnice, source lineage, konštanty, tri `Delta N_eff` body,
mriežky, tolerancie, komparatory, materiality prahy, claim ani nonclaims.
Mení iba execution packaging: jedna kombinácia fyzikálneho bodu a mriežky
je jeden immutable grid-cell raw.

## Deväť official cells

| Cell ID | `Delta N_eff` | `n` | Official output |
|---|---:|---:|---|
| `null-n2000` | `0` | 2000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_NULL_N2000.json` |
| `null-n4000` | `0` | 4000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_NULL_N4000.json` |
| `null-n8000` | `0` | 8000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_NULL_N8000.json` |
| `half-n2000` | `0.02675` | 2000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_HALF_N2000.json` |
| `half-n4000` | `0.02675` | 4000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_HALF_N4000.json` |
| `half-n8000` | `0.02675` | 8000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_HALF_N8000.json` |
| `full-n2000` | `0.0535` | 2000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_FULL_N2000.json` |
| `full-n4000` | `0.0535` | 4000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_FULL_N4000.json` |
| `full-n8000` | `0.0535` | 8000 | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_CELL_FULL_N8000.json` |

## Jeden cell

Každý cell samostatne a bez mutable cache vypočíta:

1. syntetickú `theta_reference` z V1;
2. LCDM referenčný anchor/rast pri svojom `n`;
3. modelový anchor/rast pre presné `Delta N_eff` a rovnaké `n`;
4. jeden kompletný raw point s intrinsic positivity/root/residual/quadrature,
   native JSON a non-`Delta N_eff` projection rehash guardmi.

Cell nemôže sám udeliť grid-convergence PASS. Jeho úspešný execution verdict
je iba `PASS_GRID_CELL_INTRINSIC`. `REVIEW_*` a unexpected technická vetva
zostávajú podľa V1/F001.

Komparatory `H0=66.37+/-0.05` a `S8=0.8745+/-0.002` sa aplikujú iba v
`full-n8000`. V ostatných ôsmich cells sú explicitne `NOT_APPLICABLE` a
nesmú byť decision checks.

## Cross-cell closure

Sampled výsledok vznikne až z deviatich immutable rawov po nezávislom
science audite:

1. exact cell set a mapovanie bodov/mriežok;
2. všetkých deväť intrinsic verdicts;
3. rovnaký non-`Delta N_eff` projection hash medzi `null/half/full` pri
   rovnakom `n`;
4. pre každý fyzikálny bod signed/absolute `2000→4000`, `4000→8000` a
   ich pomer pre `H0/S8`;
5. V1 high-grid prahy `|H0_8000-H0_4000|<=0.005` a
   `|S8_8000-S8_4000|<=0.0005`;
6. full high-grid comparatory;
7. endpoint delty/materiality až z audited high-grid rawov;
8. `NO_SIGN_GATE`, žiadny posterior, likelihood ani spojitý interval.

Ak cell skončí REVIEW, sampled výsledok je REVIEW. Technický crash/timeout
nevytvára vedu a unchanged SHA/cell sa nespúšťa znovu.

## Runtime, publish a DEV

- každý cell: interný limit `45 s`, vonkajší `60 s`;
- runner povoľuje iba `--official-cell` s deviatimi exact choices;
- pre-computation absent-target, temp + atomic exclusive hard-link a cleanup;
- staré combined/one-point official režimy sú z runnera nedosiahnuteľné;
- DEV iba `py_compile`, `--help`, offline synthetic `--self-test`; žiadny
  production cell ani vedecký bod.

## Handoff kapsul

```text
TASK_ID: V318-PT1-H0-S8-C2-GRID-CELL-V3-DEV-20260731
ROLE: main_orchestrator_as_DEV_source_author
ROLE_CONFIG_SHA256: NOT_APPLICABLE_ROOT_ORCHESTRATOR
ASSIGNED_AGENT_TASK_ID: /root
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/h0_s8_math_auditor
INTERNAL_AUDITOR_TASK_ID: /root/h0_s8_physics_auditor
PACKAGE_CURATOR_TASK_ID: NONE
EXTERNAL_AUDITOR_TASK_ID: NONE
SEPARATION_OF_DUTIES_CHECK: PASS(/root != both auditors; package roles NONE)
ROUTE: RELEASE/v3.18/PT1_H0/C2
CURRENT_PHASE: CONTRACT_DRAFT / DEV_SOURCE_UPDATE
ALLOWED_NEXT_ACTION: modify the same base/runner for exact grid-cell execution; no scientific run.
ALLOWED_READS: mandatory bootstrap; V1/V2/V3 contracts; exact RC9/no-result receipts; runtime/checklist/base registers.
ALLOWED_WRITES: scripts/baseScripts/release_v318_h0_s8_legacy_sensitivity_dev.py; scripts/393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py
FORBIDDEN_ACTIONS: no production cell, official output, network, theory edit, verdict, score/depth or equation/threshold change.
IMMUTABLE_INPUT_PATHS_AND_SHA256: V1=865033E55783EFC48E8C67A8DF71ACE4798ED0E2DF01172F118894B706D07780; V2=C2AAB58C565530DEA8CFC6FB7719B9B662706341A399FBAB0CC5736FD1D9C768; RC9 base=AA368719535B8D5FB6501D69F950F6A9EC680AC17A7CB6B1CF98EA6E11CE4818; RC9 runner=517B41FE16BAC420A3943523E152C867BDEAF042C9665C81310EE85E5CC06B92
PREREG_SHA256: PENDING_V3_HASH
RUN_AUTHORIZED: false
OUTPUT_PATHS: same two DEV source paths only
ERROR_BATCH_INDEX: 2
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 10
LAST_FAILED_CANDIDATE_SHA256: AA368719535B8D5FB6501D69F950F6A9EC680AC17A7CB6B1CF98EA6E11CE4818+517B41FE16BAC420A3943523E152C867BDEAF042C9665C81310EE85E5CC06B92
FINDING_ID: V318-PT1-H0-S8-F001
FINDING_CLASS: S1_LOCAL_CORRECTABLE_SAME_TRACK
EARLIEST_INVALID_CHECKPOINT_ID: NONE
INVALIDATED_DESCENDANT_CHECKPOINT_IDS: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED
CHECKPOINT_ID: NOT_CREATED
PARENT_CHECKPOINT_IDS: NONE
CANONICAL_PACKAGE_ID: NONE
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: exact grid-cell schema/runner and synthetic non-science regressions pass DEV.
NEXT_ROLE: main RC freeze, then math_script_auditor
```
