# A2-K4 / C7.7c / K7c.3 — technická smrť skriptu 179

Dátum: 2026-07-15  
Stav skriptu 179: **MŔTVA TECHNICKÁ PODKOĽAJ**  
Dopad na A2-K4: **žiadny fyzikálny verdikt; ODE sa nespustila**

Skript 179 skončil pred integráciou s chybou `RuntimeError('K7c.2 seed names changed')`. Audit ukázal, že skript 178 serializuje JSON s `sort_keys=True`, a preto Python slovník po načítaní nesie abecedné poradie. Skript 179 nesprávne vyžadoval, aby poradie kľúčov JSON objektu bolo totožné s registrovaným poradím stavu.

Množina 13 názvov sa nezmenila. Vektor sa aj v 179 skladal explicitne cez registrované `NAMES`; zlyhala iba nadbytočná kontrola poradia slovníka.

Povolená oprava 180:

- overiť presnú množinu 13 mien namiesto poradia JSON objektu;
- vektor naďalej zostaviť explicitne v poradí `NAMES`;
- nemení sa žiadna rovnica, seed, škála, solver, tolerancia, prah ani limit.

Skript 179 a oba jeho chybové behy sa nemažú.

