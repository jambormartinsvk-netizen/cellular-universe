# Audit funkčnosti a karantény Python skriptov

Dátum: 2026-07-15  
Verdikt: **PASS_SCRIPT_CORPUS_INVENTORY**  
Rozsah: zdroj/AST/compile audit; žiadny cieľový skript nebol importovaný ani spustený

## Očakávanie verzus výsledok

| Kontrola | Očakávanie pred behom | Výsledok | Odchýlka | Verdikt |
|---|---|---|---:|---|
| počet cieľových `.py` bez auditora 188 | `192` | `192` | `0` | PASS |
| syntaxové chyby | iba 118/119 | iba 118/119 | žiadna nová | PASS |
| syntakticky platný súbor bez execution entry | 186 | 186 | žiadna | PASS |
| všetky ručne karantenizované cesty existujú | áno | áno | `0` chýbajúcich | PASS |
| cieľové skripty spustené | `0` | `0` | `0` | PASS |
| runtime | `<15 s` | `0.36 s` prvý beh | pod limitom | PASS |

## Výsledná klasifikácia

Karanténa obsahuje **62** skriptov:

| Kategória | Počet | Význam |
|---|---:|---|
| `DO_NOT_RUN_TECHNICAL` | 18 | známa formálna/runtime chyba alebo neúplný súbor |
| `DO_NOT_USE_PHYSICS` | 7 | spustiteľný, ale fyzikálny verdict je zamietnutý/nahradený |
| `ENVIRONMENT_BLOCKED` | 2 | chýbajúci compiler/backend v aktuálnom prostredí |
| `RUNNABLE_REVIEW_ONLY` | 21 | iba explicitná historická alebo regresná diagnostika |
| `SUPERSEDED` | 14 | existuje autoritatívnejší nástupca; rutinne nespúšťať |

Skript 188 ku každému riadku exportuje celý názov, status, dôvod, nástupcu, syntax a SHA-256. Ľudský mirror je `scripts/00_DO_NOT_RUN_SCRIPT_REGISTRY.md`.

## Overenie blokovania

Po samostatnej predregistrácii prešli dva target smoke-testy:

- skript 118: exit `2`, `DO_NOT_RUN_TECHNICAL`, `BLOCKED`;
- skript 176: exit `0`, `NOT_IN_QUARANTINE`;
- počet spustených cieľov: `0`.

`NOT_IN_QUARANTINE` neznamená fyzikálny PASS. Znamená iba, že súbor nemá v aktuálnom registri známy rutinný blokovací dôvod.

## Surový pattern scan

Checker našiel vzory fail-open, starých markerov, chýbajúcich interných runtime argumentov, nepodporovaného slice a nedosiahnuteľného legacy kódu. Tieto nálezy nie sú samy rozsudkom: napríklad 174 obsahuje starý slice ako text určený na nahradenie a 187 obsahuje chybové vzory ako auditované citácie. Rozhoduje vykonaná cesta, ručný audit a karanténny status.

## Obmedzenie úplnosti

Audit prečítal všetkých 192 cieľových zdrojov a zosúladil známe zlyhania s auditnými MD. Nevykonal všetkých 192 skriptov, preto netvrdí, že zvyšných 130 je funkčných alebo fyzikálne správnych. Nové runtime zlyhanie sa môže objaviť až pri riadne predregistrovanom behu; potom sa musí okamžite pridať do error ledgeru a karantény.

## Povinný budúci postup

Pred každým historickým skriptom sa spustí checker 188 s `--target`. Karantenizovaný skript sa smie priamo spustiť iba pri explicitnej reprodukcii starej chyby s očakávaným exception/verdictom a časovým limitom. Bežná práca použije uvedeného nástupcu.

## Opakovaná validácia po doplnení registra

Dňa 2026-07-15 bol audit znovu spustený priamo cez `C:\Python311\python.exe` s interným limitom 15 s a externým limitom 20 s. Skončil za 0,375 s s verdictom `PASS_SCRIPT_CORPUS_INVENTORY`: 192 cieľových skriptov, 62 karanténnych položiek, syntaxové chyby iba 118/119, neúplný vstup iba 186 a nula spustených cieľových skriptov.

Následná krížová kontrola porovnala automatický JSON s Markdown registrom podľa celého názvu, statusu a SHA-256. Všetkých 62 riadkov bolo jedinečných a rozdiel bol nulový. SK aj EN dodatok obsahujú práve jednu hlavičku AR55 a jednu hlavičku Q80. Do registra bolo doplnené výslovné upozornenie, že `NOT_IN_QUARANTINE` nie je technická, numerická ani fyzikálna certifikácia.

Bežný sandboxový pomocník opakovane zlyhal pred vytvorením procesu chybou `windows sandbox: helper_unknown_error`. Rovnaké read-only príkazy so schváleným zvýšeným oprávnením prešli; nejde o chybu Pythonu ani auditovaných súborov. Python bol volaný priamo, nie cez WindowsApps alias. Reštart operačného systému nebol potrebný.

Po reštarte počítača bol bežný sandbox znovu otestovaný a opäť zlyhal pred vytvorením procesu rovnakou chybou; priamy `C:\Python311\python.exe` mimo sandboxu následne prešiel za 0,6 s a potvrdil čitateľnosť registra.

Kontrola súbehu ukázala, že v tejto úlohe beží iba hlavný agent a žiadna ďalšia aktívna Codex úloha nepoužíva `D:\Teoria`; jediná ďalšia načítaná úloha bola `idle` v inom pracovnom adresári. Súbeh úloh preto nie je podporený ako príčina poruchy sandbox helpera.

Používateľ následne uviedol, že rovnaké zlyhanie sandboxu sa občas objavuje aj v iných projektoch. Tento medziprojektový symptóm ďalej oslabuje hypotézu chyby konkrétneho repozitára alebo súbehu v `D:\Teoria` a podporuje pracovnú diagnózu problému na úrovni Codex sandbox helpera, jeho profilu alebo systémovej bezpečnostnej vrstvy; presný koreň zatiaľ nebol dokázaný.

Izolačný test po zatvorení dvoch inštancií Visual Studio, VS Code a po dobehnutí ostatných úloh zlyhal v bežnom sandboxe rovnakou chybou `helper_unknown_error: setup refresh had errors` za 0,3 s ešte pred spustením priameho Python procesu. Otvorené IDE a paralelné úlohy preto nie sú podporené ako bezprostredná príčina.

Po opätovnej žiadosti prešiel priamy `C:\Python311\python.exe` mimo chybného sandboxu pre konkrétny checker 188 s interným limitom 15 s a externým limitom 20 s; verdict bol `PASS_SCRIPT_CORPUS_INVENTORY` za 2,27 s. Toto nie je neobmedzené oprávnenie pre ľubovoľný Python: každý ďalší vedecký beh ostáva viazaný na predregistráciu, konkrétny príkaz a interný aj externý timeout.
