# V5 addendum: segmentovaná `n8000` modelová bisection

**Task ID:** `V318-PT1-H0-S8-C2-N8000-BISECTION-V5-20260731`  
**Route:** `RELEASE/v3.18/PT1_H0/C2`  
**Stav:** `CONTRACT_FROZEN / DEV_TESTS_PASS / RUN_AUTHORIZED=false`  
**Rodič V4:** `5E2A35D1E1A6EB64D200D4F18488A31849CB16079249DFB8407559A6D3925D42`  
**Immutable referencia:**
`0BFC88D8FFC5196B137570B149CBBC7ED3B93DC3EF81D14D9E7F4F130E050234`

## Dôvod a fyzikálna identita

RC12 `null n8000` modelový stage prekročil interných `45 s` počas
`solve_anchor`; raw nevznikol. Rovnaký priamy modelový stage pre `half/full`
sa nespustil. V5 nemení rovnicu backgroundu, inner fixed point, root
bracket, midpoint pravidlo, toleranciu, počet maximálnych iterácií, rast,
vstupy ani výstupný modelový point. Delí iba 29 midpoint krokov tej istej
bisection na tri procesy:

```text
A = endpointy + midpoint iterácie 1..10
B = midpoint iterácie 11..20
C = midpoint iterácie 21..29 + finálny solution + growth + model-stage raw
```

`TRACK_IDENTITY_GATE = SAME_TRACK_CONFIRMED`.

## Exact continuation state

Každý segment nesie:

- `shard_id`, frozen `Delta N_eff`, `grid_n=8000`;
- exact SHA referencie a V3/V4/V5 lineage;
- `theta_reference`, `reference_growth_D`;
- `sound_horizon_Mpc`, jeho quadrature error a `distance_target_Mpc`;
- `low`, `high`, `low_residual`, `high_residual`;
- pôvodné endpoint rezíduá pred prvým midpointom;
- `completed_midpoint_iterations` presne `10` alebo `20`;
- frozen input ledger a všetky finite/sign/bracket guards.

Python JSON float zápis/načítanie je exact roundtrip IEEE-754 hodnoty; B/C
preto pokračujú z rovnakých `low/high/residual` bitových hodnôt, aké by
ostali v jednom procese. Každý successor pred výpočtom overí file SHA,
schema, verdict, shard/delta/grid, reference SHA, V3/V4/V5 hashe a presný
iteration counter.

## Outputy

Pre každý `null/half/full`:

- A: `RUN_V318_PT1_H0_S8_CELL_{SHARD}_N8000_BISECT_A.json`;
- B: `RUN_V318_PT1_H0_S8_CELL_{SHARD}_N8000_BISECT_B.json`;
- C publikuje existujúci V4 modelový cieľ
  `RUN_V318_PT1_H0_S8_CELL_{SHARD}_N8000_MODEL_STAGE.json`.

A/B úspešný verdict je `PASS_N8000_BISECTION_SEGMENT_INTRINSIC`. C úspešný
verdict a modelová schéma ostávajú V4:
`PASS_N8000_MODEL_STAGE_INTRINSIC /
v318_pt1_h0_s8_n8000_model_stage_v4`. C raw pridá predecessor SHA a
segmentation V5 lineage. V4 agregátor potom ostáva nezmenený okrem povinnej
kontroly V5/C lineage.

## Presná matematická parita

Každý midpoint používa bez zmeny:

```text
mid = 0.5*(low+high)
mid_residual, solution, distance = residual(mid)
if low_residual*mid_residual > 0:
    low, low_residual = mid, mid_residual
else:
    high, high_residual = mid, mid_residual
```

Po kroku 29 musí `high-low<=5e-10`. C používa solution/distance/rezíduum
z posledného midpointu presne ako `solve_anchor`, doplní rovnaké polia,
spustí rovnaký `growth` a rovnaký `_public_point`. Statický audit musí
porovnať source vetvu s `solve_anchor` riadok po riadku.

## Runtime, chyby a DEV

- A/B/C interný limit `45 s`, každý externý `60 s`;
- každý immutable target sa publikuje najviac raz;
- REVIEW guard sa zachová ako raw; unexpected timeout/crash nemá vedecký
  dosah a rovnaký SHA/segment sa neopakuje;
- `half/full` A sa nesmie spustiť, kým `null` A nepotvrdí, že segmentácia
  reálne odstránila deadline blocker;
- DEV iba syntax/help a offline syntetická parita bisection state machine
  na fake skalárnej funkcii, vrátane SHA/counter/mapping mismatch;
- žiadny DEV test nepoužije produkčné `Delta N_eff`, `n=8000`, referenčný
  raw ani official target.

Očakávaný runtime jedného segmentu je pod `25 s`; je to technické
očakávanie, nie PASS prah navyše. Fyzikálne a numerické prahy ostávajú V1.

## Predregistrovaný DEV beh po implementácii

Ľudský význam: syntetický test má dokázať, že jeden beh 29 midpointov a
tri nadväzujúce behy `10+10+9` skončia s úplne rovnakým bracket state a
posledným midpointom. Súčasne má skúsiť odmietnuť predecessor s chybným
počítadlom a overiť JSON roundtrip segmentového payloadu. Nepočíta žiadny
produkčný model ani vedecký bod.

```text
py_compile + --help: očakávanie exit 0
synthetic_self_test: presne 30/30 checks PASS, all_pass=true
interný limit self-testu: 5 s
vonkajší limit každého DEV príkazu: 30 s
```

- Ak všetko prejde: zmraziť nové source SHA ako RC V5, aktualizovať tento
  kapsul a odovzdať exact RC nezávislému `math_script_auditor`; official
  beh ešte stále nie je povolený.
- Ak zlyhá syntax, help, počet kontrol alebo ľubovoľná kontrola: žiadny RC
  ani official run; zapísať jeden route-local technický error riadok a
  opraviť ten istý pracovný súbor v rámci dávky 2.
- Zmena tohto očakávania po behu je prípustná iba s explicitným dôvodom a
  nesmie spätne premeniť FAIL na PASS.

### DEV výsledok

Beh po implementácii skončil presne podľa predregistrácie:

```text
py_compile: PASS
--help: PASS; A/B/C entry points sú prítomné, priamy V4 model entry point nie
synthetic_self_test: 30/30 PASS; all_pass=true
runtime_seconds: 0.014999999984866008
scientific_effect: NONE
```

Spotrebované chyby dávky sa úspešným DEV testom podľa metodiky nenulujú.
Stav ostáva batch 2, `2/10`, kumulatívne `12`.

## Handoff

```text
TASK_ID: V318-PT1-H0-S8-C2-N8000-BISECTION-V5-DEV-20260731
ROLE: main_orchestrator_as_DEV_source_author
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: /root/h0_s8_math_auditor
INTERNAL_AUDITOR_TASK_ID: /root/h0_s8_physics_auditor
SEPARATION_OF_DUTIES_CHECK: PASS
ROUTE: RELEASE/v3.18/PT1_H0/C2
CURRENT_PHASE: RC_FREEZE_PENDING_EXACT_HASHES
ALLOWED_NEXT_ACTION: bind source to final V5 contract hash, rerun bounded exact-RC DEV suite, freeze source hashes and request independent static math audit; no official run.
ALLOWED_READS: mandatory bootstrap; V3--V5; exact RC12; immutable reference raw/hash; timeout/checklist/base registers.
ALLOWED_WRITES: scripts/baseScripts/release_v318_h0_s8_legacy_sensitivity_dev.py; scripts/393_script_V318_PT1_H0_S8_three_point_legacy_sensitivity_dev.py
FORBIDDEN_ACTIONS: no production segment/model/aggregate, network, theory edit, score/depth or equation/threshold change.
IMMUTABLE_INPUT_PATHS_AND_SHA256: V4=5E2A35D1E1A6EB64D200D4F18488A31849CB16079249DFB8407559A6D3925D42; RC12 base=F5E22457263CC30388BC40F27067F4DFBD7B05D34E23C769A4DE0ED6E088E898; RC12 runner=6935F3A04AEBCE320098FF45C30EF43EDB5214596315B4CAF9CDB8A0DEEADDD0; reference=0BFC88D8FFC5196B137570B149CBBC7ED3B93DC3EF81D14D9E7F4F130E050234
PREREG_SHA256: recorded externally in the route-local work plan to avoid self-hash recursion
RUN_AUTHORIZED: false
OUTPUT_PATHS: same two DEV source paths only
ERROR_BATCH_INDEX: 2
ERRORS_USED_IN_CURRENT_BATCH: 2/10
CUMULATIVE_TECHNICAL_ERRORS: 12
LAST_FAILED_CANDIDATE_SHA256: F5E22457263CC30388BC40F27067F4DFBD7B05D34E23C769A4DE0ED6E088E898+6935F3A04AEBCE320098FF45C30EF43EDB5214596315B4CAF9CDB8A0DEEADDD0
FINDING_ID: NONE; runtime packaging successor
FINDING_CLASS: T1_TECHNICAL_NO_CLAIM_REACH
EARLIEST_INVALID_CHECKPOINT_ID: NONE_PRE_MODEL_RAW
TRACK_IDENTITY_GATE: SAME_TRACK_CONFIRMED
DONE_WHEN: exact segmented state machine and synthetic parity/mismatch regressions pass DEV.
NEXT_ROLE: main RC freeze, then math_script_auditor
```
