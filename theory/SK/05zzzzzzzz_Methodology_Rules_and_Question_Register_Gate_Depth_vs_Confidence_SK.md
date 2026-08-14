# Dodatok k 05 — hĺbka brány verzus pravdepodobnosť chyby (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR14 oddeľuje skóre od pravdepodobnosti pravdivosti a AR30 určuje sekvenčnú
hĺbku G1–G10. Doteraz však nebolo určené, ako interpretovať spätné potvrdenie
G7 po úspechu G8–G10 a ako zabrániť falošnému násobeniu závislých testov.
AR37 dopĺňa túto medzeru.

## AR37 — Neskoršie brány nie sú automaticky nezávislé dôkazy

Skóre `100/100` neznamená 100-percentnú pravdepodobnosť správnosti. Pri
odhade zvyškovej chyby sa musí evidovať pôvod každého dôkazu:

- rovnaké rovnice, kód, dáta alebo kalibrácia sú spoločný dôkaz a nesmú sa
  násobiť ako nezávislé testy;
- nový dataset testuje predikciu, ale sám nemusí odhaliť spoločnú chybu
  implementácie;
- nezávislé odvodenie, samostatný kód, slepá predikcia a externá reprodukcia
  sú silnejšie a môžu znížiť zvyškové riziko;
- číselná pravdepodobnosť sa nesmie označiť za vedecky kalibrovanú bez prioru
  a empiricky alebo metodicky obhájených false-pass mier jednotlivých brán.

Hĺbka koľaje a confidence ledger sa preto vedú oddelene.

## Q64 — Ak G8, G9 a G10 prejdú, aká je pravdepodobnosť chyby v G7?

**Odpoveď:** Zo skóre samotného ju nemožno vypočítať.

Ak všetky neskoršie brány používajú tú istú implementáciu, fatálna chyba G7
môže prejsť spolu s nimi a zvyškové riziko zostáva nevyčíslené.

Ak G10 obsahuje skutočne nezávislé odvodenie, nezávislý kód, slepé alebo
held-out predikcie, cross-code zhodu a externú reprodukciu, pracovný
audítorský odhad fatálnej chyby G7 môže byť **pod 1 %**. Toto je rozhodovací
odhad, nie nameraná pravdepodobnosť teórie. Pravdepodobnosť menšej chyby,
aproximácie alebo dokumentačného nedostatku zostáva vyššia a nikdy nie je
nulová.

## Požiadavka na budúcu G10

Aby bolo možné použiť odhad „pod 1 %“, G10 musí minimálne obsahovať:

1. odvodenie skontrolované osobou alebo tímom, ktorý nevytvoril hlavný kód;
2. druhú implementáciu bez kopírovania numerického jadra;
3. zhodu fyzických transferov a likelihood na vopred určených toleranciách;
4. aspoň jednu predikciu uzamknutú pred otvorením validačných dát;
5. reprodukčný balík s verziou, changelogom a kontrolnými súčtami;
6. negatívne a mŕtve koľaje zachované pre spätný audit.

