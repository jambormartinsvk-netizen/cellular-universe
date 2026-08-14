# Erratum: predbežný screening krivosti v skripte 16

**Dátum:** 2026-07-13  
**Dotknuté súbory:**

- `Questions/S8_H0_styri_nove_kolaje_prvotny_audit_2026-07-13.md`;
- `scripts/16_script_S8_H0_four_tracks_screening.py`;
- `Audit/audit_stareho_registra_Q4_Q8_Q11d_Q6_S8_2026-07-13.md`, ak odkazuje na predbežný verdikt skriptu 16.

## Oprava

Skript 16 držal hustoty fixné a testoval iba geometrickú zmenu vzdialenosti. Z toho odhadol, že `ΩK=0,002` nestačí na deklarovaný posun H0 a že by bolo potrebné približne `ΩK=0,012`.

Tento odhad **nesmie byť použitý ako konečný audit pipeline 09**, pretože pipeline pri každom `ΩK` znovu rieši:

- samosúladnú dnešnú `Ωm`;
- CMB uhlovú kotvu;
- rast perturbácií na zmenenom pozadí.

Skript 17 túto samosúladnú procedúru implementoval a presne reprodukoval dodaný grid:

- `ΩK=0,002 → H0=67,2672, S8=0,85712`;
- `ΩK=0,005 → H0=68,7060, S8=0,83034`.

## Nový autoritatívny stav

Pre K4 sa používa výhradne `AUDIT_FINAL_S8_H0_drag_curvature_v3.18_2026-07-13.md` a skript 17. Skript 16 zostáva zachovaný ako historická auditná stopa fixno-hustotného limitu, nie ako platný verdikt K4.

