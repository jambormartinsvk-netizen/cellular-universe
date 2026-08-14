# A2 — kanonický stav, skóre a dôvod smrti K1 až K12

**Dátum:** 2026-07-14  
**Aktualizácia:** po jednotnej sekvenčnej rekalibrácii G0–G10 pre K1–K12 a dokončení K4.2  
**Nahrádza iba stavové tabuľky, nie historické odvodenia.**

Názov súboru s koncovkou `K1_AZ_K11` sa ponecháva kvôli stabilite starších
odkazov; obsah tejto verzie už zahŕňa aj K12.

## Význam skóre od rekalibrácie 2026-07-14

Skóre `N/100` je iba najvyššia **sekvenčne úspešne prejdená** kanonická
brána. Neskorší vykonaný no-go alebo kill test sa zapisuje do samostatného
stĺpca a skóre nezvyšuje. Mŕtva koľaj si ponecháva poslednú prejdenú bránu,
dôvod smrti aj najhlbšie vykonaný test.

| Brána | Skóre | Povinný jednotný obsah |
|---|---:|---|
| G1 | `10/100` | registrovaná fyzikálne odlišná hypotéza |
| G2 | `20/100` | uzavretý A1 background a úplný energy-momentum ledger bez placeholdera |
| G3 | `30/100` | lokálna akcia alebo úplný kovariantný konštitutívny uzáver |
| G4 | `40/100` | úplné lineárne rovnice, Einsteinove constrainty, sign/gauge/null |
| G5 | `50/100` | úplná regulárna superhorizontová báza všetkých fyzických módov |
| G6 | `60/100` | high-k a subhorizontová stabilita celej bázy s konvergenciou |
| G7 | `70/100` | vlastný plný Einstein–Boltzmann, rekombinácia a fyzické transfery |
| G8 | `80/100` | CMB-normalizované spektrá a `sigma8/S8` screen |
| G9 | `90/100` | spoločná likelihood a systematiky |
| G10 | `100/100` | všetky brány verzie a nezávislá reprodukcia |

Podrobná definícia a changelog sú v
`Audit/JEDNOTNA_SEKVENCNA_STUPNICA_HLBKY_A2_A_REKALIBRACIA_K1_K12.md`.

## Úplná stavová tabuľka
| Koľaj | Stav | Kanonická max. prejdená hĺbka | Najhlbší test / otvorená brána | Základ a dôvod |
|---|---|---:|---|---|
| A2-K1 | `MŔTVA M-009` | `40/100` | G5 no-go | `Q_c^mu=Gamma rho_f u_c^mu`; úplná regulárna báza nebola dokončená |
| A2-K2 | `MŔTVA M-008` | `30/100` | G6 FAIL | striktne barotropické palivo; `c_s^2=w<0` |
| A2-K3 | `MŔTVA M-010` | `40/100` | G5 no-go | `Q_c^mu || u_f^mu`; úplná regulárna báza nebola dokončená |
| **A2-K4** | **`PREŽÍVA K4.2; M-011 OBMEDZENÁ`** | **`60/100`** | **G7 otvorená** | úplná regulárna báza aj high-k/subhorizontová brána prešli |
| A2-K5 | `MŔTVA M-012` | `40/100` | G6 vykonaná; G8 hybridný screen FAIL | chýbala úplná G5 báza aj vlastná G7; konzervatívny screen `S8=0.9836–1.0063` ostáva kill dôkazom |
| A2-K6 | `MŔTVA M-013` | `30/100` | G6 presný `G_ij` no-go | G4–G5 sa po nutnom QS no-go nerobili |
| A2-K7 | `PREŽÍVA CEZ PODKOĽAJE` | `20/100` | G3 otvorená | chýba odvodený lokálny kernel, `delta Q`, noise/memory |
| A2-K8 | `ČAKÁ` | `10/100` | G2 otvorená | registrovaná produkcia počtu; chýba production operator a ledger |
| A2-K9 | `ČAKÁ` | `10/100` | G2 otvorená | registrovaný spoločný produkčno-rozptylový mechanizmus |
| A1-K2/A2-K10 | `ČAKÁ; INÁ A1 VETVA` | `10/100` | nová A1/G2 otvorená | prahový/fázový tok mení background |
| A2-K11 | `PREŽÍVA IBA HYPOTÉZU` | `10/100` | G2/G3 otvorená | ortogonálny drag nemá prijatý lokálny operátor a ledger |
| A2-K12 | `PREŽÍVA CEZ K12-K2/K3` | `10/100` | G2 otvorená | opačné náboje bez produkčného operátora nereprodukujú A1 tok |

## Dôvody smrti a otvorené steny po jednej vete
- **K1:** near-vacuum recoil vytvoril veľký publikovaný `1/delta` fluidný
  mód v presne definovanom constant-rate modeli.
- **K2:** záporná barotropická zvuková rýchlosť vytvorila high-k rast.
- **K3:** zmena bezmomentového rámca zmenšila, ale neodstránila publikovaný
  `Gamma/delta` problém.
- **K4:** historický M-011 dôvod je obmedzený; K4.1 našla presne tri
  regulárne módy a starý velocity seed neleží v ich priestore. K4.2 navyše
  našla zdravý propagujúci high-k symbol a na `q=30,300,1000` menší transfer
  než nulový limit. Otvorenou stenou je K4.3.
- **K5:** zdravá akcia odstránila fluidný pól, ale vynútila príliš silnú
  príťažlivú piatu silu.
- **K6:** derivatívny operátor nemenil znamienko efektívnej gravitácie v
  zdravom intervale; `mu_cc` zostalo nad jednotkou.
- **K11:** skript 47 reprodukoval silné tlmenie iba v nesprávnej ODE sústave:
  zmiešal dva fluidné uzávery, zosilnil proper-time sadzby faktorom `1/a` a
  nepropagoval `00` constraint. K11 ako fyzikálna trieda zatiaľ nezomrela.
- **K12-K1:** presná nábojová symetria zrušila čistý skalárny tok a
  neznížila lineárny celkový rast; aktívna K12-K3 potrebuje samostatný
  produkčný operátor a test nábojovej segregácie.

K4, K7–K11 a rodič K12 nemajú aktuálny konečný dôvod smrti. M-016 sa týka
iba K12-K1. K4.1 a K4.2 prešli; prípadná budúca smrť K4 musí vzniknúť v K4.3 alebo
neskoršej bráne ako nový zdokumentovaný dôvod, nie obnovením M-011.

## Obmedzenia starších stavov

- staré `MŔTVA M-011` zostáva historický záznam, ale konečný rozsudok je
  pozastavený erratom `ERRATUM_M011_K4_REFERENCE_GAIN_VS_ABSOLUTE_TRANSFER`;
- tvrdenie `11.5901 e-foldov K4` označuje iba `ln(T/T0)`, nie `ln T`;
- starý rekombinačný fuel-only velocity seed K4 je diagnostický, ale nie
  regulárny primordiálny mód; toto obmedzenie stanovila úplná báza K4.1;
- K4.2 obmedzila staré tvrdenie o všeobecnej K4 nestabilite aj
  subhorizontovo: na testovanej regulárnej báze bol `T_max` K4 menší než pri
  `lambda=0`; bez plnej Boltzmannovej hierarchie to ešte nie je tvrdenie o `S8`;
- historická `K5/K3a` je podľa taxonomického erráta A2-K6, nie otvorená
  dcéra K5;
- starý katalógový stav K6 `PREŽÍVA 40/100` bol obmedzený M-013 a jednotne prekalibrovaný na poslednú sekvenčne prejdenú G3=`30/100`;
- starý stav K7 `ČAKÁ` a neskorší checkpoint `PREŽÍVA K7.0 — 30/100` sú
  obmedzené jednotnou hĺbkou G2=`20/100`; body 32–42 zostávajú iba intra-G3 checkpointy;
- všetky `PASS` tvrdenia starého A2-K11 skriptu 45 sú obmedzené jeho
  samostatným auditom.

Podrobné základy zostávajú v zrozumiteľnom katalógu a v jednotlivých
rozsudkových súboroch. Aktuálnu retrospektívu určuje
`Audit/A2_K1_K5_RETROSPEKTIVNY_AUDIT_MAX_HLBKY_ROVNIC_VYPOCTOV_A_ROZSUDKOV.md`.





