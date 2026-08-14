# KMPC-089 — attribution serialization-bound successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `1/10`

## PF-092 a povolená oprava

KMPC-088 V1 porovnával 80-dps ledger s decimal referenciou KMPC-087 pri
absolútnom limite `1e-70`. Referenčné polia však obsahujú iba 50 významných
číslic. Posledné uložené miesto je pri residuale `~5.5e-17` rádovo `1e-66`
a pri affine norme `~1.82e-8` rádovo `1e-57`; V1 gate preto nebola
uskutočniteľná bez ohľadu na správnosť ledgeru.

KMPC-089 smie zmeniť iba validačnú vrstvu:

1. z mantisy každého uloženého decimal stringu spočíta počet významných
   číslic `d`;
2. pre nenulovú hodnotu s dekadickým exponentom `e=floor(log10(abs(x)))`
   vypočíta jednu jednotku posledného uloženého miesta
   `ulp_serialized = 10^(e-d+1)`;
3. round-trip PASS limit je presne `2*ulp_serialized`, osobitne pre residual
   a norm;
4. skutočnú chybu aj oba odvodené limity exportuje;
5. pôvodné `1e-70` názvy technických checkov nahradí serialization-aware
   názvami; ak ostane iný false check, exception musí uviesť jeho presné meno.

## Nezmenené

- všetky rovnice, vstupy, support `[0,7]`, 80 dps a prahy `1e-10/1e-9`;
- identický KMPC-087 driver/holdout fingerprint a presne dva HP solve;
- celý term ledger V1, klasifikácia M1/F0/background/M3 a holdout non-fit;
- žiadne nulovanie, fit, korekcia alebo zmena fyzikálneho verdictu.

## Zmrazená implementácia pred prvým Python behom

- V2 serialization-bound modul:
  `70EB60E8EBF01AE0DE2F84D2E08C309B59234B21CF87F79BB08F111D9B0F7242`;
- runner 333:
  `13C10A19A995407717FDFDD84658088F435AB8938803C435C72273722B0FFF0C`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `36/36` source/prerequisite hashov sedelo; všetkých
  `39` dlhých hash literálov malo 64 hex znakov.

Po freeze sa V2 ani runner pred official behom nemenia.

## Výsledok

- všetky pôvodné vecné a nové serialization-aware brány PASS:
  `REVIEW_C2_BI_K0p15_UPSTREAM_ATTRIBUTION_COMPLETE`;
- inak `TECHNICAL_ERROR / NO_PHYSICS_VERDICT` s presnými false checks.

Úspech vynuluje aktívny technický counter na `0/10`, ale C2 zostane `5/10`
a K4 `60/100`, kým sa samostatne neprepočíta predregistrovaný upstream
precision boundary.
