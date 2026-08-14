# Q20/A2 — čítaj ako prvé po zavedení jemnej hĺbky

**Dátum:** 2026-07-14

| Koľaj | Stav | Jemná hĺbka | Posledná celá brána | Aktívny krok |
|---|---|---:|---|---|
| A2-K4 | **ŽIVÁ** | **66.0/100** | **G6 PASS** | **G7/C7.7a — BR3C-a** |

## Čo sa zmenilo

Fyzika ani G7 rozsudok sa nezmenili. Zmenilo sa zobrazenie auditnej hĺbky:
šesť chronologicky uzavretých balíkov medzi G6 a G7 dostalo po `1.0` bode.
K4 preto už nie je zobrazovaná iba ako 60, ale ako `66.0/100`.

G7 zostáva otvorená. Hodnota 66.0 neznamená čiastočný fyzikálny PASS,
pravdepodobnosť správnosti ani vstup do A3/G8.

## Aktuálny dôkazový stav

- C7.1 až C7.6: PASS v presne auditovanom rozsahu;
- skript 126: zachovaný ako REVIEW, nenahrádza autoritatívne 127/128;
- C7.7 až C7.10: PENDING;
- najbližšie: zostaviť dva fyzikálne rovnaké BR3C počiatočné stavy.

## Autoritatívne dokumenty

1. `Audit/A2_DECIMAL_GATE_DEPTH_SCORING_AND_K4_RECALCULATION.md`;
2. `Audit/A2_KATALOG_DECIMAL_DEPTH_ADDENDUM_2026-07-14.md`;
3. `Questions/00_AKCNY_PLAN_v3.18_ADDENDUM_DECIMAL_DEPTH_AND_BR3C.md`;
4. SK/EN pravidlo AR43 v registri 05.

