# Scope — KMPC-081–083 BI high-precision holdout boundary

- Package ID: `EA-20260719-018-KMPC081-083-C2-BI-HP-HOLDOUT`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Auditná otázka

Reprodukuje KMPC-083 na presne float64-zostavenej 104×104 BI/k=.15 matici
80-dps driver PASS približne `9.82e-82`, ale nezávislý nefitovaný
`Einstein_0i[7]` holdout `3.019756782e-9 > 1e-9`, takže solve-roundoff je
vylúčený, C2 ostáva `5/10` a ďalší krok je exact-assembly audit?

## Poradie

1. Evidence 001–003: protokol, C2 kontrakt, interný audit.
2. Evidence 004–007: predregistrácie, PF vetvy a výsledok.
3. Evidence 008–011: error/DNR registre, failure a success raw.
4. Evidence 012–018: runnery, HP moduly, harness a aktuálny plán.
5. Dokument 03 a fresh-copy reprodukcia runnera 327.

Nonclaims: nie fyzikálny STOP, nie exact assembly, nie BI mód PASS, nie celý
C2/P5.3/P5/K4 PASS. K4 ostáva `60/100`.
