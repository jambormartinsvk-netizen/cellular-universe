# Scope — KMPC-110…112 BI/k=.15 exact-resume closure

- Package ID: `EA-20260719-025-KMPC110-112-C2-BI-EXACT-RESUME-CLOSURE`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Obnovuje KMPC-112 lossless KMPC-108/109 checkpoint v autoritatívnom poradí,
reprodukuje jeho audit `[0,7]` payload a fuel register a následne zostaví a
vyrieši presne jeden 104×104 M3 driver pri 80 dps? Prechádza pôvodnými
prahovými hodnotami driver `1e-10` aj nezávislý 16×104 non-fit holdout
`1e-9`, bez opakovania CPQR a bez pridania holdout riadkov do solve? Je preto
projektový scoped PASS `BI/k=.15/nominal`, C2 `6/10`, auditne oprávnený?

## Poradie čítania

1. Evidence 001–003: balíkový/C2 kontrakt a overený checkpointový vstup.
2. Evidence 006–009: predregistrácie KMPC-110–112 a interný audit výsledku.
3. Evidence 004–005, 017–018: checkpoint, receipt, technický failure a
   úspešný raw.
4. Evidence 019–030: runnery, restore/parity successory, exact driver a
   stabilné harnessy.
5. Evidence 010–016: error/DNR/route registre a autoritatívny živý stav.
6. Dokument 03 a izolovaná fresh-copy reprodukcia.

## Nonclaims

- PASS platí iba pre `BI/k=.15/nominal`, accepted `[0,5]` a audit `[0,7]`.
- Nie je to dôkaz pre `[0,9]`, NID/NIV, S-M, ODE, P5.4, G8/G9 ani dáta.
- F0 a background vstupy zostávajú presne bridged binary64; iba M1 a
  downstream driver/holdout assembly/solve majú deklarovaný 80-dps rozsah.
- PF-111/PF-112 sú technické udalosti bez fyzikálneho verdictu.
- KMPC-112 je T2 rovnakého equation buildera; nejde o nezávislú T3
  implementáciu.
- C2 je iba `6/10`, P5 `3.5/6` a K4 ostáva `LIVE / 60/100`.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje:

- source/copy a runtime manifest paritu a negatívny missing-prerequisite
  guard pred fyzikou;
- fresh KMPC-112 compile/help/smoke/official exit `0` bez obídenia guardov;
- field-level paritu generated raw s Evidence 018 po odrátaní iba všetkých
  polí `runtime_seconds`;
- presné checkpoint/receipt/state SHA a audit field/fuel paritu;
- pôvodnú audit false množinu presne `{M3_driver}` a všetky technical/
  physics checks `true`;
- jeden exact 104×104 solve, driver `<=1e-10`, 16×104 holdout `<=1e-9`,
  `rows_added_to_driver_solve=0` a bez opakovania CPQR;
- candidate presne
  `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY`.

Iný výsledok je `REVIEW_REPRODUCTION_MISMATCH`, nie fyzikálny STOP.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
