# História balíka EA-028

## 2026-07-19 — DRAFT_NOT_DELIVERED

Balík zhromažďuje celý C2 NIV mód: KMPC-118 až 126, PF-114/115, immutable
rawy, versioned checkpoint/multi-rank successory a interné audity 190/197.

Theory author: Martin Jambor. Script creator/internal auditor: Codex
(OpenAI). Balík sa zapečatí až po štrukturálnom preflighte, negatívnom
guard teste, success vetvách a reprodukcii oboch technických failure vetiev.

## 2026-07-19 — SEALED_READY_FOR_EXTERNAL_AUDIT

- štrukturálny preflight: `361/361`,
- fresh-copy behavior vetvy: `10/10`,
- success field parity: `7/7`,
- negatívny guard a PF-114: fail-closed bez success rawu,
- PF-115: exact failure parity,
- po tomto zápise je obsah balíka immutable.
