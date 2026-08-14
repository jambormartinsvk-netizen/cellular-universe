# Priestor, Poissonov posyp, expanzia a povinné fyzikálne mantinely KBTP

**Vrstva:** `tracks/` — pracovná syntéza, nie release korpus  
**Dátum syntézy:** 2026-08-11  
**Stav:** `WORKING_SYNTHESIS / NOT_NEW_EVIDENCE / NOT_RELEASED`  
**Dosah:** teóriový základ `A1-K1` a väzba na živú koľaj `A2-K4/P5`  
**Autoritatívny vedecký účinok:** žiadny; dokument nemení rovnice, raw,
checkpointy, hĺbku `60/100`, stav P5 `3.5/6` ani aktívny blocker

## 0. Prečo tento dokument vznikol

Tento dokument sústreďuje na jednom mieste to, čo dnešný korpus KBTP hovorí
o priestore, náhodnom posype, raste siete, kozmologickej expanzii, šírení
svetla a povinných fyzikálnych zákonoch. Jeho druhým cieľom je ukázať
spojitosti medzi týmito témami a presne pomenovať chýbajúce mosty.

Zásadné rozlíšenie je:

1. **potvrdená fyzika** je mantinel, ktorý musí KBTP obnoviť vo validovanom
   rozsahu;
2. **auditovaný výsledok KBTP** platí iba v presne uvedenom matematickom
   scope;
3. **pracovná hypotéza** určuje smer mechanizmu, ale nie je dôkazom jeho
   existencie;
4. **otvorený most** je konkrétne odvodenie alebo údaj, bez ktorého sa
   susedné úrovne nesmú stotožniť.

Slovo „dokázaný“ sa pri fyzikálnom zákone používa v zmysle matematickej
identity v danom formalizme alebo veľmi presne experimentálne potvrdeného
zákona v jeho validovanej oblasti. Fyzikálne meranie nie je absolútny
matematický dôkaz bez rozsahu a neistoty.

## 1. Najkratší pravdivý súhrn dnešného stavu

Pracovná ontológia KBTP tvrdí, že makroskopický priestor môže emergovať zo
siete lokálnych bunkových stupňov voľnosti. Referenčnou geometriou je
trojrozmerný homogénny Poissonov posyp bodov a jeho Voronoiho–Delaunayova
duálna štruktúra. Kozmologická expanzia sa skúma ako rast alebo prestavba
siete, nie ako pohyb buniek do vonkajšieho priestoru.

Tento obraz dnes **nie je hotovou mikrodynamickou teóriou**. Má niekoľko
auditovaných či podmienených mostov:

- presný stereologický priemer stupňa referenčnej 3D Poissonovej–Delaunayovej
  siete;
- podmienené čítanie réžie prestavby `delta`;
- historickú numerickú podporu sublineárne sa rozširujúceho grafového frontu;
- exaktnú párnosť jedného skalárneho cosine-Laplacian operátora;
- homogénny energetický ledger s opačnými zdrojmi paliva a popola;
- módovo nezávislú normalizáciu jedného FLRW backgroundu;
- regulárnu superhorizontovú bázu, ohraničený high-`k` principal symbol,
  statické Einsteinove rezíduá a planárny Landauov range-only výsledok v
  presných scopeoch.

Chýba však jednotný lokálny zákon, ktorý by z toho istého bunkového stavu
súčasne odvodil:

- fyzickú zmenu geometrie a počet/objem buniek;
- úplný stress-energy a prenos energie aj hybnosti;
- spoločnú efektívnu metriku a kauzálny kužeľ;
- fotónový, hmotový a gravitačný operátor;
- Einsteinovu dynamiku v continuum limite;
- entropický a rezervoárový účet nezvratnej prestavby;
- úplné kozmologické poruchy a observably.

Preto je korektný stav: **fyzikálne zaujímavá a čiastočne matematicky
ohraničená hypotéza, ale nie uzavretá teória priestoru**.

## 2. Čo presne znamená Poissonov posyp

### 2.1 Matematická definícia

V homogénnom Poissonovom bodovom procese s intenzitou `rho_P` je počet bodov
v oblasti s objemom `V` náhodná veličina

$$
N(V)\sim\operatorname{Poisson}(\rho_P V).
\tag{S1}
$$

Po podmienení na počet bodov sú ich polohy nezávislé a rovnomerne rozdelené
v danej oblasti. Z bodov `x_i` možno zostrojiť:

- **Voronoiho bunku**: oblasť bodov bližších k `x_i` než ku ktorémukoľvek
  inému zárodku;
- **Delaunayovu hranu**: spojenie dvoch zárodkov, ktorých Voronoiho bunky
  zdieľajú spoločnú stenu;
- **Delaunayovu trianguláciu**: kontaktnú simpliciálnu geometriu duálnu k
  Voronoiho mozaike.

Pre ideálnu trojrozmernú Poissonovu–Delaunayovu geometriu je používaný
stereologický priemer počtu susedov

$$
\boxed{
\langle k\rangle=\frac{48\pi^2}{35}+2\simeq15.535
}.
\tag{S2}
$$

Toto je matematický comparator. Samotná rovnica (S2) nehovorí, že fyzický
priestor je Poissonov posyp, ani že dynamicky delená sieť zostáva presne v
tej istej ensemble triede.

### 2.2 Čo posyp poskytuje

Homogénny izotropný posyp poskytuje:

- bez preferovaného priestorového smeru **v ensemble priemere**;
- lokálne konečnú, nepravidelnú kontaktnú sieť;
- prirodzené spoločné rozhrania medzi susednými bunkami;
- duálnu väzbu medzi objemami, stenami a hranami vhodnú pre lokálne toky;
- škálovaciu vlastnosť: zmena intenzity mení typickú dĺžku buniek, nie
  bezrozmerný priemerný stupeň.

To je dobrý základ pre lokálnu, približne izotropnú geometriu. Nie je to
ešte metricky, kauzálne ani dynamicky úplný časopriestor.

### 2.3 Čo čistý Poissonov posyp automaticky neposkytuje

Čistý 3D Poissonov posyp nemá automaticky:

- minimálnu vzdialenosť medzi bodmi; môžu existovať ľubovoľne blízke páry;
- maximálnu dĺžku Delaunayovej hrany; vzácne veľké prázdne oblasti vytvárajú
  dlhé kontakty;
- pevný maximálny stupeň uzla;
- fyzický čas, lokálnu rýchlosť aktualizácie ani svetelný kužeľ;
- Lorentzove boosty;
- akciu, stress-energy, Einsteinov tenzor ani zákon delenia;
- dôkaz, že embeddingové súradnice sú fyzické a nie iba reprezentácia.

Tieto vlastnosti vedú k trom okamžitým guardom:

1. jeden grafový krok nesmie automaticky znamenať rovnaký fyzický čas na
   každej hrane, inak by vzácna dlhá hrana mohla vytvoriť kauzálnu skratku;
2. Planckova minimálna dĺžka nevyplýva z čistého Poissonovho procesu a musí
   byť odvodená alebo nahradená inou fyzickou regularizáciou;
3. priemerná izotropia nestačí — treba dokázať koncentráciu anizotropných
   odchýlok a ich zánik v continuum limite.

### 2.4 3D posyp s tikom verzus 4D kauzálny posyp

Trojrozmerný posyp na priestorových rezoch je rotačne a translačne
invariantný na danom reze, ale výber spoločného globálneho tiku alebo
foliácie všeobecne vyberá preferovaný rámec. To je presne otvorená otázka
`Q24`.

Poissonov posyp do štvorrozmerného Lorentzovského objemu je známy referenčný
spôsob, ako zachovať Lorentzovu invarianciu **v distribúcii**. Takýto prechod
by však zmenil objekt posypu, kauzálnu štruktúru a pravdepodobne aj stavový
priestor. Nie je preto tichou opravou dnešnej 3D koľaje. Je to E2 referenčná
možnosť, ktorá by pri prijatí vyžadovala samostatný track-identity contract.

## 3. Čo znamená, že „delenie buniek je expanzia“

### 3.1 Presná kinematická identita, ktorú treba splniť

Nech `N(t)` je počet buniek v komovej oblasti a `v_bar(t)` jej priemerný
fyzický objem na bunku. Celkový fyzický objem je

$$
V(t)=N(t)\,\bar v(t).
\tag{S3}
$$

Pre homogénnu izotropnú geometriu `V proportional a^3`, a preto

$$
\boxed{
3H=\frac{\dot V}{V}
=\frac{\dot N}{N}+\frac{\dot{\bar v}}{\bar v}
}.
\tag{S4}
$$

Ak má expanzia vznikať čisto pribúdaním buniek s konštantným fyzickým
objemovým kvantom, potom musí platiť

$$
\boxed{
\dot{\bar v}=0,
\qquad
\frac{\dot N}{N}=3H
}.
\tag{S5}
$$

Rovnice (S3)–(S5) sú najjednoduchšou presnou formuláciou tvrdenia „expanzia
je delenie“. Nie sú dnes odvodenou rovnicou KBTP; sú povinným micro-to-FLRW
mostom.

### 3.2 Prečo samotné pridanie uzla nestačí

Ak do už existujúcej geometrickej oblasti iba vložíme nový Voronoiho
zárodok, pôvodnú oblasť jemnejšie rozdelíme. Počet buniek stúpne, ale fyzický
objem oblasti nemusí stúpnuť. Ide o **refinement**, nie nevyhnutne o expanziu.

Aby delenie bolo expanziou, teória musí odvodiť aspoň jednu z možností:

- každá nová bunka nesie nové invariantné fyzické objemové kvantum;
- lokálna prestavba mení efektívnu metriku tak, že narastú fyzické
  vzdialenosti pri zachovaných komových označeniach;
- počet a geometrická miera sú zviazané iným presným relačným zákonom, ktorý
  v continuum limite dá rovnicu (S4).

Bez tohto zákona je „delenie = expanzia“ ontologická interpretácia, nie
fyzikálne odvodenie.

### 3.3 Rozlíšenie troch vecí, ktoré sa nesmú zamieňať

1. **Rast počtu buniek**: zmena `N`.
2. **Rast fyzického objemu**: zmena invariantnej priestorovej miery `V`.
3. **Kozmologické zrýchlenie**: kladné `ddot a`, ktoré závisí od
   stress-energy a tlaku, nie iba od znamienka `dot N`.

Aj keď `dot N>0` dá `H>0`, ešte z toho nevyplýva `ddot a>0`. V GR pre plochý
FLRW limit platí

$$
H^2=\frac{8\pi G}{3}\rho_{\rm total},
\qquad
\frac{\ddot a}{a}=-\frac{4\pi G}{3}
\left(\rho_{\rm total}+3p_{\rm total}\right).
\tag{S6}
$$

Pre samostatne dominujúce palivo
`p_f=(-1+delta) rho_f` je

$$
\rho_f+3p_f=(-2+3\delta)\rho_f,
\tag{S7}
$$

takže táto zložka by zrýchľovala expanziu pri `delta<2/3`. Hodnota
`delta approximately 0.02297` túto podmienku spĺňa, ale iba v podmienenom
efektívnom fluidnom čítaní. Neodvodzuje mikroskopickú príčinu tlaku.

### 3.4 Potrebný event-rate most

Nech `R[Z]` je počet lokálnych deliacich/prestavbových udalostí na jednotku
fyzického objemu a času v stave `Z`. Potom schematicky

$$
\dot N=\int_{V} \mathcal R[Z]\,dV.
\tag{S8}
$$

Ak je stav homogénny a `v_bar` konštantný, rovnice (S5) a (S8) by dali

$$
H=\frac13\,\mathcal R\,\bar v.
\tag{S9}
$$

Rovnica (S9) je iba odvodená požiadavka na budúci lokálny zákon, nie prijatý
výsledok. Ukazuje však, že teória potrebuje naraz odvodiť:

- fyzickú objemovú mieru bunky;
- lokálnu event rate;
- mapu lokálneho času na kozmický čas;
- homogenizačný zákon;
- väzbu tej istej udalosti na stress-energy.

## 4. Geometrická réžia `delta` a jej spojenie s rastom siete

Pracovný most KBTP je

$$
\boxed{
\delta_{\rm mean}=\frac{1}{\langle k\rangle+C}
},
\qquad
\langle k\rangle\simeq15.535,
\qquad C=28,
\tag{S10}
$$

čo dáva

$$
\delta_{\rm mean}=0.0229697827528021.
\tag{S11}
$$

Toto čítanie predpokladá, že cena jednej prestavby je prevrátená celková
povrchová plus vnútorná kapacita. `C=28` je aritmeticky konzistentný počet
bozónových stavov v obnovenej fáze Standard Modelu, ale fyzická identifikácia
tohto počtu s kapacitou substrátu nie je odvodená.

Ak je lokálna réžia bunky `1/(k+C)` a až potom sa priemeruje, platí Jensenov
mantinel

$$
\boxed{
\delta_{\rm loc}=\left\langle\frac{1}{k+C}\right\rangle
\geq\frac{1}{\langle k\rangle+C}=\delta_{\rm mean}
}.
\tag{S12}
$$

Formálny momentový rozvoj je

$$
\delta_{\rm loc}=
\frac{1}{\mu+C}
+\frac{\operatorname{Var}(k)}{(\mu+C)^3}
-\frac{\langle(k-\mu)^3\rangle}{(\mu+C)^4}+\cdots.
\tag{S13}
$$

Z toho vzniká dôležitá väzba medzi geometriou a kozmológiou:

- ak dynamicky rastúca sieť zachová stacionárne `P(k)`, potom môže byť
  `delta` približne konštantná;
- ak delenie mení `P(k)`, potom všeobecne vzniká `delta(a)`;
- samotný priemer `k` nestačí, pretože fluktuácie a chvosty distribúcie menia
  lokálne priemerovanú réžiu;
- konštantné `delta` v backgroundovom modeli je preto osobitná
  coarse-graining vetva, nie automatický dôsledok Poissonovho posypu.

Na uzavretie treba dynamickú rovnicu pre distribúciu stupňa alebo priamo
pre invariantný lokálny kapacitný/stress-work koeficient.

## 5. Homogénna expanzia, ktorá je už zapísaná

Živá A1-K1 backgroundová koľaj používa pri `x=ln a`

$$
\boxed{
\begin{aligned}
\frac{d\rho_f}{dx}
  &=-3\delta\rho_f-\lambda\frac{H_0}{H}\rho_f,\\
\frac{d\rho_c}{dx}
  &=-3\rho_c+\lambda\frac{H_0}{H}\rho_f,\\
\frac{d\rho_b}{dx}&=-3\rho_b,\\
\frac{d\rho_r}{dx}&=-4\rho_r,\\
H^2&=\frac{8\pi G}{3}\rho_{\rm total}.
\end{aligned}
}
\tag{S14}
$$

Pri konvencii

$$
\dot\rho_A+3H(\rho_A+p_A)=Q_A
\tag{S15}
$$

má backgroundový transfer tvar

$$
\boxed{
Q_f=-Q_c=-\Gamma\rho_f,
\qquad
\Gamma=\lambda H_0
}.
\tag{S16}
$$

Opačný súčet `Q_f+Q_c=0` uzatvára homogénny energetický ledger. Je to
skutočný prijatý čiastkový výsledok. Neurčuje však:

- priestorové zložky `Q_A^mu`;
- prenos hybnosti;
- perturbáciu `delta Q_A`;
- lokálnu event rate delenia;
- energiu jednej udalosti;
- zdroj pary, baryónov alebo jazvy;
- mikroskopickú hodnotu `Gamma` alebo `lambda`.

Hodnota `lambda=0.15` je zmrazený historicky dátami vybraný benchmark, nie
odvodená konštanta. Body `0.10` a `0.15` nevytvárajú certifikovaný interval.

Background navyše musí byť módovo univerzálny. Ak

$$
z=\frac{ka}{H_0\sqrt{\Omega_{r0}}},
\qquad p=4-3\delta,
\tag{S17}
$$

potom prijatá normalizačná identita

$$
\boxed{
\Phi(k)=A_f
\left(\frac{H_0\sqrt{\Omega_{r0}}}{k}\right)^p,
\qquad
\Phi(k)z^p=A_fa^p
}
\tag{S18}
$$

odstráni neprípustnú závislosť homogénnej expanzie od perturbatívneho módu
`k`. Toto je zásadný guard: lokálny model môže mať vlnové módy, ale vesmír
nesmie mať iný background podľa toho, ktorý mód práve počítame.

## 6. Einsteinova rovnica a čo presne znamená „splniť GR“

V klasickom makroskopickom limite musí KBTP reprodukovať Einsteinovu rovnicu
v jej validovanej doméne,

V rovniciach (S19)–(S22) používame relativistickú konvenciu `c=1`; v SI má
pravá strana rovnice (S19) faktor $8\pi G/c^4$.

$$
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}
}.
\tag{S19}
$$

Ak KBTP nechce fundamentálnu kozmologickú konštantu, môže mať
`Lambda_fundamental=0` a efekt zrýchlenia niesť v odvodenom `T_mu_nu`
paliva alebo inom presne definovanom efektívnom príspevku. Nesmie však iba
premiestniť chýbajúcu energiu na geometrickú stranu bez fyzickej
proveniencie.

Kontrahovaná Bianchiho identita

$$
\boxed{\nabla_\mu G^{\mu\nu}=0}
\tag{S20}
$$

vynucuje pre úplnú pravú stranu

$$
\boxed{\nabla_\mu T_{\rm total}^{\mu\nu}=0}.
\tag{S21}
$$

Pre interagujúce zložky

$$
\nabla_\mu T_A^{\mu\nu}=Q_A^\nu,
\qquad
\boxed{\sum_A Q_A^\nu=0}.
\tag{S22}
$$

Rovnica (S22) je silnejšia než backgroundová kancelácia dvoch skalárov.
Kontroluje energiu aj tri zložky hybnosti, znamienka, frame a gauge.

Dôležitá fyzikálna presnosť: v generickom dynamickom zakrivenom časopriestore
neexistuje jeden univerzálny globálny skalár „celkovej energie vesmíru“.
Exaktným lokálnym zákonom je kovariantná divergencia (S21). V FLRW sa z nej
odvodzuje kontinuita s `p dV` prácou. Preto sa energia červeného posunu,
boundary work a cena prestavby nesmú započítať dvakrát ako tri nezávislé
straty.

### 6.1 Čo už KBTP v GR sektore prešlo

V statickom P5.1–P5.2 scope boli rekonštruované

$$
\boxed{
R_{00}=R_{0i}=R_{\rm tr}=R_{\rm tl}=0
}.
\tag{S23}
$$

To je presná algebraická kontrola energetického, hybnostného, trace a
traceless Einsteinovho ledgera v deklarovanom statickom stave. Nie je to
dôkaz zachovania constraintov počas evolúcie.

Archivované grafové simulácie navyše reprodukovali `1/r^2` comparator v
dvoch zvolených väzbových schémach. To nie je odvodenie Einsteinových rovníc,
univerzálneho `G`, PPN, lensingu, gravitačných vĺn ani ekvivalenčného
princípu.

### 6.2 Čo musí ešte dodať continuum limita

Treba odvodiť jednu mapu

$$
Z_{\rm graph}\longmapsto
\left(g_{\mu\nu},\ T_{\mu\nu},\ \nabla,\ R^\rho{}_{\sigma\mu\nu}\right),
\tag{S24}
$$

ktorá je:

- nezávislá od relabelingu uzlov a súradnicového embeddingu;
- lokálna alebo kontrolovane kvázilokálna;
- hladká v continuum limite;
- dimenzionálne správna;
- kompatibilná s jedným kauzálnym kužeľom;
- taká, že rovnice (S19)–(S22) vzniknú bez dodatočného fitu.

Samotný stupeň uzla alebo objem Voronoiho bunky neurčuje celý Riemannov
tenzor. Zakrivenie potrebuje viac invariantných informácií o slučkách,
uhloch, objemoch, paralelnom prenose alebo ich relačnom ekvivalente.

## 7. Lagrangián nie je disperzia

Používateľský výraz „lagranžovská disperzia“ spája dve odlišné požiadavky:

1. **Lagrangián alebo akcia** určuje dynamické rovnice, symetrie, prúdy a
   stress-energy;
2. **disperzná relácia** je spektrum linearizovaných vĺn, napríklad vzťah
   medzi `omega` a vlnovým vektorom `q`.

Pre efektívny kontinuálny opis by sa typicky hľadala akcia

$$
S_{\rm eff}[g,Z,\psi]
=\int d^4x\,\sqrt{-g}\,\mathcal L_{\rm eff},
\tag{S25}
$$

z ktorej sa definuje

$$
T_{\mu\nu}
=-\frac{2}{\sqrt{-g}}
\frac{\delta S_{\rm matter}}{\delta g^{\mu\nu}}.
\tag{S26}
$$

Difeomorfizmová invariancia vedie cez Noetherovu identitu k väzbe so
zachovaním stress-energy. Gauge invariancia vedie k príslušným constraintom
a zachovaným prúdom.

KBTP však opisuje delenie ako potenciálne disipáciu a nezvratnú prestavbu.
Obyčajná uzavretá lokálna akcia je časovo reverzibilná. Preto existujú iba
dve čestné cesty:

- fundamentálny uzavretý unitárny zákon a odvodený coarse-grained
  disipativný limit;
- explicitná otvorená/nerovnovážna formulácia s pomenovanými rezervoármi,
  šumom, passivitou, kauzalitou a entropickou produkciou.

Nie je prípustné zaviesť disipáciu bez protiledgera a potom od nej žiadať
Noetherovo zachovanie ako keby systém bol uzavretý.

## 8. Svetlo, disperzia a spoločné limitné `c`

### 8.1 Auditovaný skalárny výsledok

Pre reálny symetrický nevažovaný grafový Laplacián bol auditovaný
bezrozmerný Rayleighov podiel

$$
\boxed{
\widehat\lambda(\mathbf q)=
\frac{2}{N}\sum_{\langle ij\rangle}
\left[1-\cos(\mathbf q\cdot\boldsymbol\Delta_{ij})\right]
}.
\tag{S27}
$$

Je presne párny,

$$
\boxed{
\widehat\lambda(\mathbf q)=\widehat\lambda(-\mathbf q)
},
\tag{S28}
$$

takže v tomto skalárnom operátore nie je nepárny lineárny člen v `q`.
Vedúci člen je však všeobecne anizotropný kvadratický tvar
`q_i A^{ij}q_j` a prvá diskrétna korekcia je štvrtého rádu.

`widehat lambda` nie je fyzická frekvencia. Potrebná je odvodená časová alebo
väzbová škála,

$$
\omega^2=\Omega_{\rm cell}^2\widehat\lambda.
\tag{S29}
$$

Hodnota `Omega_cell` dnes odvodená nie je.

### 8.2 Všeobecný low-energy tvar

Linearizovaný sektor `s` môže mať schematicky

$$
\omega_s^2(\mathbf q)
=q_i A_s^{ij}q_j
+B_s^{ijkl}q_iq_jq_kq_l+\cdots.
\tag{S30}
$$

Na obnovenie lokálnej Lorentzovej fyziky treba v continuum limite najmenej:

$$
A_s^{ij}=c^2\delta^{ij}
\quad\text{pre všetky fyzické sektory }s,
\tag{S31}
$$

spoločnú časovú kinetiku, správne boosty a potlačenie neprípustných vyšších
členov. Párnosť odstraňuje odd člen, ale sama neodstraňuje:

- anizotropiu `A^{ij}`;
- kvadratické alebo kvartické Lorentz-porušenie;
- rozdielne `c_s` rôznych spinov;
- birefringenciu;
- preferovaný rámec časovej aktualizácie;
- nesprávne hmotové alebo gauge constrainty.

### 8.3 Fyzický fotón potrebuje viac než skalárnu vlnu

Úplný elektromagnetický limit musí obnoviť:

- lokálnu `U(1)` gauge redundanciu;
- Gaussov constraint;
- dve transverzálne fotónové polarizácie;
- nulovú alebo experimentálne prípustnú hmotnosť fotónu;
- mikrokauzalitu;
- správnu väzbu na nabité hmotné polia;
- rovnakú efektívnu metriku ako hodiny, meradlá a gravitácia;
- absenciu neprípustnej polarizačnej disperzie.

Súčasný skalárny grafový operátor preto nie je Maxwellov operátor.

### 8.4 Signálový front

Historické simulácie našli

$$
\sigma(R)\propto R^\chi,
\qquad
\chi\simeq0.26\text{--}0.32<1,
\tag{S32}
$$

takže `sigma/R -> 0` v testovanom scalingu. Je to mechanizmus relatívneho
zaostrovania frontu. Fyzický svetelný kužeľ však vyžaduje:

- continuum a veľkoobjemovú limitu;
- presnú mapu grafového času na vlastný čas;
- kontrolu chvosta príchodových časov, nie iba šírky frontu;
- rovnaký výsledok pre fotóny a všetky ostatné sektory;
- lokálnu boostovú kovarianciu.

### 8.5 Potvrdené experimentálne mantinely evidované vo v3.18

Súčasný register používa ako porovnávacie mantinely:

- spoločnú rýchlosť gravitačných vĺn a gama žiarenia z GW170817/GRB170817A
  na relatívnej úrovni približne `10^-15`, po započítaní neistoty emisie;
- veľmi silné GRB medze na lineárnu a kvadratickú energetickú disperziu
  fotónov;
- ekvivalenčný princíp z MICROSCOPE na úrovni rádovo `10^-15` pre testované
  zloženia.

Tieto čísla nemožno dosadiť priamo do `widehat lambda(q)` bez fyzickej mapy
`q -> energia fotónu`, časovej normalizácie, znamienka a source likelihood.

## 9. Spoločný svetelný kužeľ, ekvivalenčný princíp a gravitácia

Povinným cieľom je

$$
\boxed{
c_\gamma=c_{\rm GW}=c_{\rm matter}=c
}.
\tag{S33}
$$

Táto rovnosť nie je iba zhoda troch čísel. Vyžaduje jednu lokálnu efektívnu
metriku, ktorá súčasne určuje:

- nulové geodetiky svetla;
- charakteristiky gravitačných vĺn;
- lokálne hodiny a meradlá hmoty;
- univerzálny voľný pád;
- kauzálnu podporu interakcií.

Najsilnejšia možná spojitosť teórie je preto aj jej najtvrdší test: **ten
istý coarse-grained geometrický objekt by mal generovať Einsteinovu krivosť,
svetelný kužeľ aj hmotové kinetické členy**. Ak sa tieto tri štruktúry
odvodia z troch nezávisle nastavených operátorov, spoločný substrát prestáva
vysvetľovať ich univerzalitu a iba ju znovu vloží ako tri fitované podmienky.

## 10. Zachovanie energie pri delení a boundary work

Lokálna bunková udalosť musí mať jeden spoločný svetový tubus a jeden
energeticko-hybnostný ledger. Schematicky musí platiť

$$
\Delta E_{\rm parent}
+W_{\rm boundary}
=\sum_r\Delta E_r,
\tag{S34}
$$

kde pravá strana zahŕňa všetky dcéry, popol, paru, hmotné excitácie,
rezervoáre a prípadnú jazvu. Presná kovariantná forma je integrálom
`T^{mu nu}` cez uzavretú worldtube hranicu, nie ľubovoľným súčtom skalárov.

Živý RW1 program preto používa:

- celý existujúci `T_loc[Z_rec]`;
- budúcnosťou orientovaný Landauov smer `u_cell` iba na regular Type-I
  nedegenerovanej doméne;
- causal-traction projekciu zachovávajúcu energy, normal-normal a mixed
  traction sektory;
- jednu fyzickú spoločnú kontaktnú plochu `Sigma_prep`;
- 0/1 vlastníctvo zdieľaného kontaktu podľa pre-event kauzálnej orientácie,
  pričom nejednoznačnosť vracia `LIVE/WAITING`;
- oddelenie energy-valued work 1-formy od power ledgera.

Toto je presne miesto, kde sa spájajú geometria a energia. Rozhranie nesmie
byť raz geometrickou stenou a druhýkrát nezávislým energetickým kanálom;
inak by sa plocha alebo práca započítala dvakrát.

## 11. Landauov rámec, kauzalita a regularita

V interface-adapted `1+1` ortonormálnom rámci nech

$$
E=T^{(00)},
\qquad q=T^{(0n)},
\qquad P_n=T^{(nn)},
\qquad S=E+P_n.
\tag{S35}
$$

Prijatá planárna range-only podmienka je

$$
\boxed{
q\neq0:\quad |S|>2|q|,
\qquad
v_L=\frac{2q}{S+\operatorname{sgn}(S)\sqrt{S^2-4q^2}}
},
\tag{S36}
$$

a pre nulový tok

$$
\boxed{
q=0:\quad S\neq0,
\qquad v_L=0
}.
\tag{S37}
$$

Okrem toho treba Type-I klasifikáciu, jednoduchý časupodobný eigensmer,
priečnu nedegenerovanosť, budúcu orientáciu a hladké okolie. Výsledok
nepreukazuje neprázdnosť fyzického packetu ani dynamickú stabilitu. Ukazuje
však presne, ako potvrdená kauzálna požiadavka dáva ostrú algebraickú hranicu
na lokálny energetický tok.

## 12. Stabilita, hyperbolicita, pozitivita a passivita

Každý fyzický priestorový mechanizmus musí spĺňať:

1. **well-posedness**: počiatočné dáta určujú lokálne riešenie a malé zmeny
   dát nevytvoria nekontrolovanú odpoveď;
2. **hyperbolicitu/charakteristiky**: signálové kužele sú reálne a kauzálne;
3. **žiadny ghost**: kinetický sektor nemá fyzické zápornonormové alebo
   neobmedzene záporné energetické stupne voľnosti;
4. **žiadnu neprípustnú gradientovú nestabilitu**;
5. **kladnosť fyzických hustôt** a `H^2>0` v požadovanom backgroundu;
6. **passivitu**: lokálna odozva nevyrába čistú prácu z ničoho;
7. **source-off limit**: po vypnutí fyzického zdroja nevznikne skrytý tok.

Auditovaný high-`k` principal symbol A2-K4 má v presnom efektívnom scope

$$
\boxed{
\mathcal P_{\rm high-k}(\mu)
=\mu^4(\mu^2+1)\left(\mu^2+\frac13\right)
}.
\tag{S38}
$$

Neobsahuje K4-špecifický exponenciálne rastúci high-`k` koreň v tomto
scope. Nie je to úplná no-ghost, silná hyperbolicita ani globálna stabilita.

## 13. Termodynamika, nezvratnosť a šíp času

Ak je delenie disipativné, úplný entropický účet musí obsahovať entropický
prúd

$$
\boxed{\nabla_\mu s^\mu_{\rm total}\geq0}
\tag{S39}
$$

v presne definovanom coarse-grained scope. Treba zahrnúť entropiu:

- paliva;
- nových buniek a kontaktov;
- popola, pary a hmotných excitácií;
- rezervoárov a prípadného šumu;
- jazvy alebo pamäťového registra;
- gravitácie/horizontov tam, kde je také čítanie fyzicky definované.

Klasické energy conditions ako NEC nie sú univerzálne dokázané zákony
všetkej kvantovej fyziky a nemajú sa bez scope pridávať ako absolútny axióm.
Povinné sú konkrétne kauzálne, stabilitné, pozitivitné a observačné podmienky
príslušnej realizácie.

Pravidlo V-spojov

$$
n_V^{\rm new}=\frac12 n_V^{\rm old}+\frac12 C,
\qquad n_V^*=C
\tag{S40}
$$

a historické hranicové škálovanie približne `R^1.97` sú klasický comparator.
Nie sú dôkazom kvantovej entanglement entropy, Bekensteinovho zákona ani
šípu času.

## 14. Kvantová fyzika a gauge zákony, ktoré musí substrát obnoviť

Ak má byť KBTP fundamentálnejšia než QFT, musí v experimentálne overenom
limite reprodukovať minimálne:

- lineárny Hilbertov opis alebo fyzicky ekvivalentnú kvantovú štruktúru;
- unitárnosť uzavretého systému alebo CPTP dynamiku otvoreného systému;
- zachovanie pravdepodobnosti a pozitivity;
- no-signalling a mikrokauzalitu;
- Boseho/Fermiho štatistiku a správne kvantové čísla;
- gauge constrainty Standard Modelu;
- lokálnu Lorentzovu QFT limitu;
- stabilné častice, hmotnosti a väzby v testovaných rozsahoch.

Toy dephasing jazvy preukázal iba CPTP, zachovanie stopy, potlačenie
koherencie a no-signalling v testovanom kvbitovom scope. Nevytvoril jeden
objektívny výsledok, Bornovo pravidlo ani trvalý fyzický register.

## 15. Gauge, relabeling a otázka, či zmena priestoru je fyzická

Embedding uzlov do súradníc môže obsahovať reprezentáciu, ktorá nie je
fyzikálnym stupňom voľnosti. Preto aktuálny RW1 program rozlišuje

$$
Q_Z=V_{\rm raw}(Z)/V_{\rm rel}(Z),
\tag{S41}
$$

kde `V_rel` obsahuje iba súradnicové zmeny, reparametrizácie a relabelingy
zachovávajúce fyzický stav.

Toto rozlíšenie je fundamentálne aj pre expanziu. Ak je navrhovaná zmena
hrán, plôch alebo polôh iba relabelingom, nevznikla fyzická expanzia. Fyzický
tangent musí mať aspoň jeden invariant, napríklad zmenu relačného objemu,
plochy, kapacitnej odozvy, spektra alebo inej observably, ktorý nemožno
odstrániť zmenou súradníc.

Aktuálny accepted výsledok D2SW13 je

`N1_CERTIFICATE_DATA_WAITING`. Korpus zatiaľ nemá:

- exact rozsah/tangent aspoň jednej kontaktnej kapacity `C_e^reg` v
  konkrétnom stave;
- úplný diferenciál gluing, geometrických, passivity, conservation, Landau
  a gauge constraintov `D C_Z`;
- hash-bound same-ontology krivku `Z(s)` s nonvertical invariantom;
- ani univerzálny dôkaz, že všetky full-constraint tangenty sú vertikálne.

Preto dnes nevieme certifikovať, či aspoň jedna infinitesimálna zmena
kontaktnej kapacity/spoločného rozhrania predstavuje fyzickú zmenu priestoru
a nie iba reprezentáciu. To je najskorší lokálny blocker živého RW1
mechanizmu.

## 16. Jedna spoločná kontaktná plocha ako kľúčová spojitosť

Aktuálny same-track packet správne určuje, že spoločná kontaktná plocha a
`Sigma_prep` sú **jeden fyzický primitívny objekt**, nie dva nezávislé
smery. Z toho vyplýva:

- jedna odvodená metrika rozhrania;
- jedna orientácia a normála;
- jedna hranica;
- jedna gluing podmienka;
- jedno započítanie plochy a boundary work;
- matched-face derivácia rodiča a pripravovaného rozhrania.

Tento princíp spája štyri doteraz oddelené problémy:

1. Voronoiho stena je geometrický kontakt;
2. Delaunayova hrana nesie lokálnu susednosť/prenos;
3. traction `T^{mu nu}n_nu` nesie energiu a hybnosť cez tú istú stenu;
4. zmena tej istej steny môže byť lokálnym geometrickým príspevkom k
   expanzii.

Ak sa podarí odvodiť všetky štyri body z jedného stavového primitíva, vznikne
skutočný unifikačný most. Ak sa každý bod nastaví zvlášť, model bude mať
štyri voľné mapy namiesto jedného mechanizmu.

## 17. Najhlbšie spojitosti a ich dôsledky

### 17.1 Stacionárny posyp môže vysvetliť konštantnú réžiu iba podmienečne

Poissonova–Delaunayova bezrozmerná štatistika nezávisí od intenzity posypu.
Ak rast siete prebieha samopodobne a distribúcia `P(k)` zostáva stacionárna,
`<k>` a prípadne `delta` môžu zostať približne konštantné počas expanzie.
To je prirodzená spojitosť medzi scale-free topológiou a takmer konštantným
`w_f`.

Nie je to však veta o delení. Delenie môže vytvoriť korelácie, meniť chvost
`P(k)` a tým meniť `delta_loc`. Potrebný je dynamický invariant alebo
evolučná rovnica distribúcie.

### 17.2 Ten istý zákon musí určiť počet buniek aj energetický transfer

Background má `Gamma rho_f`; geometrický obraz má event rate `R`. Bez
odvodenia vzťahu medzi `Gamma`, energiou jednej udalosti a `R` sú expanzia a
premena paliva iba dve paralelné parametrizácie. Najmenší zjednocujúci most
má tvar

$$
\mathcal R[Z]
\longrightarrow
\left(\dot N,\ Q_A^\mu,\ \Delta g_{\mu\nu},\ \Delta s^\mu\right)
\tag{S42}
$$

z jedného pre-event stavu `Z` a bez ďalšej fitovanej energetickej škály.

### 17.3 Noetherov prúd je prirodzený most medzi akciou a RW1

Ak existuje lokálna difeomorfizmovo/gauge invariantná akcia alebo jej
nerovnovážny ekvivalent, jej Noetherove identity určujú stress-energy a
prúdy. RW1 traction-current worldtube test potom nie je dodatočný
účtovnícky trik, ale lokálna hraničná projekcia toho istého zákona. Toto je
najpriamejšia cesta k súčasnému splneniu:

- conservation;
- covariance;
- boundary work;
- integrability;
- gauge descent;
- source-off limitu.

### 17.4 Rovnaká efektívna metrika musí riadiť expanziu aj svetlo

FLRW `a(t)` a lokálne `c` nesmú pochádzať z nesúvisiacich máp. Ak
`g_mu_nu[Z]` vznikne z coarse-grainingu siete, jeho časová časť a lokálne
charakteristiky musia určovať svetelný kužeľ, zatiaľ čo priestorová časť
určuje fyzické objemy a expanziu. Tým sa rovnice (S4), (S19) a (S33)
stávajú tromi projekciami jedného geometrického objektu.

### 17.5 Náhodná izotropia nestačí bez homogenizačnej vety

Ensemble priemer `A^{ij} proportional delta^{ij}` nestačí pre jeden fyzický
vesmír. Treba ukázať, že na mierke `L` klesajú anizotropné fluktuácie,
disperzia frontu a birefringentné rozdiely pod experimentálne medze, pričom
zriedkavé dlhé hrany nevytvoria fat-tail kauzálne porušenia.

### 17.6 Nezvratné delenie spája kozmológiu so šípom času

Ak počet buniek monotónne rastie a prestavba produkuje entropiu alebo
trvalú jazvu, rovnaký lokálny proces by mohol spájať expanziu s fyzickou
nezvratnosťou. To je silná vysvetľovacia možnosť. Vyžaduje však explicitný
register, entropický prúd a mikroskopicky uzavretú dynamiku; monotónny `N`
sám nie je dôkaz šípu času.

### 17.7 Expanzia nie je automaticky vznik hmoty

Zachovanie celkového stress-energy povoľuje presun energie medzi kanálmi,
ale neurčuje, že produktom sú baryóny, CDM/popol alebo para. Aktuálny A1-K1
ledger zachováva baryóny a prenáša energiu iba medzi palivom a CDM/popolu.
Vznik Standard Model hmoty zostáva samostatným mikrofyzickým problémom.

## 18. Povinný súbor zákonov a dnešný stav ich splnenia

| Oblasť | Povinnosť | Dnešný stav KBTP |
|---|---|---|
| relačná geometria | fyzické observably nesmú závisieť od súradníc ani relabelingu | quotient/gauge pravidlo definované; konkrétny nonvertical RW1 tangent chýba |
| dimenzia a continuum | odvodiť 3+1D hladkú limitu a metriku | otvorené |
| expanzia | odvodiť `3H=dot N/N+dot v_bar/v_bar` z lokálnej udalosti | otvorené |
| Einstein/GR | obnoviť EFE, Bianchi, PPN, lensing a GW | statické rezíduá a Newton comparator iba čiastočne |
| conservation | `sum_A Q_A^mu=0` bez skrytého rezervoára | backgroundový skalárny súčet prijatý; full current otvorený |
| Lorentz/kauzalita | spoločný kužeľ a boostová kovariancia | skalárna párnosť a front comparator iba čiastočne |
| elektromagnetizmus | U(1), dve polarizácie, Maxwell, bez birefringencie | neodvodené |
| ekvivalenčný princíp | univerzálny voľný pád a jedna metrika | neodvodené |
| stabilita | no ghost, hyperbolicita, žiadna neprípustná gradientová nestabilita | high-`k` partial PASS; úplná veta chýba |
| termodynamika | passivita a `div s_total >= 0` | otvorené |
| kvantová fyzika | unitárnosť/CPTP, gauge, štatistika, no-signalling | iba úzky dephasing toy scope |
| hmotné sektory | Standard Model limita a stabilná hmota | neodvodené |
| kozmológia | jeden `H(a)`, úplné poruchy, CMB/BBN/BAO/LSS/lensing | background conditioned; A2-K4 `LIVE/WAITING 60/100` |
| observably | jedna frozen model-to-data mapa s kovarianciou | plný A3 likelihood neotvorený |

## 19. Najmenší koherentný program ďalšieho odvodenia

Nasledujúce poradie minimalizuje voľné predpoklady a spája dnešný RW1
blocker priamo s otázkou priestoru:

1. **Zmraziť jeden regular stav `Z`** s existujúcou kontaktnou geometriou,
   kapacitami a jediným spoločným rozhraním.
2. **Dať kontaktnej kapacite fyzickú operačnú definíciu** iba z existujúcej
   pasívnej traction/current odozvy a invariantnej bezrozmernej deformácie;
   bez novej energetickej škály.
3. **Zostrojiť hash-bound krivku `Z(s)`** a vypočítať všetky matched-face,
   geometry, passivity, conservation, Landau a gauge derivácie.
4. **Certifikovať nonvertical invariant** alebo dokázať univerzálny zero
   certificate. Až tu sa ukáže, či sieť má fyzickú infinitesimálnu zmenu.
5. **Odvodiť local event-rate a worldtube ledger** z toho istého zákona.
6. **Odvodiť mapu počet/objem/metrika**, ktorá dá rovnice (S4)–(S5).
7. **Odvodiť continuum stress-energy a Noetherove identity**, potom EFE a
   dynamické constrainty.
8. **Linearizovať ten istý zákon** a odvodiť celý fotónový, hmotový a
   gravitačný principal symbol, spoločné `c`, disperziu a stabilitu.
9. **Uzavrieť P5.4 a G7**, až potom CMB/LSS výpočet a spoločnú likelihood.

Toto poradie bráni trom častým skratkám:

- dosadiť `H(a)` bez odvodenia fyzického rastu siete;
- vyhlásiť párny skalárny grafový operátor za fotón a Lorentzovu vetu;
- vyhlásiť backgroundové zachovanie energie za úplnú Einsteinovu/Bianchiho
  konzistenciu.

## 20. Konkrétne hranice platnosti a no-go body

Same-track realizácia zostáva fyzicky možná iba ak súčasne existuje aspoň
jeden spoločný stav/lokálny zákon, ktorý:

- má fyzický non-gauge geometrický smer;
- má neprázdny regular kapacitný rozsah;
- zachová gluing jednej spoločnej plochy bez double countu;
- spĺňa passivitu, Landauovu regularitu a kauzalitu;
- uzatvorí `sum Q_A^mu=0`;
- dá kladné hustoty a `H^2`;
- vytvorí jednu módovo nezávislú FLRW expanziu;
- má well-posed stabilnú linearizáciu;
- obnoví spoločný svetelný kužeľ a ekvivalenčný princíp;
- má úplný entropický a rezervoárový účet;
- prejde spoločnou observačnou mapou.

Zlyhanie jedného konkrétneho ansatzu zabíja iba tento ansatz. Fyzikálny
STOP koľaje vyžaduje certifikovanú prázdnosť celej presne zmrazenej
prípustnej množiny. Aktuálne chýbajúce `D C_Z` alebo stavová krivka preto
znamenajú `LIVE/WAITING`, nie uzavretie A2-K4 ani celej teórie.

## 21. Najdôležitejšie závery hlbokej analýzy

1. **Poissonov posyp je dobrý izotropný geometrický comparator, ale nie
   hotový časopriestor.** Chýba čas, causal rule, minimálna škála a
   homogenizačná veta.
2. **Delenie uzlov nie je samo expanzia.** Fyzickú expanziu definuje zmena
   invariantného objemu/metriky; povinný most je rovnica (S4).
3. **Zrýchlenie je stress-energy tvrdenie.** Musí vyplynúť z tlaku a
   Einsteinovej rovnice, nie iba z rastúceho `N`.
4. **Najlepšia unifikačná príležitosť je spoločné rozhranie.** Tá istá
   Voronoiho stena môže niesť geometriu, susednosť, traction/current a
   lokálny príspevok k expanzii.
5. **Noether–worldtube most je prirodzené centrum mechanizmu.** Môže spojiť
   akciu alebo nerovnovážny zákon, conservation a boundary work.
6. **Lorentzova fyzika potrebuje viac než náhodnosť a paritu.** Potrebuje
   spoločnú metriku, boosty, všetky spinové sektory a experimentálne malé
   aj párne korekcie.
7. **Konštantná `delta` vyžaduje stacionárnu rastovú štatistiku alebo inú
   dynamickú ochranu.** Poissonov priemer sám ju počas delenia negarantuje.
8. **Aktuálny RW1 blocker je fundamentálny, nie iba technický.** Bez
   nonvertical constrained tangentu ešte nevieme, či navrhovaná zmena
   kontaktu je fyzická deformácia priestoru.
9. **Overená fyzika nie je konkurent KBTP.** Je prienikom mantinelov, v
   ktorom musí existovať aspoň jeden kompletný bunkový svedok.

## 22. Proveniencia a záväzné nonclaims

### Hlavné current zdroje

- `tracks/RELEASE/V3_18/DEV_SURVIVAL_REWRITE/theory/SK/01_Bunkovy_Vesmir_v3.18_SK.md`
  — current fyzikálny opis, rovnice a scope;
- `tracks/RELEASE/V3_18/DEV_SURVIVAL_REWRITE/theory/SK/03_Methodology_and_Question_Register_v3.18_SK.md`
  — otázky, dôkazové triedy a feasibility pravidlá;
- `tracks/RELEASE/V3_18/DEV_SURVIVAL_REWRITE/theory/SK/04_Theory_Existence_Conditions_Register_v3.18_SK.csv`
  — register EC01–EC43;
- `tracks/00_CURRENT_EXECUTION_PLAN.md` — jediný globálny živý stav;
- `tracks/A1/A1K1/A2/A2K4/HISTORY/00_EVENT_LEDGER.md`, task601, task607 a
  authoritative EOF task610A — exact current RW1 blocker a handoff.

### Nonclaims

Tento dokument:

- nevyhlasuje Poissonov posyp za fyzicky potvrdený substrát;
- neodvodzuje Planckovu veľkosť bunky;
- nevyhlasuje delenie za dokázaný pôvod expanzie;
- nevyhlasuje `C=28`, `delta=0.02297` ani `lambda=0.15` za konštanty prírody;
- nevyhlasuje skalárnu párnosť za úplnú Lorentzovu invarianciu;
- nevyhlasuje Newton comparator za Einsteinovu gravitáciu;
- nevyhlasuje statické rezíduá za dynamický Einstein–Boltzmann PASS;
- nepridáva nové pole, škálu, topológiu, causal rule, ownera, rezervoár ani
  fit;
- nevykonáva Python, sieťový zber dát ani official run;
- nemení stav `A2-K4 LIVE/WAITING 60/100`, P5 `3.5/6` ani aktívny task610A
  provenance gate.
