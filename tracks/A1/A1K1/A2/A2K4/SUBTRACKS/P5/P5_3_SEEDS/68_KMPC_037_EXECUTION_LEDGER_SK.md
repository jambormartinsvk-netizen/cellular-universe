# KMPC-037 až KMPC-039 — spoločný execution a technický lineage ledger

**Dátum:** 2026-07-18  
**Stav:** `KMPC039_AUTHORITATIVE_PASS / PF072_PF073_PRESERVED`  
**Autorita:** používateľ explicitne zrušil odklad do 2026-07-24  
**Predregistrácia:** dokument 67, zmrazený pred prvým Python procesom

Dokumentačné ID 69–73 boli pred commitom zlúčené sem ako náprava nadmernej
fragmentácie; výpočtové artefakty, hashe a PF záznamy sa tým nemenia.

## Povinné poradie

1. compile base;
2. compile runner;
3. runner `--help`;
4. `--smoke --max-runtime-seconds 4.8`;
5. jediný `--audit --max-runtime-seconds 45` s externým limitom 60 s;
6. hash a nezávislé prečítanie canonical JSON;
7. až potom autoritatívny projektový posudok.

Každý krok sa vykonáva iba po úspechu predchádzajúceho. Technická chyba sa
nezamieňa za fyzikálny REVIEW/STOP a zapisuje sa do Python error ledgeru.

## Predbežné očakávanie bez verdictu

- V0 musí reprodukovať KMPC-036;
- V2 correction sa očakáva rádovo pod `1e-14`;
- V2/V3 môžu, ale nemusia uzavrieť tri power-7 riadky;
- žiadny post-hoc posun `1e-10`, correction capu, dps ani metódy nie je
  dovolený.

## Výsledky krokov

- compile base: `PASS`, exit `0`;
- compile runner: `PASS`, exit `0`;
- `--help`: `PASS`, povinný explicitný runtime a exkluzívny smoke/audit mód;
- smoke `4.8 s`: `PASS`, exit `0`;
- mpmath QR API: `PASS`;
- exact float64 transfer: `PASS`;
- všetkých 10 base negatívnych fixtures: `PASS`;
- všetkých 5 runner negatívnych fixtures: `PASS`;
- canonical/failure/temp output pred auditom: neprítomný.

## Audit

- príkaz: jediný audit s interným limitom `45 s` a externým `60 s`;
- wall čas do zlyhania: `6.9 s`;
- fáza: `audit`, počas V3 `mpmath.qr_solve`;
- exception: `ValueError: matrix is numerically singular`;
- canonical success JSON: nevznikol;
- immutable failure JSON:
  `RUN_KMPC_037_P5_3G7_M1_ORDER7_NUMERICAL_REFINEMENT_TECHNICAL_FAILURE.json`;
- failure SHA-256:
  `7F1B5B4AE0A80287B29F929C76541F0F1899A404C2D800EF138A5563E44315E1`;
- fyzikálny verdict, score, prediction table a release: bez zmeny;
- Python error ledger: `PF-072`.

Runner 281 sa neopakuje. Najprv je dovolená iba read-only diagnostika príčiny
singularity; iný solver alebo native rebuild vyžaduje novú predregistráciu.

## PF-072 — príčina a zmrazený KMPC-038 nástupca

Read-only audit mpmath 1.3.0 `matrices/linalg.py`, SHA-256
`D380B78A3CCC1689BBA1BE5F5C10837F23CF768DC121BA08784F31D80EAFA85D`,
ukázal nepivotovaný Householder výraz
`-sign(re(A[j,j]))*sqrt(s)`. Pri presnej nulovej diagonále dá orientáciu `0`
namiesto štandardnej nenulovej vetvy a neskôr môže plnohodnostnú riedku
maticu označiť za singulárnu.

Pred KMPC-038 sa zmrazila jediná oprava: `+1` pre `re(A[j,j])>=0`, inak
`-1`. Matica, RHS, poradie, 80 dps, QR metóda, prahy a počet solve ostali
nezmenené; pivotovanie, normal equations, SVD a native rebuild boli zakázané.

- overlay V2 SHA:
  `81D7EA664677158E98340E39F395DE2EE0DAB6EEFCFFA785089F51E62434193A`;
- runner 282 SHA:
  `DD09A025CE0DD3927FC93E9198C50E4E7253566FED3B51CFC41010F15B939269`;
- výsledok smoke: PF-073, `AttributeError: module 'mpmath' has no attribute
  'householder'`;
- failure SHA:
  `E85E6C75DF9F92E4DFC5D4B98D5C3455E55B545EA5AF90A7C317FCEF564DA64F`;
- full audit KMPC-038: `NOT_RUN`.

Príčina PF-073 bola iba chybný runtime owner: interná callable patrí
`mpmath.mp.householder`, nie exportnému modulu `mpmath`.

## Zmrazený KMPC-039 context-owner nástupca

Jediný rozdiel voči KMPC-038 bol owner bridge na `mpmath.mp`. Bridge musel
overiť bound `__self__`, modul/názov callable a obnovenie v `finally`.
Zero-tie formula a celý vedecký kontrakt sa nemenili.

- V3 context overlay SHA:
  `1E35D147049F981F901B9A2B72C76EBE5705F5D19A04447E742AE978A9BC5278`;
- runner 283 SHA:
  `6B9B998661BC31A8CBC8F906A5FEA6F2BAB9FACCCC145642E68CDF581FECED69`;
- compile overlay/runner/help: `PASS`;
- owner, callable restore, zero-diagonal repair, nonzero-diagonal parity,
  operation-count a publish fixtures: `PASS`;
- jediný audit: exit `0`, wall `6.7 s`, internal `5.125 s`;
- canonical result SHA:
  `BDF3317235FEDEA23EDF8C23563423014F2E98A461C6E638C474DF94471CE016`;
- post-run validácia: source/prerequisite hashes, prahy, 121+18 V2/V3,
  operation counts `1/1/0` a absencia failure/temp všetko `PASS`;
- autoritatívny posudok: dokument 74.

KMPC-037 a KMPC-038 ostávajú `DO_NOT_RUN_TECHNICAL`. Ich failure JSON a
centrálne PF-072/PF-073 záznamy sa zachovávajú; nejde o fyzikálne verdikty.
