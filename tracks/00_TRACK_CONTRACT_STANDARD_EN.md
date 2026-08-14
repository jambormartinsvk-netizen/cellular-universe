# Track contract standard

This is the mandatory template for every active, blocked, or new physical
track. A dead track may use a shorter status document, but must link its
death reason, scripts, and immutable outputs. A computation may not change a
track outside its contract.

## Required fields

1. Full route and human-readable goal.
2. Parent formulation, exact state space, and prohibited reductions.
3. Finite ordered gates with PASS, STOP, and REVIEW.
4. Current state of each gate, evidence artefact, and next step.
5. Depth, scientific support, and work progress where defined.
6. Scope not yet covered.
7. Living, dead, and historical children with reasons.
8. Update rule and release control point.
9. Formula-provenance ledger: parent equation, lower form, term map,
   independent residual, limits, and dimensions.

## Use rule

Before every Python run, read the contract of the active track. The run
preregistration names its gate and may not extend the physics without a
contract change, a new physical track, or explicit review. A historical PASS
outside the active contract is evidence only for its explicitly recorded scope.
A text/AST PASS is always labelled `PASS_MAP`/`PASS_SCOPE`; a formula PASS
may be recorded only after AR66.2.
