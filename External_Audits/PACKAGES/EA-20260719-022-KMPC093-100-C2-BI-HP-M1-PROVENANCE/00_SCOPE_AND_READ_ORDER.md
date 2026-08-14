# Scope — KMPC-093 až KMPC-100 HP-M1 matrix provenance

- Package ID: `EA-20260719-022-KMPC093-100-C2-BI-HP-M1-PROVENANCE`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION_WITH_DECLARED_POST_PUBLISH_EXIT`

## Presná otázka

Potvrdzuje standalone KMPC-099, že natívna 80-dps M1 assembly po binary64
projekcii a nezávislý frozen binary64 rebuild majú rovnaký plný stĺpcový
rank `98/98`, rovnaké spektrum/condition a iba roundoff-scale coefficient
rozdiely? Je preto predošlá `mpmath.qr_solve` výnimka lokalizovaná na
high-precision QR/algoritmickú hranicu namiesto projected ranku alebo M1
assembly? Overuje KMPC-100 tento raw read-only bez opakovania matice?

## Poradie čítania

1. Evidence 001–004: protokol, C2 kontrakt a KMPC-092 východisko.
2. Evidence 005–017: osem predregistrácií, technické registre, plán a interný audit.
3. Evidence 018–023: štyri failure raws, standalone raw KMPC-099 a receipt KMPC-100.
4. Evidence 024–039: runnery 337–344 a HP-M1 moduly V1–V8.
5. Dokument 03 a dve izolované fresh-copy reprodukcie runnerov 343 a 344.

## Nonclaims

- Nie je to BI/k=.15 PASS, fyzikálny STOP ani hotové HP-M1 riešenie.
- KMPC-099 reportuje rank natívnej assembly po binary64 projekcii; natívny
  80-dps rank-revealing audit je až ďalší krok.
- Binary64 bridge nie je autoritatívny HP solve a jeho driver/holdout polia
  nie sú fyzikálne brány.
- Receipt compatibility polia false znamenajú `NOT_EVALUATED_RECEIPT_ONLY`.
- C2 ostáva `5/10`, P5 `3.5/6` a K4 `LIVE / 60/100`.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje source/copy paritu, reprodukovaný raw KMPC-099
s exitom 2 až po immutable publish, field-level paritu okrem runtime,
reprodukovaný KMPC-100 s exitom 0 a exact SHA receiptu. Ranky musia byť
`98/98/98`, RHS exact equal, autoritatívny HP-M1 solve `0` a C2 candidate
false. Iná hodnota je `REVIEW_REPRODUCTION_MISMATCH`, nie fyzikálny verdikt.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
