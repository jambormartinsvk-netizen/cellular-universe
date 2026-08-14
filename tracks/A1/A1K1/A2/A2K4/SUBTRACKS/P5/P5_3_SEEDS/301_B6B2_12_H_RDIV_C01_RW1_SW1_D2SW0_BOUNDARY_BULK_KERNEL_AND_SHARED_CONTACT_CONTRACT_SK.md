# B6b-2.12 — D2SW-0 boundary/bulk kernel a shared-contact guard contract

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW0-CONTRACT-20260731-441`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Stav:** `ANALYTIC_GUARD_CONTRACT_FROZEN / AWAITING_INDEPENDENT_STATIC_AUDIT / NO_RUN`  
**Autor formalizácie:** OpenAI Codex, hlavný orchestrátor  
**Fyzikálny rozsah:** autorom schválený `RW1-SW1` stress-work/current
kandidát a Landauov `u_cell`; bez nového poľa, škály alebo projector voľby

Tento contract prijíma task440 `SCIENTIFIC_GATE_PROGRESS` a otvára iba
najmenší D2SW-0 analytický guard. Nevyberá ani nepredpokladá existenciu
`Pi_SW1` a nemení accepted corrected D1R result300.

## 1. Frozen vstupy

```text
CONTRACT_295_SHA256: BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B
DELTA_295R1_SHA256: 6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD
DELTA_297_SHA256: ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5
ACCEPTED_RESULT_300_SHA256: 0A0F07E13C249DCD51E054185369CFD325971DA5A4253080CA2967AF05AE496A
DOCUMENT_259_SHA256: 9766E5223C7AB95B8D3D3B9914BF8B02034F160F84EF0E47BEE8E4C14EB453E2
DOCUMENT_260_SHA256: 91C25DD777FB9A10B1157F3CF729408B55A3CA264A03E29AA9C2F9E6747CA774
```

Platí signatúra `(-,+,+,+)`, regular Landau doména `D_L`, fixed-incidence
fixed-topology pre-event materiálová vetva, full envelope

```text
V_rec(Z_rec)=M_pc(Z_rec),
h_cell_(mu nu)=g_(mu nu)+u_cell_mu u_cell_nu,
h_rec=X_Z^*h_cell.
```

Opustenie tejto domény ostáva `LIVE / WAITING`, nie scientific STOP.

## 2. Otázka D2SW-0 a DONE_WHEN

D2SW-0 sa pýta iba:

1. aký exact invariantný test musí každý budúci candidate projector splniť,
   aby boundary-current a bulk stress-work boli jedným ledgerom aj na
   extrinsic/isometric smeroch s `delta h_rec=0`;
2. ako musí byť ten istý physical contact contribution pridelený medzi
   incident parent bunky, aby sa nezapočítal viackrát;
3. či accepted current inputs už vyberajú unique projector/accounting map,
   alebo zostáva presný `LIVE / WAITING_FOR` blocker.

```text
DONE_WHEN:
  exact stress-sector decomposition;
  exact K_iso and integration-by-parts identity;
  causal-current kernel test;
  shared-contact partition test;
  candidate-specific PASS/EXCLUDE/WAITING branches;
  no projector-existence or D2SW-closure overclaim.
```

## 3. Landau decomposition existujúceho `T_loc`

Na `D_L` platí

```text
T_loc^(mu nu) u_cell_nu = -rho_L u_cell^mu,
j_loc^mu := -T_loc^(mu nu)u_cell_nu = rho_L u_cell^mu.
```

Pre symmetric `T_loc` je teda jeho Landau decomposition

```text
T_loc^(mu nu) = rho_L u_cell^mu u_cell^nu + S_loc^(mu nu),
S_loc^(mu nu)u_cell_nu=0,
S_loc^(mu nu):=h_cell^mu_alpha h_cell^nu_beta T_loc^(alpha beta).
```

Plný Landau current nemá spatial flux cez boundary, ktorej normála `s^mu`
je priestorová voči `u_cell`, pretože `j_loc^mu s_mu=0`. To samo neznamená
nulovú zmenu lokálnej energie: temporal storage, stress work a flux cez
nekomovnú/contact časť causal worldtube sa musia účtovať v tej istej
conservation identite.

Pre budúci full-tensor projector

```text
T_Pi^(mu nu):=Pi[T_loc]^(mu nu),
j_Pi^mu:=-T_Pi^(mu nu)u_cell_nu,
Pi_comp:=I-Pi
```

sa Landau vlastnosť nesmie automaticky predpokladať. `Pi` a `Pi_comp` musia
byť exact, bezrozmerné, kovariantné a bez overlapu na deklarovanom tensor
space. Čisto spatial projector má `j_Pi=0`; ak pritom dáva nenulový bulk
work, jeho energy supply musí byť explicitne mapovaný do temporal/reservoir
časti toho istého ledgeru a nesmie sa nazvať boundary inflowom.

## 4. Parameter-free spatial stress sektory

Nech `n^mu` je autorom schválená spatial orientation pripravovaného
rozhrania, normalizovaná

```text
u_cell_mu n^mu=0,
n_mu n^mu=1,
q_(mu nu):=h_cell_(mu nu)-n_mu n_nu.
```

Pre každý symmetric spatial stress `S^(mu nu)` definujme

```text
S_nn := n_mu n_nu S^(mu nu),
v_mu := q_mu^alpha S_(alpha beta)n^beta,
S_q := q_(mu nu)S^(mu nu),
S_TF^(mu nu)
 := q^mu_alpha q^nu_beta S^(alpha beta) - (1/2)S_q q^(mu nu).
```

Potom exact reconstruction je

```text
S^(mu nu)
 = S_nn n^mu n^nu
 + 2 n^(mu v^(nu))
 + (1/2)S_q q^(mu nu)
 + S_TF^(mu nu).
```

Tieto štyri normal, mixed, tangential-trace a tangential-traceless sektory
sú navzájom ortogonálne parameter-free image projectory na symmetric
spatial tensor space. Každý ich subset dá algebraicky odlišný idempotentný
spatial projector s disjunktným sektorovým komplementom. Tento contract
preto zakazuje tvrdiť, že samotné `u_cell,n,q` už vybrali unique
`Pi_SW1`. Analytický result musí ukázať, či ďalší existujúci údaj
`B_rec,Sigma_prep,T_loc[Z_rec]` a causal ledger odstráni túto degeneráciu.

Full tensor extension musí navyše jednoznačne rozhodnúť o Landau energy
sector `rho_L u_cell tensor u_cell`. Prideliť ho súčasne `Pi` aj
`Pi_comp` je double count; neprideliť ho žiadnemu kanálu je neuzavretý
energy ledger.

## 5. Bulk virtual work a exact `K_iso`

Pre candidate `Pi` nech

```text
sigma_Pi^(AB):=X_Z^*(h_cell h_cell T_Pi)^(AB),
omega_bulk^Pi[Z](delta Z)
 := (1/2) integral_(M_pc) sigma_Pi^(AB) delta h_rec,AB dV_rec.
```

Definujme

```text
K_iso(Z):={delta Z in T_Z R_reg : delta h_rec[Z]=0}.
```

Potom bez ďalšej fyziky exact platí

```text
delta Z in K_iso(Z) => omega_bulk^Pi[Z](delta Z)=0.
```

Ak je regular materiálová variácia generovaná vektorom `xi^A` na `M_pc`
pri konvencii

```text
delta h_rec,AB=2 D_(A xi_B),
t_Pi^B:=s_A sigma_Pi^(AB),
```

integration by parts dá

```text
omega_bulk^Pi(delta Z)
 = integral_(boundary M_pc) t_Pi^B xi_B dA
   - integral_(M_pc) (D_A sigma_Pi^(AB))xi_B dV.
```

Na `K_iso` teda nie je všeobecne nulový každý boundary traction člen
osobitne; exact je iba rovnosť boundary a bulk-balance člena. Nulová net
physical work vyžaduje derived force/balance closure alebo identifikáciu
zvyšku ako čistého transportu. Ak `delta Z` nemá jednoznačný material
generator `xi`, result nesmie túto formulu použiť; vráti
`LIVE / WAITING_FOR_STATE_TANGENT_TO_MATERIAL_MOTION_MAP`.

## 6. Causal boundary-current kernel guard

Nech `W_pc[Z]` je pre-event causal worldtube full `M_pc` obálky a
`partial_c W_pc` jeho fyzická causal boundary s orientation odvodenou zo
stavu. Candidate `Pi` musí z toho istého `T_Pi` odvodiť oriented current
contribution `Phi_boundary^Pi[Z](delta Z)`; contract nevkladá jeho hodnotu
ani substitute flux.

Povinný kernel guard je

```text
G_K(Pi):
  for every delta Z in K_iso(Z),
  Phi_boundary^Pi[Z](delta Z)=0
  or
  Phi_boundary^Pi is an exact internal pure-transport term
  with zero net assigned RW1 work.
```

Súčasne musí existovať jeden conservation zápis, v ktorom

```text
boundary/current contribution
  = temporal storage change
    + omega_bulk^Pi(D_u Z)
    + declared disjoint export/dissipation terms,
```

s jednotným znamienkom a bez pripočítania `W_rec` ako ďalšieho stocku.
Rovnosť sa nepreukáže iba tým, že obidve strany majú jednotku energie alebo
výkonu.

Ak `Phi_boundary^Pi` dá na niektorom `K_iso` smere nenulovú net RW1 prácu,
candidate je v frozen bulk-form scope nekompatibilný. Nový surface stress,
bending moment, curvature-conjugate state, thickness, field alebo memory
nie je technická oprava a vyžaduje `TRACK_IDENTITY_GATE / MARTIN_DECISION`.

## 7. Shared-contact accounting guard

Nech `I(c)` je množina parent buniek incidentných s existujúcim contact
material region `c`. Každý physical stress/current contribution na `c`
smie v spoločnom ledgeri vstúpiť presne raz. Prípustná accounting mapa má
tvar

```text
w_(p,c)[Z_rec] >= 0,
w_(p,c)=0 for p not in I(c),
sum_(p in I(c)) w_(p,c)=1 almost everywhere on c.
```

Povinné vlastnosti:

- `w_(p,c)` je jednoznačne odvodené z pre-event `B_rec`, physical
  orientation/current a quotient-invariant parent identity;
- žiadny label order, budúci event, daughter state, fit alebo voľný mixing
  parameter;
- ak ide o binary ownership, `w` je `0/1`; ak fyzika vyžaduje split flux,
  nebinárne váhy musia byť odvodené, nie zvolené ad hoc;
- rovnaké `w` sa použije v boundary currente, bulk/contact stress worku aj
  komplementárnom ledgeri;
- súčet parent ledgerov reprodukuje contribution na `c` presne raz.

Samotné tvrdenie „shared contact sa rozdelí na polovicu“ nie je odvodenie,
pokiaľ exact symmetry a quotient jednoznačne nevynútia taký split. Ak
`B_rec` nedáva invariantnú orientation/ownership alebo odvodený split,
výsledok je

```text
LIVE / WAITING_FOR_EXACT_SHARED_CONTACT_ACCOUNTING_MAP.
```

## 8. Analytický screen K0–K9

| ID | Kontrola | PASS podmienka | Fail-closed výsledok |
|---|---|---|---|
| `K0` | epistemický scope | D2SW-0 je guard, nie projector alebo witness | overclaim=`PROCESS_CONTRACT_FAILURE` |
| `K1` | tensor typing | full-tensor `Pi`, `Pi_comp`, spatial `sigma_Pi` a currents sú well-typed | `REVIEW_ILL_TYPED` |
| `K2` | sector completeness | normal/mixed/q-trace/q-TF reconstruction je exact a bez overlapu | `REVIEW_PROJECTOR_DECOMPOSITION` |
| `K3` | energy-sector allocation | `rho_L uu` je pridelené presne raz a current/storage ledger sa uzatvára | `REVIEW_ENERGY_SECTOR_DOUBLE_COUNT_OR_GAP` |
| `K4` | bulk identity | virtual-work units, sign a integration-by-parts formula sedia | `REVIEW_BULK_WORK_IDENTITY` |
| `K5` | isometric kernel | každý `delta h_rec=0` smer má zero bulk work a boundary zero-work/pure-transport closure | candidate fail=`PRECHECK_EXCLUDED_SCOPE_FOR_EXACT_PI`; chýbajúci map=`REVIEW_KERNEL_CLOSURE_OPEN` |
| `K6` | causal/current provenance | boundary functional pochádza z toho istého `T_Pi`, causal pre-event worldtube a orientation | `REVIEW_BOUNDARY_CURRENT_PROVENANCE_OPEN` |
| `K7` | shared contacts | invariantné `w_(p,c)` dá sumu jedna a žiadny double count | `REVIEW_SHARED_CONTACT_ACCOUNTING_OPEN` |
| `K8` | source-off/conservation | bez inputu a rezervoára nevzniká work; storage/export/dissipation sú disjunktné | `REVIEW_CONSERVATION_LEDGER_OPEN` alebo candidate-specific exclusion |
| `K9` | identity/nonclaims | bez nového field, surface/bending law, thickness, scale, dynamics, fitu alebo post-event vstupu | nový obsah=`TRACK_IDENTITY_GATE / MARTIN_DECISION` |

## 9. Zmrazené rozhodovacie vetvy

```text
Ak current accepted inputs vyberú unique Pi a accounting mapu a K0-K9
prejdú:
  PASS_D2SW0_KERNEL_AND_SHARED_CONTACT_GUARD_FOR_EXACT_PI_PENDING_AUDIT;
  ešte nie D2SW projector acceptance, integrability ani witness.

Ak existuje viac než jeden inequivalent parameter-free Pi/accounting map
kompatibilný s rovnakým Z_rec a frozen law nevyberá medzi nimi:
  LIVE / WAITING_FOR_EXACT_RECONFIGURATION_PROJECTOR_OR_ACCOUNTING_MAP.

Ak exact candidate Pi poruší K5, K7 alebo conservation bez novej fyziky:
  PRECHECK_EXCLUDED_SCOPE_FOR_THAT_EXACT_PI_ONLY.

Ak oprava vyžaduje nový surface/bending/curvature state, field, thickness,
memory, dynamics alebo interaction topology:
  TRACK_IDENTITY_GATE / MARTIN_DECISION;
  žiadny automatický same-track successor.

Nenájdenie unique Pi alebo accounting mapy nie je STOP C01-RW1, P5 ani
A2-K4. Koľaj ostáva LIVE / WAITING s presne pomenovaným vstupom.
```

## 10. Fázový stav a nonclaims

```text
CURRENT_PHASE: D2SW0_GUARD_CONTRACT301_AWAITING_INDEPENDENT_STATIC_MATH_LOGIC_AUDIT
ACTIVE_BLOCKER: PHYSICAL_RW1_SW1_D2SW0_GUARD_CONTRACT301_STATIC_AUDIT_PENDING
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
```

- nevznikol ani nebol vybraný `Pi_SW1`;
- neprešla kernel closure, shared-contact map, conservation ani
  integrability;
- nevznikol `E_rec`, `P_rec`, `W_*`, reset, witness, raw alebo checkpoint;
- skóre A2-K4 `60/100` a P5 `3.5/6` sa nemení;
- nevzniká Python, official run, package ani external audit.

## 11. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW0-CONTRACT-AUDIT-20260731-442
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_contract293_audit
ARTIFACT_AUTHOR_TASK_ID: /root task441
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_contract293_audit task442
INTERNAL_AUDITOR_TASK_ID: /root/c01_rw1_d1_d2_physics_audit task436_COMPLETE_D1R_SCOPE_ONLY
PROGRESS_REVIEWER_TASK_ID: /root/c01_rw1_sw1_d1r_progress_review task440_COMPLETE
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: contract301-author-root-task441_neq-static-auditor-task442
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_D2SW0
CURRENT_PHASE: D2SW0_GUARD_CONTRACT301_AWAITING_INDEPENDENT_STATIC_MATH_LOGIC_AUDIT
ALLOWED_NEXT_ACTION: freeze-contract301-SHA; read-only-audit-exact-Landau-decomposition_spatial-sector-projectors_full-tensor-energy-allocation_bulk-integration-by-parts_Kiso-boundary-current-guard_shared-contact-partition_decision-branches_claim-reach-and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-contracts295_295R1_297; accepted-result300; exact-contract301; documents259_260_293_294R1; tasks436_438_440_441; math-auditor-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-artifacts; choose-Pi_or-accounting-map; assume-kernel_conservation_integrability; add-new-physics; Python_network_project-code_DEV_RC_official; D2I-D6; project-PASS_STOP_score_depth_checkpoint-package
IMMUTABLE_INPUT_PATHS_AND_SHA256: parent295=BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B; delta295R1=6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD; delta297=ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5; accepted-result300=0A0F07E13C249DCD51E054185369CFD325971DA5A4253080CA2967AF05AE496A; contract301=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task442-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
FINDING_ID: NONE_OPEN_PENDING_CONTRACT_AUDIT
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CANDIDATE_FOR_GUARD_ONLY_PENDING_TASK442
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: task442-verifies-contract301-is-a-complete-noncircular-guard-with-correct-tensor-identities_and-no-projector-or-new-physics-overclaim
NEXT_ROLE: math_script_auditor
```

```text
LIVE_SCIENTIFIC_ARTIFACTS: contracts295_295R1_297_result300_contract301; total-live=5
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
