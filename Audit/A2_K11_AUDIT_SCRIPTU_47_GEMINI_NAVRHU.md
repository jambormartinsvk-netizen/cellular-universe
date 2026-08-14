# A2-K11 — audit skriptu 47 a návrhu predloženého cez Gemini

**Dátum:** 2026-07-14  
**Auditovaný súbor:**
`scripts/47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py`  
**SHA-256 skriptu 47:**
`3CFFD6E9977BD8A4619362BBD0BDDCC2436BBEF468EC47B00DADD8F6F0E056BC`  
**Rozsudok vytlačeného PASS:** **`ZAMIETNUTÝ — NEPLATNÝ FYZIKÁLNY A
CONSTRAINTOVÝ DÔKAZ`**  
**Klasifikácia:** nejde o novú koľaj; je to ďalšia implementácia existujúcej
A2-K11  
**Kanonický stav A2-K11:** **`PREŽÍVA IBA FORMULAČNÚ BRÁNU — 15/100`**

## 1. Stručný výsledok

Skript 47 sa podarilo reprodukovať a jeho numerický beh je rýchly. To však
neoveruje správnosť rovníc. Audit našiel päť nezávislých rozhodujúcich chýb:

1. koeficient `-(4-3 delta)` patrí barotropickému uzáveru `c_s^2=w`, ale
   skript ho kombinuje s tlakovým členom uzáveru `c_s^2=1`;
2. konštantné proper-time sadzby sú nesprávne delené `aE` namiesto `E`, čím
   je interakcia pri štarte umelo zosilnená faktorom `1090.9`;
3. energetický tok `Q_c^mu || u_c^mu` je nesprávne vložený ako sila do CDM
   Eulerovej rovnice a fuel recoil má nesprávne znamienko aj tvar;
4. fuel kontinuita nie je úplná a CDM kontinuita stále nemá metrický člen
   `+Psi`;
5. znamienka `0i` a `00` constraintu sú v deklarovanej konvencii obrátené a
   bodové relatívne `00` rezíduum je pri veľkej amplitúde prakticky `1.0`.

Preto extrémne tlmenie `~1.4e-20` nie je výsledkom auditovaného kovariantného
modelu. Je výsledkom inej, fyzikálne neuzavretej ODE sústavy s umelo veľkou
ranou interakčnou sadzbou.

## 2. Reprodukcia predloženého výstupu

Príkaz

```powershell
python scripts\47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py
```

skončil s návratovým kódom nula a vytlačil
`PASS_RIGOROUS_S8_K1b_AUDIT`. Na tomto stroji trval približne `16.5 s`.

| Amplitúda | Transfer | Max. absolútne rezíduum | Konečné bodové relatívne rezíduum |
|---:|---:|---:|---:|
| `1` | `2.9220968893e-20` | `3.8566042203e-14` | `0.5186005312` |
| `1e6` | `1.4124826676e-20` | `3.8566037041e-8` | `0.999999999871` |
| `1e8` | `1.4124483853e-20` | `3.8566042116e-6` | `0.999999999871` |

Čísla z návrhu sú teda reprodukované. Ich interpretácia ako fyzikálny PASS
však neprešla auditom.

## 3. Eulerov koeficient: oprava je v skutočnosti nekonzistentný hybrid

Deklarované konvencie sú

```text
x = ln a,
u_A = H0 theta_A/k^2,
w_f = -1+delta,
delta = 0.02297,
c_s,f^2 = 1.
```

Pre constant-`w` tekutinu s pokojovou zvukovou rýchlosťou `c_s^2=1` má
neinteragujúca Eulerova časť tvar

```text
theta_f' - 2 H_conformal theta_f
- k^2 delta_f/delta - k^2 Psi = 0,
```

čiže po prechode na `x`:

```text
u_f,x = +2 u_f + (delta_f/delta + Psi)/(aE).
```

Skript 47 namiesto toho používa

```text
u_f,x = -(4-3 delta)u_f
        + (delta_f/delta+Psi)/(aE) + ...
```

Pre `delta=0.02297`:

```text
správny koeficient pre c_s^2=1 = +2,
skript 47                         = -3.93109.
```

Číslo `-(4-3 delta)=-(1-3w)` je koeficient barotropického uzáveru
`c_s^2=w`. V tom istom uzávere by však tlakový koeficient nebol `1/delta`,
ale

```text
w/delta = -42.5350457,
```

zatiaľ čo skript používa

```text
1/delta = +43.5350457.
```

Skript teda spája expanzné trenie barotropickej tekutiny s tlakom
nebarotropickej `c_s^2=1` tekutiny. Citácia Malik–Wands takúto kombináciu
nepredpisuje. Explicitná rovnica (35) Clemson et al. má pri `c_s^2=1`
koeficient `-2 H_conformal` na ľavej strane, teda `+2u_f` v `x` rovnici.

## 4. Chybný faktor `1/a` vytvára umelé rané tlmenie

Pri konštantnej proper-time sadzbe

```text
Gamma = lambda H0
```

je konformný interakčný člen `a Gamma`. Keď sa rovnica delí

```text
H_conformal = a H0 E,
```

faktor `a` sa zruší:

```text
a Gamma/H_conformal = lambda/E.
```

Skript 47 používa `lambda/(aE)`. Pri štarte `a=0.0009166743` je jeho sadzba
väčšia než správna proper-time sadzba faktorom

```text
1/a = 1090.9.
```

Skript 68 vypočítal v tom istom bode

```text
skript 47: lambda/(aE) = 6.9353465e-3,
správne:   lambda/E    = 6.3574539e-6.
```

Toto nie je malá numerická korekcia. Je to zmena fyzikálneho modelu a hlavný
zdroj deklarovaného extrémneho tlmenia.

## 5. Energetický tok a drag nie sú správne oddelené

K11 deklaruje

```text
Q_c^mu = Gamma rho_f u_c^mu + F_c^mu,
u_c,mu F_c^mu = 0.
```

Energetická časť rovnobežná s `u_c` nesmie dať CDM Eulerovu silu. Skript 47
ju napriek tomu vkladá do `G_c` a vytvára koeficient

```text
-lambda rho_f/(rho_c aE)
```

pri `u_c`; správny koeficient energetickej časti je nula.

Fuel energy-recoil mapa pre koeficienty `[u_c,u_f]` má byť

```text
lambda/(delta E) [-1,+2].
```

Skript 47 používa

```text
lambda/(delta aE) [+1,-1].
```

V štartovom bode skript 68 dostal

```text
skript 47: [+0.30193063,-0.30193063],
správne:   [-0.000276772,+0.000553544].
```

Nesedí faktor, znamienko ani pomer oboch zložiek.

## 6. Kontinuity zostali neúplné

CDM kontinuita musí pre deklarovaný constant-rate tok obsahovať

```text
(lambda/E)(rho_f/rho_c)(delta_f-delta_c+Psi).
```

Skript 47 vynecháva `+Psi`.

Fuel kontinuita nie je symetrický člen
`-(lambda/E)(delta_f-delta_c)`. Pri `c_s^2=1` obsahuje aj:

- `-3(1-w_f)delta_f`;
- neadiabatický velocity/sound-speed člen;
- metrický zdroj `-(lambda/E)Psi`;
- velocity-transfer člen úmerný `a lambda(1-w_f)u_f`.

Relatívny rozdiel koeficientovej mapy skriptu 47 a kanonickej K1 mapy je
`0.9999996673`. Oprava samotného tlakového delenia `delta_f/delta` preto
rovnice neuzatvára.

## 7. Einsteinove constrainty neprešli

V deklarovanej metrike a konvencii `theta_A=-k^2v_A` platí

```text
Phi_x = -Phi + (3a/2E) sum_A X_A(1+w_A)u_A,

q^2 Phi + 3(aE)^2(Phi_x+Phi)
+ 1.5 a^2 delta_rho_T = 0.
```

Skript 47 zmenil obe zdrojové znamienka na mínus. Tým sa neopravil starý
constraint; implementovala sa iná znamienková sústava odporujúca zafixovanej
definícii `theta`.

Rozhodujúca je však aj vlastná diagnostika skriptu 47. Pri `A=1e6` a `1e8`
vytlačil

```text
final_relative_residual = 0.999999999871.
```

To znamená približne stopercentnú chybu voči norme constraintových členov,
nie splnenie na strojový šum.

Navyše

```text
max_res/A = 3.8566e-14
```

je rovnaké pre všetky amplitúdy. Absolútne rezíduum preto rastie lineárne so
stavom. Keby išlo o amplitúdovo nezávislú numerickú podlahu, absolútne
rezíduum by pri zmene `A` o osem rádov zostalo približne konštantné a
`max_res/A` by kleslo.

## 8. Čo amplitúdový test skutočne dokazuje

Skript 68 priamo overil

```text
RHS(alpha y) = alpha RHS(y)
```

s relatívnym rezíduom `2.20e-16`. Implementovaný systém je homogénna
lineárna ODE. Takýto systém musí pri dostatočnom numerickom rozlíšení škálovať
lineárne s počiatočnou amplitúdou, aj keď má nesprávne rovnice.

Zhoda transferov pre `A=1e6` a `A=1e8` na `2.43e-5` preto overuje iba
numerickú konzistenciu riešiča nad jeho podlahou. Neoveruje kovarianciu,
Bianchiho identity, správne constrainty ani stabilitu fyzikálneho modelu.

## 9. Interpolátor a výkon

Rýchly beh bol reprodukovaný. Optimalizácia interpolácie však nemá dôkazovú
váhu pre fyziku.

`FastInterpolator` používa while slučky a uložený index. Pri monotónnych
dopytoch môže mať amortizované takmer konštantné náklady, ale jeho najhoršia
zložitosť nie je striktne `O(1)` a implicitný Radau nemusí volať RHS v prísne
monotónnom poradí počas vnútorných iterácií. Implementácia sa vie posúvať aj
späť, takže audit nenašiel dôvod, prečo by sama menila výsledok. Tvrdenie o
zrýchlení je výkonové, nie fyzikálne.

Aktuálny skript vytlačil `139897` backgroundových bodov, nie `700000`.
Historický dvanásťminútový baseline nebol dodaný s hashom, preto sa jeho
presné zrýchlenie nedá spätne overiť.

## 10. Superhorizontová a S8 interpretácia

Ani po oprave vyššie uvedených rovníc by jeden kompenzovaný relatívny seed
neuzatváral stabilitu. Skript:

- začína pri `z_star=1089.9`, nie v asymptotickej hlbokej radiačnej ére;
- netvorí úplnú regulárnu adiabatickú a izokurvatúrnu bázu;
- nerobí high-k test;
- nepočíta `P(k)`, `sigma_8` ani `S8`.

Názov `S8_K1b` preto nie je výsledkom pre `S8`.

## 11. Rozsudok koľaje

```text
script47 PASS = ZAMIETNUTÝ — NEPLATNÝ DÔKAZ
A2-K11        = PREŽÍVA IBA FORMULAČNÚ BRÁNU — 15/100
M-015         = NEVYDANÁ
```

Skript 47 sa nemaže. Zostáva zachovaný spolu so svojimi výstupmi a dôvodmi
zamietnutia, aby sa táto kombinácia rovníc znovu nepredkladala ako oprava.

Nejde o novú koľaj, pretože nepredkladá nový lokálny operátor, stupeň
voľnosti ani symetriu. Je to numerická revízia toho istého K11 momentum-drag
ansatzu. Zamietnutie implementácie nezabíja celú K11; formulačná možnosť
ortogonálneho prenosu zostáva otvorená.

## 12. Čo by musela obsahovať platná K11.1

1. lokálny operátor alebo kolízny člen s pravidelným limitom `rho_f -> 0`;
2. jednotnú definíciu `Q_c^mu`, `F_c^mu`, metriku a `theta_A`;
3. úplné `delta Q`, kontinuity a Eulerove rovnice odvodené z jedného ledgeru;
4. sadzby `lambda/E` a `gamma/E` pre konštantné proper-time parametre;
5. analytickú propagáciu `00` a `0i` constraintov cez Bianchiho identity;
6. úplnú regulárnu počiatočnú bázu podľa AR28;
7. nulové limity `lambda`, `gamma`, `rho_f` a `delta`;
8. high-k stabilitu; až potom výpočet `P(k)` a `S8`.

Globálna priorita A2 programu sa nemení: najprv K4.2. K11.1 zostáva
zachovanou neskoršou otvorenou koľajou.

## 13. Reprodukčné artefakty

- `scripts/47_script_A2_K11_S8_K1b_fully_consistent_einstein_test.py`;
- `scripts/68_script_A2_K11_script47_physics_and_constraint_audit.py`;
- `scripts/OUTPUT_A2_K11_47_68.md`;
- `Audit/A2_K11_EVIDENCE_MANIFEST_SHA256.md`.

## 14. Primárne zdroje

- [Clemson et al., Interacting Dark Energy — constraints and degeneracies](https://arxiv.org/abs/1109.6234), najmä rovnice (32)–(35);
- [Malik & Wands, Adiabatic and entropy perturbations with interacting fluids and fields](https://arxiv.org/abs/astro-ph/0411703);
- [Malik & Wands, Cosmological perturbations](https://arxiv.org/abs/0809.4944);
- [Ma & Bertschinger, Cosmological Perturbation Theory in the Synchronous and Conformal Newtonian Gauges](https://arxiv.org/abs/astro-ph/9506072).

