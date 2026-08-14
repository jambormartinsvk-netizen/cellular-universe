# Povinné časové limity výpočtových artefaktov

**Účinnosť:** 2026-07-29  
**Stav:** záväzné prevádzkové pravidlo

Každý proces má explicitný externý timeout. DEV a official procesy sa
nesmú miešať.

## Limity

| Typ | Limit jedného behu | Výstup |
|---|---:|---|
| read/hash/static shell kontrola | '15 s' | bez vedeckého outputu |
| compile/help/parser/synthetic unit | '30 s' | DEV-only |
| offline SelfTest | '60 s' | DEV-only |
| bežný official numerický/symbolický run | '60 s' | immutable official target |
| dlhší výpočet | úseky do '60 s' | checkpoint s frozen resume contractom |

Iný limit musí byť pred spustením zdôvodnený v capsule. Limit sa po výsledku
nesmie post-hoc predĺžiť na záchranu verdiktu.

## DEV proces

DEV smie čítať iba synthetic/mocked vstupy a zapisovať iba do capsule
allowlistu mimo official cieľov. Sieť a fyzikálna interpretácia sú zakázané.
Autor môže vykonať DEV proces iba ak kapsul uvádza exact príkaz, candidate
SHA, timeout, fixture scope a cleanup.

DEV fail:

1. ukončiť proces a odstrániť iba allowlisted temp;
2. zapísať jeden compact error row;
3. zvýšiť 'ERRORS_USED_IN_CURRENT_BATCH' o jedna pre distinct candidate;
4. neopakovať rovnaký SHA;
5. nevytvárať nový auditný dokument.

Pri '10/10' sa ďalší edit aj proces zastaví do explicitného povolenia
Martina Jambora.

## Official proces

Official vyžaduje frozen contract/RC/input hashe, nezávislý static audit,
exact DNR check, absent-output guard a 'RUN_AUTHORIZED=true'. Publikuje
presne raz do neprítomného cieľa.

Official crash alebo timeout je technická chyba, nie fyzikálny výsledok.
Čiastočný output sa označí neautoritatívne a nesmie sa interpretovať.

## Monitoring

1. Proces sa kontroluje najneskôr po 10 s intervaloch.
2. Jeden blokujúci tool call nečaká dlhšie než 60 s.
3. Po timeout procese nesmie zostať nekontrolovaný background worker.
4. Checkpoint/resume nemení frozen rovnice, prahy ani state order.
5. Wall time sa zaznamenáva do DEV receipt alebo official rawu, nie do
   samostatného Markdown dokumentu.
