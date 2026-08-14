# Audit prevzatia mainstreamovej limity a rekonštrukcie z dát

**Dátum:** 2026-08-08  
**Otázka:** možno `C_s`, tenzorový operátor a `delta(a)` prevziať zo
štandardnej fyziky alebo odvodiť z existujúcich meraní?  
**Rozsudok:** `CONDITIONAL_YES_FOR_LIMITS_AND_RECONSTRUCTION / NO_FOR_UNIQUE_MICROPHYSICAL_DERIVATION`  
**Dopad na koľaje:** bez zmeny autoritatívneho stavu, skóre a hĺbky

## 1. Stručná odpoveď

Áno, ale treba rozlíšiť tri vedecky odlišné operácie:

1. **Zdedená limita:** prevezmeme experimentálne overený tvar GR,
   štandardnej kozmológie alebo Boltzmannovej kinetiky ako povinný
   nízkoenergetický limit. To je legitímny comparator alebo efektívny
   closure, nie odvodenie bunkovej mikrofyziky.
2. **Rekonštrukcia z dát:** zvolíme konečnú parametrizáciu alebo regulovanú
   funkčnú triedu a dáta určia jej posterior/povolený pás. Výsledok je
   podmienený voľbou funkčnej triedy, priorov, datasetov a observable mapy.
3. **Mikrofyzické odvodenie:** bunkové pravidlá samy určia zdroj, operátor a
   ich parametre. Toto je najsilnejší cieľ KBTP a nemožno ho nahradiť iba
   fitom.

Prvé dve možnosti dokážu otestovať, či **existuje neprázdna prípustná
množina**, ktorá rešpektuje známu fyziku. Nemôžu samy dokázať, že daný
mechanizmus skutočne vzniká z buniek.

### 1.1 Spresnenie už dosiahnutých výsledkov KBTP

KBTP **vypočítala**

$$
\Delta N_{\rm eff}=\frac47 g_x
\left(\frac{10.75}{g_{*s,\rm dec}}\right)^{4/3}
=0.0535
$$

po dosadení `g_x=2` a `g_*s,dec=106.75`. Audit nespochybnil túto aritmetiku
ani štandardnú termálnu reliktnú rovnicu. Zúžil iba vedecký dosah výsledku:
teória zatiaľ neodvodila, že bunková para má práve dva stupne voľnosti, že sa
odpojí pri stave s `g_*s=106.75`, ani zdroj a prežitie reliktu cez zrýchlenú
fázu, exit a reheating. Presný status preto je
`CONDITIONAL_NUMERICAL_RESULT`, nie „žiadny výpočet“ a zatiaľ ani
`HARD_PREDICTION`.

KBTP zatiaľ **neodvodila úplnú GR zo siete**. Dosiahla už užšie a hodnotné
medzikroky:

- dve grafové schémy numericky reprodukovali Newtonov inverse-square
  comparator (`R^2≈0.9991/0.9996`);
- background používa Friedmannovu rovnicu a kontroluje celkovú energetickú
  bilanciu;
- A2-K4 skonštruovala statický rámec, v ktorom štyri Einsteinove constraint
  rezíduá vyšli ako exaktné algebraické nuly;
- skúmaný skalárny grafový operátor má exaktnú párnosť a grafový front má
  podporné kauzálne vlastnosti vo svojom simulovanom scope.

Tieto výsledky ukazujú kompatibilitu konkrétnych redukovaných konštrukcií s
časťami Newton/Einstein ledgera. Nie sú ešte odvodením Einsteinovej rovnice

$$
G_{\mu\nu}=8\pi G T_{\mu\nu}
$$

ako continuum limity bunkovej mikrodynamiky. Chýbajú najmä univerzálne `G`,
plná dynamická Bianchi/constraint propagation, PPN, lensing, univerzálny
voľný pád, dve tenzorové polarizácie a spoločná metrika/kužeľ všetkých polí.
Staršie formulácie, podľa ktorých Bianchiho identita alebo dobrý Newtonov fit
už znamenali odvodenú GR, boli neskorším auditom správne obmedzené.

## 2. Dôležité terminologické rozlíšenie

„Štandardný model“ môže znamenať dve rôzne veci:

- **Štandardný model časticovej fyziky (SM)** dodáva známe častice,
  interakčné rýchlosti, termodynamické stupne voľnosti a collision terms;
- **GR + LambdaCDM + štandardná kozmologická perturbácia** dodávajú
  Friedmannovu geometriu, Einsteinove constrainty, štandardný tenzorový
  operátor a Boltzmannovu hierarchiu.

SM neobsahuje bunkové palivo, popol ani kvantovú gravitáciu. Tieto členy z
neho nemožno priamo „skopírovať“. Možno však požadovať, aby nová fyzika
prechádzala do overeného SM/GR správania tam, kde experimenty nevidia
odchýlku.

## 3. Zdroj pary `C_s`

Pre relativistický produkt platí všeobecná backgroundová bilancia

$$
\boxed{
\dot\rho_s+4H\rho_s=C_s
}
\tag{R1}
$$

Ak by boli nezávisle známe celé funkcie `rho_s(t)` a `H(t)`, zdroj možno
spätne rekonštruovať:

$$
\boxed{
C_s(t)=\dot\rho_s(t)+4H(t)\rho_s(t)
}.
\tag{R2}
$$

### Čo možno prevziať

- Tvar rovnice (R1) je štandardný pre relativistickú zložku.
- Ak sa para identifikuje s konkrétnou známou alebo presne definovanou novou
  časticou, Boltzmannova kinetika môže dodať collision/source integral.
- SM vie dodať `g_*s(T)` a interakčné rýchlosti známych species. Nevysvetlí
  však branching bunkového delenia do pary bez novej väzby.
- `C_s=0` je legitímny nulový comparator po produkcii/odpojení. Nie je to
  model pary vznikajúcej delením.

### Čo vedia merania

CMB a BBN obmedzujú najmä integrovanú radiačnú hustotu a jej perturbácie,
nie jedinečnú časovú funkciu zdroja. Ako ilustrácia modelovej závislosti:
Planck 2018 spolu s BAO v jednoparametrovej extenzii uvádza
`N_eff=2.99±0.17`, pri štandardnej hodnote približne `3.046`.

Zdroj skorý a krátky, zdroj slabší a dlhší alebo zmena reheatingu môžu dať
rovnaké dnešné `Delta N_eff`. Inverzia je preto degenerovaná. Dáta môžu
obmedziť parametrizovanú rodinu `C_s(a)`, nie bez dodatočných predpokladov
určiť jediný mikroskopický zdroj.

**Primárny zdroj:** [Planck 2018 results VI — Cosmological
parameters](https://www.aanda.org/articles/aa/abs/2020/09/aa33910-18/aa33910-18.html).

### 3.1 Rozdiel medzi mainstreamovým a KBTP `Delta N_eff`

Definícia pozorovateľnej veličiny je v oboch prípadoch rovnaká:

$$
\rho_{\rm rad}=\rho_\gamma
\left[1+\frac78\left(\frac4{11}\right)^{4/3}N_{\rm eff}\right].
\tag{R2a}
$$

Mainstreamový Štandardný model s troma aktívnymi neutrínami predpovedá
`N_eff≈3.045` (malý rozdiel oproti presne trom pochádza z neinstantného
neutrínového odpojenia a termálnych korekcií). Ak sa `Delta N_eff` definuje
voči tomuto základu, baseline je

$$
\Delta N_{\rm eff}^{\rm SM}=0.
$$

Podmienený KBTP comparator pridáva jeden skorý odpojený bozónový relikt s
`g_x=2` a predpokladá odpojenie pri `g_*s,dec=106.75`:

$$
\Delta N_{\rm eff}^{\rm KBTP}=0.0535,
\qquad
N_{\rm eff}^{\rm KBTP}\simeq3.045+0.0535=3.0985\simeq3.10.
\tag{R2b}
$$

| Vlastnosť | Mainstreamový SM baseline | Podmienený KBTP comparator |
|---|---|---|
| definícia `N_eff` | rovnaká | rovnaká |
| dodatočná relativistická energia | žiadna, `Delta N_eff=0` | para/relikt, `Delta N_eff=0.0535` |
| pôvod | tri aktívne neutrína a ich štandardná termálna história | navrhovaná para bunkovej genézy |
| total `N_eff` | približne `3.045` | približne `3.10` |
| dnešný vedecký status | odvodený SM baseline | `CONDITIONAL_NUMERICAL_RESULT / SOURCE_HISTORY_OPEN` |

Mainstreamová fyzika zároveň všeobecne povoľuje `Delta N_eff>0` z ľubovoľnej
extra „dark radiation“ — napríklad ďalšieho ľahkého reliktu. Samotné nameranie
`N_eff≈3.10` by preto nepotvrdilo bunkový pôvod. Špecifickou predikciou KBTP
by sa výsledok stal až vtedy, keby teória odvodila pôvod pary, jej stupne
voľnosti, teplotu/spektrum a ďalšie korelované stopy bez dodatočného fitu.

Planck 2018 + BAO uvádza v príslušnej jednoparametrovej extenzii
`N_eff=2.99±0.17`. Táto presnosť nerozlišuje SM hodnotu približne `3.045` od
podmieneného KBTP bodu približne `3.10`; číslo `0.0535` teda nie je súčasnými
týmito dátami ani potvrdené, ani vylúčené.

### 3.2 `Delta N_eff` nie je celý produktový obsah KBTP

Predchádzajúce porovnanie je zámerne iba porovnaním observable P01. KBTP
pracuje so širším produktovým obrazom: delenie alebo prestavba bunky môže
viesť k popolu, relativistickej pare, obyčajnej hmote a nezvratnej jazve.
`Delta N_eff` vidí priamo iba tú časť produktovej energie, ktorá sa v čase
BBN a rekombinácie správa ako dodatočná relativistická zložka.

Úplný backgroundový ledger musí mať schematicky tvar

$$
\boxed{
Q_f+Q_c+Q_s+Q_m+Q_I=0
},
\tag{R2c}
$$

kde `f` je palivo, `c` popol/CDM, `s` para, `m` obyčajná hmota a `I` jazva
alebo jej energetický rezervoár. Na úrovni porúch je potrebná silnejšia
kovariantná podmienka

$$
\boxed{
\sum_A Q_A^\mu=0
}.
\tag{R2d}
$$

Nie každá jazva musí mať samostatnú homogénnu hustotu. Ak je iba
topologickým záznamom s nulovou makroskopickou energiou, môže mať `Q_I=0` v
backgrounde, no stále ovplyvňovať lokálnu dynamiku a entropiu. Ak má konečnú
energetickú cenu, musí sa objaviť v `T_I^{mu nu}` a v rovniciach (R2c–R2d);
nesmie zostať skrytým rezervoárom.

| Produkt KBTP | Hlavná priama observable oblasť | Vzťah k `Delta N_eff` |
|---|---|---|
| para `s` | BBN, CMB radiačná hustota, phase shift, prípadné reliktné spektrum | priamy príspevok, ak je relativistická |
| popol `c` | `Omega_c`, rast, `S8`, lensing, halo štruktúra | nepriamy; priamy iba kým je relativistický alebo pri rozpade na paru |
| obyčajná hmota `m` | `Omega_b`, baryónové zaťaženie CMB, BBN abundancie, baryónová asymetria | spravidla nie priamy radiačný príspevok |
| jazva `I` | závisí od jej `T_I^{mu nu}`; potenciálne background, perturbácie, entropia a nezvratnosť | nie automaticky; rozhoduje stavová rovnica a energetický obsah |

V aktuálnej živej backgroundovej koľaji A1-K1 je uzavretý iba efektívny
kanál `palivo -> popol`, teda `Q_f=-Q_c`; baryóny sú v tejto presnej koľaji
konzervované. Para, tvorba obyčajnej hmoty a energetická rola jazvy patria do
širšej ontológie a otvoreného branching/sequence problému. Nemožno ich
vyhlásiť za neexistujúce, ale zatiaľ ani za uzavreté current výsledky tejto
koľaje.

Práve spoločný pôvod produktov môže dať KBTP odlišnú predikciu oproti
mainstreamovej extra dark radiation. Jedna bunková udalosť by nemala určovať
iba `Delta N_eff`, ale súčasne pomery popola, pary, hmoty a jaziev a ich
vzájomne korelované poruchy. Fyzikálne poctivý ďalší krok preto nie je
fitovať `C_s` samostatne, ale zaviesť branching funkcie

$$
B_c(a)+B_s(a)+B_m(a)+B_I(a)=1,
\qquad B_A(a)\ge0,
\tag{R2e}
$$

prípadne oddelené paralelné, sekvenčné a zmiešané kauzálne topológie. Každá
musí prejsť spoločným conservation ledgerom, BBN, CMB, rastom, lensingom a
stabilitou. Až korelovaná predikcia viacerých produktov môže rozlíšiť KBTP od
mainstreamového modelu, ktorý jednoducho pridá jednu nezávislú relativistickú
species.

### 3.3 Proveniencia pary: čo už bolo odvodené a čo ešte chýba

Staršie dokumenty obsahujú konkrétnu kauzálnu a fenomenologickú reťaz, preto
nie je správne hovoriť, že pôvod pary je úplne neznámy:

1. energia vákua je v ontológii KBTP palivom prestavby a delenia buniek;
2. spracovanie paliva má produktový rebrík: vzácny nestrávený zvyšok ako
   obyčajná hmota, dotrávený popol a dokonale spracovaný odviazaný vlnový
   produkt siete ako para;
3. historický test časovania tvorby hmoty ukázal, že neskorá tvorba hmoty
   predlžuje zvukový horizont a posúva odvodené `H0` nadol; pre požadovaný
   opačný smer bol v testovanej rodine potrebný dodatočný relativistický
   príspevok;
4. po identifikácii pary s dvoma polarizáciami skorého odpojeného vlnového
   reliktu dala štandardná entropická aritmetika
   `Delta N_eff=0.0535`, `T≈0.905 K` a historický peak približne `53 GHz`.

Preto treba viesť štyri odlišné statusy:

| Vrstva tvrdenia | Presný status |
|---|---|
| kvalitatívny pôvod pary v spracovaní vákuového paliva pri bunkovej genéze | `COARSE_GRAINED_CAUSAL_ORIGIN_PRESENT` |
| potreba extra radiácie pre opačný smer historického `H0` posunu v testovanej rodine | `HISTORICAL_BACKGROUND_DIRECTION_RESULT` |
| hodnota `Delta N_eff=0.0535` pri `g_x=2`, `g_*s,dec=106.75` | `CONDITIONAL_NUMERICAL_DERIVATION` |
| lokálny kovariantný zdroj `C_s^mu`, branching, časová podpora, exit/reheating a prežitie | `OPEN` |

Energetické zachovanie samo osebe zatiaľ nie je dôkazom, že `Q_s` musí byť
nenulové: aktuálna A1-K1 backgroundová sústava sa matematicky uzatvára aj
ako `Q_f=-Q_c` bez explicitnej pary. Ak má byť para **povinným** produktom
každej alebo genézovej triedy delení, treba navyše odvodiť aspoň jedno z:

- bunkové pravidlo s `B_s>0`;
- exact rezíduum energie-hybnosti, ktoré nemožno uložiť do popola, hmoty,
  jazvy ani prestavby siete;
- no-steam vetu, podľa ktorej všetky riešenia s `B_s=0` porušia niektorý
  povinný fyzikálny alebo observačný mantinel.

Toto spresnenie neodvoláva pôvodnú myšlienku ani vykonaný výpočet. Oddeľuje
už existujúce odvodenie identity a podmieneného množstva pary od chýbajúcej
lokálnej produkčnej rovnice.

### 3.4 Autorom určený observačný inverzný program pre paru

Autor určuje, že odpoveď na otázky **aká časť spracovanej vákuovej energie
prejde do pary, kedy sa to stane a aký relikt prežije** sa nemá zvoliť ad hoc.
Má sa odvodiť ako povolená množina z fyzikálnych zákonov a meraní.

Pre ľubovoľný prípustný backgroundový zdroj platí presná forward mapa

$$
\boxed{
\rho_s(a)=a^{-4}\left[
a_i^4\rho_s(a_i)+
\int_{a_i}^{a}\frac{a'^3 C_s(a')}{H(a')}\,da'
\right]
}.
\tag{R2f}
$$

Merania teda nepozorujú `C_s(a)` priamo. Pozorujú rôzne integrály a
perturbačné dôsledky tej istej funkcie:

| Meranie | Čo obmedzuje |
|---|---|
| BBN: `Y_p`, D/H a expanzná miera | relativistickú energiu prítomnú pri nukleosyntéze |
| CMB TT/TE/EE, damping a akustický phase shift | `Delta N_eff` pri rekombinácii a či je para free-streaming alebo fluid-like |
| rozdiel BBN verzus CMB | produkciu, rozpad alebo ohrev medzi oboma epochami |
| rovnosť hmoty a radiácie, BAO, rast a lensing | spoločný nepriamy vplyv pary, popola a hmoty na background a perturbácie |
| priame reliktné spektrum/polarizácia, ak bude merateľné | dnešnú teplotu, spektrálny tvar a identitu vlnového reliktu |

„Prežitie“ má dve oddelené časti:

1. kinematické riedenie `rho_s∝a^-4` po skončení zdroja;
2. dynamické odpojenie, pre ktoré musí interakčná miera spĺňať približne
   `Gamma_s/H<1` a integrovaná optická hĺbka po odpojení musí byť malá.

Dáta môžu obmedziť `Gamma_s/H`, free-streaming fraction a spektrum. Prečo má
para práve takú väzbu na bunky však musí zostať kompatibilné s bunkovou
mikrodynamikou; pozorovací fit nesmie zaviesť ľubovoľnú interakciu iba na
záchranu výsledku.

Keďže konečný počet observables nemôže jednoznačne invertovať ľubovoľnú
spojitú funkciu, test sa vykoná nad predregistrovanou prípustnou triedou,
napríklad nezápornými epochovými binmi alebo hladkými kompaktnými zdrojmi.
Výstupom bude:

- posterior alebo povolený pás podmienený danou triedou;
- spoločný rozsah integrovaného parného podielu a času produkcie;
- informácia, či prienik so všetkými branching, BBN, CMB a stabilitnými
  mantinelmi je neprázdny;
- explicitný zoznam neidentifikovateľných smerov, ktoré merania zatiaľ
  nerozlišujú.

Tento program môže zmeniť historický bod `0.0535` na meraniami obmedzený
KBTP rozsah. Kým sa forward model a spoločná likelihood nevykonajú, zostáva
`0.0535` podmieneným termálnym bodom, nie posteriorom.

### 3.5 Čo má teória odvodiť a čo smie prevziať pri BBN/CMB

BBN a CMB treba rozlíšiť ako **fyzikálnu výpočtovú pipeline** a ako
**namerané dáta**.

KBTP nemusí v aktuálnej stanici znovu odvodzovať overené jadrové reakcie,
slabé interakcie, atómovú fyziku rekombinácie ani všeobecnú Boltzmannovu
kinetiku z bunkovej ontológie. Smie ich zdediť zo SM/GR ako označený
low-energy backend. Musí však dodať vlastné vstupy, ktoré tento backend menia:

- `H(T)` a všetky hustoty počas BBN;
- `C_s(a)`, teplotu, interakcie a perturbácie pary;
- branching do popola a prípadne baryónovej hmoty;
- úplné Einsteinove a species perturbácie;
- počiatočné skalárne a tenzorové spektrá;
- nulový limit, v ktorom sa výpočet vráti k štandardnej fyzike.

Forward smer vedeckej predikcie je

```text
bunkové pravidlá / prípustná funkčná trieda
  -> C_s, branching, H(a), perturbácie
  -> zdedený SM jadrový + rekombinačný + Boltzmann backend
  -> Y_p, D/H, CMB TT/TE/EE/lensing a ďalšie observables
  -> porovnanie s meraniami
```

Ak bunková mikrodynamika sama určí všetky vstupy pred porovnaním s dátami,
BBN/CMB sú nezávislým testom a výsledok možno nazvať predikciou.

Ak sa `C_s(a)` alebo branching rekonštruuje z BBN/CMB dát, ide o inverznú
kalibráciu:

```text
BBN/CMB dáta + predregistrovaná funkčná trieda
  -> posterior/povolený pás C_s a branchingu.
```

Vtedy tie isté dátové body nesmú byť znovu započítané ako potvrdenie modelu.
Povinné je označiť ich ako `CALIBRATION_DATA` a testovať odvodený región na
nezávislej alebo zadržanej vrstve, napríklad:

- BBN kalibruje skorú integrovanú radiáciu, CMB testuje free-streaming phase
  shift a rekombinačný stav;
- časť CMB spektra kalibruje, zvyšné multipóly/polarizácia/lensing validujú;
- kozmologické dáta určia `Delta N_eff`, zatiaľ čo reliktná teplota,
  frekvenčný tvar alebo korelácia s popolom zostanú predikciou;
- jeden dataset určí interval, iný nezávislý dataset skúša jeho prežitie.

Pre súčasný cieľ globálnej životaschopnosti je dovolené použiť všetky
existujúce merania iba ako mantinely a pýtať sa, či je prípustný prienik
neprázdny. Taký úspech je `OBSERVATIONALLY_COMPATIBLE_EXISTENCE_WITNESS`, nie
nová predikcia ani potvrdenie mechanizmu. Predikčná sila vznikne až tam, kde
teória alebo kalibračná podmnožina zafixuje vstupy a zostávajúce observables
sú skutočne out-of-sample.

### Minimálna užitočná funkčná trieda

Namiesto jedného uhádnutého tvaru možno zaviesť

$$
C_s(a)=\Gamma\rho_f(a)B_s(a),
\qquad 0\le B_s(a)\le1,
\tag{R3}
$$

kde `B_s(a)` je podiel transferu smerujúci do pary. Musí sa súčasne viesť
protičlen v ostatných rezervoároch, aby súčet všetkých `Q_A` bol nula.
Pozorovania potom môžu obmedziť polohu, šírku a integrál `B_s(a)`. Rovnica
(R3) je návrh rekonštrukčného rozhrania, nie current zákon KBTP.

## 4. Tenzorový operátor

Overený GR comparator pre transverzálne-bezstopové tenzorové poruchy má
schematickú podobu

$$
\boxed{
h_{ij}''+2\mathcal H h_{ij}'+c_T^2k^2h_{ij}
=16\pi G a^2\Pi_{ij}^{TT}
},
\tag{R4}
$$

pričom v GR je `c_T=1`, graviton je bez hmotnosti a ďalšie disperzné členy
v tejto limite chýbajú.

### Čo možno prevziať

- Rovnicu (R4) možno použiť ako **povinnú infračervenú limitu** a nulový
  comparator.
- Bunkový operátor môže byť parametrizovaný ako GR plus párne korekcie,
  napríklad schematicky

$$
\omega^2=c_T^2k^2+\alpha_4\ell_{\rm cell}^2k^4+\cdots.
\tag{R5}
$$

- Auditovaná párnosť P10 v danom skalárnom operátore podporuje zákaz
  lineárneho nepárneho člena iba v tomto scope. Neodvodzuje tenzorovú
  rovnicu (R4), `c_T`, `alpha_4` ani spoločný svetelný kužeľ.

Ak KBTP jednoducho prijme (R4) ako axiómu bez mapy zo siete, môže používať
štandardný tenzorový sektor ako **zdedenú efektívnu fyziku**. Tým sa dá
počítať a testovať kozmológia, ale teória nebude môcť tvrdiť, že gravitáciu
alebo tenzorový operátor odvodila.

### Čo vedia merania

Merania obmedzujú koeficienty zvolenej efektívnej rodiny: rýchlosť,
disperziu, hmotnosť, polarizácie a amplitúdu primordiálneho spektra. Neurčujú
jediný mikroskopický operátor. LIGO/Virgo testy GW170817 sú konzistentné s
GR a obmedzujú modifikovanú disperziu; BICEP/Keck BK18 uvádza
`r_0.05<0.036` pri 95 % confidence. Sú to mantinely, ktoré musí kandidát
prežiť, nie odvodenie jeho bunkového pôvodu.

**Primárne zdroje:** [LIGO/Virgo tests of GR with
GW170817](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.123.011102)
a [BICEP/Keck BK18 tensor limit](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.127.151301).

## 5. Funkcia `delta(a)`

Z backgroundovej rovnice KBTP

$$
\frac{d\rho_f}{d\ln a}
=-3\delta(a)\rho_f-\frac{\Gamma}{H}\rho_f
\tag{R6}
$$

vyplýva exaktná inverzná identita

$$
\boxed{
\delta(a)=-\frac13
\left[
\frac{d\ln\rho_f}{d\ln a}+\frac{\Gamma}{H(a)}
\right]
}.
\tag{R7}
$$

### Čo možno prevziať

- SM nemá parameter `delta`; je to definícia špecifická pre palivo KBTP.
- Štandardná kozmológia poskytuje metódy rekonštrukcie efektívneho
  `w(a)`, nie identitu medzi týmto `w_eff(a)` a `delta(a)`.
- Konštantné `delta=0.02297` možno zachovať ako zmrazený benchmark a
  `delta(a)=delta_0` ako nulový comparator časového driftu.

### Čo vedia merania

Ak by dáta nezávisle určili `rho_f(a)`, `H(a)` a `Gamma`, rovnica (R7) by
dala `delta(a)`. V skutočnosti merania prevažne určujú celkovú expanziu a
rast. Rozklad na interagujúce `rho_f`, `rho_c` a `Gamma` je degenerovaný.
Derivácia hlučne rekonštruovanej `rho_f` navyše zosilňuje chyby.

Riešením je parametrická alebo regulovaná neparametrická rekonštrukcia:

$$
\delta(a)=\delta_0+\sum_i d_i B_i(a),
\tag{R8}
$$

kde `B_i` sú vopred určené bázové funkcie alebo spliny. Fyzikálne mantinely
kladú kladnosť hustôt, stabilitu, správny skorý limit, BBN/CMB/BAO/SN/LSS
kompatibilitu a zákaz skrytého módového `k`. Dátový posterior nad `d_i`
potom dá podmienený pás `delta(a)`, nie jedinečný bunkový zákon.

Modelovo nezávislé rekonštrukcie kozmologických funkcií sú známy inverzný
štatistický problém; výsledok závisí od regularizácie a zvolenej funkčnej
triedy. Príklad metódy: [Nonparametric Reconstruction of the Dark Energy
Equation of State](https://arxiv.org/abs/1009.5443).

## 6. Najrýchlejší fyzikálne poctivý postup

### Fáza I — test existencie, nie mikrofyzické odvodenie

1. Zmraziť GR/SM/štandardnú Boltzmannovu fyziku ako comparator a povinnú
   nízkoenergetickú limitu.
2. Zaviesť čo najmenšie funkčné rodiny `B_s(a)` a `delta(a)`; tenzorový
   operátor zapísať ako GR plus párne korekcie.
3. Presne zapísať conservation ledger: zdroj pary musí mať opačný súčet v
   palive/popole/ostatných rezervoároch.
4. Pred dátovým fitom aplikovať exact fyzikálne filtre: covariance, Bianchi,
   gauge, kauzalita, kladnosť, stabilita, správne nulové limity a spoločný
   svetelný kužeľ.
5. Až na preživšiu prípustnú množinu aplikovať BBN/CMB/BAO/SN/lensing/LSS a
   GW mantinely s ich neistotami a covariance.
6. Rozhodnúť iba otázku: je spoločný prienik neprázdny? Ak áno, koľaj žije
   ako `RANGE_CONDITIONAL_OPEN`; ak je certifikovane prázdny, vzniká fyzikálny
   dôvod STOP v presnom scope.

### Fáza II — vysvetľovací cieľ KBTP

Ak Fáza I nájde živý región, bunková mikrodynamika musí následne vysvetliť,
prečo vyberá práve daný `C_s`, `delta(a)` a tenzorové koeficienty. Bez tejto
fázy ide o kompatibilnú efektívnu rekonštrukciu, nie o dokončenú teóriu
bunkového priestoru.

## 7. Rozsudok pre jednotlivé veličiny

| Veličina | Prevziať mainstreamový tvar? | Obmedziť z dát? | Jedinečne odvodiť z dnešných dát? |
|---|---:|---:|---:|
| `C_s(a)` | áno, continuity/Boltzmann rozhranie | áno, iba podmienenú rodinu | **nie** |
| tenzorový operátor | áno, GR ako IR comparator/closure | áno, jeho efektívne koeficienty | **nie** |
| `delta(a)` | nie zo SM; iba rekonštrukčnú metodiku | áno, spolu s ostatnými parametrami | **nie** bez nezávislého `rho_f`, `Gamma` a identifikovateľnosti |

Najdôležitejší záver je, že chýbajúca mikrofyzika nemusí teraz zastaviť test
existencie. Môžeme zostaviť fyzikálne obmedzenú funkčnú množinu a skúsiť
nájsť aspoň jedného svedka, ktorý prejde všetkými mantinelmi. Musí však zostať
viditeľné, ktoré rovnice boli odvodené KBTP, ktoré sú zdedené z mainstreamu a
ktoré parametre boli iba rekonštruované z dát.

## 8. Súborový rozpočet

- `LIVE_SCIENTIFIC_ARTIFACTS = 1` — tento audit;
- `LIVE_CENTRAL_REGISTERS_UPDATED = 0`;
- `RELEASE_PAYLOAD_FILES_UPDATED = 0`;
- `AUDIT_PACKAGE_COPIES = 0`;
- vedecké verdicts, skóre a hĺbka: bez zmeny.
