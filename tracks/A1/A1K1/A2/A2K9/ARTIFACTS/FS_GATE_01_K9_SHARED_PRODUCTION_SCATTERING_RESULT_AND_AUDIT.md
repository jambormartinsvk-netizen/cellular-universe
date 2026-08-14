# FS-GATE-01 — K9: spoločná cold produkcia a lineárna momentum relaxácia

**Dátum:** 2026-07-16  
**Autorita verdiktu:** hlavný orchestrátor  
**Rozsah:** momentová a Markovská realizovateľnosť jedného lokálneho
gain–loss generátora; presný zmrazený A1-K1 background; lineárny rád porúch  
**Skórovací účinok:** žiadny; hĺbka zostáva `10/100 = G1`  
**Numerický beh:** nebol potrebný; rozhodujú momentové identity, pozitivita
gain–loss semigrupy a prahový fázový priestor

## 1. Otázka po scoped smrti warm K8

Audit K8 dokázal:

```text
exact A1 + rovnaké rho_c,q + pozitívny masívny popol
=> P_c=0 => cold podpora p=0.
```

Cold source-only uzáver sa však zlieva s A2-K1 a dedí `M-009`. K9 má byť
odlišná iba vtedy, ak ten istý lokálny mechanizmus okrem cold produkcie
určí aj pasívny lineárny prenos hybnosti bez druhého fitovaného drag
parametra.

Hľadaný behaviorálny bod preto musí spĺňať naraz:

```text
background:
  S_n = q/m_c,
  q = Gamma rho_f,
  P_c = 0,
  pi_c = 0,
  Q_el^0 = 0;

linear order:
  F_c^i = -K (v_c^i-v_f^i),
  K >= 0,
  F_f^i = -F_c^i;

common limits:
  coupling -> 0 => S_n,K,noise -> 0,
  rho_f -> 0 => S_n,K -> 0.
```

Ohrev z pasívneho drag môže byť `O(|v_c-v_f|^2)`: nemusí meniť FLRW ani
lineárny energetický moment, ale na druhom ráde musí dostať presnú reakciu.

## 2. Explicitný Markovský momentový svedok

Nech `delta_u(p)` je normalizovaná delta miera na mass shell pri
`p^mu=m_c u^mu`. Definujeme jeden lokálny gain–loss generátor

```text
C_c[f_c](p)
= S_n delta_uc(p)
+ nu [n_c delta_uf(p)-f_c(p)].
```

Prvý kanál produkuje cold popol v okamžitom rámci existujúceho popola.
Druhý kanál zachováva počet a Markovsky resetuje bulk hybnosť smerom k
rámcu paliva. Oba kanály sú súčasťou jedného efektívneho generátora; to
ešte neznamená, že už boli odvodené z jedného QFT maticového elementu.

### Nultý moment

Pretože `integral delta_u dPi=1` a `integral f_c dPi=n_c`, platí

```text
integral C_c dPi = S_n.
```

Voľba `m_cS_n=q` presne reprodukuje A1 rest-mass source. Relaxačný kanál
počet nemení.

### Prvý moment

Pre cold `f_c=n_c delta_uc` je relaxačný moment na lineárnom ráde

```text
F_c^mu
= m_c nu n_c h_c^mu_nu (u_f^nu-u_c^nu)
= -K (v_c^mu-v_f^mu),

K = nu rho_c >= 0.
```

Znamienko je pasívne: relatívna rýchlosť sa tlmí. Presná momentová reakcia
sa definuje `Q_f^mu=-Q_c^mu`; bez nej svedok neplatí.

### Jeden konkrétny regularitný bod bez nového čísla

Ako dôkaz neprázdnosti behaviorálneho priestoru možno zvoliť

```text
S_n = Gamma rho_f/m_c,
nu  = Gamma delta rho_f/(rho_f+rho_c),
K   = Gamma delta rho_f rho_c/(rho_f+rho_c),
delta = 1+w_f > 0.
```

Tento bod používa iba už existujúce `Gamma=lambda H0`, `delta` a lokálne
hustoty. Dáva

```text
K/q = delta rho_c/(rho_f+rho_c),
```

bez ďalšieho konštantného fitu. Má spoločný nulový limit `Gamma->0`, pri
`rho_f->0` mizne zdroj aj drag, pri `rho_c->0` je `K->0` a koeficient
`K/rho_c` zostáva konečný. Reakčný koeficient
`K/(delta rho_f)=Gamma rho_c/(rho_f+rho_c)` zostáva konečný aj pre
`delta rho_f->0`.

Tento konkrétny pomer je **konštitutívny svedok existencie**, nie odvodená
predikcia bunkovej mikrofyziky. Nesmie sa neskôr fitovať na `S8`; buď ho
odvodí spoločná interakcia, alebo sa nahradí iným vopred odvodeným pomerom.

## 3. Pozitivita, tlak a noise

Pre `nu>=0` má relaxačná časť riešenie v tvare nezápornej kombinácie
pôvodnej miery a cold gain mier. Preto zachováva pozitivitu distribúcie.

Na presnom FLRW bode `u_f=u_c` platí

```text
C_el=0,
P_c=0,
pi_c=0,
heat_el=0.
```

Pri malej relatívnej rýchlosti je deterministický momentum transfer
`O(v_rel)`, zatiaľ čo práca/ohrev je `O(v_rel^2)`. Warm K8 no-go sa preto
na tento cold lineárny svedok nevzťahuje.

Generátor možno realizovať Poissonovými produkčnými a reset jump udalosťami.
Ich noise kovariancia má tvar

```text
N^{ab} = sum_r rate_r Delta X_r^a Delta X_r^b,
```

a je pozitívna semidefinitná, pretože pre každý `z_a`

```text
z_a N^{ab} z_b = sum_r rate_r (z.Delta X_r)^2 >= 0.
```

Na cold backgrounde zostáva produkčný number shot noise; reset bez
relatívnej rýchlosti nemá momentum kick. Pri konečnej teplote bathu by FDT
vyžadovala momentum diffusion a tá by generovala disperziu/tlak. Svedok je
preto iba zero-temperature alebo absorbing-response hranica, nie dôkaz
prípustného teplého fuel bathu.

## 4. Čo je a nie je dokázané

**Autoritatívny čiastkový verdikt:**

```text
NONEMPTY_MARKOV_MOMENT_CLASS / REVIEW
```

Dokázané je, že cold produkcia, nulový FLRW ohrev a pasívny lineárny drag
nemajú algebraický ani pozitivitný rozpor. Existuje explicitný lokálny
momentový/Markovský svedok so spoločným nulovým limitom a PSD jump noise.

Nie je dokázané:

- že oba kanály pochádzajú z jedného Lorentz-invariantného maticového
  elementu alebo jednej bunkovej mikrofyziky;
- unitárnosť, crossing ani kompletný fuel distribučný kernel;
- detailed balance/chemická afinita near-vacuum paliva;
- konečno-teplotný FDT uzáver bez vzniku `P_c>0`;
- mikrofyzické odvodenie zvoleného `K/q`;
- superhorizontová, subhorizontová ani high-`k` stabilita;
- zníženie `S8` alebo observačný fit.

Preto K9 nedostáva G2 PASS ani body. Existencia momentového svedka však
znamená, že rodičovský priestor nemožno vyhlásiť za prázdny iba z A1
backgroundu.

## 5. Prečo „jeden generátor“ ešte nie je „jeden mikrofyzický proces“

Starší audit správne ukázal, že pri rovnakom `S_n` možno meniť lineárny
momentum moment bez zmeny backgroundu. Všeobecne

```text
K/S_n = m_c [nu n_c/S_n]
```

nie je určené samotným A1 tokom, pozitivitou ani conservationom. Zapísanie
dvoch voľných funkcií do jednej rovnice by nebolo odvodením.

Plný K9 kandidát musí zadať jednu lokálnu akciu alebo maticový element
`M(g,m_i,...)` a nezávisle z neho vypočítať

```text
S_n = integral C_prod[|M|^2],
nu  = transportný moment C_scat[|M|^2].
```

A1 tok môže fixovať spoločný coupling, ale potom musí byť `K/S_n`
predikciou fázového priestoru, hmôt a stavov, nie druhým fitom.

Čisto elastické `2->2` nemôže byť jediným kanálom, lebo zachováva počet.
„Jeden proces“ preto znamená jednu mikrofyzickú interakciu alebo úplný
collision operator s number-changing aj number-conserving kanálom, nie
doslova jednu elastickú reakciu.

## 6. Scoped mŕtve podtriedy

### K9-1TO2-EXACT-THRESHOLD-FINITE-RATE

Pre obyčajný hladký konečný maticový element má dvojtelesová produkčná
šírka pri prahu fázový faktor

```text
Gamma_1to2 proportional
|M|^2 sqrt(1-4m_c^2/M_parent^2).
```

Presne cold produkty vyžadujú `M_parent=2m_c`, kde fázový priestor a šírka
zaniknú. Nad prahom je šírka nenulová, ale `p_B>0` a vznikne warm tlak,
ktorý bez ďalšieho procesu poruší presný A1.

**Scoped verdikt:**
`EMPTY_CERTIFIED_SCOPE / STOP K9-1TO2-EXACT-THRESHOLD-FINITE-RATE`.

Tento STOP neplatí automaticky pre coherent zero-mode konverziu,
kondenzátový/kolektívny proces, singular/resonant many-body kanál alebo
explicitnú coldification. Každý z nich však musí dostať vlastný ledger.

### Ďalšie vylúčené správanie

- iba elastické `2->2`: `S_n=0`, teda nereprodukuje A1;
- `C_el=0`: zlieva sa s cold K8/K1 a dedí `M-009`;
- nezávislé post-data `Gamma` a `gamma_drag`: leží mimo definície K9;
- `K<0`: anti-damping a záporná entropická produkcia;
- finite-temperature drag bez diffusion/noise: porušuje FDT;
- exact termálna rovnováha s jednosmerným `S_n>0`: chýba chemická afinita;
- nenulový FLRW elastický ohrev alebo chýbajúca fuel reakcia: mení A1 alebo
  porušuje conservation.

## 7. Najbližší fyzikálny kandidát

Pracovné označenie v tomto audite:

```text
K9-CTLR — Cold-Threshold Local Response.
```

Nie je to G2 podkoľaj ani nový parameter. Je to cieľ pre mikrofyzické
hľadanie odvodený priamo z dôvodov smrti K8:

1. lokálny metastabilný/neekvilibračný fuel stav;
2. cold alebo coherent number-changing kanál s `q=m_cS_n`;
3. tá istá interakcia generuje elastický momentum response;
4. `K=(B/A)q/m_c` bez druhého coupling fitu;
5. nulový FLRW heat a tlak, ohrev až `O(v_rel^2)` s presnou reakciou;
6. noise/diffusion kompatibilné so stavom bathu;
7. regularita pri `rho_f,rho_c,delta -> 0`.

**Ďalšia brána:** nájsť explicitnú lokálnu akciu alebo úplný collision
kernel, ktorý dá kladné konečné `A,B` a pomer `B/A`. Bez neho zostáva
`K9-CTLR` iba constraint-derived návrhový cieľ a K9 na G1.

## 8. Obmedzenie starších formulácií

`Audit/A2_K9_1_G2_SINGLE_OPERATOR_MOMENT_AUDIT.md` ostáva správny v tom, že
slovo „jeden operátor“ neurčuje `K/S_n`. Tento audit ho neprepisuje, ale
dopĺňa:

- momentová trieda nie je prázdna;
- konkrétny regularitný constitutive bod sa dá zapísať bez nového čísla;
- tento bod ešte nie je spoločnou mikrofyzickou predikciou;
- bežný smooth `1->2` exact-threshold finite-rate pokus je mŕtvy.

## 9. Vstupy a auditná stopa

| Vstup | SHA-256 |
|---|---|
| `Questions/A2_K9_1_PREREGISTRATION_SINGLE_PRODUCTION_SCATTERING_OPERATOR.md` | `2D56B2195EA5F7CA96E7C372ED1D14ED2A72CC69DD5622D07A43191A5B05F7BC` |
| `Audit/A2_K9_1_G2_SINGLE_OPERATOR_MOMENT_AUDIT.md` | `9F1C548EC5D91899664DD2FEE24A0A61000662BC60D7BFD0016B725C5287A50A` |
| `scripts/153_script_A2_K9_1_collision_moment_nonuniqueness.py` | `737FE57282EA25759225090B4454DFEEEB442116834A5FE0304669B71775B288` |
| `scripts/154_script_A2_K9_1_independent_operator_audit.py` | `8B28336226A8F3788166E9CB731C72AB8F80969D50462B8EC3C43462D5635195` |
| `scripts/155_script_A2_K9_1_manifest_sha256.py` | `902E748BF68693996789EBF41CB9CAE2FA96B8581F321B1D42E37FA047DDC121` |
| K8 pressureless-A1 audit | `F755539E88AFFACC3605867E1268F639D1322FB14B419AC93295A5CFC2B15249` |

Staré skripty 153–155 neboli znovu spustené: dokazujú nejednoznačnosť
voľného `kappa`, ktorú nový analytický výsledok nemení. Nový svedok aj
prahový STOP sú presné symbolické konštrukcie bez tolerančnej brány.
