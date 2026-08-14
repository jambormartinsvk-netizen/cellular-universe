# FULL — kontrakt K4 background adaptera

Pred prvou zmenou CLASS zdroja musí adapter splniť tento kontrakt:

1. je samostatný patch nad zmrazeným CLASS commitom, nie ručná úprava bez
   diffu;
2. jediná fyzikálna zmena v prvom kroku je `H(a)`/konformný čas z K4
backgroundu; atómové sadzby, Thomsonov prierez a HyRec ostávajú štandardné;
3. obsahuje `adapter_enabled=no` nulový limit, ktorý byte/číselne reprodukuje
   štandardný reference vstup v deklarovaných tabuľkách;
4. pred plným perturbation behom exportuje na mriežke `a` ledger
   `H_K4(a)`, `eta_K4(a)`, hustotných frakcií a kontroly kladnosti;
5. nesmie upravovať predikcie alebo S8/H0 parametre; je to implementácia už
   zmrazeného K4 pozadia;
6. každý build/run má samostatné immutable artefakty a 45/55 s limit.

## Brána pred technickým krokom

Pred mapovaním API musí prejsť
`03_K4_BACKGROUND_UNIVERSALITY_GATE.md`: CLASS potrebuje jediné `H(a)`, nie
pivotovo alebo módovo závislú K7 pomocnú premennú.

## Najbližší technický krok po PASS brány

Read-only mapovanie CLASS background API (`source/background.c`,
`include/background.h`) a návrh minimálneho adapter patchu. Žiadny zdroj sa
nemení pred zápisom `03_K4_ADAPTER_PREREGISTRATION.md` s presnými rovnicami,
mapovaním jednotiek a nulovým testom.
