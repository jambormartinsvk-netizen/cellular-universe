# L2-B2.1 — predregistrácia: presný source-equation audit BR2 (89/90)

**Stav pred behom:** `PRIPRAVENÉ`  
**Skript:** `scripts/240_script_lineage_L2_B2_1_BR2_equation_contract_audit.py`  
**Vnútorný limit / vonkajší limit:** 5 s / 10 s  
**Metóda:** AST parse + whitespace-invariantné porovnanie predregistrovaných RHS fragmentov. Bez importu modelu a bez ODE.

## Otázka

Sú 89 a 90 naozaj implementáciou povinného skorého K4 energy-frame jadra,
alebo iba obsahujú jeho názvy?

## Povinné identitné fragmenty

Pre každý zo skriptov musí zdroj obsahovať tieto ekvivalentné vzťahy:

1. `g=lambda/E`, `beta=delta X_f/(X_c+delta X_f)`, `U_d=(1-beta)U_c+beta U_f`.
2. `delta_c,x=-s² U_c-h_x/2+g r(delta_f-delta_c)`.
3. `U_c,x=(h_c-1)U_c+g r beta(U_f-U_c)`.
4. `U_f,x=(h_c+2)U_f+delta_f/delta+(g/delta)(2U_f-U_d)`.
5. `0i` hybnosť obsahuje `X_c U_c + delta X_f U_f + X_b U_b`.
6. `k` vstupuje cez `args.k_mpc`, nie cez pevné `K_MPC=0.05` backgroundové priradenie.

## Očakávania a rozsah PASS

Očakáva sa PASS oboch zdrojov. PASS znamená iba prítomnosť týchto
interakčných rovníc, hybnosti a roly módu. Neoveruje plnú palivovú
kontinuitu, gauge transformáciu, všetky Einsteinove constrainty, plnú
hierarchiu, numerickú konvergenciu ani limit `lambda→0`.

## STOP a ďalší krok

Chýbajúci fragment alebo opačné znamienko je STOP implementácie 89/90,
nie automatická smrť A2-K4. Pri PASS bude 90 iba porovnávacím historickým
ledgerom pre P5.2; pri STOP sa najprv vydá rozdielový ledger.
