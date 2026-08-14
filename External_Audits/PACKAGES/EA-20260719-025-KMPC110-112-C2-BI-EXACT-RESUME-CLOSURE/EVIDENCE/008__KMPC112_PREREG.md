# KMPC-112 — exact resume JSON-parity successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `2/10` po PF-112

## Dôvod nástupcu

KMPC-111 compile/help/smoke a checkpoint-order oprava prešli. Official sa
zastavil fail-closed iba na `audit_payload_field_parity`, pretože V17
porovnával živý Python payload s už publikovaným a znovu načítaným JSON
payloadom. Stabilný publisher mení kľúče dictov na stringy a tuple na listy;
taká typová zmena sama osebe nie je zmenou vedeckej hodnoty.

## Jediná dovolená oprava

V19 smie počas delegovania byteovo nezmenených V17/V18 dočasne nahradiť iba
reprezentačný adapter tak, aby pred parity porovnaním použil presne publish
kanonizáciu:

- `mpmath.mpf ->` lossless decimal90 string pôvodnou V15 metódou;
- každý mapping key `-> str(key)`;
- tuple/list `-> list`;
- numpy array/scalar `->` JSON builtin;
- non-finite hodnota a nepodporovaný scalar sú fail-closed.

Smoke musí samostatne overiť integer key, tuple, numpy scalar, decimal90 mpf
cestu a návrat vlastníka adaptera. Rovnice, vstupné hodnoty, restore order,
audit solve, exact driver, holdout, 80 dps, prahy a runtime sa nemenia.

## Zmrazené rozhodovanie

Rozhodovanie ostáva identické s KMPC-110/111:

- exact driver nad `1e-10` dá
  `REVIEW_C2_BI_K0p15_HP_M1_EXACT_DRIVER_UNCLOSED`;
- exact independent holdout nad `1e-9` dá
  `REVIEW_C2_BI_K0p15_HP_M1_EXACT_NONFIT_HOLDOUT_UNCLOSED`;
- oba PASS spolu so všetkými checkpoint/parity/capture bránami dovoľujú iba
  `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY`;
- technická chyba nevydáva fyzikálny verdikt ani STOP.

Autoritatívna zmena C2 je zakázaná pred samostatným interným auditom.

## Scope a limity

- KMPC-108 raw SHA `683D867D...9D995`, KMPC-109 receipt SHA
  `21EF9A9B...28118F9`, serialized-state SHA `402B42E1...5EBF40`;
- PF-112 failure SHA `1ADCB30A...BD95E40` je nový hashovaný prerequisite;
- natívny CPQR a accepted `[0,5]` solve sa neopakujú;
- driver `1e-10`, holdout `1e-9`, ostatné prahy nezmenené;
- runtime presne `45.0 s`, vonkajší shell limit najmenej `120 s`;
- `[0,9]`, iné mode/k atómy, S-M, ODE, P5.4, G8/G9 a dáta sú zakázané.

## Zmrazená implementácia pred prvým Python behom

- V17 SHA `1EC7DF765617A978940105129D74F02C1419B726CC023977F4DB426DDA5A33C4`;
- V18 SHA `3E30375748130FC69D51C2715D6521D3E1637E8F4C548E5605DCD3AB086AB492`;
- V19 SHA `067CFDBBA95712B04FCD8D571537D751A441B41F4B479FCFB54D7F7AAB281DA5`;
- runner 355 SHA
  `10656FF16FEBA7A4AD48A1EF1EF01733659DCAA46C0FC8FAC1643D3F6016422E`;
- runner 356 SHA
  `A3AA1E8F507D44AC4789B1A6EA2CE54D7BA788BC7EDB94558737FC181FE90510`;
- literal ancestor runner 346 SHA
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- contract: `48` source a `21` prerequisite položiek;
- harness SHA
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

Pred vytvorením tejto predregistrácie nebol V19 ani runner 356 spustený cez
Python. Od tohto bodu sú V19 a runner 356 immutable.
