# KMPC-084 — BI/k=.15 high-precision holdout assembly: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `TECHNICAL_FAILURE_PF089 / NO_PHYSICS_VERDICT / DO_NOT_RUN`

Zmrazené SHA-256 pred prvým Python behom:

- assembly modul: `E0F423357AE291FDEDE6BACC51D45F5F0D4326CD81C3A8453538B7A71FDE3846`;
- runner 328: `90863406F4DF7161D26B52AFDCBA433A2D53E19E94E02C0CF258434D9672A1CF`;
- stable/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

## Otázka

KMPC-083 vylúčil solve-roundoff na už float64-zostavenej matici, ale
`Einstein_0i[7] = 3.019756782389909e-9` ostal nad zmrazeným prahom `1e-9`.
KMPC-084 má rozlíšiť, či tento zvyšok vytvorilo float64 zostavenie
nezávislého holdoutu.

## Zmrazený rozsah

- iba atóm `BI`, `k=0.15 Mpc^-1`, nominal, audit support `[0,7]`;
- presne jeden 80-dps solve tej istej 104x104 driver matice ako KMPC-083;
- `Einstein_00` a `Einstein_0i` sa nikdy nepridajú do driver solve;
- všetkých 16 holdout koeficientov sa znova zostaví pri 80 dps z tých istých
  upstream koeficientov, pričom každý binary64 vstup sa prenesie presne cez
  `as_integer_ratio`;
- nemenia sa rovnice, support, prahy, normalizácia, mód, `k`, vstupy ani
  predikčná tabuľka;
- tento krok neauditujúci high-precision zostavenie driver matice nesmie sám
  vydať fyzikálny STOP.

## Povinné dôkazy

1. presná identita driver matice/konštanty s KMPC-083;
2. `precision_dps=80`, `high_precision_solve_count=1`;
3. `rows_added_to_driver_solve=0`;
4. explicitná 16x104 affine holdout matica, konštanta a SHA-256 fingerprint;
5. worst row, absolútne rezíduum, affine term norm a relatívne rezíduum;
6. osobitný údaj pre `Einstein_0i[7]`;
7. owner restore, compile, help, behaviorálny smoke a JSON serializácia.

## Predregistrované interpretácie

- ak 80-dps znovuzostavený holdout prejde `relative <= 1e-9` a
  `absolute fallback <= 1e-12`, kandidát je
  `PASS_C2_BI_K0p15_HOLDOUT_ASSEMBLY_ROUNDOFF_CLOSED_CANDIDATE_ONLY`;
- ak neprejde, kandidát je
  `REVIEW_C2_BI_K0p15_EXACT_DRIVER_ASSEMBLY_REQUIRED`;
- technická chyba je `TECHNICAL_ERROR / NO_PHYSICS_VERDICT` a zapisuje sa do
  Python error ledgeru.

Žiadny z týchto výsledkov nemení autoritatívny stav C2 bez následného
interného auditu. Externý auditný balík vznikne až po uzavretí tejto
ucelenej časti.

## Execution ledger

| Čas | Udalosť | Stav |
|---|---|---|
| 2026-07-19 | compile a help PASS; smoke zlyhal pri nesprávnom ownerovi `sha256_file` pred fyzikou | `PF-089 / DO_NOT_RUN` |
