# História balíka EA-032

## 2026-07-19 — DRAFT_NOT_DELIVERED

R5 delta capsule obsahuje `32` jedinečných source/runtime/evidence kópií,
`7` controls a jednu oddelenú response šablónu. KMPC-133 je T2 cieľ; širší
CDI mode closure je transparentne T1 hash-bound ledger.

Balík sa zapečatí až po preflighte, missing-input branche, fresh-copy
compile/help/smoke/official a field parity kontrole.

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

- štrukturálny preflight: `240/240`;
- fresh-copy compile base/runner, help a smoke: `0/0/0/0`; smoke `4/4`,
  `physics_executed=false`;
- missing-KMPC-127 guard: PASS; štyri child procesy exit `2`, parent nonzero
  a bez generated JSON;
- fresh-copy KMPC-133 official: exit `0`, refinement a pair PASS;
- field parity: PASS po odstránení iba runtime polí a environmentálneho
  absolútneho koreňa jedného `frozen_algebra_source`; všetky vedecké polia,
  relative suffix a source hash sú exact;
- package `39` + response `1` = presne R5 limit `40`;
- po tomto zápise je balík immutable.
