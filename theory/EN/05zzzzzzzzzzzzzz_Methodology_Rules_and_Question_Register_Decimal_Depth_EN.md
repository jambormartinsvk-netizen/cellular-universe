# Addendum to 05 — fine decimal audit depth (EN)

**Date:** 2026-07-14  
**Status:** binding addendum; older rules remain unchanged

## Duplication check

AR14 separated audit depth from probability of truth. AR18 prevented a
subtrack result from automatically promoting its parent. AR30 introduced the
same sequential G1–G10 gates in ten-point steps. What was missing was a way
to display audited progress **inside** an open gate without awarding the
whole gate. AR43 fills exactly this gap.

## AR43 — Track status has both a fixed gate and a fine audit depth

Every current status table must distinguish:

1. the **last fully passed canonical gate**, for example `G6 PASS`;
2. the **fine audit depth**, for example `66.0/100`;
3. the **status of the active gate**, for example `G7 OPEN`.

The interval between two canonical gates contains exactly `10.0` audit
points. Before the next calculation it is split into ordered evidence
checkpoints, each worth `0.1` to `1.0` point. Weights in one interval must
sum to exactly `10.0`.

For a track whose last passed gate is `Gg`, the fine depth is

```text
D_fine = 10*g + sum of the weights of contiguous passed checkpoints in G(g+1).
```

The following restrictions apply:

- before calculation, every checkpoint must state its deliverable,
  acceptance criterion, dependencies, and evidence file;
- no points are awarded for time spent, number of runs, number of equations,
  documentation by itself, or a favourable result without a closed test;
- the score increases only along a **contiguous** checkpoint sequence; a
  later test beyond an open gap is recorded as the deepest executed test,
  not as earned depth;
- a partial checkpoint PASS earns no proportional weight unless its own
  register explicitly contains smaller checkpoints;
- a fine value of `69.8/100` is still not `G7 PASS`; `70.0/100` requires the
  integrated verdict of the complete G7;
- fine depth does not promote a parent through AR18 and is not probability,
  confidence, or a percentage of truth;
- if a later audit invalidates a prerequisite of an earned checkpoint, the
  current fine depth is reduced and the change is explained in a changelog;
  the historical maximum and invalid evidence are not deleted;
- a dead track retains its last full gate, maximum achieved fine depth,
  deepest executed test, scripts, and death reason.

Checkpoints must not be fragmented merely to make the number increase. Each
must close a separately auditable physical or numerical claim.

## Migration of older tracks

An older integer score remains a correct statement of the last passed gate.
Decimal points must not be invented retrospectively from the location of a
failure. A track without a reliable ordered ledger remains, for example, at
`40.0/100`, while its deeper executed no-go is still reported separately.

The one-time reconstruction of the live K4 track is allowed because its G7
packages were named and archived chronologically before this addendum. Their
weights are frozen before BR3C and may not be changed in response to its
future result.

## Q70 — How should the real progress of K4 now be displayed?

**Status:** `66.0/100; G6 PASS; G7 OPEN.`

Six consecutive G7 evidence packages are closed at `1.0` point each. This
does not mean that K4.3b or the complete G7 passed. It means that the current
status no longer hides the work between 60 and 70. The detailed frozen
ledger is in
`Audit/A2_DECIMAL_GATE_DEPTH_SCORING_AND_K4_RECALCULATION.md`.

## Restriction of older wording

- Older statements that “the score remains 60 until all of G7 passes” now
  mean only that the `last full gate remains G6`; they do not prohibit fine
  depth values from 60.1 through 69.9.
- Older statements that “a subgate does not increase the score by itself”
  remain valid for awarding a full canonical gate. A fine checkpoint only
  displays the audited route toward it.
- The ban on an averaged or partial physical PASS remains in force. AR43
  introduces a depth ledger, not test voting or result averaging.

