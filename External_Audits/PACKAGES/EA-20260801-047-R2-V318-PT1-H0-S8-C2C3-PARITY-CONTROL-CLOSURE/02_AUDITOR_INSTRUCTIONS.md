# Pokyny externému auditorovi — EA-047-R2 P0 control closure

Pracujte iba s týmto sealed package. Ide o follow-up audit presného findingu
`EA047-R1-EXT-P0-001`; jeho jediná sprístupnená predchádzajúca response je
manifestovaná ako `EVIDENCE/030`. Nečítajte live projekt ani iné responses.

Najprv overte package-local hashe, counts, ruleset, identity rolí a exact
parent parity všetkých `EVIDENCE/001-029` a oboch `REPRO` položiek. Potom
porovnajte finding v `EVIDENCE/030` s opraveným field contractom v `03`.
Pred ďalším čítaním exact porovnajte všetky štyri packaged bootstrap hashe s
`AUDITOR_RULESET_PATHS_AND_SHA256` mapou v sealed `00_SCOPE`.

Táto revízia nežiada nový Python: parent audit už vykonal všetkých 23/23
bounded procesov a dosiahol T2 pre deväť final cells. Overte, že nový text:

- zachováva fresh whole-file SHA chain;
- nepožaduje nemožnú exact accepted-copy zhodu dynamických provenance SHA;
- enumeruje jediný povolený field-difference set osobitne pre reference,
  A a B/C;
- vyžaduje exact fresh SHA binding každého dynamického provenance poľa;
- nemení alebo neignoruje žiadne fyzikálne pole, guard, threshold, state,
  count, identity alebo verdict.

Výstup označte `PASS_P0_CONTROL_REPAIR` alebo
`REVIEW_P0_CONTROL_REPAIR`. Každý nový finding klasifikujte P0/T1/S1-S4,
uveďte claim reach a návratový bod. Explicitne potvrďte, či parent T2 a
vedecký checkpoint ostávajú nedotknuté. Auditor iba odporúča.

Povinné response údaje: package/checkpoint/submission identity, manifest
SHA, auditor/model/timezone, environment `NOT_RUN_P0_STATIC_FOLLOWUP`, presné
read-only kontroly a ich výsledky, evidence tagy, nonclaims a autorita.
Pri každej vykonanej read-only kontrole uveďte presný príkaz, `exit code` a
`wall time`; ak nevznikol nijaký `generated JSON`, uveďte to explicitne.
Každú odchýlku od sealed pokynov označte ako `odchýlka`; tiché rozšírenie
allowlistu nie je dovolené.
