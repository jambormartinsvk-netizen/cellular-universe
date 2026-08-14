# B6b-2.12 — D2SW-0 boundary work/power typed successor contract

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW0-TYPED-SUCCESSOR-20260731-445`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Stav:** `CORRECTED_SUCCESSOR_CONTRACT_FROZEN / AWAITING_INDEPENDENT_STATIC_AUDIT / NO_RUN`  
**Finding:** `S1-D2SW0-BOUNDARY-WORK-POWER-TYPING-001`  
**Autor formalizácie:** OpenAI Codex, hlavný orchestrátor

Tento immutable delta contract vykonáva exact same-track opravu potvrdenú
task444. Contract301 ostáva v karanténe. Jeho nedotknuté časti sa používajú
iba podľa explicitného precedence nižšie.

## 1. Precedence a frozen inputs

```text
PARENT_CONTRACT_301_SHA256: 871F67DE6696F80A2A9C5B5BCEF9EFECA5B50B2C31E09C4BE222309EA4942F90
DECISION_RECORD_302_SHA256: 03B31C4157911E96460852E4C0F0BD890DABBE0D447F05F63DEC99B4F5908BB2
CONTRACT_295_SHA256: BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B
DELTA_295R1_SHA256: 6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD
DELTA_297_SHA256: ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5
ACCEPTED_RESULT_300_SHA256: 0A0F07E13C249DCD51E054185369CFD325971DA5A4253080CA2967AF05AE496A
```

Z contractu301 sa bez zmeny zachovávajú §§1–5, §7 a K0–K4, K7, K9 v §8.
Tento delta contract úplne nahrádza contract301 §6, K5/K6/K8 a §9.
Decision302 je historický finding record; jeho draft 4-term balance je
superseded exact task444 correction nižšie.

## 2. Energy-valued boundary work 1-forma

Pre každý budúci exact candidate `Pi` musí existovať quotient-covariant
state-space 1-forma

```text
beta_boundary^Pi[Z](delta Z) : E.
```

Musí byť odvodená z toho istého pre-event `T_Pi=Pi[T_loc]`, parent causal
worldtube a fyzickej orientation. Je nulová na čistých gauge/relabel
smeroch. Nie je to automaticky traction work z contract301 §5.

Fixujeme znamienko:

```text
beta_boundary^Pi(delta Z)>0
```

znamená net causal energy contribution do parent RW1 účtu v smere
`delta Z`. Ide o orientation convention, nie clamp ani požiadavku kladnosti
pre každý tangent. Záporná hodnota zostáva fyzicky rozlíšená.

## 3. Boundary power a frozen conservation ledger

Vyhodnotenie na actual pre-event tangent dá výkon

```text
P_boundary^Pi[Z]
  := beta_boundary^Pi[Z](D_u Z) : E/T.
```

V tomto scope je to presne causal incoming power contractu295:

```text
P_boundary^Pi := S_in^Pi.
```

Frozen conservation identity sa nemení:

```text
P_rec^Pi := omega_bulk^Pi[Z](D_u Z),

P_rec^Pi
 = P_store^Pi
 + P_diss^Pi
 + P_RW1export^Pi,

D_u E_res^Pi
 = P_boundary^Pi
 - P_rec^Pi
 - L_ext^Pi.
```

Ekvivalentný incoming-power zápis je

```text
P_boundary^Pi
 = D_u E_res^Pi
 + omega_bulk^Pi[Z](D_u Z)
 + L_ext^Pi,
```

alebo po rozvinutí `P_rec`:

```text
P_boundary^Pi
 = D_u E_res^Pi
 + P_store^Pi
 + P_diss^Pi
 + P_RW1export^Pi
 + L_ext^Pi.
```

Tieto dve posledné formy sú alternatívne reprezentácie tej istej identity.
Nesmú sa zlúčiť tak, že sa súčasne sčíta `omega_bulk=P_rec` aj jeho
`P_store/P_diss/P_RW1export` zložky. `L_ext` ostáva iba strata mimo RW1
work channelu. `W_rec` nie je ďalší energy stock.

Všetky členy power rovníc majú jednotku `E/T`. Žiadna energy-valued
1-forma sa do nich nevkladá bez vyhodnotenia na `D_u Z`.

## 4. Kernel guard na 1-forme

Pre preserved

```text
K_iso(Z):={delta Z:delta h_rec[Z]=0}
```

platí candidate guard

```text
G_K(Pi):
  for every delta Z in K_iso(Z),
  beta_boundary^Pi[Z](delta Z)=0
  or beta_boundary^Pi[Z](delta Z)
     is an exact internal pure-transport 1-form contribution
     with zero net assigned RW1 work.
```

Toto nie je dôkaz, že konkrétny `Pi` guard spĺňa. Vyhodnotenie iba pozdĺž
jednej actual trajektórie nestačí na tvrdenie nulovosti celej 1-formy na
`K_iso`.

## 5. Traction work ostáva oddelený

Contract301 §5 zachoval

```text
beta_traction^Pi[Z](delta Z)
 := integral_(boundary M_pc) t_Pi^B xi_B dA : E
```

na tých regular tangents, ktoré majú jednoznačný material generator
`delta Z -> xi`. Táto virtual-work 1-forma sa nesmie stotožniť s
`beta_boundary^Pi` bez odvodenej mapy obsahujúcej:

1. tangent-to-material-motion map;
2. physical causal-worldtube orientation;
3. transport/conservation identity z toho istého `T_Pi`;
4. rovnaké shared-contact accounting weights ako current a complement.

Ak existujúce `Z_rec,T_loc` takú mapu neurčujú, exact výsledok je

```text
LIVE / WAITING_FOR_TRACTION_TO_CAUSAL_CURRENT_WORLDTUBE_MAP.
```

Nesmie sa vložiť nový bridge, surface law alebo dynamics iba na uzavretie
rovnice.

## 6. Corrected K5, K6 a K8

| ID | Kontrola | PASS podmienka | Fail-closed výsledok |
|---|---|---|---|
| `K5` | isometric kernel | `omega_bulk(delta Z)=0` a `G_K(Pi)` platí na celej `K_iso`; pure transport má nulovú net assigned RW1 work | exact candidate fail=`PRECHECK_EXCLUDED_SCOPE_FOR_EXACT_PI`; chýbajúci bridge=`REVIEW_KERNEL_CLOSURE_OPEN` |
| `K6` | boundary-current provenance | `beta_boundary:E` pochádza z toho istého `T_Pi`, pre-event worldtube a physical orientation; `P_boundary=beta_boundary(D_uZ):E/T`; traction ostáva oddelený do odvodenia bridge | `REVIEW_BOUNDARY_CURRENT_OR_WORLDTUBE_MAP_OPEN` |
| `K8` | source-off/conservation | `P_boundary=S_in`; frozen reservoir identity a presne jedna z compact/expanded `P_rec` reprezentácií platí bez double countu; bez inflowu a dostupného rezervoára work/export/dissipation zaniknú | `REVIEW_CONSERVATION_LEDGER_OPEN` alebo exact candidate-specific exclusion |

Shared-contact K7 z contractu301 sa nemení. Rovnaké odvodené weights musia
byť použité v `beta_boundary`, `omega_bulk`, `L_ext` aj complement ledgeri.

## 7. Corrected decision branches

```text
Ak current accepted inputs vyberú exact Pi, beta_boundary, worldtube map a
shared-contact accounting a všetky K0-K9 prejdú:
  PASS_D2SW0_KERNEL_AND_SHARED_CONTACT_GUARD_FOR_EXACT_PI_PENDING_AUDIT;
  ešte nie D2SW projector acceptance, integrability ani witness.

Ak je Pi/accounting nejednoznačné alebo traction-to-current bridge nie je
odvodený:
  LIVE / WAITING_FOR_EXACT_RECONFIGURATION_PROJECTOR_ACCOUNTING_OR_WORLDTUBE_MAP.

Ak exact candidate Pi poruší corrected K5, K7 alebo K8 bez novej fyziky:
  PRECHECK_EXCLUDED_SCOPE_FOR_THAT_EXACT_PI_ONLY.

Ak oprava vyžaduje nový surface/bending/curvature state, thickness, field,
memory, dynamics alebo interaction topology:
  TRACK_IDENTITY_GATE / MARTIN_DECISION.

Žiadna waiting alebo candidate-specific exclusion vetva nie je STOP celej
C01-RW1, P5 ani A2-K4 koľaje.
```

## 8. Fyzikálny a identitný dosah

Task444 potvrdil:

```text
FINDING_CLASS: S1_LOCAL_CORRECTABLE_SAME_TRACK
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED_FOR_BOUNDARY_WORK_POWER_TYPING_ONLY
EARLIEST_INVALID_CHECKPOINT_ID: NONE
```

Oprava nemení `Z_rec`, state space, `T_loc`, stress sektory, causal graph,
interaction topology ani ontológiu. Nepridáva parameter alebo physical law;
iba zachováva frozen contract295 accounting a odlišuje work 1-formu od
power. Nový surface/bridge dynamics obsah by vyžadoval Martina.

## 9. Fázový stav a nonclaims

```text
CURRENT_PHASE: D2SW0_TYPED_SUCCESSOR_CONTRACT303_AWAITING_INDEPENDENT_STATIC_AUDIT
ACTIVE_BLOCKER: PHYSICAL_RW1_SW1_D2SW0_TYPED_SUCCESSOR_CONTRACT303_STATIC_AUDIT_PENDING
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
```

- corrected typing nevyberá `Pi_SW1`, `beta_boundary` ani accounting map;
- kernel, conservation, integrability a physical witness ešte neprešli;
- nevznikol result, raw, checkpoint, package ani external audit;
- A2-K4 `60/100` a P5 `3.5/6` sa nemenia.

## 10. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-D2SW0-TYPED-SUCCESSOR-AUDIT-20260731-446
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_contract293_audit
ARTIFACT_AUTHOR_TASK_ID: /root task445
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_contract293_audit task446
INTERNAL_AUDITOR_TASK_ID: /root/c01_rw1_d1_d2_physics_audit task444_COMPLETE_SAME_TRACK_CONFIRMED
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: contract303-author-root-task445_neq-static-auditor-task446; task444-independent-physics-audit-complete
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_D2SW0_TYPED_SUCCESSOR
CURRENT_PHASE: D2SW0_TYPED_SUCCESSOR_CONTRACT303_AWAITING_INDEPENDENT_STATIC_AUDIT
ALLOWED_NEXT_ACTION: freeze-contract303-SHA; read-only-audit-exact-precedence_beta-boundary-energy_P-boundary-power_fixed-inflow-sign_frozen-contract295-conservation-no-double-count_GK-on-one-form_traction-separation_corrected-K5-K6-K8_decision-branches-and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-contracts295_295R1_297; accepted-result300; quarantined-contract301; decision302; exact-contract303; task442-and-task444-responses; task443_445-ledger; math-auditor-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-artifacts; choose-Pi_beta-boundary_accounting-or-worldtube-map; assume-kernel_conservation_integrability; add-new-physics; Python_network_project-code_DEV_RC_official; D2I-D6; project-PASS_STOP_score_depth_checkpoint-package
IMMUTABLE_INPUT_PATHS_AND_SHA256: parent295=BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B; delta295R1=6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD; delta297=ABD1C9C427CF58CD72BAD6AAFDC031C5850578D1A1C7E535DDE23E3FC090ABB5; accepted-result300=0A0F07E13C249DCD51E054185369CFD325971DA5A4253080CA2967AF05AE496A; quarantined-contract301=871F67DE6696F80A2A9C5B5BCEF9EFECA5B50B2C31E09C4BE222309EA4942F90; decision302=03B31C4157911E96460852E4C0F0BD890DABBE0D447F05F63DEC99B4F5908BB2; contract303=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task446-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
FINDING_ID: S1-D2SW0-BOUNDARY-WORK-POWER-TYPING-001
FINDING_CLASS: S1_LOCAL_CORRECTABLE_SAME_TRACK
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED_FOR_BOUNDARY_WORK_POWER_TYPING_ONLY_PENDING_TASK446
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: task446-verifies-composite-preserved-contract301-plus-delta303-is-well-typed_conservation-consistent_noncircular_and-without-projector-or-new-physics-overclaim
NEXT_ROLE: math_script_auditor
```

```text
LIVE_SCIENTIFIC_ARTIFACTS: contracts295_295R1_297_result300_contract303; total-live=5; contract301-quarantined-history; decision302-closed-history
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
