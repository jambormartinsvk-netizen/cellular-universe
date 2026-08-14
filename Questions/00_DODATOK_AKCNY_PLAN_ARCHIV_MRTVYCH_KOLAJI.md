# Dodatok k akčnému plánu — mŕtve koľaje

**Dátum:** 2026-07-13  
**Autorita:** tento dodatok je povinnou súčasťou `Questions/00_AKCNY_PLAN_v3.18_AKTUALNY_2026-07-13.md`

## Povinné pravidlo

Mŕtve koľaje sa **nemažú ani neprepisujú**. Každá sa uzavrie archívnym balíkom podľa:

- `Audit/00_PRAVIDLO_ARCHIVACIE_MRTVYCH_KOLAJI.md`;
- `Audit/REGISTER_MRTVYCH_KOLAJI_A_DOKAZOV_v3.18.md`.

Balík musí zachovať pôvodnú hypotézu, presný dôvod smrti, rozsah verdiktu, vstupy, použitý skript, reprodukovateľný výstup, analytické zdôvodnenie a pri vydaní kontrolné súčty.

## Nová brána pri každej koľaji

Koľaj možno označiť za `MŔTVA — ARCHIVOVANÁ` až keď:

1. je presne uvedené, ktorý test neprešla;
2. je oddelený numerický a analytický dôvod;
3. všetky použité skripty sú uložené v `scripts`;
4. existuje reprodukčný príkaz alebo je vysvetlené, prečo výpočet nebol potrebný;
5. je uvedené, čo verdikt nezabíja;
6. je uvedená podmienka, ktorá by oprávnila založiť novú koľaj.

Bez splnenia týchto bodov je stav iba `NEPREŠLA — ARCHIVÁCIA NEÚPLNÁ`, nie definitívne mŕtva.

## Pravidlo návratu

Tá istá mŕtva koľaj sa znovu neotvára. Pri novej fyzike, oprave výpočtu alebo nových dátach vznikne nový identifikátor a povinná sekcia `Rozdiel oproti mŕtvej koľaji`.

