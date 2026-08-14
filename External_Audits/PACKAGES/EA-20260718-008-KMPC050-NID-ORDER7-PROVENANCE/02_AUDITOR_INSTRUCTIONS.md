# Pokyny externému auditorovi — EA-008

**Autor teórie:** Martin Jambor  
**Tvorca auditovaného skriptu:** Codex (OpenAI)

Over manifest a runtime mapu. Pracuj v čerstvej kópii `REPRO/`. Spusť iba
KMPC-050 official príkazy z dokumentu 03, bez zmeny prahov, supportu,
runtime limitu alebo priameho volania solvera. KMPC-049 je `DO_NOT_RUN`.
Každý proces má externý limit 10 s a interný 4.8 s.

Zapíš presný príkaz, exit code, wall time a SHA-256 generated JSON. Uveď
Python, NumPy, BLAS/LAPACK, OS a architektúru. Over source hash guard,
passthrough/target counts, owner restore, oba ranky, matrix hashe, regresiu,
backward error, correction veľkosť a before/after driver aj holdout.

Každá odchýlka sa označí `DECLARED_DEVIATION` a nedostane T2 official
status. Rozlišuj pozorovanie od inference; externý audit nemení fyzikálny
verdict ani skóre.
