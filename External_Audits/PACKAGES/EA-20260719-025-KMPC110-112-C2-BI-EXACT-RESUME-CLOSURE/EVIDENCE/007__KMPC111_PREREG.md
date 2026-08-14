# KMPC-111 — exact resume order-reconstruction successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `1/10` po PF-111

## Dôvod nástupcu

KMPC-110 compile/help prešli, ale smoke sa zastavil pred fyzikou na
`KMPC-106 serialized M1 order mismatch`. Checkpoint KMPC-108 bol publikovaný
cez JSON `sort_keys=True`, takže poradie kľúčov načítaného objektu nie je
poradím fyzikálneho registra. Autoritatívne poradie je osobitne uložené a
zahrnuté do vnútorného fingerprintu v poliach `m1_state_order` a
`fuel_state_order`.

## Jediná dovolená oprava

V18 smie pred delegovaním byteovo nezmeneného V17:

1. vyžadovať `m1_state_order == tuple(STATE_TO_LEGACY)` a
   `fuel_state_order == (delta_f, U_f)`;
2. vyžadovať presnú zhodu množiny serializovaných kľúčov s order zoznamami;
3. zostaviť nové insertion-ordered mapy presne podľa týchto zoznamov;
4. použiť pôvodné V13 decimal90/`float.hex()` deserializéry a round-trip;
5. dočasne prekryť iba V17 restore funkciu a v `finally` obnoviť jej
   pôvodného vlastníka.

Rovnice, checkpointové hodnoty, 80-dps exact driver, non-fit holdout,
support `[0,7]`, prahy, runtime a zmrazené rozhodovanie KMPC-110 sa nemenia.

## Zmrazené rozhodovanie

Po technicky úplnom resume platí pôvodný KMPC-110 kontrakt:

- exact driver nad `1e-10` dá
  `REVIEW_C2_BI_K0p15_HP_M1_EXACT_DRIVER_UNCLOSED`;
- exact independent holdout nad `1e-9` dá
  `REVIEW_C2_BI_K0p15_HP_M1_EXACT_NONFIT_HOLDOUT_UNCLOSED`;
- oba PASS spolu so všetkými checkpoint/parity/capture bránami dovoľujú iba
  candidate
  `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY`;
- technická SHA/order/parity/owner chyba nevydáva fyzikálny payload ani STOP.

Autoritatívna zmena C2 je zakázaná pred samostatným interným auditom.

## Scope a limity

- vstupy: KMPC-108 raw SHA `683D867D...9D995`, KMPC-109 receipt SHA
  `21EF9A9B...28118F9`, serialized-state SHA `402B42E1...5EBF40`;
- natívny CPQR a accepted `[0,5]` solve sa neopakujú;
- driver `1e-10`, holdout `1e-9`, ostatné prahy nezmenené;
- runtime presne `45.0 s`; vonkajší shell limit musí mať rezervu najmenej
  do `120 s`;
- `[0,9]`, iné mode/k atómy, S-M, ODE, P5.4, G8/G9 a dáta sú zakázané.

## Zmrazená implementácia pred prvým Python behom

- immutable V17 SHA:
  `1EC7DF765617A978940105129D74F02C1419B726CC023977F4DB426DDA5A33C4`;
- V18 order successor SHA:
  `3E30375748130FC69D51C2715D6521D3E1637E8F4C548E5605DCD3AB086AB492`;
- immutable runner 354 SHA:
  `DA271E7FBF7EF6243C9B66A5DAE2875056166674ABAD2E145328309627E28454`;
- runner 355 SHA:
  `10656FF16FEBA7A4AD48A1EF1EF01733659DCAA46C0FC8FAC1643D3F6016422E`;
- literal ancestor runner 346 SHA:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- výsledný contract: `47` source a `20` prerequisite položiek;
- harness SHA:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

Pred vytvorením tejto predregistrácie nebol V18 ani runner 355 spustený cez
Python. Od tohto bodu sú V18 a runner 355 immutable.
