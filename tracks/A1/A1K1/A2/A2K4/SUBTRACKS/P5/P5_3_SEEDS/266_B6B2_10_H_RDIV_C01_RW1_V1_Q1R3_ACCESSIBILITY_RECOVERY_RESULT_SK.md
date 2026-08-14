# B6b-2.10 — Q1R3 exact-source accessibility-recovery výsledok

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-ACCESS-RESULT-20260727-183`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10`  
**Autor teórie:** Martin Jambor  
**Vykonanie access recovery:** Codex, hlavný orchestrátor  
**Stav:** `RESULT_CANDIDATE / PASS_Q1R3_FULL_TEXT_RECOVERED_FOR_FROZEN_S0_SCREEN / NO_PHYSICS_SCREEN / NO_RUN / NO_PYTHON`

## 1. Frozen vstupy

- frozen preregistrácia 265 SHA-256:
  `544D63C41537CACBA13C59A2EDD1CEFE936139B56A3AF12FF3D5515AC0FA3DAC`;
- freeze receipt task181;
- event ledger through task181 SHA-256:
  `C4456C26ED94576B0B1DB392538CB0797399F9767B28607812FCBF814049D5FF`;
- append-only exact access evidence 265A SHA-256:
  `006BF1E8BC3A88F2A9D2F68EA031AFD8CE6665DE8521436177EA6AA2E69E0F5D`;
- parent coverage result264 SHA-256:
  `DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A`.

## 2. Exact identity a provider selection

Jediný frozen exact-title query sa vykonal raz. Provider vrátil 15 hitov a
prvý hit bol:

[Model-dependent analysis method for energy budget of the cosmological
first-order phase transition](https://arxiv.org/abs/2301.12328), autori Xiao
Wang, Chi Tian a Fa Peng Huang, arXiv `2301.12328`.

Titul a autori sa presne zhodujú s frozen Q1R3; query result zároveň obsahuje
JCAP/DOI navigačné záznamy toho istého článku. Provider rank 1 preto vlastní
výber. Nijaký neskorší hit, nový kandidát ani companion zdroj nebol vybraný.

## 3. Call ledger a immutable evidencia

| ID | Call | Výsledok |
|---|---|---|
| A1 | jeden exact-title `search_query` | PASS; exact Q1R3 arXiv hit na ranku 1; raw uložený same-call |
| A2 | `open(turn38academia12)` | PASS; arXiv primary full-text view, provider uvádza 527 riadkov a sprístupňuje sekcie/rovnice |
| A3 | `open(turn39view0, line 30)` | cache miss; raw failure uložený, bez rerun |
| A4 | `open(https://arxiv.org/html/2301.12328)` | cache miss; raw failure uložený, bez rerun |

Presný rozsah:

```text
search_query calls = 1
open calls = 3
click calls = 0
open+click cap consumed = 3/3
query rewrites/pagination/new candidates = 0
Python processes = 0
```

V 265A sú presne štyri unikátne evidence IDs A1–A4 a štyri explicitné
BEGIN/END páry. Transport ani same-call publication nezlyhali.

## 4. Full-text success gate

A2 je arXiv primary full-text view toho istého záznamu, nie abstraktová alebo
citačná karta. Exact raw návrat uvádza `Total lines: 527` a priamo sprístupnil
napríklad:

- section 2 `Hydrodynamics`;
- scalar-field energy-momentum tensor `T_phi^{mu nu}`, equation (2.1);
- plasma kinetic energy-momentum tensor, equation (2.2);
- perfect-fluid tensor `(e+p)u^mu u^nu-g^mu nu p`, equation (2.3);
- explicitné väzby na friction/entropy production, fluid equations,
  across-wall EOM a ďalšie numbered energy/EOS equations.

To spĺňa iba frozen accessibility podmienku: primary full text, exact
identity, čitateľné relevantné action/EOM/energy rovnice a section/equation
identifiers sú k dispozícii v immutable 265A. A3/A4 cache miss tento úspešný
A2 dôkaz neruší.

Výsledok:

```text
PASS_Q1R3_FULL_TEXT_RECOVERED_FOR_FROZEN_S0_SCREEN
```

## 5. Čo výsledok neznamená

Tento atóm nevykonal S0–S13. Najmä nepotvrdil one-model closure,
`Z_rec`, `D_uW=P_rec>=0`, finite cycle-frozen `W_*`, disjunktný conservation
ledger, source-native `u_cell`/worldtube/`dmu_cell`, regular crossing,
dynamický daughter reset, covariance/stability ani null/source-off.

Preto:

- Q1R3 ešte nie je complete W10 ani reference-only verdict;
- W10 nebol získaný ani vyvrátený;
- C01 a `A_RW1` neboli potvrdené ani zamietnuté;
- F-A sa ešte fyzikálne neuzavrela a F-B/F-C sa neotvorili;
- fyzikálny screen smie pokračovať iba podľa už frozen dokumentu 261 po
  prijatí tohto access výsledku.

## 6. Počítadlá a súborový rozpočet

```text
P4 work atoms = 2_UNCHANGED
physical witness attempts = 0_UNCHANGED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
Python processes = 0
```

Recovery atóm vytvoril tri live vedecké artefakty: document265, evidence265A
a document266. Centrálne registre boli aktualizované jedným plánovaným
batchom current/K4/P5/event-ledger; package kópie sú nula.

## 7. Nezávislý auditný handoff

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-V1-Q1R3-ACCESS-RESULT-AUDIT-20260727-184
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_result_audit
ARTIFACT_AUTHOR_TASK_ID: /root task183
STATIC_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit task180
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_result_audit task184
PACKAGE_CURATOR_TASK_ID: RESERVED_EXTERNAL_PACKAGE_CURATOR_NOT_ACTIVATED
EXTERNAL_AUDITOR_TASK_ID: RESERVED_EXTERNAL_AUDITOR_NOT_ACTIVATED
SEPARATION_OF_DUTIES_CHECK: PASS_EXPECTED_ALL_DISTINCT
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_v1_Q1R3_ACCESS
CURRENT_PHASE: CANDIDATE_ACCESS_RESULT_AWAITING_INDEPENDENT_AUDIT
ALLOWED_NEXT_ACTION: independent read-only audit of frozen doc265, exact 265A and candidate doc266
ALLOWED_READS: mandatory bootstrap; documents259-266; receipts263A-D; evidence265A; event ledger; role config/manifest
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: web/search/open/click; edit; S0-S13 physics screen; infer W10; Python; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: document264=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A; frozen_document265=544D63C41537CACBA13C59A2EDD1CEFE936139B56A3AF12FF3D5515AC0FA3DAC; evidence265A=006BF1E8BC3A88F2A9D2F68EA031AFD8CE6665DE8521436177EA6AA2E69E0F5D
PREREG_SHA256: 544D63C41537CACBA13C59A2EDD1CEFE936139B56A3AF12FF3D5515AC0FA3DAC
RUN_AUTHORIZED: false
OUTPUT_PATHS: chat-only audit recommendation
DONE_WHEN: exact identity/provider-rank, 1-search/3-open cap, raw framing, full-text equation accessibility gate, counts/nonclaims and file budget are independently verified
NEXT_ROLE: main_orchestrator
```
