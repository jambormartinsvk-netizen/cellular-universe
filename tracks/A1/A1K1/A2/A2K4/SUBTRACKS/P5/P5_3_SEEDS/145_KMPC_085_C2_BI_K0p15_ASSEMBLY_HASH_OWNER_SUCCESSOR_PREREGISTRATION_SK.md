# KMPC-085 — assembly hash-owner successor: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_PF090 / NO_PHYSICS_VERDICT / DO_NOT_RUN`

Zmrazené SHA-256 pred prvým Python behom:

- assembly V1: `E0F423357AE291FDEDE6BACC51D45F5F0D4326CD81C3A8453538B7A71FDE3846`;
- hash-owner V2: `9DC7C357D15580AFA3276BA4E3294870B69FAD6117F3A25F46DB1FADE5EBE865`;
- runner 329: `F533189B4B8EACA1C98748544F0F5DDE5F8C39D1653FA94938CA0340604AD231`;
- stable/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

PF-089 zastavil KMPC-084 v smoke pred fyzikou. KMPC-085 smie opraviť iba
owner `sha256_file`: algebraické `Series/PairSeries` ostávajú vo vnútornom
`mode_resolved_puiseux`, kým hash helper sa explicitne vezme z
`c2_fourier_coverage`. Assembly V1, 80 dps, jediný solve, 16x104 nezávislý
holdout, rovnice, upstream koeficienty, support `[0,7]`, prahy, runtime a
predregistrované interpretácie dokumentu 144 ostávajú nezmenené.

Successor musí navyše smoke-testovať, že algebraický a hash owner sú
odlišné a správne dosiahnuteľné. KMPC-084/runner 328 sa nesmie opakovať.
Technická chyba nevydá fyzikálny verdikt.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile/help PASS; owner a hash checks PASS; jediný false bol chybný decimal-exact affine fixture | `PF-090 / DO_NOT_RUN` |
