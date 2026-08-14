# B6b-2.12 — D2SW-1 causal-traction coupled contract

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW1-CAUSAL-TRACTION-CONTRACT-20260731-454`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Stav:** `AUTHOR_INPUT_FROZEN / AWAITING_INDEPENDENT_STATIC_AUDIT / NO_RUN`  
**Autor fyzikálneho vstupu:** Martin Jambor  
**Formalizácia:** OpenAI Codex, hlavný orchestrátor

Tento contract reaktivuje exact waiting blocker resultu304 jedným coupled
E3 same-track kandidátom. Nepridáva pole, fitovanú škálu, surface dynamics,
memory ani nový stav. Výber projektora, causal boundary práce a binary
shared-contact ownership sa nesmie rozpojiť na tri nezávislé voľby.

## 1. Autorovo exact rozhodnutie

Martin Jambor schválil:

```text
Schvaľujem ako bounded E3 same-track kandidáta causal-traction projekciu,
ktorá zachová Landau energy sektor a presne normal+mixed traction sektory
P_E+P_nn+P_mix. Boundary work sa odvodí z toho istého T_Pi cez parent
causal worldtube. Shared contact sa pridelí 0/1 jedinému parentovi určenému
pre-event causal orientáciou B_rec; pri nejednoznačnosti zostáva vetva
LIVE/WAITING.
```

Rozhodnutie vyberá jeden exact kandidátsky projector a ownership triedu.
Nevyhlasuje, že worldtube transportná identita, K5–K8, integrabilita,
conservation closure alebo RW1 witness už prešli.

## 2. Frozen vstupy a precedence

```text
CONTRACT_295_SHA256: BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B
DELTA_295R1_SHA256: 6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD
DELTA_297_SHA256: ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5
ACCEPTED_RESULT_300_SHA256: 0A0F07E13C249DCD51E054185369CFD325971DA5A4253080CA2967AF05AE496A
TYPED_CONTRACT_303_SHA256: 0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345
ACCEPTED_BOUNDARY_RESULT_304_SHA256: 14900FD399BD0960FA5D785FAF273E6BB2F99E24AB77B4BB2207B11F4C3EEFD3
```

Platí:

- regular Landau doména `D_L`, signatúra `(-,+,+,+)` a unique
  future-directed unit `u_cell` z contractu297;
- fixed-incidence regular materiálová vetva a `V_rec=M_pc` z resultu300;
- work/power typing, znamienko, `K_iso`, conservation ledger a fail-closed
  vetvy contractu303;
- result304 zostáva historickou prijatou nonselection hranicou, ktorú tento
  nový autorov vstup reaktivuje; jeho tvrdenie o 16/32 algebraických
  alokáciách sa nemení.

Tento contract má prednosť iba pri výbere exact kandidátskej alokácie a
binary causal-owner pravidla. Neobnovuje quarantined časti contractu301.

## 3. Exact causal-traction projector

Na `D_L` má existujúci tensor exact Landau decomposition

```text
T_loc^(mu nu)
 = rho_L u_cell^mu u_cell^nu
 + S_nn n^mu n^nu
 + 2 n^(mu v^(nu))
 + (1/2) S_q q^(mu nu)
 + S_TF^(mu nu),
```

kde

```text
u_cell_mu n^mu=0,
n_mu n^mu=1,
q_(mu nu)=g_(mu nu)+u_cell_mu u_cell_nu-n_mu n_nu,
q_mu_nu n^nu=0,
v_mu n^mu=v_mu u_cell^mu=0,
q_mu_nu S_TF^(mu nu)=0.
```

Na direct-sum priestore Landau energy plus symmetric spatial stress
sektorov definujeme

```text
Pi_CT := P_E + P_nn + P_mix,

T_CT^(mu nu) := Pi_CT[T_loc]^(mu nu)
 = rho_L u_cell^mu u_cell^nu
 + S_nn n^mu n^nu
 + 2 n^(mu v^(nu)),

Pi_comp := I_L - Pi_CT = P_qtr + P_qTF,

T_comp^(mu nu)
 = (1/2)S_q q^(mu nu) + S_TF^(mu nu).
```

`I_L` je identity iba na deklarovanom Landau-decomposed tensor space
reached by `T_loc[Z_rec]`; contract netvrdí nový projector na ľubovoľný
off-domain tensor. Na tomto priestore musí statický audit overiť

```text
Pi_CT^2=Pi_CT,
Pi_comp^2=Pi_comp,
Pi_CT Pi_comp=Pi_comp Pi_CT=0,
Pi_CT+Pi_comp=I_L.
```

Oba projectory sú bezrozmerné a závisia iba od accepted
`u_cell,n,q`. Neobsahujú mixing coefficient, fit, threshold ani energetickú
škálu.

## 4. Prečo presne normal+mixed sektory

Spatial traction na pripravovanom rozhraní je

```text
t_CT^mu := S_CT^(mu nu)n_nu
         = S_nn n^mu + v^mu,
```

pretože

```text
q^(mu nu)n_nu=0,
S_TF^(mu nu)n_nu=0.
```

Normal a mixed sektor sú teda presne sektory viditeľné traction mapou cez
`n`; tangential trace a tangential-TF sektor tvoria disjunktný komplement.
Landau energy sektor sa zachováva v `T_CT`, aby rovnaký full tensor niesol
causal energy/current accounting:

```text
j_CT^mu := -T_CT^(mu nu)u_cell_nu = rho_L u_cell^mu,
j_comp^mu := -T_comp^(mu nu)u_cell_nu = 0.
```

`j_comp=0` neznamená, že complement nemôže niesť internal spatial stress
work. D2SW-1 musí stále preukázať jeho disjunktné účtovanie a zákaz double
countu.

## 5. Parent causal worldtube a boundary-work derivation target

Nech `W_pc[Z]` je pre-event parent causal worldtube full materiálovej
obálky `M_pc` na jednej regular fixed-incidence vetve. Jeho fyzická
orientácia sa odvodí z future orientation `u_cell`, pre-event embeddingu
`X_Z:M_pc->M`, oriented contact incidencie v `B_rec` a pripravovaného
rozhrania `Sigma_prep`.

Pre každý reachable tangent `delta Z` s jednoznačným physical material
generatorom musí D2SW-1 odvodiť z covariant transport theorem lineárnu
state-space 1-formu

```text
beta_boundary^CT[Z](delta Z)
 := TransportWork[T_CT,W_pc,X_Z,B_rec; delta Z] : E.
```

`TransportWork` je derivation target, nie voľná nová funkcia. Analytický
result musí uviesť jeho explicitnú invariantnú integrálnu formu a dokázať:

1. závisí iba od pre-event `T_CT`, `W_pc`, `X_Z`, `B_rec` a `delta Z`;
2. je lineárny v `delta Z` a nulový na pure relabel/gauge tangents;
3. orientácia `beta_boundary>0` znamená net causal energy contribution do
   parent RW1 účtu, bez `abs`, `max`, clampu alebo post-event voľby;
4. pri actual tangente

   ```text
   P_boundary^CT=beta_boundary^CT(D_uZ):E/T;
   ```

5. traction 1-forma a causal-current/worldtube zápis sa stotožnia iba cez
   odvodený transport theorem; nie iba preto, že používajú rovnaký tensor;
6. temporal caps, moving side boundary, storage a spatial stress work sú
   účtované presne raz.

Ak state tangent neurčuje unique physical generator alebo worldtube
orientation, výsledok je

```text
LIVE / WAITING_FOR_UNIQUE_CAUSAL_WORLDTUBE_TRANSPORT_MAP.
```

Žiadny substitute frame, boundary velocity, surface law ani dynamics sa
nesmie doplniť.

## 6. Binary shared-contact causal-owner map

Pre každý existujúci shared contact material region `c` nech `I(c)` je
množina incidentných parent buniek. Pre-event causal orientation v `B_rec`
indukuje pre každého incidentného parenta orientovaný vstupný príznak

```text
epsilon_(p,c)[B_rec] in {-1,0,+1},
```

kde `+1` znamená, že fyzická causal orientation contribution na `c`
smeruje do parent worldtube účtu `p`, `-1` z neho a `0` je tangenciálny
alebo nulový incidence smer. Ide o znamienko existujúcej orientation, nie o
clamp výkonu.

Unique causal owner existuje iba ak

```text
O(c):={p in I(c): epsilon_(p,c)=+1},
|O(c)|=1.
```

Potom pre jediný `owner_B(c)` v `O(c)` definujeme

```text
w_(p,c)[B_rec]
 = 1  pre p=owner_B(c),
 = 0  inak.
```

Tým exact platí

```text
w_(p,c)>=0,
w_(p,c)=0 pre p mimo I(c),
sum_(p in I(c)) w_(p,c)=1.
```

Rovnaké `w` sa musí použiť v `beta_boundary^CT`, `omega_bulk^CT`,
`L_ext`, temporal/storage termoch aj complement ledgeri. Znamienko
fyzického fluxu sa zachová v integrande; binary ownership ho nekladní ani
neprepisuje.

Ak `|O(c)|` nie je presne jedna, `B_rec` orientation chýba, je
degenerovaná alebo nie je quotient-invariantná, exact vetva je

```text
LIVE / WAITING_FOR_UNIQUE_PRE_EVENT_CAUSAL_CONTACT_OWNER.
```

Equal split, label order, magnitude-based normalization, post-event owner
ani daughter identity sú zakázané.

## 7. Bulk work, kernel a conservation povinnosti

Bulk 1-forma je exact parent contract forma pre selected `T_CT`:

```text
sigma_CT^(AB):=X_Z^*(h_cell h_cell T_CT)^(AB),

omega_bulk^CT[Z](delta Z)
 := (1/2) integral_(M_pc) sigma_CT^(AB) delta h_rec,AB dV_rec : E.
```

Na

```text
K_iso(Z):={delta Z:delta h_rec[Z]=0}
```

platí algebraicky `omega_bulk^CT(delta Z)=0`. D2SW-1 však pre selected
kandidáta musí osobitne dokázať

```text
for every delta Z in K_iso:
  beta_boundary^CT(delta Z)=0
  or beta_boundary^CT(delta Z) je exact internal pure transport
     s nulovou net assigned RW1 work.
```

Frozen ledger zostáva

```text
P_rec^CT := omega_bulk^CT(D_uZ),
P_rec^CT=P_store^CT+P_diss^CT+P_RW1export^CT,
P_boundary^CT=S_in^CT,
D_uE_res^CT=P_boundary^CT-P_rec^CT-L_ext^CT.
```

Compact `P_rec=omega_bulk(D_uZ)` a expanded channel formy sú alternatívne,
nie sčítané. Source-off, reservoir bound, disjunktný complement a shared
contact sum-one accounting musia prejsť bez novej scale alebo hidden stocku.

## 8. Bounded analytický screen D2SW-1

| ID | Povinnosť | PASS podmienka | Fail-closed vetva |
|---|---|---|---|
| `CT0` | projector algebra | `Pi_CT=P_E+P_nn+P_mix`, exact idempotence, direct-sum complement | `REVIEW_PROJECTOR_ALGEBRA` |
| `CT1` | traction support | `S_CT n=S_nn n+v`; q-trace/q-TF contraction s `n` je nula | `REVIEW_TRACTION_SECTOR_MAP` |
| `CT2` | causal current | `j_CT=rho_L u_cell`; temporal/spatial sectors bez gapu alebo overlapu | `REVIEW_ENERGY_CURRENT_ALLOCATION` |
| `CT3` | worldtube map | explicitný quotient-covariant `TransportWork` z toho istého `T_CT` | `LIVE_WAITING_FOR_UNIQUE_CAUSAL_WORLDTUBE_TRANSPORT_MAP` |
| `CT4` | kernel | `G_K(Pi_CT)` platí na celej `K_iso` | exact fail=`PRECHECK_EXCLUDED_SCOPE_FOR_CAUSAL_TRACTION_PI` alebo missing-map waiting |
| `CT5` | contact owner | unique pre-event causal owner a binary sum-one `w` | `LIVE_WAITING_FOR_UNIQUE_PRE_EVENT_CAUSAL_CONTACT_OWNER` |
| `CT6` | shared ledger | rovnaké `w` vo všetkých CT/complement kanáloch, žiadny double count | `REVIEW_SHARED_CONTACT_LEDGER` |
| `CT7` | conservation | typed frozen ledger, source-off a reservoir bound | `REVIEW_CONSERVATION_LEDGER` alebo exact candidate exclusion |
| `CT8` | identity | bez nového field/state/topology/scale/surface dynamics | nový obsah=`TRACK_IDENTITY_GATE / MARTIN_DECISION` |

Tento contract sám uzatvára iba výber `Pi_CT` a causal-owner pravidla ako
E3 candidate definition. `CT3–CT7` sú otvorené analytické povinnosti.

## 9. Rozhodovacie vetvy

```text
Ak exact Pi_CT algebra, worldtube TransportWork, G_K, binary owner,
shared ledger a conservation prejdú:
  PASS_D2SW1_CAUSAL_TRACTION_COUPLED_GUARDS_PENDING_INDEPENDENT_AUDIT;
  potom možno otvoriť D2I integrability, ešte nie D3-D6 ani witness.

Ak worldtube/material map alebo causal owner nie je unique:
  LIVE / WAITING_FOR_UNIQUE_CAUSAL_WORLDTUBE_OR_CONTACT_OWNER_MAP.

Ak exact Pi_CT poruší K5, K7 alebo K8 bez potreby novej fyziky:
  PRECHECK_EXCLUDED_SCOPE_FOR_CAUSAL_TRACTION_PI_ONLY;
  C01-RW1 zostáva LIVE.

Ak záchrana vyžaduje nový state, field, interaction topology, surface
stress/bending/curvature law, thickness, memory alebo dynamics:
  TRACK_IDENTITY_GATE / MARTIN_DECISION.

Žiadna waiting ani candidate-specific exclusion vetva nie je STOP celej
C01-RW1, P5 alebo A2-K4 koľaje.
```

## 10. Fázový stav a nonclaims

```text
CURRENT_PHASE: D2SW1_CAUSAL_TRACTION_COUPLED_CONTRACT_AWAITING_INDEPENDENT_STATIC_AUDIT
ACTIVE_BLOCKER: PHYSICAL_RW1_SW1_D2SW1_CONTRACT305_STATIC_AUDIT_PENDING
TRACK_IDENTITY_GATE: SAME_TRACK_AUTHORIZED_BY_MARTIN_FOR_THIS_BOUNDED_E3_CANDIDATE
EARLIEST_INVALID_CHECKPOINT_ID: NONE
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
```

- nevznikla explicitná worldtube transportná 1-forma ani jej PASS;
- K5–K8, D2I, integrability, `E_rec`, D3–D6 a witness zostávajú otvorené;
- nevznikol RC, raw, checkpoint, package ani external audit;
- A2-K4 `60/100` a P5 `3.5/6` sa nemenia.

## 11. Nezávislý statický auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW1-CAUSAL-TRACTION-CONTRACT-AUDIT-20260731-455
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_contract293_audit
ARTIFACT_AUTHOR_TASK_ID: /root task454
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_contract293_audit task455
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_OFFICIAL_RAW_OR_MATERIAL_FINDING
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: contract305-author-root-task454_neq-static-auditor-task455
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_D2SW1_CAUSAL_TRACTION
CURRENT_PHASE: D2SW1_CAUSAL_TRACTION_COUPLED_CONTRACT_AWAITING_INDEPENDENT_STATIC_AUDIT
ALLOWED_NEXT_ACTION: freeze-contract305-SHA; audit-author-input-fidelity_PiCT-projector-algebra_direct-sum-complement_traction-contraction_Landau-current_worldtube-TransportWork-target_binary-causal-owner-map_Kiso_conservation_decision-branches_claim-reach-and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-contracts295_295R1_297_303; accepted-result300; accepted-boundary-result304; exact-contract305; task448_452-responses; task453_454-ledger; math-auditor-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-artifacts; invent-explicit-TransportWork-or-owner-beyond-author-rule; assume-CT3-CT7-PASS; open-D2I-D6; add-new-physics; Python_network_project-code_DEV_RC_official; project-PASS_STOP_score-depth_checkpoint-package; physics-audit-without-official-raw-or-material-finding
IMMUTABLE_INPUT_PATHS_AND_SHA256: contract295=BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B; delta295R1=6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD; delta297=ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5; accepted-result300=0A0F07E13C249DCD51E054185369CFD325971DA5A4253080CA2967AF05AE496A; contract303=0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345; result304=14900FD399BD0960FA5D785FAF273E6BB2F99E24AB77B4BB2207B11F4C3EEFD3; contract305=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task455-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
FINDING_ID: NONE_OPEN_PENDING_CONTRACT_AUDIT
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_AUTHORIZED_BY_MARTIN_FOR_THIS_BOUNDED_E3_CANDIDATE_PENDING_TASK455
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: task455-verifies-contract305-faithfully-freezes-one-coupled-candidate_without-treating-worldtube_owner_kernel_or-conservation-as-passed
NEXT_ROLE: math_script_auditor
```

```text
LIVE_SCIENTIFIC_ARTIFACTS: contracts295_295R1_297_contract303_contract305; total-live=5; result304-historical-accepted-boundary
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
