# K11-CS2 full v002 — contract closure a pripravenosť pokusu 1/10

**Dátum:** 2026-07-16  
**Rozsah:** read-only fyzikálno-matematický audit; bez Pythonu a bez ODE  
**Autoritatívny stav:** `REVIEW_NOT_READY_FOR_ATTEMPT_1`  
**Technický counter pri readiness audite:** `0/10`; neskôr source-AST PASS v pokuse `5/10`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`

## 1. Čo zrušenie starého capu vyriešilo

Historické PF-061/PF-062 už K11 nezamykajú na `2/2`. Full v002 má vlastnú
úplnú technickú architektúru a cap `10`. To však samo nedodalo chýbajúcu
polarizačnú hornú uzáveru, exact-A1 thermal adapter ani TCA/full mapu.

Najväčší poctivý krok teraz je uzavrieť kontrakt a presne pomenovať, čo musí
byť hotové pred pokusom 1. Spustiť vopred neúplný base by iba spotrebovalo
technický pokus na známej chybe.

## 2. Kanonický CAMB-E auditný register

Pre `L=lmax`:

```text
Phi,
delta_c, W_c,
delta_f, W_f,
delta_b, W_b,
delta_gamma, W_gamma,
F_gamma_2 ... F_gamma_L,
E_gamma_2 ... E_gamma_L,
delta_nu, W_nu, F_nu_2 ... F_nu_L,
delta_steam, W_steam, F_steam_2 ... F_steam_L.
```

Počet je

```text
9 +(L-1)+(L-1)+(L+1)+(L+1)=4L+9,
L=4 -> 25,
L=6 -> 33,
L=8 -> 41.
```

`Psi` je algebraický slip output, nie stav. `RHS.keys` musí byť presne ten
istý ordered tuple ako state manifest. Count ani množina bez poradia nestačí.

Toto nie je natívny count CLASS. CLASS môže mať `pol0/pol1` a dynamický
TCA/RSA/UFA stav; nesmú sa premenovať na neexistujúce CAMB `E_0/E_1`.

## 3. Povinné exact-set negatívne fixtures

Preflight musí odmietnuť:

- `E_gamma_0` alebo `E_gamma_1`;
- chýbajúce `E_gamma_2` alebo `F_steam_L`;
- rovnaký count s `fake_state`;
- duplicitu alebo zmenené poradie;
- starú formulu `4L+11`;
- lokálnu kópiu manifestu v runneri;
- RHS s extra/chýbajúcim alebo preusporiadaným kľúčom;
- pozičný slice namiesto mapovania mien.

## 4. Hierarchia a horná uzávera

Generic recurrence je prípustná iba pre `2 <= ell < L`. Pre plochú regular
Bessel vetvu sú zdrojovo podopreté closure:

```text
F_gamma_L' = k F_gamma_(L-1) -(L+1)/tau F_gamma_L
             -kappa_dot F_gamma_L,
F_nu_L'    = k F_nu_(L-1) -(L+1)/tau F_nu_L,
F_steam_L' = k F_steam_(L-1) -(L+1)/tau F_steam_L.
```

V `N=ln a` sa RHS delí `mathcal H`. Znamienko opacity musí byť deklarované
tak, aby pozitívna scattering rate tlmila fotónový multipól.

### Rozhodujúci otvorený blocker

Presná horná uzávera kanonického CAMB `E_gamma_L` nie je v súčasnej
predregistrácii ani v generickom `camb.symbolic`, ktorý končí pri `ell<L`.
Natívnu CLASS `pol_L` closure nemožno bez dôkazu skopírovať do CAMB-E bázy.

Povolené sú iba dve technické koľaje:

| Koľaj | Obsah | Stav |
|---|---|---|
| `K11-TC-A0` | univerzálna exact finite-L spin-2 closure | `STOP_INVARIANT_NO_GO` |
| `K11-TC-A1` | mode-by-mode Frobenius closure | `REVIEW_SEED_ONLY` |
| `K11-TC-A3` | kanonická CAMB-E hierarchia s deklarovaným numerickým top rezom a povinnou konvergenciou | `ACTIVE` |
| `K11-TC-B` | zostať v natívnej CLASS polarizačnej báze a dokázať presnú CLASS↔CAMB-E mapu | `OPEN_ALTERNATIVE` |

Sú to technické architektúry toho istého K11-CS2, nie nové fyzikálne koľaje.
Prvá sa skúma A, lebo sa vyhne plnému adapteru. Ak A narazí na invariantný
rozpor, zdokumentuje sa dôvod a pokračuje B.

## 5. Backend-interface kontrakt bez ODE

Natívny backend musí exportovať

```text
native_manifest, canonical_manifest,
P: native -> canonical,
I: canonical -> native physical image,
native_rhs_manifest,
tca_manifest a tca/full mapy,
source/version/hash provenance.
```

Na full checkpointoch sa neskôr vyžaduje

```text
rank(P)=rank(I)=4L+9,
P I = Identity_(4L+9),
I P = projector na deklarovaný fyzický native image,
S_can P = S_native,
P A_native I = A_can,
constraint_can P = constraint_native.
```

Samotná schéma môže neskôr dostať `INTERFACE_SCHEMA_PASS`, nikdy však
`BACKEND_ADAPTER_PASS` bez reálneho adaptera a numerickej parity.

## 6. Čo možno uzavrieť bez novej mikrofyziky

- exact-A1 fuel/ash backgroundové ODE, dnešné hranice, flatness, positivity,
  `lambda->0` a `partial H/partial k=0`;
- zmrazený efektívny fuel closure `w_f=-1+delta`, `c_s,f^2=1`, nulový shear;
- K11-R deterministický operátor
  `Upsilon_R=Gamma rho_c delta rho_f/(rho_c+delta rho_f)`;
- total energy/momentum/Bianchi a sign-flip fixtures;
- conditional-S1 regular basis a worst-case singular-value stabilita bez
  fitovania primordial steam amplitúd;
- CLASS/HyRec ABI a source injection schema.

## 7. Čo zostáva fyzikálne otvorené

- steam free-streaming/self-coupled/collision kernel, vznik a decoupling;
- primordial steam korelácie pre CMB predikciu;
- mikrofyzický pôvod/noise/FDT K11-R;
- exact-A1 `x_e`, opacity, `T_b`, `c_b^2` a visibility zo skutočne zapojeného
  source-pinned HyRec;
- TCA/full overlap a switch sensitivity.

Momentum-only K11-R je nulový na FLRW a jeho disipovaný ohrev je kvadratický
v relatívnej rýchlosti. V tomto lineárnom audite sa preto zmrazuje scope
„bez priameho plasma heating/ionization od K11-R“. Nie je to dôkaz, že
všeobecné bunkové delenie alebo para sú termálne inertné.

## 8. Podmienky autorizácie technického pokusu 1/10

Pokus 1 môže byť iba bounded no-ODE
`exact-set + top-closure + backend-interface-schema` preflight. Pred jeho
spustením musí platiť:

1. zvolená a zdokumentovaná `K11-TC-A3` alebo `K11-TC-B`;
2. explicitne numerický CAMB-E top s povinnou konvergenciou alebo presná native↔CAMB-E mapa;
3. jediný autoritatívny state/RHS tuple a spoločný validator;
4. deklarované `tau`, curvature a opacity konvencie;
5. každý zo štyroch hierarchických top rows existuje presne raz, nemá
   dependency na neregistrované `L+1` a nepredstiera exact fyzikálnu identitu;
6. negatívne fixtures používajú tú istú produkčnú validačnú cestu;
7. samostatný immutable machine výstup, ktorý neprepisuje budúci full run.

PASS môže byť iba

```text
PASS_ARCH_A_ATTEMPT_1_EXACT_SET_INTERIOR_AND_REGISTERED_TRUNCATION_ONLY.
```

Nesmie udeliť structural/basis/backend/stability ani fyzikálny PASS.

## 9. Rozsudok

```text
REVIEW_NOT_READY_FOR_ATTEMPT_1
```

K11 je technicky znovu otvorená. Counter zostáva `0/10`, pretože
K11-TC-A0 skončila analytickým invariantným no-go pred kódom. Pokus 1 je
odteraz autorizovaný iba v rozsahu K11-TC-A3 podľa samostatnej
predregistrácie; jeho top je numerický rez a budúci fyzikálny význam stojí
na `lmax` a closure-family konvergencii. K11-TC-B zostáva alternatíva.

Úplný dôvod a obmedzenia sú v
`K11_TC_A_FINITE_E_CLOSURE_NO_GO_AND_NUMERICAL_TRUNCATION_DECISION_2026-07-16.md`.

## 10. Neskorší vykonaný stav

Po štyroch zachovaných technických incidentoch prešiel pokus 5 source-AST
preflightom `55/55`, counts `25/33/41`, exit 0 a wall približne 1.5 s.
Autoritatívny rozsah je iba
`PASS_ARCH_A_SOURCE_AST_EXACT_SET_AND_REGISTERED_TRUNCATION_ONLY`. Dobový
zápis bol `5/10`; podľa neskoršieho pravidla je
`historical_packages_total=5` a aktívny counter po vecnom úspechu `0/10`.
Full thermal/TCA/DAE, constraint propagácia a evolučná konvergencia zostávajú
nevykonané.
