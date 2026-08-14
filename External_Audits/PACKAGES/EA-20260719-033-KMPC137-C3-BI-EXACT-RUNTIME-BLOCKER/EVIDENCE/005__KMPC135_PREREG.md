# KMPC-135 — C3 BI/.15 fázovo oddelený HP-M1 exact resume

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Technický predchodca:** KMPC-134 / PF-120  
**Fyzikálne východisko:** KMPC-131 BI/.15 `REVIEW`; K4 ostáva `60/100`.

## 1. Dôvod jediného technického nástupcu

KMPC-134 prešiel compile/help/smoke, ale všetky štyri official workery
timeoutli. Decimal80 `mpf` checkpointový M1 register omylom vstúpil aj do
obyčajného coefficient solve, ktorý má reprodukovať binary64 C3 referenciu.
Nevznikol úplný fyzikálny shard ani nový verdikt.

KMPC-135 smie opraviť iba reprezentáciu podľa fázy:

1. obnovený HP-M1 sa lossless overí vo frozen poradí;
2. jeho explicitná binary64 projekcia sa použije pre accepted/audit
   variantové F0/M3 coefficient solves a všetky bežné C3 brány;
3. pôvodný decimal80 HP-M1 sa použije až pri auditnom exact driver/holdout
   zostavení spolu s nanovo vypočítaným variantovým fuel stavom.

## 2. Čo sa nesmie zmeniť

- iba `BI`, `K_MPC=0.15`, varianty `gamma0` a `af0`;
- accepted support `[0,5]`, audit support `[0,7]`, M1 depth `7`;
- štyri shardy `variant × accepted/audit`;
- checkpoint, receipt a serialized-state fingerprint KMPC-108/109;
- rovnice, matice, RHS, `rcond`, thresholdy a 80-dps exact boundary;
- exact supersession iba `M3_driver` a
  `M3_independent_00_0i_holdout` v audit sharde;
- každý worker `≤4.8 s`, parent solve calls `0`, vonkajší limit `≤10 s`;
- jeden nový immutable pair raw alebo jeden technical-failure receipt.

## 3. Predregistrované brány

Okrem KMPC-134 brán musí provenance explicitne potvrdiť:

- `coefficient_solve_uses_binary64_projection=true`;
- `exact_boundary_uses_original_decimal80_HP_M1=true`;
- accepted shardy nemajú exact supersession;
- audit float capture ostáva `104×104` a exact driver solve count je `1`;
- binary64 projekcia je odvodená výlučne z overeného checkpointového stavu.

## 4. Predregistrované hodnotenie

- všetky štyri shardy a pair brány PASS:
  `PASS_C3_BI_K0P15_ZERO_PAIR_PHASE_SEPARATED_HP_M1_EXACT_RESUME_CANDIDATE_ONLY`;
- exact driver/holdout ostane otvorený:
  `REVIEW_C3_BI_K0P15_HP_M1_EXACT_BOUNDARY_UNCLOSED`;
- iná fyzikálna brána fail: príslušný C3 REVIEW/STOP kandidát;
- hash, schema, timeout alebo representation-contract chyba: technická bez
  fyzikálneho verdiktu.

BI mód možno uzavrieť až samostatným interným auditom. Externý balík sa
vyrobí až po uzavretí módu alebo pri novom významnom blockeri, nie po každom
pomocnom behu.

## 5. Source freeze

Vyplní sa pred prvým Python procesom.

| artefakt | SHA-256 |
|---|---|
| nový KMPC-135 base | `64662CC4C1EFFB607E786D060B03DD26CD10FA90DDF7DD6E5226BAA7588C5841` |
| runner 379 | `837E5CBEEE48DD67E6D1C457034DF9E0BABC19D9E909BF29D831CDDA93486B48` |
