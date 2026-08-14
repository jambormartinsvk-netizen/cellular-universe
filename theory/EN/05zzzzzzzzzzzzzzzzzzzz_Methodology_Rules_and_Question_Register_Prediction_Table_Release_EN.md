# Addendum to 05 — the prediction table as a mandatory release trigger (EN)

## Duplicate check

AR48 generally requires a material trigger for a Zenodo release. AR49 specifies the sensitivity of the public prediction table: it defines a material change, permits withdrawal without a completed replacement, and introduces an operational protocol against leaving a known-wrong number public for too long. AR49 does not duplicate AR48.

## AR49 — a material prediction-table change mandates a new release

When a completed audit establishes that a published prediction, interval, status, or scope is materially wrong, the old row must be publicly marked `WITHDRAWN` or `SCOPE NARROWED`. It must not wait for a new value; the replacement may be `NOT YET AVAILABLE`.

A validated new value triggers a second release or prediction-table update. A material table change is a new minor `3.x` version, not a patch. A fundamental change belongs to `4.0`.

A change is material when it changes the status, a value beyond numerical tolerance/rounding, an interval, uncertainty, falsification threshold, sign, trend, mechanism, dataset, or scientific interpretation.

If the new value was obtained after using the target data, it must be labeled `POST-DATA FIT` or `CONDITIONAL ESTIMATE`, not `PREDICTION`.

Operational target: after an audited withdrawal, create a public working record within 3 working days and a narrow Zenodo erratum within 14 calendar days; after a validated replacement, publish an update within 30 calendar days. A delay must be publicly marked and justified. These targets do not permit bypassing the audit, manifest, or Git tag.

## Q75 — which rows of the v3.17 prediction table remain current?

**Status:** `CRITICAL RELEASE TASK — OPEN.`

Before R3.18-DOC, every row must receive `STILL CURRENT`, `SCOPE NARROWED`, `WITHDRAWN`, `REPLACEMENT VALIDATED`, or `RECALCULATION OPEN`. A withdrawn value must not be copied automatically into v3.18 merely because the new calculation is unfinished.

## Limitation of the older R3.18-PHYS wording

The requirement to wait for A2/A3/A8 applies to publishing a **new value as a physical prediction**. It does not prohibit an earlier DOC/ERRATUM release that withdraws an incorrect old value or reclassifies it as a historical/conditional estimate.

