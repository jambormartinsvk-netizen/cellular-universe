# EA-047-R1 — P0 oprava parity fresh hash reťazca

**Stav:** `SEALED_READY_FOR_AUDIT / NOT_SENT`  
**Package class:** `PACKAGE_REPAIR_REVISION`  
**Target tier:** `P0_CONTROL_REPAIR_AUDIT`; parent `T2_REPRODUCIBLE_CALCULATION` pre 9 final cells sa neopakuje  
**Autorita:** byte-identické parent evidence, exact parent response a opravená control vrstva; externý auditor iba odporúča  
**REPAIRS_PACKAGE_ID:** `EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY`  
**REPAIRS_MANIFEST_SHA256:** `646D81CE21B6CF5CCC3E3125B3DFC10DFF3E54ECE947272C3892997DD459F6B7`  
**REPAIRS_FINDING_ID:** `EA047-EXT-P0-001`  
**PARENT_RESPONSE_SHA256:** `2E6316559D687F545286DD4442489BD177D94D61006B61C0EEF10B5E8CC92E6D`  
**PACKAGE_CURATOR_TASK_ID:** `/root`  
**EXTERNAL_AUDITOR_TASK_ID:** `/root/v318_pt1_h0_s8_external_auditor`  
**SEPARATION_OF_DUTIES_CHECK:** `PASS(curator != external auditor)`  
**AUDITOR_ROLE_CONFIG_SHA256:** `98E55F94679F49D4DCE08E3281AE2A38F899B896E25726F9A3C2A85A9FC997E3`  
**RUN_AUTHORIZED:** `false`; táto revízia nevyžaduje nový Python ani vedecký run

```text
CHECKPOINT_ID: CP-RELEASE-V318-PT1-H0-S8-C2C3-20260801-001
ROUTE_AND_GATE: RELEASE/v3.18/PT1_H0/C2-C3 / P0_PACKAGE_CONTROL_REPAIR
ACCEPTED_STATE: WORKING_ACCEPTED_NINE_CELL_SAMPLED_LEGACY_SENSITIVITY / EXTERNAL_T2_CONFIRMED_WITH_P0_CONTROL_LIMITATION / NOT_RELEASED
PARENT_CHECKPOINT_IDS: NONE_FIRST_RELEASE_DIAGNOSTIC_CHECKPOINT
SUPERSEDES_CHECKPOINT_ID: NONE
CHECKPOINT_STATUS: ACCEPTED_REUSABLE_CHECKPOINT_EXTERNAL_T2_CONFIRMED_P0_REPAIR_SEALED
AUDIT_SUBMISSION_ID: SUB-20260801-047-R1-001 reserved at seal; registration/sent state lives outside immutable package
```

## Súborový rozpočet

```text
LIVE_SCIENTIFIC_ARTIFACTS=0
LIVE_CENTRAL_REGISTERS_UPDATED=0 before seal
LIVE_FILES_CHANGED_TOTAL=0 before seal
AUDIT_PACKAGE_COPIES=40
RESPONSE_TEMPLATE_FILES=1
NEW_PACKAGE_AND_RESPONSE_FILES_TOTAL=41
```

`BUDGET_EXCEPTION_JUSTIFICATION`: package prekračuje default o jediný súbor,
pretože P0 revízia musí zachovať všetkých 39 položiek parent balíka a navyše
pribaliť exact-hash response, ktorá definuje opravovaný finding. Vynechanie
response by nahradilo primárny nález parafrázou. Všetkých 29 pôvodných
vedeckých evidence a oba REPRO súbory sú byte-identické s parent balíkom.

## Presná otázka

Opravujú `02/03` rozpor tak, že:

1. fresh reference a continuation reťazec sa viaže na skutočné fresh
   whole-file SHA;
2. accepted-copy parita sa pre direct/reference/final rawy kontroluje v
   pôvodnom rozsahu;
3. pri A sa ako očakávane dynamické označia iba `runtime_seconds` a
   `reference_stage_sha256`, pri B/C iba `runtime_seconds`,
   `reference_stage_sha256` a `predecessor_segment_sha256`;
4. tieto provenance hashe sa neignorujú: musia exaktne sedieť so SHA
   skutočných fresh predecessor súborov;
5. žiadne fyzikálne pole, guard, threshold, identity, bisection state,
   iteration count alebo verdict sa nesmie normalizovať?

## Rozhodovanie

- `PASS_P0_CONTROL_REPAIR` iba ak exact parent evidence parity prejde,
  priložená response presne viaže `EA047-EXT-P0-001` a nový text odstraňuje
  rozpor bez oslabenia fresh SHA-chain integrity alebo vedeckých polí.
- `REVIEW_P0_CONTROL_REPAIR` pri nejasnom alebo neúplnom field contracte.
- Ak sa zmenil jediný pôvodný vedecký evidence/REPRO bajt, nejde o P0:
  `PACKAGE_REPAIR_IDENTITY_FAILURE`.
- Auditor nevydáva nový fyzikálny verdict; parent T2 a nonclaims ostávajú.

## Poradie čítania

1. `EVIDENCE/001-004`, manifesty, runtime map a checkpoint provenance.
2. `EVIDENCE/030__EA047_EXTERNAL_RESPONSE.md` — presný finding a parent T2.
3. `02_AUDITOR_INSTRUCTIONS.md` a `03_REPRODUCTION_AND_EXPECTATIONS.md`.
4. Manifestovo overiť byte parity `EVIDENCE/001-029` a oboch `REPRO` voči
   parent/source hashom. Nový Python nie je požadovaný ani autorizovaný.

## Nonclaims

- Revízia nemení contract, RC, input, raw, interný audit ani vedecký verdict.
- Nepridáva likelihood, posterior, fit, interval ani aktuálnu tvrdú v3.18
  predikciu `H0/S8`.
- Neuzatvára P5.4, G8, G9, covariance, gauge, causality alebo stability.
- Nemení A2-K4, A1-K1, skóre, hĺbku ani release oprávnenie.
