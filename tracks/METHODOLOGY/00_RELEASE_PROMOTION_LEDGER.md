# Ledger povýšenia pracovnej metodiky do release registra

**Aktualizované:** 2026-08-01  
**Aktuálny release candidate:** neotvorený

| Kandidát | Pracovný vlastník | SK/EN | Dôkaz uzavretý | Rozhodnutie hlavného orchestrátora | Release trigger/changelog | Stav povýšenia |
|---|---|---|---|---|---|---|
| AR70 — hranica `tracks`/`theory` | `tracks/METHODOLOGY/` | pair | organizačný audit 2026-07-16 | prijaté pre pracovný workflow | zapísať pri otvorení v3.18 RC | `WORKING_ACCEPTED / NOT_RELEASED` |
| FS-GATE-02/02a — neznáma funkcia ako prípustná množina, route-local návrat a AND/OR logika smrti | `tracks/METHODOLOGY/05_WORKING_*` + `00_CONSTRAINT_FEASIBILITY_GATE_*` | pair | autorovo rozhodnutie 2026-08-01; SK/EN ID, stavová hierarchia a povinné polia parity overené | prijaté pre pracovný workflow: hľadá sa neprázdny fyzikálne prípustný rozsah; nenájdená funkcia nie je smrť; track/theory STOP až po scoped certifikáte prázdnosti a úplnej AND/OR propagácii | zahrnúť do jediného v3.18 05aa SK/EN registra; changelog uviesť, že ide o metodické spresnenie bez nového fyzikálneho PASS/STOP | `WORKING_ACCEPTED / READY_FOR_05AA_CONSOLIDATION / NOT_RELEASED` |
| PT1 H0/S8 C2-C3 — trojbodová legacy citlivosť | `tracks/RELEASE/V3_18/PT1_H0/` | release text až v SK/EN páre | 9 immutable rawov; interný math/physics audit; externý EA-047 T2 reprodukoval všetkých 9 final cells; R2 control follow-up `PASS_P0_CONTROL_REPAIR` | prijaté iba ako tri podmienené sampled body; bez dopadu na A2-K4/G8/G9; `EA047-EXT-P0-001` a `EA047-R1-EXT-P0-001` majú claim reach `NONE`, R2 uzavrel control vrstvu | pred release zachovať nonclaims, použiť novú 11-ID status tabuľku a changelog; nepublikovať body ako interval ani tvrdú predikciu | `WORKING_ACCEPTED / EXTERNAL_T2_CONFIRMED / P0_CONTROL_CLOSED / NOT_RELEASED` |

Do tohto ledgera sa zapisuje iba delta pripravená na budúce povýšenie.
Samotný riadok nemení publikovanú verziu a neoprávňuje editovať Zenodo.
