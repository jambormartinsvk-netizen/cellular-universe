# B6b-2.10 — Q1R1 full-text eligibility re-audit preregistrácia

**Task:** `A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R1-FULLTEXT-ELIGIBILITY-PREREG-20260728-317`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> SM_v1 -> B6b-2.10 -> Q1R1`  
**Autor teórie a rozhodnutia vrátiť sa ku Q1R1:** Martin Jambor  
**Formalizácia:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_UNFROZEN / AWAITING_INDEPENDENT_PREREG_AUDIT / NO_SOURCE_ACCESS / NO_PYTHON`

## 1. Dôvod návratu a nemenná história

Autor teórie po bounded technickom uzávere Q1R7 nariadil návrat ku Q1R1.
Historické dokumenty 261, 263, 263A a 264 zostávajú immutable. Q1R1 označuje
prvý hit Q1:

```text
General relativistic bubble growth in cosmological phase transitions
arXiv:2307.12080v2
Q1 rank: 1
historical classification: PRIMARY_OUTSIDE_F_A_REQUIRED_INTERFACE_ACTION
historical source evidence: arXiv abstract/metadata only
historical S0-S13 screen: NOT_PERFORMED
```

Dokument 264 odôvodnil klasifikáciu tým, že model používa zanedbateľnú
hrúbku phase boundary a nedodáva požadovanú finite-width local
scalar/interface action s odvodeným critical interface barrierom. Tento nový
atóm starú klasifikáciu neprepisuje. Overí iba to, či ju podporuje plný text
toho istého primárneho zdroja.

## 2. Presná otázka a obmedzený cieľ

Jediná otázka je:

> Obsahuje plný text arXiv:2307.12080v2 všetky povinné fyzikálne prekurzory,
> aby Q1R1 vôbec mohol byť `ELIGIBLE_PRIMARY` kandidátom rodiny F-A podľa
> frozen dokumentu 261?

Tento atóm nehľadá nový zdroj, nemení poradie Q1–Q4 a nevykonáva úplný
passport screen S0–S13. Eligibility vyžaduje súčasný PASS všetkých štyroch
bodov:

| ID | Povinný prekurzor | PASS podmienka |
|---|---|---|
| `G0` | primary/full-text identita | plný text má exact titul, autorov a arXiv ID/verziu Q1R1 |
| `G1` | lokálny finite-width interface stav | source-native lokálne pole/interface stupne voľnosti s explicitnou akciou alebo EOM; nie iba infinitesimálna pohyblivá hranica či jump podmienky |
| `G2` | coupled fluid/reservoir ledger | ten istý model explicitne spája interface sektor s fluid/reservoir sektorom a lokálnym energy-momentum tokom alebo conservation identitou |
| `G3` | kritická bariéra | z tej istej fyziky je odvodená konečná kladná critical interface barrier/work veličina použiteľná ako pre-event threshold; nie iba zadaná nucleation podmienka alebo post hoc energia |

`G1–G3` sa hodnotia z pomenovaných sekcií, rovníc a definícií plného textu.
Abstrakt, názov alebo agentov fyzikálny odhad samy nestačia.

## 3. Zmrazený source-access kontrakt

Nie je povolený žiadny nový `search_query`, query rewrite, pagination,
citations-following ani otvorenie iného paperu. Povolené sú najviac dve
deterministické access operácie toho istého zdroja:

1. `O1`: exact `open` cieľa
   `https://arxiv.org/html/2307.12080v2`;
2. `O2`: iba ak O1 neprejde nižšie definovaným
   `FULL_TEXT_COMPLETE_FOR_ABSENCE`, exact `open` cieľa
   `https://arxiv.org/pdf/2307.12080v2`.

Obe operácie sú `AT_MOST_ONCE`. Po transportnej, provider, parser alebo
persistence chybe sa tá istá operácia neopakuje. Redirect je prijateľný iba
v rámci hosta `arxiv.org` a musí zachovať exact ID `2307.12080` a verziu
`v2`.

Deterministický completeness gate je:

```text
FULL_TEXT_COMPLETE_FOR_ABSENCE =
  exact G0 title/authors/arXiv-ID/version identity
  AND searchable substantive model body
  AND searchable equation content
  AND boundary treatment
  AND energy/conservation treatment
  AND article through references
  AND every appendix declared by the article.
```

Word-limited alebo truncated návrat, metadata/abstract, PDF placeholder,
binary-only response, chýbajúce rovnice, chýbajúce referencie/prílohy alebo
incomplete provider extraction tento gate neprejdú. Ak O1 gate prejde, O2 sa
označí `SKIPPED_NOT_CONSUMED`. Ak O1 gate neprejde, O1 je spotrebované a O2
sa vykoná presne raz. Ak ani O2 gate neprejde, výsledok musí použiť
`UNRESOLVED_ACCESS`, nikdy `ABSENT`.

Každý vykonaný návrat sa bez ručnej obsahovej úpravy uloží v tom istom
orchestrated calle do jediného fresh receiptu:

```text
287A_B6B2_10_Q1R1_FULLTEXT_ACCESS_EVIDENCE.txt
```

Pred O1 musí preflight potvrdiť neprítomnosť **oboch** cieľov 287A a 288.
Kolízia ktoréhokoľvek cieľa znamená `NO_SOURCE_ACCESS`.

Receipt obsahuje task ID, operation ID, exact URL, provider payload,
`BEGIN_EXACT_TOOL_RETURN`, exact string alebo deterministický
`JSON.stringify(result,null,2)` a `END_EXACT_TOOL_RETURN`. Cieľ sa publikuje
iba ak je neprítomný. Pre každý ordinal O1/O2 explicitne zaznamená
`CONSUMED`, `SKIPPED_NOT_CONSUMED` alebo `NOT_REACHED`. Publish failure po
`open` trvalo spotrebuje danú operáciu, zakazuje jej retry a aktivuje
technickú/unresolved vetvu. Raw evidence sa neprepisuje.

## 4. Evidenčná a interpretačná mapa

Po úspešnom full-text prístupe hlavný orchestrátor vytvorí jediný result:

```text
288_B6B2_10_H_RDIV_C01_RW1_Q1R1_FULLTEXT_ELIGIBILITY_REAUDIT_RESULT_SK.md
```

Result musí pre `G0–G3` uviesť:

- source-native názov objektu;
- exact sekciu, rovnicu, tabuľku alebo stranu;
- stručnú parafrázu bez rozsiahleho kopírovania textu;
- klasifikáciu `SOURCE_EXACT`, `DERIVED_SAME_MODEL`, `ABSENT` alebo
  `UNRESOLVED_ACCESS`;
- dôvod, prečo ide alebo nejde o požadovaný finite-width interface/barrier
  prekurzor.

Tvrdenie `ABSENT` je dovolené iba pri
`FULL_TEXT_COMPLETE_FOR_ABSENCE=PASS`, po prehľadaní celého persisted exact
payloadu podľa relevantných source-native termov a po kontrole modelovej
sekcie, rovníc, boundary treatmentu, energy/conservation časti, referencií a
všetkých deklarovaných príloh. Neznámy synonymický termín sa nesmie
automaticky vyhlásiť za absenciu.

## 5. Predregistrované vetvy

```text
Ak G0 PASS a aspoň jeden z G1-G3 je z plného textu jednoznačne ABSENT:
  CONFIRM_Q1R1_PRIMARY_OUTSIDE_F_A_REQUIRED_INTERFACE_ACTION
  / NO_S0_S13_SCREEN;
  ide iba o source-local eligibility exclusion Q1R1, nie fyzikálny STOP C01.

Ak G0-G3 všetky PASS:
  REVIEW_Q1R1_ELIGIBLE_FOR_SEPARATE_S0_S13_PREREGISTRATION;
  nevzniká complete W10 ani physical-witness attempt.

Ak full text nie je dostupný, nie je prehľadávateľný alebo G1-G3 ostanú
nejednoznačné:
  REVIEW_Q1R1_FULLTEXT_ELIGIBILITY_UNRESOLVED_NO_PHYSICAL_INFERENCE.

Nikdy z tohto atómu:
  complete W10, PASS/STOP C01, A_RW1 emptiness/nonemptiness, closure P4/MF1,
  K4/P5 score alebo depth zmena, Q1R8, Python, solver, S8/H0 fit,
  steam/completion alebo biologická validácia.
```

P4 work atoms ostávajú `3` a physical witness attempts `0`. Technicky
dokončený eligibility result nemení tieto počty. Q1R1 full-text access je
samostatná technická línia s počiatočným stavom
`historical_packages_total=0` a `consecutive_technical_failures=0/10`;
technická access chyba nie je fyzikálny výsledok.

Zmrazené účtovanie:

```text
SOURCE_ACCESS_OPERATIONS_BEFORE: 0/2
HISTORICAL_PACKAGES_TOTAL_BEFORE: 0
CONSECUTIVE_TECHNICAL_FAILURES_BEFORE: 0/10

IF OFFICIAL_TRANSACTION_TECHNICAL_OR_PERSISTENCE_FAILURE:
  historical_packages_total = 1
  consecutive_technical_failures = 1/10
  source_access_operations = actual_consumed_n/2

IF COMMITTED_INTERPRETABLE_ELIGIBILITY_RESULT:
  historical_packages_total = 1
  consecutive_technical_failures = 0/10
  source_access_operations = actual_consumed_n/2
```

Čistý committed výsledok `UNRESOLVED_ACCESS` je technicky interpretovateľný
eligibility výsledok a patrí do druhej vetvy; neznamená fyzikálnu absenciu.

## 6. Freeze, audit a súborový rozpočet

Pred source access musí nezávislý auditor overiť scope, exact URLs, full-text
sufficiency, G0–G3, vetvy, nonclaims, output collision guard a parity
historických hashov. Po prijatí auditu hlavný orchestrátor zaznamená SHA
tejto preregistrácie mimo súboru. Od freeze sa tento dokument neupravuje.

Plán celého atómu:

```text
LIVE_SCIENTIFIC_ARTIFACTS:
  1 preregistration 287
  1 immutable access receipt 287A
  1 result 288
LIVE_CENTRAL_REGISTERS_UPDATED:
  route-local event ledger; current/K4/P5 iba ak výsledok zmení živý blocker
AUDIT_PACKAGE_COPIES: 0
PYTHON_PROCESSES: 0
```

## 7. Auditný handoff kapsul

```text
TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R1-FULLTEXT-ELIGIBILITY-PREREG-AUDIT-20260728-318
ROLE: physics_track_auditor
ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
ASSIGNED_AGENT_TASK_ID: /root/c01_q1r3_access_prereg_audit
ARTIFACT_AUTHOR_TASK_ID: /root
STATIC_AUDITOR_TASK_ID: NOT_APPLICABLE_Q1R1_NO_SCRIPT_STATIC_AUDITOR
INTERNAL_AUDITOR_TASK_ID: /root/c01_q1r3_access_prereg_audit
PACKAGE_CURATOR_TASK_ID: NOT_ASSIGNED_Q1R1_PREREG_PACKAGE_CURATOR
EXTERNAL_AUDITOR_TASK_ID: NOT_ASSIGNED_Q1R1_PREREG_EXTERNAL_AUDITOR
SEPARATION_OF_DUTIES_CHECK: author(/root)!=internal(/root/c01_q1r3_access_prereg_audit):PASS; author(/root)!=static(NOT_APPLICABLE_Q1R1_NO_SCRIPT_STATIC_AUDITOR):PASS_NOT_APPLICABLE_NO_SCRIPT; curator(NOT_ASSIGNED_Q1R1_PREREG_PACKAGE_CURATOR)!=external(NOT_ASSIGNED_Q1R1_PREREG_EXTERNAL_AUDITOR):PASS
ROUTE: A1_K1_A2_K4_P5.3g7_SM_v1_B6b-2.10_H_RDIV_C01_RW1_Q1R1
CURRENT_PHASE: DRAFT_UNFROZEN_BEFORE_ANY_NEW_SOURCE_ACCESS
PARENT_DECISION: Q1R7_CLOSED_AT_BOUNDED_TECHNICAL_BOUNDARY; author_directed_return_to_Q1R1
CLAIM: test_only_whether_full_text_supports_or_reverses_historical_Q1R1_F_A_eligibility_exclusion
NONCLAIMS: no_S0_S13; no_complete_W10; no_C01_truth_or_STOP; no_score_depth_A3_or_physical_witness_change
ALLOWED_NEXT_ACTION: independent read-only preregistration audit only
ALLOWED_READS: exact fully-qualified files and hashes below; mandatory ruleset; no live web source
ALLOWED_WRITES: none
FORBIDDEN_ACTIONS: source/search/open/click; edit; infer full-text content from abstract; change old documents; choose physical truth; Python; score/depth/run/package change
IMMUTABLE_INPUT_PATHS_AND_SHA256: D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/261_B6B2_10_H_RDIV_C01_RW1_V1_W10_PRIMARY_SOURCE_PASSPORT_DISCOVERY_PREREGISTRATION_SK.md=FB94A671AA861B5B9A18639AB9A4C565FC0F90A800723D232A0B073D3B877F5B; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/263_B6B2_10_H_RDIV_C01_RW1_V1_W10_SINGLE_QUERY_DIRECT_RAW_V2_PREREGISTRATION_SK.md=8CC33C71C2C7479399741EF5F8B0019645210555F8AB59BE9AB468C75CC95AF3; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/263A_B6B2_10_W10_Q1_DIRECT_RAW_TOOL_RETURN.txt=0C4FBC6F868DAE86C7ED8FA81195E9400918C5F8F8350BDFC7A0DDE8A74132E7; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/264_B6B2_10_H_RDIV_C01_RW1_V1_W10_RAW_V2_SOURCE_COVERAGE_RESULT_SK.md=DA9F5FCACAD15FF8D00C6C582D05E05E47ED33F764FD05A0286D607E394F079A; D:/Teoria/tracks/00_CURRENT_EXECUTION_PLAN.md=6B37A2C799F14C12FBC9FB719FD8F468D8F5A789969ADACF93F86BDB650E2610; D:/Teoria/tracks/A1/A1K1/A2/A2K4/00_WORK_PLAN.md=B37BFD2A54684201AD930984F9A9F143AAB0DE50A90B1C83FA300324AC636654; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_WORK_PLAN.md=55461DA9CA6F2C0B8735B6D711E16B1D9FDE84B977FAF97692E8674E4CD4C870; D:/Teoria/tracks/A1/A1K1/A2/A2K4/HISTORY/00_EVENT_LEDGER.md=F8FD29D221E667E55D79C47DE78749ED48C894914A8E01496350DB333A6D026A
FROZEN_EQUATIONS_AND_THRESHOLDS: G0_G3_all_PASS_required_for_eligibility; ABSENT_requires_FULL_TEXT_COMPLETE_FOR_ABSENCE_PASS; any_clear_G1_G3_ABSENT_after_complete_gate_confirms_only_Q1R1_source_local_exclusion; incomplete_or_unresolved_access_is_REVIEW_not_ABSENT
PREREG_SHA256: PENDING_AFTER_AUDIT
RULESET_PATHS_AND_SHA256: D:/Teoria/AGENTS.md=226710D6467FE923D6F2CBAFF02CE9235F1B48C07C4A9DACD95C6B06486B2B29; D:/Teoria/tracks/00_PROJECT_OPERATING_SYSTEM.md=519BDCBAE2CD9BF62351586E357DE3C9A28E60AD79CDB653661DD2821D65B6E7; D:/Teoria/tracks/00_READ_FIRST.md=3BE1654E58D51F0C7B2322B4C8D0CE3E7554A8599F479788B9F781244D930411; D:/Teoria/tracks/METHODOLOGY/05_WORKING_Methodology_Rules_and_Question_Register_SK.md=AB29543ACD4F132276DF59E1020EEA6FB3A042C78FAAA1B7DDD448F5479D0FF1
AUDITOR_RULESET_PATHS_AND_SHA256: same_as_RULESET_PATHS_AND_SHA256_for_live_internal_audit
AUDITOR_ROLE_CONFIG_SHA256: 0DBB0EDB9706C09AB4057C3E7FB4645D2DEA186FF15743688FE6B9F7CB8E304E
RUN_AUTHORIZED: false
SOURCE_ACCESS_AUTHORIZED: false
TIMEOUT_AND_OUTPUT_GUARDS: web tool bounded by provider; O1_and_O2_at_most_once_in_order; O2_exactly_once_only_if_O1_fails_FULL_TEXT_COMPLETE_FOR_ABSENCE; both_287A_and_288_must_be_absent_before_O1; no_retry_after_transport_provider_parser_or_persistence_failure; receipt_records_each_ordinal_consumed_skipped_or_not_reached
OUTPUT_PATHS: D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/287A_B6B2_10_Q1R1_FULLTEXT_ACCESS_EVIDENCE.txt; D:/Teoria/tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/P5_3_SEEDS/288_B6B2_10_H_RDIV_C01_RW1_Q1R1_FULLTEXT_ELIGIBILITY_REAUDIT_RESULT_SK.md
LIVE_FILE_BUDGET: 3_scientific_total_for_atom; preparation_batch_1_prereg_plus_1_event_ledger; package_copies_0
DONE_WHEN: auditor verifies historical scope, G0-G3 necessity, exact access order, no-search/no-rerun guards, evidence persistence, decision branches, counts and nonclaims and returns PASS or exact corrections
NEXT_ROLE: main_orchestrator
```
