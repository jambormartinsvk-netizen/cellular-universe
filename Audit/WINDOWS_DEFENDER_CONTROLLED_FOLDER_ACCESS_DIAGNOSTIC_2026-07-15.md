# Diagnostika Windows Defender / Controlled Folder Access

**Dátum:** 2026-07-15  
**Rozsah:** read-only lokálna diagnostika; žiadne bezpečnostné nastavenie nebolo zmenené

## Záver

Microsoft Defender je aktívny a `Controlled Folder Access` (CFA) je zapnutý.
V posledných šiestich hodinách boli zaznamenané reálne CFA bloky, ale týkali
sa iného projektu v chránenom OneDrive priečinku
`Dokumenty\CreateWokflow`, nie aktuálneho workspace `D:\Teoria`.

Blokované procesy:

- `C:\Program Files\Git\mingw64\bin\git.exe`;
- `pwsh.exe` z balíka `Microsoft.PowerShell_7.6.3.0...`.

V kontrolovanom intervale nebol nájdený CFA blok pre `Codex`,
`C:\Python311\python.exe` ani cestu `D:\Teoria`. Chyba
`windows sandbox helper_unknown_error: setup refresh had errors` preto môže
byť nepriamo ovplyvnená CFA/snapshot mechanizmom, ale log zatiaľ nedokazuje,
že Defender blokuje samotný Codex sandbox helper.

## Odporúčané úzke nastavenie

1. Otvoriť `Windows Security`.
2. Ísť na `Virus & threat protection` → `Manage ransomware protection`.
3. Vybrať `Allow an app through Controlled folder access`.
4. Vybrať `Add an allowed app` → `Recently blocked apps`.
5. Povoliť iba konkrétne zobrazené záznamy `git.exe` a `pwsh.exe` uvedené
   vyššie.
6. Ak sa neskôr objaví blok pre Codex alebo Python pri `D:\Teoria`, povoliť
   iba presný blokovaný executable z `Recently blocked apps` a znovu
   skontrolovať event log.

Na zobrazenie alebo zmenu allowed-app zoznamu môžu byť potrebné
administrátorské práva; lokálny read-only výpis hlásil, že zoznam výnimiek
bez administrátora nezobrazí.

## Čo nenastavovať

- nevypínať real-time protection ani CFA;
- nepridávať všeobecnú antivírusovú výnimku pre celý `D:\`, používateľský
  profil, `WindowsApps`, celý OneDrive alebo všeobecne všetky Python procesy;
- nezamieňať antivírusové `Exclusions` s CFA `Allow an app`.

Antivírusová výnimka znižuje kontrolu hrozieb. CFA allowed-app iba povoľuje
konkrétnemu programu zápis do chránených priečinkov a je preto užšie riešenie.

## Kontrolný postup po zmene

1. ukončiť a znovu spustiť blokovaný `git.exe`/`pwsh.exe` proces;
2. zopakovať krátky zápisový smoke-test v dotknutom projekte;
3. skontrolovať, či nepribudol event `1123` pre ten istý executable/path;
4. v `D:\Teoria` znovu otestovať štandardný patch helper;
5. ak helper stále zlyhá bez Defender eventu, klasifikovať problém ako
   Codex/Windows sandbox technickú chybu, nie ako preukázaný Defender blok.

## Autoritatívne zdroje

- Microsoft Support: Virus & threat protection in the Windows Security app;
- Microsoft Learn: Configure controlled folder access.

