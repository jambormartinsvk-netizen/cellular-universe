# Pokyny externému auditorovi — EA-016

**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

Pracuj v čerstvej kópii adresára `REPRO`. Spusť iba runnery 317 a 319 podľa
dokumentu 03; runner 314 je voliteľná checkpoint-regeneračná diagnostika a
nesmie nahradiť dodaný hashovaný checkpoint v oficiálnej vetve. Nemeň
support, rcond, prahy, počet refinement krokov ani runtime.

Pre manifest, compile, smoke a oba official audity zapíš presný príkaz,
exit code, wall time a SHA-256 každého generated JSON. Uveď OS, Python,
NumPy a BLAS/LAPACK. Každú odchýlku označ `DECLARED_DEVIATION`.

Osobitne over:

- checkpoint SHA a jeho rolu `NO_PHYSICS_VERDICT`;
- 11-state standard a 13-state combined order;
- KMPC-073 common/tail/core PASS;
- KMPC-075 `EXACT_SAME_MATRIX_AND_CONSTANT`, baseline
  `3.8441418852221534e-10`, tri corrections a refined driver PASS;
- že PF-081–084 nemenia fyzikálny verdict a C2 `4/10` nemení K4 `60/100`.

Externý posudok je neautoritatívny. Použi povinné evidence tagy a oddeľ dopad
na package tier od dopadu na fyzikálny scope.
