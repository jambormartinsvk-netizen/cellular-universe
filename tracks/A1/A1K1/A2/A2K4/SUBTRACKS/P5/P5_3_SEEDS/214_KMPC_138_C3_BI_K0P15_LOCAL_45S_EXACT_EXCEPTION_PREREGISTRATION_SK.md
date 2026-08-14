# KMPC-138 — C3 BI/.15 lokálna 45-s exact výnimka

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3 → BI/.15`  
**Stav:** `PREREGISTERED / SOURCE_HASH_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Autorita výnimky:** používateľ výslovne zvolil „Najprv daj 45 sec“  
**Východisko:** interný audit 213, EA-033, PF-123  
**K4 pred behom:** `60/100`

## 1. Jediná povolená zmena

KMPC-138 používa byteovo nezmenený KMPC-137 fuel-order wrapper a jeho
KMPC-136 two-wave base. Mení iba process runtime contract:

- štyri binary64 coefficient workery ostávajú `≤4.8 s`;
- dva distinct audit-only 80-dps exact workery bežia paralelne a každý má
  lokálny limit `≤45.0 s`;
- parent má `≤49.0 s`, aby pokryl coefficient vlnu, dve paralelné exact
  vetvy, merge a immutable publish;
- vonkajší official proces má `≤50 s`.

Výnimka platí iba pre `BI/k=.15/gamma0+af0` exact boundary. Nie je novým
globálnym Python limitom a neprenáša sa na iný mód, k ani budúci runner.

## 2. Dôvod hodnoty 45 s

Autoritatívny KMPC-112 použil rovnaký frozen exact mechanizmus:

- `runtime_limit_seconds=45.0`;
- `runtime_seconds=34.86000000000058`;
- exact driver a independent holdout PASS.

Hodnota `45 s` preto nie je post-hoc odhad podľa KMPC-137. Je prevzatá z
existujúceho úspešného, hash-bound autoritatívneho precedensu.

## 3. Nemenný vedecký kontrakt

- identita `BI`, `K_MPC=0.15`, `gamma0` a `af0`;
- accepted `[0,5]`, audit `[0,7]`, M1 depth `7`;
- checkpoint/receipt/fingerprint KMPC-108/109;
- binary64 coefficient solve a pôvodný decimal80 HP-M1 exact handoff;
- exact matrix `104×104`, holdout `16×104`, precision `80 dps`;
- presne jeden exact driver solve na variant, holdout rows added `0`;
- všetky rovnice, matrix entries, RHS, `rcond`, supporty a fyzikálne prahy;
- supersession iba `M3_driver` a
  `M3_independent_00_0i_holdout` v audit sharde;
- temporary handoff hashe, explicitné fuel owner poradie a parent-only
  source-hash register;
- jeden immutable pair raw alebo jeden technical-failure receipt.

Frozen KMPC-137 wrapper SHA-256:
`489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D`.

## 4. Povinný preflight a hodnotenie

Procesy sa spustia oddelene: compile, help, šesť-rolový smoke a official.
Smoke nesmie vykonať fyziku.

- `4/4` coefficient + `2/2` exact, všetky fyzikálne brány PASS:
  `PASS_C3_BI_K0P15_ZERO_PAIR_LOCAL_45S_HP_M1_EXACT_RESUME_CANDIDATE_ONLY`;
- exact driver alebo holdout ostane nad frozen prahom:
  `REVIEW_C3_BI_K0P15_HP_M1_EXACT_BOUNDARY_UNCLOSED`;
- iná fyzikálna brána fail: jej existujúci C3 REVIEW/STOP kandidát;
- worker `>45 s`, parent `>49 s`, hash/order/schema chyba:
  `TECHNICAL_FAILURE_NO_PHYSICS_VERDICT`.

BI mód možno uzavrieť až následným interným auditom. K4 score sa nemení
samotným spustením.

## 5. R5 rozpočet

Najviac štyri nové live artefakty: táto predregistrácia, jeden identity a
runtime-only runner, jeden raw a jeden interný audit. Nový base nevzniká.
Externý balík sa vytvorí až po ucelenom BI mode closure alebo novom
významnom blockeri.

## 6. Source freeze

| artefakt | SHA-256 |
|---|---|
| frozen KMPC-137 wrapper | `489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D` |
| runner 382 | `15D28432CBB6C0C69E5FE1D9E9DC1848A7DFB0CAF6FC2B8970E0678C95019591` |
