# Pokyny externému auditorovi

1. Auditujte iba presnú otázku a tier hranicu v dokumente 00.
2. Spustite package preflight a uveďte exit code a wall time.
3. Reprodukciu robte vo fresh copy `REPRO/`; zapečatený balík nemeňte.
4. Zaznamenajte Python/NumPy/BLAS/OS, príkazy, exit code, wall time a SHA-256
   generated JSON.
5. Spustite smoke, missing-prerequisite guard a jeden KMPC-133 official beh.
6. Overte baseline→final driver residualy, tri kroky, matrix/RHS identitu a
   to, že tail/holdout/common/null/bridge brány ostali PASS.
7. Dovolená odchýlka je iba deklarovaná normalizácia runtime polí a jedného
   absolútneho root prefixu; vedecké polia a hashe musia byť exact.
8. Každú odchýlku označte package-integrity, implementation, numerical,
   physics, documentation alebo scope/tier.
9. Nemeňte projektový verdikt ani score.
