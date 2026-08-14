# P5.3g7-M3-FULL/R-A — pokus 8, J8 numerical review

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-029`  
**Stav:** `REVIEW_J8_NUMERICAL_DRIVER_RESIDUAL`  
**Fyzikálny rozsudok:** `NONE_NO_INVARIANT_CONTRADICTION`  
**K4:** `LIVE / 60/100`

## Immutable dôkazy

| support | SHA-256 | stav |
|---|---|---|
| J6 | `658495A11A3C72262CDCBEC9B9515794E506A6C7F14F40865704AA26E6C4636A` | všetky checks PASS |
| J8 | `1EE3FCDF3B77C6C7E4C26317A3F39AA45D4CFA5BA6B559E312E598BC3ED51AB8` | jediný check `M3_driver=false` |

Agregátor sa podľa stop pravidla nespustil; ladder tail verdict nevznikol.

## J6

M1 `87/87`, F0 `14/14`, M3 `91/91`, driver `2.916e-12`, holdout
`3.824e-12`, equilibrated singular ratio `0.2759143`; shape guard obnovený.
J6 zostáva platný kandidátsky artefakt, ale ešte nie schválený production
support bez stabilného J8 guardu.

## J8

Prešlo:

- M1 `109/109`, full-order driver `7.46e-14`, holdout `6.86e-15`;
- F0 `18/18`, driver `1.72e-12`;
- M3 rank `117/117`, equilibrated singular ratio `0.275914`;
- `00/0i` holdout `2.778e-10 < 1e-9`;
- B1/TCA0/contract/forbidden/regularity/finite a shape restoration.

Jediná nezhoda:

```text
M3 driver max relative residual = 1.5577307299e-10
frozen limit                  = 1.0000000000e-10
worst row                     = fuel_Euler[8]
```

Prekročenie je 1.56× na poslednom coefficient row. Raw ratio je `0.001027`,
equilibrated ratio `0.275914`, teda nejde o rank stenu. Uložený JSON však pre
najhorší relative row neobsahuje signed residual ani term norm; výsledok sa
nesmie spätne prekvalifikovať na PASS.

## Obmedzenie a ďalší krok

Pokus 9 musí na rovnakej J8 matici exportovať residual provenance a vykonať
presne jednu deterministickú iterative-refinement korekciu. Prahy, support,
rovnice a holdout sa nemenia. Až koeficientová zhoda, driver PASS a nezávislý
holdout PASS môžu potvrdiť numerický pôvod.

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```
