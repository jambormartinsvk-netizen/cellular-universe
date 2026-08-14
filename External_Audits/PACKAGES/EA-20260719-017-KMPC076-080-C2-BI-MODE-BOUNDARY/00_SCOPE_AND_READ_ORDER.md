# Scope — KMPC-076–080 C2 BI mode boundary

- Package ID: `EA-20260719-017-KMPC076-080-C2-BI-MODE-BOUNDARY`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Otázka

Reprodukuje reťazec KMPC-076 až 080 BI/k=.005 PASS supportu `[0,7]` voči
`[0,9]` a pri BI/k=.15 izoluje po úspešnom same-matrix main-driver
refinemente jediný otvorený nezávislý `Einstein_0i[7]` holdout, takže C2
smie zostať `5/10 PASS` a ďalší krok je high-precision holdout boundary?

## Read order

1. Evidence 001–002: protokol a frozen C2 strom.
2. Evidence 003–010: predregistrácie a autoritatívne vyhodnotenia.
3. Evidence 011–015: immutable raw/checkpoint.
4. Evidence 016–023: runnery, oba výpočtové obaly a error ledger.
5. Dokument 03 a fresh-copy reprodukcia.

Nonclaims: nie celý BI mód PASS, nie celý C2/P5.3/P5/K4 PASS, nie fyzikálny
STOP. K4 ostáva `60/100`; release a Zenodo trigger sú `NONE`.
