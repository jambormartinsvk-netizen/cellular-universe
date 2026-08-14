# Scope — KMPC-084–086 BI high-precision holdout assembly

- Package ID: `EA-20260719-019-KMPC084-086-C2-BI-HP-ASSEMBLY`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Reprodukuje KMPC-086 na driver matici identickej s KMPC-083 80-dps
znovuzostavenie všetkých 16 nezávislých holdout koeficientov, pričom
`Einstein_0i[7] = 3.0197567116259885e-9 > 1e-9`, a podporuje to záver,
že posledné float64 zostavenie/odčítanie holdoutu nie je príčinou a ďalší
krok musí auditovať high-precision zostavenie driver matice?

## Poradie čítania

1. Evidence 001–003: protokol, C2 kontrakt a východisko KMPC-083.
2. Evidence 004–007: predregistrácie, technické vetvy a interný audit.
3. Evidence 008–011: error/DNR registre a oba immutable raw výsledky.
4. Evidence 012–018: runnery, assembly vrstvy a aktuálny plán.
5. Dokument 03 a fresh-copy reprodukcia runnera 330.

## Nonclaims

- Nie je to fyzikálny STOP ani dôkaz zlej rovnice.
- Nie je to exact/high-precision assembly driver matice ani upstream M1/F0.
- Nie je to BI/k=.15 PASS, celý BI mód PASS ani celý C2/P5.3/P5/K4 PASS.
- PF-089 až PF-091 nemajú fyzikálny payload.
- K4 ostáva `60/100`, C2 ostáva `5/10`.

## Predregistrované hodnotenie

`PASS_PACKAGE_CLAIM` vyžaduje 16x104 HP holdout fingerprint, presne jeden
HP driver solve, nulový počet holdout riadkov vo fite, všetky ostatné brány
s HP replacementom PASS a reprodukovaný holdout FAIL nad nezmeneným prahom.
Odchýlka v týchto poliach je `REVIEW_REPRODUCTION_MISMATCH`, nie automatický
fyzikálny verdikt.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
