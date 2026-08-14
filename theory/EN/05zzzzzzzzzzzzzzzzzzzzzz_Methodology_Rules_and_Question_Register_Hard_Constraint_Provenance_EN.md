# Addendum to 05 — hard anchors and registry provenance (EN)

Date: 2026-07-15  
Status: binding addendum; earlier rules remain unchanged

## Duplication check

AR39 covers catastrophic cancellation and preservation of failed numerical trails. AR45 prohibits double-counting a constraint. Neither says that exact physical anchors may not remain soft least-squares rows, nor that a main-solve registry may not be overwritten by a reference limit. AR50 fills this gap without changing earlier rules.

## AR50 — Physical anchors are hard and every registry must carry solve provenance

An initial condition, regularity zero, or normalization anchor declared exact must be enforced by a hard equality or variable elimination when coefficient equations are solved numerically. A smaller global least-squares residual does not justify moving that anchor.

If the same solve function is called for both the physical background and a reference limit, every exported registry must carry and verify the mode, background parameters, and call purpose. A later reference solve must not silently overwrite the registry used for a physical verdict. Cross-comparing registries from different backgrounds is `REVIEW`, not a physical PASS or death.

## Q76 — Which earlier K7b formulations were restricted by the later audit?

- K7b.3a in scripts 168/169 is dead because high precision left physical anchors as soft LS rows and moved them.
- Script 170 is only technically dead because mpmath does not support the attempted matrix slice.
- Script 171 repaired the slice, but its HP registry was overwritten by the later `mu=0` solve; it is not the authoritative physical HP registry.
- Script 172 therefore compared different backgrounds, and its REVIEW cannot kill K4.
- Script 173 stopped on an incorrect text-marker path before calculation.
- The authoritative repair is 174/175 and the final four-surface verdict is script 176.
