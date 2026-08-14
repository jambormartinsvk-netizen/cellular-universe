# Audit všetkých číselných a exaktných podmienok existencie v3.18

**Dátum auditu:** 9. august 2026  
**Rozsah:** kandidát v3.18, dokumenty `01`–`03`, prijaté EA-004/029/039/047
a historická proveniencia v3.17  
**Autoritatívny rozsudok:** žiadny nový `PASS/STOP`; ide o inventár a
release-semantickú opravu  
**Výstup:** dvojjazyčný register `04`, 43 riadkov `EC01`–`EC43`

## 1. Dôvod

Predikčný register `02` správne zachytáva P01–P11, ale neobsahuje všetky
podmienky, ktoré musí fyzikálne prípustná realizácia KBTP splniť. Zákon
zachovania, nezávislosť FLRW backgroundu od Fourierovho módu, gauge/Bianchi
closure, stabilita, ekvivalenčný princíp alebo existencia spoločného
lokálneho operátora nie sú predikcie rovnakého druhu ako `H0` alebo `S8`.

Preto vzniká samostatný register `04`. Je to spoločný index:

- exaktných fyzikálnych zákonov a algebraických identít;
- otvorených existenčných mantinelov bez vymyslenej číselnej medze;
- podmienených mechanistických hodnôt a kalibračných benchmarkov;
- observačných survival targets P01–P11 s presným death reach;
- čísel, ktoré sa výslovne nesmú použiť ako fyzikálne kill conditions.

## 2. Hlavné zistenia

1. Žiadny riadok P01–P11 nemá vo v3.18 certifikovaný `THEORY_LEVEL` dosah.
   Každý aktívny cieľ je však záväzný v presne pomenovanej formulácii.
2. Vnútri jednej koľaje sa všetky jej povinné mantinely pretínajú. Medzi
   fyzikálne alternatívnymi top-level koľajami však platí logické `OR`:
   `A_theory=union_{t in T_top} A_t`. Teória zomiera až vtedy, keď je
   `T_top` preukázane úplná a každá množina `A_t` je certifikovane prázdna.
3. Exaktné zákony nemajú observačnú toleranciu. Merané medze sa naopak smú
   použiť iba s explicitným datasetom, modelom, CL, neistotami, kovarianciou
   a systematikami.
4. P01 a P11 sú jeden termálny záväzok. `Delta N_eff`, `N_eff`, teplota a
   peak sa nesmú počítať ako štyri nezávislé potvrdenia.
5. P03 obsahuje dve rozdielne hranice: `r>=1e-10` ruší ostrý legacy odhad,
   kým `r>=1e-3` je širší historický praktický kill marker mechanizmu.
6. P04/P05 tri body sú podmienené diskrétne výstupy, nie intervaly,
   posterior ani likelihood. Pred observačným rozsudkom treba A2/A3.
7. `C=28`, `m=1/2`, `delta=0.02297`, `lambda=0.15` a `A_f` majú rôzne
   dôkazové triedy. Nesmú sa zlúčiť pod označenie „odvodené konštanty“.
8. Register používa presne šesť kanonických tried; podrobnejšia proveniencia
   zostáva v samostatnom stĺpci `subtype_v3_18` a nevytvára ďalšiu
   rozhodovaciu triedu.
9. Skóre, počty pokrytia, solverové tolerancie, gridy, runtime a package
   počty sú procesné čísla bez fyzikálneho death reach.

## 3. Externé referenčné medze pri obsahovom cut-offe

Register uvádza iba primárne zdroje a presne označuje, že ide o comparatory:

- GW170817/GRB170817A: konzervatívny timing-derived interval
  `-3e-15 <= (c_GW-c_gamma)/c <= +7e-16` z delay `1.74±0.05 s`;
  abstrakt zdroja mu nepriraďuje konvenčnú CL;
- LHAASO GRB221009A, 95 % CL: `E_QG,1>10 E_Pl` a
  `E_QG,2>6e-8 E_Pl` v ich parametrizácii;
- Fermi-LAT GRB090510, subluminal 95 % CL: `E_QG,1>7.6 E_Pl` a
  `E_QG,2>1.3e11 GeV`;
- MICROSCOPE, 1 sigma:
  `eta(Ti,Pt)=[-1.5 ±2.3(stat) ±1.5(syst)]e-15`;
- Planck: `N_eff=2.99±0.17`, `n_s=0.9649±0.0042`,
  `H0=67.4±0.5 km/s/Mpc` pri 68 % confidence v uvedených dataset/model
  scopes;
- SH0ES: `H0=73.04±1.04 km/s/Mpc` pre Cepheid–SN distance ladder;
  publikovaná neistota zahŕňa systematiky;
- Breuval et al. 2024: `H0=73.17±0.86 km/s/Mpc` zo štyroch kalibračných
  kotiev; Chen–Wang 2026: `H0=73.30±0.92 km/s/Mpc` zo sedem-route
  covariance review;
- BICEP/Keck BK18: `r_0.05<0.036` pri 95 % CL;
- KiDS-Legacy cosmic shear: marginal mode a 68 % HPDI
  `S8=0.815^{+0.016}_{-0.021}`;
- DESI DR2+CMB+DESY5: joint CPL comparator `w0=-0.752±0.057`,
  `wa=-0.86^{+0.23}_{-0.20}` ako marginalizované 68 % intervaly so silnou
  kovarianciou;
- CMB-S4 čísla pre `r` sú výhradne budúci forecast, nie súčasný kill
  condition.

Tieto hodnoty nie sú automatické KBTP STOP prahy. Najmä konfliktné `H0`
výsledky sa nesmú zliať do jedného falošného intervalu a ich publikované
`±` neistoty nemajú naprieč všetkými zdrojmi jednu spoločnú CL konvenciu.

## 4. Veci bez povoleného číselného kill okna

Vo v3.18 sa nesmie vymyslieť číslo pre:

- súvislý prípustný interval `lambda`;
- širšie P01 okno po neznámom branchingu a reheatingu;
- drift `delta(a)`;
- detektorovú citlivosť sterilného popola bez particle modelu;
- fyzický kvadratický P10 koeficient;
- P11 detector response;
- spojitú H0/S8 obálku z troch PT1 bodov;
- neprázdnosť `K_all` bez witnessu;
- úplnú all-sector toleranciu common-`c` pred odvodením mapy.

Stav týchto položiek je `OPEN_NO_KILL_WINDOW`, nie `PASS` ani `STOP`.

## 5. Release dôsledok

Zenodo payload sa rozšíri z 13 na 15 súborov o slovenský a anglický register
`04`. Dokumenty `00`, `01`, `03`, changelog, Zenodo description a oba
manifesty musia byť zosúladené. V predikčných tabuľkách `02` sa iba uzavrela
komplementárna P03 hranica na `r>=1e-10` a výslovne sa oddelil CMB-S4
forecast od súčasnej kill condition; samotné survival targets sa nemenia.
Register `04` pridáva podmienky, ktoré nie sú predikčnými riadkami.

Plánované publikačné okno je **11.–13. august 2026**. Obsahový cut-off je
**9. august 2026**, pretože nový register je nový release obsah; publikačné
okno zostáva samostatným plánom uploadu.

## 6. Auditné nálezy a ich uzavretie

Tri nezávislé read-only kontroly našli iba opraviteľné stagingové položky;
žiadny prijatý vedecký checkpoint nebol zneplatnený:

- opravila sa falošne prísna globálna `AND` logika medzi alternatívami na
  prienik v koľaji a zjednotenie medzi koľajami;
- ostrá P03 hranica sa uzavrela na `r>=1e-10`;
- doplnil sa úplný PT1 triple-zero comparator, `16_gluon`, Landauov
  range-only mantinel, M-011 absolútny transfer, `g_*s,nu=10.75`, presné
  PT1 input-to-output párovania a metadáta observačných comparatorov;
- z EC43 sa odstránil nepovolený kill threshold `ln T_K4>=1`: čísla
  `0.4620397929` a `11.5901470198` samy nemajú death reach; rozhoduje až
  úplný K4.1 test regular-mode basis a fundamental matrix;
- EC42 sa obmedzil na interface-adapted ortonormálny `1+1` rámec s presne
  definovanými `E`, `q`, `P_n`, `S` a rootom `v_L`; numericky stabilné
  vyhodnotenie sa už nezamieňa za dynamickú stabilitu alebo Landau PASS;
- procesný stav `10 WAITING / 0 EXCLUDED` sa odstránil z poľa fyzikálnej
  požadovanej hodnoty;
- zaviedli sa presne šesťhodnotové `canonical_class` a osobitný
  `subtype_v3_18`.

Klasifikácia opráv: `SAME_TRACK_CONFIRMED`; ide o opravu draftovej logiky,
parity a proveniencie, nie o nový fyzikálny výpočet alebo nový `PASS/STOP`.

## 7. Auditné odporúčanie

`SAME_TRACK_CONFIRMED / NO_NEW_PHYSICAL_VERDICT`.

Pred zapečatením treba:

1. overiť SK/EN paritu všetkých 43 riadkov, 14 stĺpcov, kanonických tried,
   hodnôt, stavov a death reach;
2. overiť, že P01–P11 sa nezmenili a EC register ich neprepisuje;
3. overiť odkazy na primárne zdroje a scope ich čísel;
4. overiť payload `15/15`, non-self SHA riadky `14/14` a nulový mismatch;
5. zachovať stav `NOT_STAGED / NOT_COMMITTED / NOT_PUBLISHED`, kým Martin
   Jambor neschváli čitateľský kandidát.

## 8. Finálny preseal výsledok

Presný kandidát bol po opravách zmrazený a nezávisle skontrolovaný:

- staging manifest SHA-256:
  `E22A96E3CA14BF889A6796875F483C7CB3212E49198BA78F12F7B4E03BCF7D75`;
- non-self SHA manifest SHA-256:
  `DB131229D1587FC85E4078F09483222FD47BB82863F0ED2EAF95576E5B3B24DF`;
- payload `15/15`, non-self hash riadky `14/14`, mismatch `0`;
- SK/EN register `43×14`, šesť kanonických tried, numerická a death-reach
  parita bez mismatchu;
- P01–P11 `11/11`, rovnice `40/40`, release copy hash parity `15/15`;
- fyzický počet release súborov mimo `.git` je `266`;
- `git diff --check` prešiel a staged index zostal `0`.

Nezávislé odporúčania: fyzika `PASS_RECOMMENDATION`, matematika
`RECOMMEND_RC_AUDIT_PASS`, dokumentácia bez `T1/S1–S4`; jediný P0 bol zápis
R18 do živých plánov a je uzavretý týmto batchom.

**Rozhodnutie hlavného orchestrátora:**
`RELEASE_DOCUMENTATION_PRESEAL_ACCEPTED / SAME_TRACK_CONFIRMED /
NO_NEW_PHYSICAL_PASS_STOP / WAITING_MARTIN_REVIEW`.

Tento rozsudok prijíma úplnosť a vnútornú konzistentnosť inventára pre
vydanie. Nedokazuje existenciu globálnej neprázdnej množiny
`A_theory`, nemení stav A2-K4, skóre `60/100`, P5 `3.5/6`, raw evidence ani
žiadny vedecký `PASS/REVIEW/STOP` koľaje.

## 9. R19 — oddelenie čitateľského registra od interných stavov

Na rozhodnutie autora bol z verejných slovenských a anglických tabuliek
predikcií odstránený stĺpec `stav_v3_18` / `v3_18_status`. Kódy pracovného
workflow nie sú fyzikálne veličiny a čitateľ Zenodo ich nemá dekódovať.
Verejný register má po novom `11` riadkov a `9` polí: zachováva povolené
tvrdenie, survival target, presný dosah prípadného vylúčenia, význam zhody,
evidence a explicitný nonclaim. Ľudské súhrny používajú slovné
kvalifikátory ako „podmienený výsledok“, „historický cieľ“, „benchmark“
alebo „odvolaná relácia“, nie interné statusové reťazce.

Presné interné stavy P01–P11 sa nestratili. Autoritatívne zostávajú iba v
R19 bloku `tracks/00_CURRENT_EXECUTION_PLAN.md`. Statusové tabuľky koľají,
otázok a metodiky neboli týmto rozhodnutím dotknuté.

Nezávislá matematická kontrola potvrdila, že oproti R18 bolo z oboch CSV
odstránené iba statusové pole a všetkých deväť ostatných polí zostalo
nezmenených. Fyzikálny delta-audit potvrdil `FINDING_CLASS=NONE`,
`SAME_TRACK_CONFIRMED`: P03 stále rozlišuje hranice `r>=1e-10` a
`r>=1e-3`, P04/P05 zostávajú podmienenou diagnostikou, P08 zostáva
odvolaná bez aktuálneho cieľa, P09 benchmarkom bez kill okna a P01/P11
jedným podmieneným termálnym záväzkom.

**Rozhodnutie hlavného orchestrátora:**
`PUBLIC_STATUS_COLUMN_REMOVED / INTERNAL_STATE_PRESERVED /
NO_NEW_PHYSICAL_PASS_STOP / SAME_TRACK_CONFIRMED`.

Nový preseal viaže staging manifest
`8E6A66252526F6FC26411C392D51BC35A9567A3563C65C326C9ABF0AEB2DEE34`
a non-self SHA manifest
`61AB469EECD7FF37F78C8AF226F50AE3BF1C694CF845747D7D21ED87AA1F03EC`.

## 10. R20 — audit deviatich metodických nejasností

Externá čitateľská kontrola označila deväť miest, ktoré neboli vo vzájomnom
rozpore, ale umožňovali širší výklad. Hlavný orchestrátor ich vyhodnotil
takto:

| Bod | Relevantnosť | Uzavretie |
|---|---|---|
| FS-GATE-01 verzus FS-GATE-02 | vysoká | FS-GATE-01 teraz definuje správanie a `F_adm` aj bez closed-form funkcie; FS-GATE-02 až potom testuje existenciu v tejto triede. |
| kill window verzus globálna prázdnosť | vysoká | riadkový kill je formulation/track-level; theory-level smrť vyžaduje úplný zoznam top-level alternatív a prázdnosť každej z nich. |
| význam `60/100` | vysoká | ide o kumulatívnu váhu autoritatívne prejdených fyzikálnych brán G5/G6, nie percento pravdivosti, podmienok alebo nájdených funkcií. |
| technická chyba verzus `10/10` | stredná | technické chyby zastavujú proces do autorizácie; samy nikdy nemenia fyzikálny verdict. |
| Q12 evenness verzus Lorentz | stredná | evenness je lokálna algebraická vlastnosť jedného operátora, nie globálna symetria systému. |
| Q22 zákaz `k`-backgroundu | vysoká | zákaz je fundamentálne oddelenie backgroundu od porúch; staré `K_MPC`/`Phi=1` čítanie bolo obmedzené práve jeho porušením. |
| Q15/Q18 termálny cieľ | vysoká | `Delta N_eff=0.0535` je záväzok presnej P01/P11 formulácie, kým chýba úplná source-to-BBN/CMB mapa; nie global posterior. |
| historické formulácie | vysoká | ledger má teraz pri každom riadku pôvodný scope, rozhodujúci test a presný dosah; kde kill okno neexistuje, dokument ho výslovne nevymýšľa. |
| blocker A3 | vysoká | rozlíšená je procesná, fyzikálna aj auditná blokácia; stav je `WAITING`, nie STOP A3. |

Klasifikácia: `NO_MATERIAL_FINDING / DOCUMENTATION_CLARITY_CLOSURE /
SAME_TRACK_CONFIRMED`. Oprava nemení rovnice, čísla, survival targets,
death reach, raw, skóre `60/100`, stav A2-K4 ani povolenie A3.

Nezávislé exact-byte audity uzavreli R20 bez nálezu: matematika
`RECOMMEND_RC_AUDIT_PASS / FINDING_CLASS_NONE`, fyzika
`PASS_RECOMMENDATION / FINDING_CLASS_NONE / SAME_TRACK_CONFIRMED` a
dokumentácia/release `NO_FINDING`. Potvrdené boli SK/EN otázky `34/34`,
historický ledger `8/8`, manifest `14/14`, release kópia `15/15`,
`git diff --check` PASS a staged index `0`.

R20 preseal viaže staging manifest
`1EAD40A1A0BECA3354631F1793EAAD4D009EE406DBAD7798FEF159B7C648748D`
a non-self SHA manifest
`C5DAAD9B336308A4296C49CBB7B53C1D5F97F7789ABEC06F9E8A384A470D9F57`.
