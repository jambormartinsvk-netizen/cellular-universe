# Dodatok k 05 — počítanie živých koľají a breadth triage (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR10 oddeľuje fyzikálne odlišné koľaje, AR18 chráni rodiča pred automatickým
povýšením a AR30/AR43 definujú ich hĺbku. Doteraz však nebolo určené, ako
počítať „živé“ plytké hypotézy a kedy prerušiť hlbokú koľaj kvôli breadth
auditu. AR44 dopĺňa túto medzeru.

## AR44 — Počet živých koľají sa vždy člení podľa prejdenej brány

Jeden súhrnný počet `živých koľají` je zakázaný bez rozpisu najmenej na:

1. nezabité registrované hypotézy G1;
2. koľaje, ktoré sekvenčne prešli G2;
3. koľaje, ktoré sekvenčne prešli G3 alebo hlbšie.

Stav `ČAKÁ`, `nezabitá` alebo samotná G1 registrácia nie je dôkaz fyzikálnej
životaschopnosti. Breadth triage prideľuje body iba podľa rovnakých
sekvenčných brán a nesmie používať mäkšie kritériá než hlboká koľaj.

Rozpracovaná najhlbšia koľaj sa pred lacným rozhodovacím blokom neprerušuje
iba preto, aby sa zväčšil počet registrovaných alternatív. Breadth triage sa
vykoná pred nasledujúcou výrazne drahšou bránou, pri fyzikálnej smrti alebo
ak rovnaká technická stena pretrvá tri po sebe idúce ohraničené revízie.

Koľaje inej A1 backgroundovej vetvy sa v počte musia uviesť osobitne.

## Q71 — Pokračovať K4 alebo najprv rýchlo prejsť nezačaté koľaje?

**Odpoveď:** hybridne. K4 pokračuje cez BR3C po C7.8/`68.0`, pretože je
jediná A1-K1 koľaj za G3 a aktuálne má `66.2/100`. Pred drahým BR4 sa vykoná
breadth triage K8/K9 a re-entry audit K7/K11/K12. Pri fyzikálnej smrti K4 sa
triage otvorí okamžite.

Aktuálne má A1-K1 šesť nezabitých koľají, dve aspoň na G2 a iba jednu aspoň
na G3. Tieto tri čísla sa nesmú zlúčiť do tvrdenia „šesť životaschopných
modelov“.

