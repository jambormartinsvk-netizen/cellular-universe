# Vyhodnotenie externých auditov 00 a 01 hlavným orchestrátorom

**Balík:** `EA-20260717-001-KMPC-BACKGROUND-LINEAGE`  
**Dátum:** 2026-07-17  
**Rozhodovacia autorita:** hlavný orchestrátor  
**Výsledok spracovania:** `ACCEPTED_WITH_LIMITATIONS`  
**Dopad na koľaj:** bez nového `PASS/REVIEW/STOP`, bez zmeny skóre alebo
hĺbky A2-K4. Audit potvrdzuje a spresňuje existujúci scope; nie je novou
fyzikálnou bránou.

## 1. Čo bolo porovnané

1. `00_AUDITOR_AUDIT.md`: auditor poznal iba zapečatený balík.
2. `01_AUDITOR_AUDIT_ADDENDUM_BIG_PICTURE.md`: auditor navyše čítal v3.17,
   ale dodatočný korpus nebol priložený s manifestom a hashmi.
3. Hlavný orchestrátor urobil read-only kontrolu proti primárnym lokálnym
   artefaktom:
   - `scripts/213_script_A2_K4_C7_7c_K7d_integrated_G4_G6_G7_runner.py`,
     najmä riadky 64–68 a 112–123;
   - `scripts/128_script_A2_K4_3b_RG_BR3B2g_exact_order_and_hierarchy_audit.py`;
   - `RUN_FULL_002_BACKGROUND_UNIVERSALITY_RESULT.json`;
   - `Independent_Audits/K_MPC_0_05/06...` a `08...`;
   - zmrazený `Old/09_script_K3_cosmology_pipeline.py` a aktuálny
     `scripts/09_script_K3_cosmology_pipeline.py`;
   - skorší projektový audit z 2026-07-13.

Nebola spustená nová fyzikálna alebo Python kalkulácia.

## 2. Celkové hodnotenie prínosu

| Posudok | Silná stránka | Hlavné obmedzenie | Hodnotenie použiteľnosti |
|---|---|---|---|
| `00` — iba balík | disciplinované oddelenie implementácie, mapovania amplitúdy a pôvodu `A_f`; dobré rozmerové a symbolové pripomienky | chýbali primárne skripty a raw RUN-FULL-002, preto auditor nemohol sám potvrdiť citované riadky ani reprodukovať výpočet | vysoká hodnota ako `PASS_MAPY`; nie samostatný `FORMULA/COMPUTATION PASS` |
| `01` — s v3.17 | ukázal vzťah chyby ku registrovanému backgroundu, spresnil závislosť `A_f` od `lambda`, upozornil na verziu dátovej kotvy | dodatočný korpus nebol zapečatený ani presne identifikovaný; niektoré formulácie sú širšie než skontrolovaný scope | hodnotný kontextový audit, ale dôkazovo `UNSEALED_CONTEXT_REVIEW` |

Auditor teda **pomohol**. Najväčšia hodnota nebola v novom verdikte, ale v
odhalení medzier, ktoré by pri ďalšom prenose do CLASS/CAMB mohli znovu
vyrobiť rovnakú chybu: jednotky, parameter provenance, verzie dát a chýbajúce
primárne artefakty.

## 3. Tvrdenia, ktoré hlavný orchestrátor prijíma

### 3.1 Historická fixed-`K_MPC` implementácia bola chybná pre background

Primárny skript 213 skutočne obsahuje:

```text
HUBBLE0_MPC = 100*h/c
K_MPC = 0.05
z = K_MPC*a/(HUBBLE0_MPC*sqrt(Omega_r0))
fuel_piece = z**p
denominator = 1 + MU*z + fuel_piece*(1 + TRANSFER_SHAPE*z**2)
```

Raw RUN-FULL-002 zároveň obsahuje symbolický nenulový
`d(fuel)/dk` a verdikt `STOP_BACKGROUND_K_DEPENDENCE_UNRESOLVED`.
Externý záver je preto vecne správny: starý denominator nesmie byť globálny
FLRW background.

Presná korekcia dôkazového výroku: auditor 00 to z balíka overil iba cez
sekundárne mapy. **Hlavný orchestrátor** následne potvrdil zhodu mapy s
primárnym skriptom a raw výsledkom. Až kombinovaný záznam podporuje
`COMPUTED_STOP_SCOPE` historickej implementácie.

### 3.2 Mapovanie amplitúdy ruší Fourierovo `k` v ranom rade

Ak je vedúci homogénny koeficient definovaný ako

```text
rho_f/rho_r = A_f a^p + ...,
```

potom porovnanie s `Phi(k) z^p` vynúti

```text
Phi(k) = A_f (H0 sqrt(Omega_r0)/k)^p.
```

Auditor správne overil zrušenie mocnín `k` v deklarovaných fuel/ash členoch.
Toto je algebraický výsledok pre príslušný skorý rad. Nie je to dôkaz, že
celý presný background má pre každé `a` tvar jednej mocniny `A_f a^p`.

### 3.3 `A_f` nie je nový nezávislý fit, ale ani parameter z prvých princípov

Prijíma sa spresnenie:

```text
A_f = A_f(lambda, delta, DeltaN_eff, theta-star/flat-closure inputs).
```

Číslo `7809.270101963506` je výsledkom konkrétneho zmrazeného A1 pracovného
bodu. Musí niesť minimálne hodnotu `lambda`, hash runu, jednotkový výrok
„bezrozmerné“ a poznámku, že mikrofyzikálny pôvod closure je otvorený.

### 3.4 Jednotková pripomienka je správna a dôležitá

Necelá mocnina `z^p` vyžaduje bezrozmerné `z`. Primárny skript používa
`HUBBLE0_MPC = 100*h/c`, teda `H0/c` v `Mpc^-1`, ale balík túto konvenciu
neukázal. Budúci formula ledger musí deklarovať:

```text
k [Mpc^-1], H0/c [Mpc^-1], a [1], z [1].
```

### 3.5 Rozdiel dátového bodu `S8` v registrovanom skripte existuje

Zmrazený `Old/09...` používa `0.759 +/- 0.024`; aktuálny `scripts/09...`
používa `0.815 +/- 0.019`. Tento šev už bol autoritatívne zaznamenaný v
`Audit/fyzikalny_audit_bunkoveho_priestoru_2026-07-13.md`, riadky 370–378,
a v `Questions/otazky_a_navrh_krokov_v3.18.md`.

Preto nejde o nový projektový nález N-7, ale o **hodnotnú nezávislú
reprodukciu už známeho nálezu**. Potvrdzuje potrebu changelogu v3.18.

## 4. Tvrdenia, ktoré sa prijímajú iba s obmedzením

| Tvrdenie auditora | Korektné ohraničenie |
|---|---|
| „Prenos je preukázaný výpočtom“ v audite 00 | samotný auditor 00 nemal výpočet ani primárny kód; preukázal konzistenciu sekundárnej mapy. Computed status potvrdzuje až následná kontrola primárnych artefaktov hlavným orchestrátorom. |
| „Mapovanie je matematicky nutné“ | nutné pre vedúci homogénny koeficient zvoleného raného radu za premisy univerzálneho FLRW backgroundu; nie jediné možné mikrofyzikálne riešenie celého palivového sektora. |
| „Registrácia v3.17 je čistá“ | prijateľné iba ako: v kontrolovanom v3.17 backgroundovom skripte nebol nájdený fixed-`K_MPC` únik. Nie je to všeobecný certifikát všetkých predikcií v3.17; samotný `S8` version seam to vylučuje. |
| „K-N1 je a priori silne znevýhodnená hierarchiou ~58 rádov“ | správny order-of-magnitude varovný test iba pri priamej identifikácii inverse Planck cell scale s korelačnou škálou. Emergentná kolektívna korelačná dĺžka môže byť oveľa väčšia; bez mechanizmu však K-N1 nesie dôkazové bremeno. |
| „Dodatočný audit posilňuje verdikty“ | obsahovo áno, ale presné súbory v3.17 a ich hashe nie sú v addende; tvrdenia sú preto kontextové, nie sealed-reproducible. |

## 5. Čo auditorovi chýbalo

Balík porušil vlastné pravidlo protokolu v jednom bode: manifest mal obsahovať
pôvodnú relatívnu cestu, rolu a dôvod zaradenia, ale obsahoval iba meno kópie
a SHA-256. Integrita kópie bola overiteľná, jej väzba na zdrojový strom nie.

Pre tento konkrétny audit mali byť priložené aspoň:

1. frozen `scripts/213...py` — historický spotrebiteľ chybnej formulácie;
2. frozen `scripts/128...py` — deklarovaný predchodca/base;
3. prereg/expectation, raw JSON a audit RUN-FULL-002;
4. skripty `234` a `235` a ich raw JSON, ak sa má auditovať tvrdenie
   „`A_f` nie je nový fit“ a nulový prechod skráteného radu;
5. presný zmrazený v3.17 skript 09 a hlavný dokument, ak sa má vyhlásiť
   karanténa registrovaných predikcií;
6. verzie Python/SymPy/NumPy a reprodukčný príkaz s timeoutom;
7. pri každom externom súbore pôvodnú cestu, hash, rolu a stav
   `primary/derived/context`.

## 6. Sú výpočty potrebné dávať auditorovi?

**Áno, ak má hodnotiť výpočtový alebo formula-lineage verdikt.** Nie je však
potrebné posielať celú výpočtovú históriu.

### Minimálny výpočtový kapsul pre tento problém

1. spustiteľný runner a všetky importované base moduly;
2. presný vstup/config;
3. predregistrácia očakávania a tolerancií;
4. raw výsledok a ľudský audit výsledku;
5. SHA-256 každého súboru;
6. jeden krátky reprodukčný príkaz s vnútorným aj vonkajším timeoutom;
7. tabuľka troch skúšobných módov `k1,k2,k3`:
   - stará formulácia musí ukázať rozdielny `D(a,k)`;
   - opravený raný rad musí ukázať rovnaký výsledok v tolerancii;
8. negatívna kontrola: zmena `Phi(k)` bez kompenzačnej mocniny musí gate
   znovu zhodiť.

Plný CLASS/CAMB alebo CMB likelihood pre otázku fixed-`k` **nie je potrebný**.
Ten patrí do neskoršieho samostatného balíka. Cieľom je najmenší výpočet,
ktorý môže tvrdenie potvrdiť aj vyvrátiť.

## 7. Čo očakávať od ďalšieho kola auditora

1. Pri každom závere označiť `OBSERVED_IN_PRIMARY`,
   `INDEPENDENTLY_RECOMPUTED`, `INFERRED_FROM_PROJECT_DOCS` alebo
   `CONTEXT_ONLY`.
2. Citovať presnú cestu, hash a riadok primárneho vzorca.
3. Reprodukovať minimálny multi-`k` test namiesto preberania projektového
   raw verdiktu.
4. Pre `A_f` preveriť aspoň dva zmrazené body `lambda` a potvrdiť, že
   k-nezávislosť je štrukturálna, zatiaľ čo číslo `A_f` je
   pracovný-bod-dependent.
5. Určiť interval platnosti skráteného raného radu podľa relatívnej chyby
   voči exact-A1 backgroundu; nulový prechod sám iba dokazuje neskorú smrť.
6. Prejsť všetkých priamych potomkov starého `denominator` a rozdeliť ich
   na `contaminated`, `quarantined` a `independent`.
7. Ak použije súbory mimo zapečateného balíka, priložiť ich zoznam a hashe.

## 8. Autoritatívny záver

Oba posudky sa **prijímajú ako užitočné externé overenie s obmedzeniami**.
Neudeľujú nový stav koľaje. Potvrdzujú, že:

- historický fixed-`K_MPC` background je správne zastavený;
- algebraická amplitúdová transformácia je správna pre raný rad;
- exact-A1 background, nie skrátený K7 denominator, je prípustný základ
  nástupníckej vetvy;
- `A_f` musí niesť úplný provenance tag;
- budúce externé balíky musia obsahovať primárny výpočtový kapsul, ak sa
  od auditora očakáva viac než kontrola dokumentačnej mapy.

Stav balíka: `EXTERNAL_RESPONSE_ASSESSED`.  
Stav projektu: nezmenený.
