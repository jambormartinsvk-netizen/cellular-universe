# Dodatok k 05 — zákaz dvojitého počítania constraintu (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR13 vyžaduje constraintový numerický PASS a AR37 oddeľuje závislé dôkazy.
Chýbalo explicitné pravidlo pre DAE evolúciu, v ktorej sa constraint použije
priamo na definovanie derivácie. AR45 túto medzeru uzatvára.

## AR45 — Constraint použitý ako evolučná definícia nie je nezávislý PASS

Ak integrátor určuje metrickú alebo inú deriváciu priamo z constraintu, jeho
malé rezíduum v tej istej algebraickej forme je konštrukčná identita, nie
nezávislý dôkaz propagácie constraintu. Taký constraint:

- môže stabilizovať DAE evolúciu;
- musí byť označený ako `enforced`;
- nesmie dostať druhý bod alebo nezávislý confidence kredit;
- musí byť neskôr testovaný redundantnou rovnicou, propagovaným constraintom,
  druhým gauge alebo nezávislou implementáciou.

Trace/traceless rovnice, ktoré integrátor nepoužil, sa auditujú osobitne.

## Q72 — Prešla K4 po BR3C-b skorou evolúciou?

**Odpoveď:** `ÁNO IBA C7.7b; 66.5/100.` Štyri trajektórie dobehli s
konečným stavom a RHS. `00/0i` boli enforced a nemajú nezávislý PASS;
deep/shallow zhoda, trace/traceless rezíduá a konvergencie zostávajú
otvorené. Vysoký `nfev` hlbokého NIV je povinné numerické riziko.

