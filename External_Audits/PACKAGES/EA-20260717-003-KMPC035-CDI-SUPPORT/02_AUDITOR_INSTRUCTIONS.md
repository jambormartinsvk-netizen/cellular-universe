# Pokyny auditorovi

Over manifest pred výsledným auditom. Skontroluj matematickú definíciu
supportu, hranice intervalov, common/core rozlíšenie, importy runnera 279 a
úplný closure zdrojových závislostí z raw JSON.

Ak sa nájde chyba, uveď, či mení iba scope supportu, alebo celý algebraický
záver. Neudeľuj projektový verdikt.

Spusť smoke a audit podľa `03_REPRODUCTION_AND_EXPECTATIONS.md` v čerstvej
kópii `REPRO/`. Zapíš Python, NumPy, OS/architektúru, exit code, wall time a
rozdiely voči reference JSON. Bitová zhoda JSON nie je povinná; povinné je
vyhodnotenie zmrazených prahov. Externý timeout je 10 s na proces. Ak
reprodukcia neprebehne, nepouži tag `INDEPENDENTLY_RECOMPUTED`.
