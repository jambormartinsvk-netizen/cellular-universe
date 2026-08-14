# K11-CS2 — predregistrácia úplnej viacdruhovej constrained DAE

**Dátum:** 2026-07-16  
**Koľaj:** `A1-K1 -> A2-K11 -> K11-R -> K11-CS2`  
**Autorita budúceho verdiktu:** iba hlavný orchestrátor  
**Stav pred behom:** `PREREGISTERED / NOT_EXECUTED`  
**Aktuálna hĺbka:** bez zmeny, `10/100 = G1`  
**Cieľ:** rozhodnúť, či konkrétny regulárny pasívny drag K11-R odstráni
K1/M-009 v úplnom constraint-kompatibilnom superhorizontovom systéme

## 1. Ľudskou rečou

K1 vytvára popol z paliva. Keďže palivo má veľmi malú inerciálnu hustotu
`rho_f+p_f=delta rho_f`, jeho relatívna rýchlosť voči popolu sa môže
zosilňovať sadzbou obsahujúcou `Gamma/delta`. K11-R pridáva fyzikálne
prípustné trenie medzi oboma médiami.

Samotné tvrdenie „trenie tlmí rozdiel rýchlostí“ nestačí. Metrika, hustoty,
fotóny, baryóny, neutrína a para sú navzájom previazané Einsteinovými
constraintmi. CS2 preto prenesie **celý priestor regulárnych fyzických
módov**, nie jeden ručne vybraný velocity seed. Bude sledovať najhoršiu
lineárnu kombináciu a osobitne gauge-invariantný rozdiel

```text
U_fc = V_f-V_c.
```

Ak úplný fyzický mód napriek dragu stále narastie približne ako M-009,
K11-R zomrie v tomto presnom rozsahu. Ak mód zmizne a výsledok prejde
constraintmi aj konvergenciou, K11-R môže pokračovať; stále však nebude
mať odvodenú mikrofyziku noise/FDT ani subhorizontový `S8` PASS.

## 2. Nemenná fyzika

CS2 nesmie po výsledku meniť tieto definície:

```text
Q_c^mu = Gamma rho_f u_c^mu + F_c^mu,
Q_f^mu = -Q_c^mu,

F_c^mu = +Upsilon h_c^{mu nu}u_{f,nu},
F_f^mu = -F_c^mu,
u_c.mu F_c^mu = 0,

Upsilon_R = Gamma rho_c delta rho_f/(rho_c+delta rho_f),
Gamma = lambda H0,
lambda = 0.15,
delta = 1+w_f = 0.02297,
c_s,f^2 = 1,
c_a,f^2 = w_f.
```

Akceptovaný tlakový prevod je

```text
delta p_f/rho_f
= delta_f+(2-delta)[3 mathcal H delta+a Gamma]V_f.
```

`delta Upsilon` nevstupuje do lineárnej sily, pretože násobí nulovú
backgroundovú relatívnu rýchlosť. Tento fakt musí base modul odvodiť v
term-by-term conservation ledgeri.

## 3. Autoritatívny background

Použije sa presný, módovo nezávislý A1 background, nie historický K7
`K_MPC=0.05` ansatz. Pre `N=ln a`:

```text
X_f,N = -3 delta X_f-lambda X_f/E,
X_c,N = -3 X_c+lambda X_f/E,
X_b,N = -3 X_b,
X_r,N = -4 X_r,
E^2   = X_f+X_c+X_b+X_r,
H     = H0 E.
```

Dnešné vstupy sú zmrazené existujúcim A1 ledgerom:

```text
h=0.6637, Omega_m0=0.3517, omega_b=0.02237,
Delta N_eff=0.0535, N_eff,std=3.046,
omega_gamma=2.469e-5.
```

`X_r` sa rozdelí na fotóny, štandardné neutrína a registrovanú paru podľa
rovnakej dnešnej radiation normalizácie. Ak para nemá preukázateľne
rovnakú free-streaming uzáveru ako neutrína, musí mať vlastnú hierarchiu.
Žiadne perturbatívne `k` nesmie vstúpiť do `H`, `Omega_A`, `Gamma/H` ani
do opacity/background koeficientov.

Toto použitie presného A1 ODE nevyžaduje asymptotický koeficient `A_f` z
K4. Otvorená normalizácia skorého K7 radu sa nesmie preniesť do CS2.

## 4. Premenné a stav

Limit sa vždy odvodí z konečného `k`. Použijú sa

```text
N       = ln a,
epsilon = k/mathcal H,
V_A     = theta_A/k^2,
W_A     = mathcal H V_A.
```

Minimálny fyzický obsah:

- dark sector: `delta_c,W_c,delta_f,W_f`;
- baryóny: `delta_b,W_b`;
- fotóny: density, velocity, shear a potrebná polarizácia/TCA;
- štandardné neutrína: density, velocity, shear a multipóly;
- para: samostatná free-streaming hierarchia, kým nie je dokázané platné
  zlúčenie s neutrínmi;
- metrika: `Phi` evolvované cez `0i`, `Psi` určené slip rovnicou;
- vyššie multipóly škálované tak, aby regularita `F_l=O((k eta)^l)` bola
  konečná a kontrolovateľná.

Stavový register musí vzniknúť v jednom base module. Runner ho nesmie
kopírovať ani preusporiadať.

## 5. Dark rovnice, ktoré musí base presne reprodukovať

Pri definíciách

```text
g   = Gamma/H,
r   = rho_f/rho_c,
d_c = Upsilon/(H rho_c),
d_f = Upsilon/(H delta rho_f),
s   = d ln mathcal H/dN
```

platia

```text
delta_c,N
= -epsilon^2 W_c+3 Phi_N+g r(delta_f-delta_c+Psi),

delta_f,N
= -3(1-w_f)delta_f-delta epsilon^2 W_f
  -[9(1-w_f^2)+3g(1-w_f)]W_f
  +3delta Phi_N-gPsi,

W_c,N
= (s-1)W_c+Psi+d_c(W_f-W_c),

W_f,N
= (s+2)W_f+delta_f/delta+Psi
  +(g/delta)(2W_f-W_c)+d_f(W_c-W_f).
```

Pre K11-R musí byť presná identita

```text
d_c+d_f = Gamma/H = g.
```

## 6. Constrainty a netautologické holdouty

Base musí používať všetky species v súčtoch

```text
Delta = sum_A Omega_A delta_A,
M     = sum_A Omega_A(1+w_A)W_A.
```

Povinné identity:

```text
Phi_N+Psi = (3/2)M,
Delta+3M+(2/3)epsilon^2 Phi = 0,
k^2(Phi-Psi)
= 12 pi G a^2 sum_A(rho_A+p_A)sigma_A.
```

Pravidlá:

1. `0i` evolvuje `Phi`; nesmie byť súčasne hlásený ako nezávislý PASS.
2. `00` zostane holdout pozdĺž trajektórie; nesmie sa definovať nulou na
   každom kroku.
3. trace Einsteinova rovnica je druhý nezávislý holdout.
4. traceless/slip musí používať free-streaming shear; `Psi=Phi` je dovolené
   iba v explicitnom zero-shear limite.
5. conservation audit musí term po terme dokázať
   `Q_c+Q_f=0`, `F_c+F_f=0` a left-null/Bianchi mapu pre deriváciu `C_00`.
6. Rezíduum zostavené tou istou rovnicou, ktorá definovala testovanú
   premennú, je tautológia a nepridáva PASS.

## 7. Regulárna fyzická báza

CS2-A zostaví finite-`k` Frobeniovu/indiciálnu bázu. Musí určiť rank a
počet módov, nie ho predpokladať. Minimálne musí nájsť alebo vysvetliť
neprítomnosť:

- adiabatic/common-clock módu;
- CDM a baryon density isocurvature;
- neutrino density a velocity isocurvature;
- fuel entropy módu `delta_f/delta-3delta_gamma/4`;
- fuel-ash relative velocity módu `W_f-W_c`;
- parných density/velocity módov, ak je para samostatná.

Každý stĺpec počiatočnej bázy musí:

- byť regular pri skoršom štarte;
- spĺňať počiatočný `00` constraint relatívne `<1e-12` alebo absolútne
  `<1e-12`, keď je norma členov pod `1e-12`;
- byť oddelený od gauge/background-redefinition smerov;
- byť ortonormalizovaný vo vopred zapísanej fyzikálnej váženej norme.

Ľubovoľné numerické vektory z nulového priestoru jedného constraintu nie
sú fyzickou primordiálnou bázou.

## 8. Tri povinné propagácie

1. `FULL_K11`: exact-A1 background s `Gamma>0`, perturbácie K1 + K11-R;
2. `DRAG_NULL_K1`: ten istý exact-A1 background a fyzicky rovnako
   normalizovaná báza, ale `Upsilon=0`; reprodukuje akceptovaný K1;
3. `COMMON_NULL`: konzistentne prepočítaný `lambda=0` background a
   `Gamma=Upsilon=0` perturbácie; reprodukuje neinteragujúce fluidy.

`FULL_K11/DRAG_NULL_K1` izolujú účinok dragu na tom istom backgrounde.
`COMMON_NULL` je fyzický spoločný nulový limit, ale nemá numericky totožný
background; jeho báza sa páruje podľa fyzických názvov a normy, nie slepým
kopírovaním koeficientov.

Ak sa pre čisto algebraickú diagnostiku vypne `Gamma` iba v perturbáciách
na nenulovom A1 backgrounde, musí niesť názov
`NONPHYSICAL_OPERATOR_NULL`. Nesmie udeľovať constraint PASS ani byť
menovateľom fyzikálneho verdictu.

`COMMON_NULL` sa nesmie zameniť s odstránením dnešnej palivovej hustoty:
pri `lambda=0` zostáva neinteragujúce palivo s rovnakou dnešnou boundary
condition.

Primárna metrika je najväčšia singular value fyzicky váženej fundamentálnej
mapy celej regulárnej bázy. Povinné osobitné riadky:

```text
W_f-W_c,
comoving curvature,
total density,
Phi,Psi.
```

Pomer k zanikajúcej referencii sa nikdy nehlási bez absolútnej amplitúdy a
normy menovateľa.

## 9. Zmrazené povrchy a konvergencia

CS2 je superhorizontový test. Použijú sa najmenej tri módy

```text
k = {2.5e-6, 5e-6, 1e-5} Mpc^-1,
```

pričom každý musí mať na celom auditovanom intervale

```text
epsilon=k/mathcal H < 0.05.
```

Ak exact A1 background tento cap poruší, príslušný mód sa nesmie použiť a
pred behom sa zvolí menší, dokumentovaný `k`; po poznaní transferu sa grid
nesmie meniť.

Počiatočná Frobeniova plocha sa porovná aspoň na dvoch hĺbkach s pomerom
`a_start,2/a_start,1=1/2`. Endpoint je `a=1`. Ak implementácia používa
post-recombination handoff, musí samostatne preukázať, že zanedbaná skorá
K1/K11 korekcia je pod `1e-5` v počiatočnej báze; inak ide o
`REVIEW_BLOCKED_SEED_HANDOFF`.

Povinné porovnania:

| Kontrola | Zmrazený prah |
|---|---:|
| počiatočný `00` constraint | `<1e-12` |
| evolučný relatívny `00` holdout na aktívnej norme | `<1e-6` |
| evolučný trace/traceless holdout | `<1e-6` |
| nezávislá Bianchi/left-null mapa | `<1e-6` |
| posun skorého štartu | `<1e-5` |
| `k -> k/2` transferová konvergencia | `<1e-6` |
| tolerančná alebo nezávislá metódová konvergencia | `<1e-6` |
| zvýšenie hierarchy closure/lmax | `<1e-6` |
| lineárne amplitúdové škálovanie | `<1e-8` |

Ak päťsekundový limit nedovolí splniť mriežku, výsledok je `REVIEW` a nie
fyzikálny STOP. Prahy sa po výsledku neuvoľnia; zmena vyžaduje nový
predbehový dokument s dôvodom.

## 10. Očakávanie pred spustením

CS1 dokázala interaction-only saddle

```text
det M_int = -d_c(g/delta) < 0.
```

Pre K11-R je relatívna drag sadzba iba `Gamma`, kým K1 pump nesie
`Gamma/delta`. Hrubý, nie rozhodovací odhad od `z_star=1089.9` po dnešok je

```text
N_K1     = 12.213,
N_K11-R  approximately (2/delta-1) Gamma Delta t approximately 12.07,
ln(A_rel,FULL/A_rel,NULL) expected in [10,13].
```

Očakávame teda, že K11-R M-009 úplne nevylieči. Rozdiel približne `-0.14`
oproti K1 je príliš malý. Tento odhad nesmie nahradiť úplný constrained
beh a nesmie sa spätne upraviť podľa výsledku.

## 11. Predregistrované verdict vetvy

### `STRUCTURAL_PASS`

Všetky species, tlak, conservation/Bianchi, znamienka a nulové limity sú
presné. Neznamená stabilitu ani body za evolúciu.

### `BASIS_PASS`

Úplná regulárna fyzická báza, jej počet, constraints a nezávislá
klasifikácia prešli. Neznamená stabilitu.

### `STABILITY_PASS_SCOPE_K11_R`

Možný iba ak všetky regulárne módy a najhoršia kombinácia:

- prejdú všetkými holdoutmi a konvergenciou;
- nemajú rast, ktorý sa zhoršuje pri skoršom štarte alebo `k->0`;
- majú `ln(A_rel,FULL/A_rel,NULL) <= 1` pre gauge-invariantný relative
  sektor na všetkých registrovaných konfiguráciách;
- pri primordiálnej fyzickej amplitúde `1e-5` ostanú v lineárnej norme
  striktne `<1`.

Aj potom zostáva noise/FDT a subhorizontový `S8` sektor otvorený.

### `STOP_SCOPE_K11_R`

K11-R dostane scoped smrť iba ak všetky holdouty a konvergencie prejdú a
nastane aspoň jedno:

1. constraint-kompatibilný gauge-invariantný relative mód má
   `ln(A_rel,FULL/A_rel,NULL)>1` na každom registrovanom `k`, štarte,
   closure a metóde;
2. najhoršia singular value alebo `U_fc` rastie bez konvergentnej limity
   pri skoršom štarte alebo `k->0`;
3. amplitúda `1e-5` dosiahne fyzickú váženú normu `>=1` pred endpointom;
4. stabilita vyžaduje `Upsilon<0`, nový fit alebo singularitu vloženú ako
   `1/delta` do dragu;
5. deklarovaný operátor nevie uzavrieť Bianchiho identitu.

Smrť K11-R automaticky nezabíja každú abstraktnú pasívnu funkciu
`Upsilon(Y)`, ak dôkaz nepokrýva celú túto triedu. Dôvod smrti a všetky
skripty zostanú zachované.

### `REVIEW_BLOCKED_IMPLEMENTATION`

Povinné pri timeout-e, chýbajúcej species/hierarchii, nejasnom mode count,
constraint failure, nekonvergencii, floor efekte alebo závislosti od
jedného štartu/módu. Taký výsledok nesmie zabiť fyzickú koľaj.

## 12. Implementačná architektúra a limity

Povolené sú iba:

```text
scripts/baseScripts/a2_k11_cs2/__init__.py
scripts/baseScripts/a2_k11_cs2/full_multispecies_constrained_dae.py
scripts/262_script_A2_K11_CS2_full_multispecies_constrained_DAE_runner.py
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_001.json
```

Base vlastní background, stav, rovnice, basis, normy a holdouty. Runner
iba odovzdá parametre, spustí jednu matrix ODE, vynúti deadline a
serializuje výsledok. Historické skripty 45–54 sa neimportujú.

Každý Python beh:

- používa priamo `C:\\Python311\\python.exe`;
- má vnútorný limit `<=5 s`;
- má vonkajší shell timeout `<=10 s`;
- sa spustí až po aktualizácii tohto Markdownu alebo samostatného prerun
  dodatku s ľudským očakávaním;
- pri prekročení limitu končí fail-closed bez nekonečného čakania.

Povolené sú najviac dve technické opravy. Po nich sa nevytvorí CS3a/CS3b:
stav bude autoritatívne `PASS_SCOPE`, `STOP_SCOPE` alebo `REVIEW_BLOCKED`.

### Registrovaná technická oprava 1/2 po S0 RUN-001

Runner 262 dokončil a zapísal celý structural payload, ale vonkajší shell
nepozoroval korektný exit do `10 s` po duplicite plného JSON na stdout.
Runner aj RUN-001 ostávajú zachované. Úzko povolený nástupca
`263_script_A2_K11_CS2_S0_structural_quiet_output_rerun1.py` nemení base ani
fyziku; pri `--output` tlačí iba krátke zhrnutie. Audit:
`K11_CS2_S0_RUN001_EXTERNAL_EXIT_TIMEOUT_AUDIT.md`.

## 13. Dopad na release a dokumentáciu

Predregistrácia ani budúci deterministický CS2 beh automaticky nemenia
Zenodo release. K11 je záložná nepublikovaná koľaj. Release review vznikne
iba pri materiálnom dopade na publikovaný mechanizmus alebo tabuľku
predikcií.

Výsledný audit bude iba v route-local `ARTIFACTS`; koreňový `Audit/`
duplikát nevznikne. Staré FS/CS1 artefakty a eventy sa neprepisujú.

## Neskoršie metodické obmedzenie §12

Historický limit dvoch opráv platil pre S0-v001. Full v002 je samostatná
úplná technická architektúra s presným `4*lmax+9` kontraktom a vlastným
ledgrom `0/10`. Technický neúspech nemení fyzikálny verdikt; po desiatom
technickom neúspechu by sa zastavila iba v002 implementácia s presnou
kategóriou príčiny a K11 by zostala `REVIEW_TECHNICAL_UNRESOLVED`.
