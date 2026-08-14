# B6b-2.12 — C01-RW1-SW1 stress-work/current successor contract

**Task:** `A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-CONTRACT-20260730-421`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.12`  
**Autor fyzikálneho vstupu:** Martin Jambor  
**Formalizácia:** OpenAI Codex, hlavný orchestrátor  
**Stav:** `CONTRACT_DRAFT / AUTHOR_INPUT_RECORDED / NO_RUN / NO_PYTHON`  
**Rodičovská koľaj:** `C01-RW1 LIVE / D1-D2R1 BOUNDARY ACCEPTED`

## 1. Autorovo rozhodnutie

Martin Jambor 2026-07-30 výslovne schválil:

```text
RW1-SW1 je E3_PROVISIONAL same-track kandidát.
B_rec je lokálny väzbový graf s existujúcou kapacitou a geometriou.
Sigma_prep je fyzická geometria pripravovaného rozhrania.
Lokálny zákon sa má odvodiť ako integrabilná causal stress-work/current
projekcia existujúceho stress-energy, bez nového poľa a bez fitovanej
energetickej škály.
```

Toto rozhodnutie vyberá jednu testovaciu source-law triedu z trojice
prijatej v result294R1. Nevyberá hotový projektor, numerickú tension,
prácu jednej väzby, `W_*`, cell measure ani reset. Nie je to fyzikálny
witness, PASS/STOP ani povolenie výpočtu.

## 2. Zachovanie identity koľaje

Schválenie nemení carrier

```text
Z_rec = [B_rec, Sigma_prep]_rel.
```

Používa iba:

- existujúcu lokálnu bunkovú sieť a jej causal support;
- existujúcu kapacitu kontaktu `C=28` ako štrukturálnu kapacitu, nie energiu;
- lokálnu geometriu kontaktov a pripravovaného rozhrania;
- existujúci lokálny celkový stress-energy tensor `T_loc^(mu nu)`.

Zakázané je pridať nový fundamentálny tensor, pole, druh kontaktu,
species-dependent bond weight alebo druhú vlastnosť kontaktu čítanú rôzne
jednotlivými poľami. Projekcia je účtovný/kinematický rozklad existujúceho
`T_loc`, nie nový zdroj energie.

```text
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED_FOR_CONTRACT_DRAFT.
```

Ak by odvodenie vyžadovalo nový stavový druh, interaction topology,
causal graph, ontologický objekt alebo nezávislé pole, workflow sa zastaví
na `TRACK_IDENTITY_GATE / MARTIN_DECISION`.

## 3. Stavový alphabet a quotient

### 3.1 Väzbový záznam

Na causal supporte jednej parent bunky nech

```text
G_loc = (V_loc, E_loc)
```

je konečný lokálny incidentný graf. Každý existujúci kontakt nesie iba
už prijatú spoločnú kapacitu a fyzickú geometriu kontaktnej plochy. Záznam

```text
B_rec := [G_loc, capacity_loc, geometry_loc]_rel
```

zahŕňa incidenciu, lokálnu kontaktnú geometriu, orientácie a tie zmeny
geometrie, ktoré sú fyzicky rozlíšiteľné v existujúcej sieti. Hodnota
`C=28` ani počet kontaktov nie sú energetická škála.

### 3.2 Pripravované rozhranie

`Sigma_prep` je fyzický lokálny geometrický záznam čiastočne pripraveného
deliaceho rozhrania. Na regular vetve obsahuje aspoň:

```text
Sigma_prep := [S_prep, q_ab, n^mu, boundary(S_prep)]_rel,
```

kde `S_prep` je lokálny face complex alebo embedded čiastočné rozhranie,
`q_ab` jeho indukovaná geometria, `n^mu` lokálna orientácia a
`boundary(S_prep)` fyzický front nedokončeného rozhrania. Nezavádza sa
samostatný progress clock; progress musí byť určiteľný z tejto geometrie.

### 3.3 Ekvivalencia a reachable doména

`_rel` quotientuje iba:

- prelabelovanie buniek, väzieb a face elementov;
- dovolené lokálne súradnicové zmeny;
- reprezentácie zachovávajúce incidenciu, kapacitu a fyzickú geometriu.

Nesmie quotientovať fyzicky odlišnú geometriu, connectivity ani stav
pripravovaného rozhrania. Na prvom regular scope sa pripúšťajú causal,
piecewise-`C1` pre-event trajektórie, na ktorých je virtual-work forma
definovaná. Diskrétna jump vetva bez regular embedding patrí mimo tohto
`H_RDIV-MF1-v1` regular scope, nie mimo celej C01-RW1 koľaje.

Rovnaký úplný `Z_rec` musí určovať rovnaký work credit. Rozdielny kredit pri
rovnakom grafe a geometrii je hidden-history clock, pokiaľ rozdiel nezanechá
ďalší autorom schválený fyzický stavový záznam.

## 4. SW1 lokálny zákon, ktorý sa má odvodiť

### 4.1 Bezparametrická projekcia existujúceho stress-energy

Hľadaný objekt je lokálny, kovariantný a bezrozmerný projektor

```text
Pi_SW1[Z_rec],
T_SW1^(mu nu) := Pi_SW1[Z_rec] T_loc^(mu nu).
```

Musí byť zostrojený iba z `B_rec`, `Sigma_prep`, lokálnej metriky a fyzicky
odvodeného `u_cell`. Nesmie obsahovať nový fit coefficient, `H0`, `a`,
`Theta_cell`, Fourierovo `k`, `S8`, `delta`, `C=28` ako energy scale ani
post-event veličinu. Musí mať explicitný komplement, aby jeden stress-energy
príspevok nebol započítaný súčasne v SW1 aj mimo SW1 kanála.

Povinný state-sufficiency guard je

```text
sigma_SW1 = sigma_SW1[Z_rec].
```

Žiadna nezaznamenaná lokálna matter/field premenná nesmie pri pevnom
`B_rec,Sigma_prep` meniť virtual-work formu alebo `W_rec`. Ak stress stav
nie je constitutively určený schváleným `Z_rec`, carrier nie je úplný a
workflow sa vráti na author state-space gate; nesmie sa skryto rozšíriť.

Ak existujúca fyzika neurčí projektor alebo jeho normalizáciu, výsledok je
`LIVE / WAITING_FOR_EXACT_RECONFIGURATION_STRESS_PROJECTOR`, nie voľba
koeficientu podľa želaného výsledku.

### 4.2 Causal current a objemová stress-work 1-forma

Pre future-directed jednotkovú tangentu parent bunky sa definuje odvodený
lokálny energy current

```text
j_SW1^mu := -T_SW1^(mu nu) u_cell_nu.
```

Nech `V_rec(Z)` je lokálne konečný trojrozmerný reconfiguration support:
zjednotenie tých častí parent bunky a contact regions, ktorých fyzická
geometria sa mení pri príprave `Sigma_prep`. `V_rec` musí byť určené
existujúcou bunkovou geometriou; nesmie sa vložiť voľná interface thickness.
Nech `h_rec,AB` je odvodená priestorová materiálová geometria tohto supportu
a `sigma_SW1^(AB)` jeho spatial-stress projekcia z `T_SW1`. Virtual-work
1-forma na reachable state space má tvar

```text
omega_SW1[Z](delta Z)
  := (1/2) integral_(V_rec(Z)) sigma_SW1^(AB) delta h_rec,AB dV_rec,
```

s orientáciou znamienka zvolenou tak, že kladná hodnota znamená prácu do
prípravy rozhrania. Kladnosť sa nesmie vyrobiť operáciou `abs` ani
post-hoc `max(0,...)`; neadmissible smer zostáva fyzicky rozlíšený.
Pri `[sigma_SW1]=E/L^3`, bezrozmernom strain variation
`delta h_rec,AB` a `[dV_rec]=L^3` platí `[omega_SW1]=E`.

Pre-event výkon je

```text
P_rec := omega_SW1[Z](D_u Z),
[P_rec] = E/T,
P_rec >= 0
```

iba na admissible preparation path. Boundary-current a stress-work zápis
musia byť dve konzistentné formy toho istého lokálneho energy ledgeru, nie
dva sčítané zdroje.

### 4.3 Integrabilita a state functional

SW1 patrí do C01 iba ak na každej deklarovanej reachable vetve platí

```text
d omega_SW1 = 0,
integral_closed_loop omega_SW1 = 0,
```

vrátane všetkých netriviálnych cyklov state space. Potom existuje
single-valued accounting potential

```text
E_rec[Z] - E_rec[Z_birth]
  = integral_(Z_birth -> Z) omega_SW1,

W_rec[Z;Z_birth] = E_rec[Z] - E_rec[Z_birth],
D_u W_rec = P_rec >= 0,
[E_rec] = [W_rec] = E.
```

Energy scale musí pochádzať z existujúceho `T_loc` a fyzickej geometrie.
`E_rec` musí byť invariantné pod `_rel` quotientom a zdola ohraničené na
deklarovanej reachable doméne.
Ak closed loop nesie nenulovú prácu alebo disipácia/export zanechá kredit,
ktorý nie je viditeľný v schválenom `B_rec,Sigma_prep`, konkrétny SW1
functional zlyhá hidden-history/integrability guard.

Irreverzibilný kanál je dovolený iba ak jeho fyzický následok je úplne
zakódovaný v schválenom grafe alebo geometrii. Inak by sa musel pridať nový
stavový carrier a pred tým rozhoduje Martin.

## 5. D3 conservation a disjunktné kanály

Odvodenie musí uzavrieť jeden lokálny ledger

```text
E_res >= 0,
S_in >= 0,
L_ext >= 0,
P_rec = P_store + P_diss + P_RW1export >= 0,
D_u E_res = S_in - P_rec - L_ext.
```

`S_in` sa odvodí ako causal flux existujúceho energy currentu cez hranicu
parent causal supportu. `P_store`, `P_diss`, `P_RW1export` a `L_ext` musia
byť vzájomne disjunktné a zmapované do komplementárnych stress-energy
kanálov. `W_rec` je work credit, nie ďalší energy stock.

```text
S_in=0 a E_res/current nie je dostupný
  => P_rec=0
  => D_u W_rec=0.
```

Pri `S_in=0`, ale `E_res>0`, je dovolené iba konzervatívne dočerpanie tak,
aby integrovaný výdaj neprekročil počiatočný rezervoár.

## 6. D4 completion work

Najprv sa musí odvodiť geometrická množina `Z_complete` stavov, v ktorých
fyzické pripravované rozhranie spĺňa lokálne completion podmienky. Pre
konkrétny parent cycle potom

```text
W_* := E_rec[Z_complete] - E_rec[Z_birth] > 0,
chi_div := W_rec/W_*,
chi_c := 1.
```

`W_*` musí byť predvídateľne určené najneskôr na začiatku parent cyklu a
počas cyklu frozen. Nesmie sa fitovať podľa event rate, `H0`, `S8`,
produktov ani realizovaného crossing-u. Ak complete geometry alebo jej
energy difference nie je jednoznačná, D4 ostáva `WAITING`, nie STOP.

## 7. D5 cell measure a reset

Z tej istej lokálnej siete sa majú odvodiť:

- future-directed jednotková `u_cell` parent worldline;
- regular cell congruence;
- invariantná lokálne konečná occupation measure `dmu_cell`;
- parent retirement a nové daughter IDs;
- lokálna `R_reset^Z`, pre ktorú

```text
W[Z_rec,daughter] = 0.
```

Residual configuration/interface energy sa zachová v oddelenom post-event
conservation state. Nesmie sa skopírovať ako dcérsky work credit. Same-ID
reset je zakázaný.

## 8. Analytické poradie a DONE_WHEN

| ID | Blok | DONE_WHEN |
|---|---|---|
| `D1R` | invariantný state passport | `B_rec,Sigma_prep`, quotient a reachable regular doména sú úplné bez hidden clocku |
| `D2SW` | stress-work projektor | existuje parameter-free covariant `Pi_SW1`, disjunktný komplement a well-typed virtual-work forma |
| `D2I` | integrabilita | `d omega=0`, všetky periods sú nulové a `E_rec[Z]` je single-valued |
| `D3` | power/conservation | causal-current a stress-work formy sú totožné účtovanie; source-off a reservoir ledger sa uzatvoria bez double countu |
| `D4` | completion | `Z_complete` a kladné finite cycle-frozen `W_*` vzniknú z tej istej fyziky |
| `D5` | measure/reset | odvodia sa `u_cell`, congruence, `dmu_cell` a fyzický zero-credit daughter reset |
| `D6` | witness | jeden explicitný reachable pre-event stav prejde W0-W12 a regular first passage R0-R11 |

Poradie je

```text
D1R -> D2SW -> D2I -> D3 -> D4 -> D5 -> D6.
```

Bez prijatého `D2SW+D2I` sa D3-D6 neinterpretujú ako fyzikálny výsledok.

## 9. Behaviorálne mantinely a rozhodovacie vetvy

Povinný behaviorálny obal obsahuje:

| Podmienka | Povinný výsledok |
|---|---|
| žiadna zmena fyzického grafu/geometrie | `P_rec=0` |
| source-off bez rezervoára | `P_rec=0` a `W_rec` stojí |
| admissible preparation | `P_rec>=0` bez post-hoc clampu |
| closed state-space cycle | nulová SW1 work perioda |
| complete interface | kladné finite `W_*`, prvý simple transversal crossing |
| daughter birth | nový ID a `W_rec=0` bez straty residual energie |

Rozhodnutia:

```text
Ak D1R-D6 dajú explicitný parameter-free lokálny prvok A_RW1:
  CANDIDATE_PHYSICAL_RW1_SW1_WITNESS_FOUND_PENDING_INDEPENDENT_AUDIT.

Ak geometria neurčí jedinečný Pi_SW1 alebo energy normalization:
  LIVE / WAITING_FOR_EXACT_RECONFIGURATION_STRESS_PROJECTOR_OR_ENERGY_MAP.

Ak konkrétny Pi_SW1 poruší integrabilitu, conservation, source-off,
single-valuedness alebo potrebuje fitovanú škálu:
  PRECHECK_EXCLUDED_SCOPE iba pre tento SW1 kandidát.

Ak oprava potrebuje nový field, state species, topology, causal graph alebo
ontológiu:
  TRACK_IDENTITY_GATE / MARTIN_DECISION; žiadny automatický run.
```

Nenájdenie projektora ani zlyhanie jedného ansatzu neuzatvára C01-RW1.

## 10. Fázový a technický stav

```text
CURRENT_PHASE: CONTRACT_DRAFT_AUTHOR_INPUT_RECORDED_AWAITING_SHA_FREEZE_AND_STATIC_AUDIT
RUN_AUTHORIZED: false
PYTHON_AUTHORIZED: false
NETWORK_AUTHORIZED: false
OFFICIAL_OUTPUT_AUTHORIZED: false
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
P4_PHYSICAL_WITNESS_ATTEMPTS_CONSUMED_BY_THIS_CONTRACT: 0
```

Tento contract povoľuje po statickom audite iba analytické odvodenie.
Neobsahuje implementovateľný RC, official command ani output path.

## 11. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-12-H-RDIV-C01-RW1-SW1-CONTRACT-AUDIT-20260730-422
ROLE: math_script_auditor
ROLE_CONFIG_SHA256: EE536D71B70D7FCAF5C72D1CF30BCE2851496C1593191208C454BDF377B5DF79
ASSIGNED_AGENT_TASK_ID: /root/c01_rw1_contract293_audit
ARTIFACT_AUTHOR_TASK_ID: /root task421
STATIC_AUDITOR_TASK_ID: /root/c01_rw1_contract293_audit task422
INTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_NO_RESULT_OR_RAW
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED
SEPARATION_OF_DUTIES_CHECK: contract295-author-root_neq-independent-static-auditor-task422
ROUTE: A1_K1_A2_K4_P5.3_SM_v1_B6b-2.12_C01_RW1_SW1
CURRENT_PHASE: CONTRACT_DRAFT_AWAITING_EXTERNAL_SHA_FREEZE_AND_INDEPENDENT_STATIC_MATH_LOGIC_AUDIT
ALLOWED_NEXT_ACTION: main-orchestrator-freezes-exact-contract295-SHA-outside-this-file; independent-auditor-checks-author-input-fidelity_state-types_covariance_units_projector-noncircularity_integrability_conservation_source-off_D1R-D6-order_claim-reach_and-track-identity
ALLOWED_READS: mandatory-bootstrap; exact-contract295; contract293; accepted-result294R1; documents245_254_256_259_260_292; theory-main-A1-A7-and-A15; tasks419_420_421; role-config-and-manifest
ALLOWED_WRITES: none-by-auditor; advisory-response-only
FORBIDDEN_ACTIONS: edit-contract295_or-frozen-upstream; choose-or-invent-Pi_SW1_energy-scale_Wstar_measure_reset; add-new-field; Python_network_project-code_official; assign-project-PASS_STOP_score_depth_checkpoint_or-package
IMMUTABLE_INPUT_PATHS_AND_SHA256: contract293=BDE7C343F63590400704CA14F773E02F5BD227AAD058DBC4771A3EAF731937B2; accepted-result294R1=55C27502135A3260279329B42BC614C8ED7279741CD6FCB84DE0CFA8EB9D4677; theory-main=01B8DD903C3BB97B30E29E2C1E2E2B280D3968EDD0679C610E84A78CC55CBF43; contract295=RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
PREREG_SHA256: RECORDED_EXTERNALLY_AFTER_FINAL_BYTE_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only-audit-recommendation; no-project-output
ERROR_BATCH_INDEX: 1_NEW_PHYSICAL_ATOM
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 8
FINDING_ID: NONE_OPEN
FINDING_CLASS: NOT_APPLICABLE_PENDING_AUDIT
EARLIEST_INVALID_CHECKPOINT_ID: NONE
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED_CANDIDATE_PENDING_AUDIT
CHECKPOINT_ID: NONE_CONTRACT_IS_NOT_CHECKPOINT
PARENT_CHECKPOINT_IDS: CP-A2K4-P5-Q1R1-V3-20260729-001_SOURCE_BOUNDARY_ONLY
AUDIT_SUBMISSION_ID: NONE_INTERNAL_PHASE
DONE_WHEN: exact-frozen-contract-faithfully-encodes-author-SW1-input; projector-and-virtual-work-types-are-auditable; integrability-and-conservation-branches-are-noncircular; no-new-field-or-fitted-scale-enters; next-step-is-uniquely-bounded-analytic-D1R-D2SW-D2I-before-D3-D6
NEXT_ROLE: math_script_auditor
```

## 12. Nonclaims a súborový rozpočet

- nebol odvodený `Pi_SW1`, `E_rec`, `P_rec`, `W_*`, `u_cell`, measure ani reset;
- nevznikol physical witness ani prázdnosť celej `A_RW1`;
- C01-RW1, P5 a A2-K4 ostávajú `LIVE`, nie `CLOSED`;
- K4 `60/100` a P5 `3.5/6` sa nemenia;
- nevzniká raw, checkpoint, externý balík, Python ani official run.

```text
LIVE_SCIENTIFIC_ARTIFACTS: 1-new-contract295; accepted-result294R1-and-frozen-contract293-retained; quarantined-result294-retained
LIVE_CENTRAL_REGISTERS_UPDATED: current-plan_A2K4-plan_P5-plan_route-ledger
LIVE_FILES_CHANGED_TOTAL: 5
AUDIT_PACKAGE_COPIES: 0
```
