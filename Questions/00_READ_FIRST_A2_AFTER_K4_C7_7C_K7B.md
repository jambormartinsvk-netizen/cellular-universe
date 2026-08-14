# READ FIRST — A2 po PASS K4/C7.7c-K7b

Aktuálny stav: **A2-K4 je ŽIVÁ, 66.5/100; K7a a K7b PASS; C7.7c stále otvorená.**

## Uzavreté

- K7a: úplný projektovaný Jacobián vrátane `T' T^-1`, nulový limit a štyri NID/NIV deep/shallow plochy.
- K7b: high-precision počiatočné `D,M`, rekonštrukcia `delta_fs,U_fs`, Einsteinove `00`/`0i` constrainty a 13 projektovaných RHS na štyroch plochách.
- NID koeficientový floor: odstránený tvrdo viazaným 80-dps solve bez uvoľnenia tolerancií.
- Autoritatívny konečný skript: `scripts/176_script_A2_K4_C7_7c_K7b_final_four_surface_gate.py`.

## Otvorené

K7b bola iba koeficientová a počiatočná constraintová brána. Nevykonala ODE. Nasleduje **K7c — evolučná reprezentácia**:

1. `D,M` musia nahradiť presne dva druhové smery v invertibilnom 13-zložkovom stave;
2. nesmú vzniknúť dva nové fyzikálne stupne voľnosti;
3. prvý beh bude krátky, segmentovaný a časovo obmedzený;
4. pozdĺž trajektórie sa budú ukladať constrainty, aktivita, safety cap a checkpointy;
5. skóre sa nemení pred úplným K7d PASS.

## Zakázané skratky

- nepridať `D,M` ako 14. a 15. nezávislú premennú;
- nepoužiť HP register z referenčného `mu=0` solve pre fyzikálny background;
- nezmeniť fyzikálne kotvy na mäkké least-squares riadky;
- neuvoľniť activity ani constraint prahy po výsledku.

Autoritatívny audit: `Audit/A2_K4_C7_7C_K7B_FINAL_FOUR_SURFACE_VERDICT_2026-07-15.md`.

