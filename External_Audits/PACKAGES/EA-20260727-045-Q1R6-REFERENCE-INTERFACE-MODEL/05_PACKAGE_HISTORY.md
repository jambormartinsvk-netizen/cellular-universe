# História balíka EA-045

## 2026-07-27 — DRAFT_NOT_DELIVERED / NOT_SEALED

- nový package ID; existujúce balíky a responses zostali immutable;
- scope je T1 static reference-interface audit jediného immutable source
  archívu `2204.13120` a jeho frozen Q1R6 receipt/result mappingu;
- 13 single-copy evidence položiek a 7 control files, response template 1:
  spolu 21 nových files, pod limitom 40;
- jediný primary archive je `EVIDENCE/002`; `main.tex` ani ďalšie vnútorné
  položky sa mimo archívu neduplikujú;
- `REPRO=0`, runtime mapa je header-only, Python/network/solver/generated
  JSON sú zakázané;
- curator `/root/q1r6_ea045_curator`, author `/root`, internal auditor
  `/root/c01_q1r3_access_result_audit` a reserved external auditor
  `/root/q1r6_ea045_external_auditor` majú rozdielne identity;
- live county: science 0, central register 1, total 1; package copies 20;
- balík čaká na curator live-side R6 preflight a potom na nezávislý pre-seal
  review. Kurátor nevydáva auditný názor ani seal.

## 2026-07-27 — PREFLIGHT_PASSED_AWAITING_INDEPENDENT_PRESEAL_REVIEW / NOT_SEALED

- live-side PowerShell 7 R6 preflight prešiel `86/86`, exit code `0`, wall
  time `986 ms`;
- source/copy parita prešla `13/13`; package files `20`, response template
  `1`, `REPRO` files `0`, runtime rows `0`, temp files `0` a pending-hash
  markery `0`;
- preflight nevykonal Python, solver, network ani generated JSON;
- bol aktualizovaný iba tento lifecycle zápis, scope lifecycle marker a jeden
  append-only package-register row; evidence a manifest TSV sa nemenili;
- ďalšia rola je nezávislý read-only pre-seal reviewer. Kurátor nevykonal
  seal ani audit a balík nie je sent.

## 2026-07-27 — F1 protocol-classification correction / NOT_SEALED

- independent pre-seal reviewer found F1: the previous static
  reference-interface scope omitted the mandatory protocol section-6 result
  classification;
- exact-delta correction added
  `REQUIRED_PROTOCOL_RESULT_CLASSIFICATION=NONE_OF_FIVE_STATIC_REFERENCE_SCOPE`
  and an explicit nonclaim of all five protocol classes;
- the response contract now requires the external auditor to select one of
  the five protocol classes or `NONE_OF_FIVE_STATIC_REFERENCE_SCOPE` with a
  justification, without pre-filling an audit opinion;
- manifest TSV now hash-binds the changed package-generated scope control;
  evidence source/copy mappings and all science files remain unchanged;
- corrected live-side PowerShell 7 R6 preflight passed `88/88`, exit code
  `0`, wall time `721 ms`; `REPRO=0`, runtime rows `0`, temp files `0`,
  pending-hash markers `0`, and no Python/network/solver/generated JSON;
- package remains `PREFLIGHT_PASSED_AWAITING_INDEPENDENT_PRESEAL_REVIEW`,
  `NOT_SEALED`, `NOT_SENT`; next role is the same independent steward for
  exact-delta re-review.

## 2026-07-27 — independent pre-seal F1 delta review receipt (verbatim)

```text
TASK_ID: A2K4-Q1R6-EA045-INDEPENDENT-PRESEAL-F1-DELTA-REVIEW-20260727-271
ROLE: documentation_release_steward
ROLE_CONFIG_SHA256: 035FEDFB8D248BEF556BC75FE51E935B56190C1B7FB4087F074929F67C187DE7
ASSIGNED_AGENT_TASK_ID: /root/q1r6_ea045_preseal_review
FILES_CHANGED: 0
PYTHON_PROCESSES: 0
NETWORK: 0
RESULT: PASS
SEPARATION_OF_DUTIES_CHECK: PASS_REVIEWER_DISTINCT_FROM_CURATOR_AND_EXTERNAL_AUDITOR
F1_STATUS: CLOSED_NONE_OF_FIVE_STATIC_REFERENCE_SCOPE_AND_BLANK_REQUIRED_RESPONSE_CLASSIFICATION_WITH_JUSTIFICATION
MANIFEST_STATUS: 14_ROWS_13_EVIDENCE_PLUS_1_PACKAGE_GENERATED_SCOPE_CONTROL_ALL_SOURCE_COPY_PARITY_PASS
COUNTS: PACKAGE20_EVIDENCE13_CONTROLS7_RESPONSE1_REPRO0_RUNTIME_ROWS0
INDEPENDENT_R6_PREFLIGHT: 88_OF_88_PASS_EXIT_0
LIFECYCLE: NOT_SEALED_NOT_SENT_AT_REVIEW_NO_STALE_ACTIVE_MARKERS
SCIENCE_SCORE_DEPTH_RELEASE_RUN_CHANGE: NONE_RUN_AUTHORIZED_FALSE
RECOMMENDATION: CURATOR_MAY_EXECUTE_ONLY_EXACT_DELTA_SEAL
ROLE_IDENTITY_HASH: 035FEDFB8D248BEF556BC75FE51E935B56190C1B7FB4087F074929F67C187DE7
PRE_SEAL_SHA: scope D7E90B1EEE458F780F4D6C03B72CEE10C7EA33D36BF5AEE07F24ACA7302922A9; manifest_md 6093B7DFAF6AC448AFDE9CC15AB60D7C5E09CD61FDA4A9B9E703FA80EEAD3F1E; manifest_tsv D2DE66C878BB6728BB9FF68A9D5D51D4FB85BD75483C4ECB4A3089A9DEEA6DD7; history 10E417916B1FB5A0F07E640CF09B28ACA66D54F687EC5C46866217413513E9D4; register 6DA046D5D73AC0592165E55462B600BFFEBBE93537952A05E8A745FBA9604A5D
RUN_AUTHORIZED: false
```

## 2026-07-27 — SEALED_READY_FOR_AUDIT / NOT_SENT

- hlavný orchestrátor autorizoval iba exact päťsúborový seal delta po
  nezávislom `PASS` receipte vyššie;
- curator `/root/q1r6_ea045_curator` a designated external auditor
  `/root/q1r6_ea045_external_auditor` sú rozdielne identity;
- package scope lifecycle bol zmenený na `SEALED_READY_FOR_AUDIT / NOT_SENT`
  a scope control hash bol rebound v oboch manifestoch;
- evidence `001` až `013`, response, `02`, `03` a `04` neboli zmenené;
- ďalší krok je iba package-only externý audit. Curator už balík nemení.
