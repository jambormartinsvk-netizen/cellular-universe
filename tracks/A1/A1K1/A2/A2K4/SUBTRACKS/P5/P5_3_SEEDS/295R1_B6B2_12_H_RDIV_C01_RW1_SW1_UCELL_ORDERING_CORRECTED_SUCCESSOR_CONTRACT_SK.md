# B6b-2.12 — C01-RW1-SW1 corrected successor contract: `u_cell` dependency order

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-CONTRACT-R1-20260730-423`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Autor fyzikálneho vstupu:** Martin Jambor  
**Autor correction delta:** OpenAI Codex, hlavný orchestrátor  
**Stav:** `CORRECTED_SUCCESSOR_CONTRACT / NO_RUN / NO_PYTHON`  
**Supersedes:** contract295 SHA-256
`BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B`

## 1. Dôvod immutable successora

Contract295 správne zmrazil autorov SW1 vstup, state-sufficiency,
stress-work units, integrability, conservation a rozhodovacie vetvy. Po
jeho SHA freeze však autor contractu pri finálnej dependency kontrole našiel:

```text
Pi_SW1, j_SW1 a spatial-stress projection používajú u_cell,
ale tabuľka poradia v contracte295 odvodzuje u_cell až v D5,
za D2SW, D2I, D3 a D4.
```

To je vnútorný dependency cycle. Contract295 sa nemení. Tento successor
opravuje iba poradie odvodenia a presne uvedené odkazy.

```text
DETECTION_STAGE: author-post-freeze-pre-independent-audit
CLAIM_REACH: NONE_no-analytic-result_raw_checkpoint-or-physical-verdict-exists
EARLIEST_AFFECTED_ARTIFACT: contract295
EARLIEST_INVALID_CHECKPOINT_ID: NONE
INVALIDATED_DESCENDANT_CHECKPOINT_IDS: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED
TECHNICAL_ERROR_EVENT: NONE_not-a-failed-candidate-build-test-runtime-or-RC
```

## 2. Efektívny contract

Efektívny auditovaný contract je exact dvojica:

```text
PARENT_CONTRACT:
  295_B6B2_12_H_RDIV_C01_RW1_SW1_STRESS_WORK_D3_D6_DERIVATION_CONTRACT_SK.md
  SHA256=BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B

CORRECTION_DELTA:
  this-contract295R1
  SHA256=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
```

Všetky ustanovenia contractu295 zostávajú účinné okrem explicitných
náhrad v oddiele 3. Pri rozpore má tento correction delta prednosť.

## 3. Exact náhrady

### 3.1 Náhrada D1R

`D1R` sa rozširuje z invariantného state passportu na frame-complete state
passport. Z autorom schváleného lokálneho väzbového grafu, jeho causal
orientation a parent worldtube sa musí odvodiť:

```text
u_cell^mu u_cell_mu = -1,
u_cell^mu je future-directed,
u_cell je lokálne a jednoznačne určené na deklarovanej Type-I/regular doméne.
```

Súčasne sa určia:

- úplné `B_rec,Sigma_prep` a `_rel` quotient;
- reachable regular doména;
- priestorová/material geometry `h_rec,AB` v `u_cell` frame;
- lokálne konečný `V_rec(Z)` bez voľnej interface thickness;
- state-sufficiency podmienka `sigma_SW1=sigma_SW1[Z_rec]`.

Ak schválený graf a geometria neurčia jednoznačný fyzický `u_cell`, D1R
končí

```text
LIVE / WAITING_FOR_EXACT_PARENT_CELL_FRAME_DERIVATION,
```

nie voľbou frame podľa výpočtového výsledku.

### 3.2 Náhrada závislosti D2SW

V contracte295 §4.1 sa spojenie

```text
fyzicky odvodeného u_cell
```

číta presne ako

```text
u_cell odvodeného a auditovaného v D1R.
```

`D2SW` sa nesmie otvoriť, kým D1R frame passport nie je úplný. Potom sa
`Pi_SW1`, `T_SW1`, `j_SW1`, spatial stress, `V_rec` a virtual-work forma
definujú v tom istom frame bez kruhu.

### 3.3 Náhrada D5

Contract295 §7 sa mení iba v prvej odrážke a jej dependency význame:

```text
u_cell sa v D5 už neodvodzuje.
D5 rozšíri D1R-u_cell na regular cell congruence,
odvodí invariantnú lokálne konečnú dmu_cell,
parent retirement, new daughter IDs a R_reset^Z.
```

D5 musí overiť, že congruence a occupation measure používajú ten istý
`u_cell`, ktorý vstúpil do D2SW-D4. Zmena frame medzi blokmi je
`PROCESS_CONTRACT_FAILURE`.

### 3.4 Náhrada DONE_WHEN tabuľky a poradia

Autoritatívne DONE_WHEN sú:

| ID | Blok | DONE_WHEN |
|---|---|---|
| `D1R` | frame-complete state passport | `B_rec,Sigma_prep`, quotient, reachable regular doména, fyzický `u_cell`, `h_rec` a `V_rec` sú úplné bez hidden clocku |
| `D2SW` | stress-work projektor | parameter-free covariant `Pi_SW1` používa D1R frame; má disjunktný komplement a well-typed virtual-work formu |
| `D2I` | integrabilita | `d omega=0`, všetky periods sú nulové a `E_rec[Z]` je single-valued |
| `D3` | power/conservation | causal-current a stress-work formy sú jedno účtovanie; source-off a reservoir ledger sú bez double countu |
| `D4` | completion | `Z_complete` a kladné finite cycle-frozen `W_*` vzniknú z tej istej fyziky a toho istého frame |
| `D5` | congruence/measure/reset | D1R `u_cell` sa rozšíri na regular congruence; odvodia sa `dmu_cell` a physical zero-credit daughter reset |
| `D6` | witness | jeden explicitný reachable stav prejde W0-W12 a regular first passage R0-R11 |

Poradie zostáva

```text
D1R -> D2SW -> D2I -> D3 -> D4 -> D5 -> D6,
```

ale `u_cell` je teraz explicitný výstup D1R a vstup všetkých downstream
blokov.

## 4. Zachované fyzikálne hranice

Successor nemení:

- autorom schválené `B_rec`, `Sigma_prep` ani SW1 source-law triedu;
- zákaz nového poľa a fitovanej energy scale;
- `T_SW1=Pi_SW1[Z]T_loc`, state-sufficiency a disjunktný komplement;
- objemovú stress-work formu s `[omega_SW1]=E`;
- exactness/closed-period integrability guard;
- source-off, reservoir ledger, `W_*`, reset a W0-W12 hranice;
- `RUN_AUTHORIZED=false`, skóre, hĺbku ani checkpointy.

## 5. Rozhodovacie vetvy delty

```text
Ak D1R nedá fyzicky jednoznačný u_cell:
  LIVE / WAITING_FOR_EXACT_PARENT_CELL_FRAME_DERIVATION.

Ak D1R prejde, ale D2SW/D2I nedajú parameter-free integrabilný projector:
  LIVE / WAITING_FOR_EXACT_RECONFIGURATION_STRESS_PROJECTOR_OR_ENERGY_MAP.

Ak konkrétny frame/projector poruší covariance, integrability, conservation
alebo potrebuje fit:
  PRECHECK_EXCLUDED_SCOPE iba pre tento SW1 kandidát.

Ak oprava potrebuje nový field, state species, topology, causal graph alebo
ontológiu:
  TRACK_IDENTITY_GATE / MARTIN_DECISION.
```

Bez fyzikálneho rozporu sa C01-RW1 neuzatvára.

## 6. Fázový stav

```text
CURRENT_PHASE: CORRECTED_SUCCESSOR_CONTRACT_AWAITING_SHA_FREEZE_AND_INDEPENDENT_STATIC_AUDIT
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
```

## 7. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-CONTRACT-R1-AUDIT-20260730-424
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_contract293_audit
ARTIFACT_AUTHOR_TASK_ID: /root task423
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_contract293_audit task424
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_RESULT_OR_RAW
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: contract295R1-author-root_neq-independent-static-auditor-task424
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_R1
CURRENT_PHASE: CORRECTED_SUCCESSOR_CONTRACT_AWAITING_EXTERNAL_SHA_FREEZE_AND_INDEPENDENT_STATIC_AUDIT
ALLOWED_NEXT_ACTION: freeze-exact-contract295R1-SHA; audit-effective-contract-parent295-plus-delta295R1_with-special-focus-on-u-cell-dependency-order_frame-covariance_units_state-sufficiency_integrability_conservation_and-identity
ALLOWED_READS: mandatory-bootstrap; exact-parent-contract295; exact-delta295R1; contract293; accepted-result294R1; documents245_254_256_259_260_292; theory-main-A1-A7-A15; tasks419_420_421_423; role-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-contracts; invent-u-cell_projector_field_scale_Wstar_measure_reset; Python_network_project-code_official; assign-project-PASS_STOP_score_depth_checkpoint-package
IMMUTABLE_INPUT_PATHS_AND_SHA256: parent-contract295=BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B; contract295R1=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT; contract293=BDE7C343F63590400704CA14F773E02F5BD227AAD058DBC4771A3EAF731937B2; result294R1=55C27502135A3260279329B42BC614C8ED7279741CD6FCB84DE0CFA8EB9D4677
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
FINDING_ID: AUTHOR-DETECTED-U-CELL-ORDER-001_CORRECTED_PENDING_AUDIT
FINDING_CLASS: PENDING_INDEPENDENT_CLASSIFICATION_NO_CLAIM_REACH
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED_CANDIDATE_PENDING_AUDIT
CHECKPOINT_ID: NONE
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: auditor-verifies-exact-composite-contract-has-no-u-cell-dependency-cycle_and-preserves-all-parent-guards; returns-PASS-or-earliest-exact-correction
NEXT_ROLE: math_script_auditor
```

## 8. Nonclaims a súborový rozpočet

- nebol odvodený `u_cell`, `Pi_SW1`, `E_rec`, `P_rec`, `W_*`, measure ani reset;
- nevznikol physical witness, raw, checkpoint ani fyzikálny verdict;
- contract295 zostáva immutable a je superseded-before-audit;
- C01-RW1, P5 a A2-K4 zostávajú `LIVE`, nie `CLOSED`.

```text
LIVE_SCIENTIFIC_ARTIFACTS: 1-new-corrected-contract295R1; parent-contract295-retained-superseded; upstream-evidence-unchanged
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
