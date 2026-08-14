# A2-K4 / K7b P0 — fail-closed audit po PF-012 a timeoute 193

Dátum: 2026-07-15  
Stav: `REVIEW_TIMEOUT_UNCLOSED`  
Hĺbka A2-K4: **66.5/100**, bez zmeny

## Výsledok

Pôvodný skript 189 prešiel `py_compile`, ale zlyhal už pri `--help` na `RuntimeError: generated parser marker is not unique`. Koreň PF-012: parser bol patchovaný vo wrapper vrstve 169, hoci cieľový parser vzniká až vo finálnom texte 166. Fyzika ani child exporter sa nespustili. Skript 189 je technicky mŕtvy; 190 je nepoužiteľný pre závislosť od 189. Oba ostali zachované.

Nástupcovia 192–194 prešli `py_compile` aj CLI smoke-testom. Skript 194 potvrdil:

- verdict `PASS_SCRIPT_CORPUS_INVENTORY`;
- 198 ostatných Python súborov;
- 66 karanténnych položiek;
- statusy 20 technických, 7 fyzikálne nepoužiteľných, 2 environmentálne blokované, 21 review-only a 16 superseded;
- syntaxové chyby iba 118/119;
- neúplný vstup iba 186;
- nula spustených cieľových skriptov;
- target 192 a 193 `NOT_IN_QUARANTINE`.

## Beh 193

Predregistrovaný agregátor 193 bol spustený s interným limitom 15 s, child limitom 8 s a externým limitom 20 s. Po 10 s ešte bežal a skončil na internom limite s exitom `124` a verdictom `TIMEOUT_UNCLOSED`. Neexportoval úplnú maticu pozitívnych/negatívnych výsledkov, preto nie je dovolené vyvodiť PASS ani fyzikálny FAIL.

Surový výstup: `Audit/A2_K4_K7B_P0A_PF012_CORRECTED_RAW_2026-07-15.json`  
SHA-256: `7261EA02195F30A2AE20E7AAF45E08DA3F0B3436FCE83087CDEC963D71A9D4EF`

## Rozsudok

- K7b predchádzajúci numerický PASS sa týmto neruší.
- Fail-open hardening ešte nie je uzavretý, pretože úplná pozitívna a negatívna regresná matica nedobehla.
- A2-K4 ostáva živá na 66.5/100.
- Timeout agregátora nie je smrť koľaje ani dôkaz chyby rovníc.
- Ďalší pokus nesmie iba predĺžiť jeden monolitický beh; musí checkpointovať jednotlivé prípady.

## Ďalší krok

Samostatne a s vlastným výstupom spustiť 2 baseline NID prípady cez 175, 2 kandidátske NID prípady cez 192, 2 NIV prípady cez 166 a 3 negatívne fault-injection prípady cez 192. Každý prípad má interný limit 8 s a externý 12 s. Až potom sa vykoná ne-exekučné offline porovnanie fingerprintov, zaokrúhlených regresií a presných failed-check množín.

