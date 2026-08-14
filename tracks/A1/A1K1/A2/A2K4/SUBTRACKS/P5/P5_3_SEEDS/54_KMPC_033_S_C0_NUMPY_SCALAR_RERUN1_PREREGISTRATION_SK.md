# KMPC-033 — S-C0 numpy-scalar RERUN1 predregistrácia

**Dátum:** 2026-07-16  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Predchodca:** KMPC-032/PF-069  
**Technický balík S-C0:** `2`; active counter pred behom `1/10`  
**Skóre/hĺbka:** bez zmeny; K4 `LIVE / 60/100`, P5 `3.5/6`

## Povolená jediná oprava

KMPC-032 prešiel compile/help/smoke, ale prvý skutočný koeficient typu
`numpy.float64` sa pokúsil skonvertovať cez text `np.float64(...)`. RERUN1
smie zmeniť iba túto konverziu:

```text
ľubovoľný konečný numbers.Real
→ builtin float(value)
→ repr(float(value))
→ SymPy Rational
```

V1 modul a failure JSON sa nemenia. Verziovaný overlay musí pred volaním
auditu dočasne nahradiť iba helper `_q` a v `finally` obnoviť pôvodnú
referenciu. Runner zmrazí hashe V1, overlayu, nezávislého kontraktu a
všetkých priamo používaných solverových zdrojov.

## Zakázané zmeny

RERUN1 nesmie zmeniť:

- `alpha`, `N_nu`, `N_s` ani exact radiation weights;
- päť módov, supporty, 13-state/driver/holdout contract;
- skutočné M1 zdroje pri `k=0.05`, nominal;
- rovnice kontinuity, Euler, shear alebo operator `l=3,4`;
- negatívne fixtures, nulový limit, PASS/STOP hranice;
- interný limit `4.8 s`, vonkajší limit `10 s`;
- scope: vyššie multipólové coefficients ostávajú NOT IN SCOPE.

## Očakávanie

Behaviorálny smoke musí dokázať, že `float(0.125)` a
`numpy.float64(0.125)` dajú presne rovnaké `SymPy Rational(1,8)`. Potom má
plný audit buď:

- vytvoriť immutable výsledok s kandidátom
  `PASS_S_C0_LOWER_MOMENT_COEFFICIENT_LIFT_COLLAPSE_PASSPORT_ONLY`, alebo
- zachovať presný formulačný CHECK fail ako REVIEW/STOP iba pre S-C0, alebo
- pri technickej chybe vytvoriť nový failure JSON bez fyzikálneho verdiktu.

Vecný úspešný výsledok vynuluje active counter na `0/10`; compile/help/smoke
ho nevynulujú.

## Zdroje pred prvým Python procesom

| Súbor | SHA-256 |
|---|---|
| `s_c0_coefficient_passport_v2_numpy_scalar.py` | `06EE03C939FBCCFA6FA130421EEF98D0B8CC7571937EF02A7A46A57367534C11` |
| `277_script_KMPC_033_P5_3g7_s_c0_coefficient_passport_rerun1.py` | `9FC086E85AE23A6B96F4A859B9C8CB06B8E3F293959756CB354C82DEF06C8B0F` |

Hashe boli získané read-only PowerShellom. Runner zároveň zmrazil pôvodný
V1 hash `C370B610...A2A6B95` aj všetky solverové závislosti; prvý Python
proces RERUN1 je dokumentačne povolený.

## Outcome

RERUN1 technicky prešiel s 20/20 kontrolami a 10/10 odmietnutými fixtures.
Immutable JSON SHA je `4CED9D48...CFE8C`. Autoritatívny scoped rozsudok,
obmedzenia a ďalší krok sú v dokumente 56; táto predregistrácia zostáva
historickým záznamom očakávaní pred behom.
