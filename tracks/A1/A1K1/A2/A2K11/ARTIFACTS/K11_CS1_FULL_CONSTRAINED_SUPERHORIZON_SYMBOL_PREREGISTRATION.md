# K11-CS1 — predregistrácia úplného constrained superhorizontového symbolu

**Dátum zmrazenia:** 2026-07-16  
**Autorita:** hlavný orchestrátor  
**Stav pred behom:** `PREREGISTERED / NOT YET DECIDED`  
**Skórovací účinok pred výsledkom:** žiadny  
**Numerika:** v CS1 zakázaná; ide o analytický/DAE symbol a constraint audit

## 1. Rozhodovacia otázka

Má úplný lineárny superhorizontový systém s akceptovaným A1-K1 tokom

```text
Q_c^mu=Gamma rho_f u_c^mu+F_c^mu,
Q_f^mu=-Q_c^mu,
```

a regulárnym pasívnym K11 operátorom

```text
F_c^mu=Upsilon h_c^{mu nu}u_f,nu,
Upsilon=gamma_*(Y) rho_c(delta rho_f)/(rho_c+delta rho_f)
```

regulárnu constraint-compatible bázu bez fyzického rastúceho
superhorizontového módu pri `Gamma>0`, `delta=0.02297`?

CS1 nesmie odpovedať iba vlastnými číslami neuzavretej velocity podmatice.
Tá už má dokázaný saddle determinant, ale density, pressure, Hubble a metric
väzby môžu meniť celý constrained systém.

## 2. Nemenné rodičovské konvencie

- konformný Newtonov gauge
  `ds^2=a^2[-(1+2Psi)deta^2+(1-2Phi)dx^2]`;
- Fourier `nabla^2 -> -k^2`, `theta_A=-k^2v_A`;
- veľkoškálové premenné `V_A=theta_A/k^2`;
- `w_f=-1+delta`, `delta=0.02297`, `c_s,f^2=1`, `c_a,f^2=w_f`;
- `Gamma=lambda H0>0`, `lambda=0.15`;
- pressure conversion paliva sa preberá celý, vrátane velocity termu;
- reakcia dragu je presne `F_f=-F_c`;
- `Upsilon>=0`; záporné znamienko sa nesmie použiť na stabilizáciu;
- background A1 sa nemení, pretože `F_c=0` na FLRW.

Autoritatívne rovnice a znamienka sú v
`Audit/A2_1_linearne_perturbacie_Einsteinove_constrainty_a_superhorizontovy_test.md`.

## 3. Povinný dark-sector blok pri `k->0`

Definujme konformné sadzby

```text
A   = a Gamma rho_f/rho_c,
G   = a Gamma/delta,
A_c = a Upsilon/rho_c,
A_f = a Upsilon/(delta rho_f).
```

CS1 musí odvodiť, nie predpokladať, tieto limitné rovnice:

```text
delta_c' - 3Phi'
= A(delta_f-delta_c+Psi),

V_c' + Hc V_c - Psi
= A_c(V_f-V_c),

delta_f'
+3Hc(1-w_f)delta_f
+9Hc^2(1-w_f^2)V_f
-3delta Phi'
= -aGamma[Psi+3Hc(1-w_f)V_f],

V_f' -2Hc V_f -delta_f/delta-Psi
= G(2V_f-V_c)+A_f(V_c-V_f).
```

Každý rozdiel oproti týmto riadkom je `REVIEW`, kým nebude odvedený priamo
z toho istého `Q_A^mu`.

## 4. Povinný stavový priestor — zákaz neúplného päťstavového PASS

Minimálny dark blok je

```text
(delta_c,delta_f,V_c,V_f,Phi,Psi).
```

Sám osebe však nie je automaticky úplným fyzickým superhorizontovým
systémom. Einsteinove zdroje obsahujú všetky prítomné druhy:

```text
delta rho_total,
sum_A(rho_A+p_A)V_A,
delta p_total,
sum_A(rho_A+p_A)Sigma_A.
```

CS1 musí urobiť jedno z dvoch, bez tretej možnosti:

### CS1-FULL

Zahrnúť regulárny vedúci superhorizontový blok všetkých prítomných druhov
na auditovanom A1 backgrounde:

- baryóny;
- fotóny vrátane potrebného leading shear/polarization uzáveru;
- štandardné neutrína a každú decouplovanú parnú zložku vrátane leading
  scaled shear;
- metrické potenciály a prípadný slip.

Vyššie multipóly sa smú odstrániť iba rádovým dôkazom, že pri zvolenom
Frobeniovom ráde nevstupujú.

### CS1-COMP

Dokázať, že zvolená kompenzovaná dark-sector podmnožina s vynechanými
štandardnými perturbáciami je invariantná pod úplnými rovnicami, zachováva
`00`, `0i`, trace aj traceless constraint a nie je gauge mód.

Ak sa invariantnosť nedokáže, redukovaný dark-only symbol nemôže dostať
fyzický PASS ani STOP celej K11.

## 5. Constraintové holdouty

Nasledujúce identity sa nesmú použiť súčasne na definovanie a „overenie“
toho istého metrického riadku:

```text
00:
k^2Phi+3Hc(Phi'+HcPsi)=-4piGa^2 delta rho,

0i po vydelení k^2:
Phi'+HcPsi=4piGa^2 sum_A(rho_A+p_A)V_A,

trace:
Phi''+Hc(Psi'+2Phi')+(2Hc'+Hc^2)Psi
=4piGa^2 delta p              [k->0],

traceless/slip:
Phi-Psi=12piGa^2 sum_A(rho_A+p_A)Sigma_A.
```

Aspoň jeden nezávislý constraint musí zostať holdoutom a jeho propagácia sa
musí odvodiť z `sum_A Q_A^mu=0` a backgroundových rovníc.

## 6. Symbol a časová závislosť

Backgroundové koeficienty `Hc,A,G,A_c,A_f,rho_A` závisia od času. CS1
preto nesmie zameniť okamžité vlastné čísla `M(eta_0)` za globálne
evolučné exponenty.

Prípustné sú iba:

1. Frobeniov symbol v deklarovanom asymptotickom režime, kde majú
   koeficienty zmrazené vedúce mocniny;
2. presný lokálny principal/interaction symbol s výslovne obmedzeným
   rozsahom;
3. analytický invariant alebo Lyapunov/energy odhad platný na celom
   deklarovanom intervale.

Ak ani jeden z týchto objektov nemožno uzavrieť bez numerickej evolúcie,
výsledok CS1 je `UNDETERMINED_REVIEW` a musí presne určiť vstup pre budúci
ohraničený runner. Nesmie si vyrobiť konštantnú maticu zamrazením dnešného
backgroundu bez scope označenia.

## 7. Povinné nulové a hraničné limity

- `Upsilon->0`: presná obnova akceptovanej K1/M-009 sústavy;
- `Gamma->0` so spoločným couplingom: štandardný uncoupled constant-`w`
  fluid + CDM;
- `rho_c->0`, `rho_f->0`, `delta rho_f->0`: konečné akceleračné
  koeficienty a zánik sily;
- `k->0`: konečné `V_A` a scaled shear; nijaké delenie nulou;
- spoločný boost sa nesmie zameniť s gauge-invariantným `V_f-V_c`;
- regular `gamma_*(Y)` nesmie byť zvolená podľa výsledného `S8`.

## 8. Predregistrované očakávania

Na základe už dokázaného interaction determinant-u sa očakáva:

- čistý velocity interaction podblok zostane saddle;
- najjednoduchší `gamma_*=Gamma` pravdepodobne nebude dostatočný proti
  vedúcemu `Gamma/delta` pumpu;
- úplný systém môže výsledok zmeniť iba cez explicitný pressure/density/
  metric/Hubble coupling, nie tým, že sa slovne vyhlási drag za tlmiaci.

Tieto očakávania nie sú verdikt. Ak úplný symbol ukáže opak, výsledok sa
prijme iba s presným vysvetlením, ktorý povinný člen zmenil znamienko a
prečo nejde o gauge alebo constraint artefakt.

## 9. Predregistrované výsledky

### `NONEMPTY_WITNESS_K11_CS1_FULL_CONSTRAINED_SYMBOL`

Iba ak jeden úplný regular basis/symbol:

- spĺňa všetky constrainty a ich propagáciu;
- nemá fyzický rastúci superhorizontový mód v deklarovanom rozsahu;
- prejde nulové limity;
- používa odvodenú, nie post-data `gamma_*`.

Samotný výsledok ešte nie je high-`k`, Boltzmann ani `S8` PASS.

### `K11-CS1-<PREDECLARED_SCOPE>: EMPTY_CERTIFIED_SCOPE`

Iba ak analytický invariant, charakteristický/Frobeniov polynóm alebo
constraint-compatible separačný dôkaz vylúči celý vopred deklarovaný
rozsah. Neúspech jedného `gamma_*` bodu nestačí.

### `UNDETERMINED_REVIEW`

Ak chýba úplný stav, invariantná redukcia, epochový asymptotický režim,
gauge mapa alebo uzavretý symbol. Toto je správny výsledok pri neúplnom
odvodení a nesmie zvýšiť hĺbku.

## 10. Ďalší postup podľa výsledku

- úplný svedok: až potom samostatná high-`k`/constraint predregistrácia;
- scoped prázdnosť: zachovať dôvod a posúdiť, či zostala iná K11
  mikrofyzická dcéra;
- REVIEW: vytvoriť najmenší úplný DAE/base kontrakt a jeden ohraničený
  symbolický runner s vnútorným limitom `<=5 s` a vonkajším `<=10 s`;
  pred jeho spustením vznikne samostatný Markdown očakávaní.

Žiadny výsledok CS1 sám nemení release/PT1/PT2 stav.
