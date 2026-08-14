# KMPC-137 — C3 BI/.15 frozen fuel-order roundtrip

**Dátum:** 2026-07-19  
**Route:** `A1-K1 → A2-K4 → P5.3g7 → C3`  
**Stav:** `PREREGISTERED / SOURCE_HASHES_FROZEN / READY_FOR_PREFLIGHT`  
**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)  
**Technický predchodca:** KMPC-136 / PF-122  
**Fyzikálne východisko:** KMPC-131 BI/.15 `REVIEW`; K4 `60/100`.

## 1. Jediná povolená oprava

KMPC-136 úspešne dokončil všetky štyri binary64 coefficient shardy za
`1.188–1.625 s`. Oba exact workery zastali ešte pred exact boundary, pretože
JSON roundtrip s canonical `sort_keys=true` zmenil poradie fuel ownerov z
frozen `delta_f, U_f` na abecedné `U_f, delta_f`.

KMPC-137 bude tenký wrapper nad byteovo nezmeneným KMPC-136 base. Pred volaním
frozen `_merge_m1_and_fuel` obnoví fuel mapu výlučne podľa explicitného
kontraktu `("delta_f", "U_f")`. Hodnoty, mocninové kľúče a fingerprint sa
nesmú zmeniť. Wrapper po každom volaní obnoví pôvodného vlastníka funkcie.

## 2. Nemenný kontrakt

- identita `BI/0.15`, supporty `[0,5]` a `[0,7]`, M1 depth `7`;
- dve vlny `4 coefficient + 2 exact` a dočasné hashované handoffy;
- KMPC-136 base a všetky transitive vedecké zdroje byteovo nezmenené;
- decimal80 HP-M1, binary64 coefficient state, exact `104×104` matrix,
  80 dps, rovnice, RHS, `rcond`, thresholdy a supersession scope bez zmeny;
- worker `≤4.8 s`, parent `≤9.0 s`, vonkajší proces `≤10 s`;
- jeden immutable pair raw alebo technical-failure receipt.

## 3. Nové povinné smoke a official brány

- JSON-roundtrip fixture musí reálne vytvoriť poradie `U_f, delta_f`;
- adapter ho musí obnoviť na presne `delta_f, U_f`;
- value fingerprint pred/po reorder musí byť identický;
- merge owner musí byť po volaní obnovený;
- všetky pôvodné KMPC-136 šesť-rolové brány ostávajú povinné.

## 4. Predregistrované hodnotenie

- úplný PASS:
  `PASS_C3_BI_K0P15_ZERO_PAIR_FUEL_ORDERED_TWO_WAVE_HP_M1_EXACT_RESUME_CANDIDATE_ONLY`;
- exact driver/holdout ostane otvorený:
  `REVIEW_C3_BI_K0P15_HP_M1_EXACT_BOUNDARY_UNCLOSED`;
- order/hash/schema/timeout chyba: technická bez verdiktu.

BI mód sa uzavrie až interným auditom. Auditný balík vznikne po uzavretí
módu alebo pri významnom novom blockeri.

## 5. Source freeze

Vyplní sa pred prvým Python procesom.

| artefakt | SHA-256 |
|---|---|
| frozen KMPC-136 base | `3313C8861856289CFAC44B336B73D3AC4C7E153913DCFFFC3B1F3EFA6BA2802F` |
| nový KMPC-137 thin wrapper | `489ED57D2F874CAC60E7733050C7DB4E8D59AABAD197827965F6322B80515D0D` |
| runner 381 | `D8117F3F79A8614E42F8176BA15F63421235ABA65F698B7D72557C48D04FA85C` |
