# Addendum to 05 — hierarchical living plans and bounded search (EN)

**Date:** 2026-07-15  
**Status:** binding addendum; earlier rules remain unchanged  
**New rule:** AR66

## Duplication check

TRACK BIRTH already governs physically new tracks. AR30 and C7-W1 separate
sequential depth from evidence weight. The existing pre-run expectation,
timeout, Python error-ledger, and script-quarantine rules remain binding.

What was missing was a rule that limits the number of maintained navigation
control points, defines when they are updated, and prevents unlimited
numerical sub-branch proliferation. AR66 fills that gap without modifying
the earlier rules.

## AR66 — Three living-plan levels and a bounded-search contract

Each active route maintains at most three living work-plan control points:

1. a parent physical-branch plan listing living/dead tracks, the active
   track, and the stopping condition;
2. an active physical-track plan listing mandatory gates, depth, support,
   work progress, and the finite formulation register;
3. a current implementation/subtrack plan listing the concrete next
   computations, expectations, and decision branches.

The deepest plan is updated after a decision-bearing package. Its parent is
updated only when a whole gate, score, active child, or verdict changes. The
top plan is updated only when the physical track, station, or release
snapshot changes. A parser fix, log, or technical rerun does not require all
three documents to be rewritten.

Every plan must contain:

- the full route path and a plain-language problem statement;
- current status, active child, and separately identified sequential depth,
  scientific support, and work progress where applicable;
- completed work, missing work, and explicit PASS/STOP completion;
- a table of living, dead, waiting, and active children with reasons;
- authoritative links to audits, scripts, outputs, and HISTORY;
- the event that triggers the next plan update;
- the release-snapshot information needed by the changelog and manifest.

## Bounded search instead of millions of names

Before a numerical search begins, the finite list of existing discrete
formulations is recorded. A new formulation is allowed only when it removes
a documented failure cause and is mathematically different in its
representation or operator. A tolerance, solver, parameter, parser, or JSON
serialization change is not a new track.

For a continuous or large option space:

1. use one versioned runner and a configuration matrix;
2. start with a cheap broad screen under a fixed budget;
3. refine coarse-to-fine only in surviving regions;
4. preregister the target, PASS/STOP rule, and maximum iterations;
5. create a new subtrack name only after a physically or mathematically new
   cause has been identified, not after every result.

Each scientific package permits an initial implementation and no more than
two technical corrections. It must then end in PASS, physical STOP, or
`REVIEW_BLOCKED` with an architectural decision.

## Runtime and supervision rule

Every Python computation requires both an internal deadline and an external
timeout. Before execution, the expected result and the decision for both an
in-range and out-of-range result must be written in plain language. A run
longer than five minutes requires a separate justification, checkpoint or
resume support, and explicit user approval. Cases run separately so one
timeout cannot block the whole package.

## Release use

The three living plans are mandatory release control points. Before a
release, check their mutual consistency, update dates, active route,
depth/scores, open limitations, prediction-table changes, and links to the
changelog and SHA-256 manifest. Historical audits are never silently
rewritten; living plans link to them and identify the later audit that
limited an older statement.

## AR66.1 — binding contract of the current track

AR66 sets the number of living plans. AR66.1 adds an execution boundary:
before every new computation, one authoritative contract for the current
track must be identified. It must state the required state space, finite
ordered gates, PASS/STOP/REVIEW, prohibited reductions, current status, and
the scope not yet passed. A run preregistration must name its gate and may
not test a different system without a contract change or a physically new
track.

A historical numerical PASS cannot be carried into a new contract merely by
the track name. If a later audit finds a missing state or a different
formulation, the living contract needs a visible correction and the old plan
remains history with a link to the limiting audit. Template:
`tracks/00_TRACK_CONTRACT_STANDARD_EN.md`.

## AR66.2 — formula-provenance closure before an audit PASS

Before an audit PASS of a lower-level specification or script, correct
variable names, a successful solver, or a small internal residual are not
sufficient. Every required formula must have a formula-provenance ledger in
the track contract:

1. the parent covariant or canonical equation and an unambiguous convention
   for time, gauge, Fourier sign, and velocity normalization;
2. the derived lower-level form with every sign, coefficient, and
   approximation;
3. a map from every parent term to an implementation term, or an explicitly
   documented omission with its validity scope;
4. at least one independent algebraic or invariant residual test that is not
   merely a restatement of the definition of the same variable;
5. null limits and a dimensional check for every new coupling or fractional
   exponent.

A text/AST audit may only award `PASS_MAP` or `PASS_SCOPE`; a physical
formula PASS requires items 1–5. If an imprecise lower-level formula is found
after a PASS, preserve the old result but visibly limit it; all downstream
numerical gates return to `REVIEW_BLOCKED` until a new ledger passes. Record
the error in the error ledger and the track contract before proceeding.
