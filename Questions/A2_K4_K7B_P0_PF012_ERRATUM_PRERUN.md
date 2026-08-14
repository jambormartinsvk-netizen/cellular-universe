# A2-K4 / K7b P0 — PF-012 erratum a predregistrácia nástupcov 192–194

Dátum: 2026-07-15  
Typ: `REGRESSION` + technické erratum  
Skóre: `NONE`; A2-K4 ostáva `66.5/100`

## Zachovaný neúspech

Skript 189 zlyhal už pri `--help` na `RuntimeError: generated parser marker is not unique`. Parserový marker bol hľadaný vo wrapper vrstve 169, hoci vzniká až vo finálnom texte 166. Fyzika ani child exporter sa nespustili. Skript 189 je `DO_NOT_RUN_TECHNICAL`; 190 je technicky nepoužiteľný, pretože závisí od 189. Oba ostávajú nezmenené.

## Povolená oprava

Skript 192 smie zlúčiť transformácie 172/175 priamo nad zdrojom 169 a vložiť parserovú transformáciu do jediného finálneho compile markera 169. Fyzikálny producent ostáva 174. Rovnice, koeficienty, parametre, tolerancie, 13 RHS a rozhodovacie prahy sa nesmú meniť.

Skript 193 smie oproti 190 zmeniť iba dieťa 189 na 192 a príslušné identifikátory verdictov/testu. Všetky pozitívne hodnoty, relatívna tolerancia `1e-4`, exact NID physics fingerprint, solver counts a tri negatívne fault-injection očakávania ostávajú presne podľa `A2_K4_K7B_P0_FAIL_CLOSED_IMPLEMENTATION_PRERUN.md`.

## Checker 194

Po pridaní 192–194 sa očakáva 198 ostatných Python súborov z pohľadu 194 a 66 karanténnych položiek. Syntaxové chyby musia zostať iba 118/119, neúplný vstup iba 186 a počet spustených cieľov nula. Nové statusy: 189 `DO_NOT_RUN_TECHNICAL`, 190 `DO_NOT_RUN_TECHNICAL`, 191 `SUPERSEDED`; historický 188 ostáva `SUPERSEDED`.

## Poradie a limity

1. AST/`py_compile` 192–194, externý limit 10 s.
2. `--help` 192–194, externý limit 10 s; 192 musí exportovať fault flag.
3. Checker 194 pre celý korpus a target 192/193; interný limit 15 s, externý 20 s.
4. Až potom 193: child najviac 8 s, agregátor interne 15 s, externe 20 s, kontrola najneskôr po 10 s.

Marker count iný než 1, timeout, invalid JSON alebo zmena fyzikálneho fingerprintu znamená `REVIEW`; nie fyzikálnu smrť K4.
