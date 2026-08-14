# A1-K1 -> A2-K4 — živá mapa progresu a prechodu na A3

**Aktualizované:** 2026-08-14  
**Autoritatívny stav:** `A1-K1 LIVE / CONDITIONED / PRE_A0`; `A2-K4 LIVE / FROZEN_PENDING_A0 / 60/100`  
**Aktívna cesta:** žiadna v `A2` — aktívna je stanica `A0` (`tracks/A0/00_STATION.md`)  
**Aktívny blocker:** `A0_UNDECIDED` (upstream). Starý blocker `N1+N2+N3` zostáva zaznamenaný, ale je zmrazený a **nesmie sa zjemňovať**  
**RUN_AUTHORIZED:** `false`  
**Nahrádza:** zastaranú živú mapu z 2026-07-18 s blockerom `KMPC-036`; jej
vedecké artefakty a história sa nemažú.

## 1. Identifikátory a význam skóre

- `A0`, `A1`, `A2`, `A3` sú kontrolné stanice (*verification stations*).
  `A0` bola zavedená 2026-08-14 a je **upstream od `A1`**; do jej rozhodnutia
  sú `A2` aj `A3` zmrazené.
- `K1`, `K4`, ... sú koľaje (*tracks*) v rámci úplnej route.
- `S1` sa nepoužíva ako náhrada A1, pretože už označuje
  `S1_LOCAL_CORRECTABLE_SAME_TRACK` auditný nález.
- `T1` sa nepoužíva ako náhrada K, pretože už označuje
  `T1_TECHNICAL_NO_CLAIM_REACH`.
- `60/100` je súčet váh fyzicky prejdených brán, nie percento pravdivosti.
  Historická technická hĺbka redukovaného K7 runnera `66.5/100` nie je
  prenositeľná do fyzikálneho skóre.

## 2. Mapa prijatého progresu

| Míľnik | Čo prešlo | Reprezentatívny vzorec/výsledok | Stav po míľniku | Dôkaz |
|---|---|---|---|---|
| `A1-K1 background` | backgroundový zdrojový ledger paliva a popola zachováva celkovú energiu FLRW pozadia | `rho_f'=-3delta rho_f-lambda(H0/H)rho_f`; `rho_c'=-3rho_c+lambda(H0/H)rho_f` | `A1-K1 LIVE / CONDITIONED`; úplný `Q_A^mu` nie je odvodený | `Questions/A1_rozhodnutie_Q19_a_kovariantny_background_v3.18.md` |
| `A1-K1 K-N2` | odstránenie neprípustnej módovej závislosti backgroundu | `Phi(k)=A_f[H0 sqrt(Omega_r0)/k]^p`, `Phi z^p=A_f a^p` | univerzálny background kandidát; `A_f` zostáva podmienené | `scripts/234_script_KMPC_001_A1_frozen_background_Af_audit.py`; package `EA-20260717-004` |
| `A2-K4 identity` | energy-frame prenos popola a paliva | `(rho_c+delta rho_f)theta_d=rho_c theta_c+delta rho_f theta_f`; `Q_f^mu=-Q_c^mu=-Gamma rho_f u_d^mu` | otvorená K4 koľaj | `SUBTRACKS/P5/00_WORK_PLAN.md` |
| `M-011 erratum` | stará „explózia“ bola relatívny gain voči skoro nulovej referencii | `ln T_K4=0.462<1` | stará smrť zrušená; bez automatického PASS | `Audit/ERRATUM_M011_K4_REFERENCE_GAIN_VS_ABSOLUTE_TRANSFER.md` |
| `K4.1` | tri regulárne superhorizontové módy, constraint a nezávislý integrátor | `p^3(p+2)^2(p+3)[p^2+(5-3delta)p+12-6delta]` | historický checkpoint `55/100`; kanonicky G5=`50/100` | scripts `66`, `67`; audit `A2_K4_1_UPLNA_REGULARNA_CONSTRAINT_BAZA_A_ROZSUDOK.md` |
| `K4.2` | principal-symbol high-`k` stabilita v deklarovanom effective scope | `mu^4(mu^2+1)(mu^2+1/3)` | historický checkpoint `59/100`; po rekalibrácii G6=`60/100` | scripts `69`–`71`; audit `A2_K4_2_HIGH_K_SUBHORIZONTOVY_AUDIT_A_ROZSUDOK.md` |
| `K4.3a` | oddelené species, anisotropický stress, Thomsonova kancelácia a nulový limit | presné algebraické nulové rezíduá | zachovala `60/100` bez zmeny skóre | script `72`; audit `A2_K4_3A_SPECIES_LEDGER_ANISOTROPIC_STRESS_AND_NULL_AUDIT.md` |
| `P5.1` | exact-A1 background a povinné species v general-synchronous ledgeri | `U_d=(1-beta)U_c+beta U_f` | `PASS` v statickom scope | script `236` a jeho raw/audit |
| `P5.2` | úplné deklarované Einsteinove constraint štruktúry a nulové limity | `R_00=R_0i=R_tr=R_tl=0` | `STRUCTURAL_PASS`; nie dynamika | script `241`; `P5_2_CONSTRAINT_LEDGER/01_RESULT_SK.md` |
| `P5.3 C2` | register 10/10 seed atómov | `coverage=10/10` | coverage PASS, nie fyzický witness | script `371`; package `EA-20260719-029` |
| `P5.3 C3` | 45/45 logických kontrol | `logical_coverage=45/45` | logical PASS; externý T2 `AGREE_IN_SCOPE` | script `392`; package `EA-20260722-039` |
| `P5.3 D1-D2SW10` | v prijatých corrected successors: Landauova regulárna doména, projektory, traction/current/divergence identity, rank/nullity a podmienené rozsahy | `A_Q` vedie complete quotient family, `A_X` sourced admissible whole-map family a `A_K={(Q,X,ker X)}` až potom rozlišuje PK1/I0; nejde o celý global-operator existence test | `10 WAITING / 0 EXCLUDED`; karantenizované reaches sú vylúčené; bez zmeny 60/100 | `HISTORY/00_EVENT_LEDGER.md` + exclusions v `tracks/00_CURRENT_EXECUTION_PLAN.md` |

## 3. Čomu sa dnes dá veriť

### Prijaté v presnom scope

1. A1 konzervačné backgroundové rovnice a ich homogénny nulový ledger.
2. Povinnosť odstrániť Fourierovo `k` z globálneho backgroundu a K-N2
   transformácia amplitúdy pri zmrazených A1 vstupoch.
3. Definícia A2-K4 energy-frame koľaje.
4. Tri regulárne superhorizontové módy v perfect-radiation scope.
5. High-`k` principal-symbol výsledok v deklarovanom efektívnom scope.
6. Statický species/constraint ledger P5.1-P5.2.
7. C2/C3 pokrytie a logická úplnosť iba ako registre kontrol.
8. Presné analytické hranice D1-D2SW10, ak sa nepoužijú karantenizované
   tvrdenia uvedené v živom pláne a event ledgeri.

### Neprijaté

- mikroskopický pôvod `A_f` alebo čísla `0.05`;
- úplný lokálny produkčno-transportný zákon;
- existencia fyzického seedu iba z C2/C3 coverage;
- dynamické zachovanie constraintov;
- plná fotónová/neutrínová hierarchia;
- CMB-normalizované `H0`, `sigma8` alebo `S8`;
- vstup do A3;
- **(nové 2026-08-14)** existencia Lorentzovsky invariantného kontinuálneho
  limitu substrátu stabilného voči radiačným korekciám — stanica `A0`.

### 3.1 Odstránenie rozporu s publikovanými survival targets (2026-08-14)

Externý audit 2, V.10, správne zistil jediné miesto, kde je proces v rozpore
sám so sebou: zoznam **Neprijaté** vyššie uvádza *„CMB-normalizované `H0`,
`sigma8` alebo `S8`"*, zatiaľ čo publikovaný release v3.18 uvádza
`H0 ≈ 66.4 ± 0.4` a `S8 ≈ 0.86–0.87` v tabuľke *„Value or physical
condition"* ako survival targets. Obe strany sú naše vlastné dokumenty, takže
je to najzraniteľnejšie miesto voči externému čitateľovi. K tomu `FS-C12`:
observačné filtre sa smú aplikovať až na fyzikálne neprázdnu množinu, a
neprázdna nie je.

**Rozhodnutie: platí interný stav.** Nasledujúce predikcie sa preklasifikujú:

| ID | Starý status | Nový status | Dôvod |
|---|---|---|---|
| `P01` | survival target | `PRE_A3_DIAGNOSTIC / NOT_A_TARGET` | A3-typové číslo pred autorizáciou A3 |
| `P04` (`H0`) | survival target | `PRE_A3_DIAGNOSTIC / NOT_A_TARGET` | to isté; navyše nie je θ\*-kalibrované (audit II.5) |
| `P05` (`S8`) | survival target | `PRE_A3_DIAGNOSTIC / NOT_A_TARGET` | to isté |
| `P06` | survival target | `PRE_A3_DIAGNOSTIC / NOT_A_TARGET` | „neither a new fit nor a posterior" — vlastný text |
| `P11` (steam) | merateľná predikcia | `PRE_A3_DIAGNOSTIC` + povinná dichotómia FIRAS/gravitóny | pri 0.905 K je EM-viazaný steam vylúčený o 3–4 rády, gravitónový je nedetegovateľný (audit II.7, overené: 17.8 % / 9.8 % / 2.4 % pri 30 / 53 / 100 GHz) |
| `P10` (párnosť `λ̂`) | predikcia so *survival boundary* a *death scope* | **`IDENTITY / NOT_A_PREDICTION`** | párnosť vyplýva z toho, že kosínus je párny a neorientovaný graf obsahuje `Δ` aj `−Δ`; platí pre akýkoľvek reálny symetrický grafový Laplacián. Žiadne meranie ju nemôže vyvrátiť |
| `P02` (`n_s`) | predikcia | predikcia + **povinná poznámka o degenerácii s α** | s voľným `α` v `n_s = 1 − αδ` sedí každé `C`; `C = 28 → α = 1.528`, `C = 106.75 → α = 4.292`. Zhoda je dvojparametrická koincidencia |

**Dôsledok, ktorý je vo váš prospech.** Ak sú `P04`/`P05` interne neprijaté,
potom falzifikácia z auditu II.3 (`S8 ≈ 0.87` na ~3.8σ nad KiDS-Legacy aj
Planckom) **nezasahuje teóriu** — zasahuje iba ten zamrznutý anchor výpočet.
Platí to však len ak sa čísla z release-u stiahnu. Kým tam stoja ako survival
targets, II.3 na ne platí.

**Pozitívny nález k `P10`, ktorý sa nevyužíva.** Keďže párnosť vyplýva
z neorientovanosti, je absencia lineárneho člena v tejto konštrukcii
**generická**, nie šťastná náhoda v jednom sektore. Lineárny člen je pritom
najsilnejšie obmedzovaný (`E_QG,1 > 7.6 E_Pl`). To je skutočná vlastnosť
konštrukcie a treba ju sformulovať korektne — ako vlastnosť, nie ako predikciu.

### 3.2 Upstream zmrazenie (2026-08-14)

`A2-K4` je od tohto dátumu `FROZEN_PENDING_A0`. Blocker `P5.3` sa **nesmie
ďalej zjemňovať** (`AGENTS.md` §4.1, `HRUBÝ_KANDIDÁT_FIRST`). Nasledujúci
zákonný krok v `A2` nie je task 634; je to buď rozhodnutie `A0`, alebo — po
`A0_PASS` — jeden konečný rez `X_K` podľa `FS-C13`.

Diagnóza, ktorá k tomu viedla (audit 2, V.3–V.5), stojí za zaznamenanie:

```text
16.7.2026 -> 13.8.2026
  vnorene podkolaje  D2SW0 ... D2SW16      17 urovni
  tasky              task411 -> task633    222 cisel
  KMPC runnery       KMPC-003 -> KMPC-046   44 runnerov
  fyzikalna hlbka    60/100 -> 60/100       ZMENA: NULA
  P5                 3.5/6  -> 3.5/6        ZMENA: NULA
  D2SW15 CR1a        0 certified / 4 waiting / 0 excluded
  kategorialne nalezy agentovej auditnej vrstvy   NULA
```

Nie je to zlyhanie úsilia ani disciplíny. Je to očakávaný výstup správnej
metódy pustenej na nekonečnodimenzionálny priestor bez konečného rezu, a od
`AGENTS.md` §11 vieme aj to, prečo sa ten rez nikdy nezaviedol sám.

## 4. Aktuálny blocker P5.3

Whole-map diskriminačná otázka je

```text
A_Q(Z) = complete overlap-resolved quotient family
A_X(Z,Q) = sourced admissible whole-map family
A_K(Z) = {(Q,X,ker X) : Q in A_Q(Z), X in A_X(Z,Q)}.
```

Na jej rozhodnutie musí jeden spoločný, provenienčne uzavretý packet obsahovať:

1. `N1`: complete overlap-resolved physical quotient `Q_Z` alebo dokázane
   neprázdnu úplnú `A_Q(Z)`;
2. `N2`: sourced actual whole map `X_Z` alebo dokázane neprázdnu P1–P2 úplnú
   `A_X(Z,Q)` so všetkými prijatými guardmi;
3. `N3`: až potom klasifikáciu `ker X={0}` verzus nenulový fyzický kernel
   witness, prípadne univerzálnu alebo mixed klasifikáciu kompletnej rodiny;
   `W1-W4` smie nahradiť direct whole-map test iba po úplnom overlap a
   image-independence dôkaze.

Sektorové výpočty samy nestačia, pretože nulové smery sa môžu rušiť medzi
sektormi. Každý kernel obsahuje nulu, takže jeho samotná neprázdnosť nie je
test. Nenulový fyzický kernel witness vylučuje iba presný `PK1/I0` scope;
injektivita povoľuje neskoršie brány a mixed family zostáva waiting. Ani jedna
vetva sama nedokazuje jeden globálny local-natural zákon alebo celý A2-K4.
Súčasný výsledok preto nezakladá witness ani no-go. Koľaj je živá a čaká na
fyzický vstup/exaktnú vetu; Python ani official run nie sú autorizované.

## 5. Povinná cesta do A3

### L1 — uzavrieť P5.3 fyziku

- rozhodnúť N1-N3 v prijatom poradí bez kernel inference pred complete
  quotientom a sourced whole mapou;
- po per-state `PK1/I0` diskriminácii uzavrieť pevný residual,
  owner/power/reservoir a preukázať jeden globálny local-natural bridge alebo
  scoped no-go;
- uzavrieť source/current/owner/power/reservoir ledger;
- odvodiť globálny `K_bridge` bez kruhovej definície, skrytého poľa alebo
  dodatočného fitu.

### L2 — P5.4 species-first dynamika

- úplné kontinuity a Eulerove rovnice pre všetky zložky;
- dynamické Einsteinove constrainty a konzervácia;
- linearita/amplitúdové škálovanie;
- aspoň dva nezávislé štarty;
- kroková, tolerančná a metódová konvergencia.

### L3 — plná Einsteinova–Boltzmannova hierarchia

- fotónové a neutrínové multipóly;
- anisotropický stress a Thomsonov coupling;
- exact-A1 background adapter bez `k`-úniku;
- `lmax` a metódová konvergencia;
- štandardný nulový limit.

### L4 — zmrazený route-local A2 observačný passport

- zmraziť fyziku a vstupy pred porovnaním s dátami;
- uzavrieť route-local transferové a observačné rozhranie pripravené na
  nezávislú implementáciu;
- výsledok nesmie spätne meniť operátor, počiatočný mód, drag, opacity ani
  amplitúdu bez otvorenia novej koľaje alebo autorovho rozhodnutia.

### L5 — vstupná kontrola a nezávislá reprodukcia A3 (`M1-M6`)

| A3 míľnik | Povinnosť |
|---|---|
| `M1` | presná verzia CLASS/CAMB, commit, patch, konfigurácia, jednotky a vstupy |
| `M2` | nulový limit reprodukuje štandardný background, `C_l` a `P(k)` |
| `M3` | implementovaný je celý prijatý A2 operátor, nie iba background alebo rastová skratka |
| `M4` | numerická konvergencia, runtime hranice a checkpointy |
| `M5` | fyzikálna interpretácia bez post-data ad-hoc záchrany |
| `M6` | reprodukovateľné transfery a CMB-normalizované `sigma8/S8` a `H0` |

A3 otvorí iba hlavný orchestrátor po prijatí úplnej A2 brány. A3 nie je
ďalšie percento za veľký kódový beh; je to nová kontrolná stanica. V
zmrazenej verzii CLASS/CAMB má nezávisle implementovať a reprodukovať celý
prijatý A2 operátor a až potom vytvoriť CMB-normalizované observably; nesmie
spätne meniť A2 fyziku.

## 6. Namespace G-brán

Historický jemný register používa `C7-G8` pre plnú hierarchiu a `C7-G9` pre
downstream CMB/`S8`. Globálny A2/A3 passport môže označovať plnú
Einsteinovu–Boltzmannovu dynamiku ako G7, CMB normalizáciu ako G8 a likelihood
ako G9. Preto sa v rozhodnutí vždy uvádza úplný prefix; holé `G8` je
nejednoznačné.

## 7. Pravidlo aktualizácie

Mapa sa mení iba po autoritatívnom výsledku alebo po zmene blockeru. Každá
zmena uvedie dátum, presný artefakt, scope, starý a nový stav a dôvod.
Technická chyba nemení fyzikálny verdikt. Historické dôkazy a mŕtve koľaje sa
nemažú; karantenizované tvrdenia sa nesmú citovať ako prijaté.

## 8. R21 auditná korekcia P5.3

Externý whole-document audit správne upozornil, že každé lineárne jadro
obsahuje nulu a jeho samotná neprázdnosť preto nemôže byť existenčným testom.
Prvý preseal návrh opravy s nezdrojovaným `X_Z(z)=b` bol následným nezávislým
auditom zablokovaný a nikdy sa nestal prijatou route sémantikou.

Autoritatívna R21-R2 oprava zachováva presný event-ledger contract:

```text
A_Q(Z) -> A_X(Z,Q) -> A_K(Z)={(Q,X,ker X)}.
```

Bez complete `Q` a sourced actual `X` alebo proved-nonempty P1-P2 complete
family nie je dovolená kernel inference. Nenulový fyzický kernel witness
vylučuje iba `PK1/I0`; injektivita iba otvorí `E_N`; mixed family zostáva
`WAITING`. Ani jedna vetva nie je global-operator witness ani celý A2-K4
verdict. Nezávislé R21-R2 matematické a fyzikálne audity odporučili PASS bez
zvyškového S1+. Stav ostáva `A2-K4 LIVE_ACTIVE / 60/100`, `P5.3 LIVE /
WAITING`, A3 blokovaná.
