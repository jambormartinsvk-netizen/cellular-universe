# Q20/A2 — čítaj ako prvé po skriptoch K4.3b-73/74

**Dátum:** 2026-07-14  
**Aktuálny stav:** `A2-K4 ŽIVÁ 60/100; K4.3b NEUZAVRETÁ`

## Čo prešlo

- fotónový temperature/polarization hierarchy ledger;
- neutrínová a S1 parná hierarchy;
- exact `nu + steam` kolektívny/interný rozklad;
- Thomsonov tight-coupling collision block;
- CAMB 1.6.6 nulový rekombinačný interface;
- počet a nezávislosť siedmich štandardných analytických skalárnych seedov.

## Čo zmenilo starší obraz

K4.1 mala úplnú trojicu iba v systéme s jednou perfektnou radiáciou. Po
pridaní fotónov, neutrín a voľne letiacej pary má S1 sedem módov. Dva nové
velocity smery sú gauge-invariantne regulárne, ale Newtonova `U` premenná a
potenciály rastú ako `1/(k tau)`. Nesmú sa preto zabiť testom konečnosti v
Newtonovej gauge.

## Bezprostredný krok

**K4.3b-RG:** odvodiť a reziduálne otestovať sedem konečno-štartových radov
v regulárnej gauge, vrátane podvedúcich `lambda/E=O(a^2)` členov. Až potom
možno K4.3b uzavrieť a otvoriť K4.3c.

## Autoritatívna stopa

1. `Audit/A2_K4_3B_HIERARCHY_MODE_TAXONOMY_RECOMBINATION_AUDIT.md`;
2. `scripts/73_script_A2_K4_3b_hierarchy_and_regular_mode_taxonomy_audit.py`;
3. `scripts/74_script_A2_K4_3b_CAMB_recombination_interface_reference.py`;
4. `scripts/OUTPUT_A2_K4_3B_73_74.md`;
5. `Audit/A2_K4_3B_SCORE_AND_K4_1_SCOPE_ADDENDUM.md`;
6. `theory/SK/05zzzzz_Methodology_Rules_and_Question_Register_A2_K4_3b_SK.md`;
7. `theory/EN/05zzzzz_Methodology_Rules_and_Question_Register_A2_K4_3b_EN.md`.

