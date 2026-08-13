# Selected external-audit evidence for v3.18

This directory is a Git-only audit layer. It is not part of the fixed
14-file Zenodo attachment set. Sealed package contents and existing auditor
responses were copied byte-for-byte from the project evidence archive;
their inclusion in Git does not itself grant a `PASS`.

The Slovak main document is the semantic authority. Links beside supported
equations point to the exact `00_SCOPE_AND_READ_ORDER.md` below. Responses
remain separate because a sealed package, an auditor recommendation, and an
authoritative project assessment are different evidence objects.

## Formula and result evidence

| Release equations | Package | Achieved scope | Response state | Mandatory boundary |
|---|---|---|---|---|
| (17)–(22), (30) | [EA-004](PACKAGES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/00_SCOPE_AND_READ_ORDER.md) | `T2_REPRODUCIBLE_CALCULATION_WITH_ENVIRONMENT_GAP` for formula lineage, multi-mode cancellation and conditional $A_f$ bookkeeping | [accepted with limitations](RESPONSES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/00_AUDITOR_AUDIT.md); [project assessment](RESPONSES/EA-20260717-004-KMPC-BACKGROUND-PRIMARY-REPRO/01_MAIN_ORCHESTRATOR_ASSESSMENT_2026-07-18.md) | no CLASS/CAMB, complete perturbations, CMB/$S_8$, author intent for `0.05`, or microphysical $A_f$ derivation |
| (25)–(27) | [EA-047](PACKAGES/EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY/00_SCOPE_AND_READ_ORDER.md) | T2 reproduction of exactly three conditional legacy-anchor sensitivity points | [`AGREE_WITH_LIMITATION`](RESPONSES/EA-20260801-047-V318-PT1-H0-S8-C2C3-THREE-POINT-LEGACY-SENSITIVITY/SUB-20260801-047-001/00_AUDITOR_AUDIT.md) | no likelihood, posterior, fit, interval, continuous envelope, hard prediction, full perturbations, P5.4/G8/G9, covariance, gauge, causality, or stability closure |
| (38), C2 half | [EA-029](PACKAGES/EA-20260719-029-KMPC127-C2-AUTHORITATIVE-AGGREGATE/00_SCOPE_AND_READ_ORDER.md) | sealed aggregate reproduction capsule | external response not completed at the cutoff | `10/10` is registry coverage, not a physical seed witness or external confirmation |
| (38), C3 half | [EA-039](PACKAGES/EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE/00_SCOPE_AND_READ_ORDER.md) | accepted T2 reproduction of a read-only logical aggregate | [`AGREE_IN_SCOPE`](RESPONSES/EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE/00_AUDITOR_AUDIT.md); [project assessment](RESPONSES/EA-20260722-039-KMPC148-C3-AUTHORITATIVE-AGGREGATE/01_MAIN_ORCHESTRATOR_ASSESSMENT_2026-07-22.md) | `45/45` does not re-audit the underlying physical solvers and is not a seed witness or new physical point |

## EA-047 package-control history

The scientific T2 calculation remains in primary package EA-047. Its later
revisions repaired only package control and did not rerun or extend the
science:

1. [R1 control repair](PACKAGES/EA-20260801-047-R1-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-REPAIR/00_SCOPE_AND_READ_ORDER.md) received a
   [`CANNOT_AUDIT` package-closure response](RESPONSES/EA-20260801-047-R1-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-REPAIR/SUB-20260801-047-R1-001/00_AUDITOR_AUDIT.md).
2. [R2 control closure](PACKAGES/EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE/00_SCOPE_AND_READ_ORDER.md) received a
   [control-only PASS response](RESPONSES/EA-20260801-047-R2-V318-PT1-H0-S8-C2C3-PARITY-CONTROL-CLOSURE/SUB-20260801-047-R2-001/00_AUDITOR_AUDIT.md).

The preserved checkpoint/submission relationships are listed in
[`HISTORY/00_CHECKPOINT_AND_AUDIT_SUBMISSION_REGISTER.tsv`](HISTORY/00_CHECKPOINT_AND_AUDIT_SUBMISSION_REGISTER.tsv).
The governing package protocol is
[`00_AUDITOR_PACKAGE_PROTOCOL_SK.md`](00_AUDITOR_PACKAGE_PROTOCOL_SK.md).

## Global nonclaims

- A package is not automatically a `PASS`.
- T2 reproduces a declared calculation; it is not proof of the full physical
  theory or of every assumption used by that calculation.
- None of the selected results has reached `T3_INDEPENDENT_IMPLEMENTATION`.
- Equations without a material package link in the main document do not have
  a canonical external package in this release.
- External recommendations do not themselves change a project track, score,
  depth, or release status.
