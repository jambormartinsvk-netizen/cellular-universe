# História EA-047-R2

## 2026-08-01 — DRAFT_NOT_DELIVERED / NOT_SEALED

- `PACKAGE_REPAIR_REVISION` R1 podľa findingu `EA047-R1-EXT-P0-001`;
- R1 skončil fail-closed pred auditom `02/03`, pretože sealed charter nemal
  explicitnú `AUDITOR_RULESET_PATHS_AND_SHA256` mapu;
- R2 pridáva exact mapu `EVIDENCE/001-004` a zachováva R1 parity contract;
- `EVIDENCE/001-029` a 2 REPRO položky sú byte-identické; `030` je exact R1
  response `FB55DA8D...E9E8D1`;
- scientific claim/checkpoint effect `NONE`; DEV/RC/official/science rerun `0`;
- package `40`, nested response `1`, spolu `41`; výnimka ostáva odôvodnená
  presnou primary response opravovaného findingu;
- manifest rebind dokončený: 37 riadkov, vrátane exact R1 response source/copy
  hashu `FB55DA8D...E9E8D1` a nových control hashov;
- live-side read-only preflight:
  `Test-ExternalAuditPackage.ps1 -AuditSubmissionId SUB-20260801-047-R2-001`;
  exit `0`, `197/197 PASS`, bez Pythonu a bez generated scientific outputu;
- čaká na nezávislý pre-seal review.

## 2026-08-01 — independent pre-seal review PASS

- recommendation: `PASS_PRESEAL — /root may seal EA-047-R2`;
- immutable capsule hashe, role config a separation of duties `PASS`;
- exact ruleset mapa `EVIDENCE/001-004` `PASS`;
- R1→R2 preserved evidence a REPRO `31/31 PASS`; `EVIDENCE/030` je exact
  R1 response `FB55DA8D...E9E8D1`;
- manifest `37/37`, package `40`, unlisted files `0`, nested response presne
  `1`, budget `40+1` s deklarovanou výnimkou;
- package-only inštrukcie a lifecycle marker review `PASS`;
- nezávislý preflight `197/197 PASS`, exit `0`; Python `0`.

## 2026-08-01 — SEALED_READY_FOR_AUDIT / NOT_SENT

- scope a human manifest boli prepnuté na sealed lifecycle;
- TSV scope hash sa znovu viaže a final nested-path preflight musí prejsť
  pred registry/submission zápisom;
- od úspešného final preflightu sa package bajty nesmú meniť.

### Final seal receipt

- final R8 nested-path preflight: `197/197 PASS`, exit `0`, wall time
  `1.4 s`;
- scope SHA-256:
  `750EB17B9D71224AD4C2902AB6D9D1A2958CBC182561021C8FCA87C6F03A98CC`;
- human manifest SHA-256:
  `014EAD3F977DEB850257B508BF07CEE60892B4EA2E152306B99C34EC7E7D2B96`;
- canonical machine manifest SHA-256:
  `B6EE1EABEAFA52210465DE4E08C445B282421CDEA10AB550F858C0862661A6BF`;
- inventory: `40` immutable package files; `1` nested response template
  outside package;
- canonical state: `SEALED_READY_FOR_AUDIT / NOT_SENT`;
- from this receipt onward no package file may be edited.
