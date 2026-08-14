# Scope — KMPC-103…109 HP-M1 support checkpoint

- Package ID: `EA-20260719-024-KMPC103-109-C2-BI-HP-M1-SUPPORT-CHECKPOINT`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Vytvára KMPC-108 z natívneho 80-dps HP-M1 riešenia lossless, hashovo
overiteľný checkpoint po accepted `[0,5]` a audit `[0,7]` F0/M3? Potvrdzuje
KMPC-109 bez opakovania solve jeho file SHA, vnútorný register SHA,
autoritatívne poradie 13 stavov, decimal90/float-hex round-trip a presnú
false množinu? Je jedinou otvorenou vecnou bránou checkpointu float64
`M3_driver` na `tight_coupling[7]`, takže samostatný exact resume je dovolený
bez udelenia C2 PASS alebo STOP?

## Poradie čítania

1. Evidence 001–004: auditný protokol, C2 kontrakt a upstream atribúcia.
2. Evidence 040–048: predchádzajúci native HP-M1 CPQR boundary.
3. Evidence 049–055: predregistrácie KMPC-103…109.
4. Evidence 057–060: dve technické failure raw, checkpoint a receipt raw.
5. Evidence 061–073: runnery a V11–V16 implementácie.
6. Evidence 056 a 013–016/074–076: interný audit, error/DNR/route registre a živý stav.
7. Dokument 03 a dve izolované fresh-copy reprodukcie.

## Nonclaims

- Balík neudeľuje BI/k=.15 ani C2 PASS a nevydáva fyzikálny STOP.
- Float64 `M3_driver` REVIEW sa nepovažuje za uzavretý; rozhodne ho až nový
  exact-driver/non-fit-holdout resume, ktorý nie je súčasťou balíka.
- Receipt KMPC-109 nevykonáva rovnice ani solve.
- KMPC-108 nepreukazuje `[0,9]`, iný mode/k atóm, S-M, ODE, P5.4, G8/G9
  ani zhodu s dátami.
- PF-107…PF-110 sú technické lifecycle udalosti, nie fyzikálne pokusy.
- C2 zostáva `5/10`, P5 `3.5/6` a K4 `LIVE / 60/100`.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje:

- source/copy a runtime paritu;
- fresh KMPC-108 compile/help/smoke/official exit 0 s dostatočnou vonkajšou
  rezervou a field-level paritu okrem `runtime_seconds`;
- exact raw false množinu
  `{audit_support_complete, pre_exact_core_complete}` a audit false množinu
  `{M3_driver}`;
- M1, accepted, audit F0, M3 rank/production contract/holdout,
  common/tail/S-C0/background PASS;
- checkpoint file SHA a recomputed serialized-state SHA zhodné;
- presne šesť deklarovaných lossless `mpf` konverzií;
- fresh KMPC-109 compile/help/smoke/official exit 0 a field-level paritu okrem
  `runtime_seconds`;
- explicitné `pass_c2_atom_candidate=false` v oboch raw.

Iný výsledok je `REVIEW_REPRODUCTION_MISMATCH`, nie fyzikálny verdikt.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
