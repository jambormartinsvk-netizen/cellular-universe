# KMPC-086 — assembly affine-fixture successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `EXECUTED / IMMUTABLE / REVIEW_EXACT_DRIVER_ASSEMBLY_REQUIRED`

Zmrazené SHA-256 pred prvým Python behom:

- assembly V1: `E0F423357AE291FDEDE6BACC51D45F5F0D4326CD81C3A8453538B7A71FDE3846`;
- hash-owner V2: `9DC7C357D15580AFA3276BA4E3294870B69FAD6117F3A25F46DB1FADE5EBE865`;
- fixture V3: `0FF2B72AFB5A480A891A71685DBA3394566C6945385F33913DAEA888AACA1C99`;
- runner 330: `14B82468790AFA1CE6330EF8B332E894309D2FE702BE29CE5BA0A7877D87728B`;
- stable/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

PF-090 zastavil KMPC-085 v smoke pred fyzikou, pričom všetky owner a hash
kontroly prešli. KMPC-086 smie zmeniť iba `assembly_affine_reassembly_fixture`:
fixture použije explicitnú afinnú funkciu `r(x)=a+b*x` a porovná jej priamu
hodnotu s rekonštrukciou `r(0)+(r(1)-r(0))*x` nad tými istými presne
prenesenými binary64 vstupmi. Nesmie predpokladať exact desiatkovú identitu.

Numerický assembly V1, hash-owner V2, 80 dps, jeden driver solve, holdout
non-fit, 16x104 assembly, rovnice, prahy, support, runtime a interpretácie
dokumentu 144 ostávajú nezmenené. Runnery 328 a 329 sa nesmú opakovať.
Technická chyba nevydá fyzikálny verdikt.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help/smoke PASS | `PREFLIGHT_PASS` |
| 2026-07-19 | prvé official volanie bez povinného `--output`; argument guard pred fyzikou | `PF-091 / RERUN_SAME_IMMUTABLE_RUNNER_ALLOWED` |
| 2026-07-19 | corrected official dokončený; raw SHA `54F9A116...B65649E` | `IMMUTABLE / REVIEW_EXACT_DRIVER_ASSEMBLY_REQUIRED` |
