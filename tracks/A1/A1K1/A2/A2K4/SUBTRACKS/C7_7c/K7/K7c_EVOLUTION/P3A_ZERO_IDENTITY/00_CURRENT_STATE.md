# P3a — presná nulová koeficientová identita

Stav: **P3a-A PASS / HANDOFF DO P3b DOKONČENÝ**
Stabilné ID: `SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY`  
Score effect P3a-A: `NONE`

P3a testuje, či sú dve cancellation-nebezpečné kombinácie v `M'` presne
nulové už z registrovaných definícií backgroundu. P3a-A je audit identity
bez ODE. Skript 201 dal `PASS_P3A_EXACT_ZERO_IDENTITY`: racionálne rezíduá
sú presne nula a najhoršie 80-dps normalizované rezíduum je `2.5069e-81`.
Tým bola P3b povolená. Nástupnícky skript 205 zmenil iba vyhodnotenie týchto
dvoch identít na nulu, zopakoval nezmenené RK4 mriežky 100/200/400 a prešiel
s pomerom `16.004121`. Evolučný výsledok patrí do samostatného uzla P3b.

Autoritatívna predregistrácia:
`Questions/A2_K4_C7_7C_K7C_P3A_EXACT_ZERO_COEFFICIENT_IDENTITY_PREREGISTRATION.md`.

Konečný P3a-A audit:
`Audit/A2_K4_C7_7C_K7C_P3A_EXACT_ZERO_IDENTITY_FINAL_AUDIT_2026-07-15.md`.
