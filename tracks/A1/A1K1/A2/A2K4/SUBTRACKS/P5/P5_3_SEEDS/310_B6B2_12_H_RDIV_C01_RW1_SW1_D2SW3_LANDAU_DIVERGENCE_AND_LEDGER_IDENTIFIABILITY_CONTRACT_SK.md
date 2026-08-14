# B6b-2.12 — D2SW-3 Landau divergence a identifikovateľnosť reservoir ledgera

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW3-CONTRACT-20260801-477`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Stav:** `AUTHOR_BOUNDED_ATTEMPT_FROZEN / AWAITING_INDEPENDENT_STATIC_AUDIT / NO_RUN / NO_PYTHON`  
**Autor fyzikálneho pokynu:** Martin Jambor  
**Formalizácia:** OpenAI Codex, hlavný orchestrátor

Tento successor contract vykonáva autorov pokyn z 2026-08-01:

```text
Pokus sa opraviť chyby vo výpočte a urobiť výpočet.
```

Pokyn sa v súlade s task476 interpretuje ako povolenie jedného bounded
same-track analytického pokusu. Nepovoľuje nové pole, fitovanú energetickú
škálu, hidden history, budúce informácie, automatické `T_A7=T_loc`, Python
ani official run. Najprv sa odstráni posledná algebraická nejasnosť v
lokálnej Landauovej divergencii a potom sa vypočíta hodnosť frozen
reservoir ledgera.

## 1. Precedence a immutable vstupy

```text
LANDAU_CONTRACT_297_SHA256:
ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5

TYPED_LEDGER_CONTRACT_303_SHA256:
0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345

CAUSAL_TRACTION_CONTRACT_305_SHA256:
3163534BCBA12123A220A25321FB684E6CAFFCBA01F5F128D6CB8B637631ADC8

PROJECTED_BALANCE_CONTRACT_307_SHA256:
EAA0BE263E3E414D15D070A33FD7AA43CD78DF739ABF8D15C6B2E65369EF8C91

CORRECTED_RESULT_309_SHA256:
E9240D1DDBF29CC77A34F531ACB282BEF81BB5CCE8971F3D6E6EF96F71FD70E2
```

Contract307 a result309 zostávajú immutable a používajú sa ako prijaté
historické vstupy. Result308 ostáva v karanténe. Tento contract nesmie
obnoviť `Q_loc=0`, `Q_CT=-Q_comp` ani úplný channel split z resultu308.

Platí regular Landauova doména `D_L`, unique material-worldtube doména
`D_WB`, conditional owner doména `D_owner`, `V_rec=M_pc` a všetky frozen
typing, kernel, source-off a no-double-count guardy contractov303–307.

## 2. Povolený lokálny objekt a derivative-sufficiency doména

Na `D_L` je jediný povolený lokálny tensor

```text
T_loc^(mu nu)[Z]
 = rho_L u^mu u^nu + S_loc^(mu nu),

u_mu S_loc^(mu nu)=0,
u_mu u^mu=-1.
```

Používame iba odvodené veličiny

```text
D_u := u^mu nabla_mu,
theta := nabla_mu u^mu,
a^alpha := u^mu nabla_mu u^alpha,
D_mu := h_mu^nu nabla_nu,
Q_loc^nu := nabla_mu T_loc^(mu nu).
```

Nevzniká nový source field. Analytický výpočet je povolený iba na doméne
`D_J`, kde hladká state-functional mapa `T_loc[Z]` a povolený worldtube
generator určujú jej prvý variation/jet jednoznačne:

```text
dT_loc[Z](delta Z), D_u T_loc[Z], D_mu T_loc[Z]
```

sa musia dať vypočítať z existujúceho `Z_rec`, jeho povoleného tangentu a
existujúcej parent/contact geometrie. `D_J` nepridáva jet ako nový stav;
je to exact sufficiency guard už schválenej hladkej mapy. Ak rovnaký
`Z_rec,delta Z` pripúšťa dva derivative jets, výsledok je

```text
LIVE / WAITING_FOR_UNIQUE_LOCAL_TLOC_DERIVATIVE_PROVENANCE.
```

## 3. Povinný Landau-divergence výpočet

Pri signatúre `(-,+,+,+)` musí výsledok odvodiť produktovým pravidlom

```text
Q_loc^nu = e_loc u^nu + f_loc^nu,
u_nu f_loc^nu=0,

e_loc := -u_nu Q_loc^nu
       = D_u rho_L
         + rho_L theta
         + S_loc^(mu nu)nabla_mu u_nu,

f_loc^alpha := h^alpha_nu Q_loc^nu
             = rho_L a^alpha
               + D_mu S_loc^(mu alpha)
               + S_loc^(mu alpha)a_mu.
```

Audit musí osobitne overiť znamienko časovej projekcie a acceleration člen
v spatial projekcii. Source-off sa nesmie definovať iba nulou jednej
skalárnej projekcie. Exact význam je

```text
Q_loc^nu=0
iff
e_loc=0 and f_loc^alpha=0
```

na deklarovanej regular vetve.

## 4. Opravený CT energy identity

Frozen split zostáva

```text
T_loc=T_CT+T_comp,
j_CT^mu=rho_L u^mu,
j_comp^mu=0,
S_loc=S_CT+S_comp.
```

Preto exact platí

```text
e_comp=S_comp^(mu nu)nabla_mu u_nu,

e_CT=e_loc-e_comp,

e_CT-S_CT^(mu nu)nabla_mu u_nu
 =D_u rho_L+rho_L theta
 =nabla_mu(rho_L u^mu).
```

Povinný worldtube výpočet je teda

```text
Delta E_cap^CT+Phi_side^CT
 =integral_W [D_u rho_L+rho_L theta] dV4
 =integral_W nabla_mu j_CT^mu dV4
 =integral_(boundary W) j_CT^mu dSigma_mu.
```

Toto je kinematická source-provenance identita z toho istého
`T_loc[Z]`; nie je to postulát `Q_loc=0`. Má jednotku energie po integrácii
cez štvorobjem a zachováva oriented cap signs contractu307.

## 5. Candidate current 1-form a bridge guard

Pre infinitesimálny parent slab generovaný `delta Z` sa smie testovať iba

```text
beta_J^CT[Z](delta Z)
 := d/d epsilon|_(epsilon=0)
    integral_(boundary W_p[Z,epsilon delta Z])
      j_CT^mu dSigma_mu.
```

Result musí overiť linearitu v `delta Z`, quotient covariance, orientation
a nulovosť na pure relabel smeroch. `beta_J^CT` je najprv current-transport
1-forma. Nesmie sa bez dôkazu premenovať na fyzickú
`beta_boundary^CT`: rovnosť vyžaduje exact bridge k schválenej causal
traction/stress-work 1-forme z toho istého `T_CT` a worldtube.

Ak sa current transport a traction work líšia o nenulový geometry/source
člen, tento člen musí zostať explicitný. Zakázané je nastaviť ho na nulu
konvenciou.

## 6. Exact hodnosť reservoir ledgera

Po prípadnom určení `P_boundary` a `P_rec` je frozen ledger

```text
P_rec=P_store+P_diss+P_RW1export,

P_boundary
 =D_u E_res
  +P_store+P_diss+P_RW1export+L_ext.
```

Result musí zostaviť neznámy vektor

```text
x=(D_uE_res,P_store,P_diss,P_RW1export,L_ext)^T
```

a maticu

```text
A = [1 1 1 1 1
     0 1 1 1 0],

A x = (P_boundary,P_rec)^T.
```

Povinné je exact rank/nullity vyhodnotenie nad reálnymi lokálnymi power
kanálmi, nie numerický fit. Ak `rank(A)=2`, všeobecné riešenie sa musí
zapísať napríklad pomocou troch voľných fyzikálnych funkcií
`alpha,beta,gamma`:

```text
P_store=alpha,
P_diss=beta,
L_ext=gamma,
P_RW1export=P_rec-alpha-beta,
D_uE_res=P_boundary-P_rec-gamma.
```

Zodpovedajúce null directions sú

```text
v_alpha=(0,1,0,-1,0),
v_beta =(0,0,1,-1,0),
v_gamma=(-1,0,0,0,1).
```

Source-off, sign a reservoir bounds sa majú aplikovať po tomto rank teste.
Ak iba ohraničia `alpha,beta,gamma`, ale neurčia ich, nejde o unique mapu.
Názvy kanálov, minimum-norm voľba ani nastavenie voľných funkcií na nulu
nie sú fyzikálny zákon.

## 7. Guard matrix

| ID | Kontrola | PASS podmienka | Fail-closed výsledok |
|---|---|---|---|
| `LD0` | domain | `D_L ∩ D_WB ∩ D_J` a prípadne `D_owner` je jednoznačná | `LIVE_WAITING_EXACT_DOMAIN` |
| `LD1` | Landau divergence | časová aj spatial projekcia §3 exact | `REVIEW_DIVERGENCE_SIGNS_OR_PROJECTORS` |
| `LD2` | CT Stokes | §4 a oriented caps/side sú identické s contract307 | `REVIEW_STOKES_ORIENTATION` |
| `LD3` | current 1-form | `beta_J` je lineárna, quotient-covariant a source-derived | `LIVE_WAITING_DERIVATIVE_OR_WORLDTUBE_MAP` |
| `LD4` | traction bridge | current a physical boundary-work 1-forma sú exact prepojené so všetkými geometry členmi | `LIVE_WAITING_TRACTION_CURRENT_BRIDGE` |
| `LD5` | ledger rank | exact rank, nullspace a source-off/bound kontroly | `LIVE_WAITING_RANK_THREE_CHANNEL_CLOSURE_MAP` |
| `LD6` | identity | bez nového field/state/topology/scale/history alebo macro/local substitution | nový obsah=`TRACK_IDENTITY_GATE / MARTIN_DECISION` |

## 8. Rozhodovacie vetvy

```text
Ak LD0-LD4 prejdú a LD5 má nullity=0 po už prijatých fyzikálnych zákonoch:
  PASS_D2SW3_UNIQUE_BOUNDARY_AND_CHANNEL_MAP_PENDING_RESULT_AUDIT;
  potom možno otvoriť D2I, ešte nie D3-D6.

Ak Landau divergence a CT Stokes prejdú, ale ledger má nullity=3:
  LIVE / WAITING_FOR_ONE_EXACT_RESERVOIR_CHANNEL_CLOSURE_MAP
  WITH_THREE_INDEPENDENT_SCALAR_CONSTRAINTS;
  parent track zostáva LIVE.

Ak derivative jet alebo traction-current bridge nie je jednoznačný:
  LIVE / WAITING_FOR_EXACT_MISSING_PROVENANCE_OR_BRIDGE.

Ak closure potrebuje nový field, state, topology, surface dynamics,
constitutive scale alebo hidden memory:
  TRACK_IDENTITY_GATE / MARTIN_DECISION.
```

Žiadna vetva tohto contractu sama neuzatvára C01-RW1, P5 ani A2-K4.

## 9. DONE_WHEN a nonclaims

Contract je splnený, keď bounded analytický result:

1. nezávisle od makro A7 vypočíta exact `e_loc,f_loc`;
2. overí zrušenie stress termov v CT Stokes integrande;
3. klasifikuje `beta_J` voči fyzickej traction-work 1-forme;
4. vypočíta `rank(A)`, nullspace a účinok source-off/bounds;
5. vydá iba presný PASS alebo `LIVE/WAITING_FOR_<exact input>`.

```text
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 8/10
CUMULATIVE_TECHNICAL_ERRORS: 14
```

Nevzniká numerický raw, RC, checkpoint, package, score/depth zmena,
physical witness, D2I ani D3-D6. Analytický result sa nesmie vytvoriť pred
nezávislým statickým PASS contractu.

## 10. Nezávislý statický auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW3-CONTRACT-AUDIT-20260801-478
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: TO_BE_ASSIGNED_BY_MAIN_ORCHESTRATOR
ARTIFACT_AUTHOR_TASK_ID: /root task477
STATIC_AUDITOR_TASK_ID: task478
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_RESULT_OR_MATERIAL_FINDING
PACKAGE_CURATOR_TASK_ID: NONE
EXTERNAL_AUDITOR_TASK_ID: NONE
SEPARATION_OF_DUTIES_CHECK: contract310-author-root-task477_neq-task478-independent-static-auditor
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_D2SW3
CURRENT_PHASE: D2SW3_CONTRACT310_AWAITING_INDEPENDENT_STATIC_AUDIT
ALLOWED_NEXT_ACTION: freeze-contract310-SHA-and-audit-author-input-precedence_Landau-divergence-signs_spatial-projector_acceleration-term_CT-Stokes-cancellation_betaJ-linearity-and-typing_ledger-matrix-rank-nullspace_source-off-bounds_decision-branches-and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-contracts297_303_305_307; exact-result309; task470_474_476; exact-contract310; math-auditor-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-artifacts; perform-result-calculation; assume-Qloc-zero_or-T_A7-equals-Tloc; choose-alpha-beta-gamma; add-new-physics; Python_network_DEV_RC_official; D2I-D6; PASS_STOP-score-depth-checkpoint-package
IMMUTABLE_INPUT_PATHS_AND_SHA256: contract297=ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5; contract303=0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345; contract305=3163534BCBA12123A220A25321FB684E6CAFFCBA01F5F128D6CB8B637631ADC8; contract307=EAA0BE263E3E414D15D070A33FD7AA43CD78DF739ABF8D15C6B2E65369EF8C91; result309=E9240D1DDBF29CC77A34F531ACB282BEF81BB5CCE8971F3D6E6EF96F71FD70E2; contract310=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task478-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 8/10
CUMULATIVE_TECHNICAL_ERRORS: 14
FINDING_ID: NONE_PENDING_CONTRACT_AUDIT
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_KINEMATIC_DIVERGENCE_AND_IDENTIFIABILITY_TEST_CANDIDATE_PENDING_TASK478
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: task478-confirms-or-corrects-the-exact-bounded-calculation-contract-before-any-result
NEXT_ROLE: math_script_auditor
```

```text
LIVE_SCIENTIFIC_ARTIFACTS: contracts295_295R1_297_contract310; total-live=4; contract307-and-result309-historical-accepted-predecessors; result308-quarantined
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
