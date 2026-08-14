# A2-K11 — dodatok k revízii 45 s SHA `973905D...`

**Dátum:** 2026-07-13  
**Aktuálne auditovaná revízia skriptu 45:**
`973905D79CBECBFD2DE55F13D3D3713D66C18B068BA74C7CAB566001A7312AEB`  
**Predchádzajúca auditovaná revízia:**
`61558FAF0D08E35B9B6D6CAFE30FFD55FD2E3FB2399D2A69F92D534EFC590CB1`  
**Verdikt novej revízie:** `NUMERICKY ČIASTOČNE OPRAVENÁ; FYZIKÁLNY PASS STÁLE ZAMIETNUTÝ`

## Čo nová revízia skutočne opravila

Nová revízia zmenila solver na

```text
rtol=1e-12,
atol=1e-16.
```

Reprodukovaný jemný transfer je
`1.9928603330433126e-13`, teda približne `1993*atol`. Námietka, že **táto
konkrétna revízia** má konečný výsledok pod `atol`, už neplatí.

Bez použitia vetvy `or is_damped` vyšli:

```text
step_log_transfer_relative_difference = 7.596109900001958e-7 < 1e-6
k_log_transfer_relative_difference = 1.729644785762819e-7 < 1e-6
```

Skript 54 navyše ukázal, že pri zväčšení počiatočnej amplitúdy o `10^12`
sa transfer zmenil iba s logaritmickou relatívnou metrikou
`1.4031451722414333e-7`. Aktuálna revízia teda prešla vlastným krokovým,
`k` a amplitúdovým numerickým testom.

Týmto sa explicitne obmedzuje starší audit: tvrdenia o výsledku pod `atol`
a o neprejdenej krokovej bráne platia pre hash `61558...`, nie pre hash
`973905...`.

## Tvrdenie 1 — „relatívne rezíduum 1.0 je iba šum/šum“

**Rozsudok:** `NEPRAVDA PRE TENTO BEH.`

Skript 45 počíta pomer dvoch globálnych maxím. Skript 54 preto vypočítal aj
bodové rezíduum v každom integračnom bode. Maximum jemného behu vzniklo pri

```text
index = 10
x = -6.994133327444566
a = 0.0009172474016952193
max_abs_state_at_point = 3.797893872691155e-5
```

Nie je to dnešný utlmený stav rádu `1e-13`. Constraintové členy boli

```text
q^2 Phi                                  = 3.31533651864446e-26
3(aE)^2(Phi_x+Phi)                       = 8.247609732449503e-10
1.5 a^2 delta_rho_T                      = 7.537973691400696e-13
sum(abs(terms))                           = 8.255147706140903e-10
abs(sum(terms))                           = 8.255147706140903e-10
pointwise relative residual               = 1.0
```

Všetky členy majú rovnaké znamienko. Nejde o `0/0` ani o zrušenie veľkých
členov s malým zvyškom; constraintová ľavá strana sa rovná celej norme.

Rozhodujúci test je linearita. Po zväčšení počiatočného módu o `10^12`
vznikli v tom istom bode

```text
terms = [3.3153e-14, 824.760973239322, 0.7537973691341978]
term norm = absolute residual = 825.5147706084562
pointwise relative residual = 1.0
```

Rezíduum sa škáluje spolu so stavom; nie je to pevná numerická podlaha.
Absolútna brána `residual<1e-8` preto závisí od svojvoľnej normalizácie
počiatočného lineárneho módu. Už stonásobné preškálovanie matematicky tej
istej lineárnej trajektórie by túto bránu zmenilo zo zelenej na červenú.
Taká brána nemôže dokazovať zachovanie Einsteinovho constraintu.

Malé absolútne číslo tiež nemožno nazvať „presnosť na deväť desatinných
miest“ bez referenčnej škály. Tu je prirodzená lokálna škála práve norma
constraintových členov a voči nej je chyba 100 %.

## Tvrdenie 2 — „výsledok nad atol a e^-37 dokazujú úplnú stabilitu“

**Rozsudok:** `PRVÁ ČASŤ ÁNO; ZÁVER NIE.`

Áno:

- výsledok novej revízie je nad `atol`;
- kroková a `k` metrika prešli prahom `1e-6`;
- amplitúdové škálovanie prešlo tou istou logaritmickou metrikou;
- zvolený kompenzovaný relatívny počiatočný vektor sa v implementovaných
  rovniciach pri `gamma=0.03` silno utlmí.

Nie:

1. Beh nazvaný `uncoupled_fine` má stále `lambda=0.15`. Faktor
   `exp(-37.1438)` je pomer `drag/no-drag` pri nenulovom energetickom toku,
   nie plný interakčný nulový limit.
2. Jeden utlmený počiatočný vektor nie je dôkaz, že všetky nezávislé
   fyzikálne eigenmódy sú stabilné. Potrebná je fundamentálna matica alebo
   úplná eigenanalýza adiabatic, relative-velocity a entropy módov.
3. Evolúcia nepropaguje kontrolovaný `00` constraint. Výsledok teda nie je
   riešením súčasne fluidných a Einsteinových rovníc v deklarovanom zmysle.
4. Rovnice skriptu 45 majú naďalej chyby zdokumentované v hlavnom audite:
   energetický tok `Q||u_c` nesprávne tlmí CDM Euler, fuel kontinuita je
   neúplná, fuel tlak nemá `1/delta`, energetický recoil má iný tvar a
   predložený mínusový štvorvektor nezodpovedá tlmiacej Eulerovej rovnici.
5. Skript stále nepočíta `P(k)`, `sigma_8` ani `S8`.

## Nevysvetlený scratch výsledok `1.71e-16`

Tvrdenie, že rozdiel medzi `1.99286e-13` a `1.71e-16` spôsobuje iba
interpolácia backgroundu, zatiaľ nie je doložené. Ide o faktor približne
`1165`. Krok `1e-4` leží medzi auditovanými krokmi `1.25e-4` a `6.25e-5`,
ktoré obe dávajú približne `1.9928e-13`. Hladká interpolačná konvergencia
preto sama osebe nepredpovedá medzihodnotu o tri rády menšiu.

Scratch tvrdenie môže byť auditované až po zachovaní jeho presného skriptu,
rovníc, SHA-256, tolerancií a plného výstupu. Dovtedy nemá dôkazovú váhu.

## Kanonický stav po dodatku

```text
A2-K11 = PREŽÍVA IBA FORMULAČNÚ BRÁNU — 15/100
script45 hash 973905... = FAIL FYZIKÁLNEJ/CONSTRAINTOVEJ BRÁNY
```

Skóre sa nemení, pretože numericky lepšie vyriešené riešenie nesprávnej a
constraint-neuzavretej sústavy neposúva fyzikálnu auditnú bránu. Aktívny
krok zostáva K11.1: lokálny pravidelný operátor a úplné rovnice odvodené z
jedného kovariantného ledgeru.

