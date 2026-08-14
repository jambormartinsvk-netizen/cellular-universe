# Addendum to 05 — AR69, artifact ownership and shared core (EN)

**Date:** 2026-07-16  
**Scope:** additive rule; earlier rules are unchanged

## Duplication check

AR59 defines routes, AR61 history, and AR62 versioning of shared code. They do
not yet bind a track, runner, base module, result, and audit into one mandatory
chain. AR69 adds that binding without changing those rules.

## AR69 — One owner and a complete evidence chain for every artifact

Every script, base module, result, and audit has one route-conditioned owner.
The track manifest records the full chain
`gate → preregistration → runner → base+SHA → result → audit → verdict`.
A historical file is not copied into several tracks; a shared artifact belongs
to the nearest common node and other tracks only reference it.

A base module used by a result is immutable by version or SHA-256. A fix
creates a new version/hash, a list of every affected manifest, new results,
and a differential audit. A runner's technical PASS or a module's algebraic
PASS must not be recorded as a physical PASS of the whole track.

Moving historical files is forbidden until a Git baseline, a complete
`OLD_PATH → NEW_PATH` and SHA manifest, and a check of every dependency exist.
Until then navigation directories contain references, not copies.

Canonical layout: `tracks/00_ROUTE_AND_ARTIFACT_LAYOUT_SK.md`.

