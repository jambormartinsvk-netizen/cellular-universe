# Pokyny externému auditorovi

1. Auditujte iba presnú otázku a tier hranicu v dokumente 00.
2. Najprv spustite package preflight a uveďte jeho exit code a wall time.
3. Reprodukciu vykonajte výhradne vo fresh copy `REPRO/`; zapečatený balík
   nemeňte.
4. Zaznamenajte presné príkazy, verzie Python/NumPy/BLAS/OS, exit code,
   wall time a SHA-256 generated JSON.
5. Spustite smoke, missing-prerequisite guard a jeden official KMPC-132 beh.
6. Porovnajte všetky vedecké polia. Dovolená je iba deklarovaná normalizácia
   runtime polí a jedného absolútneho root prefixu provenance cesty.
7. Každú odchýlku označte ako package-integrity, implementation,
   numerical, physics, documentation alebo scope/tier problém.
8. AD/.15 hodnotíte ako immutable T1 evidence; jeho samostatný official run
   nie je súčasťou tejto capsule.
9. Nemeňte projektový verdikt ani score; formulujte neautoritatívne
   odporúčanie s explicitnými nonclaims.
