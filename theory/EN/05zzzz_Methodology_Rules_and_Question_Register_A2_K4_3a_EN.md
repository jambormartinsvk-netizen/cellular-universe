# Addendum to 05 — A2-K4.3a status (EN)

**Date:** 2026-07-14  
**Scope:** question-register entry and interpretation limit; earlier rules are unchanged

## Rule-duplication check

No new rule is added. AR30 already awards a score only for a complete
sequentially passed gate, and existing rules already require null,
conservation, and sign tests. This addendum records the partial K4.3a result
and prevents it from being confused with the whole G7 gate.

## Q58 — Is the K4.3 species and anisotropic-stress interface ready for a full Boltzmann implementation?

**Status:** `K4.3a PASSED AT FORMULATION LEVEL; K4 REMAINS 60/100; G7 IS OPEN.`

The exact algebraic checks passed for:

- pairwise K4 energy and momentum conservation;
- the Einstein anisotropic constraint and the `Psi -> Phi` limit;
- recovery of the K4.2 `0i` interface at zero anisotropic stress;
- aggregation of photons, neutrinos, and steam into perfect radiation in the declared limit;
- Thomson-momentum cancellation between baryons and photons.

The test did not contain the complete photon-polarisation hierarchy, tight
coupling, recombination, the complete regular basis of the enlarged system,
or physical transfer functions. It therefore does not close G7 and does not
change the score.

Steam branch S1 is preregistered as free-streaming extra radiation because
that is the convention used by the existing CAMB reference. S2
(self-interacting steam) and S3 (a network-derived collision kernel) remain
separate waiting branches; death of one does not automatically kill the
others.

**Next question Q58a:** Does K4.3b pass the full hierarchies, tight coupling,
recombination, and the complete regular initial modes without violating the
constraints?

**Audit trail:**

- `Questions/A2_K4_3_G7_PROBLEM_PODBRANY_A_KILL_KRITERIA.md`;
- `Audit/A2_K4_3A_SPECIES_LEDGER_ANISOTROPIC_STRESS_AND_NULL_AUDIT.md`;
- `scripts/72_script_A2_K4_3a_species_ledger_and_anisotropic_stress_audit.py`;
- `scripts/OUTPUT_A2_K4_3A_72.md`.

