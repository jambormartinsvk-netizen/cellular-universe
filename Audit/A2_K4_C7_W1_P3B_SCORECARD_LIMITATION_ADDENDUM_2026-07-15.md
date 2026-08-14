# A2-K4 / C7-W1 — limitation addendum starého G5 blockera po P3b

**Dátum:** 2026-07-15  
**Typ:** obmedzenie staršieho auditu; bez zmazania alebo prepisu dôkazu

## Obmedzený dokument

`Audit/A2_K4_C7_7C_K1_K7_LINEAGE_GATE_COVERAGE_AND_WEIGHT_AUDIT_2026-07-15.md`
vznikol pred P3a/P3b a správne vtedy zachytil P1 stav:

- G5 ako `FAIL/REVIEW` blocker s váhou 20;
- support 40, blocker 20, otvorené 40;
- RK4 pomer `0.367129` a dominanciu `M` v legacy float64 zápise.

## Neskorší dôkaz

P3a dokázala dve koeficientové identity ako presné nuly. P3b zmenila iba
tieto dve identity na kanonickú nulu a dosiahla:

- `diff200/400 = 3.0308221211e-14`;
- klasický RK4 pomer `16.004121`;
- source-delta dôkaz, že ostatná fyzická RHS sa nezmenila.

## Rozsah obmedzenia

Starý G5 blocker zostáva platný iba pre legacy float64 reprezentáciu a ako
dôkaz nebezpečného numerického zápisu. Nie je už blockerom kanonicky
opravenej formulácie. P3b však sama neuzatvorila celý G5, pretože ešte
chýba tolerančná a metódová konvergencia.

Aktuálny scorecard opravenej formulácie:

| Vedro | Hodnota |
|---|---:|
| strict support | `40/100` |
| aktuálny autoritatívny blocker | `0/100` |
| otvorené | `60/100` |
| pracovný WBS-1 progress | `48/100` |

Aktuálny G5 stav je `PARTIAL PASS / REVIEW`. Historický lineage audit sa
nemaže; pri každom jeho použití sa musí citovať aj toto addendum a konečný
P3b audit.

## Autoritatívne aktuálne zdroje

- `Audit/A2_K4_C7_7C_K7C_P3B_ZERO_IDENTITY_RK4_FINAL_AUDIT_2026-07-15.md`;
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/C7_7c/K7/00_SCORECARD.md`;
- `tracks/A1/A1K1/A2/A2K4/00_PROGRESS.md`.
