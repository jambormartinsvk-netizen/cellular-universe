# Pokyny externému auditorovi — EA-007

**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)

Over manifest a runtime mapu. Pracuj v čerstvej kópii `REPRO/`. Spusť iba
official príkazy z dokumentu 03, bez zmeny prahov, supportu, limitu alebo
priameho volania solvera. Každý proces má externý limit 10 s a interný 4.8 s.

Zapíš presný príkaz, exit code, wall time a SHA-256 generated JSON; uveď
Python, NumPy, SymPy, BLAS/LAPACK, OS a architektúru. Over osobitne regresiu,
rank, driver, holdout, combined-`R_fs`, S-C0, common a envelope tail.

dokumentovaná odchýlka sa označí `DECLARED_DEVIATION` a nedostane T2
official status. Použi
dôkazové tagy. Externý audit nemení fyzikálny verdict ani skóre.
