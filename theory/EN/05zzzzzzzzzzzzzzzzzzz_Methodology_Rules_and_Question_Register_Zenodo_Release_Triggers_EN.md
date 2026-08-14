# Addendum to 05 — criteria for publishing Zenodo versions (EN)

## Duplicate check

AR5 protects the immutability of an already published version. AR9 requires a Git commit/tag and the technical release chain. AR48 adds the previously missing decision of **when** to publish a new version, when not to publish, and how to distinguish a patch, a new `3.x`, and `4.0`. The rules do not duplicate one another.

## AR48 — a Zenodo release requires a material trigger and a complete release gate

A new Zenodo version may be created only for a material trigger: a critical correction of a published claim, a completed scientific milestone, a coherent audit snapshot, a preregistration freeze before external data, or a reproducibility change that alters the scientific result.

An individual working subtest, timeout, open question, new hypothesis, decimal depth increment, or result-preserving refactor does not trigger a new version. Such changes accumulate in Git history and the working changelog.

Changing a published file always creates a new version, even when Zenodo technically provides a short correction window. Only non-semantic metadata may be changed without a new version, and every such change requires a metadata changelog.

A `3.x.y` patch must not change equations, numbers, verdicts, scope, or conclusions. A material change within the same theory receives a new `3.x` version. A change of fundamental postulates, core dynamics, ontology, or causal structure requires `4.0`.

A release is `GO` only after the complete checklist, agreement with the Git tag, changelog, manifest/SHA-256, and an audit of the frozen candidate. Any change after the manifest resets the release candidate.

## Q74 — when is v3.18 ready for Zenodo?

**Status:** `OPEN RELEASE GATE; CURRENTLY NO-GO.`

`R3.18-DOC` may be released while K4/G7 remains open if the open gates are stated precisely and no new predictive claim is made. It must still complete documentation cleanup, a single canonical status, the v3.17 -> v3.18 changelog, SK/EN cross-check, whole-package manifest, Git commit/tag, and an independent release audit.

`R3.18-PHYS/PREDICTION` remains NO-GO without the relevant A2/G7, A3/G8, and—for a data fit—G9 gates.

## Limitation of the older A0 wording

“A0 is complete” means that the rule of immutability, changelogs, and checksums was adopted. It does not mean that every current workspace or v3.18 candidate automatically passes the publication gate.

