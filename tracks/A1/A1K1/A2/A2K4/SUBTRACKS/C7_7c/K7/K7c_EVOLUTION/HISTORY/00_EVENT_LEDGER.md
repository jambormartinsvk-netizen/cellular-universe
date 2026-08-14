# K7c evolúcia — event ledger

| Event ID | Dátum | Udalosť | Dopad |
|---|---|---|---|
| `K7C-E20260715-001` | 2026-07-15 | P1 čistý RK4 reprodukoval tri mriežky | G5 zostala FAIL/REVIEW; bez bodov |
| `K7C-E20260715-002` | 2026-07-15 | vedecké P2 zmrazené ako `SCI-A2K4-C7G5-K7C-P2-MLEDGER` | rozsah a poradie nezmenené |

| `K7C-E20260715-003` | 2026-07-15 | skript 199 vykonal P2 s bitovou paritou stavov/RHS voči P1 | finálne `math.fsum` zlepšenie bolo `1×` na všetkých troch checkpointoch; fsum-only vetva STOP |
| `K7C-E20260715-004` | 2026-07-15 | P2 odhalilo dve analyticky nulové koeficientové kombinácie vytvorené v nebezpečnom float64 tvare | otvorená P3a vetva `SCI-A2K4-C7G5-K7C-P3A-ZERO-IDENTITY`; stav K7c REVIEW a hĺbka bez zmeny |
| `K7C-E20260715-005` | 2026-07-15 | P3a-A dokázalo presnú nulovosť racionálne aj pri 80 dps | povolená izolovaná P3b evolúcia; bez skóre |
| `K7C-E20260715-006` | 2026-07-15 | P3b po odstránení iba dvoch presných núl dosiahla pomer `16.004121` a rozdiel `3.0308221211e-14` | starý P1 G5 blocker obmedzený na legacy zápis; aktuálny G5 PARTIAL PASS/REVIEW; hĺbka `66.5` |
