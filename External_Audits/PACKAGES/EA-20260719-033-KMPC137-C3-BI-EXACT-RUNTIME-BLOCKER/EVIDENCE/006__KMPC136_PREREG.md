# KMPC-136 — C3 BI/.15 dvojvlnový exact resume

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Technický predchodca:** KMPC-135 / PF-121  
**Fyzikálne východisko:** KMPC-131 BI/.15 `REVIEW`; K4 `60/100`.

## 1. Jediná zmena: procesná segmentácia

KMPC-135 potvrdil, že binary64 coefficient fáza funguje: úplný
`gamma0/accepted` shard prešiel za `1.656 s`. Pair nevznikol, pretože dva
audit workery stále sériovo spájali coefficient solve s decimal80 exact
boundary a všetky štyri procesy súťažili v jednej vlne.

KMPC-136 zachová identickú matematiku a rozdelí beh na dve vlny:

1. štyri paralelné binary64 coefficient shardy
   `gamma0/af0 × accepted/audit`;
2. po ich úplnom PASS dve paralelné audit-only decimal80 exact-boundary
   shardy `gamma0/af0`.

Audit coefficient shard zachytí frozen float64 driver matrix/constant a
variantový fuel stav. Parent ich uloží iba do dočasného pracovného adresára.
Každý handoff nesie SHA-256; exact worker ho pred použitím overí. Dočasný
adresár sa odstráni pri úspechu aj chybe a nie je live ani auditným artefaktom.
Transitive source-hash register sa vypočíta raz v parent merge, nie znovu v
každom zo šiestich workerov; všetky publikované shardy dostanú tú istú mapu.

## 2. Zmrazený vedecký kontrakt

- iba `BI`, `K_MPC=0.15`, `gamma0` a `af0`;
- accepted `[0,5]`, audit `[0,7]`, M1 depth `7`;
- checkpoint/receipt/fingerprint KMPC-108/109 bez zmeny;
- ordinary solve používa iba explicitnú binary64 projekciu HP-M1;
- exact worker obnoví pôvodný decimal80 HP-M1, pridá iba coefficient workerom
  vypočítaný variantový fuel a zostaví tú istú audit maticu `104×104`;
- prenesená float64 matrix/constant slúži iba na assembly-difference
  provenance, nie ako exact fit vstup;
- 80 dps, rovnice, rows, RHS, `rcond`, thresholdy, supporty bez zmeny;
- exact supersession iba `M3_driver` a non-fit `Einstein_0i[7]` holdout;
- každý coefficient aj exact worker `≤4.8 s`, parent solve calls `0`, celý
  parent proces `≤9.0 s`, vonkajší proces `≤10 s`;
- jeden immutable pair raw alebo jeden immutable technical-failure receipt.

## 3. Povinné technické brány

- presne `4/4` coefficient shardy pred spustením exact vlny;
- presne `2/2` exact shardy;
- accepted shardy bez exact supersession;
- handoff identity, hash, driver shape `104×104`, capture count `1`;
- coefficient solve bez `mpf`; exact HP-M1 s `mpf`;
- variant fuel fingerprint pred/po handoff identický;
- exact driver solve count `1`, holdout rows added `0`;
- dočasný adresár odstránený pred publikovaním parent payloadu;
- source-hash register je parent-only, jednotný a prítomný vo finálnom raw;
- compile, help, behavior smoke a official sú oddelené procesy.

## 4. Predregistrované hodnotenie

- všetko vrátane oboch exact hraníc PASS:
  `PASS_C3_BI_K0P15_ZERO_PAIR_TWO_WAVE_HP_M1_EXACT_RESUME_CANDIDATE_ONLY`;
- exact driver/holdout ostane otvorený:
  `REVIEW_C3_BI_K0P15_HP_M1_EXACT_BOUNDARY_UNCLOSED`;
- iná fyzikálna brána fail: príslušný C3 REVIEW/STOP kandidát;
- timeout, handoff, hash alebo schema chyba: technická bez verdiktu.

BI mód možno uzavrieť až následným interným auditom. Externý auditný balík
sa vytvorí po mode closure alebo významnom novom blockeri.

## 5. Source freeze

Vyplní sa pred prvým Python procesom.

| artefakt | SHA-256 |
|---|---|
| nový KMPC-136 base | `3313C8861856289CFAC44B336B73D3AC4C7E153913DCFFFC3B1F3EFA6BA2802F` |
| runner 380 | `B44908ABD3BA1266DC22AA08AC02D53F3059A92D634A8361BC2C14BABFBF3E28` |
