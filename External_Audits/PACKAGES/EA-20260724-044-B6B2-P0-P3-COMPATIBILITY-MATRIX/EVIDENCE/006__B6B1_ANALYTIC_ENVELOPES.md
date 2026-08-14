# B6b-1 — analytické background/source-moment obálky MF1–MF4

**Task:** `A2K4-B6B1-ANALYTIC-ENVELOPES-20260723-47`  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> S-M/Q18/Q22 -> SM_v1 -> V1-D03 -> B6b-1`  
**Autor teórie a fyzikálneho smeru:** Martin Jambor  
**Tvorca pracovného analytického artefaktu:** Codex, hlavný orchestrátor  
**Stav:** `DRAFT_FOR_INDEPENDENT_PHYSICS_AUDIT / NO_VERDICT / NO_PYTHON`  
**Dátum:** 2026-07-23

## 1. Cieľ a hranica kroku

B6b-0 vytvoril štyri rovnocenné otvorené rodiny `MF1–MF4`. B6b-1 nemá
vybrať víťaza ani odvodiť detailnú mikrofyziku. Má pre každú rodinu zapísať
rovnaký minimálny analytický obal, ktorý umožní v ďalšom kroku rozhodnúť:

1. ktoré veličiny sú spoločné a odvodené;
2. ktoré veličiny zostávajú otvoreným fyzikálnym vstupom;
3. aké nerovnosti a recovery limity musí každý mechanizmus splniť;
4. či niektorá rodina už na tejto hĺbke tvorí prázdnu behaviorálnu množinu.

Tento krok nepoužíva číselný interval `S8`, nespúšťa perturbácie a nemení
`D03`, K4 ani P5. Jeho výstupom je ohraničený priestor funkcií, nie jedna
presná funkcia trávenia.

## 2. Autorovo spresnenie úlohy pozorovaní

Autor teórie určil, že približne známe pozorované pásmo `S8` sa smie použiť
ako mantinel pri hľadaní množiny prípustných funkcií. Taký krok je platná
**inverzná feasibility/kalibrácia**, nie nezávislá predikcia.

Rozlišujeme preto:

```text
S8_CALIBRATION_USE
  = povolené filtrovanie vopred definovaných rodín a parametrov
    proti vopred zmrazenému dátovému pásmu;

S8_POST_HOC_SHAPE_CHANGE
  = zakázané pridanie novej funkčnej voľnosti, switchu alebo parametra
    až po prezretí nevyhovujúceho modelového výsledku;

S8_CONFIRMATION_STATUS
  = NOT_INDEPENDENT, ak ten istý S8 passport vstúpil do kalibrácie.
```

Ak bude `S8` použitý na vytvorenie množiny kandidátov, nezávislý holdout
musí pochádzať z observably, dátovej časti, mierky alebo epochy, ktorá do
výberu nevstúpila. Split sa zmrazí pred výpočtom, musí explicitne zohľadniť
spoločnú covariance a systematiky a nesmie mať informačný leakage. Iný názov,
mierka, epocha alebo subset samy osebe nezaručujú nezávislosť. Presný
passport, interval, confidence level a rozdelenie kalibrácia/holdout patria
až do B6b-2. Toto spresnenie nerobí `S8` lokálnou stavovou premennou a
nepovoľuje switch podľa kozmického času alebo želaného výsledku.

## 3. Spoločný analytický passport

Nech `dR_D(p|x)` je nezáporná označená miera parent udalostí na jednotku
vlastného objemu a vlastného času, `E_J(p,x)>=0` energia jednej udalosti a
`0 <= beta_s(p,x) <= 1` jej prompt steam podiel. Pre `n in N_0` definujeme

```text
R_D(x)       = integral dR_D(p|x),
J_n,D(x)     = integral E_J(p,x)^n dR_D(p|x),
J_0,D(x)     = R_D(x),
Q_D(x)       = J_1,D(x),
Q_s(x)       = integral beta_s(p,x) E_J(p,x) dR_D(p|x),
Q_M,birth(x) = Q_D(x) - Q_s(x).
```

Bez voľby rodiny presne platí

```text
R_D >= 0,
J_n,D >= 0,
0 <= Q_s <= Q_D,
0 <= Q_M,birth <= Q_D,
Q_s + Q_M,birth = Q_D.
```

Konečnosť každého použitého `J_n,D` sa musí dokázať osobitne; nezápornosť
neimplikuje konečnosť. Ak `R_D>0` a druhý energetický moment je konečný,
Cauchyho nerovnosť dáva

```text
Q_D^2 <= R_D J_2,D,
Var_R(E_J) = J_2,D/R_D - (Q_D/R_D)^2 >= 0.
```

Táto nerovnosť oddeľuje mieru udalostí od energie udalosti. Rovnaký
background `Q_D` môže vzniknúť z mnohých slabých alebo z mála silných
udalostí, ale ich šum a vyššie momenty nemusia byť rovnaké.

Completion tok je backlogový lokálny tok

```text
Q_M_to_C >= 0,
Q_M_to_C = integral E_M(p,x) dR_C(p|x),
```

a nemusí byť bodovo menší než súčasný `Q_D`, pretože môže dokončovať skôr
narodené kohorty. Musí však byť krytý existujúcou energiou hmotného
rezervoára, zachovať `rho_M>=0` a pri `rho_M=0` musí byť nulový. Pre studený
`M` dáva cohort-resolved balance nutnú kumulatívnu podmienku

```text
integral_[t_i,t] a^3 Q_M_to_C dt'
  <= a_i^3 rho_M(t_i)
     + integral_[t_i,t] a^3 Q_M,birth dt'.
```

Pri `p_M!=0` sa musí v integračnom faktore zachovať aj pracovný/tlakový člen;
studená nerovnosť sa na taký sektor nesmie použiť bez úpravy.

### 3.1 Background obálka

V konvencii `x=ln(a)` platí pre paru

```text
d rho_s/dx + 4 rho_s = S_s(x),
S_s(x) = Q_s(x)/H(x).
```

Pre `H>0` je preto exact integračný tvar

```text
a^4 rho_s(a)
  = a_i^4 rho_s(a_i)
    + integral_[x_i,x] exp(4x') S_s(x') dx'.
```

Z `Q_s>=0` vyplýva, že počas parent source je `a^4 rho_s` neznižujúce.
Po source-off je konštantné. Integrovaný steam budget teda závisí od celej
histórie `Q_s/H`, nie iba od okamžitej hodnoty source.

Spoločný background ledger zostáva

```text
-Q_D + Q_s + (Q_M,birth - Q_M_to_C) + Q_M_to_C = 0.
```

Ide o identitu vynútenú konštrukciou; sama nie je nezávislým testom.
Nezávislé testy musia kontrolovať kauzálnu dostupnosť energie, správny
rezervoár, source-off, stavové rovnice a perturbation momenty.

### 3.2 Minimálny source-moment obal

Každá rodina musí z tej istej označenej miery odvodiť aspoň:

```text
M0: event rate R_D,
M1: energy transfer Q_A a four-vector Q_A^mu,
M2: pressure/stress, recoil covariance a energy variance,
Mdelta: delta Q_A a momentum-transfer response,
Mnoise: spoločný source-noise/cross-power passport P_AB(k).
```

Povinné guards:

- `sum_A Q_A^mu=0` na každom vertexe aj po priemerovaní;
- event-wise `sum_A Delta p_A^mu(p)=0` a z toho odvodené null smery
  `sum_A P_AB^{mu nu}(k)=0` aj `sum_B P_AB^{mu nu}(k)=0`;
- `P_AB` je pozitívne semidefinitná na fyzickom sektorovom priestore;
- kauzálny mark spĺňa príslušnú energy-momentum doménu a dostupný budget;
- pressure, shear a noise sa nevolia nezávisle od background kernelu;
- cross-channel korelácie sa nesmú automaticky nastaviť na nulu;
- Poissonovský šum sa nesmie predpokladať bez odvodenia event procesu;
- source-off ruší všetky energy-momentum-weighted parent source momenty
  `M1–Mnoise`; samotné `M0=R_D` môže zostať nenulové iba ako explicitná
  miera nulovoenergetických opportunities, ktoré nevytvárajú fyzický source
  ani energy-momentum source noise; completion kohorty môžu iba dobehnúť;
- neskorý A1 `F -> C` používa odlišný rezervoár a nepridáva steam.

## 4. Rodinné obálky na rovnakej hĺbke

### 4.1 MF1_DIVISION_LOCKED

```text
dR_D = p_D(Y_local) dR_div Pi_D(dp,dmarks|Y_local),
0 <= p_D <= 1,
0 <= R_D <= R_div.
```

Tu je `p_D=dR_D/dR_div` Radonov–Nikodýmov thinning weight/submeasure na
supporte division opportunities, nie nový voľný fitovací zákon.

Ak existuje konečný lokálny event-energy strop `E_max`, potom

```text
0 <= J_n,D <= R_div E_max^n.
```

Ak `E_max` nie je odvodený, stav je explicitne
`MF1_MOMENT_UPPER_BOUND_OPEN`.

Otvorené zostávajú `R_div`, podmienka `p_D`, energia/marky a steam podiel.
Rodina zomrie až vtedy, ak auditovaný division budget nemôže v celom scope
vytvoriť požadovaný integrovaný source ani pri dovolených horných hraniciach.
Samotná neznalosť mikroskopického počtu delení nie je STOP.

### 4.2 MF2_INTERNAL_CLOCK

```text
R_D = integral dY f_act(Y;x) Gamma_int(Y)
```

alebo ekvivalentná lokálna first-passage flux, pričom

```text
f_act(Y;x) >= 0,
n_act(x) = integral dY f_act(Y;x),
Gamma_min <= Gamma_int(Y) <= Gamma_max  na supporte f_act.
```

Ak sú na zvolenom scope odvodené konečné hranice, platí

```text
n_act Gamma_min <= R_D <= n_act Gamma_max.
```

Ak navyše `E_J<=E_max`, rovnaká hĺbka momentového obalu dáva

```text
J_n,D <= n_act Gamma_max E_max^n.
```

Bez odvodeného `E_max` je stav `MF2_MOMENT_UPPER_BOUND_OPEN`.

PH1 je iba podmienený kandidát na časť clock passportu. Neurčuje identitu
udalosti, `n_act`, event energy, steam marky ani completion. Rodina zostáva
otvorená, kým nie je odvodený lokálny clock/source-off a nepreukáže sa
nenulový kauzálny energetický svedok.

### 4.3 MF3_STATE_SWITCHED_HYBRID

Pri jednom spoločnom opportunity measure sa smie analytický obal zapísať

```text
dR_D = w(z(Y_local)) dR_1 + [1-w(z(Y_local))] dR_2,
0 <= w <= 1.
```

Každý moment je potom lineárnym obrazom týchto dvoch stavovo označených
mier. Ak opportunity measures nie sú spoločné, bezpečný horný obal je súčet,
nie automaticky konvexný priemer:

```text
J_n,D
  = integral w(Y) dJ_n,1(Y)
    + integral [1-w(Y)] dJ_n,2(Y).
```

Tento tvar platí na spoločnom opportunity measure a s `w` chápaným pointwise
na lokálnom stave; iba pri konštantnom `w` na supporte sa smie vytknúť pred
integrál. Ak endpoint rate/energy bounds nie sú odvodené, stav je
`MF3_MOMENT_UPPER_BOUND_OPEN`.

Rodina je samostatná iba ak:

- oba limitné režimy sú fyzicky prítomné;
- `z`, prah a transition rule sú odvodené z lokálneho stavu;
- prechod zachová vertex ledger a nevytvorí delta-source bez partnera;
- tá istá udalosť sa nezapočíta v oboch režimoch.

Switch pridaný až podľa nevyhovujúceho `S8` výsledku je post-hoc rozšírenie
rodiny a nesmie sa započítať do toho istého testu.

### 4.4 MF4_PARALLEL_CONSERVATIVE_CHANNELS

```text
dR_D = sum_r dR_D,r,
J_n,D = sum_r J_n,D,r,
Q_A^mu = sum_r Q_A,r^mu.
```

Ak má každý kanál odvodené `R_max,r` a `E_max,r`, potom

```text
J_n,D <= sum_r R_max,r E_max,r^n,
```

pričom celkový source musí navyše prejsť spoločným reservoir capom. Bez
týchto hraníc je stav `MF4_MOMENT_UPPER_BOUND_OPEN`.

Pri spoločnom rezervoári sa zavedú nezáporné alokačné podiely `f_r` s
`sum_r f_r<=1`; pri odlišných rezervoároch musí mať každý kanál vlastný
ledger. Event/cohort labels musia byť disjunktné. Druhé momenty a noise
obsahujú aj cross-channel kovariancie, pokiaľ ich nezávislosť nebola
odvodená.

MF4 je neprázdna iba pri aspoň dvoch súčasne nenulových rozlíšiteľných
kanáloch s platným spoločným ledgerom. Ak prežije iba jeden kanál, kandidát
sa reklasifikuje na príslušnú jednoduchšiu rodinu. MF4 je prázdna v scope,
ak nemožno zostaviť takýto najmenej dvojkanálový súčet bez porušenia
rezervoára alebo dvojitého započítania.

## 5. Equal-depth porovnanie a otvorené vstupy

| Rodina | Čo ohraničuje event rate | Špecifický guard | Najbližší chýbajúci vstup | Stav pred auditom |
|---|---|---|---|---|
| MF1 | `0<=R_D<=R_div` | event iba v division opportunity | auditovaný `R_div` a event-energy budget | `OPEN` |
| MF2 | `R_D=integral f_act Gamma_int` | lokálny first-passage a source-off | `n_act`, clock a event identity | `OPEN` |
| MF3 | stavovo označená kombinácia limitov | odvodený switch, bez double-count | lokálny diskriminátor a transition ledger | `OPEN` |
| MF4 | aditívny súčet kanálov | reservoir allocation a cross-noise | počet/identita kanálov a ich ledgers | `OPEN` |

Na tejto hĺbke nie je dostupný univerzálny argument, ktorý by ktorúkoľvek
rodinu vyradil. Neexistuje ani nenulový plný svedok s uzavretými `M0–Mnoise`.
Preto sa nesmie vydať `BEHAVIORAL_EMPTY_SCOPE`, fyzikálny PASS ani výber
rodiny. Informačný zisk B6b-1 je v explicitných inequalities a v presnom
zozname chýbajúcich vstupov.

## 6. Opravený workflow kalibrácie a holdoutu

```text
B6b-1  spoločné a rodinné analytické obálky
  -> B6b-2  perturbation-sign/moment passport
              + exact S8 dátový passport
              + vopred určený parameter/function search space
              + oddelenie calibration a holdout informácie
      -> B6b-3a  forward výpočet každého vopred prípustného kandidáta
                  + inverse výber množiny kompatibilnej so S8 pásmom
                  = FEASIBILITY/CALIBRATION, nie nezávislé potvrdenie
          -> freeze preživšej množiny
              -> B6b-3b  covariance-aware nezávislý holdout bez leakage
                          na nepoužitej observably alebo informácii
                  -> detailná mikrofyzika iba pre preživšie triedy.
```

Ak po B6b-3a zostane viac funkcií, všetky sa zachovajú. Vyberá ich až
rozlišovací holdout, fyzikálna jednoduchosť a ďalšie nezávislé dôsledky.
Ak nezostane žiadna, vzniká observačný STOP iba pre úplne pokrytý a vopred
zmrazený search space; nie univerzálny dôkaz, že nijaká funkcia neexistuje.

## 7. Predregistrované auditné otázky

1. Sú spoločné nerovnosti skutočne odvodené z označenej event measure?
2. Nezamieňa sa completion backlog s okamžitým parent tokom?
3. Sú MF1–MF4 porovnané na rovnakej hĺbke bez skrytého výberu PH1?
4. Je rozdiel medzi S8 kalibráciou a nezávislým potvrdením explicitný?
5. Nevkladá dokument nový fyzikálny parameter, switch alebo event energy?
6. Je správne, že všetky štyri rodiny zostávajú `OPEN`?
7. Je navrhnutý B6b-2 najmenší krok schopný zúžiť množinu?

## 8. Nonclaims a návrh handoffu

```text
B6B1_STATUS = DRAFT_ANALYTIC_ENVELOPE_CONTRACT
MF1 = OPEN
MF2 = OPEN
MF3 = OPEN
MF4 = OPEN
S8_ROLE = CALIBRATION_BAND_ALLOWED_WITH_NONINDEPENDENT_LABEL
S8_NUMERICAL_PASSPORT = NOT_YET_FROZEN
INDEPENDENT_HOLDOUT = NOT_YET_SELECTED
V1_D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
D04_D11 = BLOCKED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
PYTHON = NOT_RUN
```

Odporúčaný nasledujúci krok je nezávislý read-only fyzikálny audit tohto
kontraktu. Až jeho prijatie hlavným orchestrátorom môže uzavrieť B6b-1 ako
obálkový contract a otvoriť B6b-2; nemôže samo zvýšiť K4 ani vybrať rodinu.
