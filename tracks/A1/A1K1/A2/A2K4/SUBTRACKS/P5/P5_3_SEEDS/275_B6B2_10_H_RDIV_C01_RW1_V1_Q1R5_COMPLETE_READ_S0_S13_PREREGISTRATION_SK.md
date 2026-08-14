# B6b-2.10 — Q1R5 complete-read S0–S13 physics-screen preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R5-COMPLETE-READ-S0-S13-PREREG-20260727-228`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_PREREGISTRATION / EXACT_Q1R5_ONLY / NO_PYTHON`

## 1. Jediný cieľ a nemenný kandidát

Cieľom je nad jediným Q1R5 zdrojom vykonať evidence-complete W10 passport a
S0–S13 screen bez tematického cherry-pickingu:

```text
title: Gravitional radiation from first-order phase transitions in the
       presence of a fluid
authors: John T. Giblin Jr.; James B. Mertens
arXiv: 1405.4005v2
journal: Physical Review D 90, 023532 (2014)
DOI: 10.1103/PhysRevD.90.023532
family/rank: F-A / Q1R5
sole PDF provider ref: turn49view1
PDF total lines: 1203, exact target range L0..L1202
```

Q1R3 zostáva `24/24_TERMINAL`, fyzicky neprijatý a nevylúčený. Q1R4 je jeho
duplicate. Tento screen nesmie meniť ich stav, otvoriť companion ani doplniť
Q1R5 fyziku z refs [43–47].

## 2. Immutable vstupy a stav

```text
frozen ordered-transition document273 SHA256:
  C4B5BAE25EDD7E0D08CF692267BC7B6FC01A42034BC157942819AD95B5366DD3
access receipt273A SHA256:
  F3573A76750691B13CF97730856CF4C2B2987BC890AD002E1691D9BB0247B395
accepted eligibility result274 SHA256:
  199D481BDA260D5E3CFB4E805CC59299617382C9ED8C32BE536E1D5BAC52A451
current plan SHA256 after task226:
  CC8B8E73D823C614AAC2053CA35C171C8D55341A4B5040300A81AE4C364EE026
K4 plan SHA256 after task226:
  9228A028EBB57C41A7EC225832FF040C7D901AD61579A28F283B0075E212921B
P5 plan SHA256 after task226:
  8C6F629024BBB70437A8C41910263202F0C5B0DCD6A437DDCD061464E82232F7
event ledger through task226 SHA256:
  1A89D8ECE015D27CEEDD380A954445A2C15F426C96178010119B7D980599BDD1
progress review task227:
  BOUNDARY_OR_BLOCKER_PROGRESS / Q1R5 source-specific screen legal
```

Receipt273A zachytáva PDF interval `L0..L364` a same-identity landing metadata.
Formulácia result274 „11-stranový PDF text“ autoritatívne znamená excerpt z
11-stranového PDF, nie už úplný `L0..L1202` read.

Stav zostáva K4 `60/100`, P5 `3.5/6`, P4 work atoms `2`, physical witness
attempts `0`, `RUN_AUTHORIZED=false`.

## 3. Deterministický complete-read coverage plán

### 3.1 Stage A — presne sedem okien

Po nezávislom auditnom PASS, out-of-file SHA freeze a absent-target
preflighte sa vykoná presne jeden batched `web__run/open` call s
`response_length=long`:

```json
{"open":[
  {"ref_id":"turn49view1","lineno":425},
  {"ref_id":"turn49view1","lineno":545},
  {"ref_id":"turn49view1","lineno":665},
  {"ref_id":"turn49view1","lineno":785},
  {"ref_id":"turn49view1","lineno":905},
  {"ref_id":"turn49view1","lineno":1025},
  {"ref_id":"turn49view1","lineno":1145}
]}
```

Stage A spotrebuje presne 7 candidate-local screen operations. Očakávané
intervaly sú zvolené iba geometricky s krokom 120; nie podľa priaznivého
obsahu. Exact raw return sa publikuje raz do absent cieľa:

`275A_B6B2_10_Q1R5_COMPLETE_READ_STAGE_A_RAW.txt`.

### 3.2 Mechanická coverage kontrola

Bez Pythonu sa z receipt273A a každého provider bloku 275A vyberú source-line
tokeny `L<number>@P<number>`. Pre každý blok sa určí `[min L,max L]`; ich union
s base intervalom `[0,364]` sa zoradí a zlúči. Coverage PASS platí iba vtedy,
ak union bez jedinej medzery obsahuje každý integer line index `0..1202`.

Obsah riadkov nesmie ovplyvniť výber ďalšieho okna.

### 3.3 Stage B — najviac jeden deterministický gap-fill batch

Ak Stage A nechá `1..8` maximálnych uncovered intervalov `[a_i,b_i]`, vykoná
sa presne jeden batched open call. Pre každý interval sa použije anchor
`floor((a_i+b_i)/2)` v rastúcom poradí. Exact payload a intervaly sa pred
callom zapíšu do event ledgera; raw return sa publikuje raz do absent cieľa:

`275B_B6B2_10_Q1R5_COMPLETE_READ_STAGE_B_GAP_FILL_RAW.txt`.

Stage B má najviac 8 operations. Ak gapov je viac ako 8, payload nemožno
zostaviť, call zlyhá, receipt koliduje alebo union po Stage B stále nepokrýva
celé `0..1202`, výsledok je iba
`REVIEW_Q1R5_SCREEN_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE`. Žiadny tretí
call, retry, fallback, find, search, click ani companion nie je povolený.

Candidate-local screen cap je `7+max8=15`. Nijako nemení Q1R3 `24/24`.

### 3.4 One-call/one-file pravidlo

275A aj prípadný 275B majú jeden header s exact payloadom, operation count,
coverage stage, `BEGIN_EXACT_BATCH_RETURN`, neupravený string alebo
`JSON.stringify(result,null,2)` a `END_EXACT_BATCH_RETURN`. Append, overwrite,
silent repair a opakovanie spotrebovanej operation sú zakázané. Delimiter
collision alebo publish/transport chyba končia technickým REVIEW bez fyziky.

## 4. Nemenný W10 passport kontrakt

Výsledok musí explicitne zmapovať:

```text
(Z_rec, P_rec, W_*, u_cell, dmu_cell, R_reset^Z,
 disjoint local conservation ledger)
```

| Pole | Povinný fyzický obsah |
|---|---|
| `Z_rec` | source-native lokálna konfigurácia a rekonštruovateľné `W_rec=W[Z_rec]`, nie hidden history clock |
| `P_rec` | odvodený causal current/stress-work/reservoir power s exact znamienkom a podmienkami `>=0` |
| `W_*` | kladná konečná pre-event cycle-frozen delivered-work threshold z tej istej fyziky |
| conservation | disjunktné stored/dissipated/RW1-export/external-loss kanály, local identity a residual-interface tok |
| `u_cell` | source-native future-directed unit timelike parent-cell pole |
| congruence/`dmu_cell` | regular once-only parent worldtube/congruence a finite invariant proper measure |
| crossing | dynamicky dosiahnuteľná on-shell absolútne spojitá jednoduchá upward cesta |
| `R_reset^Z` | fyzická daughter/event mapa, zero daughter work credit a oddelená residual energy |
| source-off | bez vstupu a dostupného reservoiru nevzniká rast ani event |
| noncircularity | bez GW/S8/H0/division/biology/downstream targetu vo vstupe |

Každý riadok má `SOURCE_EQUATION_OR_SECTION`, `PROVENANCE_CLASS` a
`EVIDENCE_STATUS`. Provenance je iba `SOURCE_EXACT`, `DERIVED_SAME_MODEL`,
`E3_MAPPING` alebo `MISSING`. `E3_MAPPING` nesmie tvoriť nový objekt.

`MISSING` je dovolené iba po mechanickom full coverage PASS `L0..L1202` a
zdokumentovanom source-wide vyhodnotení. Pri neúplnej coverage je každé
neuzavreté pole `UNASSIGNED_DUE_TO_INCOMPLETE_EVIDENCE /
NOT_ASSESSABLE_EVIDENCE_INCOMPLETE`, nikdy inferované `MISSING`.

Rodičovský kontrakt zostáva:

```text
W_rec(tau_birth)=0,
D_u W_rec=P_rec>=0,
W_*>0 a D_u W_*=0 počas parent cyklu,
chi_div=W_rec/W_*, chi_c=1,
prvý jednoduchý transverzálny upward crossing.
```

Potential, latent heat, bubble-wall energy a GW spectrum nie sú automaticky
reálne dodaná kumulatívna work energia ani `W_*`.

## 5. Povinný S0–S13 screen

| ID | PASS podmienka |
|---|---|
| `S0` | original primary Q1R5 identity a evidence-complete relevant source |
| `S1` | jedna action/EOM/state/`T^{mu nu}`/convention/dimension/boundary/regime closure bez splice |
| `S2` | fyzický lokálny `Z_rec` a `W[Z_rec]` bez hidden history clocku |
| `S3` | na tej istej on-shell pre-event ceste pointwise `D_uW=P_rec>=0`, odvodený zdroj aj reservoir |
| `S4` | finite positive cycle-frozen `W_*` z tej istej fyziky |
| `S5` | disjunktný local energy-momentum ledger, residual-interface tok a source-off identity |
| `S6` | source-native future unit `u_cell`, once-only parent worldtube/congruence a finite invariant `dmu_cell` |
| `S7` | dosiahnuteľná on-shell absolútne spojitá jednoduchá upward cesta; nie seeded interpolation, jump ani numerical initialization |
| `S8` | fyzická dynamická `R_reset^Z`, zero daughter credit a oddelená residual energy; nie rename/reinitialization |
| `S9` | covariance/gauge meaning, causal well-posed použitý režim, bez relevantnej ghost/gradient/wrong-sign/negative-reservoir instability; jednotky a orientation konzistentné |
| `S10` | bez GW spectrum, `R_div`, expansion outputu, S8/H0/k, biology targetu alebo fitu vo vstupe |
| `S11` | všetky passport objekty mapovateľné do jedného provisional `Y_div` bez novej fyziky |
| `S12` | bez fyzického vstupu/rezervoára nevzniká rast ani event |
| `S13` | bez Pythonu, fitu, steam/completion, score/depth change alebo downstream runu |

Každý gate dostane `PASS`, `FAIL`, `MISSING` alebo
`NOT_ASSESSABLE_EVIDENCE_INCOMPLETE` s exact source evidence.

## 6. Frozen adverse-indicator pravidlá

Screen musí osobitne vyhodnotiť:

1. exchange current (14) ako fenomenologický derivative coupling, nie
   automaticky odvodený reservoir;
2. source statement, že spatial coupling môže dominovať s wrong sign, módy
   môžu rásť exponenciálne a simulácie sa v danom regime rozpadajú;
3. source restriction na stabilnú časť parameter space. S9 nesmie byť
   vyhlásené FAIL iba z nestability mimo použitého passport režimu, ale PASS
   vyžaduje source-supported stabilný admissible pre-event režim;
4. nucleation/simulation initialization: seeded bubble alebo numerical setup
   nie sú regular first passage ani fyzický reset;
5. total conservation cez add/subtract exchange nie je automaticky
   disjunktný stored/dissipated/export/loss ledger;
6. fluid `U^mu` nie je automaticky parent-cell congruence/once-only measure;
7. gravitational-wave output je downstream observable a nesmie definovať
   `W_rec`, `W_*`, ranking alebo crossing.

## 7. Decision vetvy

```text
Ak coverage PASS a S0-S13 prejdú bez MISSING:
  CANDIDATE_COMPLETE_W10_INTERFACE_ACTION_PASSPORT_FOUND
  / PENDING_INDEPENDENT_PHYSICS_AUDIT.

Ak coverage PASS a model je koherentná interface referencia, ale má MISSING:
  PASS_Q1R5_REFERENCE_INTERFACE_MODEL_ONLY
  / REVIEW_Q1R5_NOT_A_COMPLETE_W10_WITNESS.

Ak coverage PASS odhalí formula/physical/scope konflikt:
  PRECHECK_Q1R5_EXCLUDED_SCOPE
  / CAUSE_Q1R5_CANDIDATE_ONLY_FORMULA_PHYSICAL_OR_SCOPE_CONFLICT
  / REVIEW_Q1R5_NOT_A_COMPLETE_W10_WITNESS.

Ak coverage nie je úplná alebo transport/persistence zlyhá:
  REVIEW_Q1R5_SCREEN_EVIDENCE_INCOMPLETE_NO_PHYSICAL_INFERENCE
  alebo exact technical-failure variant.
```

Po contiguous coverage PASS a nezávislom audite/main acceptance zvýši každý
úplne vykonaný výsledok complete-W10, reference-only alebo candidate-local
exclusion `P4 work atoms 2->3`. Physical witness attempts sa zvýšia `0->1`
iba pri prijatom complete-W10. Evidence-incomplete a technical-failure vetvy
zachovajú oba počty. Nijaká vetva sama nie je C01/global no-go, `A_RW1`
emptiness, P5.3 closure, A3, K4/P5 score change alebo run permission.

## 8. Výstup a rozpočet

Result sa publikuje presne raz do absent cieľa:

`276_B6B2_10_H_RDIV_C01_RW1_V1_Q1R5_S0_S13_PHYSICS_SCREEN_RESULT_SK.md`.

Atóm má najviac 4 live vedecké artefakty: document275, receipt275A,
voliteľný receipt275B a result276. Central closure je najviac current/K4/P5
+ ledger po auditovanom main acceptance. Audit package copies `0` do
interného auditu a progress review. Python procesy `0`.

## 9. Auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R5-COMPLETE-READ-S0-S13-PREREG-AUDIT-20260727-229
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task228
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::task229
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit::RESERVED_DISTINCT_RESULT_AUDIT
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_AUTHOR_PREREG_RESULT_AUDITOR_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R5_COMPLETE_READ_SCREEN
CURRENT_PHASE: DRAFT_BEFORE_ANY_Q1R5_SCREEN_SOURCE_OPERATION
ALLOWED_NEXT_ACTION: independent read-only prereg audit; after PASS, SHA freeze and absent-target preflight
ALLOWED_READS: mandatory bootstrap; documents261,267,272-275; receipts271A/273A; result274; ledger tasks219-228; current/K4/P5 plans; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; web/source operation; Python; Q1R3 operation/reset; companion/splice; passport verdict; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document273=C4B5BAE25EDD7E0D08CF692267BC7B6FC01A42034BC157942819AD95B5366DD3; receipt273A=F3573A76750691B13CF97730856CF4C2B2987BC890AD002E1691D9BB0247B395; result274=199D481BDA260D5E3CFB4E805CC59299617382C9ED8C32BE536E1D5BAC52A451; current=CC8B8E73D823C614AAC2053CA35C171C8D55341A4B5040300A81AE4C364EE026; K4=9228A028EBB57C41A7EC225832FF040C7D901AD61579A28F283B0075E212921B; P5=8C6F629024BBB70437A8C41910263202F0C5B0DCD6A437DDCD061464E82232F7; ledger_through_task226=1A89D8ECE015D27CEEDD380A954445A2C15F426C96178010119B7D980599BDD1
PREREG_SHA256: PENDING_AFTER_AUDIT
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit; after freeze exact 275A, optional275B and result276
DONE_WHEN: sole-source identity, deterministic complete coverage, gap-fill rule, 15-operation cap, raw persistence, passport/S0-S13, adverse-indicator handling, decision branches, accounting/nonclaims and four-artifact budget are fail-closed
NEXT_ROLE: main_orchestrator
```
