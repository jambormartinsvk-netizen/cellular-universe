# FULL backend — plán získania zdrojového CLASS

**Súhlas používateľa:** 2026-07-15  
**Prvá voľba:** CLASS, otvorený C Boltzmann/recombination backend.

## Prečo CLASS ako prvý

Lokálny CAMB je prekompilovaná DLL a staršia vetva už narazila na chýbajúci
Fortran compiler. CLASS umožňuje auditovať zdroj a upraviť background bez
vydávania binárnej DLL za zdroj teórie. Výber nie je fyzikálny: nulový
referenčný beh musí pred K4 adapterom zreprodukovať štandardný backend.

## Postup a hranice

1. read-only inventár: Git, C compiler, make/CMake a architektúra;
2. stiahnuť nemenný release/tag do `external/CLASS/` a zaznamenať URL,
   commit/tag a SHA-256 zdrojového archívu alebo klonu;
3. bounded build bez K4 úprav a krátky štandardný reference smoke-test;
4. až potom vytvoriť samostatný, malý K4 adapter s nulovým limitom;
5. build/import/physics výsledky držať oddelene v `FULL_BACKEND/ARTIFACTS`.

Nevykoná sa tichá inštalácia do systému, zmena PATH ani prepis CAMB. Ak
Windows nemá kompatibilný C toolchain, stav sa zapíše ako technický blok a
zvolí sa explicitne ďalšia cesta (napr. WSL alebo CAMB so schváleným
Fortran toolchainom).

## Vykonanie 2026-07-15

- zdroj bol naklonovaný z oficiálneho `lesgourg/class_public` do
  `external/CLASS/`, shallow clone commit
  `e85808324f51fc694d12e3ed7439552a3c3f9540`;
- README SHA-256 je
  `1CE30F841FD5CAFA284C62F1B4A6C83D9F5C629FBF175B70E2D5C407C5686A98`;
- do izolovaného `C:\msys64` bol so súhlasom používateľa pridaný GNU
  toolchain `gcc 16.1.0` a `make 4.4.1` (balíky neboli pridané do systémového
  PATH ani do Visual Studio);
- prvý MSYS2 štart mal neplatný sandboxový HOME a chýbajúci Unix Git PATH.
  Budúce MSYS príkazy preto explicitne používajú `HOME=/tmp`; Git provenance
  sa číta z PowerShellu. Nešlo o build ani fyzikálny výsledok.
