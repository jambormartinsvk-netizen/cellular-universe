# B6b-2.12 — D2SW-2 projected-channel balance a worldtube closure contract

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW2-BALANCE-CONTRACT-20260731-460`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Stav:** `DERIVATION_CONTRACT_CANDIDATE / AWAITING_INDEPENDENT_STATIC_AUDIT / NO_RUN`  
**Autor contractu:** OpenAI Codex, hlavný orchestrátor

Tento contract prijíma task457 statický PASS resultu306 a task459
`BOUNDARY_OR_BLOCKER_PROGRESS`. Otvára iba jeden coupled analytický pokus:
z existujúceho `T_CT`, jeho complementu, parent causal worldtube a frozen
conservation ledgera odvodiť mapu `B_CT[Z]`. Nepridáva field, source,
surface dynamics, constitutive law, memory, fit ani energetickú škálu.

## 1. Frozen vstupy

```text
CONTRACT_295_SHA256: BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B
DELTA_295R1_SHA256: 6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD
DELTA_297_SHA256: ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5
TYPED_CONTRACT_303_SHA256: 0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345
CAUSAL_TRACTION_CONTRACT_305_SHA256: 3163534BCBA12123A220A25321FB684E6CAFFCBA01F5F128D6CB8B637631ADC8
ACCEPTED_RESULT_306_SHA256: 74E1A15039C18041C2235B2A8D1D06CD55F11732E246ADDCB553C121D65F8A8D
TASK457_RECOMMENDATION: RECOMMEND_STATIC_AUDIT_PASS
TASK459_PRIMARY_CLASS: BOUNDARY_OR_BLOCKER_PROGRESS
```

Platí regular Landau Type-I nondegenerate doména contractu297,
`V_rec=M_pc`, fixed incidence, unique tangent-to-material-generator branch
a conditional causal-owner doména `D_owner`. Mimo ktorejkoľvek z týchto
domén zostáva vetva fail-closed `LIVE/WAITING`.

## 2. Jediný povolený tensorový split

Contract305 a result306 zmrazili

```text
T_loc=T_CT+T_comp,

T_CT^(mu nu)
 =rho_L u^mu u^nu
 +S_nn n^mu n^nu
 +2n^(mu v^(nu)),

T_comp^(mu nu)
 =(1/2)S_q q^(mu nu)+S_TF^(mu nu),

j_CT^mu=-T_CT^(mu nu)u_nu=rho_L u^mu,
j_comp^mu=-T_comp^(mu nu)u_nu=0.
```

Žiadny ďalší projector, energy-sector split ani presun normal/mixed
traction sektora nie je v D2SW-2 povolený.

Definujeme iba odvodené residualy

```text
Q_loc^nu := nabla_mu T_loc^(mu nu),
Q_CT^nu  := nabla_mu T_CT^(mu nu),
Q_comp^nu:= nabla_mu T_comp^(mu nu),

Q_loc=Q_CT+Q_comp.
```

`Q_*` nie sú nové fields ani voľné sources. Ak accepted parent equations
určujú `Q_loc`, musí sa použiť ich exact hodnota a proveniencia. Ak ju
neurčujú, nesmie sa dosadiť `Q_loc=0`.

Energy a spatial momentum projections sú iba shorthand

```text
e_a:=-u_nu Q_a^nu,
f_a^alpha:=h^alpha_nu Q_a^nu,

e_loc=e_CT+e_comp,
f_loc=f_CT+f_comp,
```

pre `a in {CT,comp,loc}`. Nezavádzajú nový stav.

## 3. Oriented parent-worldtube transport identity

Pre tangent `delta Z` s unique material generator musí existovať jediný
parent worldtube slab

```text
W_p[Z,delta Z]
```

s initial cap `C_-`, final cap `C_+`, side `S_p` a orientation určenou
pre-event `B_rec`. Contract nezmrazuje konvenčné znamienko slovom
„incoming/outgoing“; audit musí najprv overiť directed surface elements.

Pre každý `a in {CT,comp,loc}` sa smie použiť iba exact Stokesova identita

```text
Stokes_a[W_p]
 := integral_(boundary W_p) j_a^mu dSigma_mu
  = integral_(W_p) nabla_mu j_a^mu dV4,

nabla_mu j_a^mu
 =-u_nu Q_a^nu-T_a^(mu nu)nabla_mu u_nu.
```

Pre `a=CT` sa musí explicitne odvodiť cap/side forma s auditovanými
znamienkami. Symboly

```text
Delta E_cap^CT,
Phi_side^CT
```

sú povolené až po definícii cez oriented integrals; nie sú nové energy
stocks. Na comoving side môže byť `j_CT.N=0`, ale z toho sa nesmie odvodiť
nulová traction ani nulové boundary work.

## 4. Stress-power a force-residual bridge

Result306 prijal exact spatial virtual-power identity

```text
beta_traction^CT(delta Z)
 =omega_bulk^CT(delta Z)+R_force^CT(delta Z),

R_force^CT(delta Z)
 =integral_(M_pc)(D_A sigma_CT^(AB))xi_B dV.
```

D2SW-2 musí odvodiť, nie postulovať, vzťah medzi `R_force^CT` a spatial
projection `f_CT`. Povinné je zachytiť všetky acceleration, induced-metric,
embedding/extrinsic-curvature a moving-boundary členy, ktoré vzniknú pri
3+1 projekcii. Povolené sú iba algebraicky odvodené členy z
`T_CT,u_cell,h_rec` a worldtube embeddingu už určeného `Z_rec`.

Ak pre exact accepted geometry neexistuje jednoznačný projection bridge,
výsledok je

```text
LIVE / WAITING_FOR_UNIQUE_PROJECTED_FORCE_AND_WORLDTUBE_GEOMETRY_BRIDGE.
```

Nesmie sa dosadiť `R_force=0`, `f_CT=0`, geodesic `u_cell`, force balance
ani zanedbať embedding term bez accepted dôvodu.

## 5. Jediný cieľový objekt `B_CT[Z]`

Povolený cieľ je jedna spoločná state-functional mapa

```text
B_CT[Z]:
  (Q_CT,Q_comp,Q_loc,
   R_force^CT,
   Delta E_cap^CT,Phi_side^CT,
   omega_bulk^CT,
   w_owner)
  ->
  (beta_boundary^CT,E_res^CT,
   P_store^CT,P_diss^CT,P_RW1export^CT,L_ext^CT).
```

Mapa prejde iba ak každý output je jednoznačne vynútený oriented Stokes,
stress-power/projection bridgeom a frozen ledgerom. Neexistuje samostatná
voľba pre force, current, owner, reservoir alebo complement kanál.

Povinné vlastnosti:

1. `beta_boundary^CT[Z](delta Z)` je quotient-covariant energy-valued
   1-forma, lineárna v `delta Z` a odvodená z toho istého `T_CT` a `W_p`;
2. actual power je iba
   `P_boundary^CT=beta_boundary^CT(D_uZ)=S_in^CT`;
3. `P_rec^CT=omega_bulk^CT(D_uZ)` a compact/expanded zápisy frozen
   ledgera sú alternatívne, nikdy sčítané dvakrát;
4. `Q_CT/Q_comp/Q_loc`, cap change a side flux sa priradia presne raz;
5. internal CT–complement exchange sa v parent sum zruší; accepted external
   source alebo loss ostane explicitný a nesmie sa premenovať na internal;
6. žiadny nový stock vedľa `E_res^CT` a žiadny hidden history term;
7. všetky power outputs majú jednotku `E/T`; 1-formy jednotku `E`;
8. source-off a frozen reservoir bound contractu303 zostávajú zachované.

Frozen identity sa nemení:

```text
P_rec^CT:=omega_bulk^CT(D_uZ),
P_rec^CT=P_store^CT+P_diss^CT+P_RW1export^CT,
P_boundary^CT=S_in^CT,
D_uE_res^CT=P_boundary^CT-P_rec^CT-L_ext^CT.
```

`B_CT` smie iba odvodiť členy tejto identity; nesmie zmeniť jej význam.

## 6. Kernel, contact a uniqueness guards

Na celej

```text
K_iso(Z):={delta Z:delta h_rec[Z]=0}
```

musí odvodená kompletná 1-forma spĺňať

```text
beta_boundary^CT(delta Z)=0
or
beta_boundary^CT(delta Z)
  is exact internal pure transport
  with zero net assigned RW1 work.
```

Result306 rovnosť `beta_traction^CT=R_force^CT` na `K_iso` sama nestačí.
Pure-transport klasifikácia musí byť dôsledok complete `B_CT`, nie label.

Na `D_owner` vstupuje ten istý binary weight `w_(p,c)` do:

```text
traction work,
CT current/cap/side terms,
Q_CT a Q_comp exchange,
reservoir channels,
parent sum.
```

Pre každý shared physical contact musí parent sum dať jednu a iba jednu
kópiu. Mimo `D_owner` platí

```text
LIVE / WAITING_FOR_UNIQUE_PRE_EVENT_CAUSAL_CONTACT_OWNER.
```

Ak Stokes/projection/ledger identity pripúšťa dve fyzikálne rozdielne mapy
`B_CT` na tom istom `Z_rec`, contract neumožňuje vybrať jednu konvenciou:

```text
LIVE / WAITING_FOR_UNIQUE_PROJECTED_CHANNEL_BALANCE_MAP.
```

## 7. Bounded guard matrix

| ID | Povinnosť | PASS podmienka | Fail-closed vetva |
|---|---|---|---|
| `WB0` | orientation/domain | unique worldtube slab a directed caps/side z `Z_rec,B_rec` | `LIVE_WAITING_UNIQUE_WORLDTUBE` |
| `WB1` | Stokes signs | exact cap/side/divergence identity pre CT, complement a total | `REVIEW_STOKES_ORIENTATION` |
| `WB2` | energy projection | `e_loc=e_CT+e_comp`, bez `Q=0` predpokladu | `LIVE_WAITING_LOCAL_SOURCE_PROVENANCE` |
| `WB3` | force bridge | exact `R_force`–`f_CT` relation so všetkými geometry/inertia terms | `LIVE_WAITING_PROJECTED_FORCE_BRIDGE` |
| `WB4` | boundary 1-form | unique quotient-covariant `beta_boundary^CT` z toho istého `T_CT,W_p` | `LIVE_WAITING_BOUNDARY_MAP` |
| `WB5` | ledger | exact-once frozen channel allocation, units, source-off, bound | `REVIEW_CONSERVATION_LEDGER` |
| `WB6` | kernel | complete `G_K(Pi_CT)` na celej `K_iso` | missing-map waiting alebo exact scoped exclusion |
| `WB7` | contacts | rovnaké binary `w` vo všetkých kanáloch a parent sum-one | ambiguity `LIVE_WAITING_OWNER` |
| `WB8` | identity | bez nového field/state/topology/scale/surface dynamics/history | nový obsah=`TRACK_IDENTITY_GATE / MARTIN_DECISION` |

CT3/CT4/CT7 možno označiť PASS iba ak príslušné `WB0–WB8` prešli spolu.
Čiastkové identities sa nesmú agregovať na physical closure.

## 8. Rozhodovacie vetvy

```text
Ak WB0-WB8 určia unique B_CT a complete G_K:
  PASS_D2SW2_PROJECTED_CHANNEL_BALANCE_GUARDS_PENDING_INDEPENDENT_AUDIT;
  potom možno otvoriť D2I, ešte nie D3-D6 ani witness.

Ak chýba local source provenance, worldtube/force bridge, unique balance
map alebo causal owner:
  LIVE / WAITING_FOR_EXACT_MISSING_INPUT;
  C01-RW1, P5 a A2-K4 ostávajú LIVE.

Ak exact unique B_CT poruší frozen kernel, conservation, source-off alebo
reservoir bound bez potreby novej fyziky:
  PRECHECK_EXCLUDED_SCOPE_FOR_CAUSAL_TRACTION_PI_ONLY;
  C01-RW1 ostáva LIVE pre inú author-approved fyzikálnu realizáciu.

Ak closure vyžaduje nový field, state, topology, surface dynamics,
constitutive law, hidden memory alebo fit:
  TRACK_IDENTITY_GATE / MARTIN_DECISION;
  bez rozhodnutia sa nič nepridá.
```

Žiadna vetva tohto contractu sama neuzatvára rodičovskú koľaj.

## 9. Fázový stav a nonclaims

```text
CURRENT_PHASE: D2SW2_BALANCE_CONTRACT307_AWAITING_INDEPENDENT_STATIC_AUDIT
ACTIVE_BLOCKER: PHYSICAL_RW1_SW1_D2SW2_CONTRACT307_STATIC_AUDIT_PENDING
PHYSICAL_TRACK_STATUS: LIVE_ACTIVE_NO_PHYSICAL_WITNESS_NO_STOP
TRACK_IDENTITY_GATE: SAME_TRACK_EXISTING_PHYSICS_DERIVATION_ONLY_PENDING_TASK461
EARLIEST_INVALID_CHECKPOINT_ID: NONE
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
```

- nevznikla `B_CT`, boundary 1-forma ani CT3/CT4/CT7 PASS;
- `Q_CT`, `Q_comp`, cap/side a force residual nie sú nové fields/stocks;
- D2I, D3–D6, RC, raw, checkpoint, package a external audit nevznikli;
- A2-K4 `60/100`, P5 `3.5/6` a error counter sa nemenia.

## 10. Nezávislý statický auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW2-BALANCE-CONTRACT-AUDIT-20260731-461
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_contract293_audit
ARTIFACT_AUTHOR_TASK_ID: /root task460
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_contract293_audit task461
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_OFFICIAL_RAW_OR_MATERIAL_FINDING
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: contract307-author-root-task460_neq-static-auditor-task461
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_D2SW2_BALANCE
CURRENT_PHASE: D2SW2_BALANCE_CONTRACT307_AWAITING_INDEPENDENT_STATIC_AUDIT
ALLOWED_NEXT_ACTION: freeze-contract307-SHA; audit-input-lineage_Q-residual-typing_Stokes-orientation-contract_force-bridge-obligations_BCT-exact-once-ledger_kernel-owner-uniqueness_decision-branches_claim-reach-and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-contracts295_295R1_297_303_305; accepted-result306; exact-contract307; task457_459-responses; task458_460-ledger; math-auditor-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-artifacts; construct-BCT-in-contract-audit; assume-Qloc-QCT-Rforce-zero; choose-among-nonunique-maps; add-new-physics; Python_network_project-code_DEV_RC_official; D2I-D6; project-PASS_STOP_score-depth_checkpoint-package; physics-audit-without-official-raw-or-material-finding
IMMUTABLE_INPUT_PATHS_AND_SHA256: contract303=0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345; contract305=3163534BCBA12123A220A25321FB684E6CAFFCBA01F5F128D6CB8B637631ADC8; result306=74E1A15039C18041C2235B2A8D1D06CD55F11732E246ADDCB553C121D65F8A8D; contract307=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task461-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
FINDING_ID: NONE_OPEN_PENDING_CONTRACT307_AUDIT
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_EXISTING_PHYSICS_DERIVATION_ONLY_PENDING_TASK461
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: task461-verifies-contract307-is-a-bounded-proof-obligation_without-hidden-balance-selection-or-new-physics
NEXT_ROLE: math_script_auditor
```

```text
LIVE_SCIENTIFIC_ARTIFACTS: contracts295_295R1_297_contract305_contract307; total-live=5; result306-historical-accepted-boundary
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
