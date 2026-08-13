# Pokyny externému auditorovi — EA-047

Pracujte iba so sealed package. Nečítajte live projekt ani staršie response.
Najprv overte package-local hashe, counts, ruleset a identitu rolí. Potom
vykonajte reprodukciu podľa `03_REPRODUCTION_AND_EXPECTATIONS.md` výlučne v
novej dočasnej kópii `REPRO/`; originál package nechajte read-only.

Pri každom príkaze zapíšte presný príkaz, exit code, wall time, OS,
architektúru, Python, NumPy, SciPy a SHA-256 každého generated JSON.
Generated JSON porovnajte s jedinou accepted kópiou v `EVIDENCE/` po
odstránení iba povoleného top-level poľa `runtime_seconds`. Každú inú
normalizáciu alebo zmenu zdroja, prahu, CLI, output mena či priame volanie
funkcie označte ako `DECLARED_DEVIATION`.

Každé hlavné tvrdenie označte `OBSERVED_IN_PRIMARY`,
`INDEPENDENTLY_RECOMPUTED`, `INFERRED_FROM_PROJECT_DOCS` alebo
`CONTEXT_ONLY`. Oddeľte package tier od fyzikálneho verdictu. Material
finding klasifikujte presne ako `P0`, `T1` alebo `S1-S4` a uveďte claim
reach, earliest invalid checkpoint a odporúčaný workflow return point.

Odpoveď musí zachovať nonclaims z `00_SCOPE_AND_READ_ORDER.md`, uviesť
`CHECKPOINT_ID`, `AUDIT_SUBMISSION_ID`, package manifest SHA a explicitne
vyhlásiť, že externý auditor iba odporúča. Package-only príkazy nesmú čítať
live source paths, live registre, sieť ani predchádzajúce audity.

Každú odchýlku od sealed postupu zapíšte osobitne; nesmie byť potichu
započítaná ako deklarovaná T2 reprodukcia.
