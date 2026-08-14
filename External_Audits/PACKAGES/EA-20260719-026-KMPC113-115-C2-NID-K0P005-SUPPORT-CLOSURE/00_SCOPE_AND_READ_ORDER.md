# Scope — KMPC-113…115 NID/k=.005 support closure

- Package ID: `EA-20260719-026-KMPC113-115-C2-NID-K0P005-SUPPORT-CLOSURE`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Reprodukuje frozen nominal KMPC-113 pri NID/k=.005 tail-only REVIEW pre
accepted `[0,5]`, audit `[0,7]` bez core/common/background zlyhania? Vytvorí
KMPC-114 hashovaný verdict-free checkpoint accepted `[0,7]`, M1 depth 9 a
obnoví ho KMPC-115 pre audit `[0,9]`? Prejdú potom nezmenené prahy M1,
driver, independent `00/0i` holdout, common, tail, S-C0 a background tak,
že projektový scoped PASS NID/k=.005 a C2 `7/10` je auditne oprávnený?

## Poradie čítania

1. Evidence 001–002: package protokol a frozen C2 rozhodovací kontrakt.
2. Evidence 003, 005, 007: tri predregistrácie v poradí výpočtu.
3. Evidence 004, 006, 008: tri immutable raw výsledky.
4. Evidence 009: interný audit a autoritatívny scoped verdict.
5. Evidence 010–016: ordering prerequisite, technické registre a živé plány.
6. Evidence 017–041: runnery, checkpoint vrstvy, equation lineage a harness.
7. Dokument 03: negatívna kontrola a tri nezávislé fresh-copy reprodukcie.

## Nonclaims

- PASS platí iba pre `NID/k=.005/nominal`, accepted `[0,7]`, audit `[0,9]`.
- Nie je to dôkaz pre NID/k=.15, NIV, support `[0,11]`, S-M, ODE, P5.4,
  G8/G9, dáta ani prechod A2→A3.
- KMPC-114 je checkpoint bez fyzikálneho verdiktu; samostatne nezvyšuje C2.
- PF-113 je operátorská CLI udalosť pred fyzikou, nie fyzikálny výsledok.
- Checkpoint/resume je tá istá implementácia a rovnaký equation builder;
  balík je T2, nie nezávislá T3 implementácia.
- P5.3 ostáva čiastočný PASS a K4 ostáva `LIVE / 60/100`.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje:

- source/copy a runtime manifest paritu a negatívny missing-prerequisite
  guard pred fyzikou;
- fresh KMPC-113, KMPC-114 a KMPC-115 compile/help/smoke/official exit `0`
  v troch nezávislých vetvách s pôvodným hashovaným predchodcom a bez
  obídenia runner guardov;
- field-level paritu každého generated raw s Evidence 004/006/008 po
  odrátaní iba polí pomenovaných `runtime_seconds` a po normalizácii iba
  absolútneho root prefixu poľa
  `frozen_B1_left_null_Bianchi.frozen_algebra_source`; relatívny suffix
  `scripts/baseScripts/p5_general_synchronous/full_ra_b1_preflight.py`
  musí zostať presne rovnaký;
- KMPC-113 false množinu iba v tail vetve a candidate presne
  `REVIEW_C2_NID_K0p005_SUPPORT_07_09_REQUIRED`;
- KMPC-114 execution status
  `TECHNICAL_CHECKPOINT_COMPLETE_NO_PHYSICS_VERDICT`, 9/9 checkpoint
  preconditions a SHA-bound resume;
- KMPC-115 všetky physics/technical brány true, 13-state order PASS,
  driver/holdout/common/tail/background pod zmrazenými prahmi a candidate
  `PASS_C2_NID_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`.

Iný výsledok je `REVIEW_REPRODUCTION_MISMATCH`, nie fyzikálny STOP.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP môže zapísať iba hlavný projektový orchestrátor.
