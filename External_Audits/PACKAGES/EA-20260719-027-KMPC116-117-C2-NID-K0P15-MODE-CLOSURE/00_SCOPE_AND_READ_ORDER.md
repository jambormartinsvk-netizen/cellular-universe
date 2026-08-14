# Scope — KMPC-116…117 NID/k=.15 a uzavretie NID módu

- Package ID: `EA-20260719-027-KMPC116-117-C2-NID-K0P15-MODE-CLOSURE`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Reprodukuje frozen nominal KMPC-116 pri NID/k=.15 jedinú core hranicu
`M3_driver`, pričom M1, accepted solve, independent holdout, common, tail,
S-C0 a background prejdú? Použije KMPC-117 presne tú istú 104×104 maticu
a pravú stranu, tri predregistrované residual corrections bez pridania
holdoutu do fitu, a uzavrie všetky zmrazené brány tak, že scoped PASS pre
NID/k=.15, celý NID mód a C2 `8/10` sú auditne oprávnené?

## Poradie čítania

1. Evidence 001–002: package protokol a frozen C2 rozhodovací kontrakt.
2. Evidence 003 a 005: predregistrácie v poradí výpočtu.
3. Evidence 004 a 006: immutable raw výsledky.
4. Evidence 007: interný audit a autoritatívny scoped verdict.
5. Evidence 008–014: ordering prerequisite, technické registre a plány.
6. Evidence 015–042: runnery, same-matrix vrstva, equation lineage a harness.
7. Dokument 03: negatívna kontrola a dve nezávislé fresh-copy reprodukcie.

## Nonclaims

- PASS platí iba pre `NID/k=.15/nominal`, accepted `[0,5]`, audit `[0,7]`.
- Spolu s predchádzajúcim NID/k=.005 PASS uzatvára iba NID mód C2.
- Nie je to dôkaz pre NIV, S-M, ODE/P5.4, G8/G9, dáta ani prechod A2→A3.
- KMPC-116 REVIEW je zachovaná numerická hranica, nie fyzikálny STOP.
- Same-matrix refinement nemení rovnice ani prahy a nie je nezávislá T3
  implementácia.
- P5.3 ostáva čiastočný PASS a K4 ostáva `LIVE / 60/100`.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje:

- source/copy a runtime manifest paritu a negatívny missing-prerequisite
  guard pred fyzikou;
- fresh KMPC-116 a KMPC-117 compile/help/smoke/official exit `0` v dvoch
  nezávislých vetvách s pôvodným hashovaným predchodcom;
- field-level paritu oboch generated rawov s Evidence 004/006 po odrátaní
  iba polí pomenovaných `runtime_seconds` a po normalizácii iba absolútneho
  root prefixu poľa `frozen_B1_left_null_Bianchi.frozen_algebra_source`;
- KMPC-116 false množinu presne `M3_driver`, worst
  `gamma_Euler[7]`, candidate `REVIEW_C2_CORE_GATE_UNCLOSED` a nezávislý
  holdout pod `1e-9`;
- KMPC-117 identitu `EXACT_SAME_MATRIX_AND_CONSTANT`, presne tri corrections,
  driver po refinement pod `1e-10`, independent holdout pod `1e-9`, všetky
  ostatné brány true a candidate
  `PASS_C2_NID_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`.

Iný výsledok je `REVIEW_REPRODUCTION_MISMATCH`, nie fyzikálny STOP.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
