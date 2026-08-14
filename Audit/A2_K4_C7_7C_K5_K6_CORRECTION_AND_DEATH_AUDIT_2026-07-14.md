# A2-K4 / C7.7c — korekcia K5 a rozsudok K6

**Dátum:** 2026-07-14  
**Skóre pred/po:** `66.5/100`  
**A2-K4:** **ŽIVÁ**, C7.7c neuzavretá  
**C7.7c-K5:** **MŔTVA numerická podkoľaj**  
**C7.7c-K6:** **MŔTVA numerická podkoľaj**

## 1. Korekcia prvého K5a behu z používateľom zachovaného výstupu

Predchádzajúci dodatok uvádzal, že prvý 8-sekundový beh K5a nedal agentovi JSON pred ukončením vonkajšieho obalu. Používateľ zachoval jeho úplný výstup, preto sa audit spresňuje:

| Pole | Hodnota |
|---|---:|
| trajektória | NID/deep |
| cieľ | `x=-25→-24` |
| runtime | `8.016 s` |
| RHS volania | `416 129` |
| dokončené segmenty | `0/1` |
| redukcia `max|J|` | `7.062168114071022×10^13` |
| relatívna odchýlka spektra | `1.693632718507244×10^-10` |
| solver | timeout v internej RHS poistke |

Výstup nemení rozsudok. Potvrdzuje, že ani dlhší K5a beh neurobil prvý segment. Opakovanie s limitom 6 s malo rovnaký výsledok s 296 833 RHS volaniami.

## 2. K6a — fyzikálny stav s vektorovým atol

Skript `154_script_A2_K4_C7_7c_K6_vector_atol_segment_evolution.py` ponechal stav a RHS vo fyzikálnych premenných. Jedinou zmenou bolo

`atol_i = 10^-12 max(|y_i,start|,|y_i,series(-18)|,10^-300)`.

Dva dlhšie pokusy narazili na vonkajší limit bez včasného JSON. Posledný diagnostický beh s vnútorným limitom 3 s poskytol úplný výstup:

| Pole | Hodnota |
|---|---:|
| trajektória | NID/deep |
| runtime | `3.015 s` |
| RHS volania | `131 201` |
| dokončené segmenty | `0/1` |
| posledné `x` | `-25.0` |
| stav/RHS konečné | áno |
| safety cap | neprekročený |

Vybrané tolerancie ukazujú príčinu:

| Komponent | `S_env` | `atol_i` |
|---|---:|---:|
| `h` | `1.7589×10^-14` | `1.7589×10^-26` |
| `eta` | `5.1140×10^-10` | `5.1140×10^-22` |
| `delta_f` | `3.3982×10^-17` | `3.3982×10^-29` |
| `L3_fs` | `1.3125×10^-16` | `1.3125×10^-28` |
| `L4_fs` | `1.8039×10^-24` | `1.8039×10^-36` |

NID počiatočné metrické a palivové komponenty vznikajú vo vyššom ráde a cez kompenzované species kombinácie. Požadovaná absolútna presnosť leží hlboko pod aritmetickou podlahou niektorých double-precision súčtov v RHS.

## 3. Dôvod smrti C7.7c-K6

K6 je mŕtva ako numerická podkoľaj, pretože:

1. nedokončila ani prvý predregistrovaný NID segment;
2. pevný faktor `10^-12` voči každej analytickej obálke vyžaduje pri constraintovo kompenzovaných premenných absolútnu presnosť, ktorú double-precision RHS nevie reprezentovať;
3. ďalšie predlžovanie času by nemenilo nesúlad medzi požadovaným `atol_i` a aritmetickou podlahou.

K6 sa nesmie opakovať s rovnakým tolerančným predpisom. Skript 154 a tento dôvod smrti sa zachovávajú.

## 4. Čo rozsudok neznamená

- Nejde o fyzikálnu smrť A2-K4.
- Nejde o dôkaz runaway alebo porušenia Einsteinových rovníc.
- Neznamená to, že `h`, `delta_f`, `L3` alebo `L4` sú fyzikálne nulové.
- Znamená to, že ich aktivitu nemožno čestne dokazovať jedným double-precision evolučným behom s absolútnymi toleranciami až `10^-36`.

## 5. Povinný ďalší audit

Pred novou podkoľajou sa musí kvantifikovať podmienenosť jednotlivých RHS súčtov. Komponenty nad aritmetickou podlahou môžu zostať v numerickom ledgeri; komponenty pod ňou budú vyžadovať vyššiu presnosť alebo analytický/Puiseuxov certifikát aktivity. Prah aktivity sa nesmie spätne znížiť iba preto, aby koľaj prešla.
