# Scope — KMPC-087 BI high-precision driver assembly

- Package ID: `EA-20260719-020-KMPC087-C2-BI-HP-DRIVER-ASSEMBLY`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Reprodukuje KMPC-087 high-precision zostavenie a solve tej istej 104x104
driver sústavy, pričom driver prejde na `8.720279045e-82`, ale nezávislý
`Einstein_0i[7]` zostane `3.0197565776e-9 > 1e-9`? Podporuje differential
voči KMPC-083/086 záver, že solve, holdout assembly ani driver assembly
roundoff nevysvetľujú hranicu a ďalší audit má smerovať na upstream
M1/F0/background koeficienty?

## Poradie čítania

1. Evidence 001–003: protokol, C2 kontrakt a východisko KMPC-083.
2. Evidence 004–018: holdout-assembly lineage, error/DNR registre, raw a plán.
3. Evidence 019–023: KMPC-087 predregistrácia, interný audit, raw, runner a
   high-precision driver modul.
4. Dokument 03 a fresh-copy reprodukcia runnera 331.

## Nonclaims

- Nie je to fyzikálny STOP ani dôkaz nesprávnej rovnice.
- Nie je to high-precision nové odvodenie upstream M1, F0 alebo backgroundu;
  ich binary64 hodnoty sú iba presne prenesené do 80-dps aritmetiky.
- Nie je to BI/k=.15 PASS, celý BI mód PASS ani celý C2/P5.3/P5/K4 PASS.
- Holdout sa nesmie pridať do driver solve.
- K4 ostáva `60/100`, C2 ostáva `5/10`.

## Predregistrované hodnotenie

`PASS_PACKAGE_CLAIM` vyžaduje 104x104 exact-driver fingerprint, presne dva
HP solve celkom, nulový počet holdout riadkov vo fite, driver PASS, holdout
FAIL nad nezmeneným prahom a reprodukovaný differential voči KMPC-086.
Odchýlka je `REVIEW_REPRODUCTION_MISMATCH`, nie automatický fyzikálny verdikt.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
