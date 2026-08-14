# Codex Windows — koreňová príčina `pwsh.exe` App Execution Alias

**Dátum:** 2026-07-15  
**Stav:** `ROOT CAUSE CONFIRMED / čaká vypnutie aliasu a retest`

**Neskoršia aktualizácia:** používateľ nainštaloval oficiálny
`PowerShell-7.6.3-win-x64.msi`. Store alias `pwsh.exe` zostáva vypnutý.
Očakávaná nová cesta je `C:\Program Files\PowerShell\7\pwsh.exe`;
inštalácia ešte nemá úspešný Codex sandbox retest, preto sa stav auditu
zatiaľ neuzatvára.

## Koreňová príčina

Codex pred spustením sandboxovaného príkazu vyberá PowerShell cez PATH a
preferuje `pwsh.exe`. Na tomto počítači sa `pwsh.exe` rozkladá na
používateľský Microsoft Store/App Execution Alias:

```text
C:\Users\jambor.CHASTIA\AppData\Local\Microsoft\WindowsApps\pwsh.exe
```

Store balík sa fyzicky nachádza v `C:\Program Files\WindowsApps`, ale
`C:\Program Files\PowerShell\7\pwsh.exe` neexistuje. Sandboxovaný token
nevie alias spustiť a Codex zlyhá ešte pred vykonaním príkazu:

```text
CreateProcessAsUserW failed: 5 (Access is denied.)
```

Rovnaký výsledok nastal v režimoch `elevated` aj `unelevated` a v dvoch
nezávislých workspace koreňoch. Defender pri teste nevytvoril nový blok.

## Nezávislé potvrdenie

Otvorený issue v oficiálnom repozitári `openai/codex` opisuje rovnaký
mechanizmus: generická PATH detekcia vyberie WindowsApps alias pred platným
PowerShell executable a shell príkazy následne zlyhajú. Ďalší issue žiada
konfigurovateľný default shell; aktuálny verejný manuál taký kľúč
nedokumentuje.

## Najmenšia oprava bez novej inštalácie

Systémový Windows PowerShell existuje:

```text
%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe
```

Postup:

1. Windows `Settings` → `Apps` → `Advanced app settings` →
   `App execution aliases`;
2. vypnúť iba alias `pwsh.exe`/PowerShell patriaci Store balíku;
3. Store aplikáciu neodinštalovať;
4. úplne reštartovať Codex;
5. overiť, že sandboxovaný shell už používa systémový `powershell.exe`;
6. otestovať `D:\Teoria`, druhý workspace a štandardný `apply_patch`.

Vypnutie aliasu možno kedykoľvek vrátiť. Store PowerShell ostáva
nainštalovaný a dá sa spustiť jeho priamou package cestou; odstráni sa iba
problematické automatické rozlíšenie mena `pwsh.exe` v používateľskom PATH.

## Zdroje

- `https://github.com/openai/codex/issues/18937`;
- `https://github.com/openai/codex/issues/16579`;
- `https://learn.chatgpt.com/docs/windows/windows-sandbox`.
