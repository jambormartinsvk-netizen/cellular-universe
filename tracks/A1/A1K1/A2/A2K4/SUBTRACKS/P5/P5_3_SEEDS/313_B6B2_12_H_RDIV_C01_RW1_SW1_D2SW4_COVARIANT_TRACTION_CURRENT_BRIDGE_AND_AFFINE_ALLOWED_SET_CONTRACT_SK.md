# B6b-2.12 — D2SW-4 covariant traction–current bridge a affine allowed set

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW4-CONTRACT-20260801-489`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Stav:** `AUTHOR_BOUNDED_SET_VALUED_INPUT_FROZEN / AWAITING_INDEPENDENT_STATIC_MATH_AUDIT / NO_RUN / NO_PYTHON`  
**Autor fyzikálneho vstupu:** Martin Jambor  
**Formalizácia:** OpenAI Codex, hlavný orchestrátor

Tento successor contract otvára nový bounded same-track fyzikálny atóm po
prijatom result312. Nežiada unique reservoir channel map. Povoleným
vedeckým výstupom je úplná množina riešení frozen ledgera, pričom
traction–current bridge musí zostať covariantný a musí niesť všetky
intrinsic, moving-boundary, metric/embedding, source, cap, side a owner
členy. Žiadny z nich sa nesmie vynulovať konvenciou.

## 1. Autorovo exact rozhodnutie

Martin Jambor schválil:

```text
Schvaľujem bounded same-track set-valued successor na D_* ∩ D_owner,
úplný covariant traction–current bridge so všetkými geometry členmi a
reservoir affine allowed set bez nových polí, škál alebo svojvoľného
nastavenia null smerov.
```

Toto rozhodnutie:

1. obmedzuje successor na `D_* intersection D_owner`;
2. povoľuje nenulový geometry/source rozdiel medzi traction work a current
   transportom, ak je úplne odvodený z existujúcich objektov;
3. prijíma set-valued reservoir mapu ako cieľ, nie ako technické zlyhanie;
4. nepovoľuje nový field, state, scale, surface dynamics, hidden history,
   fit, minimum-norm výber ani voľbu null smerov podľa názvu kanála;
5. nie je povolením Pythonu, siete, DEV/RC/official runu ani publikácie.

## 2. Precedence a immutable vstupy

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

D2SW3_CORRECTION_CONTRACT_311_SHA256:
C96B403157EB18B087B4E2DDC2E994E3E9986E25D294F39828E7F22FDC5460C3

ACCEPTED_RESULT_312_SHA256:
DE24556A70952EDEDE8312EA39B5A594024334C229923B47528474A4687E4893
```

Contracty303, 305, 307, 311 a výsledky309, 312 zostávajú immutable.
Result308 zostáva v karanténe a contract310 je frozen superseded blocker.
Tento contract nesmie obnoviť `Q_loc=0`, `Q_CT=-Q_comp`, nulový bridge ani
unique channel split.

## 3. Exact doména a existujúce objekty

Používa sa iba

```text
D_SV := D_* intersection D_owner,
D_*  := D_L intersection D_WB intersection D_J.
```

Na `D_SV` sú jednoznačné a hladké:

- future-directed unit Landau frame `u_cell` a `h_cell`;
- `T_loc[Z_rec]`, `T_CT=Pi_CT[T_loc]`, `j_CT^mu=rho_L u_cell^mu` a ich
  povolený prvý derivative jet;
- parent causal worldtube `W_pc[Z]`, jeho pre-event embedding, orientation,
  cap/side decomposition a material generator `xi[delta Z]`;
- binary shared-contact weights `w_(p,c)` odvodené z pre-event causal
  orientácie `B_rec`.

Mimo `D_SV` je výsledok presne

```text
LIVE / WAITING_FOR_EXACT_LANDAU_DERIVATIVE_WORLDTUBE_OR_CAUSAL_OWNER_DOMAIN.
```

Nevkladá sa clamp, substitute frame, post-event owner, svojvoľná null
orientácia ani rozšírenie domény.

## 4. Covariant current transport vrátane geometry členov

Nech `epsilon_g` je existujúca oriented spacetime volume 4-forma a

```text
J_CT := i_(j_CT) epsilon_g
```

je current 3-forma. Potom exact

```text
d J_CT = (nabla_mu j_CT^mu) epsilon_g.
```

Pre tangent `delta Z` označme `dot J_CT[delta Z]` intrinsic Eulerian
variation pri fixovanom embeddingu. Derivácia pullbacku na pohybujúci sa
parent worldtube je

```text
delta_pull J_CT
 := dot J_CT[delta Z] + L_xi J_CT.
```

Úplná current-transport 1-forma je preto

```text
beta_J^CT[Z](delta Z)
 := integral_(boundary W_pc) delta_pull J_CT
  = integral_(boundary W_pc)
      [dot J_CT[delta Z] + i_xi dJ_CT + d(i_xi J_CT)].
```

Na complete oriented `boundary W_pc` sa exact-form člen zruší až po
spoločnom započítaní oboch caps, side boundary, corners a rovnakých owner
weights:

```text
sum_(caps+side) integral d(i_xi J_CT)=0.
```

Nesmie sa zahodiť na jednotlivom face ani pred overením corner cancellation.
Po tejto kontrole možno použiť skrátený tvar

```text
beta_J^CT
 = integral_(boundary W_pc) dot J_CT[delta Z]
   + integral_(boundary W_pc) i_xi dJ_CT.
```

Toto je explicitný Cartan/Reynolds shape derivative. `dot J_CT` ani `xi`
nie sú nové polia: sú určené hladkou mapou `T_loc[Z_rec]`, existujúcim
worldtube embeddingom a tangenciou `delta Z` na `D_SV`.

## 5. Covariant traction/stress-work identita

Definujme odvodený local residual

```text
Q_CT^nu := nabla_mu T_CT^(mu nu).
```

Pre symmetric `T_CT` a ten istý generator `xi` platí pointwise Noetherova
identita

```text
nabla_mu(T_CT^(mu nu) xi_nu)
 = Q_CT^nu xi_nu
   + (1/2) T_CT^(mu nu) (L_xi g)_(mu nu).
```

Po integrácii cez celý oriented parent worldtube:

```text
B_T^CT[Z](delta Z)
 := integral_(boundary W_pc) T_CT^(mu nu) xi_nu dSigma_mu
  = integral_(W_pc)
      [Q_CT^nu xi_nu
       +(1/2)T_CT^(mu nu)(L_xi g)_(mu nu)] dV4.
```

Face signs a binary owner weights sa preberajú z tej istej pre-event
orientation ako v §4. Incoming convention contractu303 sa aplikuje jednou
odvodenou orientation mapou `Orient_in[B_rec]`; nie je to voľný sign ani
clamp. Výsledná energy-valued traction/stress-work 1-forma je

```text
beta_T^CT := Orient_in[B_rec](B_T^CT).
```

Analytický result musí rozložiť túto formu na temporal caps, moving side,
normal+mixed traction, metric/embedding work a `Q_CT` source časť. Musí
ukázať, že tangential complement, ktorý nie je v `Pi_CT`, sa nepripíše do
CT účtu a že shared contact dostane presne jeden owner weight.

## 6. Úplný traction–current bridge

Fyzická boundary-work forma tohto kandidáta je traction/stress-work forma
odvodená z toho istého `T_CT`:

```text
beta_boundary^CT := beta_T^CT.
```

Úplný covariant bridge je identita

```text
beta_boundary^CT
 = beta_J^CT + beta_geo/src^CT,

beta_geo/src^CT
 := Orient_in[B_rec]
      integral_(W_pc)
       [Q_CT^nu xi_nu
        +(1/2)T_CT^(mu nu)(L_xi g)_(mu nu)] dV4
    - integral_(boundary W_pc)
       [dot J_CT[delta Z]
        +i_xi dJ_CT
        +d(i_xi J_CT)].
```

`beta_geo/src^CT` je názov pre úplne rozvinutý rozdiel existujúcich
traction a current výrazov, nie nový constitutive člen. Bounded analytický
result musí:

1. dosadiť `j_CT=rho_L u_cell`, `dJ_CT=(nabla.j_CT)epsilon_g` a
   `Q_CT=nabla.T_CT`;
2. uviesť intrinsic-current, moving-boundary, cap, side, corner,
   metric/embedding, traction, source a owner príspevky s exact znamienkami;
3. overiť linearitu v `delta Z`, quotient covariance a nulovosť na pure
   relabel tangente;
4. ponechať každý nenulový term explicitný a započítať ho presne raz;
5. overiť units `E` pre 1-formy a až potom definovať
   `P_boundary^CT=beta_boundary^CT(D_uZ):E/T`;
6. zlyhať closed, ak ľubovoľný člen nie je single-valued funkciou
   existujúceho `Z_rec`, geometrie a povoleného tangentu.

Zakázané sú skratky

```text
beta_boundary^CT=beta_J^CT,
beta_geo/src^CT=0,
Q_CT=0,
L_xi g=0
```

bez exact dôkazu na celej deklarovanej doméne. Bridge PASS nevyžaduje, aby
`beta_geo/src^CT` bol nulový; vyžaduje jeho úplnosť a existujúcu
provenienciu.

## 7. Reservoir affine allowed set

Po vyhodnotení bridge na actual tangente zostáva frozen ledger

```text
P_rec=P_store+P_diss+P_RW1export,

P_boundary
 =D_uE_res+P_store+P_diss+P_RW1export+L_ext.
```

Pre

```text
x=(D_uE_res,P_store,P_diss,P_RW1export,L_ext)^T,

A=[1 1 1 1 1
   0 1 1 1 0],

b(Z)=(P_boundary(Z),P_rec(Z))^T
```

definujeme affine solution space

```text
S_aff(Z):={x in R^5 : A x=b(Z)}.
```

Jeho povolený parametrizačný origin a exact kernel basis sú

```text
x_0(Z)=(P_boundary-P_rec,0,0,P_rec,0)^T,

v_alpha=(0,1,0,-1,0)^T,
v_beta =(0,0,1,-1,0)^T,
v_gamma=(-1,0,0,0,1)^T,

x=x_0+alpha v_alpha+beta v_beta+gamma v_gamma.
```

`x_0` je iba súradnicový origin affine priestoru. Nie je to fyzický výber
`alpha=beta=gamma=0`.

Nech `C_existing(Z)` označuje presne frozen source-off, sign, reservoir,
kernel, complement, no-double-count a binary-owner guardy contractov303,
305 a 307 bez novej nerovnosti alebo scale. Fyzickým set-valued výstupom je

```text
A_res^CT(Z)
 := S_aff(Z) intersection C_existing(Z)
  = {x_0+alpha v_alpha+beta v_beta+gamma v_gamma
     : all existing guards hold}.
```

Analytický result musí určiť, ktoré existujúce guardy obmedzujú
`alpha,beta,gamma`, a musí vrátiť celú množinu. Nesmie vybrať jej prvok
minimum normou, regularizáciou, entropickým pravidlom, názvom kanála,
priorom, fitom ani ľubovoľným nastavením null smerov. Workflow je bounded;
matematická množina sa nesmie vyhlásiť za kompaktnú alebo jednoznačnú, ak
to existing guards nedokazujú.

## 8. Guard matrix

| ID | Povinnosť | PASS podmienka | Fail-closed vetva |
|---|---|---|---|
| `SV0` | domain | exact `D_SV=D_* intersection D_owner` | `LIVE_WAITING_EXACT_DOMAIN_OR_OWNER` |
| `SV1` | current shape derivative | Cartan/Reynolds forma vrátane cap/side/corner a owner accounting | `REVIEW_CURRENT_GEOMETRY_LEDGER` |
| `SV2` | traction Noether identity | `Q_CT.xi+(1/2)T_CT:L_xi g` a full boundary orientation exact | `REVIEW_TRACTION_SOURCE_OR_GEOMETRY_SIGNS` |
| `SV3` | complete bridge | `beta_boundary=beta_J+beta_geo/src`; každý term existing, single-valued a započítaný raz | `LIVE_WAITING_COMPLETE_TRACTION_CURRENT_BRIDGE` |
| `SV4` | typing | 1-formy majú `E`; powers vzniknú iba evaluation na `D_uZ` a majú `E/T` | `REVIEW_WORK_POWER_TYPING` |
| `SV5` | affine algebra | `rank(A)=2`, `ker(A)=span(v_alpha,v_beta,v_gamma)` a `Ax_0=b` | `REVIEW_AFFINE_LEDGER_ALGEBRA` |
| `SV6` | allowed set | presne `S_aff intersection C_existing`, bez selection null smerov | `REVIEW_ALLOWED_SET_OR_HIDDEN_SELECTION` |
| `SV7` | source/kernel/contact | frozen source-off, `G_K`, complement a binary sum-one accounting | exact exclusion alebo domain-specific `LIVE/WAITING` |
| `SV8` | identity | bez nového field/state/topology/scale/history/surface law alebo macro-local substitution | nový obsah=`TRACK_IDENTITY_GATE / MARTIN_DECISION` |

## 9. Rozhodovacie vetvy

```text
Ak SV0-SV8 prejdú a A_res^CT(Z) je neprázdna:
  PASS_D2SW4_SET_VALUED_BOUNDARY_AND_RESERVOIR_MAP_PENDING_RESULT_AUDIT;
  povoleným výsledkom je celá A_res^CT(Z), nie unique channel tuple.

Ak bridge term nie je určený existujúcim Z_rec/worldtube/jet:
  LIVE / WAITING_FOR_EXACT_MISSING_TRACTION_CURRENT_GEOMETRY_PROVENANCE.

Ak D_owner nie je unique:
  LIVE / WAITING_FOR_UNIQUE_PRE_EVENT_CAUSAL_CONTACT_OWNER.

Ak A_res^CT(Z) je prázdna iba na presne určenej reachable poddoméne po
aplikovaní existing guards:
  PRECHECK_EXCLUDED_FOR_EXACT_STATE_OR_SUBDOMAIN_ONLY;
  parent C01-RW1, P5 a A2-K4 zostávajú LIVE / WAITING.

Ak nonempty allowed set alebo bridge vyžaduje nový field, state, topology,
scale, surface dynamics, hidden memory alebo arbitrary null selection:
  TRACK_IDENTITY_GATE / MARTIN_DECISION.
```

Po prijatom nezávislom audite bounded resultu možno otvoriť iba set-valued
`D2I` integrability successor. D3–D6, RW1 witness, P5.4, G8 a G9 sa týmto
contractom neotvárajú. Žiadna vetva sama neuzatvára rodičovskú koľaj bez
fyzikálneho dôvodu a autorovho rozhodnutia.

## 10. DONE_WHEN, povolenia a nonclaims

Contract je splnený, keď budúci bounded analytický result bez Pythonu:

1. explicitne odvodí full bridge §§4–6 na `D_SV`;
2. overí všetky geometry/source/owner znamienka a no-double-count;
3. zostaví `A_res^CT(Z)` ako celý affine-intersection výstup;
4. oddelí nonempty, empty-subdomain a missing-provenance vetvu;
5. vydá iba exact bounded záver bez unique-channel alebo witness overclaimu.

```text
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_D2SW4_SET_VALUED_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 16
```

Nevzniká Python, DEV/RC/official run, numerický raw, fit, observable,
checkpoint, package, score/depth zmena ani release claim. Analytický result
sa nesmie vytvoriť pred nezávislým staticko-matematickým PASS contractu.

## 11. Nezávislý staticko-matematický auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW4-CONTRACT-AUDIT-20260801-490
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_d2sw3_contract_audit
ARTIFACT_AUTHOR_TASK_ID: /root task489
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_d2sw3_contract_audit task490
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_RESULT_OR_MATERIAL_FINDING
PACKAGE_CURATOR_TASK_ID: NONE
EXTERNAL_AUDITOR_TASK_ID: NONE
SEPARATION_OF_DUTIES_CHECK: contract313-author-root-task489_neq-task490-independent-static-auditor
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_D2SW4
CURRENT_PHASE: D2SW4_CONTRACT313_AWAITING_INDEPENDENT_STATIC_MATH_AUDIT
ALLOWED_NEXT_ACTION: freeze-contract313-SHA-and-read-only-audit-author-input-fidelity_domain-intersection_current-shape-derivative_Cartan-corner-cancellation_traction-Noether-identity_orientation_full-bridge_typing_affine-rank-kernel_allowed-set_existing-guards_decision-branches-claim-reach-and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-contracts297_303_305_307_311_313; exact-results309_312; task482_484_486_487_488_489; math-auditor-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-artifacts; perform-result-calculation; drop-geometry-source-cap-side-corner-owner-terms; set-beta-geo-src_or-QCT_or-Lie-metric-zero-without-proof; choose-alpha-beta-gamma_or-any-null-direction; add-new-physics; Python_network_DEV_RC_official; D2I-D6; PASS_STOP-score-depth-checkpoint-package; close-parent-track
IMMUTABLE_INPUT_PATHS_AND_SHA256: contract297=ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5; contract303=0FF8F7E9575ACCBECA83C5D18856323ABF5FAF962E1817484E025B2A5DABC345; contract305=3163534BCBA12123A220A25321FB684E6CAFFCBA01F5F128D6CB8B637631ADC8; contract307=EAA0BE263E3E414D15D070A33FD7AA43CD78DF739ABF8D15C6B2E65369EF8C91; result309=E9240D1DDBF29CC77A34F531ACB282BEF81BB5CCE8971F3D6E6EF96F71FD70E2; contract311=C96B403157EB18B087B4E2DDC2E994E3E9986E25D294F39828E7F22FDC5460C3; result312=DE24556A70952EDEDE8312EA39B5A594024334C229923B47528474A4687E4893; contract313=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task490-static-math-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_D2SW4_SET_VALUED_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 0/10
CUMULATIVE_TECHNICAL_ERRORS: 16
FINDING_ID: NONE_PENDING_CONTRACT_AUDIT
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_AUTHORIZED_BY_MARTIN_FOR_BOUNDED_SET_VALUED_SUCCESSOR_PENDING_TASK490
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: task490-confirms-or-identifies-the-earliest-exact-defect-before-any-bounded-analytic-result
NEXT_ROLE: math_script_auditor
```

```text
LIVE_SCIENTIFIC_ARTIFACTS: contracts295_295R1_297_313; total-live=4; contract311-and-result312-historical-accepted-predecessors; result308-quarantined
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
