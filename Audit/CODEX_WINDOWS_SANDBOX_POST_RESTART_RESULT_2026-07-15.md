# Codex Windows sandbox — výsledok po reštarte Windows

**Dátum:** 2026-07-15  
**Stav:** `ELEVATED SANDBOX SPAWN BLOCKED`  
**Fyzikálny projekt:** nedotknutý

**Aktualizácia po súhlase používateľa:** konfigurácia bola overená s presne
jednou sekciou `[windows]` a hodnotou `sandbox = "unelevated"`. Zmena sa
aktivuje až po úplnom reštarte Codex desktop aplikácie. Kontrolný sandbox
beh ešte neprebehol.

## Výsledok

Po úplnom reštarte Windows pôvodná chyba

```text
setup refresh had errors
```

zmizla. `elevated` sandbox setup teda postúpil do ďalšej fázy, ale spustenie
príkazu zlyhalo v oboch nezávislých workspace koreňoch:

```text
CreateProcessAsUserW failed: 5 (Access is denied.)
```

Zlyhávajúci executable je v oboch prípadoch používateľský Microsoft Store
alias:

```text
C:\Users\jambor.CHASTIA\AppData\Local\Microsoft\WindowsApps\pwsh.exe
```

Testované korene:

- `D:\Teoria`;
- Codex `visualizations` workspace na disku `C:`.

Výsledok preto nie je chyba ACL jedného repozitára. Dedicated
nižšie-privilegovaný používateľ `elevated` sandboxu nevie spustiť PowerShell
cez alias viazaný na profil hlavného používateľa.

## Konfigurácia a podporovaný ďalší krok

Aktívna konfigurácia je:

```toml
[windows]
sandbox = "elevated"
```

Aktuálny oficiálny Codex manuál neuvádza podporovaný konfiguračný kľúč pre
explicitnú cestu k agentovmu PowerShell executable. Uvádza však
`unelevated` ako fallback, keď administrátorsky schvaľovaný `elevated`
setup v prostredí nefunguje:

```toml
[windows]
sandbox = "unelevated"
```

Táto zmena zachováva Windows sandbox s obmedzeným tokenom a ACL hranicami,
ale je slabšia než dedicated-user `elevated` implementácia. Preto sa nesmie
vykonať potichu; vyžaduje vedomý súhlas používateľa a následný reštart Codex
aplikácie.

## Zdroj

OpenAI Codex manual, `Windows sandbox`:
`https://learn.chatgpt.com/docs/windows/windows-sandbox`.

## Uzavretie incidentu po čistej úlohe a MSI inštalácii (2026-07-15)

**Stav:** `PASS — shell sandbox znovu funkčný`.

Historický záznam vyššie sa zachováva: pôvodná úloha mala v procese uloženú
cestu k Store aliasu
`C:\Users\jambor.CHASTIA\AppData\Local\Microsoft\WindowsApps\pwsh.exe`.
Po vypnutí aliasu táto už bežiaca úloha logicky končila chybou `error 2`
(súbor neexistuje). Nebola to fyzikálna ani projektová chyba.

V novej úlohe po inštalácii oficiálneho MSI prešiel neeskalovaný test v
časovom limite 10 s:

```text
PSVERSION=7.6.3
PSHOME=C:\Program Files\PowerShell\7
PROCESS=C:\Program Files\PowerShell\7\pwsh.exe
CWD=D:\Teoria
SHELL_OK
```

Nezávislý test `Get-Item` zároveň úspešne otvoril oba oprávnené korene:

- `D:\Teoria`;
- `C:\Users\jambor.CHASTIA\.codex\visualizations\2026\07\13\019f5ad0-1446-7842-94a8-af1af94fc79e`.

Nasledujúca malá zmena tohto Markdown súboru bola vykonaná cez riadený
patch. Tým sa overuje aj cesta pre bezpečné zápisy do projektu. Záver:
nepokračovať v ďalšom ladení Defenderu; pre túto úlohu je problém shellu
vyriešený. Každý výpočtový beh však naďalej používa vlastný interný aj
vonkajší časový limit.
