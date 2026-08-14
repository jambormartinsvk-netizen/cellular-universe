# P5.3g7/S-C0 coefficient passport — technický ledger

**Dátum založenia:** 2026-07-16  
**Route:** `A1-K1 → A2-K4 → P5 → P5.3g7 → S-C0`  
**Run ID:** `KMPC-032`  
**historical_packages_total:** `2`  
**consecutive_technical_failures:** `0/10` po vecne úspešnom KMPC-033  
**Fyzikálny stav:** `CANDIDATE_SCOPED_PASS / PENDING_ORCHESTRATOR`; K4 ostáva `LIVE / 60/100`

## Pravidlá počítania

- Jeden balík je vopred zapísaná sada compile/help/smoke/audit procesov pre
  rovnaký fyzikálny rozsah KMPC-032.
- Syntax, import, CLI, timeout, sandbox, serializácia alebo hash mismatch sú
  technické chyby. Nesmú zabiť S-C0, P5 ani K4.
- Vecne úspešný audit s aspoň čiastkovým interpretovateľným výsledkom
  vynuluje `consecutive_technical_failures` na `0/10`.
- `py_compile`, `--help`, smoke a hash-only kontrola counter nevynulujú.
- História balíkov sa nikdy nemaže. Pri technickom zlyhaní sa zachová
  failure JSON a presný dôvod.

## Balíky

| Balík | Stav | Vecný výsledok | Technický dôvod/poznámka | Active counter po balíku |
|---:|---|---|---|---:|
| 1 | `TECHNICAL_FAILURE_PF069` | žiadny; audit zastal pri prvom M1 skalári | `np.float64` repr nebol platný vstup `SymPy Rational`; failure SHA `51C7B3...1EA03` | `1/10` |
| 2 | `TECHNICAL_COMPLETE_PENDING_ORCHESTRATOR` | 20/20 exact checks, päť M1 módov, 10/10 fixtures; výsledok SHA `4CED9D...CFE8C` | PF-069-only overlay, rovnice/váhy/supporty/prahy nezmenené | `0/10` |

## STOP hranica

Po desiatich po sebe idúcich technických zlyhaniach sa zastaví iba táto
implementačná línia s verdiktom `TECHNICAL_STOP_S_C0_PASSPORT`. Fyzikálny
stav bude `REVIEW_TECHNICAL_UNRESOLVED`, nie mŕtva koľaj. Fyzikálny alebo
formulačný STOP je možný iba z reprodukovaného nenulového presného
rezídua cez správne zmrazené rovnice, nie z nefunkčného programu.
