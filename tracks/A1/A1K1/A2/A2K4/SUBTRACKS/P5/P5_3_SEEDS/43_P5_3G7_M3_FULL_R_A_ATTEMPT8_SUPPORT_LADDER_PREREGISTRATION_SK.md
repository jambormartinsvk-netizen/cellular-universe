# P5.3g7-M3-FULL/R-A — pokus 8/10, support-ladder predregistrácia

**Dátum:** 2026-07-16  
**Run ID:** `KMPC-029`  
**Route:** `A1-K1 -> A2-K4 -> P5 -> P5.3g7-M3-FULL/R-A`  
**Stav:** `ATTEMPT_8_PREREGISTERED / NOT_RUN`  
**Vstup:** immutable KMPC-028 AD/0.05/nominal J2/J4 REVIEW  
**Fyzikálny dopad:** žiadna zmena rovníc; iba vyšší truncation support

## 1. Otázka testu

Je nález pokusu 7 iba dôsledok príliš plytkého J2 production seedu, alebo sa
pri ďalšom rozšírení začnú posúvať už prijaté koeficienty a constrainty?

Testuje sa jediný sentinel `AD / k=0.05 / nominal`. Žiadny iný mód, k ani
variant sa zatiaľ nespúšťa. Existujúci J4 stav sa nerepočíta ani neprepisuje;
načíta sa z immutable KMPC-028 súboru s hashom
`2294E8623675B49F2D5A814005306D4E98E3CBDF4A1A66BD3AE1A9C0331EFC83`.

## 2. Frozen fyzika a prahy

Nesmú sa zmeniť:

- physics base `full_ra_m3_seed.py`, SHA
  `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2`;
- 13 stavov, 13 driverov, `00/0i` holdout, synchronous gauge a M1 anchor;
- F0/M3 rovnice, PF-063 tlak, B1/TCA0 guard a spectator-order pravidlá;
- `rcond=1e-12`, rank ratio `1e-10`, driver `1e-10`, holdout `1e-9`;
- common coefficient `1e-8`, absolute fallback `1e-12`;
- tail `1e-6`, plochy `z=1e-4,1e-2`, cap `z<=0.05`;
- conditional Phi1/M3-TCA0 scope a všetky jeho zákazy.

Prah tail sa po výsledku pokusu 7 neuvoľňuje.

## 3. Dva nové atómy

Každý proces znovu zostaví frozen M1 štandardný AD stav a vyrieši presne jeden
F0/M3 support:

| atóm | F0 rows/unknowns | M3 rows/unknowns | immutable výsledok |
|---|---:|---:|---|
| J6, support `0..6` | `14/14` | `91/91` | `RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J6.json` |
| J8, support `0..8` | `18/18` | `117/117` | `RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J8.json` |

M1 štandardný seed musí mať rovnaký maximálny rád ako daný atóm; frozen
default `order=5` sa nesmie použiť pre J6/J8. Použije sa existujúci anchored
builder bez zmeny rovníc:

| atóm | M1 order | full/reduced unknowns | driver+initial rows |
|---|---:|---:|---:|
| J6 | 6 | `88/87` | `110` |
| J8 | 8 | `110/109` | `132` |

Okrem existujúceho helper metadata sa znovu vyhodnotia **všetky** driver a
holdout powers `-1..J`, nie iba pôvodný nízky `checked_hi`. Plný rank,
anchor, driver aj holdout musia prejsť rovnakými frozen toleranciami. Chýbajúci
M1 koeficient sa nesmie ticho nahradiť nulou.

M1 full-order rezíduá sa normalizujú legacy-kompatibilným globálnym maximom
absolútnej hodnoty stavového koeficientu. Je to kontrola konzistencie s
existujúcim M1 helperom, nie per-row affine backward-error dôkaz. Driver používa
`1e-10`, všeobecný Einstein holdout `1e-9`; toto obmedzenie sa musí uviesť aj
vo výsledku.

Poradie je J6, potom J8. Každý má interný limit `4.8 s` a vonkajší `10 s`.
Pri technickom páde alebo neprejdení rank/driver/holdout sa balík zastaví.
Oba procesy sú spolu jeden pokus 8/10.

### Povolený shape-guard adaptér

Frozen `_solve_fuel_zero` a `_solve_m3` obsahujú technickú kontrolu počtu,
ktorá rozlišuje iba pôvodný primary J2 a extended J4. Rovnice a zostavenie
matice samy vyšší support podporujú, ale bez adaptéra by J6/J8 skončil pred
solve na očakávanom starom počte `10/65`.

Nový wrapper preto smie v každom samostatnom procese **iba dočasne** nastaviť
`EXPECTED_F0_EXTENDED[AD]` a `EXPECTED_M3_EXTENDED[AD]` na predregistrovaný
počet daného supportu. Musí:

1. pred zmenou overiť pôvodné frozen hodnoty `10` a `65`;
2. pre J6 nastaviť `14` a `91`, pre J8 `18` a `117`;
3. použiť `try/finally` a vždy obnoviť `10` a `65`;
4. exportovať before/during/after hodnoty a `restored=true`;
5. nemení support, rovnice, coefficients, tolerancie ani žiadny iný globál.

Toto je technické rozšírenie shape guardu, nie zmena fyziky. Ak statický audit
nájde inú mutáciu, pokus sa nesmie spustiť.

## 4. Agregátor bez nového solve

Výsledok
`RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_LADDER_ATTEMPT8.json` musí načítať:

1. frozen J4 stav z KMPC-028;
2. nový J6 stav;
3. nový J8 stav.

Fail-closed overí hashe, supporty, plné ranky, driver, holdout, contract,
finite koeficienty a potom vypočíta:

- common `j=0..4` J4/J6;
- common `j=0..6` J6/J8;
- per-state tail J4/J6 a J6/J8 na oboch frozen plochách;
- dominantný nový člen osobitne pre powers `5,6` a `7,8` ako
  `(state,power,abs(c_j z^j))` na každej ploche a efektívny exponent medzi
  plochami, všetko diagnostic-only;
- explicitnú konečnosť všetkých F0/M3 koeficientov;
- monotónnosť relative aj absolute fallback tailu cez normalizovaný scalar
  `max(relative/1e-6, absolute/1e-12)` na oboch plochách;
- presnú množinu dvoch support súborov J6/J8; extra support JSON je FAIL.

Agregátor má rovnaký interný limit `4.8 s` a externý limit `10 s`.

## 5. Vopred zmrazené výsledkové vetvy

### Adekvátny J4 production support

Oba common-coefficient testy prejdú a J4/J6 aj J6/J8 tail sú najviac `1e-6`:

```text
PASS_SUPPORT_LADDER_SENTINEL_J4_ADEQUATE
```

Toto je iba `candidate_interpretation_not_verdict`; autoritatívny scoped
verdikt udeľuje hlavný orchestrátor po číselnom audite. Iba tento sentinel
potom smie pokračovať do novej 45-atómovej matice s production
J4 a guard J6. K4 ostáva najviac 60/100.

### J4 nedostatočný, J6 adekvátny

J4/J6 tail neprejde, ale J6/J8 prejde a koeficienty/ranky/holdouty sú stabilné:

```text
REVIEW_PRODUCTION_SUPPORT_MUST_BE_AT_LEAST_J6
```

Nejde o fyzikálnu smrť. Pred novou maticou treba predregistrovať production
J6/guard J8.

### Hlbší truncation alebo formulačný review

J6/J8 tail neprejde, common koeficienty sa posunú, rank alebo holdout zlyhá:

```text
REVIEW_SUPPORT_LADDER_UNCLOSED
```

Bez post-hoc prahu sa osobitne audituje asymptotickosť, conditioning a prvý
vynechaný rád. Fyzikálny STOP vyžaduje invariantný rozpor, nie iba pomalú
konvergenciu radu.

### Technický pád

Timeout, syntax, serializácia alebo storage:

```text
ATTEMPT_8_TECHNICAL_FAILURE
PHYSICS_VERDICT=NONE
```

## 6. Procesné a failure názvy

Presné poradie je:

```text
py_compile(wrapper, runner) -> --help -> J6 -> J8 -> aggregate
```

Po prvom nenulovom exite sa ďalší proces nespustí. Failure súbory sú:

```text
RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J6_TECHNICAL_FAILURE.json
RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_J8_TECHNICAL_FAILURE.json
RUN_KMPC_029_P5_3G7_M3_FULL_RA_SUPPORT_AGGREGATE_TECHNICAL_FAILURE.json
```

Chyba pred úspešným CLI parsingom alebo chyba samotného zápisu môže mať iba
Markdown/error-ledger dôkaz; nikdy sa nepovažuje za fyzikálny výsledok.

## 7. Release hranica

```text
NO_NEW_TRIGGER
EXISTING_PT1_REMAINS_OPEN
PT2_NOT_ESTABLISHED
```

## 8. Statický audit a hash freeze

Read-only fyzikálny, matematický a dokumentačný audit pred prvým Python
procesom odstránil order-5 M1 blocker, doplnil full-order M1 residualy, finite
gate, exact power sets, per-state tail a normalizovanú monotónnosť. Fyzikálne
rovnice ani frozen base sa nemenili.

| artefakt | frozen SHA-256 |
|---|---|
| physics base | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` |
| ladder wrapper | `934AE0E9663A6D8CFD92DE2843E59D7A94065D277227EECC73F9B6646B6EE475` |
| runner 273 | `4B44F183325E5BC4437EA5703E2A3DE242A2F11E86D0DB46B1878EAFB12D1F33` |

**Stav po freeze:** `ATTEMPT_8_FROZEN_READY / NOT_RUN`; counter zostáva
`7/10`, kým sa nespustí prvý Python proces.
