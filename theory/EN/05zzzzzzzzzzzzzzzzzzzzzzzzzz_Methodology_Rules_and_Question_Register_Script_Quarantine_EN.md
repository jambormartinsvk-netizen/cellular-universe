# Addendum to 05 — central quarantine for historical scripts (EN)

Date: 2026-07-15  
Status: binding addendum; earlier rules remain unchanged

## Duplication check

AR29 governs time limits, AR53 the formal-error ledger, and AR54 pre-run expectations. A rule was missing that requires a central status check before every historical execution and distinguishes technically unrunnable, physically non-authoritative, environment-blocked, review-only, and superseded files. AR55 fills this operational gap without changing older verdicts.

## AR55 — A quarantined script is not run routinely

Before executing any existing `scripts/*.py`, consult `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md` or run checker 188 with `--target` and an explicit timeout.

A script classified as `DO_NOT_RUN_TECHNICAL`, `DO_NOT_USE_PHYSICS`, `ENVIRONMENT_BLOCKED`, `RUNNABLE_REVIEW_ONLY`, or `SUPERSEDED` may not enter a normal evidence chain. Direct execution is allowed only as a preregistered reproduction of an old error or a historical regression; it must state the expected error/REVIEW and may not replace the successor.

Status is bound to the full filename and SHA-256 revision, not merely the script number. Original files are not renamed or given new comments, preserving historical hashes and references. A repair should receive a new numbered file or an audited immutable wrapper.

`NOT_IN_QUARANTINE` is not a physical PASS. It means only that no known blocking reason is registered. Every other methodological and physical gate remains mandatory.

When a new error is found, update the formal-error ledger, checker-188 quarantine, and dated MD registry before continuing.

## Q80 — What is the current result of the first corpus audit?

Without executing targets, the checker read 192 Python files. It found exactly the preserved syntax errors 118/119, incomplete script 186 without an execution entry, and reconciled 62 quarantined files: 18 technical, 7 physically non-authoritative, 2 environment-blocked, 21 review-only, and 14 superseded. The target smoke test blocked 118 with exit 2 and labelled non-quarantined 176 only as `NOT_IN_QUARANTINE`, with no physical credit.
