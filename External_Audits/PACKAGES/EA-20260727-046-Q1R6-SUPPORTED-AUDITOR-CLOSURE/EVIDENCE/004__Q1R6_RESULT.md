# B6b-2.10 — Q1R6 local-reprocess S0–S13 výsledok

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R6-LOCAL-REPROCESS-S0-S13-RESULT-20260727-262`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Vykonanie a formalizácia:** Codex, hlavný orchestrátor  
**Frozen prereg SHA-256:** `266BCABBF7C7AEA87E9E01BC1120FDF3E44CE7841FC892AF391CD11B060C1228`  
**Kandidátny výsledok:** `PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY / REVIEW_Q1R6_NOT_A_COMPLETE_W10_WITNESS`

## 1. Integrity a complete local source

```text
archive277A SHA256:
  5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416
parent receipt277B SHA256:
  E26C8CCEC518E0358D8B8368EF1AEC9261315571F31C2D3AD374D1DA31953D02
local receipt279A SHA256:
  3D0A958E41298339173152DAB2561F5A6F6FF691DBFB1F0813CBFF15338CDEDA
entries:
  11
content classes:
  4 READABLE_TEXT / 7 BINARY_NON_TEXT
classification failures:
  0
include gaps:
  0
utphys.bst:
  READABLE_TEXT / UTF-8-STRICT
LOCAL_SOURCE_UNIVERSE_COMPLETE:
  PASS
new source operations:
  0
Q1R6 source lineage:
  1/1_TERMINAL_UNCHANGED
Python processes:
  0
```

Predchádzajúce pre-execution parser chyby a jeden performance timeout
nevytvorili receipt, nemenili archív a nenesú fyzikálnu inferenciu. Úspešný
receipt279A je publish-once immutable výsledok opraveného frozen procesu.

## 2. Primary/F-A stav

Q1R6 je pôvodný research source `First principles determination of bubble
wall velocity`, Benoit Laurent a James M. Cline (`main.tex:L83–91`). Je to
koherentný relativistický scalar–plasma interface model:

- Lorentz-invariant Boltzmannova rovnica a source term
  (`main.tex:L121–168`, Eq. `BE`, `BESimplified`, `source`);
- scalar a plasma EMT, EOM a total conservation
  (`main.tex:L174–247`, Eq. `EMTcons`, `EOM`, `EMT`, `EMTsimplified`);
- benchmark scalar potential a wall profiles
  (`main.tex:L356–423`, Eq. `vtree`, `EOMtop`, `ansatz`, `EOMmoments`);
- pressure barrier a terminálne wall riešenia
  (`main.tex:L428–449`).

Preto Q1R6 prechádza primary/F-A eligibility. Eligibility však nie je
complete W10.

## 3. W10 passport

| Pole | Provenance | Evidence status | Exact dôvod |
|---|---|---|---|
| `Z_rec` | `MISSING` | `NOT_A_W10_OBJECT` | Source-exact stav `{phi_i,T,u_plasma,delta f_i}` existuje (`L123–160`, `L174–247`), ale neexistuje kumulatívne `W_rec=W[Z_rec]`. |
| `P_rec` | `MISSING` | `NOT_A_NONNEGATIVE_RESERVOIR_POWER` | EMT flux a net pressure sú exact (`L218–247`, `L417–449`), ale nejde o pointwise `D_uW=P_rec>=0`; tlak mení znamienko a terminálny stav rieši `P_tot=0`. |
| `W_*` | `MISSING` | `PRESSURE_BARRIER_NOT_DELIVERED_WORK_THRESHOLD` | Potential/latent heat/Jouguet pressure barrier (`L360–368`, `L437–441`, `L465–476`) nie sú positive cycle-frozen delivered-work threshold. |
| conservation | `MISSING` | `TOTAL_EMT_ONLY` | Total EMT conservation je `SOURCE_EXACT` (`L174–235`), ale chýba disjunktný stored/dissipated/RW1-export/external-loss ledger a residual-interface tok. |
| `u_cell` | `MISSING` | `PLASMA_FLOW_NOT_PARENT_CELL_FLOW` | `u_plasma^mu` a wall velocity sú exact (`L134–148`), parent-cell význam by bol nová fyzika. |
| congruence/`dmu_cell` | `MISSING` | `NO_ONCE_ONLY_CELL_MEASURE` | Planárna wall coordinate a spherical fluid profile (`L134–137`, `L700–717`) nie sú parent worldtube/genealógia ani invariantná finite measure. |
| crossing | `MISSING` | `STATIC_PROFILE_NOT_TEMPORAL_FIRST_PASSAGE` | Source rieši spatial false→true wall profil a nonlinear terminal eigenvalue (`L249–267`, `L391–423`); nucleation je vstup (`L367–368`, `L715–717`). |
| `R_reset^Z` | `MISSING` | `NO_DAUGHTER_RESET_MAP` | Boundary transition medzi vákuami nie je reset, zero daughter work credit ani residual-energy ledger. |
| source-off | `MISSING` | `NO_EVENT_OFF_IDENTITY` | Pri `delta f=0` zostávajú LTE wall riešenia (`L372–375`, `L443`, `L502–506`); friction-off nie je event-off identita. |
| noncircularity | `DERIVED_SAME_MODEL` | `PASS_SCOPE_LIMITED` | Rovnice používajú scalar/plasma vstupy (`L104–118`, `L121–267`); GW a baryogenesis sú downstream motivácia/aplikácia, nie input. |

Jediné `MISSING` vylučuje complete W10; tu chýba deväť povinných riadkov.

## 4. S0–S13

| Gate | Výsledok | Dôvod |
|---|---|---|
| `S0` | `PASS` | original primary identita a complete local source universe |
| `S1` | `MISSING` | benchmark thermal/loop potential odkazuje na externý source (`L365`); explicitný OOE výpočet zahŕňa iba top quark, ostatné species sú future work (`L374–375`) |
| `S2` | `MISSING` | bez `W_rec=W[Z_rec]` |
| `S3` | `MISSING` | bez pointwise nonnegative reservoir power identity |
| `S4` | `MISSING` | bez cycle-frozen work threshold |
| `S5` | `MISSING` | total EMT nie je povinný disjunktný ledger |
| `S6` | `MISSING` | bez source-native parent-cell congruence a measure |
| `S7` | `MISSING` | static terminal boundary/eigenvalue problem, nie time first passage |
| `S8` | `MISSING` | bez physical reset mapy |
| `S9` | `MISSING` | Lorentz covariance a numerická konvergencia sú doložené, ale nie celý W10 causal/stability contract; collision/gradient aproximácie majú scope limity |
| `S10` | `PASS` | downstream GW/baryogenesis nie sú vstupom passportu |
| `S11` | `MISSING` | celý provisional `Y_div` by vyžadoval nové objekty |
| `S12` | `MISSING` | bez W10 source-off/event-off identity |
| `S13` | `PASS` | bez Pythonu, fitu do W10, steam/completion, score/depth zmeny a downstream runu |

## 5. Disposition a účtovanie

```text
PASS_Q1R6_REFERENCE_INTERFACE_MODEL_ONLY
/ REVIEW_Q1R6_NOT_A_COMPLETE_W10_WITNESS
```

Q1R6 je prijateľná referenčná interface fyzika, nie complete W10 witness a
nie fyzikálne vyvrátenie C01. Po nezávislom result audite a main acceptance
sa podľa frozen účtovania zvýši P4 work atoms `2->3`; physical witness
attempts zostanú `0`.

```text
P4 work atoms = 2_PENDING_3_AFTER_AUDIT_AND_MAIN_ACCEPTANCE
physical witness attempts = 0
K4 = 60/100
P5 = 3.5/6
RUN_AUTHORIZED = false
Q1R6 source operations = 1/1_TERMINAL
further Q1R6 fetch/reset = FORBIDDEN
```

Nevzniká C01/global no-go, dôkaz `A_RW1` emptiness, P5.3 closure, A3,
score/depth change ani run permission.

Live vedecké artefakty local-reprocess atómu sú presne 3: document279,
receipt279A a result280. Archive277A je immutable input, nie nová kópia.
Central register doteraz zmenil iba event ledger. Audit package copies `0`.

## 6. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R6-LOCAL-REPROCESS-S0-S13-RESULT-AUDIT-20260727-263
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_result_audit
ARTIFACT_AUTHOR_TASK_ID: /root::task262
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit::tasks254_256
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit::task263
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVE
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVE
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_AUTHOR_PREREG_RESULT_AUDITOR_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R6_LOCAL_REPROCESS
CURRENT_PHASE: COMPLETE_REFERENCE_ONLY_RESULT_AWAITING_INDEPENDENT_AUDIT
ALLOWED_NEXT_ACTION: read-only exact result280 audit against frozen document279 and receipt279A
ALLOWED_READS: mandatory bootstrap; documents261,277-280; archive277A metadata/hash; receipts277B/279A; result278; ledger tasks252-262; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: edit; internet/source operation; Python; companion/splice; invent W10 mapping; score/depth/run/package change; authoritative acceptance
IMMUTABLE_INPUT_PATHS_AND_SHA256: document279=266BCABBF7C7AEA87E9E01BC1120FDF3E44CE7841FC892AF391CD11B060C1228; archive277A=5CE87BF1E5D9CF0D170439D14EA4F1A6898453799810F834E68E5A179C335416; receipt279A=3D0A958E41298339173152DAB2561F5A6F6FF691DBFB1F0813CBFF15338CDEDA
PREREG_SHA256: 266BCABBF7C7AEA87E9E01BC1120FDF3E44CE7841FC892AF391CD11B060C1228
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation
DONE_WHEN: complete-universe integrity, primary/F-A eligibility, all 10 passport rows, exact line/equation provenance, S0-S13 map, reference-only branch, conditional P4 accounting, nonclaims and three-artifact budget are independently verified
NEXT_ROLE: main_orchestrator
```
