# Windows Defender CFA — výsledok testu po povolení aplikácií

**Dátum:** 2026-07-15  
**Vzťah:** dodatok k `WINDOWS_DEFENDER_CONTROLLED_FOLDER_ACCESS_DIAGNOSTIC_2026-07-15.md`

## Test

Po povolení blokovaných `git.exe`/`pwsh.exe` bol zopakovaný štandardný
sandboxovaný PowerShell smoke-test v `D:\Teoria`.

Výsledok:

```text
windows sandbox: helper_unknown_error: setup refresh had errors
```

Proces zlyhal okamžite ešte pred vykonaním príkazu.

## Defender korelácia

Bezprostredne po zlyhaní bol read-only skontrolovaný Defender Operational
event log. Nepribudol nový CFA/antivírusový blok pre Codex, Python,
PowerShell ani `D:\Teoria`. Zobrazené zostali iba staršie eventy `1123` pre
`git.exe` v inom OneDrive projekte.

## Rozsudok

Povolenie `git.exe` a `pwsh.exe` rieši potvrdené bloky OneDrive projektu,
ale nevyriešilo Codex sandbox helper. Aktuálny `helper_unknown_error` preto
nie je preukázaný Defender blok a nemajú sa pridávať ďalšie široké
bezpečnostné výnimky.

Odporúčaný ďalší technický krok je úplne ukončiť a znovu spustiť Codex
desktop aplikáciu. Dovtedy sa smú používať iba explicitne schválené,
ohraničené príkazy a auditovaný replacement workaround pre existujúce
súbory.

