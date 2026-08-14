# REGISTER 05 — EN addendum for the A1-K1/A2 programme

**Date:** 2026-07-14  
**Status:** binding addendum; older rules remain unchanged

## Duplicate check

Existing track rules already preserve dead branches, maximum depth, and the
creation of physically distinct children. They did not explicitly state when
the death of an A2 child may be inherited by its A1-K1 background parent or
when the mechanism space is sufficiently exhausted. AR27 is therefore not a
duplicate.

## AR27 — Death of an A2 child is not automatically inherited by its A1 parent

A1-K1 remains `OPEN AND CONDITIONAL` while:

- at least one physically distinct A2 track remains open; or
- no general no-go theorem covers every A2 completion of A1-K1.

A1-K1 may be abandoned after a general no-go theorem or after documented
exhaustion of all registered K4, K7, K8, K9, K11, and K12 classes. Every
death must retain its scope, proof, script/calculation, and cross-check. A new
track must remove a specific death mechanism through new physics; renaming or
a post-data parameter does not count as an unexhausted possibility.

## Q53 — Is A1-K1 already a blind branch?

**Status:** `NO; THE A2 PROGRAMME REMAINS OPEN.`

- K1–K3, K5, and K6 are dead only in their exact tested scopes.
- K4 passed K4.1 and survives at `55/100`; K4.2 remains open.
- K7, K8, K9, K11, and K12 still contain open mechanisms.
- K10 changes the background and does not count as an A1-K1 rescue.

The immediate step is K4.2; if it dies, K8.1 follows.

### Limitation of older formulations

Older shorthand that inferred the death of the A1-K1 background from the
death of a particular A2 track is restricted by AR27. Only the precisely
tested completion is dead unless a document explicitly proves a general
no-go theorem.

## AR28 duplicate check

Existing rules require Einstein constraints and regularity, but they did not
explicitly distinguish a vector constructed at a finite time from the full
space of regular primordial Frobenius modes. AR28 is therefore not a
duplicate.

## AR28 — A primordial kill test must belong to the complete regular basis

A vector satisfying the Einstein constraints at a finite time is not thereby
an admissible primordial mode. A kill test based on initial perturbations
must:

1. derive the complete Frobenius/indicial basis as `a -> 0`;
2. reject divergent modes with `Re(p)<0` unless microphysics explicitly
   proves another admissible initial interface;
3. show that the tested vector belongs to the regular constrained space;
4. report absolute transfer separately from the ratio to a null reference;
5. preserve any invalid historical seed and explain the limitation.

A death produced by a vector outside the regular primordial space must not
be inherited by the whole track.

## Q54 — Did A2-K4 pass the complete regular superhorizon gate?

**Status:** `YES WITHIN K4.1 SCOPE; K4 SURVIVES AT 55/100.`

The indicial audit found exactly three regular modes, and both the primary and
independent integrators passed. The historical M-011 velocity seed is outside
their span. The result does not include high-k physics, a full Boltzmann
hierarchy, or CMB-normalised growth. The immediate step is K4.2.

### Limitation of the older M-011 formulation

M-011 is retained as a historical row, but K4.1 restricts its substitution of
`ln(T/T0)` for absolute `ln(T)` and its use of a non-regular primordial seed.
Any future death of K4 must have a new reason.

## AR29 duplicate check

Existing rules govern preservation of calculations, evidence, and dead
tracks, but they do not impose a mandatory runtime limit on launched
processes. A register search found no older rule with the same content. AR29
is therefore not a duplicate.

## AR29 — Every script execution must have an explicit time limit

Every new or historical script may be launched only with an explicit external
time limit.

- reads, searches, hashes, and short checks: `15 s` by default;
- normal numerical or symbolic runs: at most `60 s`;
- longer calculations: split into segments of at most `60 s` with
  checkpoints;
- inspect a running process at intervals no longer than `10 s`;
- after a timeout, terminate the process, record `TIMEOUT` in MD, and rerun
  only with a new explicit limit;
- a limit must never be silently removed or replaced by unbounded waiting.

A timeout is not a physical FAIL. The track remains without a verdict until a
complete result exists. New long-running scripts should also provide an
internal runtime limit and checkpoint where practical, but the external limit
remains mandatory.

The detailed operational record is `scripts/00_EXECUTION_TIME_LIMITS.md`.
