# A1_K1_A2_K4_P5_3_SM_v1 — draft autorovho vstupného kontraktu

**Dátum:** 2026-07-22  
**Route:** `A1-K1 -> A2-K4 -> P5.3g7 -> S-M/Q18/Q22 -> SM_v1`  
**Stav:** `AUTHOR_BRANCH_SELECTED / INPUT_CONTRACT_INCOMPLETE / NO_CODE_AUTHORIZED`  
**Autor teórie:** Martin Jambor  
**Procesný vlastník:** hlavný orchestrátor  
**Predchodca:** dokument 244; EA-039 T2 prijatý; C3 `45/45`; K4 `60/100`; P5 `3.5/6`

Tento dokument je pracovný draft. Nie je ešte immutable preregistráciou a
nemá pre-run SHA receipt. Zmrazí sa až po úplnom autorovom vyplnení všetkých
11 rozhodovacích blokov a po nezávislom formula/process audite. Dovtedy sa
nesmie vytvoriť ani spustiť Python implementácia.

## 1. Kanonické označenie mechanizmov

| Kanonické ID | Historický alias v dokumente 244 | Význam | Stav |
|---|---|---|---|
| `A1_K1_A2_K4_P5_3_SM_v1` | vetva A | skorý exit/reheating rezervoár | `SELECTED_BY_THEORY_AUTHOR / INPUT_INCOMPLETE` |
| `A1_K1_A2_K4_P5_3_SM_v2` | vetva B | lokálna scar/event produkcia | `PARALLEL_UNSELECTED_CANDIDATE` |

`v1` a `v2` označujú dve paralelné mechanizmové varianty. `v2` nie je
oprava, nástupca ani vyššia verzia `v1`. Historické označenia A/B zostávajú
v dokumente 244 kvôli nemennosti dôkazovej histórie, ale v živých plánoch sa
ďalej používajú iba kanonické ID.

Identifikátor zámerne obsahuje `P5_3`, nie `P5.4`: P5.4 je stále `NOT RUN`
a môže sa otvoriť až po úplnom P5.3, prijatom T1 formula audite a samostatnej
výpočtovej predregistrácii.

## 2. Autorova voľba

Používateľ 2026-07-22 schválil premenovanie pôvodných A/B na v1/v2 a pokyn
„zapíš značenie a pokračuj“ sa v nadväznosti na odporúčanú pôvodnú vetvu A
zachytáva ako voľba:

```text
SELECTED_MECHANISM = A1_K1_A2_K4_P5_3_SM_v1
MEANING = EARLY_EXIT_REHEATING_RESERVOIR
RUN_AUTHORIZED = false
```

Voľba mechanizmovej triedy sama neurčuje rezervoár, kernel, parametre ani
čas produkcie. Preto ešte nevzniká formula PASS ani fyzikálny bod.

Autor teórie následne 2026-07-22 doslovne potvrdil:

> Schvaľujem V1-R1

Tým je uzavretý iba blok `V1-D01`:

```text
V1-D01 = CLOSED_BY_THEORY_AUTHOR
SELECTED_RESERVOIR_CLASS = V1-R1
RESERVOIR_IDENTITY = SEPARATE_EARLY_EXIT_REHEATING_COMPONENT_e
DISTINCT_FROM_LATE_A1_FUEL_rho_f = true
```

Toto rozhodnutie neurčuje stavové premenné, `T_e^(mu nu)`, stavovú rovnicu,
transfer, clock, potenciál, parametre ani počiatočné podmienky. Tie zostávajú
otvorené v `V1-D02` až `V1-D11`.

## 3. Zmrazené hranice zdedené z dokumentu 244

V1 musí odvodiť lokálny zápis najmenej v tvare

```text
nabla_mu T_s^(mu nu) = +S_s^nu,
nabla_mu T_e^(mu nu) = -S_s^nu,
S_s^nu = C_s u^nu + J_s^nu,
u_nu J_s^nu = 0.
```

Platí:

- `C_s` nesmie mať ako voľný argument kozmický čas, `ln a`, globálne `H0`
  ani realizovaný Fourierov mód `k`;
- `J_s^nu=0` smie vyplynúť iba v homogénnom izotropnom limite, nie byť
  vopred vloženou perturbatívnou skratkou;
- neskorý registrovaný kanál zostáva takmer čistý `F -> C` a nesmie sa
  potichu premenovať na významný steam source;
- `Delta N_eff=0.0535` je iba superseded legacy sensitivity benchmark, nie
  cieľ pre amplitúdu, clock, branch ratio ani kernel;
- po source-off musí para prejsť do odvodeného collisionless alebo inak
  explicitne uzavretého pozostatkového režimu.

## 4. Jedenásť povinných rozhodovacích blokov v1

| ID | Autor musí dodať alebo výslovne schváliť | Stav |
|---|---|---|
| `V1-D01` | identitu lokálneho skorého rezervoára `e` | `CLOSED: V1-R1 / AUTHOR_APPROVED_2026-07-22` |
| `V1-D02` | jeho stavové premenné, jednotky, doménu, `T_e^(mu nu)` a stavovú rovnicu | `CLOSED_FORM_ONLY: V1-S1 + V1-P1 + V_min=0 / PARAMETERS DEFERRED D06` |
| `V1-D03` | lokálny decay/transfer zákon a invariantný clock `chi` | `PARTIAL_AUTHOR_INPUT: B6-C0 FIRST-PASSAGE TOPOLOGY APPROVED / RATE-ENERGY MAP OPEN` |
| `V1-D04` | zdroj energie-hybnosti pary a ledger všetkých ostatných produktov | `OPEN_AUTHOR_INPUT` |
| `V1-D05` | paralelné alebo sekvenčné poradie popola/pary; pri sekvencii aj medzistav | `OPEN_AUTHOR_INPUT` |
| `V1-D06` | úplný zoznam nových konštánt a počiatočných podmienok | `OPEN_AUTHOR_INPUT` |
| `V1-D07` | fyzikálny source-off mechanizmus, jeho null limit a dôkaz, že nejde o voľný čas | `OPEN_AUTHOR_INPUT` |
| `V1-D08` | produktovú kinematiku a matrix element alebo collision operator `C[f]` | `OPEN_AUTHOR_INPUT` |
| `V1-D09` | steam interakcie a thermalization/decoupling kritérium alebo dôvod collisionless vzniku | `OPEN_AUTHOR_INPUT` |
| `V1-D10` | počiatočný štatistický stav a noise prescription pre `P_AB(k)` a módové korelácie | `OPEN_AUTHOR_INPUT` |
| `V1-D11` | pozostatkový zákon vrátane `rho_s proportional a^-4` a všetkých párových energy/momentum identít | `OPEN_AUTHOR_INPUT` |

Žiadny blok sa nevyplní odhadom agenta. Codex smie ponúknuť fyzikálne
varianty a vysvetliť ich dôsledky, ale výber nového objektu alebo zákona musí
výslovne potvrdiť autor teórie.

## 5. Uzavreté rozhodnutie — V1-D01

Pre identitu rezervoára `e` boli predložené tieto evidence-backed možnosti:

1. `V1-R1` — samostatná skorá exit/reheating zložka, odlišná od neskorého
   A1 paliva; najčistejšie oddeľuje skorý relikt od neskorého `F -> C`;
2. `V1-R2` — existujúce A1 palivo `rho_f`, ale iba s novým **odvodeným**
   lokálnym skorým prepnutím/transferom, ktorý nemení neskorý konštantný
   `Gamma` kanál a nevkladá voľný čas;
3. `V1-R3` — iná už existujúca zložka teórie, ktorú autor presne pomenuje a
   doloží jej `T_e^(mu nu)`.

Autor výslovne schválil `V1-R1`. `V1-R2` a `V1-R3` zostávajú iba
nezvolenými historickými alternatívami; živý kontrakt ich nekombinuje s v1.

## 6. Historický priebeh voľby V1-D02 — superseded oddielom 6.6

Oddiely 6.1–6.5 zachovávajú auditovateľný priebeh voľby. Ich tokeny
`PARTIAL_AUTHOR_APPROVAL` a `ACTIVE_SUBSTEP` sú historické snapshoty,
superseded closure v oddiele 6.6. Autoritatívny živý stav je v tabuľke
vyššie a jediný aktívny krok je oddiel 7 (`V1-D03`).

Pre samostatný skorý rezervoár treba zvoliť jeho lokálny stav a
energy-momentum tensor. Dve minimálne formulovateľné možnosti sú:

Pre oba kandidáty v tejto sekcii platí metrická signatúra `(-,+,+,+)`.
Výber označenia `V1-S1` alebo `V1-S2` sám osebe **neuzatvára** `V1-D02`:
autor musí zároveň schváliť nižšie uvedenú doménu a úplnú stavovú closure.

1. `V1-S1` — kanonické minimálne viazané lokálne skalárne pole `phi_e`:

   ```text
   T_e^(mu nu) = partial^mu phi_e partial^nu phi_e
                 - g^(mu nu) [1/2 partial_alpha phi_e partial^alpha phi_e
                              + V_e(phi_e)],
   rho_e = 1/2 dot(phi_e)^2 + V_e,
   p_e   = 1/2 dot(phi_e)^2 - V_e.
   ```

   Stav tvoria `phi_e` a jeho lokálny kovariantný gradient. Pre časupodobný
   gradient definujme

   ```text
   X_e = -1/2 partial_alpha phi_e partial^alpha phi_e > 0,
   u_e^mu = -partial^mu phi_e / sqrt(2 X_e)
             (future-directed),
   dot(phi_e) = u_e^mu partial_mu phi_e.
   ```

   Vzťahy `rho_e = X_e + V_e` a `p_e = X_e - V_e` platia v lokálnom
   scalar-rest-frame; uvedený zápis s `dot(phi_e)` je jeho homogénna FLRW
   projekcia. Doména musí obmedziť reálne `phi_e`, časupodobný gradient a
   potenciál tak, aby `rho_e = X_e + V_e >= 0`; pozitivita nie je dôsledkom
   zatiaľ neurčeného `V_e`. V prirodzených jednotkách `hbar=c=1` má `phi_e`
   rozmer energie, operátor `partial_mu` rozmer energie,
   `partial_mu phi_e` rozmer energie na druhú a `X_e`, `V_e`, `rho_e`,
   `p_e` rozmer energie na štvrtú. Interpretácia ako koherentný kondenzát je iba
   možný neskorší odvodený režim, nie synonymum alebo súčasť voľby `V1-S1`.
   Na uzavretie D02 treba schváliť aj funkčný tvar/triedu `V_e(phi_e)` a jej
   doménu; numerické konštanty a počiatočné podmienky patria do `V1-D06`.
   Transfer ostáva otvorený v `V1-D03`.
2. `V1-S2` — efektívna lokálna perfektná tekutina
   `(rho_e, u_e^mu)`:

   ```text
   T_e^(mu nu) = (rho_e + p_e) u_e^mu u_e^nu + p_e g^(mu nu),
   p_e = w_e rho_e,
   u_e^mu u^e_mu = -1,
   rho_e >= 0.
   ```

   Doména vyžaduje `rho_e >= 0` a budúcnosťou orientovaný jednotkový
   časupodobný vektor `u_e^mu`. V prirodzených jednotkách `hbar=c=1` majú
   `rho_e` a `p_e` rozmer energie na štvrtú; `u_e^mu` a `w_e` sú
   bezrozmerné. Autor musí určiť, či `w_e` je konštantný barotropný parameter
   alebo odvodená stavová funkcia, a pri funkcii uviesť jej argumenty a
   doménu. Výber samotného názvu `V1-S2` preto D02 neuzatvára. Efektívny
   fluid navyše ešte nedodáva lokálnu mikrofyziku transferu.

Procesné odporúčanie pre prvé odvodenie je `V1-S1`: dáva explicitné lokálne
`T_e^(mu nu)` a dynamický stav bez zavedenia voľného konštantného `w_e`.
Nie je to však autorova voľba. Ak ani jedna možnosť nezodpovedá teórii, autor
môže dodať tretiu explicitnú lokálnu stavovú definíciu s rovnakými povinnými
údajmi.

### 6.1 Historická autorova čiastková voľba V1-S1

Autor teórie po vysvetlení, že najprv treba nájsť mantinely hľadanej funkcie
a že prvé odhady sú nutné, odpovedal 2026-07-22 „Schvaľujem, pokračuj“.
V kontexte jedinej položenej otázky sa to zachytáva ako schválenie
odporúčaného `V1-S1`:

```text
V1-D02 = PARTIAL_AUTHOR_APPROVAL
SELECTED_STATE_CLASS = V1-S1_CANONICAL_MINIMALLY_COUPLED_REAL_SCALAR
POTENTIAL_V_e = NOT_SELECTED
ACTIVE_SUBSTEP = V1-D02a_POTENTIAL_CONSTRAINT_MANTLE_MAPPING
RUN_AUTHORIZED = false
```

Schválené sú iba stavové premenné, signatúra, kanonický `T_e^(mu nu)`,
scalar-rest-frame doména a jednotky uvedené vyššie. Nie je schválený tvar,
amplitúda ani parameter potenciálu. `V1-D02` sa uzavrie až po vytvorení
mantinelového pasu, prvých odhadov a autorovej voľbe jednej prípustnej triedy
`V_e(phi_e)` s doménou.

### 6.2 Historický substep V1-D02a — mantinely pred funkciou

Podľa `FS-GATE-01` sa teraz nesmie hádať jedna účelová funkcia. Najprv sa
zostaví behaviorálny obal `B_V` a prienik mantinelov pre ten istý potenciál,
ten istý parameterový bod a tie isté okrajové podmienky. Prvé numerické alebo
rádové odhady sú povinné, ale zostávajú `E3_PROVISIONAL`, kým nemajú úplnú
mapu na lokálny mechanizmus alebo meranie. Najmä sa nesmie ladiť na legacy
`Delta N_eff=0.0535`, `S8` ani `H0`.

Povinný pas bude obsahovať aspoň:

1. doménu a kodoménu `V_e: phi_e -> energy_density`;
2. pozitivitu `rho_e=X_e+V_e >= 0`, regularitu a spodnú ohraničenosť v
   navštívenej doméne;
3. smer pohybu/exit podmienku odvodenú z lokálneho stavu, nie z vloženého
   kozmického času;
4. počiatočný energetický podiel rezervoára a maximálny dostupný steam
   budget z lokálnej conservation identity;
5. source-off a neskorý limit, v ktorom `rho_e` aj transfer zanedbateľne
   zaniknú bez zmeny neskorého A1 `F -> C` ledgeru;
6. null limit väzby, stabilitu kanonického skalára a počet nových konštánt;
7. oddelenie tvrdých `E0/E1` hraníc od `E2` comparatorov a prvých
   `E3_PROVISIONAL` odhadov;
8. najmenej jedného jednoduchého analytického svedka až po dôkaze, že
   behaviorálny obal nie je prázdny.

Kým pas nie je zostavený a auditovaný, `POTENTIAL_V_e=NOT_SELECTED`.

### 6.3 Behaviorálny mantinelový pas V1-D02a

Aktuálny stav prieniku je

```text
B_V = UNDETERMINED_REVIEW
LOCAL_STATE_CLASS = V1-S1
POTENTIAL_CLASS = NOT_SELECTED
ABSOLUTE_ENERGY_SCALE = NOT_DERIVED
```

Efektívna FLRW história s kladným skorým ukončeným zdrojom je neprázdna,
ale nedokazuje existenciu lokálneho potenciálu. Pre `V_e` platí tento prvý
pas:

| Mantinel | Rovnica/nerovnosť a doména | Trieda dôkazu | Stav a dôsledok |
|---|---|---|---|
| lokálny stav | reálne `phi_e`, `X_e>0`, signatúra `(-,+,+,+)` | `E0_EXACT` po autorovom V1-S1 | pole a jeho gradient sú stav; tvar `V_e` neurčený |
| regularita | pracovný kandidátny priestor `X_K` vyžaduje `V_e` najmenej `C^2` na celej navštívenej doméne | `E0_METHOD / DEFINITION_OF_X_K` pre neskoršiu silu a lineárne poruchy | je to scope definícia, nie odvodená identita teórie; zakáže cusp/singularity v testovanej trajektórii |
| energia | `rho_e=X_e+V_e>=0`, `rho_s>=0`, `H^2>0` | `E0_EXACT` | `V_e` nemusí byť všade kladný, ale spoločná trajektória nesmie dať zápornú celkovú energiu |
| conservation | `nabla T_s=+S_s`, `nabla T_e=-S_s` | `E0_EXACT` | integrovaná steam energia nesmie prekročiť odobratú energiu `e` |
| lokálnosť | bez voľného `t`, `ln a`, `H0` alebo realizovaného `k` | `E0_EXACT` | exit musí byť funkciou lokálneho stavu; časovaný bump je zakázaný |
| stabilná navštívená doména | `V_e` konečný a zdola ohraničený na trajektórii; kanonické znamienko kinetiky | `E0` pre kinetic/no-ghost, hranica tvaru zatiaľ `E3` | konkrétne `V_e''` a rozsah poľa treba zvoliť a testovať |
| vypnutý režim | `S_s^mu -> 0`, neskoré `rho_e` a transfer zanedbateľné; `rho_s proportional a^-4` | `E0_EXACT` ako zmluvná hranica | minimum `V_e` môže pomôcť, ale samo bez D03 nedokazuje source-off |
| časovanie | konzervatívny comparator: zdroj skončí pred BBN | `E2_REFERENCE_MODEL` | neskoršie varianty vyžadujú BBN+CMB likelihood; nejde o odvodený čas alebo `phi_e` |
| neskorý A1 limit | persistentný priamy steam podiel je legacy screenom `f_R,direct less than about 3.2e-5` | `E3_LEGACY_BACKGROUND_SCREEN` | chráni prakticky čistý neskorý `F -> C`; neobmedzuje priamo skorú výšku `V_e` |
| predikčnosť | žiadny voľný profil, počet funkcií a parametrov explicitný | `E0_METHOD` | dáta nesmú určiť tvar, čas, šírku ani amplitúdu |

Tento pas ukazuje neprítomnosť priameho rozporu v už zvolenej kanonickej
stavovej triede, ale nie neprázdnosť úplného `F_K^(3)`: chýba D03 transfer,
D04 produktový ledger a D07 source-off mechanizmus.

### 6.4 Prvé bezrozmerné odhady — iba E3_PROVISIONAL

Keďže absolútny exit scale ešte nie je odvodený, prvý odhad sa zapisuje
bezrozmerne. Nech `H_*` je lokálne Hubbleovo tempo na zatiaľ neurčenej
exit trajektórii, `M_Pl,red` je redukovaná Planckova hmotnosť a
`3 M_Pl,red^2 H_*^2` je kritická hustota v tom istom lokálnom exit bode:

```text
f_e,*   = rho_e,* / (3 M_Pl,red^2 H_*^2),
s_m     = sign[V_e''(phi_e,*)],
r_|m|   = sqrt(|V_e''(phi_e,*)|) / H_*.
```

Prvé logaritmické pracovné kotvy, nie prior ani fyzikálny interval, sú:

| Veličina | Prvé kotvy | Prečo ich vôbec držať | Čo neznamenajú |
|---|---|---|---|
| `r_|m|` | `0.1, 1, 10`, vždy s `s_m=-1` alebo `+1`; presne plochá hranica je osobitne `r_|m|=0, s_m=0` | rozlíšia veľkosť krivosti voči Hubbleovmu treniu a zachovajú konkávnu, plochú aj konvexnú časť | nie je to odhad hmotnosti `m` bez `H_*`; oscilujúci stabilný režim navyše vyžaduje lokálne `s_m=+1` |
| `f_e,*` | `10^-4, 10^-2, 10^-1, 1` | pokrývajú spectator, subdominantný aj dominantný reheating rezervoár bez potichu zvolenej amplitúdy | nie je to povolený interval ani fit na `Delta N_eff` |
| floor minima | prvý svedok `V_min=0` | odstráni iba reziduálny vacuum-energy floor a nepridá novú konštantu | samo nedáva `rho_e -> 0`; oscilácie/kinetická energia zaniknú alebo sa prevedú iba cez D03/D07 dynamiku |

Legacy thermal benchmark dáva iba kontrolu rádu:

```text
2 / 106.75 approximately 1.9e-2                    (starý high-g* podiel),
X_steam / X_r = 6.8100197e-7 / 9.55038e-5
              approximately 7.1e-3                (dnešný legacy radiačný podiel).
```

Tieto dve čísla sú `E3_LEGACY_SENSITIVITY`, nie cieľ. Ak budúca D04
konverzná účinnosť do pary bude `0 < epsilon_s <= 1`, energy ledger dá iba
schematickú hranicu `f_e,* >= f_s,*/epsilon_s`, pričom oba podiely musia byť
definované v tej istej epoche a voči tej istej normalizačnej hustote.
Dnešný legacy podiel sa sem nesmie vložiť bez entropy mapy medzi produkciou
a dneškom. Dnes nie je schválená ani `epsilon_s`, ani `f_s,*`, ani entropy
mapa. Absolútne `H_*`, teplota, `sqrt(|V_e''|)`, `V_0` a `phi_e,*` preto
zostávajú `NOT_DERIVED`.

### 6.5 Tri analytické triedy pre prvý svedok

| ID | Kandidát | Nové tvarové stupne voľnosti | Silná stránka | Otvorené riziko |
|---|---|---:|---|---|
| `V1-P1` | `V_e=V_min + 1/2 m_e^2 (phi_e-phi_0)^2` | po `V_min=0` a posune počiatku v izolovanom potential sektore jeden scale `m_e`; budúci D03 coupling sa musí posunúť konzistentne | najjednoduchšie stabilné minimum; prirodzený prechod pri `sqrt(V_e'')/H=O(1)` | samotný potenciál nedáva transfer ani steam branch; bez D06 vychýlenia nemá určenú energiu |
| `V1-P2` | `V_e=V_min+V_0[1-exp(-(phi_e-phi_0)/mu)]^2` | najmenej `V_0,mu` | plateau a stabilné minimum v jednom lokálnom tvare | viac parametrov; exit a počiatočná strana musia byť odvodené |
| `V1-P3` | `V_e=V_min+lambda_e(phi_e^2-v_e^2)^2/4` | najmenej `lambda_e,v_e` | lokálny symmetry-breaking prechod a dve minimá | doménové steny/defekty a vetva vákua vyžadujú samostatnú M7–M8 kontrolu |

Čistý monotónny exponenciálny potenciál sa nedáva medzi prvé tri: bez
doplneného mechanizmu nemá prirodzené stabilné minimum/source-off a mohol by
sa zameniť so starým efektívnym A1 backgroundovým skalárom. Nie je tým
globálne vylúčený; iba nemá prioritu ako prvý minimálny svedok.

Procesne najúspornejší kandidát na prvý analytický svedok je `V1-P1` s
`V_min=0`. Testuje iba stavový/potenciálový mantle. Bez D03 transferu, D06
počiatočného vychýlenia a D07 source-off nie je reheatingovým mechanizmom
ani úplným `F_K^(3)` svedkom. Toto je odporúčanie na autorovu voľbu, nie
prijatá fyzika.

### 6.6 Autorova voľba V1-P1 a closure rozsahu D02

Na jedinú aktívnu otázku `V1-P1/P2/P3/custom` autor teórie 2026-07-22
odpovedal:

> Pokračuj

V priamom kontexte odporúčania bez inej otvorenej voľby sa pokyn zachytáva
ako schválenie:

```text
SELECTED_POTENTIAL_CLASS = V1-P1
V_e(phi_e) = 1/2 m_e^2 phi_e^2
V_min = 0
V1-D02 = CLOSED_FORM_ONLY
m_e = DEFERRED_TO_V1-D06
phi_e_initial_and_dot_phi_e_initial = DEFERRED_TO_V1-D06
RUN_AUTHORIZED = false
```

Počiatok poľa je zvolený v minime `phi_0=0`; každý budúci coupling v D03/D08
sa musí zapísať v tej istej posunutej konvencii. Closure D02 určuje stav,
tenzor, doménu a funkčnú triedu potenciálu, nie jeho numerickú mierku,
počiatočnú energiu, transfer, branch ratio alebo source-off dôkaz.

## 7. Aktívny blok V1-D03 — lokálny transfer a kandidát clocku

Po výbere kvadratického poľa sa musí odvodiť lokálny zákon odoberajúci
energiu z `e` a až v D04 ju rozdeliť medzi paru a ostatné produkty. D03 musí
pred autorovou voľbou uzavrieť najmenej:

1. kovariantný source vector a jeho FLRW projekciu;
2. lokálny future-directed frame, ktorý ostane definovaný aj pri
   `dot(phi_e)=0` v bodoch obratu oscilácie;
3. invariantný clock z lokálnych stavov, nie z voľného kozmického času;
4. znamienko a rozmery transfer rate;
5. nulový limit coupling/rate a limit vyčerpaného rezervoára;
6. oddelenie celkového drainu v D03 od steam branch a produktového ledgera
   v D04;
7. prvé iba `E3_PROVISIONAL` bezrozmerné kotvy, kým mikroskopický coupling
   a matrix element zostávajú otvorené v D08.

Scalar-rest-frame `u_e^mu=-partial^mu phi_e/sqrt(2X_e)` sa pri `X_e=0`
stáva nedefinovaný. D03 preto nesmie potichu použiť `u_e^mu` cez body obratu;
musí zvoliť pravidelný lokálny frame alebo ekvivalentný source zápis, ktorý
má v tomto limite jednoznačný nulový výsledok.

### 7.1 Presná identita a oddelenie D03 od D04

Pre kanonický skalár platí mimo jeho interakčného operátora identita

```text
nabla_mu T_e^(mu nu)
  = [Box phi_e - V_e'(phi_e)] partial^nu phi_e.
```

D03 najprv definuje celkový drain `S_D^nu` z rezervoára:

```text
nabla_mu T_e^(mu nu) = -S_D^nu.
```

Až D04 musí zaviesť jednotlivé produkty tak, aby

```text
S_D^nu = S_s^nu + sum_other S_A^nu,
sum_all_components Q_A^nu = 0.
```

Tým sa v D03 nevkladá steam branch ratio ani tvrdenie, že všetka odobratá
energia ide do pary.

### 7.2 Kandidát V1-T1 — perturbatívny lokálny Markovský drain

Nech `U_L` označuje iba Type-I doménu, v ktorej má celkový lokálny
`T_tot^(mu nu)` jednoznačný future-directed jednotkový časupodobný Landauov
vlastný vektor `u^mu` a `Theta=nabla_mu u^mu>0`:

```text
T_tot^(mu nu) u_nu = -rho_tot u^mu,
u_mu u^mu = -1,
D_u phi_e = u^alpha partial_alpha phi_e.
```

Mimo `U_L` kandidát T1 nedefinuje frame ani clock. Ak sa jedinečnosť frame
stratí presne v bode `partial_mu phi_e=0` a `Gamma_e` má konečný spojitý
limit pozdĺž `U_L`, iba source možno rozšíriť nulovou kontinuitou;
`H_loc` a clock tam tým definované nie sú. Použitie pozdĺž celej
trajektórie preto neskôr vyžaduje buď dôkaz zotrvania v `U_L`, alebo inú
kovariantnú kongruenciu.

Nech `J_a` sú nezávislé lokálne stavové invarianty a mikroskopické dáta,
ktoré neobsahujú `Gamma_e` ani z nej odvodené `chi_Gamma`. Prvý lokálny
parent-drain kandidát v `U_L` postuluje samostatnú dynamickú rovnicu a z
nej source:

```text
Box phi_e - V_e'(phi_e) = Gamma_e(J_a) D_u phi_e,
S_D^nu = -Gamma_e(J_a) (D_u phi_e) partial^nu phi_e,
Gamma_e >= 0,
[Gamma_e] = energy.
```

Tenzorová conservation identita sama v bode `partial_mu phi_e=0` neurčuje
skalárnu rovnicu, pretože obe jej strany zaniknú. Vyššie uvedená rovnica
poľa je preto definíciou T1 (a spojitou lokálnou extenziou), nie výsledkom
delenia conservation identity gradientom poľa.

V presnom homogénnom FLRW limite
`partial^nu phi_e=-(D_u phi_e)u^nu`, preto

```text
S_D^nu = Gamma_e (D_u phi_e)^2 u^nu,
ddot(phi_e) + (3H_loc + Gamma_e) dot(phi_e) + m_e^2 phi_e = 0,
dot(rho_e) + 3H_loc(rho_e+p_e) = -Gamma_e dot(phi_e)^2.
```

Source má správne znamienko pre drain pri `Gamma_e>=0`. Pri bode obratu
`D_u phi_e=0` dá priamo `S_D^nu=0` a nepoužíva singularitu `1/sqrt(X_e)`.
Mimo FLRW sa celý štvorvektor rozloží na časovú a priestorovú časť; budúci
D04/M7 audit nesmie priestorovú časť vopred zahodiť.

Kandidát platí iba v scope

```text
PERTURBATIVE_MARKOVIAN_LOCAL_DRAIN
UNIQUE_TIMELIKE_LANDAU_FRAME
NO_PREHEATING_OR_PARAMETRIC_RESONANCE_CLAIM
```

Konštantná mikroskopická šírka je najjednoduchší podprípad, nie odvodená
hodnota. Jej pôvod, matrix element a prípadná závislosť od poľa/teploty
patria D08; numerická hodnota patrí D06.

### 7.3 Lokálne diagnostiky, kandidát clocku a prvé E3 kotvy

V expandujúcej doméne s `Theta=nabla_mu u^mu>0` definujme

```text
H_loc = Theta/3,
chi_m = m_e/H_loc = 3m_e/Theta,
chi_Gamma = Gamma_e/H_loc = 3Gamma_e/Theta,
zeta = Gamma_e/m_e = chi_Gamma/chi_m.
```

Ide o lokálne skaláre; žiadny z nich nepoužíva voľný kozmický čas alebo
globálne `H0`. `chi_m` odlišuje frozen/transition/oscillatory dynamiku a
`chi_Gamma` silu drainu voči expanzii. Pár
`chi=(chi_m,chi_Gamma)` je zatiaľ iba odvodený lokálny diagnostický pár a
kandidát clocku. Jeho evolúcia ani monotónna vetva zatiaľ nie sú odvodené;
preto `CLOCK_STATUS=DIAGNOSTIC_ONLY` a D03 zostáva čiastkový. Navyše
`chi_m`, `chi_Gamma` a `zeta` nie sú tri nezávislé parametre: každý bod musí
spĺňať `zeta=chi_Gamma/chi_m`.

Prvé pracovné body sú iba `E3_PROVISIONAL`:

| Veličina | Kotvy | Účel | Nonclaim |
|---|---|---|---|
| `chi_m` | `0.1, 1, 10` | frozen, prechodový a oscilujúci režim | bez hodnoty `m_e` alebo `H_loc` |
| `chi_Gamma` | `0.1, 1, 10` | slabý, prechodový a rýchly drain voči expanzii | nie je interval povolenej decay rate |
| `zeta=Gamma_e/m_e` | `10^-2, 10^-1`; `1` iba hranica scope | prvý screen perturbatívnej width; `zeta=1` testuje stratu tejto aproximácie | sama nerozhoduje underdamped režim ani nie je odvodený coupling/width |

Pre `zeta` neexistuje v súčasnom korpuse tvrdý číselný prah. Uvedené body
iba rozlíšia bezpečne slabý test od hranice, kde lokálny `Gamma dot(phi)`
ansatz už nesmie predstierať plnú neperturbatívnu produkciu.

Pri lokálnej frozen-coefficient aproximácii kvadratického FLRW oscilátora
zahŕňa tlmenie aj expanziu:

```text
q_damp = (3H_loc + Gamma_e)/m_e = 3/chi_m + zeta,
underdamped iba ak q_damp < 2.
```

Pri časovo premenlivých koeficientoch to nie je globálne kritérium, iba
lokálny E3 screen.

### 7.4 Alternatívy a odporúčanie

| ID | Trieda | Výhoda | Prečo nie je prvá |
|---|---|---|---|
| `V1-T1` | lokálny perturbatívny Markovský drain vyššie | minimálny regular source, presný null limit, jasný energy drain | width a produktový kernel ešte musia prísť z D08 |
| `V1-T2` | action-derived explicitný coupling poľa k produktom a z neho odvodený collision kernel | mikrofyzikálne najsilnejší a určí width/branch | bez D08 produktových polí a interakcie ho dnes nemožno zapísať |
| `V1-T3` | neperturbatívna rezonancia/preheating | môže zachytiť silnú koherentnú produkciu | nie je všeobecne lokálnym `Gamma_e dot(phi_e)` zákonom; vyžaduje módové rovnice a samostatný lifecycle |

Primárna literatúra o reheatingu výslovne upozorňuje, že silná počiatočná
parametrická rezonancia sa nedá všeobecne nahradiť trením
`Gamma_e dot(phi_e)`; časovo závislá width navyše závisí od konkrétneho
couplingu. Preto je `V1-T1` odporúčaný iba ako prvý perturbatívny D03
analytický svedok, nie ako úplný reheatingový zákon:

- Kofman, Linde, Starobinsky, *Reheating after Inflation*,
  `arXiv:hep-th/9405187`;
- Ahmed, Grzadkowski, Socha, *Implications of time-dependent inflaton decay
  on reheating and dark matter production*, `arXiv:2111.06065`.

Autorova voľba T1 by uzavrela iba tvar parent drainu a jeho Type-I doménu.
Neuzavrela by globálnu existenciu frame ani clock, steam branch, matrix
element, numerickú width alebo source-off toleranciu; D03 by po tejto voľbe
zostal `PARTIAL`, kým sa nevyberie a neoverí clock branch.

## 8. Autorov smer: constraint-first rekonštrukcia hmota–para–popol

Autor 2026-07-22 neurčil vybrať hotový ansatz podľa podobnosti. Určil
odvodiť najmenšiu funkčnú rodinu zo spoločného prieniku:

```text
pozorovania + filozofia bunkového vesmíru + už vykonané výpočty
  -> dovolené lokálne funkcie
  -> forward trajektórie
  -> spätná recovery známych výsledkov.
```

Pozorovania tu smú určiť okrajové podmienky a vyradiť funkcie, nie
potichu vyrobiť voľný čas, amplitúdu alebo branch ratio. T1 preto zostáva
možným kovariantným obalom parent drainu, nie zvolenou hotovou odpoveďou.

### 8.1 Bunková identita skorého rezervoára

Starší zákaz `no fundamental inflaton / no new fundamental field` zostáva
tvrdý. Preto sa `phi_e` smie v tejto vetve interpretovať iba ako efektívna
lokálna kolektívna súradnica exit stavu existujúceho bunkového rezervoára,
nie ako nové fundamentálne inflatónové pole. D02 je naďalej uzavreté iba
`CLOSED_FORM_ONLY`; fyzikálnu mapu `phi_e <-> cellular state` musí neskôr
uzavrieť D05/D08.

V pevnej Planckovej konvencii `V_P=l_P^3` a `rho_P=E_P/V_P` definujme
lokálny bezrozmerný stav

```text
rho_e = X_e + V_e(phi_e),
X_e = 1/2 (D_u phi_e)^2              # homogénna FLRW projekcia
y_e = rho_e/rho_P,
chi_E = y_e^(1/4).
```

Pre kanonický rezervoár v expandujúcom FLRW a nezáporný parent drain platí

```text
dot(rho_e) = -3H (D_u phi_e)^2 - Q_D <= 0.
```

Nerovnosť platí na homogénnej expandujúcej vetve s `H>=0` a `Q_D>=0`.
`y_e` je vpred nezvyšujúci lokálny stav, ale môže mať stacionárne
intervaly. Preto platí `CLOCK_STATUS=DIAGNOSTIC_ONLY`. Plnohodnotný clock
vznikne až po dôkaze

```text
3H (D_u phi_e)^2 + Q_D > 0
```

mimo nanajvýš izolovaných bodov pozdĺ celej použitej exit trajektórie.
Stav nepoužíva voľný `t`, `ln(a)`, globálne `H0` ani realizovaný mód `k`.

### 8.2 Najmenší produktový rebrík

Označme `M` bezprostredný hmotný/SM zvyšok, `s` paru a `C` popol.
Filozofia neurčuje tri nezávislé prompt vetvy. Určuje sekvenčný rebrík:
para je odviazaný vlnový produkt parent udalosti a popol je neskoršie
dokončenie spracovania hmotného zvyšku. Produktová vrstva preto potrebuje
jednu prompt funkciu a jednu lokálnu dokončovaciu sadzbu:

```text
beta_s(Y_D) in [0,1]   # podiel parent drainu do pary
Gamma_C(Y_C) >= 0      # lokálna sadzba M -> C
```

V energetickej projekcii Landauovho frame potom

```text
Q_s = beta_s Q_D,
Q_e_to_M = (1-beta_s) Q_D,
Q_M_to_C = Gamma_C(Y_C) rho_M,

dot(rho_M) + 3H(rho_M+p_M) = Q_e_to_M - Q_M_to_C,
dot(rho_C) + 3H(rho_C+p_C) = Q_M_to_C,
dot(rho_s) + 3H(rho_s+p_s) = Q_s.
```

Po sčítaní so stratou rezervoára `-Q_D` sa všetky zdroje bodovo
vynulujú. Zápis odstraňuje jeden nadbytočný prompt branch a na rozdiel od
kohortovej pravdepodobnosti zostáva lokálny aj pri kontinuálnej produkcii.
Nie je ešte úplným collision
operatorom: kolmé recoil vektory, birth frame, tlak, shear a noise patria
D08. Existujúci neskorý A1 kanál zostáva oddelený `F -> C`; po skorom
source-off nesmie vytvárať novú hmotu `M` ani významnú paru.

### 8.3 Prvý kandidát parnej funkcie bez nového voľného parametra

Staršie A12 obsahuje dve použiteľné asymptoty, ale nie hotový zdroj:

1. pri lokálnej energii udalosti Planckovho rádu je relatívna účinnosť
   vlnového produktu rádu jedna a podmienený rovnovážny pomer je
   `rho_s/rho_SM = 2/g_*`;
2. pri malej energii na bunku klesá účinnosť ako
   `(E_cell/E_P)^2`.

Ak `y_e=E_cell/E_P=rho_e/rho_P` v Planckovej bunke, najjednoduchší
rekonštrukčný kandidát bez nového čísla na doméne `0<=y_e<=1` je

```text
r_s(y_e) = (2/g_*) y_e^2,
beta_s(y_e) = r_s(y_e)/(1+r_s(y_e)),
g_* = 106.75   # iba conditional high-temperature endpoint SM state count
```

Stav tejto rovnice je `HYPOTHESIS_RECONSTRUCTED_FROM_EXISTING_ASYMPTOTES`,
nie odvodený steam kernel ani matematicky jediná bezparametrická
interpolácia. Pri `y_e=1` reprodukuje iba podmienený rovnovážny pomer
`rho_s/rho_M=2/g_*` voči bezprostrednému SM/hmotnému produktu `M`, nie voči
už vytvorenému súčtu `M+C`. Pri `y_e` rádu `10^-123` dáva parný podiel rádu
`10^-248`, teda známy nulový neskorý limit. Nepoužíva legacy
`Delta N_eff=0.0535` ako cieľ. Doména `y_e>1` je neauditovaná extrapolácia.

Kritický spätný test je opačný: ak odvodená exit trajektória nikdy
nedosiahne `y_e` dostatočne blízke rovnovážnej oblasti, táto funkcia
nevytvorí relevantnú paru a vetva zomrie. Para vytvorená pred približne
1280 e-foldmi sa nesmie započítať; integrál musí pochádzať z exitu alebo
rethermalizácie po poslednom veľkom riedení.

### 8.4 Popol nie je samostatný voľný branch

Pre jednu označenú kohortu narodenú s `Tau_C=0` sa dokončovacia
pravdepodobnosť odvodí z lokálneho hazardu spracovania hmotného zvyšku:

```text
D_u Tau_C = Gamma_C(Y_C),
Tau_C|_birth = 0,
d_C = 1-exp(-Tau_C),
Tau_C = integral Gamma_C(Y_C) d tau_local.
```

Tento zápis garantuje `0<=d_C<=1`, nulový limit `Gamma_C->0` a absorpčný
limit pri veľkom optickom čase. Pri kontinuálnej produkcii sa v
backgroundových rovniciach nepoužíva `d_C Q_D`; používa sa lokálny tok
`Q_M_to_C=Gamma_C rho_M`, prípadne neskôr vekovo rozlíšená distribúcia
kohôrt. `Gamma_C(Y_C)` zatiaľ nie je odvodená. Dnešný pomer hmoty a
popola obmedzuje iba integrovaný dokončovací tok; sám neurčuje jeho lokálnu
funkciu a nesmie sa použiť ako skrytý fit.

Ako prvý scale-free `RECONSTRUCTION_ANSATZ` sa smie pred odvodením porovnať
jednoparametrická power-law family pre každú sadzbu

```text
Gamma_D(y_D) = t_P^-1 y_D^alpha_D,   y_D=y_e, alpha_D>0,
Gamma_C(y_C) = t_P^-1 y_C^alpha_C,   y_C=OPEN_LOCAL_STATE, alpha_C>0.
```

Porovnanie Planck-rate intuície s dnešným efektívnym A1 rate dáva iba
cross-sector comparator exponentu blízkeho `1/2`. Nie je to odvodenie ani
silný hint pre `Gamma_D`, pretože dnešný A1 rate patrí oddelenému palivu
`F`, nie skorému rezervoáru `e`. Použiť ho bude možné iba po budúcom
dôkaze spoločného operátora. Dovtedy sa `alpha_D=1/2` ani
`alpha_C=alpha_D` nesmú vložiť do runnera alebo označiť za predikciu.

### 8.5 Povinný spätný test funkčnej rodiny

Pred akýmkoľvek fitom musí jedna forward trajektória pre každú vopred
zmrazenú funkciu prejsť:

1. **ledger recovery:**
   `-Q_D + Q_s + (Q_e_to_M-Q_M_to_C) + Q_M_to_C = 0` bodovo a neskôr aj
   ako štvorvektor;
2. **source-off recovery:** pri vyčerpaní `e` zaniknú parent zdroje
   `Q_s,Q_e_to_M` bez voľného kozmického času; dokončovací tok
   `Q_M_to_C` smie dobehnúť a zanikne až pri `Gamma_C rho_M=0`;
3. **post-source scaling:** po vypnutí parent aj completion toku platí
   `a^4 rho_s=const` a pre studený popol `a^3 rho_C=const`;
4. **late A1 recovery:** po vypnutí `e` zostáva existujúci `F -> C` ledger
   plus prípadný oddelený dobiehajúci tok `M -> C`. Zdroj popola je počas
   prekryvu
   `Q_C_total=Q_F_to_C^A1+Q_M_to_C`; oba členy majú odlišný rezervoár.
   Na čistý neskorý A1 ledger sa systém presne redukuje až pri
   `Q_D=0` aj `Q_M_to_C=0`, vždy bez steam source;
5. **early survival:** dnešná para sa počíta iba z
   `integral a^4 beta_s Q_D d tau` po poslednom veľkom riedení;
6. **matter/ash moment:** pozorované konečné zásoby testujú primárny tok
   `(1-beta_s)Q_D` a následný lokálny tok `Gamma_C rho_M`, nie ručne
   vybrané okamžité podiely;
7. **no-target check:** `S8`, `H0`, legacy `Delta N_eff`, `0.90 K`, `53 GHz`
   ani `f_R,direct` sa nepoužijú na konštrukciu funkcie; až zmrazený
   výsledok sa s nimi porovná v ich platnom scope.

Prvý krok je symbolický feasibility/backward audit týchto identít a
asymptôt. Python zostáva zakázaný, kým sa nezmrazí konečná rodina,
počiatočné podmienky a STOP kritériá.

### 8.6 Počet zostávajúcich voľností

| Objekt | Aktuálny stav |
|---|---|
| lokálny stav `y_e` | `DERIVED_LOCAL_STATE / CLOCK_STATUS=DIAGNOSTIC_ONLY`; globálny clock otvorený |
| parent drain shell `Q_D` | T1 formulačne konzistentný, autorom nezvolený |
| `Gamma_D(y)` | jedna otvorená funkcia; scale-free family iba rekonštrukčný hint |
| `beta_s(y)` | kandidát bez nového voľného parametra pri podmienenom high-T `g_*`; nie jedinečný |
| `Gamma_C(y_C)` | jedna otvorená funkcia aj otvorený lokálny stav; kohortové `d_C` je iba odvodený dôsledok |
| počiatočná energia a `m_e` | D06, otvorené |
| recoil/matrix element/noise | D08, otvorené |

Výsledkom tejto etapy preto nie je jediná odvodená funkcia, ale podstatne
užší a falzifikovateľný systém: jeden parent rate, jeden fixed-form steam
kandidát a jeden lokálny completion rate. Najbližší audit má
rozhodnúť, či `y_e`, `beta_s` a rebríkový ledger naozaj prejdú M0–M2 a
či známe asymptoty nie sú dvojito započítané.

### 8.7 Prvý analytický backward screen B0 — energia poslednej produkcie pary

Tento screen testuje iba rekonštruovaný kandidát `beta_s`, nie celú S-M
vetvu. Predpokladajme úzky posledný exit/rethermalization interval, v ktorom
je `y_e` približne `y_x` a bezprostredné produkty `s` a `M` sa porovnávajú
pri narodení. Potom presne

```text
R_sM,x = Q_s/Q_e_to_M
       = beta_s/(1-beta_s)
       = r_s(y_x)
       = (2/g_*) y_x^2.
```

Podmienený high-temperature endpoint staršieho A12 je
`R_sM,eq=2/g_*`. Rekonštruovaná funkcia ho teda obnoví iba ak

```text
(2/g_*) y_x^2 = 2/g_*  ->  y_x = 1
```

na auditovanej doméne `0<=y_x<=1`. Pre každý sub-Planckovský exit je
pomer voči tomuto endpointu potlačený presne faktorom `y_x^2`.

Ak sa navyše iba ako tepelný comparator použije
`y_x approximately (T_x/T_P)^4`, potom

```text
R_sM,x/R_sM,eq approximately (T_x/T_P)^8.
```

Historická A13 mierka zamrznutia `T approximately 2–7 x 10^9 GeV` nie je
odvodená exit teplota a nesmie sa ňou funkcia kalibrovať. Ak by sa však
neskôr ukázalo, že exit leží na tejto mierke, pri
`T_P approximately 1.2 x 10^19 GeV` by potlačenie bolo iba rádu
`10^-78` až `10^-74`. Relevantný tepelný parný relikt by tento kandidát
nevytvoril.

Preto B0 dáva ostrý rozhodovací strom:

1. `y_x approximately 1` po poslednom veľkom riedení: kandidát môže
   prežiť, ale exit energetika musí vysvetliť obnovu Planckovej lokálnej
   udalosti;
2. `y_x << 1` a `E_cell/E_P=rho_e/rho_P`: kandidát `beta_s` predikuje
   zanedbateľnú paru a legacy tepelný výsledok sa neobnoví;
3. lokálna energia udalosti nie je `rho_e V_P`: treba odvodiť odlišnú
   bunkovú mapu, nie ju zvoliť podľa želaného výsledku;
4. exit vytvára paru cez samostatný relaxation/collision operator: tento
   prompt branch kandidát sa vyradí a otvorí sa iná vopred definovaná
   funkčná trieda.

Stav B0 je `ANALYTIC_CONDITIONAL_SCREEN`, nie fyzikálny STOP. Bez D05/D06
mapy `cellular exit state -> E_event,y_x` ešte nevieme vybrať vetvu 1–4.
Screen však už ukazuje, že pôvodný tepelný pomer, dlhé zrýchlené riedenie a
jednoduchá `y^2` produkcia nemôžu byť súčasne iba slovné tvrdenia; ich
spoločná energetická mapa musí prejsť tento backward screen.

### 8.8 Analytický backward screen B1 — 1280 e-foldov a lokálna energia

B1 pridáva k B0 jednu explicitnú, falzifikovateľnú mapu. Predpokladajme:

1. kolektívny rezervoár `e` je energia, ktorá nesie dlhú zrýchlenú fázu
   staršieho A13;
2. pred terminálnym exit drainom sleduje efektívnu stavovú rovnicu
   `w_e=-1+delta`;
3. na začiatku tejto fázy `y_i=rho_e,i/rho_P=1`;
4. počet e-foldov po poslednú relevantnú produkciu je `N=1280`.

Pri nezápornom parent draine dáva continuity rovnica bez voľného profilu

```text
d ln(rho_e)/dN = -3 delta - Q_D/(H rho_e) <= -3 delta,
y_x <= y_i exp(-3 delta N).
```

Rovnosť platí iba v subcase `Q_D=0` počas celej predterminálnej fázy;
každý skorší kladný drain hranicu iba sprísni.

Pre existujúce `delta=0.02297` a `N=1280`:

```text
3 delta N approximately 88.2,
y_x <= exp(-88.2) approximately 10^-38.3,
R_sM,x/R_sM,eq = y_x^2 lesssim 10^-76.6.
```

B1 vyjadruje tú istú podmienenú A13 backgroundovú mapu priamo v lokálnej
premennej `y_e` a ukazuje jej dôsledok pre `beta_s`; nie je nezávislým
potvrdením A13 ani B0. V presnom scope predpokladov 1–4 preto jednoduchý prompt
kandidát `beta_s proportional y_e^2` **neobnoví relevantný tepelný parný
pomer pri exite**.

Rozsudok je

```text
B1 = CONDITIONAL_FUNCTION_FAIL
scope = SHARED_1280_EFOLD_BACKGROUND_ENERGY_MAP
```

Nie je to STOP celej parnej vetvy ani zmena K4. Zostáva najmenej päť
fyzikálne odlišných možností, ktoré sa nesmú zlúčiť voľným parametrom:

1. `e` nie je energia A13 backgroundu; treba odvodiť jeho samostatnú
   cellular mapu a energetický ledger;
2. lokálna energia jednej exit udalosti zostáva Planckovská aj pri malej
   priemernej `rho_e V_P`; treba odvodiť event measure a počet udalostí;
3. para nevzniká prompt branchom `beta_s`, ale exitovým relaxation/collision
   operatorom, ktorý ju po poslednom riedení znovu vytvorí alebo
   rethermalizuje;
4. rekonštruovaný prompt tvar `beta_s proportional y_e^2` je nesprávny a
   mikrofyzika odvodí inú lokálnu prompt funkciu alebo ďalšie invarianty;
5. niektorá zo spoločných A13 podmienok `w_e=-1+delta`, `y_i=1` alebo
   `N=1280` neplatí pre poslednú relevantnú produkciu.

B1 teda zúžil D03a: pred odvodením `Gamma_D` sa musí vybrať a dokázať
jedna z explicitne rozlíšených energetických máp alebo odvodiť iná.
Pozorovaný parný rozpočet sa na ich
výber nepoužije; bude až následným testom zmrazenej mapy.

### 8.9 Dependency split B2 — energia udalosti verzus miera udalostí

B1 ukazuje, že skalár `y_e=rho_e/rho_P` sám nemôže súčasne určovať
makroskopický drain aj vlnovú účinnosť jednej diskrétnej udalosti. Minimálny
bunkový operátor musí oddeliť:

```text
R_J(Y) >= 0       # invariantná miera udalostí na fyzický objem a vlastný čas
E_J(Y) >= 0       # energia odobratá rezervoáru jednou udalosťou
epsilon_J=E_J/E_P # lokálna energia udalosti, nie priemerná energia bunky
```

V prirodzených jednotkách `[R_J]=E^4`, `[E_J]=E` a priestorovo časová
projekcia parent drainu je

```text
Q_D = R_J E_J,                 [Q_D]=E^5.
```

Pri `V_P=l_P^3` definujme bezrozmerný počet udalostí na Planckov bunkový
štvorobjem a bezrozmerný drain

```text
nu_J = R_J V_P t_P,
j_D  = Q_D V_P t_P/E_P = nu_J epsilon_J.
```

Makroskopická continuity rovnica teda určuje iba súčin
`nu_J epsilon_J`. Bez ďalšej bunkovej fyziky nevie oddeliť, či drain tvorí
veľa slabých udalostí alebo málo energetických udalostí.

Parný kandidát sa teraz musí viazať na energiu udalosti:

```text
r_s(epsilon_J) = (2/g_*) epsilon_J^2,
beta_s(epsilon_J) = r_s/(1+r_s),
Q_s = beta_s(epsilon_J) R_J E_J.
0 <= epsilon_J <= 1.
```

Ide o ten istý `HYPOTHESIS_RECONSTRUCTED` prompt kandidát, nie odvodený
event kernel; `epsilon_J>1` je neauditovaná extrapolácia. Faktor `2/g_*`
sa použije presne raz ako birth ratio `Q_s/Q_M`. Nesmie sa neskôr znovu
vložiť ako druhá nezávislá normalizácia produkcie. Následná
entropy/decoupling mapa je evolúcia produktov, nie druhé vetvenie energie.

V slabom limite je preto

```text
j_s approximately (2/g_*) nu_J epsilon_J^3.
```

To je nový rozlišujúci dôsledok: dva operátory s rovnakým `Q_D` môžu mať
radikálne odlišný parný výťažok.

| Mikročítanie | `epsilon_J` | `nu_J` pri rovnakom `j_D` | Dôsledok pre paru |
|---|---:|---:|---|
| distribuované slabé spracovanie | približne `y_e` | približne `j_D/y_e` | B1 potlačenie `beta_s proportional y_e^2` |
| vzácne Planckovské udalosti | približne `1` | približne `j_D` | podmienený high-T podiel na udalosť môže zostať nenulový |
| všeobecná bunková mapa | odvodené `epsilon_J(Y)` | `j_D/epsilon_J` | testuje sa bez fitu |

Druhý riadok nie je riešením ani povolením nastaviť
`epsilon_J=1`. Musí sa dokázať, odkiaľ jednotlivá udalosť vezme energiu,
ako sa lokálne odpočíta z `rho_e` a prečo jej miera neporuší pozitivitu.
Východisková lokálna identita je

```text
dot(rho_e) + 3H(rho_e+p_e) = -Q_D.
```

Na jednotku komovingového objemu preto

```text
integral[t_i,t_f] a^3 Q_D dt
  = a_i^3 rho_e,i - a_f^3 rho_e,f
    - integral[a_i^3,a_f^3] p_e d(a^3).
```

Každá jednotlivá udalosť navyše musí spĺňať
`E_J<=E_available` v jej odvodenom lokálnom kauzálnom zbernom regióne.
Definícia tohto regiónu je pre vzácne Planckovské udalosti otvorená.
Celý zápis musí mať presný štvorvektorový recoil ledger.

Vzácne udalosti navyše generujú discreteness/shot noise. Jeho
Poissonovský, sub-Poissonovský alebo korelovaný charakter musí odvodiť ten
istý mikroskopický event operator vrátane vyšších momentov bodového procesu.
`R_J,E_J` určujú iba prvý moment; D10 potrebuje aj eventové korelácie/noise
kernel, napríklad `two_point(delta J,delta J)`. Tým B2 priamo prepája
D03/D04 s D08/D10 a zabraňuje, aby sa správny background dosiahol za cenu
nežiaducej izokurvatúry.

Stav B2 je

```text
EVENT_FACTORIZATION = REQUIRED_FOR_B2_DISCRETE_EVENT_BRANCH
R_J(Y) = OPEN_FUNCTION
E_J(Y) = OPEN_FUNCTION
MACRO_IDENTIFIABILITY = PRODUCT_ONLY
```

V rámci B2 diskrétnej eventovej vetvy sa nemal hľadať ďalší tvar `beta_s`,
ale konečná constraint-first sada kandidátov `E_J(Y),R_J(Y)`. Tento krok bol
vykonaný v B3, oddiel 8.10. Jeho interný výsledok je `PASS_B3` iba ako
`FINITE_HYPOTHESIS_MAP` pre deterministické `F1–F3`; nejde o výber eventového
operátora. Relaxačný alebo iný prompt operator zostáva legitímnou samostatnou
možnosťou z B1.

### 8.10 B3 — A13 účtovný split a konečný katalóg granularít udalosti

B2 oddelil mieru a energiu udalosti, ale ešte neurčil ich spoločný súčin.
Najprv treba odstrániť jednu možnú dvojitú evidenciu. Pre všeobecný
homogénny parent platí

```text
q_D = Q_D/(H rho_e),
d ln(rho_e)/dN = -3(1+w_e) - q_D.
```

Historická A13 backgroundová škála `rho_e proportional a^(-3 delta)`
určuje iba súčet

```text
3(1+w_e) + q_D = 3 delta.
```

Sama teda nerozhoduje, či sa geometrická réžia prejaví ako tlaková práca
rezervoára alebo ako explicitný transfer do produktov. Bez nového voľného
mixing parametra existujú dva krajné účtovné zápisy:

```text
P: w_e = -1+delta,  q_D^(delta)=0,
T: w_e = -1,        q_D^(delta)=3 delta.
```

Oba dávajú rovnaké škálovanie samotného parent rezervoára
`rho_e proportional a^(-3 delta)`, ale iba vetva `T` odovzdáva energiu do
`M/s/C`. Nedávajú tým automaticky rovnaké celkové `H(a)`, pretože vytvorené
produkty majú iné tlaky a spätne gravitačne pôsobia. Zápis

```text
w_e=-1+delta  AND  q_D^(delta)=3 delta
```

by dal pokles `a^(-6 delta)` a tú istú réžiu by použil dvakrát. B1 zostáva
platným horným screenom pri `w_e=-1+delta,Q_D>=0`, ale jeho nerovnosť nie je
povolením vložiť transfer `3 delta` do tej istej A13 interpretácie.
Voľný konštantný mix

```text
w_e=-1+(1-xi)delta,  q_D=3 xi delta,  0<xi<1
```

je backgroundovo degenerovaný a zavádza nové neodvodené `xi`. Preto sa
nezaraďuje do konečného bezparametrického katalógu. Stavovo odvodené
`xi(Y)` z jedného mikrofyzického operátora však zostáva otvorenou možnosťou.
Pre súčasný T1 kanonický skalár platí

```text
rho_e+p_e = Pi_e^2,
Q_D = Gamma_D Pi_e^2,
q_D = (Gamma_D/H)(1+w_e),
(1+w_e)(3+Gamma_D/H) = 3 delta,
xi(Y) = q_D/(3 delta) = Gamma_D/(3H+Gamma_D).
```

Takto odvodené `xi(Y)` nie je štvrtým kandidátom, kým nie je odvodená
`Gamma_D(Y)`. Zároveň presný roh `T` s `w_e=-1,q_D=3 delta` nevznikne pri
konečnom `Gamma_D/H` v súčasnom perturbatívnom T1: je to singulárny limit
`Gamma_D/H->infinity`. Preto platí

```text
T_SCALAR_REALIZATION = OPEN
```

a `F1–F3` pod `T` vyžadujú samostatný net-T1 eventový drain operator alebo
dôkaz nového regulárneho stavového mechanizmu, ktorý dokáže odoberať aj
potenciálovú energiu. Nie sú automaticky granularizáciami T1.

#### 8.10.1 Spoločný transferový obal

Nasledujúci katalóg je podmienený vetvou `T` a hypotézou
`A2_OVERHEAD_AVAILABLE_TO_PRODUCTS`. Definujme iba existujúce lokálne
veličiny

```text
kappa = <k> + C = 1/delta approximately 43.54,
Theta_cell = nabla_mu u_cell^mu,
h = (Theta_cell/3) t_P,             # v spoločnej FLRW projekcii h=H t_P
y = rho_e/rho_P.
```

Ak bunky zachovávajú lokálny vlastný objem a expanzia vzniká ich delením,
relatívny rast fyzického objemu `Theta_cell` dáva na jednu bunku

```text
d_J = Theta_cell t_P = 3h
```

príležitostí na delenie za Planckov čas. Bunková kongruencia zatiaľ nie je
automaticky scalar-rest-frame `u_e` ani celkový Landauov vektor. Katalóg
predpokladá `u_cell^mu=u_Landau^mu` iba na auditovanej expandujúcej `U_L`
vetve; mimo nej treba odvodiť vlastnú regulárnu bunkovú kongruenciu. Je to
lokálny kinematický clock, nie globálne `H0` ani voľný čas. Ak jedna divízia
sprístupní produktom geometrickú energetickú réžiu `delta`, potom
spoločný bezrozmerný drain je

```text
j_D^(delta) = 3 delta h y,
Q_D^(delta) = 3 delta H rho_e             # homogénna FLRW projekcia.
```

Rovnica je `TRANSFER_REPRESENTATION_HYPOTHESIS` samostatného eventového
operatora, nie už odvodená mikrofyzika ani súčasný T1. Ak je A2 réžia celá
iba tlakovou prácou/prestavbou siete,
vetva `T` aj všetky nasledujúce tri faktorizácie dostanú spoločný STOP.

#### 8.10.2 Tri bezparametrické granularizácie toho istého drainu

Tri kandidáty nemenia `j_D`; menia iba to, čo bunková teória považuje za
jednu udalosť:

```text
EVENT_ENERGY_STATUS = DETERMINISTIC_GIVEN_Y_FOR_F1_F3
```

To je explicitný scope katalógu, nie tvrdenie o všetkých diskrétnych
operátoroch. Ak má energia udalosti pri rovnakom `Y` rozdelenie, musí sa
zaviesť označená eventová miera `d nu_J(epsilon|Y)` a počítať

```text
j_D = integral epsilon d nu_J(epsilon|Y),
j_s = integral beta_s(epsilon) epsilon d nu_J(epsilon|Y).
```

Pre nelineárne `beta_s` nemožno druhý integrál nahradiť výrazom
`beta_s(<epsilon>) j_D`; v slabom limite skúša tretí energetický moment,
zatiaľ čo background pozná iba prvý. Distribučná vetva preto potrebuje
vlastnú vopred odvodenú markovú mieru a nie je skrytým štvrtým kandidátom.

| ID | Bunkové čítanie | `nu_J(Y)` | `epsilon_J(Y)` |
|---|---|---:|---:|
| `D03a-F1` | jedna režijná energetická udalosť na jednu divíziu | `3h` | `delta y` |
| `D03a-F2` | réžia rozdelená medzi `kappa` kanálových mikroudalostí | `3h/delta` | `delta^2 y` |
| `D03a-F3` | vzácna koherentná Planckovská udalosť | `3 delta h y` | `1` |

Pre každý riadok platí bodovo

```text
nu_J epsilon_J = 3 delta h y = j_D^(delta).
```

`F1` je najmenšie čítanie „jedna divízia — jeden režijný balík“. `F2`
rozlišuje `kappa=1/delta` kanálov a celkovú réžiu `delta y` rozdelí medzi
ne; rovnomernosť tohto delenia je hypotéza, nie dôsledok samotného priemeru
`<k>`. `F3` má energiu udalosti `E_P` a algebraicky ekvivalentnú
pravdepodobnosť `p_J=delta y` na division opportunity. Táto
pravdepodobnosť je rekonštrukčná hypotéza z požadovaného spoločného drainu,
nie odvodený zákon ani povolenie nastaviť Planckovskú udalosť podľa želaného
parného výsledku.

Povinný nulový control je `nu_J epsilon_J=0`; nepočíta sa ako štvrtý
fyzikálny kandidát. Všetky tri vetvy majú `nu_J>=0`, `epsilon_J>=0` na
`0<=y<=1` a nepoužívajú `lambda`, dnešné `rho_F`, realizovaný mód `k` ani
pozorované parné číslo.

#### 8.10.3 Spoločná hmota–para–popol mapa

Pri stále iba rekonštruovanom prompt kandidátovi z B2 je pre každú vetvu

```text
r_s,F = (2/g_*) epsilon_J,F^2,
beta_s,F = r_s,F/(1+r_s,F),
Q_s,F = beta_s,F Q_D^(delta),
Q_e_to_M,F = (1-beta_s,F) Q_D^(delta),
Q_M_to_C = Gamma_C(Y_C) rho_M.
```

Tým hmota, para a popol nevytvárajú tri nezávislé voľné funkcie. Jedna
parent udalosť vytvorí prompt paru a hmotný zvyšok; popol vzniká následným
lokálnym dokončením hmotného zvyšku. `Gamma_C` zostáva otvorená completion
sadzba a nesmie sa zvoliť tak, aby spätne trafila dnešný pomer hmoty a
popola.

Úplná backgroundová net identita bez skrytia následného toku je

```text
-Q_D + Q_s + (Q_e_to_M-Q_M_to_C) + Q_M_to_C = 0.
```

Jej štvorvektorová recoil verzia zostáva otvorená D08.

Rozlišovací prompt pomer je presne

| ID | `r_s=Q_s/Q_e_to_M` | pomer voči A12 endpointu `2/g_*` |
|---|---:|---:|
| `F1` | `(2/g_*) delta^2 y^2` | `delta^2 y^2` |
| `F2` | `(2/g_*) delta^4 y^2` | `delta^4 y^2` |
| `F3` | `2/g_*` | `1` |

Na spoločnej B1 mape `y_x^2 lesssim 10^-76.6` preto

```text
F1: R_sM,x/R_sM,eq lesssim 10^-79.9,
F2: R_sM,x/R_sM,eq lesssim 10^-83.2,
F3: R_sM,x/R_sM,eq = 1.
```

`F1` a `F2` teda dostávajú `CONDITIONAL_PROMPT_STEAM_FAIL` v tom istom
shared-1280-e-fold scope; zostávajú však užitočnými matter/ash a nulovými
granularitnými kontrolami. `F3` algebraicky obnoví iba podmienený A12 birth
pomer

```text
beta_s,F3 = 2/(g_*+2),
```

nie dnešnú `Delta N_eff`, teplotu ani frekvenciu. Nie je tým potvrdená:
musí ešte odvodiť zdroj Planckovskej energie, kauzálny zber a vyššie momenty
udalostí.

#### 8.10.4 Povinné backward/STOP testy B3

Každý kandidát musí pred numerikou prejsť:

1. **background identity:** `nu_J epsilon_J=3 delta h y` bez fitovania;
2. **no-double-count:** použiť buď `P`, alebo `T`; nikdy oboje naraz;
3. **backreaction guard:** rovnosť samotného `rho_e(a)` neoprávňuje prevziať
   `N=1280` ani celý A13 background do `T`; spoločný systém `e+M+s+C` sa
   musí znovu odvodiť s tlakmi všetkých produktov;
4. **four-vector ledger:** strata parentu sa musí rovnať súčtu recoil
   zdrojov `M,s,C` aj mimo backgroundu;
5. **source-off:** `Q_D->0` pri `y->0`; samotná miera nulovoenergetických
   division opportunities nemusí byť fyzikálnym zdrojom;
6. **F1 energy guard:** jedna divízia musí skutočne uvoľniť
   `delta rho_e V_P` do produktov;
7. **F2 channel guard:** lokálna distribúcia stupňa, channel recoil a šum
   musia dovoliť rovnomerné `kappa` čítanie; priemer `<k>` sám nestačí;
8. **F3 causal-energy guard:** udalosť s `epsilon_J=1` potrebuje lokálny
   kauzálny zber aspoň rádu `N_collect>=1/y` Planckových buniek alebo
   ekvivalentný uložený kolektívny mód;
9. **distribution/noise guard:** pri nedeterministickej energii sa osobitne
   zmrazia markové momenty; vyššie momenty eventového procesu nesmú byť
   automaticky Poissonovské a musia prejsť budúcu izokurvatúrnu/D10 bránu;
10. **late recovery:** po skorom source-off zostane oddelený neskorý A1
   rezervoár `F->C`; `delta`, `h` ani `y` sa nesmú nahradiť jeho `lambda`;
11. **no-target:** legacy para, `H0`, `S8` ani dnešný matter/ash pomer
    neurčujú žiadnu z troch funkcií.

Stav B3 je

```text
B3 = FINITE_HYPOTHESIS_MAP
A13_ACCOUNTING_SPLIT = REQUIRED
A2_OVERHEAD_AVAILABLE_TO_PRODUCTS = OPEN_PHYSICAL_QUESTION
COMMON_TRANSFER_DRAIN = 3 delta H rho_e  # hypothesis in T only
T_SCALAR_REALIZATION = OPEN
T_BACKREACTION_GUARD = REQUIRED
EVENT_ENERGY_STATUS = DETERMINISTIC_GIVEN_Y_FOR_F1_F3
F1_F2 = CONDITIONAL_PROMPT_STEAM_FAIL_IN_B1_SCOPE
F3 = REVIEW_CAUSAL_ENERGY_AND_NOISE
Gamma_C = OPEN_FUNCTION
D03 = SOLE_ACTIVE
NO_SCORE_CHANGE
```

Tento formula-lineage krok bol vykonaný ako B4 v oddiele 8.11. Jeho výsledok
je `PASS_FORMULA_LINEAGE`: aktuálny korpus podporuje `P`, zatiaľ čo `F1–F3`
ako energia A2 réžie majú scoped `STOP_CURRENT_CORPUS_ONLY`. Ďalším krokom
je definičný B5, nie ďalší tvar funkcie ani Python.

### 8.11 B4 — formula-lineage audit významu réžie `delta`

B4 nepoužíva pozorované parné číslo ani nový model. Číta iba to, čo
existujúci korpus už priradil symbolu `delta`.

| Primárny zdroj | Doslovný formulačný obsah | Dôsledok pre B3 |
|---|---|---|
| `theory/SK/01_Introduction_and_Philosophy_SK.md`, Réžia | časť paliva pri prestavbe spojení „zhorí naprázdno“; odpad, popol a para sú opísané osobitne ako rebrík trávenia | réžia nie je identifikovaná s energiou produktového eventu |
| `theory/SK/04_Main_Document_Theory_Equations_Values_v3.17_SK.md`, A2 | `delta=1/(<k>+C)` je prestavaný podiel a priamo dáva `w_f=-1+delta` | explicitná rola `P`: efektívne tlakové/expanzné riedenie |
| ten istý dokument, A7 | `-3 delta Omega_f` je mikropôvod `w_f=-1+delta`; párová výmena palivo–hmota je samostatný `lambda(H0/H)Omega_f` člen | V1 nemá produktový `+3 delta Omega_f` zdroj |
| ten istý dokument, A12 | parná účinnosť používa otvorenú energiu udalosti `E_udalosti`, nie `delta rho_f V_P` | A12 neurčuje `E_J` z A2 réžie |
| `Audit/Q22A_Q4_Q72_MICROPHYSICAL_OPERATOR_BRIDGE_AUDIT_2026-07-15.md` | A2 určuje réžiu a efektívne `w_f`, ale neurčuje príjemcu, podiel produktov ani hybnosť; Q22a-G0 je blokované Q4-P0 | produktový most z `delta` v korpuse neexistuje |
| `Questions/Q22A_MINIMAL_DIVISION_OPERATOR_CONTRACT_SK.md` | event musí osobitne určiť mieru, energiu, štvorvektory, podiel a poruchové momenty | chýbajúci most nemožno nahradiť B3 algebraickou faktorizáciou |

Tento rozdiel je viditeľný priamo v homogénnom V1 ledgeri:

```text
d rho_f/dN = -3 delta rho_f - (Gamma/H) rho_f,
d rho_m/dN = -3 rho_m       + (Gamma/H) rho_f.
```

Členy `-(Gamma/H)rho_f` a `+(Gamma/H)rho_f` sú párový transfer. Člen
`-3 delta rho_f` nemá v produktovej rovnici párové `+3 delta rho_f`, pretože
je už reprezentovaný cez `3H(rho_f+p_f)` pri `p_f=(-1+delta)rho_f`.
Premeniť ho na `Q_D=3 delta H rho_f` bez pridania a opätovného odvodenia
produktových rovníc by nebolo čítanie V1, ale nový model.

#### 8.11.1 Rozsudok B4

Súčasný korpus preto vyberá pre A2 presne formulačnú rolu `P`, nie
produktovú rolu `T`:

```text
B4 = PASS_FORMULA_LINEAGE
A2_DELTA_ROLE = EFFECTIVE_PRESSURE_NETWORK_WORK
A2_TO_PRODUCT_TRANSFER = PRECHECK_EXCLUDED_NO_PROVENANCE
F1_F2_F3_AS_A2_ENERGY_EVENTS = STOP_CURRENT_CORPUS_ONLY
DIVISION_OPPORTUNITY_CLOCK_3H = SUPPORTED_BACKGROUND_KINEMATICS
PRODUCT_EVENT_RATE_AND_ENERGY = OPEN_Q4_P0_Q22A_G0
D03 = SOLE_ACTIVE
NO_SCORE_CHANGE
NO_PYTHON
```

`STOP_CURRENT_CORPUS_ONLY` nie je fyzikálny STOP diskrétnych udalostí,
pary ani celej S–M vetvy. Znamená iba, že `F1–F3` sa nesmú vyhlásiť za
odvodené z A2 a nesmú pokračovať do operator passportu pod názvom
„energia réžie“. B3 zostáva archivovanou mapou toho, ako by rôzna
granularita rozlíšila paru, keby nový mikrofyzický zákon neskôr odvodil
rovnaký transferový súčin. Také znovuotvorenie musí priniesť nový párový
štvorvektorový ledger a znovu odvodiť celý background `e+M+s+C`; nestačí
vetvu premenovať.

Kinematická identita „expanzia = delenie“ naďalej podporuje počet division
opportunities `3H`, ale neurčuje, koľko z nich je produktová udalosť ani akú
má energiu. Produktový event patrí podľa vlastnej filozofie teórie k
tráveniu/zlyhaniu/jazve alebo k samostatnému exit relaxation/collision
operatoru. Jeho `R_J,E_J` sa musia odvodiť z Q4-P0/Q22a-G0 a nesmú sa
preniesť z dnešného neskorého A1 `lambda` bez dôkazu spoločného operátora.

Najbližší krok B5 je preto čisto definičný event passport, nie ďalšia
interpolácia: z korpusu vytiahnuť alebo presne označiť ako chýbajúce
`F,I,E_I,N_trial`, invariantnú mieru udalosti, kauzálny zberný región a
štvorvektorové momenty produktov. Ak tieto definície korpus nemá, D03 sa
zastaví na presnom autorovom/mikrofyzickom vstupe namiesto numerického fitu.

### 8.12 B5 — definičný passport udalosti trávenia/zlyhania/jazvy

B5 auditoval `Questions/Q4_problem_epsilon_jazvy_kolaje_K1-K4.md`,
Q22a/Q4/Q72 bridge audit, minimálny division-operator contract, AR46 a
`Audit/A2_K8_1_G2_NUMBER_SOURCE_MOMENT_AUDIT.md`. Výsledok je:

| Povinný objekt | Čo korpus obsahuje | Úplná definícia pre skorý event? |
|---|---|---|
| `F` — zlyhanie | slovný význam „nestrávený zvyšok/obyčajná hmota“ | **NIE** — chýba vstupný a výstupný stav, vlastný čas a kritérium jednej udalosti |
| `I` — jazva | historické pomenovanie trvalej stopy | **NIE** — chýba stavová zmena a kritérium trvalosti |
| `p_F` | historická K1 hypotéza kladie `p_F=p_I=epsilon_eff`; až spoločný výťažok `P(F intersection I)` má rád `epsilon_eff^2` | **NIE** — chýba odvodený hazard na definovaný pokus |
| `p_I` alebo `p(I|F)` | koľaje Q4-K1/K2 uvádzajú možné významy | **NIE** — ide o hypotetické parametrizácie |
| `xi` | Q4 eviduje viac možných interpretácií | **NIE** — interval, fyzikálny význam aj limit `xi->1` sú otvorené |
| `E_I` / `E_J` | A12 vyžaduje energiu udalosti; B2/B3 ukazujú jej dôležitosť | **NIE** — chýba energia aj kauzálny zberný región |
| `N_trial` / event measure | A7 podporuje `3H` iba pre division opportunities; trávenie má slovne vlastné vnútorné hodiny | **NIE** — ani jeden údaj neurčuje počet produktových pokusov skorého rezervoára |
| `pasca #7` | názov v starom registri | **NIE** — zakázaná degenerácia nie je definovaná |
| `Q_A^mu`, birth frame a recoil | minimálny contract ich vyžaduje | **NIE** — FLRW skalár nie je úplný prvý moment |
| tlak, shear, entropy a noise | AR46/Q72 ich vyžadujú z rovnakého collision kernelu | **NIE** — eventové vyššie momenty chýbajú |

Úplne definovaných položiek Q4-P0 je teda `0/8`; slovný význam `F` sa
nepočíta ako matematická definícia. Prvých osem riadkov tabuľky je presný
Q4-P0 passport; posledné dva riadky sú dodatočné požiadavky Q22a-G0/AR46.
Q22a-G0 preto neprechádza iba zadaním ôsmich názvov, kým chýbajú
štvorvektorové a kinetické momenty.

#### 8.12.1 Prečo historické `epsilon_eff^2` passport neuzatvára

Pre neskorý A1 fit platí aritmeticky

```text
epsilon_eff = lambda H0 t_P approximately 1.74 x 10^-62,
epsilon_eff^2 approximately 3.03 x 10^-124.
```

Táto zhoda rádu s `10^-123` neurčuje `p_F`, `p_I`, `E_J` ani `N_trial`.
Používa fitované neskoré `lambda`, globálny dnešný `H0` a iný rezervoár
`F`; preto sa nesmie preniesť na skorý `e` event bez dôkazu spoločného
operátora. Rovnako slovné tvrdenie, že genéza mala `E/bunku` Planckovského
rádu, neurčuje, či jedna produktová udalosť zbiera jednu bunku, viac buniek
alebo iba malú energetickú značku.

#### 8.12.2 Najmenší nový vstup, ktorý by znovu otvoril odvodenie

Zložitosť potrebného operátora je malá, ale obsah musí byť fyzikálny. Jedna
nová hypotéza alebo odvodenie musí v jednom pasporte určiť:

1. lokálny stav pred pokusom a po ňom a vlastný clock pokusov;
2. invariantnú mieru realizovaných udalostí alebo označenú distribúciu;
3. energiu jednej udalosti/distribúciu energií a kauzálny zberný región;
4. odvodený podiel produktov `s+M` alebo dôkaz nulového podielu a pri
   sekvencii `M->C` normalizovanú lokálnu sadzbu/kernel alebo explicitnú
   dynamiku medzistavu;
5. úplný štvorvektorový recoil a spätnoreakčný ledger paliva spolu s tlakom,
   anizotropným stresom, entropiou a šumom z toho istého operátora, vrátane
   `delta Q_A` a spoločného zdroja korelácií `S`, z ktorého sa odvodí
   `P_AB(k)`.

Pozorovania potom smú tento jediný zmrazený operátor vyradiť. Nesmú určiť
jeho amplitúdu, pravdepodobnosť, šírku ani eventovú energiu.

#### 8.12.3 Stav B5 a D03

```text
B5 = PASS_DEFINITION_INVENTORY
Q4_P0_COMPLETE = 0/8
Q22A_G0 = REVIEW_BLOCKED_BY_Q4_P0_DEFINITIONAL_INPUT
EARLY_EVENT_OPERATOR = NOT_DERIVABLE_FROM_CURRENT_CORPUS
D03 = SOLE_ACTIVE_REVIEW_BLOCKED
D04_D11 = BLOCKED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
NO_PYTHON
```

Toto je terminálny formulačný blocker aktuálneho korpusu, nie dôkaz, že
teória alebo skorá para sú nepravdivé. Najprv sa ucelená časť B3–B5 odovzdá
na malý externý T1 audit a jeho odpoveď sa autoritatívne vyhodnotí. Až potom
ďalší vedecký krok vyžaduje nový autorov mikrofyzický postulát alebo nové
odvodenie vyššie uvedených piatich bodov. Bez neho by každá ďalšia „funkcia“
bola iba voľný fit prezlečený za bunkovú terminológiu.

### 8.13 B6 — autorom schválená topológia C0: lokálna first-passage udalosť

EA-041 prijal B3–B5 ako `AGREE_IN_SCOPE / T1_PRIMARY_FORMULA` bez nálezu.
Orchestrátor následne navrhol najmenší eventový obraz: bunka má lokálny
priebeh trávenia, jedna udalosť nastane pri jeho prvom dokončení, energia je
rozdiel lokálneho stavu pred a po udalosti, prompt výstup tvorí para a
hmotný zvyšok a tento zvyšok sa môže neskôr dokončiť na popol. Autor teórie
2026-07-23 na túto jedinú otvorenú voľbu odpovedal:

> Pokračuj

Tým sa schvaľuje iba topológia

```text
B6_C0_OPERATOR_CLASS = LOCAL_CELLULAR_DIGESTION_FIRST_PASSAGE
PARENT_EVENT = e -> s + M
COMPLETION_EVENT = M -> C
RELATION_TO_Q4 = ALTERNATIVE_EXIT_OPERATOR; FAILURE_SCAR_Q4_P0_REMAINS_0_OF_8
RUN_AUTHORIZED = false
```

Nie je tým schválená sadzba, eventová energia, pravdepodobnosť, šírka,
causal collection region, steam fraction ani collision kernel.

#### 8.13.1 Lokálny stav a invariantná miera prvého prechodu

Nech `chi_D` je bezrozmerný vnútorný progress existujúceho bunkového
rezervoára, nie nové fundamentálne pole a nie diagnostický pár
`chi=(chi_m,chi_Gamma)` z oddielu 7.3. Pre aktívnu kohortu platí

```text
0 <= chi_D <= 1,
D_u_cell chi_D = omega_D(Y_D) >= 0,
chi_D|_birth = 0.
```

`u_cell^mu` musí byť odvodená future-directed bunková kongruencia. Rovnosť
`u_cell=u_Landau` je dovolená iba na už auditovanej Type-I doméne a nie ako
globálny predpoklad. Funkcia `omega_D` má rozmer energie a zostáva otvorená;
nesmie obsahovať voľný kozmický čas, `ln(a)`, globálne `H0` ani realizovaný
mód `k`.

Jedna udalosť je **prvý** prechod plochou `chi_D=1`. Pre proper density
aktívnych kohôrt `n_act` má invariantná skalárna miera na vlastný
štvorobjem tvar

```text
R_J(x) = n_act(x) I_first(x)
         delta_D[chi_D(x)-1] [D_u_cell chi_D(x)]_+,
d nu_J = R_J dV_4,
dV_4 = sqrt(-g) d^4x.
```

Lokálny rozklad `dV_4=dV_prop d tau_cell` je dovolený iba v adapted frame
príslušnej bunkovej kongruencie. `I_first` je indikátor priradený konkrétnej
identifikovanej kohorte/worldline. Po prvom prechode sa táto kohorta vyradí
z `n_act`; dcérska bunka smie začať s `chi_D=0` iba ako nová identifikovaná
kohorta. Tým je zakázaný tichý reset aj dvojité započítanie. Rozmery sú
`[n_act]=E^3`, `[D_u chi_D]=E`, teda `[R_J]=E^4`. Zápis je first-passage
passport, nie tvrdenie, že kohorty sú Poissonovské. Distribúcia birth phases
a korelácie susedných buniek patria do D08/D10.

#### 8.13.2 Energia udalosti a kauzálny zber

Nech `C_x` je lokálny kauzálny worldtube jednej udalosti, uzavretý dvoma
spacelike rezmi `Sigma_-` a `Sigma_+` a orientovanou bočnou hranicou
`B_side`. `Delta P_e^mu(C_x)` je úbytok štvorhybnosti rezervoára medzi
oboma rezmi vrátane orientovaného fluxu cez `B_side`. Všetky príspevky sa
pred sčítaním paralelne prenesú po zmrazenej lokálnej transportnej konvencii
do jedného tangentného priestoru, respektíve tetrády udalosti `x`. Eventová
značka je

```text
p_J^mu = Delta P_e^mu(C_x),
E_J = -u_cell_mu p_J^mu >= 0,
E_J <= E_available(C_x).
```

Tým je energia definovaná ako fyzický skok, nie ako `delta rho_e V_P`,
`rho_e V_P`, fitované číslo alebo automaticky `E_P`. Ak je `p_J` pri tom
istom lokálnom stave rozdelená, zavedie sa normalizovaná mark distribution
`Pi_J(dp|x)`, `integral Pi_J(dp|x)=1`, a lokálna mark-intensity

```text
dR_J(p|x) = R_J(x) Pi_J(dp|x),
Q_D(x) = integral E_J(p,x) dR_J(p|x),
S_D^mu(x) = integral p_J^mu dR_J(p|x).
```

`Q_D` a `S_D^mu` sú lokálne source densities; až
`integral_Omega Q_D dV_4` a `integral_Omega S_D^mu dV_4` sú celkové zdroje
v oblasti `Omega`. V deterministickom podprípade `Q_D=R_J E_J`. C0 ponecháva otvorené, či
`C_x` obsahuje jednu Planckovu bunku, viac buniek alebo uložený kolektívny
mód. Bez tejto mapy sa nesmie nastaviť `E_J=E_P` iba preto, aby prešla para.

#### 8.13.3 Jediný vertexový ledger hmoty a pary

Na každom parent evente musí platiť

```text
p_J^mu = p_s^mu + p_M^mu,
S_D^mu(x) = integral p_J^mu dR_J(p|x),
S_s^mu(x) = integral p_s^mu dR_J(p|x),
S_M,birth^mu(x) = integral p_M^mu dR_J(p|x),
S_D^mu = S_s^mu + S_M,birth^mu.
```

Tento vertexový zápis je conservation identity a chráni recoil aj mimo FLRW;
sám neodvodzuje recoil distribution ani collision kernel. V cell-rest-frame možno
definovať energetický podiel

```text
beta_s = (-u_cell.p_s)/E_J,   0 <= beta_s <= 1.
```

Už auditovaný bezparametrický steam kandidát zostáva iba testovanou
rekonštrukčnou hypotézou

```text
r_s(E_J) = (2/g_*) (E_J/E_P)^2,
beta_s(E_J) = r_s/(1+r_s),
0 <= E_J/E_P <= 1.
```

Nie je súčasťou autorovho schválenia C0 a nesmie sa použiť mimo svojej
domény. Pri markovanej energii sa počíta lokálne
`Q_s(x)=integral beta_s(E_J) E_J dR_J(p|x)`, nie
`beta_s(<E_J>)Q_D`.

#### 8.13.4 Popol ako druhý first-passage stav, nie tretí prompt branch

Hmotný zvyšok sa narodí s `chi_C=0` a môže sa lokálne dokončiť pri prvom
prechode `chi_C=1`. Nech `f_M(a,Y_C;x)` je proper kohortová/age density
aktívnych hmotných zvyškov, kde `a` je vlastný vek kohorty. Potom

```text
D_u_M chi_C = omega_C(Y_C) >= 0,
n_M,act(x) = integral da dY_C f_M(a,Y_C;x),
R_C(x) = integral da dY_C f_M I_C,first
         delta_D(chi_C-1) [D_u_M chi_C]_+.
```

`I_C,first` vyradí kohortu po prvom prechode rovnako ako pri parent evente;
nový reset je dovolený iba pre novú dcérsku kohortu.

Jeho vertex musí osobitne zachovať štvorhybnosť. Ak je prechod iba zmenou
sektorového/interaction stavu pri rovnakej štvorhybnosti, platí
`p_C^mu=p_M^mu`. Ak odovzdáva ďalšiu energiu alebo hybnosť, chýbajúci produkt
sa musí explicitne pridať; nesmie sa skryť do `Gamma_C`.

Pre normalizovanú completion mark distribution `Pi_C(dp|x)` platí
`dR_C(p|x)=R_C(x)Pi_C(dp|x)`. Lokálny energetický prenos je
`Q_M_to_C(x)=integral E_M(p,x)dR_C(p|x)`. Po
coarse-grainingu sa smie background zapísať ako

```text
Q_M_to_C = Gamma_C,eff rho_M,
Gamma_C,eff = Q_M_to_C/rho_M  pre rho_M > 0.
```

Pri `rho_M=0` musí konzistentný no-source limit dať aj `Q_M_to_C=0`; podiel
sa v tomto bode samostatne nedefinuje. `Gamma_C,eff` je teda odvodený hazard
z first-passage kohôrt, nie nová nezávislá power-law zvolená podľa dnešného
pomeru hmoty a popola. Kým však nie sú odvodené `omega_C` a kohortová
distribúcia `f_M`, funkčná voľnosť iba zmenila reprezentáciu a nebola
odstránená.

#### 8.13.5 Povinné recovery a STOP brány C0

Pred numerikou musí ten istý C0 passport prejsť:

1. **first-passage:** každá kohorta sa započíta najviac raz;
2. **local clock:** `omega_D,omega_C` sú funkcie lokálneho stavu a majú
   odvodený nulový/source-off limit;
3. **causal energy:** `E_J<=E_available(C_x)` vrátane boundary fluxu;
4. **vertex conservation:** štvorhybnosť sa ruší na parent aj completion
   evente, nie iba po FLRW priemerovaní;
5. **background recovery:** po priemerovaní sa obnoví
   `-Q_D+Q_s+(Q_e_to_M-Q_M_to_C)+Q_M_to_C=0`;
6. **steam discriminator:** relevantný prompt steam pri rekonštruovanom
   `beta_s` vyžaduje skutočne odvodenú vysokú eventovú energiu; pri malej
   `E_J/E_P` musí zostať potlačený;
7. **source-off:** po vyčerpaní rezervoára platí `R_J<E_J>->0` bez voľného
   času; completion kohorty smú iba dobehnúť;
8. **late recovery:** neskorý A1 `F->C` zostane oddelený a nevytvorí nový
   steam source;
9. **moment completeness:** birth frame, pressure, shear, entropy, noise,
   `delta Q_A` a spoločný zdroj `P_AB(k)` sa odvodia z tej istej markovanej
   miery/kernelu;
10. **no-target:** `S8`, `H0`, legacy para ani dnešný `M/C` pomer neurčujú
    `omega_D`, `E_J`, `beta_s` alebo `omega_C`.

#### 8.13.6 Stav po autorovom pokyne

```text
B6 = AUTHOR_APPROVED_EVENT_TOPOLOGY_C0
B6_C0 = LOCAL_CELLULAR_DIGESTION_FIRST_PASSAGE
V1_D03 = PARTIAL_AUTHOR_INPUT
EVENT_RATE_omega_D = OPEN_FUNCTION
EVENT_ENERGY_AND_CAUSAL_REGION = OPEN
STEAM_KERNEL = HYPOTHESIS_ONLY
COMPLETION_RATE_omega_C = OPEN_FUNCTION
Q4_P0_FAILURE_SCAR = 0/8_UNCHANGED
D04_D11 = BLOCKED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
NO_PYTHON
```

C0 zužuje topológiu: parent drain aj `M->C` používajú rovnakú first-passage
architektúru a popol nie je tretia prompt vetva. Funkčnú voľnosť ešte
neznižuje, pretože `omega_D`, `omega_C`, mark distribution a kohortová
distribúcia zostávajú otvorené. D03 však ešte
nie je uzavretý, kým sa neodvodí `chi_D <-> phi_e/cellular state`, lokálna
progress law `omega_D`, eventová energia a pravidelná bunková kongruencia.
Tento read-only interný re-audit topológie bol následne dokončený stavom
`PASS_B6_C0_TOPOLOGY`; historicky po ňom nasledoval B6a, nie výber čísel ani
Python.

### 8.14 B6a — mantinel pre väzbu `phi_e -> chi_D,omega_D`

#### 8.14.1 Prečo energetická frakcia nie je clock

Najjednoduchšie algebraické návrhy

```text
chi_D = 1-y_e/y_e,birth
alebo
chi_D = 1-rho_e/rho_e,birth
```

sa neprijímajú ako event clock. Na homogénnej expandujúcej vetve totiž

```text
D_u rho_e = -Theta (D_u phi_e)^2 - Q_D.
```

Taký `chi_D` by rástol aj čistým Hubbleovým riedením bez trávenia a po
zapnutí udalostí by obsahoval vlastný výstup `Q_D`; eventová miera by sa
definovala kruhovo. Ľubovoľný energetický prah by navyše pridal nový
neodvodený podiel. `y_e` preto zostáva stavom/budgetom, nie B6a clockom.

#### 8.14.2 Nekruhový fázový kandidát PH1

Na už zvolenom `V1-P1`, `V_e=m_e^2 phi_e^2/2`, existuje parameter-free
lokálna fázová súradnica. Jej prvý scope je iba Type-I, lokálne homogénna
časť regularnej bunkovej/Landauovej kongruencie, medzi distribučnými
eventovými skokmi:

```text
Theta = nabla_mu u_cell^mu > 0,
D_u^2 phi_e + Theta D_u phi_e + m_e^2 phi_e = 0,
A_phi^2 = m_e^2 phi_e^2 + (D_u phi_e)^2 > 0,
X_phi = m_e phi_e,
Y_phi = -D_u phi_e,
theta_D = unwrap atan2(Y_phi,X_phi).
```

`X_phi` a `Y_phi` majú rovnaký rozmer `E^2`. Future direction kongruencie
fixuje orientáciu fázy; zmena konvencie `phi_e -> -phi_e` iba posunie
`theta_D` o `pi` a nemení jedno celé vinutie. Priamo z rovnice pohybu plynie

```text
D_u theta_D
  = (X_phi D_u Y_phi - Y_phi D_u X_phi)/A_phi^2
  = m_e - (Theta/2) sin(2 theta_D).
```

Toto je odvodená lokálna rýchlosť fázy, nie fitovaná decay width. Nepoužíva
`t`, `ln(a)`, `H0`, realizovaný `k`, legacy `lambda` ani dnešný pomer
produktov. Má rozmer energie a je striktne kladná na mantineli

```text
2m_e > Theta
equivalently m_e/H_loc > 3/2,  H_loc=Theta/3.
```

Je to pointwise hranica striktnej monotónnosti fázy. Pri frozen konštantnom
`Theta` sa zhoduje s underdamped hranicou voľného kvadratického oscilátora.
Pri časovo premenlivom `Theta` sama nezaručuje, že sa celé vinutie dokončí
v konečnom vlastnom čase skôr, než trajektória opustí Type-I doménu. Pri
`2m_e<=Theta` nie je monotónny phase first-passage dokázaný a PH1 sa nesmie
extrapolovať.

#### 8.14.3 Kandidát jedného topologického vinutia

Ak autor fyzikálne identifikuje **jedno úplné kladné vinutie** s jednou
dokončenou udalosťou trávenia identifikovanej kohorty, potom bez nového
spojitého parametra možno definovať

```text
chi_D = [theta_D-theta_D,birth]/(2 pi),
chi_D|_birth = 0,
omega_D^PH1 = D_u chi_D
             = [m_e-(Theta/2)sin(2 theta_D)]/(2 pi),
event J = first crossing chi_D=1.
```

`theta_D` je kontinuálne zdvihnutá fáza tej istej kohorty od jej birth
záznamu. Hybridné poradie je zmrazené:

```text
1. crossing sa testuje z ľavého limitu theta_D(tau_J^-);
2. až po prvom crossingu sa aplikuje eventový impulz;
3. parent kohorta sa potom vyradí z n_act.
```

Vlastný impulz udalosti preto nemôže spätne vytvoriť ani preskočiť svoj
crossing. Skorší distribučný skok ukončí PH1 scope alebo vyžaduje osobitne
predregistrované continuation pravidlo; nesmie sa potichu absorbovať do
`unwrap`. Po prechode sa parent kohorta vyradí podľa B6-C0. Dcérska kohorta má nový
birth záznam; phase variable tej istej kohorty sa potichu neresetuje.
Normalizácia `2 pi` je topologické celé vinutie, nie numericky ladená
konštanta.

Rovnica sama však **neodvodzuje fyzikálnu identitu**

```text
ONE_FULL_PHASE_WINDING == ONE_CELLULAR_DIGESTION_EVENT.
```

Polovičné vinutie, crossing konkrétnej fázy alebo energetický prah by dali
inú event count a boli by novými diskrétnymi mikrofyzickými voľbami. Korpus
A2/A7/A12 ani Q4/Q22a túto identitu neurčuje. PH1 je preto kandidát na
autorovo schválenie, nie hotový zákon teórie.

#### 8.14.4 Source-off, regularita a čo PH1 ešte neuzatvára

Pri `A_phi=0` fáza neexistuje. Tento bod sa interpretuje ako vyčerpaný
rezervoár iba vtedy, keď z rovnakého stavového ledgera plynie
`n_act->0`, a potom `R_J->0`; nesmie sa deliť nulou ani umelo pokračovať vo
fáze. Strata Type-I frame, `A_phi=0` mimo preukázaného vyčerpania alebo
porušenie `2m_e>Theta` sú hranice scope/review, nie automatický fyzikálny
source-off.

PH1 stále neurčuje:

1. mikroskopickú mapu jedného phase windingu na bunkové kanály `C=28`;
2. proper density aktívnych kohôrt `n_act` z diskrétnej siete;
3. eventovú energiu `E_J` a kauzálny worldtube `C_x`;
4. mark distribution, steam kernel, recoil/noise ani completion law;
5. `m_e`, počiatočnú amplitúdu alebo birth phase — tieto údaje zostávajú
   v D06/autorovom mikrofyzickom vstupe.

#### 8.14.5 Stav B6a pred autorovou voľbou

```text
B6a_ENERGY_FRACTION_CLOCK = REJECTED_CIRCULAR_OR_DILUTION_CONTAMINATED
B6a_PH1_PHASE_LAW = DERIVED_CONDITIONAL_MANTLE
B6a_PH1_DOMAIN = TYPE_I_LOCAL_HOMOGENEOUS_AND_2m_e_GT_Theta
ONE_WINDING_EVENT_IDENTITY = AUTHOR_DECISION_REQUIRED
omega_D = NOT_YET_AUTHOR_APPROVED
n_act = OPEN
EVENT_ENERGY_AND_PRODUCTS = OPEN
V1_D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
D04_D11 = BLOCKED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
NO_PYTHON
```

Nezávislý read-only re-audit algebraickej fázy, monotónnosti a source-off
hranice skončil `PASS_B6A_PH1_CONDITIONAL_MANTLE`. Historicky po ňom vznikla
autorova one-winding brána, ale B6b ju následne supersedoval ako jediný
najbližší krok. PH1 zostáva podmieneným MF2 kandidátom; audit stále nesmie
fyzikálnu identitu vinutia s udalosťou schváliť za autora.

### 8.15 B6b — constraint-first mapa množiny reálnych mechanizmov

#### 8.15.1 Opravené poradie otázok

Autor spresnil, že v tejto hĺbke sa ešte nemá vyberať ani detailne odvodzovať
jedna mikrofyzika trávenia. Primárna otázka je:

> Existuje aspoň jedna lokálna, konzervatívna a pozorovaniami prípustná
> trieda mechanizmov, ktorá vie vytvoriť potrebný steam/matter/ash source;
> a ak áno, aké mantinely musí spĺňať?

Potrebu tohto chýbajúceho operatora vytvorila source rovnica

```text
d rho_s/dx + 4 rho_s = S_s(x),  x = ln(a),
nabla_mu T_e^(mu nu) = -S_D^nu,
nabla_mu T_s^(mu nu) = +S_s^nu,
nabla_mu T_M^(mu nu) = +S_M,birth^nu - S_M_to_C^nu,
nabla_mu T_C^(mu nu) = +S_M_to_C^nu,
S_D^nu = S_s^nu + S_M,birth^nu.
```

„Funkcia trávenia“ preto v tejto fáze nie je nutne jedna skalárna funkcia.
Je to trieda lokálnych operatorov

```text
M_D: Y_local -> {dR_D(p|x), E_J, beta_s, recoil, noise,
                 completion marks},
Q_s(x) = integral beta_s(E_J) E_J dR_D(p|x),
S_s(x) = Q_s(x)/H(x)
```

v použitej FLRW konvencii. `Y_local` smie obsahovať iba lokálne bunkové,
poľové, kohortové a geometrické stavové veličiny povolené passportom. Cieľom
B6b je najprv určiť neprázdnu množinu prípustných `M_D`, nie predčasne
vyrobiť ich detailnú vnútornú dynamiku.

Týmto sa historická otázka

```text
ONE_FULL_PHASE_WINDING == ONE_CELLULAR_DIGESTION_EVENT
```

prestáva byť jedinou najbližšou autorovou bránou. PH1 zostáva auditovaným
podmieneným kandidátom v jednej z nižšie uvedených rodín, ale nesmie byť
vybraný skôr než sa rovnakým sitom preveria aj ostatné rodiny.

#### 8.15.2 Štyri podvetvy na rovnakej úrovni detailu

Označenia `MF1` až `MF4` sú **mechanism-family IDs**, nie nové koľaje ani
verzie hlavnej route.

##### MF1_DIVISION_LOCKED — trávenie viazané na delenie bunky

Udalosť trávenia môže nastať iba pri fyzicky identifikovanom delení bunky.
Schematický source má tvar

```text
dR_D = dR_div Pi_D(dp,dmarks|Y_local),
Q_s = R_div <E_J beta_s>_div.
```

Ak sa z A7 a z bunkovej kongruencie podarí odvodiť
`R_div ~ n_cell Theta`, môže byť počet príležitostí určený delením a nový
nezávislý event clock vôbec nemusí existovať. Zostáva však odvodiť výťažok,
energiu, steam fraction, recoil/noise a podmienku, kedy delenie produkuje
paru namiesto iného kanála. Samotný vzťah `N_cell proportional a^3` ešte
nedokazuje mikroskopický počet delení ani energiu jedného vertexu.

Rozlišujúci znak MF1 je: po podmienení na kompletný lokálny stav delenia
neexistuje ďalší samostatný first-passage čas, ktorý by mohol spustiť
trávenie bez delenia.

##### MF2_INTERNAL_CLOCK — samostatný vnútorný proces

Trávenie je first-passage alebo hazard aktívnej kohorty, ktorý môže byť
odlišný od okamihu delenia:

```text
R_D = integral dY f_act(Y;x) Gamma_int(Y),
alebo event J = first crossing chi_D(Y)=1.
```

`Gamma_int` ani `chi_D` nesmú byť voľnou funkciou kozmického času, `a`,
`H0` alebo požadovaného S8. B6a-PH1 patrí sem ako
`MF2_CONDITIONAL_CANDIDATE`: na svojom Type-I mantineli dáva odvodenú
fázovú rýchlosť, ale identita jedného vinutia s jednou udalosťou zostáva
neodvodená. MF2 zahŕňa aj iné lokálne first-passage kandidáty, ak vzniknú
nezávisle z povoleného stavového priestoru a nie z fitu na výsledok.

Rozlišujúci znak MF2 je: pri rovnakom lokálnom stave delenia môže vnútorný
stav zákonne dokončiť alebo nedokončiť trávenie podľa vlastnej odvodenej
trajektórie.

##### MF3_STATE_SWITCHED_HYBRID — lokálne stavovo závislý režim

Mechanizmus sa môže v jednom fyzikálnom režime správať ako MF1 a v inom ako
MF2, ak prepnutie určuje z toho istého lokálneho kernelu odvodený
bezrozmerný diskriminátor `z(Y_local)`, odvodený prah `z_*` a odvodená
transition weight, nie vložený kozmický čas:

```text
z << z_* : division-locked limit,
z >> z_* : internal-clock limit
```

alebo opačne. V B6b sa ešte nevolí interpolačná funkcia ani číslo `z_*`.
Najprv sa musí ukázať, že oba asymptotické limity, prechodová oblasť a
source-off môžu zdieľať jeden konzervatívny lokálny kernel. Ľubovoľný switch
zvolený podľa epochy, S8 alebo žiadaného výsledku je hidden fit a rodinu
vyradí. Cez prechod musia byť všetky `Q_A^mu` a ich momenty spojité alebo
distributionally konzervatívne spárované. Tá istá udalosť ani energia sa
nesmie započítať v oboch limitných režimoch.

Rozlišujúci znak MF3 je: oba limitné režimy sú fyzicky prítomné a výber
režimu robí lokálny stav. Ak sa váha jedného režimu ukáže identicky nulová,
mechanizmus sa zaradí do MF1 alebo MF2, nie ako falošne samostatný hybrid.

##### MF4_PARALLEL_CONSERVATIVE_CHANNELS — súbežné odlišné procesy

Dva alebo viac fyzicky odlišných lokálnych procesov môžu bežať súbežne bez
toho, aby jeden bol asymptotickým režimom druhého:

```text
S_D^mu = sum_r S_D,r^mu,
S_D,r^mu = S_s,r^mu + S_M,birth,r^mu.
```

Každý kanál `r` musí mať identifikovaný lokálny spúšťač, vlastné marky a
presne vedený podiel spoločného alebo vlastného rezervoára. Súčet musí mať
jeden vertex-level conservation ledger: tá istá energia, bunka alebo
udalosť sa nesmie odpočítať ani započítať dvakrát. Ak kanály v skutočnosti
predstavujú iba dva stavové limity jedného kernelu, patria do MF3; MF4 je
vyhradená pre skutočný konzervatívny súčet rozlíšiteľných procesov.

Rozlišujúci znak MF4 je: po zafixovaní kompletného lokálneho stavu môžu byť
naraz nenulové aspoň dva identifikovateľné kanály bez switchu medzi nimi.

#### 8.15.3 Množina prípustnosti a spoločné mantinely

Definujeme zatiaľ symbolickú množinu

```text
F_D = {M_D in MF1 union MF2 union MF3 union MF4 |
       M_D prejde M0-M10, Q22a-G0, B6-C0,
       background passport, perturbation passport a nezávislé holdouty}.
```

Každý člen musí bez ohľadu na rodinu splniť aspoň:

1. lokálnosť, kovarianciu a spoločnú štvorhybnostnú konzerváciu všetkých
   produktov;
2. nezáporné fyzické event rates a normalizované mark distributions;
3. odvodený reservoir, birth/reset pravidlo, first-passage/no-double-count a
   source-off bez voľného času;
4. kauzálny energetický rozpočet jedného vertexu a pozitívnu steam energiu;
5. skoré časovanie a reliktnú steam normalizáciu bez porušenia neskorého
   budgetu;
6. rovnaký kernel pre background, tlak, shear, momentum transfer, entropy,
   stochastic noise, `delta Q_A` a spoločné `P_AB(k)`;
7. stabilitu a kauzalitu perturbácií;
8. žiadne ladenie na `H0`, S8, legacy paru, dnešný `M/C` pomer alebo
   realizovaný mód `k` v background zákone;
9. oddelenie skorého steam source od fitovaného neskorého A1 `F->C` člena;
10. recovery limit, v ktorom sa nulový event source skutočne redukuje na
    zodpovedajúcu source-free dynamiku.

Tieto podmienky sú mantinely výstupu mechanizmu. Nevyžadujú ešte poznať jeho
jedinú mikroskopickú realizáciu, ale bránia tomu, aby sa neznáma funkcia iba
prekreslila podľa žiadaného kozmologického výsledku.

#### 8.15.4 Úloha S8: vylučovacie sito, nie konštrukčný vstup

Približne známy meraný rozsah S8 poskytuje užitočný vonkajší mantinel, ale
nesmie sa vložiť do definície `M_D`. Pred numerickým testom sa jeho konkrétny
dátový passport, interval a treatment napätia medzi meraniami samostatne
zmrazia. Až potom sa mechanizmus odvodený bez S8 propaguje dopredu:

```text
M_D
 -> {Q_A(a), delta Q_A, momentum transfer, pressure, shear, noise}
 -> background + perturbation growth
 -> S8 prediction
 -> compare with frozen observational interval.
```

Background source `S_s(a)` sám S8 neurčuje. Rovnaké background dejiny môžu
mať rozdielny rast podľa momentum transferu, tlaku, shear a korelovaného
šumu. Preto sa rodina nesmie prijať ani vyradiť zo S8, kým nemá aspoň
uzavretý perturbation-moment passport.

Legacy výsledky, v ktorých čistá neskorá tvorba hmoty smerovala k vyššiemu
S8 a dodaná frikčná vetva ho znižovala, sa smú použiť iba ako
`E3_LEGACY_SIGN_COMPARATOR`. Nie sú aktuálnou predikciou ani fit targetom.
Kvalitatívne dávajú tri možné životaschopné obálky:

1. steam/matter source sa ukončí dostatočne skoro a nemá významný priamy
   neskorý rastový účinok;
2. neskorší source má z toho istého kernelu odvodený stabilný momentum/
   pressure/shear účinok, ktorý nevedie k nadmernému rastu;
3. stavový hybrid oddelí skorý steam-producing režim od neskorého
   matter/ash completion režimu bez časového switchu vloženého rukou.

Existencia jednej z týchto obálok ešte nedokazuje teóriu. Ich neexistencia
po úplnom passporte by však mohla uzavrieť skúmanú SM_v1 rodinu ako
neživotaschopnú.

#### 8.15.5 Hĺbky skúmania a rozhodovací workflow

Práca sa má zastaviť na najnižšej hĺbke, ktorá vie rodinu korektne vyradiť:

```text
B6b-0  symbolická mapa MF1/MF2/MF3/MF4 a spoločné mantinely
  -> B6b-1  analytické background/source-moment obálky
      -> B6b-2  perturbation-sign/moment closure + zmrazenie S8 passportu
          -> B6b-3  predregistrovaná forward predikcia a porovnanie so S8
              -> detailná mikrofyzika iba pre preživšie ekvivalenčné triedy.
```

Na každej hĺbke sú prípustné iba štyri závery:

```text
F_D = empty
  -> scoped STOP: v skúmanom kontrakte neexistuje životaschopná rodina;

F_D obsahuje jednu ekvivalenčnú triedu
  -> promote túto triedu na detailnejšie odvodenie, nie ešte na pravdu;

F_D obsahuje viac tried
  -> preregistrovať rozlišujúci test a zachovať všetky dovtedy živé triedy.

existencia alebo neexistencia F_D ešte nie je dokázaná
  -> REVIEW / ohraničený ďalší test; žiadny STOP.
```

`F_D=empty` sa smie vyhlásiť iba po univerzálnom argumente alebo uzavretom
site, ktoré pokrýva všetky definované rodiny. To, že sa v ohraničenom
hľadaní nenašiel svedok, samo osebe dokazuje iba `REVIEW/UNRESOLVED`, nie
neexistenciu funkcie.

Žiadna rodina sa nesmie rozpracovať do podrobnej mikrofyziky len preto, že
bola zapísaná prvá. Najprv sa na rovnakej hĺbke preveria MF1 až MF4.

#### 8.15.6 Stav B6b po fyzikálnom audite

```text
B6b = PASS_B6B_FAMILY_MAP
MF1_DIVISION_LOCKED = OPEN_FAMILY
MF2_INTERNAL_CLOCK = OPEN_FAMILY
MF3_STATE_SWITCHED_HYBRID = OPEN_FAMILY
MF4_PARALLEL_CONSERVATIVE_CHANNELS = OPEN_FAMILY
PH1 = MF2_CONDITIONAL_CANDIDATE_ONLY
ONE_WINDING_AUTHOR_GATE = SUPERSEDED_BY_BROADER_FAMILY_MAP
S8_ROLE = INDEPENDENT_HOLDOUT_NOT_CONSTRUCTOR
S8_NUMERICAL_PASSPORT = NOT_YET_FROZEN
V1_D03 = PARTIAL_AUTHOR_INPUT_UNCHANGED
D04_D11 = BLOCKED
K4 = 60/100_UNCHANGED
P5 = 3.5/6_UNCHANGED
RUN_AUTHORIZED = false
NO_PYTHON
```

Nezávislý read-only fyzikálny audit po piatich vecných a jednej redakčnej
oprave uzavrel mapu stavom `PASS_B6B_FAMILY_MAP`. Po dokumentačnom closure
review je najbližší vedecký krok B6b-1: analytické background/source-moment
obálky MF1 až MF4 na rovnakej hĺbke, bez výberu víťaza alebo zmeny skóre.

## 9. Ďalší proces

1. B6b mapa MF1/MF2/MF3/MF4 prešla nezávislým fyzikálnym auditom
   `PASS_B6B_FAMILY_MAP`;
2. pre každú rodinu sa na rovnakej hĺbke zostaví analytická background a
   source-moment obálka bez výberu detailnej mikrofyziky;
3. autor postupne uzavrie iba tie `V1-D01` až `V1-D11`, ktoré sú potrebné na
   rozlíšenie alebo vyradenie živých rodín;
4. orchestrátor oddelí dodané postuláty od odvodených dôsledkov a zmrazí
   nezávislé observačné holdout passporty;
5. preživšie rodiny prejdú perturbation-moment sitom a až potom
   predregistrovaným ohraničeným numerickým feasibility testom;
6. ucelená auditovaná časť sa odovzdá v malom T1 externom balíku;
7. detailná mikrofyzika sa otvorí iba pre preživšiu ekvivalenčnú triedu
   alebo pre preregistrovaný rozlišovací test medzi viacerými triedami.

Kým nie sú všetky tieto kroky splnené:

```text
INPUT_CONTRACT_INCOMPLETE
NO_CODE_AUTHORIZED
P5_4_NOT_RUN
G8_G9_BLOCKED
K4_60_OF_100_UNCHANGED
```
