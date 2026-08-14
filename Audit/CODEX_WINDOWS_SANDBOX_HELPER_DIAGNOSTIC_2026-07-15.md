# Codex Windows sandbox helper — diagnostika

**Dátum:** 2026-07-15  
**Stav:** `OPEN — čaká test po reštarte Windows`

## Overené fakty

1. Štandardný sandboxovaný PowerShell zlyháva pred vykonaním príkazu:

   ```text
   windows sandbox: helper_unknown_error: setup refresh had errors
   ```

2. Rovnaká chyba nastala v dvoch nezávislých povolených workspace koreňoch:
   `D:\Teoria` aj v Codex `visualizations` adresári na disku `C:`. Chyba je
   preto globálna pre natívny Codex Windows sandbox, nie špecifická pre
   repozitár teórie.
3. Bezprostredne po teste nevznikol nový Microsoft Defender/CFA blokovací
   event. Defender nie je preukázaná príčina.
4. Codex konfigurácia obsahuje:

   ```toml
   [windows]
   sandbox = "elevated"
   ```

5. Nebola nájdená používateľská ani projektová `requirements.toml`, ktorá
   by zakazovala fallback.
6. Nainštalovaná aplikácia je `OpenAI.Codex 26.707.9981.0`.

## Oficiálne relevantné správanie

Aktuálny Codex manuál uvádza, že `elevated` Windows sandbox používa
pomocných nízko-privilegovaných používateľov, ACL hranice, firewallové
pravidlá a lokálne politiky. Ak tento setup v danom prostredí nefunguje,
oficiálny fallback je:

```toml
[windows]
sandbox = "unelevated"
```

`unelevated` používa obmedzený token aktuálneho používateľa a ACL hranice.
Je slabší než `elevated`, ale stále zachováva sandbox a je určený presne pre
prostredia, kde administrátorsky schvaľovaný setup blokuje lokálna alebo
firemná politika.

## Rozhodovací postup

1. Úplne reštartovať Windows bez ďalšej zmeny konfigurácie.
2. Zopakovať sandbox smoke-test v oboch workspace koreňoch.
3. Ak prejdú, ponechať `elevated` a uzavrieť tento audit.
4. Ak zlyhajú rovnakou chybou, zmeniť iba jeden riadok na
   `sandbox = "unelevated"`, reštartovať Codex aplikáciu a test zopakovať.
5. Ak zlyhá aj `unelevated`, exportovať logy/feedback a nahlásiť chybu
   podpore; nepridávať ďalšie Defender exclusions.

## Zdroj

OpenAI Codex manual, sekcia `Windows sandbox`:
`https://learn.chatgpt.com/docs/windows/windows-sandbox`.

