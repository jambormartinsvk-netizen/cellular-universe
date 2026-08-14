# B6b-2.12 — D2SW-3 korekcia projekcie voľného spatial indexu

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW3-CORRECTION-20260801-481`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Stav:** `CORRECTED_SUCCESSOR_FROZEN / AWAITING_INDEPENDENT_STATIC_AUDIT / NO_RUN / NO_PYTHON`  
**Autor povolenia dávky a fyzikálneho scope:** Martin Jambor  
**Formalizácia:** OpenAI Codex, hlavný orchestrátor

## 1. Povolenie a precedence

Martin Jambor 2026-08-01 výslovne otvoril
`ERROR_BATCH_INDEX=2` pre D2SW3 s najviac desiatimi ďalšími technickými
chybami a povolil iba:

1. opravu free-index spatial projectora v successor contracte;
2. opakovaný nezávislý statický audit;
3. po jeho `PASS` bounded analytický výpočet bez Pythonu a bez official runu.

Immutable blocked predecessor je

```text
CONTRACT_310:
310_B6B2_12_H_RDIV_C01_RW1_SW1_D2SW3_LANDAU_DIVERGENCE_AND_LEDGER_IDENTIFIABILITY_CONTRACT_SK.md

CONTRACT_310_SHA256:
E39F40CD9EACE0378CE20D64666AABB6042394DBE6B78CDAE868E6A00925EBDD

CONTRACT_310_STATUS:
FROZEN_UNCORRECTED_STATIC_AUDIT_BLOCKER_TASK478
```

Tento dokument je minimálny correction delta. Pri kompozitnom čítaní
`contract310 + contract311` nahrádza iba:

- definíciu spatial derivácie v §2 contractu310;
- explicitný spatial-divergence člen a `LD1` v §3/§7 contractu310;
- zastaraný error-batch a auditný handoff v §9/§10 contractu310.

Všetky ostatné rovnice, immutable vstupy, guardy, rozhodovacie vetvy a
nonclaims contractu310 zostávajú bez zmeny. Contract310 sa neprepisuje ani
nemaže.

## 2. Exact corrected spatial derivative

Na regular Landauovej doméne so signatúrou `(-,+,+,+)` platí

```text
h^mu_nu := delta^mu_nu + u^mu u_nu,
u_mu u^mu=-1,
u_mu S_loc^(mu nu)=0.
```

Plne spatial covariant derivácia dvojtensora je

```text
D_beta S_loc^(gamma delta)
 := h_beta^lambda h^gamma_mu h^delta_nu
    nabla_lambda S_loc^(mu nu).
```

Jej kontrahovaná divergencia s explicitne projektovaným voľným indexom je

```text
D_mu S_loc^(mu alpha)
 := h_mu^lambda h^alpha_nu
    nabla_lambda S_loc^(mu nu).
```

Posledný riadok je záväzná explicitná definícia všade, kde sa v kompozitnom
contracte objaví `D_mu S_loc^(mu alpha)`. Neznamená iba projekciu
derivačného indexu.

## 3. Corrected Landau spatial projection

Pre

```text
T_loc^(mu nu)=rho_L u^mu u^nu+S_loc^(mu nu),
Q_loc^nu=nabla_mu T_loc^(mu nu)
```

zostáva časová projekcia contractu310 nezmenená:

```text
e_loc := -u_nu Q_loc^nu
       = D_u rho_L
         + rho_L theta
         + S_loc^(mu nu)nabla_mu u_nu.
```

Spatial projekcia je záväzne

```text
f_loc^alpha := h^alpha_nu Q_loc^nu
             = rho_L a^alpha
               + D_mu S_loc^(mu alpha)
               + S_loc^(mu alpha)a_mu,

D_mu S_loc^(mu alpha)
 := h_mu^lambda h^alpha_nu
    nabla_lambda S_loc^(mu nu),

u_alpha f_loc^alpha=0.
```

Acceleration člen sa neduplikuje. Z ortogonality `u_mu S_loc^(mu nu)=0`
produktové pravidlo dáva

```text
h^alpha_nu nabla_mu S_loc^(mu nu)
 = D_mu S_loc^(mu alpha)+S_loc^(mu alpha)a_mu,
```

preto je uvedený rozklad presne spatial a odstraňuje task478 blocker.

Corrected `LD1` podmienka je:

```text
LD1_PASS
iff
e_loc aj f_loc^alpha sú odvodené s vyššie uvedenou dvojitou spatial
projekciou, správnym znamienkom a u_alpha f_loc^alpha=0.
```

## 4. Nezmenený bounded scope

- `Q_loc^nu=0` sa nesmie predpokladať; platí iba ekvivalencia
  `Q_loc=0 iff e_loc=0 and f_loc=0` na regular vetve.
- CT Stokes identity, `beta_J` bridge guard, ledger matica, rank/nullspace,
  source-off/bounds a identity guard zostávajú presne podľa contractu310.
- Nevzniká nové pole, stav, topológia, surface dynamics, energetická škála,
  hidden memory ani makro/lokálna substitúcia.
- Correction contract sám nie je analytický výsledok ani fyzikálny witness.
- Rodičovská koľaj zostáva `LIVE / WAITING`; tento technický predecessor
  blocker nie je fyzikálny dôvod na jej uzavretie.

```text
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 2
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 16
LAST_FAILED_CANDIDATE_SHA256: E39F40CD9EACE0378CE20D64666AABB6042394DBE6B78CDAE868E6A00925EBDD
```

## 5. Nezávislý statický auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW3-CORRECTION-AUDIT-20260801-482
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_d2sw3_contract_audit
ARTIFACT_AUTHOR_TASK_ID: /root task481
STATIC_AUDITOR_TASK_ID: task482
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_RESULT_OR_MATERIAL_FINDING
PACKAGE_CURATOR_TASK_ID: NONE
EXTERNAL_AUDITOR_TASK_ID: NONE
SEPARATION_OF_DUTIES_CHECK: contract311-author-root-task481_neq-independent-static-auditor-task482
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_D2SW3
CURRENT_PHASE: D2SW3_CONTRACT311_AWAITING_INDEPENDENT_STATIC_AUDIT
ALLOWED_NEXT_ACTION: read-only-static-math-logic-audit-of-exact-contract310-plus-correction-contract311_with-special-check-of-free-index-projector_spatial-orthogonality_acceleration-term_and-unchanged-CT-ledger-guards
ALLOWED_READS: mandatory-bootstrap; exact-contracts297_303_305_307_310_311; exact-result309; task478_480_481; math-auditor-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-artifacts; calculate-result-as-auditor; assume-Qloc-zero_or-T_A7-equals-Tloc; choose-ledger-free-functions; add-new-physics; Python_network_DEV_RC_official; D2I-D6; PASS_STOP-score-depth-checkpoint-package
IMMUTABLE_INPUT_PATHS_AND_SHA256: contract297=ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5; contract303=0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345; contract305=3163534BCBA12123A220A25321FB684E6CAFFCBA01F5F128D6CB8B637631ADC8; contract307=EAA0BE263E3E414D15D070A33FD7AA43CD78DF739ABF8D15C6B2E65369EF8C91; result309=E9240D1DDBF29CC77A34F531ACB282BEF81BB5CCE8971F3D6E6EF96F71FD70E2; contract310=E39F40CD9EACE0378CE20D64666AABB6042394DBE6B78CDAE868E6A00925EBDD; contract311=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task482-static-audit-recommendation
ERROR_BATCH_INDEX: 2
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 16
FINDING_ID: NONE_PENDING_CONTRACT_AUDIT
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_FREE_INDEX_PROJECTOR_CORRECTION_PENDING_TASK482
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: task482-confirms-the-exact-double-spatial-projection-and-composite-contract-before-any-analytic-result
NEXT_ROLE: math_script_auditor
```

```text
LIVE_SCIENTIFIC_ARTIFACTS: contracts295_295R1_297_contract311; total-live=4; contract310-frozen-superseded-blocker; contract307-and-result309-historical-accepted-predecessors; result308-quarantined
LIVE_CENTRAL_REGISTERS_UPDATED: pending-task481-state-batch
LIVE_FILES_CHANGED_TOTAL: pending-task481-state-batch
AUDIT_PACKAGE_COPIES: 0
```
