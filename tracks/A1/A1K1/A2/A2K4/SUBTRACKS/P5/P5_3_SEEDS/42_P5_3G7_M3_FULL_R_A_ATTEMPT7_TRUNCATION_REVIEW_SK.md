# P5.3g7-M3-FULL/R-A — pokus 7, výsledok truncation review

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-028`  
**Vykonaný atóm:** `AD / k=0.05 Mpc^-1 / nominal`  
**Stav:** `REVIEW_TRUNCATION_EXTENSION_REQUIRED`  
**Fyzikálny rozsudok:** `NONE_NO_INVARIANT_CONTRADICTION`  
**K4:** `LIVE / 60/100`, bez zmeny

## 1. Immutable dôkaz

| súbor | SHA-256 | veľkosť |
|---|---|---:|
| `RUN_KMPC_028_P5_3G7_M3_FULL_RA_ATOM_AD_K0p05_NOMINAL.json` | `2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83` | 30 430 B |

Runtime bol `2.047 s` pod interným limitom `4.8 s`; nejde o technický
timeout. Runner vrátil exit `2`, preto sa podľa predregistrácie zvyšných
44 atómov nespustilo a agregátor zostal zakázaný.

## 2. Čo prešlo

- frozen contract, B1 left-null/Bianchi a produkčný TCA0 bridge;
- M1 anchor `76/76`, driver `7.97e-15`, holdout `6.07e-15`;
- F0 primary `6/6` a extended `10/10`;
- M3 primary `39/39` a extended `65/65`;
- všetky driver brány, `00/0i` holdouty, forbidden-layer/stress a produkčný
  contract;
- common `j=0..2` koeficienty medzi J2/J4: maximum `3.78e-13`, absolútna
  fallback `1.27e-16`;
- nulový limit daného nominal variantu a S-C weight split.

Toto je silný dôkaz, že sentinel nenarazil na chybnú rovnicu, chýbajúci stav,
rank deficit ani porušený Einsteinov constraint. Stále to nie je celý P5/G7
PASS.

## 3. Jediná neprejdená brána

J2/J4 per-state tail mal byť podľa frozen požiadavky najviac `1e-6`:

| plocha | maximum | najhoršia zložka | absolútna fallback |
|---|---:|---|---:|
| `z=1e-4` | `3.27706e-5` | `delta_f` | `4.12e-17` |
| `z=1e-2` | `3.27220e-3` | `eta` | `4.18e-17` |

Prah sa spätne neuvoľňuje. J2 seed preto na týchto plochách nemá požadovanú
rekonštrukčnú presnosť.

## 4. Prečo to nie je fyzikálna smrť

Rozšírený rad našiel legitímny prvý nový člen `j=3`. Pre metriku:

```text
eta_2 =  9.14447935e-3
eta_3 = -2.99661489e-3
|eta_3/eta_2| = 0.3276966
```

Preto očakávaný relatívny rozdiel J2/J4 vedie
`0.3276966*z`. Dáva `3.27697e-5` a `3.27697e-3`, prakticky presne pozorované
hodnoty. Pomer tailov je `99.85` pri pomere plôch `100`, teda efektívny
exponent `0.99968`: ide o očakávaný relatívny `O(z)` tail prvého vynechaného
rádu, nie o explóziu alebo porušenie constraints.

Autoritatívne obmedzenie je preto:

```text
J2 IS NOT ADEQUATE AT 1e-6 ON z=1e-4,1e-2
R-A/K4 NOT DEAD
```

## 5. Ďalší krok

Predregistrovať support ladder `J4 -> J6 -> J8` s rovnakými rovnicami,
plochami a prahmi. Musí overiť stabilitu spoločných koeficientov, rank/driver/
holdout na oboch nových supportoch a pokles J4/J6 aj J6/J8 tailu. Až potom sa
určí minimálny production support a môže vzniknúť nová 45-atómová matica.

## 6. Release hranica

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```
