# Pokyny externému auditorovi — EA-017

**Autor teórie:** Martin Jambor  
**Tvorca skriptov:** Codex (OpenAI)

Pracuj v čerstvej kópii `REPRO`. Najprv over manifest a runtime mapu.
Spusť iba runnery 320 až 324 v poradí dokumentu 03, vždy compile/smoke/official
oddelene a s limitom 4.8 s. Nemeň support, prahy, `rcond`, počet corrections
ani checkpoint. Zaznamenaj príkaz, exit, wall time a SHA generated JSON.

Osobitne over checkpoint `NO_PHYSICS_VERDICT`, 13-state poradie, BI/.005
tail PASS, BI/.15 exact-same-matrix tri corrections, `M3_driver=true` a
zostávajúci nezávislý holdout REVIEW. Každú odchýlku označ.
