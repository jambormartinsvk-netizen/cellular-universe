# REGISTER 05 — EN update after A3/M-012 and K3a.0

**Date:** 2026-07-13  
**Status:** binding addendum; the older AR1–AR7 rules are unchanged

## Duplicate check

AR8 adds a physical rule for a mandatory fifth force; AR6 already separates
levels of evidence but does not govern a force required by an action. AR9
adds the GitHub -> Zenodo chain and safe documentation migration; AR5 already
protects the immutability of a published version but does not require a Git
commit/tag or a path-migration map. The new rules do not duplicate AR1–AR7.

## AR8 — A mandatory force is not deleted; an underived force cannot carry the result alone

If a local action or a conservation law requires a fifth force, it must be
included in both the background and perturbations with the correct sign. Its
existence is not an automatic death reason. A track may not survive by
deleting a mandatory term or by cancelling it with an independent post-data
brake. An alternative momentum transfer must arise from one covariant action,
pass the null limit and stability gates, and establish `G_eff` before fitting
`S8`. Until microphysics derives its magnitude, it is a declared
parameter/scaffolding rather than a prediction.

## AR9 — A Git commit is a mandatory predecessor of a Zenodo release

Before every new Zenodo release, a reviewed Git commit and release tag must
exist in the canonical repository. The release manifest contains the commit,
tag, changelog, and SHA-256 hashes. Documents are not moved without an
inventory, an old-path -> new-path map, and a link check. Generated caches and
local dependencies are not committed. Neither Git history nor a Zenodo record
is force-rewritten.

## Question updates

| ID | Question | Status |
|---|---|---|
| Q20 | What is the complete perturbative closure of the A1 transfer? | `OPEN IN A NEW FORM.` K5/K1 is dead M-012. K3a.0 passed its action, background, and high-k stability gate; K3a.1 must derive the full equations and `G_eff`. |
| Q35 | Did K5/K1 pass the CMB-normalized A3 growth gate? | `NO — DEAD M-012.` Conservative hybrid `S8=0.9836–1.0063`; rescue requires a 23–26% reduction of `A_s`. This is not claimed to be a full custom likelihood. |
| Q36 | Is there a healthy energy+momentum action not wholly dependent on the K5/K1 force? | `PARTLY.` `f=-f1(phi)rho_c+eta Z^2` exactly reproduces A1 and passes the first stability gate for `eta>=0`. `G_eff<=G` has not yet been proved. |
| Q37 | How will the documentation connect to GitHub and Zenodo? | `PLANNED.` Inventory and path map first, then safe Git staging, validation, commit/tag, and only then Zenodo with a changelog. |

## Older formulations restricted by the later audit

- `SURVIVES A2-K5.1 — 60/100; A3 red` was the correct preliminary state.
  The CMB-normalized growth gate supersedes it with `DEAD M-012`.
- The statement that `f2=eta Z^2` automatically gives weak gravity applies
  to the simple literature limit `f1=0`. Reproducing A1 requires `f1!=0`, so
  K3a.1 must derive the joint `G_eff`; importing the simple formula would be
  invalid.
- “Without a mandatory fifth force” is refined as follows: a fifth force is
  allowed when microphysics requires it; the model must not depend wholly on
  an underived term and may not cancel it post-data.

Details: `Audit/A3_K5_K1_MRTVA_CMB_normalizovana_rastova_brana_M012.md`
and `Audit/A2_K5_K3a_0_akcna_backgroundova_stabilitna_brana.md`.
