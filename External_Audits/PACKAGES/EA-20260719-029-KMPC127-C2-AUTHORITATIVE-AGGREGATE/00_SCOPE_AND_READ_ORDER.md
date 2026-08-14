# Scope — KMPC-127 C2 authoritative atom aggregate

- Package ID: `EA-20260719-029-KMPC127-C2-AUTHORITATIVE-AGGREGATE`
- Theory author: **Martin Jambor**
- Script creator/internal auditor: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`

## Presná otázka

Overí read-only KMPC-127 bez fyzikálneho solve presne desať frozen
mode×k rawov cez exact SHA/identity/candidate/brány, exact kartézsky register
a cross-mode/cross-k background spread `<=1e-12`? Oprávňuje reprodukcia
scoped C2 aggregate PASS, odblokovanie C3 a zároveň nulovú zmenu K4 skóre?

## Poradie čítania

1. Evidence 001–002: balíkový protokol a pôvodný frozen C2 kontrakt.
2. Evidence 003–005: KMPC-127 predregistrácia, raw a interný audit.
3. Evidence 006–011: živý stav a technické registre.
4. Evidence 012–013: jediný runner a read-only base.
5. Evidence 014–023: presných desať immutable vstupných rawov.
6. Dokument 03: nezávislá negatívna a success reprodukcia.

## Nonclaims

- Balík znovu nerieši ani neauditue rovnice jednotlivých C2 atómov.
- PASS iba uzatvára C2 register a odblokuje C3.
- K4 ostáva `LIVE / 60/100`; P5 ostáva `3.5/6`.
- Bez C3 `gamma0/af0`, S-M, P5.4, G8/G9, dát a A3.
- Nejde o nezávislú T3 implementáciu ani validáciu teórie dátami.

## Predregistrované hodnotenie balíka

`PASS_PACKAGE_CLAIM` vyžaduje:

- úplnú source/copy a runtime hash paritu;
- negatívnu fresh-copy vetvu bez KMPC-126: exit `2`, bez outputu;
- fresh-copy compile base/runner, help a smoke: všetko exit `0`;
- fresh-copy official: exit `0`;
- field-level paritu generated/raw Evidence 004 po odstránení iba
  `runtime_seconds`;
- exact register `10/10`, všetky brány true, technical failures `0`;
- všetkých osem spreadov `<=1e-12`, maximum
  `4.60781186570449e-16`;
- explicitné `read_only_no_physics_solve=true`, score effect `NONE`.

Iný výsledok je `REVIEW_REPRODUCTION_MISMATCH`, nie fyzikálny STOP.

## Autorita

Externý auditor vydáva nezávislé read-only odporúčanie. Autoritatívny
PASS/REVIEW/STOP zapisuje iba hlavný projektový orchestrátor.
