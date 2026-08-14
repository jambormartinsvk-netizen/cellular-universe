# KMPC-087 — BI/k=.15 high-precision driver assembly: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`

## Otázka

KMPC-083 vylúčil solve-roundoff a KMPC-086 vylúčil posledné float64
zostavenie/odčítanie holdoutu. KMPC-087 má rozlíšiť, či hranicu
`Einstein_0i[7]` vytvára float64 zostavenie 104x104 driver matice.

## Zmrazený rozsah

- iba `BI`, `k=0.15 Mpc^-1`, nominal, support `[0,7]`;
- presné poradie 13 stavov, 13 driver rovníc a 2 holdout rovníc z
  `full_ra_contract.py`;
- jeden baseline 80-dps solve float64-zostavenej driver matice na zachovanie
  parity s KMPC-083/086 a jeden 80-dps solve znovuzostavenej driver matice;
- 104x104 driver affine matica sa zostaví pri 80 dps z nulového a 104
  jednotkových probe; všetky binary64 upstream koeficienty sa prenesú presne
  cez `as_integer_ratio`;
- na exact-driver riešení sa samostatne znovuzostaví 16x104 holdout pri
  80 dps; `Einstein_00/0i` sa nikdy nepridajú do solve;
- rovnice, support, mód, `k`, vstupy, normalizácia a prahy `1e-10/1e-9`
  sa nemenia;
- upstream M1, F0 a background generátory ostávajú binary64 a tvoria
  explicitný scope limit výsledku.

## Povinné dôkazy

1. exact ordered contract a shapes `104x104` driver, `16x104` holdout;
2. baseline driver SHA identický s KMPC-083/086;
3. exact-driver SHA, float64-versus-HP assembly difference a solution SHA;
4. presne dva HP solve celkom, z toho jeden exact-driver solve;
5. exact-driver residual PASS/FAIL s worst row;
6. exact-driver-solution holdout residual a osobitný `Einstein_0i[7]`;
7. `rows_added_to_driver_solve=0`, owner restore, compile/help/smoke a
   immutable JSON.

## Zmrazená implementácia pred prvým spustením Pythonu

- výpočtový modul `c2_bi_k0p15_high_precision_driver_assembly.py`:
  `4C11A3EE3C08B084E53E5F313152A29C768E2F0F48D74588D0F5E37688B50B46`;
- runner `331_script_KMPC_087_P5_3g7_C2_BI_k0p15_high_precision_driver_assembly.py`:
  `F297F116ADC873999AF15E41CA3D4CCB9110293C8E97B404A86E607B6471400C`;
- stabilný atomický harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5`;
- high-precision harness:
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola pred freeze: všetkých `32/32` deklarovaných source a
  prerequisite hashov sedelo; všetky hash literály mali 64 hex znakov.

Po tomto freeze sa výpočtový modul ani runner pred oficiálnym behom nemenia.

## Predregistrované interpretácie

- exact driver PASS a exact holdout PASS:
  `PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_CANDIDATE_ONLY`;
- exact driver PASS, ale exact holdout FAIL:
  `REVIEW_C2_BI_K0p15_UPSTREAM_COEFFICIENT_PRECISION_REQUIRED`;
- exact driver sa nedá plnohodnotne vyriešiť alebo jeho vlastný residual
  neprejde:
  `REVIEW_C2_BI_K0p15_EXACT_DRIVER_SYSTEM_UNCLOSED`;
- technická chyba: `TECHNICAL_ERROR / NO_PHYSICS_VERDICT`.

Žiadny výsledok s upstream binary64 scope limitom sám nevydá fyzikálny STOP.
Autoritatívny stav sa zmení iba po internom audite immutable raw.
