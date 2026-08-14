# KMPC-070/071 — C2 CDI/k=.005 support [0,7]→[0,9]: checkpoint/resume

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Stav:** `KMPC-070 CHECKPOINT_COMPLETE / KMPC-071 PF-083 DO_NOT_USE_PHYSICS`  
**Nástupca:** PF-082 / KMPC-069 bez fyzikálneho raw  

Fyzika, support `[0,7]→[0,9]`, M1 depth 9, plochy, prahy a rozhodovací strom
ostávajú identické s KMPC-068/069. Jediná numerická zmena je rozdeliť ten
istý atóm na dva procesy s presným interným limitom `4.8 s` každý:

1. KMPC-070 vypočíta invariantné kontrakty, depth-9 M1 a accepted `[0,7]`
   solve. Zapíše immutable checkpoint bez fyzikálneho kandidáta alebo verdiktu.
2. KMPC-071 fail-closed overí SHA checkpointu, source chain, identitu, support,
   depth, prahy a prerequisite. Z checkpointu obnoví standard a accepted stav,
   vypočíta audit `[0,9]`, common/tail/S-C0/background brány a až potom smie
   publikovať výsledkový candidate.

Obe fázy používajú single-thread backend. Checkpoint nesmie meniť koeficienty,
zaokrúhľovať ich na kratší zápis ani zameniť integer power keys; serializuje sa
plná Python float reprezentácia. Resume nesmie použiť checkpoint s iným hashom.

PASS candidate KMPC-071:
`PASS_C2_CDI_K0p005_SUPPORT_07_ADEQUATE_CANDIDATE_ONLY`. Tail-only FAIL
otvorí iba `[0,9]→[0,11]`. Bez agregácie, skóre alebo triggera.

Poradový fyzikálny prerequisite ostáva KMPC-067 SHA
`DC11201E7301831153F4D3D5450A95FC1D5F311E5EE3E9176BDE6E471F657F8F`.
Technické failure artefakty KMPC-068/069 nie sú fyzikálnym vstupom.

Plánované artefakty:

- base: `c2_checkpointed_single_atom.py`;
- runner 314 / checkpoint:
  `RUN_KMPC_070_P5_3G7_C2_CDI_K0p005_SUPPORT_07_ACCEPTED_CHECKPOINT.json`;
- runner 315 / final:
  `RUN_KMPC_071_P5_3G7_C2_CDI_K0p005_SUPPORT_07_09_CHECKPOINT_RESUME.json`.

Zmrazené pred prvým Python behom:

- base SHA-256:
  `76B707973FA285733AFF61A8A931A51D4C09D249D1F6CB983758C09F0F0D05CF`;
- runner 314 SHA-256:
  `32E299078A6B7E65A2723347F109321D1B09509FAE0953E8AEEF37E01977D899`;
- checkpoint KMPC-070 SHA-256:
  `AD8CD12F5E6CBABE28C512DFDA6D3867C3E713F5582E152F6289CD78540A7D00`;
- runner 315 SHA-256:
  `0C59F6BA91BE93369A19F55BFB766100E06F074780B8F7C7BC1A8E0016B90A1D`;
- harness SHA-256:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | dvojstupňová numerická delta a nezmenený fyzikálny kontrakt zmrazené | `PREREGISTERED` |
| 2026-07-19 | checkpoint base a runner 314 hashovo zmrazené; oba ciele neprítomné | `KMPC-070 FROZEN / NOT_RUN` |
| 2026-07-19 | KMPC-070 compile/help/smoke PASS; checkpoint complete 9/9, M1 a accepted PASS; runtime 2.61 s | `CHECKPOINT_IMMUTABLE_NO_VERDICT` |
| 2026-07-19 | checkpoint hash a runner 315 zmrazené; final cieľ neprítomný | `KMPC-071 FROZEN / NOT_RUN` |
| 2026-07-19 | KMPC-071 dokončil; jediný core false je state tuple order po JSON sort; raw SHA `B2A1F7D3...50DC5` | `PF-083 / DO_NOT_USE_PHYSICS` |
