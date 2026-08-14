# Scope — KMPC-067–075 C2 CDI mode closure

- Package ID: `EA-20260719-016-KMPC067-075-C2-CDI-MODE-CLOSURE`
- Theory author: **Martin Jambor**
- Script creator: **Codex (OpenAI)**
- Package state: `SEALED_READY_FOR_EXTERNAL_AUDIT`
- Target tier: `T2_REPRODUCIBLE_CALCULATION`
- Autorita: externý auditor odporúča; projektový verdict nemení

## Presná otázka

Reprodukujú oficiálne runnery 317 a 319 pri nezmenených prahoch PASS oboch
CDI C2 k-bodov, teda CDI/k=.005 accepted `[0,7]` voči `[0,9]` a CDI/k=.15
accepted `[0,5]` voči `[0,7]`, vrátane checkpoint integrity, 13-state order
a same-matrix refinement provenance, takže projekt smie viesť C2 ako
`4/10 PASS`?

## Predregistrované kritérium

- PASS v scope: oba generated raw majú exact kandidáty KMPC-073/KMPC-075,
  M1/core/common/tail/background PASS, source a prerequisite hashe sedia;
- REVIEW: oficiálna vetva dobehne, ale niektorá zmrazená brána alebo exact
  reference parity neprejde;
- TECHNICAL_STOP: import/runtime/hash/publish chyba bez fyzikálneho hlasu;
- COMPUTED_STOP_SCOPE sa z tohto balíka neudeľuje.

## Poradie čítania

1. Evidence 001–002: protokol a frozen C2 strom.
2. Evidence 003–014: predregistrácie a výsledkové uzávery oboch k-bodov.
3. Evidence 015–016: PF-081 až PF-084 a `DO_NOT_RUN` stav.
4. Evidence 017–024: immutable raw/failure/checkpoint referencia.
5. Evidence 025–036: finálne runnery, technická lineage a výpočtové obaly.
6. `03_REPRODUCTION_AND_EXPECTATIONS.md`, potom fresh-copy reprodukcia.

## Nonclaims

Nie T3, nie celý C2/P5.3/P5/K4 PASS, nie ODE, P5.4, hierarchy, G8/G9,
likelihood, dáta ani release trigger. Checkpoint KMPC-070 nemá fyzikálny
verdikt. KMPC-071 je `DO_NOT_USE_PHYSICS`; KMPC-068/069/072 nemajú
fyzikálny raw. Skóre K4 ostáva `60/100`.
