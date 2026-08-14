# A2 — ledger realizovateľnosti funkcií a kernelov

**Brána:** `FS-GATE-01`  
**Dátum:** 2026-07-16; **revízia R2:** 2026-08-14 (externý audit 2, V.6 + V.7)  
**Rozsah:** živé záložné rodiče A2-K7, K8, K9, K11 a K12; K10 patrí pod
samostatný background A1-K2  
**Skórovací účinok:** žiadny  
**Metodika:** `tracks/METHODOLOGY/00_CONSTRAINT_FEASIBILITY_GATE_SK.md`
**Stav:** `FROZEN_PENDING_A0` — viď `tracks/A0/00_STATION.md`

## 0. Revízia R2 — čo sa zmenilo a prečo

**R2-1: `FS-C1` presunuté z tvrdého obalu do mäkkých cieľov.**

Audit 2, V.6 ukázal rozpor vnútri tohto ledgeru. `FS-C1` požaduje
`q(a) = Γρ_f`, `Γ = λH₀` — čo je fenomenologický ansatz z A1-K1, povýšený na
povinný mantinel pre všetkých päť kandidátskych mikrofyzík. Dôsledok:
K7, K8, K9, K11 a K12 nehľadali „lokálny produkčný zákon". Hľadali
**mikrofyzikálnu realizáciu presne tohto ansatzu** — podstatne menší priestor,
definovaný tým, čo nebolo odvodené.

Horšie: §5.1 release-u pripúšťa, že `λ = 0.15` je *„historically
data-selected"*. Tým `FS-C1`, ako bol inštancovaný, **porušoval `FS-C11`**
toho istého ledgeru, ktorý sadzby z trafenia dát zakazuje. Tvrdý obal
obsahoval mantinel, ktorý vlastné predikčné kritérium zakazuje.

Dôsledok pre existujúce výsledky: **všetkých pätnásť certifikátov prázdnosti
v tomto ledgeri je podmienených `FS-C1`.** Nie sú to výpovede o tom, či je
bunková produkcia možná; sú to výpovede o tomto ansatze. Zostávajú platné vo
svojom scope, ale ich scope sa týmto explicitne zužuje. Nič sa nemaže.

Nový režim: mikrofyzika určí **tvar** `q`, a až výsledný `H(a)` sa porovná
s dátami. Tým sa obráti doterajšia logika, ktorá fixovala kozmológiu a hľadala
mikrofyziku pod ňu.

Otvorená otázka, ktorú `FS-C1` zakrýval a ktorá zostáva nezodpovedaná:
`Γ = λH₀ ≈ 3.2×10⁻¹⁹ s⁻¹` je lokálne prípustné iba ak je `Γ` konštanta
prírody. Potom je ale nevysvetlené, prečo je práve `0.15 ×` dnešnej Hubbleovej
rýchlosti — to je problém kozmologickej konštanty prenesený na `Γ`.

**R2-2: nový mantinel `FS-C13` — finitný rez.** Viď §1.

| ID | Nový status |
|---|---|
| `FS-C1` | **mäkký cieľ**, nie tvrdý obal |
| `FS-C13` | **nový tvrdý obal** — finitný rez priestoru `X_K` |

## 1. Spoločný tvrdý obal A1-K1

Každý kandidát musí pri tom istom parameterovom bode splniť:

| ID | Spoločný mantinel | Povinný výsledok alebo okrajová hodnota |
|---|---|---|
| `FS-C13` | **finitný rez** (nový, R2) | pred otvorením contractu je deklarovaný `DERIVATION_ORDER = n`, konečnorozmerný `COEFFICIENT_SPACE` a `DECISION_METHOD = SOS \| CAD`; bez toho sa otázka existencie neotvára |
| `FS-C2` | celková conservation | `sum_A Q_A^mu=0` pre background aj poruchy |
| `FS-C3` | backgroundová univerzálnosť | `partial H(a)/partial k=0`; žiadny fixed Fourierov mód v hustote |
| `FS-C4` | pozitivita | `rho_A>=0`, `H^2>0`, pozitívna semidefinitná noise/kinetická matica podľa mechanizmu |
| `FS-C5` | nulová väzba | pri spoločnej väzbe `g->0` zmizne nový tok, sila, produkcia aj súvisiaci šum |
| `FS-C6` | zánik zdroja | pri `rho_f->0` musí produkčný tok zmiznúť a nijaká reakčná sadzba nesmie divergovat |
| `FS-C7` | zánik prijímača | pri `rho_c->0` zostane operátor konečný a nevytvára delenie nulou |
| `FS-C8` | vacuum-like limit | pri `delta=1+w_f->0` musí každý člen delený `delta rho_f` mať čitateľ rovnakého alebo vyššieho rádu |
| `FS-C9` | veľké/malé škály | `k->0` dá regulárnu constraintovo prípustnú bázu; `k->infinity` nemá ghost, záporné `c_s^2`, acausalitu ani runaway |
| `FS-C10` | lokálnosť | argumentmi sú lokálne polia/stavy; žiadny budúci stav ani voľný profil v `ln a` |
| `FS-C11` | predikčnosť | všetky sadzby a pomery pochádzajú z jedného deklarovaného mechanizmu alebo nezávislého merania, nie z trafenia `S8/H0` |
| `FS-C12` | observačný filter | BBN/CMB/BAO/lensing/rast sa aplikujú až na fyzikálne neprázdnu množinu s vopred zmrazenými rozsahmi |

`FS-C12` nie je požiadavka trafiť presne `S8=0.82` alebo `H0=68`. Tieto
čísla sú cieľ auditu, nie okrajové podmienky, ktorými sa smie skonštruovať
funkcia.

### 1.1 Mäkké ciele (od R2)

Mäkký cieľ je porovnávací bod **po** nájdení svedka, nie mantinel, ktorý
priestor hľadania orezáva vopred.

| ID | Mäkký cieľ | Poznámka |
|---|---|---|
| `FS-C1` | `q(a) = Γρ_f(a)`, `Γ = λH₀` | ansatz z A1-K1; `λ = 0.15` je historicky data-selected. Kandidát, ktorý dá iný tvar `q`, **nie je tým vylúčený**; jeho `H(a)` sa porovná s dátami samostatne a to porovnanie je testovateľné |

### 1.2 Ako sa uplatňuje `FS-C13`

```text
1. zafixuj derivacny rad n
2. napis NAJVSEOBECNEJSI lokalny prenosovy stvorvektor v tom rade:

   Q_A^mu = a_A rho_f u_f^mu + b_A rho_f u_c^mu + c_A grad^mu rho_f
          + d_A rho_f h^{mu nu} u_{f,nu} + e_A rho_c h^{mu nu} u_{f,nu} + ...

   s koeficientmi ako funkciami lokalnych skalarov (rho_f, rho_c, delta),
   pri sum_A Q_A^mu = 0

3. FS-C2 (conservation), FS-C4 (pozitivita), FS-C6/C7/C8 (limity zdroja,
   prijimaca, vakua), FS-C9 (ziadny ghost, c_s^2 >= 0, kauzalita) a
   FS-C10 (lokalnost) su potom SEMIALGEBRAICKE podmienky na konecne
   mnoho koeficientov

4. prazdnost semialgebraickej mnoziny je ROZHODNUTELNA:
   cylindricka algebraicka dekompozicia, alebo v praxi
   sum-of-squares certifikat cez semidefinitne programovanie

5. bud dostanes explicitny bod (svedok, hotovy F_K^(3)),
   alebo SOS certifikat prazdnosti pre CELY priestor v danom rade

6. ak prazdno -> rad n+1; ak prazdno pri dvoch po sebe iducich radoch
   -> obhajitelny NO_GO
```

Keď je priestor konečný, „konštruovať" a „vylúčiť" sú tá istá operácia a nedá
sa medzi nimi driftovať. Toto je jediná zmena, ktorá odstraňuje príčinu
regresu opísaného v `AGENTS.md` §4 a §4.1 naraz.

## 2. Súhrnný stav prienikov

| Koľaj | Hľadaný objekt | Behaviorálny obal | Stav fyzickej množiny | Už certifikovane vylúčené podmnožiny | Chýba do svedka |
|---|---|---|---|---|---|
| A2-K7 | pozitívna spektrálna hustota, retarded kernel a noise z jedného bath/mediátora | `BEHAVIORAL_OPEN`: požadované `Q1,Q2` sú kinematicky kompatibilné s kladnými sadzbami | `F_K7^(3): UNDETERMINED_REVIEW` | fixed-width cascade M-014a; holý Onsager cross-term M-014b; thermal gravity-only M-014d1; lokálny KMS M-014d1b; vedúci spin-2 M-014d2a | jeden lokálny kernel s požadovanou sadzbou, pasivitou, FDT/noise a platným cutoffom |
| A2-K8 | pozitívny produkčný collision kernel `C_prod[f_c]` | `NONEMPTY_WITNESS_MOMENT_CONE`; ale warm source-only prienik s presným A1 je prázdny | rodič `F_K8^(3): UNDETERMINED_REVIEW`; `K8-Fkin-WARM-A1-SOURCE-ONLY: EMPTY_CERTIFIED_SCOPE` | warm `P_c>0` + rovnaké `q,rho_c` odporuje A1; cold `Q||u_c` dedí M-009; cold `Q||u_f` dedí M-010 | iba explicitný relaxačný kernel môže prekročiť source-only triedu; spoločný production/scattering proces sa testuje ako K9 |
| A2-K9 | jeden maticový element/kernel pre produkciu aj rozptyl | `NONEMPTY_MARKOV_MOMENT_CLASS`: cold source a lineárny pasívny drag sú kompatibilné | `F_K9^(3): UNDETERMINED_REVIEW`; momentová trieda neprázdna | `K9-1TO2-EXACT-THRESHOLD-FINITE-RATE: EMPTY_CERTIFIED_SCOPE`; nezávislý `kappa` je mimo K9; `C_el=0` sa zlieva s K8/K1 | jedna akcia/interakcia odvodzujúca finite cold production, transportný pomer, fuel reakciu a noise bez druhého fitu |
| A2-K11 | lokálny ortogonálny drag `F_c^mu=Upsilon h_c^{mu nu}u_{f,nu}` | regular constitutive class neprázdna; early indicial null limit GR-like; CS2/S0 formula identities PASS | `K11-CS1: UNDETERMINED_REVIEW`; S0 state register v001 STOP po PF-062; full multispecies DAE required | staré znamienko/`gamma rho_c`; uniform regular exact-pole cure; passive interaction-block Hurwitz cure; COMP invariant shortcut | posledný versioned CS2 full base: správny `4l+9` state contract, všetky species/shear, regular basis, constraint propagátor |
| A2-K12 | párový `fuel -> c_+ + c_-` kernel plus opačná silová matica | `NONEMPTY_WITNESS_K12_K3_1_PAIR_MOMENT_CONE`: cold neutral pair moment je možný | `F_K12^(3): UNDETERMINED_REVIEW`; symmetric source-only COM cure neexistuje | K12-K1 M-016; dispersive pressureless A1; symmetric internal-force COM cure; smooth 1->2 exact-threshold finite-rate | coherent/cold finite-rate kernel, externý total momentum ledger a stabilný separation mód bez net fifth-force/fitu |

Rodičovské prieniky zatiaľ nie sú dokázane prázdne ani neprázdne. Stav
`UNDETERMINED_REVIEW` je autoritatívny: nemožno z neho odvodiť PASS G2/G3,
ale ani smrť rodiča.

## 2.1 Behaviorálny obal — čo vieme bez presnej funkcie

| Koľaj | Vstup alebo podmienka | Výstup, ktorý sa musí správať známym spôsobom | Už vylúčené správanie |
|---|---|---|---|
| K7 | dostupné palivo/bath a relatívny stav | tok má byť konečný, pasívny, kauzálny; bez bathu alebo väzby nulový | záporný Onsagerov smer; sadzba nedosiahnuteľná auditovaným thermal/KMS/spin-2 kanálom |
| K8 | lokálna zásoba paliva a otvorený produkčný kanál | počet/energia produkcie nezáporné; `q^2-|j|^2>=m_c^2S_n^2`; bez paliva alebo väzby nulové | warm source-only popol má `P_c>0` a nemôže zachovať presný pressureless A1; cold hranica sa zlieva s K1 |
| K9 | jeden spoločný mikrofyzický proces | cold produkcia dá `q=mS,P=0`; lineárny drag má `K>=0`, nulový FLRW ohrev a spoločný nulový limit | hladký 1->2 exact cold threshold nemôže mať konečnú šírku; nezávislý ľubovoľný drag nie je K9 |
| K11 | nenulová relatívna rýchlosť dvoch prítomných médií | sila pôsobí proti relatívnemu pohybu, používa redukovanú entalpiu a mizne pri rovnakej rýchlosti alebo chýbajúcom médiu | staré znamienko/`gamma rho_c`; uniformne regular drag nemôže rušiť celý Gamma/delta pól asymptoticky |
| K12 | palivo nad párovým prahom | cold pair môže niesť q s nulovým čistým nábojom a korelovaným noise; bez paliva/kanála produkcia mizne | náboje nerušia pressure; vnútorné symetrické sily nemenia COM; exact cold smooth 1->2 má nulovú šírku |

Tieto riadky sú „pozorovanie ohňa“: určujú nutné správanie bez tvrdenia,
že poznáme presnú chémiu/kernel. Pri K7/K11/K12 už zabili konkrétne
podmnožiny. Pri rodičoch ostáva obal otvorený, pretože nepoznáme všeobecný
rozpor všetkých dovolených správaní.

## 3. A2-K7 — bath/mediátor

Hľadané objekty sú spektrálna hustota `J(omega,Y)>=0`, retarded odozva
`K_R` a noise kernel `N`. Okrem spoločného obalu musia spĺňať:

Pre auditovanú kanonickú realizáciu s `rho_M=epsilon rho_F` je už zo
správania backgroundu nutné

```text
0 < epsilon < delta,
Q2 = Gamma rho_F,
Q1 = [(1-epsilon)Gamma + 3H epsilon(1-delta)] rho_F.
```

Tieto výstupné rovnosti nie sú samy v rozpore s kladnými sadzbami. Otázkou
je, či ležia v obraze jedného kauzálneho pozitívneho kernelu.

| Mantinel | Povinná hodnota/vzťah |
|---|---|
| pasivita | disipovaná energia a entropická produkcia nesmú mať záporné znamienko |
| kauzalita | `K_R(t<t')=0`; reálna a imaginárna časť rešpektujú disperznú väzbu |
| noise | `N` je pozitívna semidefinitná; pri rovnováhe je zviazaná s disipáciou, nie voľná |
| nulový bath | pri coupling/bath density `->0` platí `J,K_R,N,q->0` |
| cutoff | odozva nad EFT cutoffom nevytvára požadovanú sadzbu použitím neplatnej teórie |
| požadovaný moment | ten istý kernel reprodukuje A1 tok a jeho `delta Q`, nie iba zvolenú šírku |

Aktuálne nemáme spoločného svedka. Existujúce M-014* sú certifikáty
prázdnosti uvedených podpriestorov, nie celého K7.

## 4. A2-K8 — produkčný collision kernel

Pre lokálny on-shell kernel `C_prod(x,p)` sú nutné:

```text
S_n        = integral dPi C_prod,
Q_c^mu     = integral dPi p^mu C_prod,
Delta T_c  = druhy moment a evolucia distribucie,
Q_f^mu     = -Q_c^mu - Q_ostatne^mu.
```

Okrajové hodnoty:

- produkčná časť je nezáporná na budúcej mass shell `p^0>0`;
- `m S_n` a časový moment reprodukujú `q=Gamma rho_f` bez dvojitého
  započítania creation pressure;
- pri `Gamma->0` alebo `rho_f->0` platí `C_prod->0` a všetky jeho momenty
  vrátane shot noise zmiznú;
- všetky momenty sú konečné a ich frame vyplýva z birth distribúcie;
- pressure/anizotropný stres a noise nie sú dodatočné voľné funkcie.

Pozitívna birth miera existuje práve v momentovom kuželi

```text
q_B^2-|j_B|^2 >= m_c^2 S_n^2.
```

To je `NONEMPTY_WITNESS_MOMENT_CONE`, nie úplný `F_K8^(3)` svedok.
Prienik s presným A1 však pridá ďalší mantinel. Pre rovnaké `rho_c` a `q`
platia súčasne

```text
dot rho_c+3H rho_c=q,
dot rho_c+3H(rho_c+P_c)=q,
```

odkiaľ pri `H>0` vyplýva `P_c=0`. Pozitivita masívnej distribúcie potom
vynúti podporu `p=0`, `q=m_cS_n` a `Q_c^mu=q u_c^mu`. Preto je
`K8-Fkin-WARM-A1-SOURCE-ONLY` certifikovane prázdna. Cold source-only limit
sa mapuje na K1/M-009. Širší rodič zostáva v REVIEW iba ak obsahuje nový
účtovaný relaxačný proces; spoločný production/scattering proces sa má
testovať ako K9.

Úplný dôkaz, explicitný momentový svedok a obmedzenie staršieho auditu sú v
`A2K8/ARTIFACTS/FS_GATE_01_K8_FKIN_MOMENT_CONE_RESULT_AND_AUDIT.md`.

## 5. A2-K9 — spoločný production/scattering proces

K9 musí splniť všetky K8 mantinely a navyše:

- jeden maticový element, akcia alebo spoločný collision kernel určí
  `C_prod` aj number-conserving `C_el`;
- `integral dPi C_el=0`, ale jeho prvý moment môže byť nenulový;
- pomer elastickej relaxácie k produkcii je odvodený z couplingov, hmôt,
  fázového priestoru a distribúcií;
- spoločný coupling `->0` vypne oba procesy aj noise;
- samostatný voľný `kappa` alebo `gamma_drag` je neprípustný.

Momentový priestor nie je prázdny. Jeden positivity-preserving cold
gain–loss generátor môže mať

```text
C_c = S_n delta_uc + nu [n_c delta_uf-f_c],
S_n = Gamma rho_f/m_c,
K = nu rho_c >= 0.
```

Na FLRW je relaxačný člen nulový; na lineárnom ráde dá
`-K(v_c-v_f)` a ohrev až `O(v_rel^2)`. Konkrétny regularitný witness

```text
nu = Gamma delta rho_f/(rho_f+rho_c)
```

spĺňa spoločné nulové a hraničné limity bez nového konštantného čísla.
Dokazuje iba `NONEMPTY_MARKOV_MOMENT_CLASS`: zvolený pomer `K/S_n` ešte
nebol odvodený z jednej bunkovej/QFT interakcie a nesmie sa fitovať na dáta.

Plná K9 brána vyžaduje jednu akciu alebo maticový element, z ktorého sa
nezávisle vypočíta number-changing sadzba aj transportný moment, vrátane
fuel reakcie, detailed balance/afinity a noise. Ak svedok dá `C_el=0`, patrí
do K8/K1. Ak vyžaduje nezávislý post-data `kappa`, leží mimo `X_K9`.

Bežná podtrieda `K9-1TO2-EXACT-THRESHOLD-FINITE-RATE` je certifikovane
prázdna: exact cold dvojtelesový prah má nulový fázový priestor a nad prahom
vzniká warm tlak. Coherent/kolektívne kanály tým nie sú vylúčené; tvoria
cieľ `K9-CTLR` a potrebujú vlastný mikrofyzický ledger. Úplný výsledok je v
`A2K9/ARTIFACTS/FS_GATE_01_K9_SHARED_PRODUCTION_SCATTERING_RESULT_AND_AUDIT.md`.

## 6. A2-K11 — čistý ortogonálny momentum drag

Pri tlmiacej konvencii musí kandidát spĺňať

```text
u_c,mu F_c^mu=0,
F_f^mu=-F_c^mu,
F_c^mu=0 na presnom FLRW backgrounde,
Upsilon>=0.
```

Okrajové hodnoty regularity sú rozhodujúce:

```text
Upsilon -> 0             pre rho_c -> 0 alebo rho_f -> 0,
Upsilon/(delta rho_f)    zostava konecne pre delta rho_f -> 0,
Upsilon -> 0             pri nulovom spolocnom scatter coupling.
```

Explicitný neprázdny konštitutívny svedok je

```text
h_f=delta rho_f,
mu_h=rho_c h_f/(rho_c+h_f),
Upsilon_R=Gamma mu_h.
```

Obe akceleračné sadzby sú najviac `Gamma`; relatívny mód má presne exponent
`-Gamma` a `dot E_rel=-Upsilon_R|v_c-v_f|^2<=0`. Onsagerova matica
`Upsilon_R[[1,-1],[-1,1]]` je PSD a pripúšťa momentum-conserving noise.
To dokazuje `NONEMPTY_WITNESS_K11_R_CONSTITUTIVE_CLASS`, nie mikrofyzický
`F_K11^(3)` svedok.

`Upsilon=gamma rho_c` z pôvodného návrhu zostáva mŕtvy, pretože jeho
reakcia na palivo diverguje. Navyše uniformne regular `nu_drag=O(Gamma)`
nemôže pre všetky malé `delta` zrušiť vedúci M-009 pól
`nu=O(Gamma/delta)`. Podtrieda
`K11-R-UNIFORM-REGULAR-EXACT-POLE-CANCELLATION` je preto certifikovane
prázdna. Pri pevnom `delta=0.02297` to ešte nie je smrť K11: treba odvodiť
`gamma_*(Y)` a následne analyticky preveriť úplnú rýchlostnú maticu bez
post-data fitu. Úplný výsledok je v
`A2K11/ARTIFACTS/FS_GATE_01_K11_R_REGULAR_ORTHOGONAL_DRAG_RESULT_AND_AUDIT.md`.

Presnejší interaction-only audit dáva

```text
M=[[-A_c,A_c],[-G+A_f,2G-A_f]],
G=Gamma/delta,
A_c=Upsilon/rho_c,
A_f=Upsilon/(delta rho_f),
det M=-A_c G<0.
```

Pre každý pasívny drag teda ostáva jeden kladný interaction eigenvalue;
`K11-R-PASSIVE-INTERACTION-BLOCK-HURWITZ-CURE` je certifikovane prázdna.
Celá K11 tým ešte neumiera, pretože tento velocity blok nie je pri `H!=0`
uzavretý voči density, pressure a metric premenným. Ďalšia brána musí byť
úplný constrained superhorizontový symbol, nie ladenie samostatného
`gamma_*` v starej ODE.

K11-CS1 tento symbol odvodila po úroveň presného dark bloku a Einsteinovej
constraintovej plochy. Zistila však, že fyzický reálny background vyžaduje
baryóny, fotóny, neutrína, paru a scaled free-streaming shear; dark-only
`5x5` truncation nie je dokázaná invariantná.

Pre `N=ln a`, `W_A=mathcal H V_A` platia holdouty

```text
Phi_N+Psi=(3/2)sum Omega_A(1+w_A)W_A,
sum Omega_A delta_A
 +3sum Omega_A(1+w_A)W_A
 +(2/3)(k/mathcal H)^2Phi=0.
```

Pri finite proper-time `Gamma,gamma_*` je v radiačnej ére
`Gamma/H,gamma_*/H=O(a^2)`. Leading indicial symbol je preto GR-like a
prešiel `PASS_EARLY_INDICIAL_NULL_LIMIT`; M-009 je konečná/neskorá
amplifikácia, nie nový primordial leading exponent. Fixed-`delta` full
stabilita zostáva `UNDETERMINED_REVIEW`.

Povolený je už iba jeden K11-CS2 multi-species DAE/base a jeden ohraničený
propagátor. Bez neho sa K11 nesmie
ďalej vetviť ani dostať body.

CS2/S0 potvrdila exact K11/A1/CAMB formula identity. Neskorší PF-062 však
zrušil state-register časť: scalar CAMB E-mode reťazec začína pri `E_2`,
zatiaľ čo v001 pridal `E_0,E_1`; správny count je `4*lmax+9`, nie
`4*lmax+11`. V001 base je zmrazená ako formula-regression/STOP-state dôkaz.
Stav zostáva `10/100 = G1 / REVIEW`; full v002 musí mať presnú state-set
parity kontrolu. Neskoršie pravidlo cap `10` ho eviduje ako novú úplnú
technickú architektúru `ARCH-A` na `0/10`. Historické incidenty S0-v001
`PF-061/PF-062` sa nemažú, ale nie sú fyzikálnymi pokusmi a K11 nezabíjajú.

CS2-COMP navyše exaktným analytickým auditom vylúčila skratku cez izolovaný
kompenzovaný dark mód. Exact reaction zachová `D_rho=D_Pi=0`, ale

```text
(delta p_f)'=rho_f B V_f Xi_p,
Xi_p -> -2mathcal H-A_f(1+s)<0
```

v skorom radiačnom limite pre každý pasívny `A_f>=0`. Tlak preto budí
metriku a štandardné species. Scoped prázdna trieda nemení rodičovský REVIEW;
potvrdzuje nutnosť full DAE.

## 7. A2-K12 — párová produkcia a opačné náboje

Kandidát obsahuje `C_+(x,p_+)`, `C_-(x,p_-)` a silovú akciu s
`beta_+=-beta_-`. Musí platiť:

```text
Q_+^mu + Q_-^mu + Q_f^mu + Q_phi^mu = 0,
Q_+^0 + Q_-^0 = q = Gamma rho_f              (FLRW),
```

spolu s:

- pozitívnymi on-shell birth distribúciami a lokálnym prahom páru;
- odvodenou koreláciou hybností a pozitívnou noise kovarianciou;
- `Gamma->0` alebo `rho_f->0`: oba produkčné kernely a shot noise `->0`;
- `beta->0`: čistá párová produkcia zostane, opačná sila zmizne;
- regulárnym center-of-mass aj separačným módom;
- silovou/kinetickou maticou bez ghosta, gradientového alebo segregation
  runaway na G5–G6.

K12-K1 je už prázdna podmnožina pre požiadavku nenulového A1 toku:
`epsilon=0` bez production kernelu dá `Q_total=0`. K12-K2/K3 tým nie sú
zabité.

K12-K3.1 má neprázdny cold momentový kužeľ. Pre equal-mass pár

```text
S_pair=q/(2m),
Q_+^mu=Q_-^mu=(q/2)u_c^mu
```

dáva pozitívne on-shell miery, nulový čistý náboj, presnú fuel reakciu a
pair number noise `S_pair[[1,1],[1,1]]`, ktorý je PSD a nemá charge-noise
vlastný mód.

Tri užšie prieniky sú však certifikovane prázdne:

1. `K12-K3.1-DISPERSIVE-PRESSURELESS-A1`: `P_+,P_->=0`, takže opačné
   náboje ani counter-stream momentá nezrušia total pressure;
2. `K12-K3.1-SYMMETRIC-INTERNAL-FORCE-COM-CURE`: `F_++F_-=0`, preto
   vnútorná sila priamo nemení total COM/fuel blok, ktorý zostáva K1-like;
3. `K12-K3.1-1TO2-EXACT-THRESHOLD-FINITE-RATE`: hladký regulárny
   dvojtelesový rozpad má na exact cold prahu nulový fázový priestor.

Coherent/kolektívna produkcia alebo asymetria tým nie sú vylúčené. Musia
však odvodiť nový total momentum/field ledger, korelovaný noise a stabilný
separation mód; inak K12 nepridáva cestu z M-009. Úplný výsledok je v
`A2K12/ARTIFACTS/FS_GATE_01_K12_K3_1_PAIR_PRODUCTION_MOMENT_RESULT_AND_AUDIT.md`.

## 8. Ďalší pracovný postup (R2, 2026-08-14)

Pôvodné poradie bolo: (1) doplniť tvar mantinelov, (2) hľadať analytické
rozpory, (3) až potom konštruovať explicitného svedka. Audit 2, V.4 ukázal,
prečo nekonvergovalo: **bod 2 sa vetví rýchlejšie, než sa uzatvára**, takže
P5.3 sa k bodu 3 nikdy nedostal. Poradie je preto obrátené.

```text
1. FS-C13: zafixuj derivacny rad a napis konecnorozmerny koeficientovy
   priestor (§1.2). BEZ TOHTO SA CONTRACT NEOTVARA.

2. HRUBY_KANDIDAT_FIRST: postav najhrubsieho mozneho explicitneho kandidata
   -- aj vymysleneho, aj zleho -- a prezen ho cez FS-C2..C13.
   Zlyhanie povie, ktore mantinele su aktivne. To je viac informacie nez
   dalsie zjemnenie specifikacie.

3. az potom hladaj analyticke rozpory, a to UZ V KONECNOM priestore
   (SOS / CAD, nie po podtriedach).

4. vysledok je bud explicitny svedok F_K^(3), alebo SOS certifikat
   prazdnosti pre CELY priestor v danom rade.

5. neuspech jedneho svedka vytvori mrtvu dceru, nie automaticky mrtveho
   rodica.

6. rodic zomrie po EMPTY_CERTIFIED_SCOPE pre cely KONECNY rez X_K pri
   dvoch po sebe iducich derivacnych radoch.
```

**Zmena bodu 6 je vecná.** Pôvodné znenie („celý vopred definovaný priestor
`X_K`") bolo formálne nesplniteľné, keď je `X_K` priestor funkcií. Doklad:
K7 má päť zabitých podtried a je `UNDETERMINED_REVIEW`; K11 má štyri a je
`UNDETERMINED_REVIEW`. Podmienka smrti bola nesplniteľná, teda `§8` nemohol
skončiť ani v jednom smere.

**Hľadá sa raz, nie päťkrát.** Podľa `00_TRACK_REGISTER.md` je hľadaný objekt
pre K4, K7, K8, K9, K11 aj K12 ten istý — lokálny operátor produkcie a
transportu. Konečný rez sa preto robí **jeden** a jeho výsledok platí pre
všetkých šesť. Rozdelenie na päť trati s vlastnými adresármi násobí režijné
náklady bez pridania šance.

**Odhad:** tri až šesť týždňov práce; ukončí `P5.3` v oboch smeroch.

Predpokladom je rozhodnutie stanice `A0`. Kým `A0` nie je rozhodnutá, tento
postup sa **nespúšťa** — ak `A0` padne, je celý priestor `X_K` bezpredmetný,
lebo substrát, na ktorom má operátor žiť, neexistuje.
