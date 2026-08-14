# KMPC-075 — C2 CDI/k=.15 same-matrix M3 refinement: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Predchodca:** KMPC-074 SHA
`7771610FC77C2F3AA3FD9EA7D9BDE01F9C9D8F6751AC5BCD1075E67B9FBBB1A0`

Jediný povolený numerický zásah sa aplikuje iba na auditnú M3 maticu
`104×104` pre `CDI/k=.15`, support `[0,7]`. Pôvodný equilibrated SVD/lstsq
solution sa zachová ako baseline. Na tej istej row/column equilibrated matici
sa vykonajú presne tri korekčné kroky `A δ = -r` cez `numpy.linalg.solve`;
po každom sa exportujú rovnaké autoritatívne row-residual metriky.

Za refined solution sa vyberie iba konečný finite krok, ktorý
nezhorší absolútne fallback rezíduum a zníži maximálne relatívne rezíduum.
Prahy sa nemenia: driver `1e-10`, absolute fallback `1e-12`. Rank, rcond,
rovnice, pravá strana, stavový/riadkový register, `[0,5]→[0,7]`, M1 depth 7,
common/tail prahy, plochy a vetvenie ostávajú identické s KMPC-074.

Backend sa pred importom zmrazí na jedno vlákno. Smoke musí overiť syntetický
same-matrix correction fixture, presné zacielenie iba `expected_rank=104`,
source hash chain a obnovu solver ownera.

PASS candidate ostáva
`PASS_C2_CDI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`. Ak refined audit M3
driver ostane nad `1e-10` alebo sa zhorší iná core brána, CDI mód zostáva
`REVIEW_CORE_GATE_UNCLOSED` a vznikne blocker vhodný na externý audit; prah
sa neupraví.

Artefakty: `c2_cdi_k0p15_same_matrix_refinement.py`, runner 319 a raw
`RUN_KMPC_075_P5_3G7_C2_CDI_K0p15_SAME_MATRIX_REFINEMENT.json`.

Zmrazené SHA-256:

- refinement base:
  `EA589E4CBAD3AD618DEBC41C81B271EAC23F229AEA82C80E962CD792091468F6`;
- runner 319:
  `7E8281C8C7ECF3A76C8A15F37E14CDB673FB66BADF485DE00517DAE9DB4E5F8E`;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | matica, tri korekcie, selection rule, prahy a vetvenie zmrazené | `PREREGISTERED` |
| 2026-07-19 | base, runner a source chain hashovo zmrazené; cieľ neprítomný | `FROZEN / NOT_RUN` |
