# V2 addendum: sharded legacy citlivosť `H0/S8`

**Task ID:** `V318-PT1-H0-S8-C2-SHARDED-V2-20260730`  
**Route:** `RELEASE/v3.18/PT1_H0/C2`  
**Stav:** `CONTRACT_DRAFT / RUN_AUTHORIZED=false`  
**Rodič:** frozen V1 contract SHA
`865033E55783EFC48E8C67A8DF71ACE4798ED0E2DF01172F118894B706D07780`

## Dôvod a invarianty

Jednorazový spoločný RC8 proces skončil interným 45-sekundovým timeoutom bez
rawu. V1 výslovne predregistroval, že pri nedostatočnom runtime sa úloha
rozdelí po `Delta N_eff` bodoch a limit sa nepredĺži na neobmedzený čas.

V2 nemení žiadnu rovnicu, znamienko, konštantu, mriežku, toleranciu,
komparator, materiality prah, claim ani nonclaim z V1. Mení iba execution
packaging z jedného procesu na tri nezávislé shardy.

## Shardy a immutable outputy

| Shard | `Delta N_eff` | Official output |
|---|---:|---|
| `null` | `0` | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_SHARD_DNEFF_NULL.json` |
| `half` | `0.02675` | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_SHARD_DNEFF_HALF.json` |
| `full` | `0.0535` | `scripts/results/release_v318_h0_s8/RUN_V318_PT1_H0_S8_SHARD_DNEFF_FULL.json` |

Každý shard samostatne vypočíta `theta_reference`, LCDM referenčný rast a
modelový bod na `n=[2000,4000,8000]`. Tým je samostatne auditovateľný a
nezávisí od mutable cache iného procesu.

## Povinný shard payload

Každý úspešný payload obsahuje:

- `shard_id`, presné `Delta_N_eff`, contract/addendum hash;
- všetky tri raw grid body a high-grid summary;
- `H0`, `Omega_m0`, conditional `sigma8/S8`, `r_s(z_star)`, `D_M`, rast;
- všetky V1 positivity/root/residual/quadrature/grid guardy;
- signed/absolute coarse→medium a medium→high diagnostiku a pomer;
- per-grid canonical non-`Delta_N_eff` input projection a SHA-256;
- rovnaké nonclaims ako V1.

`full` navyše musí prejsť komparatormi
`abs(H0-66.37)<=0.05` a `abs(S8-0.8745)<=0.002`. `null` a `half` tieto
komparatory neaplikujú a nesmú ich vykazovať ako PASS.

## Cross-shard closure

Sampled rozsah možno zostaviť až keď interný science audit potvrdí:

1. presné zoradenie shardov `null/half/full` a body `[0,0.02675,0.0535]`;
2. všetky tri úspešné shard verdicts a native/finiteness;
3. pre každý grid rovnaký non-`Delta_N_eff` projection hash vo všetkých
   shardoch;
4. V1 high-grid a comparator guardy;
5. endpoint rozdiely a materiality sa dopočítajú iba z immutable shard rawov;
6. platí `NO_SIGN_GATE` a nevzniká spojitý interval ani likelihood.

Ak čo i len jeden shard skončí REVIEW, vznikne sampled REVIEW, nie rozsah.
Technický crash/timeout nevytvára vedecký výsledok a unchanged SHA sa
nespúšťa znovu.

## Runtime a publish

- každý shard: interný limit `45 s`, vonkajší `60 s`;
- runner robí pre-computation absent-target guard;
- publish je temp + atomic exclusive hard-link s cleanupom;
- starý combined output ostáva neprítomný a je `RETIRED_NO_RESULT_TARGET`;
- tri shardy sa smú spustiť každý presne raz až po jednom nezávislom static
  audite exact spoločného RC.

## DEV a regresie

DEV smie iba `py_compile`, `--help`, a offline `--self-test`. Fixture používa
iba nevedecké štítky. Musí testovať spoločný one-shard output builder,
tri-grid diagnostiku, tri-state REVIEW, unexpected-error propagation,
native JSON a collision cleanup. Nesmie volať reálny `run_one_point`.

## Handoff kapsul

```text
TASK_ID: V318-PT1-H0-S8-C2-SHARDED-V2-DEV-20260730
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
ALLOWED_NEXT_ACTION: modify the same allowlisted base/runner for exact one-point sharding; no scientific run.
ALLOWED_READS: mandatory bootstrap; V1 contract, this addendum, exact RC8 and receipt, runtime/checklist/base registers.
ALLOWED_WRITES: scripts/baseScripts/release_v318_h0_s8_legacy_sensitivity_dev.py; scripts/393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py
FORBIDDEN_ACTIONS: no scientific point execution, official output, network, theory edit, verdict, score/depth or parameter/equation/threshold change.
IMMUTABLE_INPUT_PATHS_AND_SHA256: V1 contract=865033E55783EFC48E8C67A8DF71ACE4798ED0E2DF01172F118894B706D07780; RC8 base=7D1462117BDB01054E403F1B5FD535B2C619914F4C71F8D68F8EB849CFADCCF6; RC8 runner=D01C1E3F36F4BFA96F4CEEDB98FA29180AEDFCE2E184B83FB457FB2837AD96D9
PREREG_SHA256: PENDING_ADDENDUM_HASH
RUN_AUTHORIZED: false
OUTPUT_PATHS: same two DEV source paths only
ERROR_BATCH_INDEX: 1
ERRORS_USED_IN_CURRENT_BATCH: 8/10
CUMULATIVE_TECHNICAL_ERRORS: 8
LAST_FAILED_CANDIDATE_SHA256: 7D1462117BDB01054E403F1B5FD535B2C619914F4C71F8D68F8EB849CFADCCF6+D01C1E3F36F4BFA96F4CEEDB98FA29180AEDFCE2E184B83FB457FB2837AD96D9
FINDING_ID: V318-PT1-H0-S8-F001
FINDING_CLASS: S1_LOCAL_CORRECTABLE_SAME_TRACK
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED
CHECKPOINT_ID: NOT_CREATED
PARENT_CHECKPOINT_IDS: NONE
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: DEV source implements exact independent shard schema and guards and passes only synthetic DEV suite.
NEXT_ROLE: main RC freeze, then math_script_auditor
```
