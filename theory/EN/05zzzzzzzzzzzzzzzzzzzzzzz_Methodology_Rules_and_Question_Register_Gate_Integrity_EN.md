# Addendum to 05 — imported-gate integrity and code reachability (EN)

Date: 2026-07-15  
Status: binding addendum; earlier rules remain unchanged

## Duplication check

AR39 already requires a composite verdict to fail closed when a data path is missing. AR45 already prohibits treating an enforced algebraic identity as an independent constraint PASS. AR51 therefore adds only an executable existence/type requirement for imported fields. AR52 closes a different gap in generated scripts that leave future markers in unreachable code. Tautological checks receive no duplicate rule; Q77 records the concrete application of AR45.

## AR51 — Imported fields must exist before they are compared

A gate comparing two values from JSON, a registry, or child output must separately verify before equality or a numerical threshold:

- that both keys exist at the expected path;
- that they have the expected type and, where relevant, are finite;
- the producer, mode, surface, and background identities when they affect the value's meaning.

The standalone pattern `mapping.get(a) == mapping.get(b)` is prohibited because it returns `True` when both keys are missing. A missing field is `REVIEW/FAIL-CLOSED`, never an implicit PASS.

## AR52 — An authoritative marker must be on a demonstrably executed path

When a wrapper generates source by inserting a block before an early `return`, it may not leave an old solver or a future patch marker after that return as an apparently active path. A new numerical variant must be a separately reachable function or script and must export the identity of the path actually executed. Patching a marker in unreachable code is a technical failure even when the textual replacement succeeded.

## Q77 — Which K7b/K7c formulations were restricted by the scripts 173–185 audit?

- The numerical PASS of 174–176 is not withdrawn: the physical registry was repaired and the actual payload had `reduced_rank=free_count=58`.
- The rank check inherited from 172 is nevertheless fail-open in implementation and needs a new fail-closed replacement before publication.
- `seed["D"]==D`, `seed["M"]==M`, `rhs[0]-(3D+2s²eta)`, and `rhs[1]-M` are self/construction identities with no independent confidence credit.
- Reconstructing the density/momentum species after defining them through `D,M` is only a float64 cancellation monitor.
- Script 185 exports the refinement ratio but does not gate on it. The current REVIEW is unchanged because the endpoint threshold also failed and the ratio `0.367` is non-asymptotic.
- The fixed-RK4 block in 183–185 executes, but the old `solve_ivp` after the early return is unreachable and must not serve as another marker.
- Incomplete script 186 is a non-authoritative preserved trail; its replacement must receive a new script number.
