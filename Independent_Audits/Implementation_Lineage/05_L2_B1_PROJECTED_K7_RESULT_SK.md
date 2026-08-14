# L2-B1 — výsledok equation/state auditu projektovaného K7 lineage

**Dátum:** 2026-07-15  
**Skript:** `scripts/238_script_lineage_L2_B1_projected_k7_ast_audit.py`  
**Vnútorný limit / vonkajší limit:** 5 s / 10 s  
**Výstup:** `scripts/results/k_mpc_005/RUN_LINEAGE_L2_B1_PROJECTED_K7_AST_AUDIT.json`  
**Verdikt auditu:** `PASS_AUDIT / IMPLEMENTATION_STOP_FOR_K4`

## Čo sa overilo

Statický AST audit bez importu modelov a bez ODE prešiel pod 0.1 s. Presne
roztriedil 16 artefaktov historickej vetvy K7 podľa toho, či definujú
redukovanú RHS, alebo iba overujú jej výstup.

| Trieda | Počet | Súbory | Verdikt |
|---|---:|---|---|
| Definuje redukovanú RHS bez `U_c` | 7 | 179, 197, 203–205, 209, 213 | `DO_NOT_USE_PHYSICS` pre A2-K4 |
| Checker redukovanej RHS | 9 | 181–183, 206–207, 210, 214–216 | `RUNNABLE_REVIEW_ONLY` |

Šesť definujúcich skriptov 197, 203–205, 209 a 213 súčasne používa starý
pevný `K_MPC` vo backgroundovej formulácii. Skript 179 je tiež redukovaný
a navyše už bol technicky karantenizovaný pre predpoklad poradia JSON kľúčov.

## Fyzikálny význam

Deklarovaný A2-K4 energy-frame prenos vyžaduje dynamickú rýchlosť popola
`U_c`. Projektovaná K7 RHS ju nemá. Preto ani jej dobre zdokumentovaná
numerická stabilita, constrainty, konvergencia a G0–G7 nemôžu potvrdiť plný
K4 mechanizmus. To je stop implementačnej vetvy, nie dôkaz, že mechanizmus
A2-K4 neexistuje.

Historické súbory a ich JSON sa nemenia. Sú uvedené v centrálnom registri
`scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md` s hashmi a AR8 stavom, aby sa
nemohli omylom znovu použiť ako fyzikálny dôkaz.

## Čo tento audit netvrdí

- nehodnotí správnosť plnej general-synchronous/P5 formulácie;
- neprepočítava historické ODE;
- nemení staré čísla hĺbky ani ich hash;
- nepridáva skóre A2-K4.

## Ďalší krok

`L2-B2`: rovnaký prenosový audit pre vetvu so zachovaným `U_c`
(testové pole 86, BR/general-synchronous nástupcovia a P5). Až ak táto
vetva prejde C1–C6, možno vykonať P5.2 constraint ledger a neskôr ODE.
