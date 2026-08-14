# Addendum to 05 — Python formal-error ledger (EN)

Date: 2026-07-15  
Status: binding addendum; earlier rules remain unchanged

## Duplication check

AR29 already requires an external time limit for every execution and states that a timeout is not a physical FAIL. AR39 preserves a failed trail for catastrophic-cancellation repairs. AR50–AR52 cover hard anchors, imported fields, and generated-code reachability. A general rule was missing that requires a uniform ledger, pre-run syntax/serialization checks, and a preventive lesson for every formal Python failure. AR53 fills only that gap and does not alter the AR29 timeout thresholds.

## AR53 — Every formal Python error must remain in a ledger with its prevention

Before the first numerical run of a new or generated Python script, at least `py_compile`, a parser/CLI smoke test, and, where applicable, a JSON serialization smoke test must run under an external time limit. For generated source, the generated text itself must be compiled, not merely the wrapper.

When a syntax, parser, import, marker, serialization, CLI, data-path, or runtime-API error occurs:

- preserve the original script and output;
- record the exact exception, root cause, and whether any physics executed;
- classify the result as `TECHNICAL_ERROR/REVIEW`, not a physical PASS or death;
- create the repair as a newly numbered script or an explicitly audited immutable wrapper;
- add a preventive check to `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` so that the same error class is not repeated silently.

A successful `py_compile` is not sufficient evidence. It must be followed by a minimal behavioural smoke test capable of exposing key-order, marker-path, serialization, fail-open, and executed-path errors.

AR29 remains independently mandatory for every launch: the external timeout may not be omitted even when the script has an internal deadline.

## Q78 — Where is the permanent obligation to record errors and timeouts?

Global assistant memory across independent tasks is not guaranteed. The authoritative project memory is:

- AR29 and `scripts/00_EXECUTION_TIME_LIMITS.md` for every external/internal time limit;
- AR53 and `scripts/00_PYTHON_FORMAL_ERROR_LEDGER.md` for formal and implementation errors;
- audit MD files and preserved old scripts for the specific cause and retrospective reproduction.

When future work reads these files first, the rules survive a new chat or a change of auditor.
