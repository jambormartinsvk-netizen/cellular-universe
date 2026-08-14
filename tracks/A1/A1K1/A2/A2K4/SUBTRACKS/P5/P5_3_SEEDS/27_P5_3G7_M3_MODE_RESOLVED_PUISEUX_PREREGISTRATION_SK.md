# A2-K4/P5.3g7-M3 — predregistrácia módovo rozlíšeného Puiseuxovho seedu

**Dátum:** 2026-07-16  
**Stav pred behom:** `PREREGISTERED / NOT RUN`  
**Vlastník:** `A1-K1 → A2-K4 → P5 → P5.3g7-M3`  
**Budúci runner:** jediný povolený `scripts/261_script_KMPC_022_P5_3g7_mode_resolved_full_seed_audit.py`  
**Skóre:** žiadne; ide o vstupnú bránu P5.3, nie G7/G8 PASS.

## Ľudské vysvetlenie výpočtu

Štandardný seed opisuje päť základných druhov prvotných porúch: AD, CDI, BI,
NID a NIV. K4 k nim pridáva palivo, popol a podmienene aj samostatnú paru.
M3 má zistiť, či sa prvá malá K4 korekcia metriky dá odvodiť z pohybových
rovníc bez toho, aby sme si výsledok vybrali z Einsteinovho constraintu,
ktorý chceme následne testovať.

Ak je koľaj konzistentná, dynamické rovnice určia regulárne koeficienty
`h, eta` a všetkých druhov. Dve nepoužité rovnice `00` a `0i` potom musia
vyjsť samy. Ak ich použijeme už pri výbere seedu, malé rezíduum by bolo iba
kruhovou identitou zakázanou AR45.

## Autoritatívne vstupy a obmedzenie starého BR3

- štandardný nulový limit a amplitúdy: `26_P5_3G7_M1_STANDARD_METRIC_SOURCE_MAP_SK.md`;
- exact-A1 background: `Independent_Audits/K_MPC_0_05/09_P4_EXACT_A1_BACKGROUND_REDERIVATION_PLAN_AND_SOURCE_AUDIT_SK.md`;
- kovariantné K4 species znamienka: `Independent_Audits/K_MPC_0_05/11_P4B2A_COVARIANT_K4_SPECIES_LEDGER_SK.md`;
- plný P5 stav a constrainty: `scripts/baseScripts/p5_general_synchronous/`;
- leading `delta_f,U_f,U_c`: P5.3d/script 245.

Skripty 95–124 sú iba regresný oracle. Skript 95 použil presný background,
ale držal metriku ako test field. Skripty 119/124 riešili naraz aj `00` a
`0i`, iba pre NID/NIV, a normalizovali výsledok na staré `Phi z^p` pri
pevnom móde. Nemôžu preto samy udeliť M3 PASS. Presný lineage rozsah je v
`Audit/A2_K4_P5_3G7_M3_LEGACY_BR3_LINEAGE_AUDIT_2026-07-16.md`.

## Oddelenie backgroundu a perturbatívneho módu

Definujme

```text
H_r0 = H0 sqrt(Omega_r0),   q = k/H_r0,   z=q a,
p = 4-3 delta,
Phi(k) = A_f q^(-p),        A_f = 7809.270101963506.
```

Potom presne platí `Phi(k) z^p = A_f a^p`.

V skorom backgrounde bez paliva je `D0(z)=1+MU z`, kde
`MU=(Omega_m H0/sqrt(Omega_r0))/k`. Interakčný koeficient má tvar

```text
gamma_0(z)=G2 z^2 / sqrt(1+MU z),
G2=[lambda/sqrt(Omega_r0)]/q^2.
```

Na prvom ráde v `Phi` sa palivo `F`, transferovaný popol `C` a ich súčet
`D1=F+C` rozvinú takto:

```text
F_0=1,  F_1=0,
F_j=-(1/j) sum_(l=2..j) gamma_l F_(j-l),
C_0=C_1=0,
C_j=(1/(p+j-1)) sum_(l=2..j) gamma_l F_(j-l),
D1_j=F_j+C_j.
```

Prvé povinné koeficienty sú

```text
D1_0 = 1,
D1_1 = 0,
D1_2 = G2[-1/2 + 1/(p+1)],
D1_3 = (-G2 MU/2)[-1/3 + 1/(p+2)].
```

Po násobení `Phi z^(p+j)` sa pri `j=0,2,3` všetky mocniny `q` presne
vykrátia. Runner musí túto identitu overiť symbolicky aj numericky pre
`k={0.005,0.05,0.15} Mpc^-1` pri rovnakom fyzickom `a`.

## Módovo rozlíšené vrstvy

Jedna univerzálna mocnina nestačí, pretože NID/NIV majú skoršie kompenzované
radiačné hustotné alebo rýchlostné členy.

| Mód | vedúca mocnina `h_x` | povinné prvé frakčné vrstvy `p+j` | dôvod |
|---|---:|---|---|
| AD | 2 | `j=0,1,2` | nižšie vrstvy musia byť nulové; common fuel začína pri `p+2` |
| CDI | 1 | `j=0,1` | common fuel/background odpoveď pri `p+1` |
| BI | 1 | `j=0,1` | common fuel/background odpoveď pri `p+1` |
| NID | 3 | `j=0,1,2,3` | rýchlosť → matter dressing → shear → common fuel |
| NIV | 2 | `j=-1,0,1,2` | vedúca relatívna rýchlosť začína o jeden rád skôr |

Rozsah sa nesmie zmenšiť po zhliadnutí výsledku. Rozšírenie je povolené iba
ak holdout ukáže prvý nenulový vynechaný rád; dôvod sa najprv zapíše do MD.

## Rovnice použité na odvodenie a holdout

| Úloha | Rovnice | Hodnotenie |
|---|---|---|
| určujú koeficienty | photon continuity/Euler, collisionless continuity/Euler/shear, baryon continuity, CDM continuity, Einstein trace a traceless | ich rezíduum testuje vyriešenie sústavy, nie nezávislú fyziku |
| nezávislý holdout | Einstein `00` a `0i` | nesmú vstúpiť do matice ani regularizácie |
| samostatná kontrola | total energy/momentum ledger a nulový interaction limit | nezávislý súčet druhov |

`U_c` ostáva povinnou stavovou premennou. Na prvom ráde v `Phi` je jeho
energy-frame silový zdroj nulový, pretože `Q` je `O(Phi)` a
`U_d-U_c` je ďalšie `O(Phi)`. Prvý nenulový člen je teda `O(Phi^2)` a musí
byť prenesený z P5.3d ako `U_c ∝ a^(n+8-6 delta)`, s nenulovým
koeficientom pri fyzikálnom transfere a nulou pri `lambda→0`. Stav `U_c` sa
nesmie odstrániť ani natrvalo nastaviť na nulu.

## Podmienená para S-C

Na matematický M3 test sa používa výslovne podmienená vetva S-C:

- celková collisionless radiácia sa rozdelí podľa `N_eff=3.046+0.0535` na
  štandardné neutrína a paru;
- v každom štandardnom móde majú obe časti rovnaký seed a rovnakú
  collisionless hierarchiu;
- ich vážený súčet musí byť identický s už auditovaným spoločným
  collisionless sektorom.

Toto dokazuje iba existenciu konzistentného matematického rozdelenia. Nie je
to odvodenie vzniku pary, predikcia korelácie ani dôvod zvýšiť fyzikálne
skóre. S-M z Q18/Q22 ostáva otvorená fyzikálna vetva.

## Pred behom zmrazené očakávania

Runner bude bez ODE. Použije dve fyzické štartovacie plochy
`a_deep=1e-6`, `a_shallow=1e-4` a tri vyššie uvedené `k`.

### Predbehové spresnenie TCA rozsahu

Po prečítaní P5.3g4/g5/g6 sa pred implementáciou potvrdilo, že presný tvar
photon `l=2` kolízneho bloku a synchronný gauge most sú známe, ale fyzická
finite-start amplitúda stále obsahuje neuzavretú normalizáciu
`n_e0 sigma_T`. Preto runner musí podporovať dve explicitne odlíšené fázy:

1. `M3-TCA0`: prísny skorý limit `epsilon=1/opacity→0`; smie testovať
   módovú Puiseuxovu metriku a holdouty, ale nemôže uzavrieť celé P5.3g7;
2. `FULL-FINITE-OPACITY`: rovnaký kód s odvodenou, nie fitovanou hodnotou
   opacity; do jej dodania musí skončiť fail-closed `REVIEW_BLOCKED` bez
   fyzikálneho behu.

Prvý povolený beh je iba `M3-TCA0`. Aj pri úspechu bude verdikt
`PASS_M3_TCA0_CONDITIONAL`, fyzikálna hĺbka ostane `60/100` a P5.3g7 ostane
blokovaná finite-opacity vstupom. Toto spresnenie vzniklo pred výpočtom a
nemení nižšie reziduálne prahy.

| Kontrola | PASS rozsah | STOP/REVIEW |
|---|---|---|
| symbolické `k`-cancel identity | presná nula | nenulový výraz → STOP M3 formulácie |
| štandardný M1 seed | normalizačný/row residual `<1e-10` | väčší → REVIEW zdroja, nie fyzikálny STOP |
| dynamická M3 matica | plná hodnosť v každom móde a `k` | strata hodnosti/singularita → REVIEW alebo STOP podľa invariantnosti |
| driver rezíduá | škálované maximum `<1e-10` | väčšie → STOP runnera |
| nezávislé `00`,`0i` | coefficient-scaled maximum `<1e-9` | väčšie → fyzikálny STOP/REVIEW M3; nesmie sa opravovať ich vložením do matice |
| zakázané skoršie vrstvy AD/CDI/BI | amplitúda `<1e-10` na jednotku `Phi` | nenulová regulárna vrstva → skontrolovať úplnosť vstupného seedu |
| tri módy `k`, rovnaké `a` | background rozdiel `<1e-12` relatívne | závislosť backgroundu od `k` → STOP |
| S-C split | vážený súčet `<1e-14` | nesúlad → STOP implementácie |
| dva štarty | konečné stavy; pomer vedúcich K4 členov zodpovedá registrovanej mocnine s relatívnou odchýlkou `<1e-6` | neregulárnosť alebo opačná mocnina → STOP/REVIEW |
| `U_c` | prítomný stav; leading identita `<1e-12`; `lambda→0` presne nula | chýbajúci stav alebo nútené `U_c=0` → STOP |

Starý BR3 mal pre NID/NIV rezíduá približne `1e-15`, ale používal všetky
Einsteinove rovnice naraz. Preto sa táto hodnota nepoužíva ako dôkaz; nový
holdout limit `1e-9` je vopred širší a samostatný.

## Výsledkové vetvenie

- **PASS M3-TCA0:** uzavrie prísny skorý metrický limit a povolí neskorší
  `FULL-FINITE-OPACITY` beh toho istého runnera; P5.3g7 ani skóre nemení.
- **REVIEW:** iba pri numerickej hodnosti, truncation okraji alebo chýbajúcom
  vyššom ráde; najviac dve technické opravy podľa capu.
- **STOP:** invariantný nenulový holdout, `k`-závislý background, chýbajúci
  povinný stav alebo singularita pri zmrazených A1 parametroch.

## Prevádzkové limity

- runner aj shared modul musia prejsť error-ledger kontrolou;
- interný deadline `<=5 s`;
- každý `version`, `py_compile`, `--help`, smoke a plný beh je samostatný;
- každý vonkajší timeout `<=10 s`;
- immutable JSON vznikne až po úspešnom preflighte;
- žiadna zmena očakávania po behu bez samostatného odôvodnenia v Markdowne.

## PF-055 a povolený RERUN1

Prvý plný pokus runnera 261 skončil po zostavení payloadu na
`TypeError: Object of type bool is not JSON serializable`. Výstup
`RUN_KMPC_022...json` nevznikol a žiadny fyzikálny verdict sa neprijíma.
Pôvodný runner s hashom `6f7499...6846b` je zachovaný
`DO_NOT_RUN_TECHNICAL`.

Povolený nástupca
`261_script_KMPC_023_P5_3g7_mode_resolved_full_seed_audit_rerun1.py` smie
pridať iba rekurzívnu konverziu NumPy skalárov na natívne JSON typy. Zostáva
rovnaký base hash `5a89cf...b7ae`, rovnaké rovnice, tri `k`, dve plochy,
prahy, interný limit 5 s a vonkajší limit 10 s. Očakávania sa nemenia.

## Neskoršie obmedzenie po KMPC-024

RERUN2 správne opravil M1 anchor, ale contract-parity audit zistil, že base
V1 nesplnil vlastnú nadradenú predregistráciu: frakčný `VARS` neobsahoval
`delta_f,U_f` a driver neobsahoval ich continuity/Euler rovnice. Preto sa
machine `REVIEW_M3_TCA0_UNCLOSED` obmedzuje na 11-zložkový ansatz. Nenulové
holdouty nie sú rozsudkom smrti úplnej K4. Autoritatívny rozsah je v
`31_P5_3G7_M3_TCA0_RERUN2_RESULT_AND_CONTRACT_STOP_SK.md`.
