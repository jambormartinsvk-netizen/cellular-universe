# A2-K4 / C7.7c / K7a-J4b — preregistrácia opravy parsera

**Dátum:** 2026-07-14, pred prvým behom skriptu 164

## Povolená zmena

Jediná vecná zmena oproti skriptu 163 je cesta:

```text
results / MODE / SURFACE / zero_integration_jacobian_diagnostic /
K7a_projected_jacobian_audit
```

Navyše sa zmení iba textové meno testu z J4 na J4b.

## Zakázané zmeny

- žiadna zmena rovníc, \(T\), \(T'\), backgroundu alebo bezpečného výpočtu \(B'/B\);
- žiadna zmena prahov ani rozhodovacej logiky;
- žiadne odstránenie starej FD diagnostiky;
- žiadna ODE evolúcia;
- žiadne zvýšenie hĺbky.

## Brána

Najprv sa opakuje NID/deep. Iba ak prejde všetkými už zaregistrovanými J4 bránami, pokračuje sa NID/shallow, NIV/deep a NIV/shallow.

