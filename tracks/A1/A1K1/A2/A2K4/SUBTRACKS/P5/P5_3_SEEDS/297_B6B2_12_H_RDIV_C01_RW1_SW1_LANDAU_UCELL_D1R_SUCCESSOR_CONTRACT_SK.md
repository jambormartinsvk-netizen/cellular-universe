# B6b-2.12 — C01-RW1-SW1 Landau `u_cell` D1R successor contract

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-LANDAU-UCELL-CONTRACT-20260731-431`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Autor fyzikálneho vstupu:** Martin Jambor  
**Formalizácia:** OpenAI Codex, hlavný orchestrátor  
**Stav:** `AUTHOR_INPUT_FROZEN / AWAITING_INDEPENDENT_STATIC_AUDIT / NO_RUN / NO_PYTHON`  
**Rodičovský výsledok:** result296, audit task426 a milestone review task429 prijaté

## 1. Autorovo exact rozhodnutie

Martin Jambor 2026-07-31 výslovne schválil:

```text
Schvaľujem u_cell ako jedinečný budúcnosťou orientovaný jednotkový
Landauov časupodobný vlastný vektor existujúceho T_loc[Z_rec]. Platí iba
na regular doméne, kde je T_loc typu I, časupodobný vlastný priestor je
jednorozmerný, vlastná hodnota je nedegenerovaná a mapa T_loc[Z_rec] je
jednoznačná a hladká. Tento smer predstavuje pohyb identity parent bunky.
Mimo tejto domény zostáva vetva LIVE / WAITING; bez clampingu, náhradného
frame, nového poľa alebo fitovanej škály.
```

Toto rozhodnutie uzatvára iba otvorený fyzikálny pôvod parent-cell frame v
D1R. Nie je to výber `Pi_SW1`, dôkaz integrability, conservation, `W_*`,
measure/reset, fyzikálny witness ani povolenie výpočtu.

## 2. Efektívny contract a precedence

Efektívny contract po audite tejto delty bude exact trojica:

```text
parent295 SHA256:
BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B

ordering-delta295R1 SHA256:
6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD

Landau-u_cell-delta297 SHA256:
RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
```

Contract295 a delta295R1 zostávajú immutable. Táto delta má prednosť iba
pri exact definícii a doméne `u_cell`; všetky ostatné guardy, poradie a
rozhodovacie vetvy zostávajú účinné.

## 3. Exact Landau frame

Používa sa signatúra metriky `(-,+,+,+)` a existujúci symetrický lokálny
stress-energy tensor `T_loc^(mu nu)[Z_rec]`. Zmiešaný tensor je

```text
T_loc^mu_nu[Z_rec] := T_loc^(mu alpha)[Z_rec] g_(alpha nu).
```

Na povolenej regular doméne `D_L` je `u_cell` určené rovnicami

```text
T_loc^mu_nu[Z_rec] u_cell^nu = -rho_L[Z_rec] u_cell^mu,
g_(mu nu) u_cell^mu u_cell^nu = -1,
u_cell je future-directed.
```

Doména `D_L` obsahuje presne tie reachable pre-event stavy a ich regular
vetvy, na ktorých sú súčasne splnené:

1. `T_loc=T_loc[Z_rec]` je jednoznačná hladká mapa schváleného quotient
   stavu; rovnaký `Z_rec` nesmie dať iný tensor ani iný frame;
2. `T_loc` je Hawkingovho–Ellisovho typu I;
3. časupodobný vlastný priestor zmiešaného tensora je jednorozmerný;
4. jeho vlastná hodnota `lambda_t=-rho_L` je jednoduchá a odlišná od
   každej priestorovej vlastnej hodnoty `lambda_A`, teda

   ```text
   product_A (lambda_t-lambda_A) != 0;
   ```

5. zvolený normalizovaný future-directed eigensmer je hladký na každej
   deklarovanej connected reachable vetve.

Podmienka v bode 4 je exact nenulovosť, nie numerická tolerancia ani
fitovaný spectral-gap prah. Future orientation odstraňuje zostávajúcu
znamienkovú dvojznačnosť. Pri týchto podmienkach je `u_cell[Z_rec]`
jednoznačné, kovariantné a bez novej energetickej škály.

## 4. Fyzický význam a same-track identita

Autor určuje, že Landauov eigensmer existujúceho `T_loc[Z_rec]` je fyzický
smer pohybu identity danej parent bunky. `u_cell` preto nie je nový field,
nezávislý cell-number current ani importovaný makroskopický `u_d`; je to
odvodený frame existujúceho lokálneho stress-energy tej istej bunky.

```text
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED_FOR_LANDAU_UCELL_INPUT.
```

Tým sa nemení `Z_rec=[B_rec,Sigma_prep]_rel`, interaction topology, causal
graph, kapacita kontaktu, bunková ontológia ani zákaz species-dependent
bond property. Ak by ďalší krok potreboval iný tensor, nový current alebo
novú identity-flow premennú, vráti sa na `TRACK_IDENTITY_GATE / MARTIN_DECISION`.

## 5. D1R geometrické dôsledky a zostávajúca analytická povinnosť

Z auditovaného `u_cell` sa bez nového parametra definuje spacelike
projektor

```text
h_cell_(mu nu) := g_(mu nu) + u_cell_mu u_cell_nu,
h_cell_(mu nu) u_cell^nu = 0.
```

Materiálová geometria `h_rec,AB` musí byť pullback `h_cell` na fyzický
reconfiguration support `V_rec(Z)` určený existujúcou parent-cell/contact
geometriou podľa contractu295. `V_rec` nesmie dostať voľnú interface
thickness. Bounded analytický successor musí ešte overiť:

- quotient invarianciu a hladkosť `u_cell,h_rec,V_rec` na `D_L`;
- jednoznačnosť `V_rec` z existujúcej geometrie;
- úplnosť D1R state passportu bez hidden clocku;
- že `sigma_SW1=sigma_SW1[Z_rec]` ostáva state-sufficient.

Táto delta sama nevyhlasuje úplný D1R PASS a neotvára D2SW pred nezávislým
statickým auditom exact trojice contractov.

## 6. Fail-closed hranica domény

Ak stav alebo reachable vetva opustí `D_L`, presný výsledok je

```text
LIVE / WAITING_FOR_REGULAR_TYPE_I_UNIQUE_LANDAU_FRAME.
```

Zakázané je:

- pokračovať posledným dostupným `u_cell` cez degeneráciu;
- prepnúť na centroid, `u_d`, graph orientation alebo cell current;
- zaviesť `abs`, clamp, regularizačný smer či numerický gap cutoff;
- vybrať frame podľa `H0`, `S8`, `a`, `Theta_cell`, event rate, outputu
  alebo post-event stavu.

Táto fail-closed hranica vylučuje iba danú regular Landau vetvu. Nie je to
STOP C01-RW1, P5 ani A2-K4.

## 7. Downstream dependency

Po auditnom prijatí tejto delty je povolené iba bounded analytické poradie

```text
D1R-completion(u_cell,h_rec,V_rec,state-sufficiency)
  -> D2SW(Pi_SW1,T_SW1,j_SW1,omega_SW1)
  -> D2I(integrability,E_rec,W_rec).
```

`D3-D6` zostávajú zatvorené, kým ten istý parameter-free projektor
neprejde D2SW a všetky exact/closed-period integrability guardy D2I.
Landau frame neurčuje automaticky `Pi_SW1`; iba odstránil najskorší frame
blocker.

## 8. Rozhodovacie vetvy

```text
Ak exact composite contract prejde nezávislým auditom:
  otvoriť bounded read-only analytické D1R-completion -> D2SW -> D2I.

Ak definícia frame nie je kovariantná, unique alebo state-sufficient:
  vrátiť sa na exact D1R contract point bez downstream záveru.

Ak D1R prejde, ale neexistuje jednoznačný parameter-free Pi_SW1:
  LIVE / WAITING_FOR_EXACT_RECONFIGURATION_STRESS_PROJECTOR.

Ak konkrétny Pi_SW1 poruší integrabilitu alebo potrebuje fitovanú škálu:
  PRECHECK_EXCLUDED_SCOPE iba pre tento SW1 projektor.

Ak by oprava potrebovala nový field, current, state species, topology,
causal graph alebo ontológiu:
  TRACK_IDENTITY_GATE / MARTIN_DECISION.
```

## 9. Fázový stav

```text
CURRENT_PHASE: LANDAU_UCELL_AUTHOR_INPUT_FROZEN_AWAITING_INDEPENDENT_STATIC_AUDIT
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
```

Autorovo fyzikálne rozhodnutie ani jeho formalizácia nie sú failed
candidate/build/test a nemenia technický error counter.

## 10. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-LANDAU-UCELL-CONTRACT-AUDIT-20260731-432
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_contract293_audit
ARTIFACT_AUTHOR_TASK_ID: /root task431
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_contract293_audit task432
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_RESULT_OR_RAW
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: contract297-author-root-task431_neq-independent-static-auditor-task432
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1_LANDAU_D1R
CURRENT_PHASE: LANDAU_UCELL_AUTHOR_INPUT_CONTRACT_AWAITING_EXTERNAL_SHA_FREEZE_AND_INDEPENDENT_STATIC_AUDIT
ALLOWED_NEXT_ACTION: freeze-exact-contract297-SHA; audit-effective-contract-parent295-plus-delta295R1-plus-delta297_for-author-input-fidelity_Landau-signs-Type-I-domain_uniqueness_nondegeneracy_smoothness_covariance_state-sufficiency_fail-closed-boundary_dependency-order_claim-reach_and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-parent295; exact-delta295R1; exact-delta297; accepted-result296; tasks426_429_430_431; documents245_254_256_259_260_292; theory-main-A1-A7-A15; role-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-frozen-contracts-or-result296; choose-Pi_SW1_energy-map_Wstar_measure_reset; add-field_current_scale_threshold; open-D2SW-D6; Python_network_project-code_DEV_RC_official; assign-project-PASS_STOP_score_depth_checkpoint-package; close-C01-RW1-without-physical-reason
IMMUTABLE_INPUT_PATHS_AND_SHA256: parent295=BFD7A56DBB1B0BD8EC9EEAF644382A2E3E35BC66EF8633D677C566EEB941AE5B; ordering-delta295R1=6C9FFAE27FE212E52046A540E1D028793138131078EB03BAA9655DA16A7076CD; accepted-result296=AEA5343A94D28AF94534DF54E96A0C3A2BD3A51BC0644EC8717F1EBFE4FE12E2; Landau-delta297=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-task432-audit-recommendation
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
FINDING_ID: NONE_OPEN
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CANDIDATE_PENDING_AUDIT
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE
DONE_WHEN: auditor-verifies-exact-composite-contract-faithfully-freezes-author-Landau-input_without-new-field-scale-threshold-or-domain-clamping_and-returns-PASS-or-earliest-exact-correction
NEXT_ROLE: math_script_auditor
```

## 11. Nonclaims a súborový rozpočet

- `u_cell` je autorom definovaný fyzický frame iba na `D_L`; úplný D1R
  passport ešte čaká na audit a bounded analytickú kontrolu;
- nebol odvodený `Pi_SW1`, `E_rec`, `P_rec`, `W_*`, congruence, measure ani
  reset;
- nevznikol physical witness, raw, checkpoint, package ani fyzikálny
  PASS/STOP;
- skóre A2-K4 `60/100`, P5 `3.5/6` a upstream evidence sa nemenia;
- C01-RW1, P5 a A2-K4 zostávajú `LIVE`, nie `CLOSED`.

```text
LIVE_SCIENTIFIC_ARTIFACTS: 1-new-contract297; effective-contract295-plus-295R1-and-accepted-result296-retained
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
