# A2-K4.2 — problém, brány a kill kritériá

**Dátum predregistrácie:** 2026-07-14  
**Východiskový stav:** `A2-K4 PREŽÍVA K4.1 — 55/100`  
**Rozsah:** deklarovaný deväťpremenný effective-fluid systém s perfektnou
radiáciou; nie plná fotónovo-neutrínová Boltzmannova hierarchia

## Cieľ

K4.2 má rozhodnúť, či entalpicky vážený energy-frame uzáver K4:

1. nemá high-k gradientový alebo efektívny kinetický problém;
2. má správny nulový limit;
3. zachováva Einsteinov `00` constraint na aktívnych bodoch;
4. nespôsobuje stratu linearity úplnej regulárnej bázy po vstupe módov pod
   horizont.

Výpočet nesmie byť ladený na `S8` a jeho PASS sa nesmie nazvať
observačným alebo Boltzmannovým PASS.

## Predregistrovaná mriežka

```text
q = k/H0 = 30, 300, 1000
```

Pri `H0/c = h/2997.9 Mpc^-1` približne zodpovedá

```text
k = 0.010, 0.100, 0.334 h/Mpc.
```

Počiatočný bod je `x=ln a=-20`. Pre `q=1000` musí platiť
`q/(aE)<1e-3`, aby všetky módy začínali bezpečne mimo horizontu.

## T0 — identita rovníc

- rovnaký background, `lambda=0.15`, `delta=0.02297` ako K4.1;
- rovnaké kontinuity, Eulerove rovnice a constrainty ako skripty 28, 30 a
  66;
- žiadny nový parameter ani člen pridaný podľa výsledku.

**KILL:** zistená zmena rovníc alebo konvencie bez novej koľaje.

## T1 — high-k hlavný symbol

Po eliminácii nedynamického potenciálu cez Einsteinov constraint musí mať
effective-fluid symbol iba rýchlosti

```text
0, 0, 0, 0, +1, -1, +1/sqrt(3), -1/sqrt(3).
```

**PASS:** všetky fyzické rýchlosti sú reálne a `|c|<=1`.  
**KILL:** záporné `c_s^2`, komplexná charakteristická rýchlosť alebo
superluminálna vetva.

## T2 — efektívne kinetické znamienko

Pre fuel uzáver `c_s,f^2=1` musí byť

```text
(rho_f+p_f)/c_s,f^2 = delta rho_f > 0.
```

Radiácia musí mať `rho_r+p_r=4rho_r/3>0`; prachové sektory majú kladnú
hustotu a nulovú zvukovú rýchlosť.

**KILL:** záporná efektívna zotrvačnosť.  
**OBMEDZENIE:** bez mikroskopickej akcie to nie je úplný UV ghost dôkaz.

## T3 — interakčný rád a nulový limit

Členy `lambda/E` nesmú meniť high-k hlavný symbol a pri `lambda=0` musia
všetky interakčné členy presne zmiznúť.

**KILL:** interakčný člen rádu `k` alebo `k^2`, ktorý mení znamienko
charakteristického polynómu, alebo neprejdený nulový limit.

## T4 — úplná regulárna báza

Numerika musí preniesť všetky tri módy K4.1:

1. adiabatický;
2. CDM density izokurvatúrny;
3. baryónový density izokurvatúrny.

Jeden vybraný seed nestačí. Počiatočný `00` constraint musí mať relatívne
rezíduum `<1e-10`.

## T5 — Einsteinov constraint

Na bodoch, kde norma troch `00` členov presahuje `1e-12` ich globálneho
maxima, musí platiť

```text
max pointwise relative residual < 1e-6.
```

Súčasne sa hlási maximálne absolútne rezíduum normalizované na počiatočnú
auditnú normu. Pomer dvoch globálnych maxím sa nepoužíva ako jediný test.

**KILL:** aktívne bodové relatívne rezíduum `>=1e-6` po konvergenčnej
kontrole.

## T6 — numerická konvergencia

Pre `q=300`:

- sprísnenie `rtol/atol`: relatívny rozdiel finálnej matice `<1e-5`;
- zmena backgroundového kroku: `<1e-4`;
- posun štartu `x=-20 -> -22`: `<1e-4`.

Každý beh má externý limit `<=60 s`, interný runtime limit a checkpoint.
Timeout je `NEUZAVRETÉ`, nie fyzikálny FAIL.

## T7 — linearita a nekontrolovaný rast

Pre každé `q` sa vypočíta najväčší singulárny transfer úplného regulárneho
priestoru. Pri referenčnej primordiálnej auditnej amplitúde `1e-5` musí byť

```text
1e-5 T_max < 1.
```

Osobitne sa hlási K4/`lambda=0` pomer. Veľký pomer k zanikajúcej referencii
nie je automaticky absolútna explózia.

**KILL:** absolútna strata linearity, nefinite stav alebo rast obálky úmerný
kladnej mocnine `q`, ktorý odporuje analytickému symbolu.

## Rozsudky

- všetky T0–T7 PASS: `PREŽÍVA K4.2 — 59/100`;
- analytika PASS, numerika TIMEOUT: `K4.2 NEUZAVRETÁ`;
- fyzikálny KILL: nový dôvod smrti K4; historický M-011 sa neobnovuje.

Po úspechu K4.2 nasleduje plná fotónovo-neutrínová/A3 brána. K4.2 samo
nepočíta `P(k)`, `sigma_8` ani `S8`.

## 8. Výsledok po uzamknutí brán

**Rozsudok:** `PREŠLA K4.2 V PERFECT-RADIATION ROZSAHU`.
**Stav:** `PREŽÍVA K4.2 — 59/100`.

Všetky T0–T7 brány prešli. Najväčší `1e-5 T_max` bol `0.240017`, najhoršie aktívne bodové relatívne `00` rezíduum `4.41484e-8` a tri q=300 konvergenčné rozdiely boli `2.10624e-8`, `7.02159e-8`, `1.99290e-6`. K4 transfer bol pri `q=30,300,1000` menší než nulový limit. Nijaký timeout ani nový dôvod smrti nevznikol.

Podrobný rozsudok: `Audit/A2_K4_2_HIGH_K_SUBHORIZONTOVY_AUDIT_A_ROZSUDOK.md`. Ďalšia brána je K4.3.

