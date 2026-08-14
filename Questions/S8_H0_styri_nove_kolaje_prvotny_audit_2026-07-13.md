# Problém S8–H0: štyri nové koľaje a ich prvotný audit

**Dátum:** 2026-07-13  
**Vetva:** kozmologické perturbácie a geometria  
**Cieľ:** preveriť štyri navrhnuté mechanizmy skôr, než sa niektorý z nich zapíše ako predikcia v3.18.

## 1. Spoločná brána vetvy

Žiadna z koľají zatiaľ nesmie používať formuláciu „posunie S8 na 0,82“ alebo „posunie H0 na 67,8“ ako výsledok teórie. Na taký verdikt treba:

1. covariantné rovnice pozadia a perturbácií;
2. špecifikované počiatočné podmienky a všetky prenášané zložky energie/hybnosti;
3. stabilitu bez ghostov a gradientových nestabilít;
4. implementáciu v CLASS/CAMB alebo ekvivalentnom Boltzmannovom riešiči;
5. spoločnú likelihood CMB + BAO + SN + lensing/LSS;
6. porovnanie informačným kritériom alebo Bayesovým faktorom, nie iba trafenie centrálnej hodnoty.

Prvotný výpočet je uložený v `scripts/16_script_S8_H0_four_tracks_screening.py`.

## 2. Stav koľají

| Koľaj | Hypotéza | Stav | Prvý verdikt |
|---|---|---|---|
| K1 | Čistý prenos hybnosti / trenie popola | **PREŽÍVA; najvyššia priorita** | Znamienko potlačenia rastu funguje, ale navrhnutá rovnica má trenie zapísané s opačným znamienkom. Presná hodnota S8 nebola odvodená. |
| K2 | Rozpadajúci sa popol | **PREŽÍVA S VYSOKÝM RIZIKOM** | Mechanizmus môže znížiť rast, ale `τ = 50–100 Gyr` znamená veľký rozpadový podiel a mení aj pozadie. Zvýšenie H0 nie je automatické. |
| K3 | Vyššie rané `g*` zvýši `ΔN_eff` | **MŔTVA V UVEDENEJ PODOBE** | Pre tú istú skoro odpojenú ľahkú zložku vyššie viditeľné `g*` znižuje jej teplotu a `ΔN_eff`, teda má opačné znamienko. |
| K3b | Viac tmavých relativistických stupňov alebo neskorý ohrev pary | **NOVÁ NÁHRADNÁ KOĽAJ; NEOVERENÁ** | Môže zvýšiť `ΔN_eff`, ale je to iný mechanizmus než iba vyššie SM `g*`. |
| K4 | Nenulová makroskopická krivosť | **PREŽÍVA AKO FENOMENOLÓGIA; NA STENE ODVODENIA** | `ΩK = 0,002` nie je odvodené z Delaunayovej neusporiadanosti a v jednoduchom teste je geometrický efekt príliš malý na deklarovaný posun H0. |

## 3. K1 — negeodetický prenos hybnosti

### 3.1 Oprava znamienka

Pri deriváciách podľa `ln a` má štandardný rastový tvar

$$
D''+\left(2+\frac{H'}{H}+A\right)D'
-\frac{3}{2}\Omega_m(a)D=0.
$$

Pre `A > 0` ide o trenie a rast sa tlmí. Člen `-\tilde\gamma` v koeficiente pri `D'` by bol antitrenie a rast by zosilnil.

Toy-model s konštantným trením zapnutým od `a = 0,5` našiel:

- potrebný pomer amplitúd `0,815 / 0,874 = 0,932494`;
- približné `A = 0,7081` pre tento konkrétny toy model;
- so správnym `+A` sa dosiahne pomer `0,932494`;
- s rovnakým členom ako `-A` rastie amplitúda na pomer `1,08994`.

Hodnota `0,7081` **nie je fit kozmologického modelu**. Závisí od zvoleného času zapnutia a zanedbáva škálovú závislosť, rýchlosti ostatných tekutín a CMB.

### 3.2 Podmienky fyzikálnej konzistencie

Čistý prenos hybnosti môže v covariantnom modeli ponechať homogénne pozadie bez výmeny energie, ale treba definovať štvorvektor `Q^μ` tak, aby v určenom rámci platilo `u_μ Q^μ = 0`, a zároveň zachovať celkovú konzerváciu `Σ_i Q_i^μ = 0`.

„Gravitačný ťah siete“ nestačí, lebo obyčajná gravitácia vedie k geodetickému pohybu. Negeodetická sila musí mať partnera, mediátor alebo explicitnú väzbu na stav siete. Treba určiť, kam odchádza odovzdaná hybnosť.

Existujú fyzikálne modely čistého prenosu hybnosti bez zmeny pozadia, ale ich potlačenie `σ8` môže saturovať a vyžaduje plnú Boltzmannovu implementáciu; pozri [symmetry-protected momentum exchange, 2026](https://arxiv.org/abs/2603.07879). To je analóg, nie dôkaz pre bunkový model.

### 3.3 Testy K1

- K1-T1: covariantná celková konzervácia;
- K1-T2: správne znamienko a nezáporná produkcia entropie;
- K1-T3: žiadne superluminálne módy, ghosty ani gradientové nestability;
- K1-T4: konzistentné Eulerove rovnice popola, pary a baryónov;
- K1-T5: CLASS/CAMB a spoločný fit S8/H0/CMB/BAO.

**Stav:** prežíva a ide prvá. Stojí však pred mikrofyzikálnou stenou, nie pred numerickou stenou.

## 4. K2 — rozpadajúci sa popol

Pre vopred existujúcu zložku je rozpadový podiel za `t0 = 13,8 Gyr`

$$
f_{\rm dec}=1-e^{-t_0/\tau}.
$$

Výsledky:

| `τ` | Rozpadnutý podiel za 13,8 Gyr |
|---:|---:|
| 50 Gyr | 24,12 % |
| 100 Gyr | 12,89 % |
| 137 Gyr | 9,58 % |
| 220 Gyr | 6,08 % |

Rozsah `50–100 Gyr` teda nie je nepatrná oprava, ak sa rozpadá všetok popol. V bunkovom modeli navyše popol priebežne vzniká. Minimálne pozadie musí mať tvar

$$
\dot\rho_Q+3H\rho_Q=S_Q-\Gamma_d\rho_Q,
$$

$$
\dot\rho_{dr}+4H\rho_{dr}=f_{dr}\Gamma_d\rho_Q,
$$

plus rovnicu pre prípadnú masívnu dcérsku zložku. Treba určiť rozvetvenie, hmotnosti dcér, ich voľný tok a perturbácie.

Publikované analýzy ukazujú, že DDM môže v niektorých dátových kombináciách zmierniť S8, ale nie je všeobecným riešením oboch napätí. Jedna analýza našla preferované životnosti približne `137–220 Gyr` podľa dcérskych produktov ([Tanimura et al.](https://arxiv.org/abs/2301.03939)); širšia štúdia dospela k negatívnejšiemu záveru pre spoločné H0 a σ8 ([Davari & Khosravi](https://arxiv.org/abs/2203.09439)).

**Stav:** koľaj prežíva, ale nesmie sa zapísať pevné `τ = 50–100 Gyr` ani sľub zvýšenia H0 bez likelihood. Ide druhá po K1.

## 5. K3 — zvýšenie raného g*

Pre tú istú ľahkú zložku, ktorá sa odpojila pri `g* = g*dec`, platí štandardné entropické škálovanie

$$
\Delta N_{\rm eff}\propto T_x^4
\propto g_{*s,\rm dec}^{-4/3}.
$$

Pri zachovaní normalizácie `ΔNeff = 0,0535` pre `g* = 106,75` dá zvýšenie viditeľných stupňov voľnosti:

| `g*` | `ΔNeff` tej istej odpojenej zložky |
|---:|---:|
| 106,75 | 0,0535 |
| 150 | 0,03399 |
| 200 | 0,02316 |
| 300 | 0,01349 |

Na `0,15–0,20` by v tom istom škálovaní bolo potrebné efektívne `g* ≈ 49,3–39,7`, teda menšie, nie väčšie. Fyzikou ľahkých reliktov a entropického zriedenia sa podrobne zaoberá [The Physics of Light Relics](https://arxiv.org/abs/2203.07943).

Vyššie rané SM/SUSY `g*` môže zvýšiť celkovú energiu **kým sú stavy relativistické**, ale ak neskôr anihilujú do viditeľného kúpeľa po odpojení pary, paru relatívne ochladia. Pôvodný mechanizmus má preto opačné znamienko.

### Náhradná koľaj K3b

Vetva sa dá zachrániť iba zmenou mechanizmu, napríklad:

- pridaním ďalších stabilných tmavých relativistických stupňov;
- neskorým selektívnym ohrevom pary po jej odpojení;
- ne-termálnou produkciou pary.

Každá možnosť musí prejsť BBN, CMB, voľným tokom a fázovým posunom akustických píkov. Planck+BAO uvádza `Neff = 2,99 ± 0,17` v rozšírenom modeli ([Planck 2018 VI](https://arxiv.org/abs/1807.06209)); presné obmedzenie bunkovej verzie však vyžaduje vlastný fit.

**Stav:** pôvodná K3 je mŕtva. K3b je nová, zatiaľ neoverená koľaj a nesmie sa vydávať za tú istú hypotézu.

## 6. K4 — topologická krivosť

Otvorený FLRW priestor má pri bežnej konvencii `ΩK > 0`. Samotná náhodnosť Delaunayovho grafu však neimplikuje nenulovú makroskopickú krivosť. Delaunayova triangulácia bodov vložených do euklidovského priestoru môže byť lokálne neusporiadaná a pritom mať nulovú priemernú FLRW krivosť.

Na odvodenie treba diskrétnu metriku a napríklad Reggeho deficitné uhly alebo jasne definovanú grafovú Ricciho krivosť, potom koarse-graining a limit s rastúcim N.

Prvotný FLRW test pri pevných hustotách a `z* = 1089,92` dal:

- `ΩK = 0,002` zväčší bezrozmernú priečnu vzdialenosť iba faktorom `1,002753`, teda o `0,275 %`;
- deklarovaný posun `66,4 → 67,5` je pomer `1,016566`, teda `1,657 %`;
- v tomto obmedzenom teste by rovnaký geometrický účinok vyžadoval `ΩK ≈ 0,01206`.

Toto nie je CMB+BAO fit, ale stačí na vyvrátenie tvrdenia, že deklarovaný posun H0 už bol z `ΩK = 0,002` vypočítaný. Pre porovnanie Planck+BAO dáva `ΩK = 0,0007 ± 0,0019` ([Planck 2018 VI](https://arxiv.org/abs/1807.06209)); preto veľkosť okolo `0,012` nie je bezproblémová.

**Stav:** fenomenologická K4 prežíva, ale odvodenie zo siete a deklarovaný posun H0 neprešli. Po K1 a K2 má nižšiu prioritu.

## 7. Rozhodnutie vetvy

Poradie ďalšieho hlbokého testovania:

1. **K1 — čistý prenos hybnosti**, po oprave znamienka a zapísaní covariantného `Q^μ`;
2. **K2 — DDM**, so zdrojom nového popola a explicitnými dcérami;
3. **K4 — krivosť**, až po nezávislom meraní diskrétnej krivosti siete;
4. **K3b — tmavé relikty/ohrev**, iba ak vznikne mikrofyzikálny dôvod.

Pôvodná K3 zomrela. Vetva S8/H0 žije, lebo K1, K2, K4 a nová K3b ešte nenarazili na definitívnu experimentálnu alebo matematickú stenu.

## 8. Ďalší konkrétny krok K1

Založiť rovnice pre dve rýchlostné polia `θ_Q` a `θ_I/θ_v`, určiť covariantný prenos

$$
Q_Q^\mu = A(a,k)\rho_Q\,h^{\mu}{}_{\nu}(u_I^\nu-u_Q^\nu),
\qquad Q_I^\mu=-Q_Q^\mu,
$$

a preveriť, či doména I vôbec môže niesť protihybnosť bez zavedenia zakázanej novej dynamickej zložky. Až potom má zmysel vyberať veľkosť trenia podľa S8.

