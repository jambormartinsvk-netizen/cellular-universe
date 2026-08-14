# A2-K12.0 — dvojzložkový popol s opačnými skalárnymi nábojmi

**Dátum:** 2026-07-14  
**Rodičovská koľaj:** A2-K12  
**Stav rodiča:** `PREŽÍVA IBA PRVÚ ANALYTICKÚ BRÁNU — 25/100`  
**Aktívna podkoľaj:** `K12-K3 — symetrická produkcia párov + opačné náboje`  
**Rozsah:** akcia/ledger, backgroundový tok a kvázistatická silová matica;
nejde o Boltzmannov výpočet, likelihood ani predikciu `S8`.

## 1. Rozsudok ľudskou rečou

Áno, dva druhy popola s opačným skalárnym nábojom sú fyzikálne mysliteľný
mechanizmus. Rovnaké druhy sa skalárnou silou priťahujú a opačné druhy sa
odpudzujú. To môže viesť k rozdeleniu, fragmentácii a menšej hustote jadier
niektorých halo.

Opačné náboje však samy osebe **nevytvárajú energiu popola**. Určujú silu a
výmenu energie s časovo premenným skalárnym poľom. Pri presne rovnakom
množstve oboch druhov sa ich skalárne backgroundové prenosy navzájom zrušia.

Ak palivo skutočne vytvára pár `c+ + c-`, energia oboch nových častíc môže
pochádzať z paliva. Vtedy však čistý prenos energie zabezpečuje **produkčný
operátor**, nie samotné opačné náboje. Ide o novú koľaj spájajúcu produkciu
počtu častíc s dvojzložkovou skalárnou interakciou.

## 2. Minimálny kovariantný model

Kanonický kandidát má dva druhy popola s

```text
beta_+ = +beta,
beta_- = -beta,
A_+(varphi)=exp(+beta varphi),
A_-(varphi)=exp(-beta varphi).
```

Schematicky

```text
S = integral sqrt(-g) [M_Pl^2 R/2 - (partial phi)^2/2 - V(phi)]
    + S_+[A_+^2(phi) g, psi_+]
    + S_-[A_-^2(phi) g, psi_-]
    + S_f + S_creation.
```

V znamienkovej konvencii lokálneho auditu K5 sú backgroundové rovnice

```text
rho_+' + 3 Hc rho_+ = + beta varphi' rho_+ + C_+,
rho_-' + 3 Hc rho_- = - beta varphi' rho_- + C_-,
```

kde `C_+` a `C_-` sú prípadné zdroje skutočnej produkcie z paliva. Pre
`rho_c=rho_+ + rho_-` a `Delta rho=rho_+ - rho_-` preto

```text
rho_c' + 3 Hc rho_c = beta varphi' Delta rho + C_+ + C_-.
```

Celková energia a hybnosť sa zachová, iba ak palivo a skalár dostanú presne
opačné zdroje. Tento ledger ešte nenahrádza mikroskopický produkčný operátor.

## 3. Prvá stena: symetria ruší aj skalárny prenos energie

Definujme nábojovú asymetriu

```text
epsilon = (rho_+ - rho_-)/(rho_+ + rho_-).
```

Bez samostatnej produkcie platí

```text
Q_scalar,total / Q_scalar,single = epsilon.
```

Pre rovnaké množstvá `epsilon=0`:

- celkový skalárny prenos energie je nulový;
- backgroundová piata sila je samoregulačne tienená;
- pôvodný nenulový tok palivo -> popol z A1 sa tým nereprodukuje.

Pre `epsilon=1` sa požadovaný tok pri pôvodnom `beta` obnoví, ale zostane iba
jeden druh a model sa vráti k mŕtvej K5. Zníženie `epsilon` a súčasné zvýšenie
`beta` tak, aby `beta epsilon` zostalo konštantné, zväčšuje silový člen ako
`beta^2/epsilon^2`; nie je to bezplatné riešenie.

## 4. Druhá stena: nejde o obyčajný tlak alebo pokojný rozptyl

V ľahkom skalárnom limite a v lokálnej normalizácii K5 je sila medzi druhmi

```text
mu_ij = G_ij/G = 1 + 2 beta_i beta_j.
```

Pre `beta_+=+beta` a `beta_-=-beta`:

```text
mu_same     = 1 + 2 beta^2,
mu_opposite = 1 - 2 beta^2.
```

Pri rovnakých hustotách má vážená silová matica dva vlastné módy:

```text
delta_total  ~ (delta_+ + delta_-),  eigenvalue = 1,
delta_charge ~ (delta_+ - delta_-),  eigenvalue = 2 beta^2.
```

Prvý mód rastie na tejto bráne ako obyčajná gravitácia: presná symetria teda
**automaticky nezníži lineárne `S8`**. Druhý mód oddeľuje oba druhy. Nie je to
stabilný tepelný tlak, ale nábojová segregácia: jeden druh môže vytvoriť
prehustenie tam, kde druhý vytvorí podhustenie.

## 5. Čísla pre väzbu pôvodnej K5

Skript 65 pri `beta=1.52883` dáva

| Veličina | Výsledok |
|---|---:|
| `mu_same` | `5.6746423378` |
| `mu_opposite` | `-3.6746423378` |
| symetrický celkový mód | `1.0000000000` |
| nábojovo-separačný mód | `4.6746423378` |
| symetrický čistý skalárny tok | `0` |

Záporné `mu_opposite` znamená, že skalárne odpudzovanie opačných druhov je
silnejšie než ich vzájomná bežná gravitácia. Súčasne sa rovnaké druhy veľmi
silno priťahujú. Preto je pri tomto pracovnom bode riziko segregácie červené.

## 6. Podkoľaje

| Podkoľaj | Mechanizmus | Stav | Max. hĺbka | Dôvod alebo stena |
|---|---|---|---:|---|
| K12-K1 | presne rovnaké hustoty, opačné konformné náboje, bez produkčného operátora | `MŔTVA M-016` | `25/100` | symetria dá `Q_scalar,total=0` a celkový lineárny mód `mu=1`; nesplní nenulový tok ani zníženie `S8` |
| K12-K2 | asymetrické hustoty, prenos iba cez ten istý skalár | `OTVORENÁ — ČERVENÁ` | `25/100` | nenulový tok sa vracia spolu s netienenou silou; treba úplný časový no-go alebo nájsť povolené okno |
| K12-K3 | palivo produkuje symetrické páry `c+ c-`; náboje riadia ich následnú silu | `AKTÍVNA HYPOTÉZA` | `20/100` | čistý tok môže byť `C_++C_->0`, ale chýba lokálny produkčný operátor, šum, počiatočné módy a test segregácie |

M-016 zabíja iba presne definovanú K12-K1. Nezabíja K12-K2 ani K12-K3.

## 7. Čo literatúra už overila a čo nie

Modely s dvoma CDM druhmi a opačnými väzbami na skalár sú známa trieda
multi-coupled dark energy. Publikované práce ukazujú:

- potlačenie účinku väzby na backgrounde a v lineárnom adiabatickom móde;
- súčasnú príťažlivú a odpudivú piatu silu;
- pri väčších väzbách nelineárnu segregáciu, fragmentáciu halo a zmeny
  malomierkového výkonu.

To podporuje fyzikálnu zmysluplnosť mechanizmu, ale **nedokazuje**, že náš
pracovný bod zníži `S8` z `0.87` na `0.82`. Publikovaný malomierkový útlm sa
nesmie zameniť za výpočet `sigma8` bez vlastnej Boltzmannovej a nelineárnej
pipeline.

Primárne opory:

- [Baldi 2012 — self-regulating multiple dark matter](https://arxiv.org/abs/1204.0514)
- [Baldi 2012 — nonlinear structure formation](https://arxiv.org/abs/1206.2348)
- [Baldi 2014 — halo segregation and fragmentation](https://arxiv.org/abs/1403.2408)

## 8. Ďalšia brána K12-K3.1

1. Odvodiť lokálny operátor `fuel -> c+ + c-`, nie iba vložiť `C_+=C_-/2`.
2. Dokázať celkové `nabla_mu T_total^(mu nu)=0` vrátane skalára a paliva.
3. Odvodiť kontinuity a Eulerove rovnice pre celkový aj nábojový mód.
4. Otestovať ghost, gradient, superhorizontový izokurvatúrny mód a high-k mód.
5. Predregistrovať prípustný rozptyl `rho_+/rho_-`; presná rovnosť nesmie byť
   iba numericky nanútená.
6. Až potom spustiť lineárny rast a Boltzmannovu `S8` bránu.

## 9. Reprodukcia

- `scripts/65_script_A2_K12_two_opposite_charge_ash_analytic_gate.py`
- `scripts/OUTPUT_A2_K12_0_65.md`

