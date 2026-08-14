# KMPC-110 — checkpoint exact M3 resume: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `0/10`

## Presná otázka

Bol jediný checkpointový false check `M3_driver` s worst
`tight_coupling[7]=2.7715917114e-10 > 1e-10` iba binary64 solve/assembly
hranica? Alebo zostane nad prahom aj po 80-dps znovuzostavení a solve, keď
sa použije lossless HP-M1 checkpoint a bitovo identický audit F0 register?
Prejde zároveň nezávislý non-fit holdout vrátane `Einstein_0i[7]`?

## Vstupný kontrakt

- checkpoint KMPC-108 SHA:
  `683D867D19324B7B45F3724545FFB1D975DFBED883936298D790C12836E9D995`;
- receipt KMPC-109 SHA:
  `21EF9A9BF8D6E437CC848BD76EC026C5621534F35C0D88F99D2BFAFAD28118F9`;
- serialized-state SHA:
  `402B42E11C3582B4E3E46D047EA917A4C256E552F65C9DB070589150675EBF40`;
- HP-M1 sa obnoví z decimal90 pri 80 dps; audit F0 z `float.hex()`;
- natívny CPQR ani accepted `[0,5]` solve sa nesmú opakovať.

## Jediný dovolený výpočet

1. fail-closed overiť oba file SHA, receipt verdict, schema, poradie,
   round-trip a vnútorný fingerprint;
2. zopakovať iba audit `[0,7]` support solve na zachytenie frozen 104×104
   float64 M3 matice;
3. vyžadovať field-level paritu celého audit payloadu s KMPC-108 a bitovú
   `float.hex()` paritu fuel registra;
4. zlúčiť checkpoint HP-M1 a checkpoint F0 do autoritatívneho 13-state
   registra;
5. znovuzostaviť a vyriešiť presne jeden 104×104 driver pri 80 dps;
6. vyhodnotiť presne jeden 16×104 independent holdout bez pridania holdout
   riadkov do driver solve.

## Zmrazené rozhodovanie

`PASS_C2_BI_K0p15_SUPPORT_05_ADEQUATE_HP_M1_CANDIDATE_ONLY` je dovolený
iba ak súčasne platí:

- všetky SHA/schema/receipt/register/audit-parity/capture checks;
- pôvodná false množina je presne `{M3_driver}`;
- checkpoint non-driver gates sú všetky PASS;
- exact driver spĺňa `1e-10` a exact independent holdout `1e-9`;
- `rows_added_to_driver_solve=0`, jeden exact solve a owner restore PASS.

Exact driver false dá
`REVIEW_C2_BI_K0p15_HP_M1_EXACT_DRIVER_UNCLOSED`. Exact holdout false dá
`REVIEW_C2_BI_K0p15_HP_M1_EXACT_NONFIT_HOLDOUT_UNCLOSED`. Technická
SHA/parity/capture/schema chyba nevydá fyzikálny payload. Skript udeľuje iba
candidate; autoritatívny C2 krok vznikne až interným auditom.

## Scope a prahy

- driver `1e-10`, holdout `1e-9`, common/tail/background prahy nezmenené;
- M1 je 80-dps checkpoint, F0 zostáva presne checkpointová binary64 hodnota
  a background vstupy sú frozen binary64 presne bridged do `mpmath`;
- `[0,9]`, iné mode/k atómy, S-M, ODE, P5.4, G8/G9 a dáta sú zakázané;
- runtime presne `45.0 s`, bez predĺženia.

## Zmrazená implementácia pred prvým Python behom

- V17 exact resume:
  `1EC7DF765617A978940105129D74F02C1419B726CC023977F4DB426DDA5A33C4`;
- runner 354:
  `DA271E7FBF7EF6243C9B66A5DAE2875056166674ABAD2E145328309627E28454`;
- prior runner 353:
  `A390718F258FE47408888EFD6A825A5387D5C6573E8B66FF1AF5E81B2D3CAE57`;
- literal ancestor runner 346:
  `5DF6010385C76F743B4F59DA5F5F39C88CC4F205645CE2167864CAC40A548BCB`;
- výsledný contract: `46` source a `20` prerequisite položiek;
- harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`.

Pred vytvorením tejto predregistrácie nebol V17 ani runner 354 spustený cez
Python. Od tohto bodu sú V17 a runner 354 immutable.
