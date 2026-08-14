# KMPC-033 — výsledok a audit S-C0 lower-moment coefficient passportu

**Dátum:** 2026-07-16  
**Autorita rozsudku:** hlavný fyzikálny audítor  
**Autoritatívny rozsudok:**
`PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY`  
**K4:** `LIVE / 60/100`; bez zmeny  
**P5:** `3.5/6`; bez zmeny  
**Release/Zenodo/predikcie:** `NONE / NONE / NO_CHANGE`

## 1. Dva zachované behy

### KMPC-032 — technická chyba bez fyziky

Runner 276 prešiel compile/help/smoke, ale prvý skutočný M1 skalár
`numpy.float64` poslal do `SymPy Rational` text s wrapperom
`np.float64(...)`. Audit zastal pred prvou S-C0 identitou. Failure JSON

```text
RUN_KMPC_032_P5_3G7_S_C0_COEFFICIENT_PASSPORT_TECHNICAL_FAILURE.json
SHA-256 51C7B32B84F498ACD9CEFD7BC72D546D87F1DDCBC4C2BC189A02E1036991EA03
```

je immutable dôkaz PF-069. Runner 276 a V1 implementácia zostávajú
`DO_NOT_RUN_AUDIT_TECHNICAL`; chyba nezabila S-C0, P5 ani K4.

### KMPC-033 — úzky PF-069 RERUN1

Overlay skonvertoval iba konečný `numbers.Real` cez builtin `float` a po
behu obnovil pôvodný helper. Nezmenil rovnice, váhy, supporty, módy,
prahy ani zdrojové stavy. Výsledok

```text
RUN_KMPC_033_P5_3G7_S_C0_COEFFICIENT_PASSPORT_RERUN1.json
SHA-256 4CED9D48FD9866113739580E20F69E8122D70204E37C055251C8A49B3E0CFE8C
```

má `all_checks_pass=true`, všetkých 20 booleanov `true`, 10/10 chybných
fixtures odmietnutých a žiadny failure artefakt. Devätnásť kontrol patrí
pôvodnému passportu; dvadsiata je `PF069_overlay_restored`. Tým sa opravuje
nepresný pomocný počet 19 v jednom read-only dokumentačnom posudku.

## 2. Presné váhy a päť skutočných M1 vstupov

Zo zmrazených desatinných konvencií `alpha=0.2271`, `N_nu=3.046` a
`N_s=0.0535` vznikli presné racionálne váhy v rámci tejto konvencie:

```text
R_gamma = 20000000/34077929
R_nu    = 13834932/34077929
R_s     =   242997/34077929
R_fs    = 14077929/34077929
```

Presnosť tu neznamená fundamentálne odvodenie neutrínovej termodynamiky;
znamená presnú algebru nad zmrazenými vstupmi.

Runner skutočne načítal ukotvené M1 stavy pre `AD, CDI, BI, NID, NIV` pri
`k=0.05 Mpc^-1`, nominal. Každý mal `rank=unknowns=76`, presnú M1 kotvu a
metadata PASS. Kontrolovalo sa 21 uložených koeficientov na mód, teda sedem
integer powers pre každý z `delta_fs`, `U_fs`, `sigma_fs`.

| Mód | condition | driver scaled residual | holdout scaled residual |
|---|---:|---:|---:|
| AD | 1924.31 | `7.97e-15` | `6.07e-15` |
| CDI | 340.32 | `1.13e-15` | `9.21e-16` |
| BI | 340.32 | `2.28e-15` | `1.64e-15` |
| NID | 1381.45 | `1.14e-14` | `2.75e-15` |
| NIV | 2084.21 | `2.80e-15` | `3.10e-15` |

## 3. Čo presne prešlo

V podmienenej vetve `Y_nu=Y_s=Y_fs` vyšli ako presné nuly:

- lift/collapse každého skutočného lower-moment M1 koeficientu;
- symbolická mapa každého registrovaného extended slotu;
- vážené zdroje hustoty, hybnosti a shear;
- coefficient-wise rovnosť collisionless continuity, Euler a shear mapy;
- správna NID/NIV kompenzácia s `R_fs`;
- odmietnutie nesprávnej kompenzácie s `R_nu`, ktorej rezíduum je úmerné
  nenulovému `R_s=242997/34077929`;
- kolektívny limit `R_s→0`, v ktorom `R_fs=R_nu`;
- generické komutovanie lineárneho collisionless operátora pre `l=3,4` s
  váženým collapse.

Nezávislý contract odmietol rovnakou produkčnou validačnou cestou všetkých
10 fixtures: chýbajúci mód, AD/J4 support vložený NID, chýbajúci shear,
holdout medzi drivermi, `Y_s!=Y_nu`, nesprávne NID a NIV váhy, nenulový
`Q_s`, weight-only tautológiu bez coefficient mapy a priamy script-84
`q→U` prenos.

## 4. Čo je na výsledku podmienené

Rovnosti nie sú nezávislým odvodením fyziky pary. `nu`, `steam` a `fs`
dostali ten istý stav a ten istý lineárny operátor, preto ich row rovnosť je
nutný dôsledok hypotézy S-C0. Symbolické extended slots dokazujú mapu pre
ľubovoľný koeficient, nie existenciu solved M3 koeficientu. Exact
`Rational(repr(float))` robí presnú kópiu numerickej hodnoty, nie analyticky
presné riešenie M1 rovníc.

Automatizovaný support guard priamo porovnal primary support, counts a
`leading_j`, ale neporovnal samostatne celý extended tuple s pravidlom
`extended=(lo,hi+2)`. Manuálny audit potvrdil správne hodnoty:

| Mód | primary | extended | F0 primary/ext | M3 primary/ext |
|---|---|---|---:|---:|
| AD | `[0,2]` | `[0,4]` | 6/10 | 39/65 |
| CDI | `[0,1]` | `[0,3]` | 4/8 | 26/52 |
| BI | `[0,1]` | `[0,3]` | 4/8 | 26/52 |
| NID | `[0,3]` | `[0,5]` | 8/12 | 52/78 |
| NIV | `[-1,2]` | `[-1,4]` | 8/12 | 52/78 |

Pred CDI C1 sa musí pravidlo `hi+2` aj odvodenie counts kontrolovať
programovo, nie iba duplikovanými konštantami.

## 5. Povinné nonclaims

Tento PASS nedokazuje:

1. pôvod, produkčný kernel, thermalizáciu alebo decoupling pary S-M;
2. prečo majú para a neutrína rovnaké perturbácie;
3. nulovosť interných `nu-steam` density/velocity módov — iba ich nastavil;
4. úplnú sedemmódovú species-resolved bázu;
5. skutočné päťmódové `F_l>=3` coefficients, closure alebo konvergenciu;
6. full `N_s→0` kozmologický solve; iba algebraický split limit;
7. finite opacity, ODE stabilitu, CMB, BBN, G8/G9, CLASS, S8 alebo H0;
8. CDI/BI/NID/NIV primary→extended M3 coverage, iné `k` alebo varianty;
9. nový parameter, prediction-table zmenu, bod, hĺbku alebo release trigger.

Výsledok musí vždy niesť label
`HIGHER_MULTIPOLE_COEFFICIENTS_NOT_IN_SCOPE`.

## 6. Nezávislé posudky a hlavný rozsudok

- fyzikálny read-only auditor potvrdil konzistentnosť iba ako zmenu
  reprezentácie spoločného collisionless sektora a odmietol extrapoláciu na
  pôvod/dynamiku pary;
- matematický read-only auditor potvrdil hashe, exact váhy, päť reálnych M1
  vstupov, PF-069 delta-only charakter a JSON; upozornil na podmienenosť
  identít a chýbajúci priamy extended-tuple guard;
- dokumentačný/release steward potvrdil nulový score, depth, prediction,
  Zenodo a release trigger.

Hlavný audítor preto udeľuje iba

```text
PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY
```

S-C0 matematický lower-moment embedding je živý a jeho double-counting
blocker je uzavretý. Fyzický S-M blocker, full hierarchy a mode coverage
zostávajú otvorené. K4 ani P5.3 tým nie sú dokončené.

## 7. Počítadlá a ďalší krok

S-C0 technický ledger má dva historické balíky. Vecne úspešný KMPC-033
vynuloval active counter z `1/10` na `0/10`; PF-069 história zostáva.

Ďalší beh nebude opak KMPC-033. Predregistruje sa CDI C1 pri
`k=0.05 Mpc^-1`, nominal, primary `[0,1]` verzus extended `[0,3]`,
`leading_j=1`. Musí samostatne preveriť M3 rank, drivers, nezávislé `00/0i`
holdouty, forbidden orders, `U_c` regularitu a čistý added-tail. S-C0
passport sa použije iba ako conditional split guard, nie ako náhrada týchto
brán.

