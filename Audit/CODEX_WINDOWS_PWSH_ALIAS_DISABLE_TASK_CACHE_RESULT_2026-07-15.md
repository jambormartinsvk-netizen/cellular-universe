# Codex Windows — výsledok po vypnutí `pwsh.exe` aliasu

**Dátum:** 2026-07-15  
**Stav:** `CURRENT TASK CACHED REMOVED SHELL PATH`

**Aktualizácia po MSI:** používateľ nainštaloval oficiálny x64 MSI
PowerShell 7.6.3 a reštartoval Codex. Tento existujúci task napriek tomu
naďalej volal starú absolútnu cestu
`C:\Users\jambor.CHASTIA\AppData\Local\Microsoft\WindowsApps\pwsh.exe`
a skončil chybou `CreateProcessAsUserW failed: 2`. Tento výsledok nehovorí,
že MSI executable nefunguje; dokazuje iba, že shell cesta je cached v
aktuálnom tasku. Rozhodujúci MSI test musí prebehnúť v novom forku/tasku.

## Výsledok

Po vypnutí App Execution Alias `pwsh.exe` a reštarte Codex aplikácie sa
chyba zmenila z:

```text
CreateProcessAsUserW failed: 5 (Access is denied.)
```

na:

```text
CreateProcessAsUserW failed: 2 (The system cannot find the file specified.)
```

Chybová správa naďalej uvádzala starú absolútnu cestu:

```text
C:\Users\jambor.CHASTIA\AppData\Local\Microsoft\WindowsApps\pwsh.exe
```

To znamená, že vypnutie aliasu prebehlo, ale existujúci Codex task si
uchoval predtým zvolenú shell cestu. Ani explicitné volanie systémového
PowerShellu vo vnútri command stringu nepomôže, pretože vonkajší cached
shell musí vzniknúť skôr, než sa vnútorný príkaz vykoná.

## Rozhodovací postup

1. Ponechať alias `pwsh.exe` vypnutý.
2. Vytvoriť nový/forknutý Codex task, ktorý zachová kontext, ale vykoná
   čerstvú detekciu shellu.
3. Overiť, či nový task používa
   `%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe`.
4. Ak áno, otestovať oba workspace a patch helper; následne možno skúsiť
   vrátiť sandbox z `unelevated` na `elevated`.
5. Ak nový task napriek vypnutému aliasu stále požaduje `pwsh.exe`,
   nainštalovať oficiálny x64 MSI PowerShell 7 do
   `C:\Program Files\PowerShell\7` po SHA-256/podpis kontrole.

Reaktivácia aliasu by obnovila schválené nesandboxované príkazy v tomto
tasku, ale nevyriešila by sandboxový `Access denied`. Je to iba dočasný
fallback, nie oprava.
