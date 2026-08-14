# Audit pôvodu kotvy `H0 = 66.37 km/s/Mpc`

**Task ID:** `V318-PT1-H0-LINEAGE-20260728`  
**Stav:** `PASS_STATIC_LINEAGE / REVIEW_NUMERICAL_SENSITIVITY_NOT_RUN`  
**Rozsah:** iba historické skripty 08, 09 a 17; bez Python behu

**Poznámka k názvu súboru:** reťazec `DRAFT` v ceste je zachovaný kvôli
stabilite odkazov. Obsah bol po nezávislom audite autoritatívne uzavretý;
nejde o tiché premenovanie historického artefaktu.

## Predbežný výsledok

Historické `H0 = 66.37 km/s/Mpc` nie je v preskúmanom reťazci samostatná
bezparametrická predikcia. Je to výsledok inverzie modelového backgroundu
voči **syntetickej uhlovej kotve**, ktorú si kód najprv vytvorí z
referenčného plochého `LambdaCDM` s pevným `h = 0.673`.

Preto sa zatiaľ smie nazývať iba:

```text
legacy conditional background inversion relative to an h=0.673 LCDM anchor
```

Nie je to priamy CMB likelihood ani nezávislé odvodenie `H0` zo
substrátovej fyziky teórie.

## Presná proveniencia

### Skript 08

1. Nastaví `h_ref = 0.673`.
2. Pri tomto vstupe vypočíta `rs_ref` a `DM_ref`.
3. Definuje `theta = rs_ref / DM_ref`.
4. Funkcia `solve_h(theta)` túto syntetickú hodnotu invertuje späť na `h`.
5. Vetva pary mení `extra_r`, ale drží rovnakú syntetickú `theta`.

Reprodukcia `h_back = 0.673` je preto užitočný numerický round-trip, nie
nezávislý observačný test.

### Skript 09

1. Globálna `theta_target` je na začiatku `None`.
2. Pri prvom volaní sa skonštruuje z `r_s(0.673, 0)` a vzdialenosti plochého
   `LambdaCDM` s `h0 = 0.673`.
3. Pre zvolené `Delta N_eff` sa vytvorí `DM_target = r_s/theta_target`.
4. `anchor(...)` bisekciou hľadá `h`, ktorého modelová vzdialenosť sa rovná
   tomuto cieľu, a súčasne upravuje `Omega_m0`, aby držala fyzickú hustotu
   `omega_m = Omega_m h^2 = 0.1430` pri rekombinácii.

Skript teda `H0` numericky rieši, ale podmienene voči referenčnej
kalibrácii; nevkladá priamo nameranú `theta_*` ani jej neistotu.

### Skript 17

Skript 17 reprodukuje rovnakú architektúru:

- `flat_theta_target()` používa `h = 0.673`, `Delta N_eff = 0` a ploché
  `LambdaCDM`;
- `THETA_TARGET` je výsledok tejto internej konštrukcie;
- `anchor()` hľadá `h`, pričom používa `Delta N_eff = 0.0535` a požaduje
  `D_M = r_s/THETA_TARGET`.

Jeho kontrola `H0 približne 66.37` overuje reprodukciu historickej pipeline,
nie zhodu s pôvodnými CMB dátami.

Súbor zároveň obsahuje `66.373` v tabuľke historicky hlásených comparatorov.
Výpočtová vetva `anchor()` túto tabuľku nepoužíva na riešenie `h`; používa ju
iba následné porovnanie. Presné tvrdenie preto nie je „v súbore nie je
hardcode“, ale „hardcoded comparator nie je vstupom bisekcie“.

## Čo je a nie je vstup

| Veličina | Úloha v historickej pipeline |
|---|---|
| `h=0.673` | pevný referenčný vstup použitý na vytvorenie syntetickej kotvy |
| `theta_target` | odvodená interná kalibračná hodnota, nie priamo načítané pozorovanie |
| `omega_m=0.1430`, `omega_b=0.02237` | pevné fyzické hustoty prevzaté ako vstupy |
| `Delta N_eff` | scenárový vstup meniaci skorú radiáciu a zvukový horizont |
| modelové `h` | numericky invertovaný výstup pri vyššie uvedených podmienkach |
| `H0=66.37` | podmienený modelový výstup, nie voľne vložená konštanta v `anchor()` |

Teda tvrdenia „`H0` je iba hardcoded output“ a „`H0` je úplne nezávislá
predikcia“ sú obe príliš silné. Presná klasifikácia je **podmienená
inverzia**.

## Vzťah ku chybe `K_MPC=0.05`

V preskúmaných skriptoch 08, 09 a 17 sa Fourierov mód `k` ani `K_MPC`
nenachádza. Táto legacy background pipeline preto netrpí priamo tým, že by sa
globálny `H(a)` menil podľa evolvovaného perturbatívneho módu.

To však neuzatvára K4/G8. Skripty integrujú fenomenologický trojzložkový
background spätne od dneška a nepoužívajú ešte neuzavretú univerzálnu K4
normalizáciu `A_f`. Výsledok môže slúžiť na audit dopadu zmeny starého
release predpokladu, nie ako konečný K4 background.

## Oprava `r_d` verzus `r_s(z_star)`

Skripty integrujú zvukový horizont po pevnú rekombinačnú hranicu
`z_star=1089.9`. Počítaná veličina je preto `r_s(z_star)`, nie drag-epoch
sound horizon `r_d`. Staršie znenie v PT1 návrhu, ktoré žiadalo `r_d`, je
týmto auditom obmedzené. `r_d` by vyžadovalo samostatný drag/recombination
contract.

## Je trojbodový PT1 test zmysluplný?

Predbežne áno, ale iba na úzku otázku:

> O koľko sa zmení historický podmienený bod, keď v tej istej legacy
> kalibrácii nahradíme `Delta N_eff=0.0535` hodnotami `0.02675` a `0`?

Taký výpočet môže rozhodnúť, či PT1 odvolanie pary materiálne zasiahne starý
riadok `H0=66.4`. Nemôže vytvoriť novú verejnú predikciu `H0`, kým nebude
uzavretý K4 background a použitá riadne zdokumentovaná observačná kotva alebo
likelihood.

Tri sample body samy nedokazujú spojitú obálku ani monotónnosť. Výstup preto
musí niesť názov `THREE_POINT_LEGACY_ANCHOR_SENSITIVITY`; „envelope“ je
prípustné iba s výslovným slovom `sampled` alebo po samostatnom dôkaze medzi
bodmi.

## Riziká, ktoré musí budúci výpočet explicitne niesť

1. `theta_target` je syntetická a dedí referenčné `h=0.673`.
2. `z_star=1089.9`, `omega_m`, `omega_b` a zjednodušený zvukový horizont sú
   zmrazené vstupy bez propagácie neistôt.
3. Skripty 09/17 pred rekombináciou zanedbávajú palivo a používajú
   štandardizovaný `r_s`; to je modelový predpoklad, nie dokázaná K4 veta.
4. Trojbodová obálka neobsahuje parameter covariance ani CMB likelihood.
5. Monotónnosť `H0(Delta N_eff)` je fyzikálne očakávanie, nie dôvod meniť
   výsledok alebo prahy po behu.
6. Historické bisekcie neoverujú zmenu znamienka na brackete, vnútorná
   normalizácia `Omega_m0` má fixných šesť iterácií bez rezídua a integračné
   chyby kvadratúry sa zahadzujú.
7. Floor `max(...,1e-30)` môže maskovať záporný background; successor musí
   reportovať positivity a každú aktiváciu flooru.

## Odporúčaný najmenší successor

Po nezávislom potvrdení lineage vytvoriť nový versioned base a tenký runner,
ktoré pre tri zmrazené hodnoty `Delta N_eff`:

- použijú jeden explicitne pomenovaný legacy `theta` anchor;
- nebudú volať S8, drag, curvature ani pseudo-`chi2`;
- publikujú `H0`, `r_s`, `D_M`, rezíduum kotvy a všetky pevné vstupy;
- majú interný limit, vonkajšiu rezervu, null test a grid/step convergence;
- označia výsledok výhradne ako
  `THREE_POINT_LEGACY_ANCHOR_SENSITIVITY`.

Kanonickým formulačným predkom má byť flat vetva skriptu 09. Skript 17 je
reprodukčný comparator a jeho `r_s` implementácia nie je identická: používa
kandidátne `h` a podporuje krivosť. Successor nesmie tieto vetvy potichu
zmiešať.

## Nezávislý audit a prijatie

Read-only rola `physics_track_auditor` (`/root/h0_lineage_audit`, config SHA
`0DBB0E...304E`) overila všetkých päť zmrazených vstupov a odporučila:

- potvrdiť syntetický pôvod `theta_target`;
- klasifikovať `H0` ako podmienenú numerickú inverziu;
- obmedziť k-nezávislosť iba na implementačný scope 08/09/17;
- povoliť trojbodový krok iba ako sampled legacy-impact diagnostiku;
- pred kódom zmraziť formulačný contract, numerické guardy a `NO_SIGN_GATE`.

Hlavný orchestrátor odporúčanie prijíma. Ide o lineage/classification PASS,
nie o fyzikálny, numerický, likelihood ani release PASS.

## Nonclaims

- Žiadny Python proces nebežal.
- Nevznikol nový interval `H0`.
- Nezmenil sa PT1/PT2 release verdict.
- Nezmenil sa stav, skóre ani hĺbka A2-K4.
- Nebola potvrdená univerzálna K4 normalizácia ani G8.
- Nebola numericky reprodukovaná hodnota `66.37` ani vypočítané tri body.
