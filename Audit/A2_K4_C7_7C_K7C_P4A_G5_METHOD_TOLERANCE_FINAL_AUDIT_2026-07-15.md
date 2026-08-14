# A2-K4 / C7.7c / K7c / P4a — finálny audit metódovej a tolerančnej konvergencie G5

**Dátum:** 2026-07-15  
**Stabilné ID:** `SCI-A2K4-C7G5-K7C-P4A-METHOD-TOLERANCE`  
**Rozsudok:** `PASS_P4A_G5_METHOD_TOLERANCE_BREADTH`  
**Celý C7-G5:** `PASS`  
**Technické opravy použité:** `0`; prešla prvá implementácia V0

## Otázka

P3b dokázala štvrtý rád klasickej RK4 po kanonizácii dvoch presných núl.
P4a testovala, či rovnaký endpoint na tom istom NID/deep intervale dostanú
aj DOP853 pri dvoch toleranciách a implicitný Radau.

Source-delta audit 210 pred fyzikou potvrdil AST-identitu backgroundu,
seedu, scale, intervalu, fyzikálnych väzieb a všetkých 13 RHS komponentov.
Skript 209 menil iba solverový obal a fail-closed diagnostiku.

## Zmrazené očakávanie a výsledok

| Porovnanie | PASS hranica | Výsledok | Rezerva | Stav |
|---|---:|---:|---:|---|
| DOP853-tight vs P3b RK4-grid400 | `<=1e-8` | `1.1102230246e-14` | `9.01e5×` | PASS |
| DOP853-medium vs DOP853-tight | `<=1e-8` | `1.7526952112e-13` | `5.71e4×` | PASS |
| Radau-tight vs P3b RK4-grid400 | `<=1e-8` | `1.1213252549e-14` | `8.92e5×` | PASS |
| Radau-tight vs DOP853-tight | `<=1e-8` | `2.3279989048e-15` | `4.30e6×` | PASS |

Všetky tri prípady dosiahli presne `x=-24.75`, zachovali 13 stavových mien,
mali konečný endpoint a RHS, normalized maximum `1.0`, zostali hlboko pod
RHS capom `100000` a zapísali immutable JSON.

| Prípad | `nfev` | Diagnostika | Runtime | Stav |
|---|---:|---|---:|---|
| DOP853-medium | 41 | `njev=0`, `nlu=0` | `8.329 s` | PASS |
| DOP853-tight | 53 | `njev=0`, `nlu=0` | `6.891 s` | PASS |
| Radau-tight | 337 | `njev=2`, `nlu=6` | `6.812 s` | PASS |

## Kauzálny rozsudok

Na testovanom NID/deep intervale 0.25 e-foldu nie je endpoint závislý od
RK4, DOP853 alebo Radau ani od dvoch auditovaných DOP853 tolerancií na úrovni
relevantnej pre bránu. Kroková, tolerančná a metódová časť C7-G5 sú preto
uzavreté.

Výsledok podstatne znižuje riziko, že doterajšia K7 trajektória bola
artefaktom jedného solvera. Neodstraňuje riziká netautologickej aktivity,
ostatných módov/plôch, celého intervalu ani plnej hierarchie.

## Skóre a hĺbka

- C7-W1 strict support: `40 -> 60/100`;
- blocker aktuálnej K7: `0/100`;
- otvorené/nedosiahnuté: `60 -> 40/100`;
- úplné gate pokrytie: `40 -> 60/100`;
- WBS-1 progress: `48 -> 60/100`;
- jemná hĺbka A2-K4 zostáva `66.5/100`, kým ju nezmení samostatný depth
  crosswalk.

## Obmedzenia starších tvrdení

1. Stav „celý G5 PARTIAL PASS/REVIEW“ je nahradený úplným G5 PASS.
2. P3b zostáva samostatným dôkazom krokovej konvergencie.
3. P1 zostáva reprodukciou legacy float64 zápisu, nie blockerom K7.
4. Mŕtva fsum-only vetva zostáva mŕtva.

## Čo P4a nedokázala

- netautologickú C7-G4 aktivitu a constrainty;
- NID/NIV × deep/shallow C7-G6;
- plný interval a endpoint agreement C7-G7;
- plnú fotónovú/neutrínovú hierarchiu C7-G8;
- CMB, `S8`, `H0` alebo likelihood C7-G9.

## Ďalšia stena

Najbližšia rozhodujúca stena je jeden integrovaný balík
`C7-G4+G6+G7`. Z jedného spoločného runnera musí vyhodnotiť netautologické
constrainty a aktivitu, NID/NIV × deep/shallow a celý interval. Nové
písmenové P4b/P4c vetvy nevznikajú.

## Dôkazy

- `Audit/A2_K4_K7C_P4A_SOURCE_DELTA_210_2026-07-15.json`;
- `Audit/A2_K4_K7C_P4A_CORPUS_CHECKER_211_2026-07-15.json`;
- `Audit/A2_K4_K7C_P4A_DOP853_MEDIUM_RAW_2026-07-15.json`;
- `Audit/A2_K4_K7C_P4A_DOP853_TIGHT_RAW_2026-07-15.json`;
- `Audit/A2_K4_K7C_P4A_RADAU_TIGHT_RAW_2026-07-15.json`;
- `Audit/A2_K4_K7C_P4A_G5_AGGREGATE_RAW_2026-07-15.json`;
- `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/C7_7c/K7/K7c_EVOLUTION/P4A_G5_METHOD_TOLERANCE/ARTIFACTS/00_MANIFEST.md`.

