# KMPC-034 — CDI C1 primary/extended coverage predregistrácia

**Dátum:** 2026-07-16  
**Stav pri zmrazení:** `PREREGISTERED / NOT_RUN`  
**Neskorší stav:** `EXECUTED / dokument 59: CORE+COMMON PASS; PRIMARY [0,1] INSUFFICIENT; [0,3] REMAINDER OPEN`  
**Route:** `A1-K1 → A2-K4 → P5 → P5.3g7 → C1/CDI`  
**Runner:** `scripts/278_script_KMPC_034_P5_3g7_CDI_C1_primary_extended_coverage.py`  
**Výsledok:**
`scripts/results/k_mpc_005/RUN_KMPC_034_P5_3G7_CDI_C1_PRIMARY_EXTENDED_COVERAGE.json`  
**K4/P5:** `LIVE / 60/100`; `3.5/6`; bez automatickej zmeny

> Predbehové očakávania nižšie ostávajú historicky zmrazené. Výsledok,
> interpretácia a SHA sú autoritatívne zapísané v dokumente 59.

## 1. Čo sa vypočíta ľudskou rečou

Pre jediný mód `CDI`, jedinú škálu `k=0.05 Mpc^-1` a variant `nominal` sa
na nemennom R-A fyzikálnom jadre vypočítajú dve frakčné série:

```text
primary  support [0,1],
extended support [0,3].
```

Nie je dovolené preniesť AD/J4 verdikt. CDI má vlastný `leading_j=1` a
vlastnú hodnosť, driver rezíduá, `00/0i` holdouty, forbidden-order guard,
`U_c` regularitu a tail.

Raw rozdiel dvoch solve sa zachová ako diagnostika, ale nie je
autoritatívnym tail testom, pretože mieša common-coefficient drift s novými
mocninami. Rozklad sa preto súdi dvoma samostatnými bránami: stabilitou
spoločných koeficientov `j=0,1` a čistým tailom z extended koeficientov
mocnín `2,3`.

## 2. Povinný support/count guard pred solve

Nezávislý S-C0 contract a frozen solver musia dať:

```text
primary=(0,1),
extended=(primary.lo, primary.hi+2)=(0,3),
leading_j=1.
```

Počty sa nesmú iba skopírovať. Program ich odvodí z kardinality supportu:

```text
number_of_powers(primary)=2,
number_of_powers(extended)=4,
F0 counts = 2 × powers = 4/8,
M3 counts = 13 × powers = 26/52.
```

Každá odvodená hodnota sa porovná osobitne s nezávislým contractom aj s
frozen implementáciou. Tým sa uzatvára auditná medzera KMPC-033, kde
extended tuple nebol priamo automatizovane porovnaný.

## 3. Core fyzikálno-matematické brány

Pred interpretáciou tailu musia platiť:

1. frozen 13-state/driver/holdout contract a B1 left-null/Bianchi guard;
2. M1 accepted state `rank=unknowns=76`;
3. primary aj extended fuel a M3 matice majú plnú hodnosť a driver PASS;
4. `Einstein_00` a `Einstein_0i` ostávajú nezávislé holdouty a PASS;
5. forbidden layers/stress a production contract PASS;
6. `U_c` lower-order maximum `<=1e-12`;
7. všetky relevantné polia konečné;
8. S-C0 exact lift/collapse pre všetky skutočné `delta_fs,U_fs,sigma_fs`
   koeficienty primary aj extended.

KMPC-033 sa používa iba ako conditional split guard. Nenahrádza žiadnu z
týchto CDI M3 brán.

Nominálny `_single_variant` vracia dekoratívne `null_limit.pass=True` bez
výpočtu. Táto hodnota sa nezapočíta do core a exportuje sa iba scope marker
`NO_GAMMA0_OR_AF0_NULL_BRIDGE_EXECUTED_IN_C1`. Skutočné null varianty
patria až C3.

## 4. Common-coefficient bridge, čistý added-tail a očakávaný rozsah

Najprv sa samostatne overí prvý člen rozkladu

```text
sum_{j=0..1} (c_extended[j]-c_primary[j]) z^j.
```

Použije sa existujúci coefficient-wise bridge z frozen solvera: relatívny
prah `1e-8` a absolútny fallback `1e-12`. Táto brána musí prejsť; malé nové
mocniny nesmú zakryť prepísanie vedúceho koeficientu.

Potom sa na plochách `z=1e-4` a `z=1e-2` pre každý z 13 stavov vypočíta:

Na plochách `z=1e-4` a `z=1e-2` sa pre každý zo 13 stavov vypočíta:

```text
base       = sum_{j=1..1} c_extended[j] z^j,
added_tail = sum_{j=2..3} c_extended[j] z^j,
full       = base + added_tail.
```

Ak `max(|base|,|full|)>1e-12`, použije sa relatívna metrika
`|added_tail|/max(|base|,|full|)` s prahom `1e-6`; inak absolútna metrika s
prahovou hodnotou `1e-12`. Všetky hodnoty musia byť konečné. Raw mixed
truncation sa exportuje, ale nesmie prebiť čistý tail.

Pred behom nepredpokladáme, že `[0,3]` je dostatočný. Očakávame:

- core brány pravdepodobne PASS, ak CDI implementácia zdieľa správne R-A
  rovnice;
- common bridge alebo pure tail môžu legitímne vyžiadať väčší
  support/precision či audit conditioning;
- invariantný core rozpor sa nesmie zameniť za truncation REVIEW.

## 5. Rozhodovací strom

| Výsledok | Kandidát skriptu | Hlavný význam |
|---|---|---|
| core PASS + S-C0 PASS + common bridge PASS + pure tail PASS | `PASS_CDI_C1_PRIMARY_EXTENDED_ATOM` | CDI C1 kandidát na scoped PASS; stále nie P5.3/G8 |
| core PASS + common bridge FAIL | `REVIEW_CDI_C1_COMMON_COEFFICIENT_CONVERGENCE_UNCLOSED` | koľaj živá; support/precision/conditioning audit |
| core PASS + common bridge PASS + pure tail FAIL | `REVIEW_CDI_C1_SUPPORT_EXTENSION_REQUIRED` | koľaj živá; odvodiť ďalší support, bez zmeny prahov |
| core/holdout/regularita FAIL | `REVIEW_CDI_C1_CORE_GATE_UNCLOSED` | žiadna smrť bez nezávislej reprodukcie a auditov znamienok/vzorcov |
| timeout/syntax/import/hash/JSON | technical failure | žiadny fyzikálny verdikt; active counter +1 |

Fyzikálny STOP CDI by vyžadoval reprodukovaný invariantný rozpor po
dostatočnom supporte a nezávislom formulačnom audite. Jeden fail tu nestačí.

## 6. Nonclaims

Beh nepokrýva BI/NID/NIV, iné `k`, `gamma0/af0`, full hierarchy,
finite opacity, S-M, interné nu-steam módy, ODE, CMB, G8, CLASS, S8/H0,
skóre ani release. Do budúcich payloadov sa povinne exportuje
`release_trigger=NONE` a `prediction_table_effect=NONE`.

## 7. Prevádzkový limit a zdroje

Každý Python proces má interný limit najviac `4.8 s` a vonkajší najviac
`10 s`. Pred každým procesom je očakávanie v execution ledgeri 58.

| Súbor | SHA-256 |
|---|---|
| `cdi_c1_coverage.py` | `D57CA8CA5571A07440A987F4FB0DDA08A40DAF7EA8C95AF929FC5C936F2FCE0F` |
| runner 278 | `E8C2677E590D8129C6425AABAD5D80C1746BC5EF0B1E90E055A23641040695A4` |

Hashe boli získané read-only PowerShellom po zapracovaní nezávislého
preflightu common-coefficient bridge a odstránení dekoratívneho nominal
null checku. Runner zmrazil všetky priame zdroje a immutable KMPC-033
prerekvizitu. Prvý Python proces je dokumentačne povolený.
