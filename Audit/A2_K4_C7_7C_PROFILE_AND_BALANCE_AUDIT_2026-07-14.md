# A2-K4 / C7.7c — audit profilovania a maticového vyváženia

**Dátum:** 2026-07-14  
**Auditovaný stav:** A2-K4, brána C7.7c  
**Skóre pred auditom:** `66.5/100`  
**Skóre po audite:** `66.5/100`  
**Hlavný rozsudok:** A2-K4 ostáva **ŽIVÁ**; numerická podkoľaj **C7.7c-K4 analytická obálka bez vyváženia je MŔTVA**.

## 1. Čo bolo testované

Skripty:

- `scripts/150_script_A2_K4_C7_7c_segment_profiler.py` — jeden mód, jeden povrch a najviac jeden segment, bez zmeny rovníc;
- `scripts/151_script_A2_K4_C7_7c_initial_scaled_jacobian_profile.py` — nulovo-integračný 13×13 Jacobian v normalizovaných premenných;
- `scripts/152_script_A2_K4_C7_7c_matrix_balance_diagnostic.py` — nulovo-integračné diagonálne vyváženie toho istého Jacobianu bez permutácie stavov.

Všetky skripty dedia fyziku, počiatočné stavy, background, uzáveru `L5=0`, tolerancie a analytickú obálku z auditnej vetvy skriptov 136/139/142/146/147. Nové skripty pridávajú iba výber trajektórie a diagnostické výstupy.

## 2. Segmentový profil

| Mód/povrch | Interval | Vnútorný limit | Dokončené segmenty | RHS volania | Výsledok |
|---|---:|---:|---:|---:|---|
| NIV/deep | `-25→-24` | 8 s | 0/1 | 362 305 | `TIMEOUT_UNCLOSED` v RHS, 8.015 s |
| NIV/shallow, prvý pokus | `-23→-22` | 8 s | nezískaný JSON | nezískané | vonkajší limit 10 s; proces ukončený |
| NIV/shallow, opakovanie | `-23→-22` | 6 s | 0/1 | 275 329 | `TIMEOUT_UNCLOSED` v RHS, 6.015 s |
| NID/deep | `-25→-24` | 6 s | 0/1 | 227 521 | `TIMEOUT_UNCLOSED` v RHS, 6.016 s |

Orientačná rýchlosť bola približne 45 tisíc RHS/s v oboch NIV behoch a 38 tisíc RHS/s v NID. Ani kontrolný NID mód nedokončil prvý segment. Problém preto nie je špecifický pre NIV ani dôkaz fyzikálnej nestability.

## 3. Lokálny Jacobian bez integrácie

Oba profily použili centrálny rozdiel s krokom `10^-7` v normalizovaných súradniciach a iba 28 RHS volaní.

| Diagnostika | NID/deep | NIV/deep |
|---|---:|---:|
| rozsah analytických škál `max/min` | `5.5435×10^23` | `4.5540×10^25` |
| `max|J_ij|` pred vyvážením | `4.1886×10^14` | `8.8471×10^10` |
| najväčšia singulárna hodnota | `6.0889×10^14` | `1.3177×10^11` |
| spektrálny polomer | `3.4441515426` | `3.4441515426` |
| dominantný normalizovaný RHS | `delta_f` | `U_gamma` |

Najväčšie NID väzby boli `delta_gamma, delta_fs → delta_f` s veľkosťou `4.19×10^14`. V NIV dominovali `U_gamma, U_fs → eta` s veľkosťou `8.85×10^10`. Vlastné čísla však ostali rádu jednotiek. Ide teda o extrémne nenormálnu reprezentáciu s veľkými rušiacimi sa medzičlenmi, ktorá núti explicitný solver opakovane zmenšovať alebo odmietať kroky.

## 4. Diagonálne vyváženie

Použitá bola štandardná diagonálna podobnostná transformácia

`J_bal = D^-1 J D`,

bez permutácie komponentov. Tá nemení vlastné čísla ani fyzikálne riešenie; mení iba numerické súradnice.

| Diagnostika | NID/deep | NIV/deep |
|---|---:|---:|
| `max|J_ij|` pred | `4.1886×10^14` | `8.8471×10^10` |
| `max|J_bal,ij|` po | `5.93109` | `5.93109` |
| redukčný faktor | `≈7.06×10^13` | `≈1.49×10^10` |
| spektrálny polomer po | `3.4441515426` | `3.4441515426` |
| relatívna odchýlka spektra | `1.69×10^-10` | `5.84×10^-15` |
| rozsah výsledných fyzikálnych škál | `1.1891×10^21` | `3.5676×10^21` |

Výsledok prešiel diagnostickou bránou: obrovské mimo-diagonálne prvky zmizli, kým spektrum sa v numerickej presnosti zachovalo.

## 5. Rozsudok a dôvod smrti podkoľaje

### C7.7c-K4 — MŔTVA numerická podkoľaj

**Základ:** analytická obálka `max(|y_start|,|y_series(-18)|)` bez ďalšieho vyváženia.  
**Dôvod smrti:** obálka síce odstránila problém s nulovým `atol`, ale zaviedla škálovaný Jacobian s prvkami až `4.19×10^14`; NID aj NIV nedokončili ani prvý e-fold v časovom limite.  
**Čo rozsudok neznamená:** nejde o smrť fyzikálnej koľaje A2-K4 ani o dôkaz rastúceho fyzikálneho módu.  
**Zachované dôkazy:** skripty 146–152, predregistrácia segmentového profilu a tento audit.

### A2-K4 — ŽIVÁ, technicky otvorená

K4 zostáva na `66.5/100`. Brána C7.7c ešte neprešla, lebo maticové vyváženie zatiaľ nebolo použité v evolúcii a úplný komponentový audit nebol zopakovaný.

### C7.7c-K5 — NOVÁ numerická podkoľaj

K5 použije jedinú novú numerickú operáciu: pevnú diagonálnu podobnostnú transformáciu odvodenú z lokálneho počiatočného Jacobianu. Fyzika, počiatočné stavy, solver a tolerancie zostanú nezmenené.

## 6. Ďalší krok

1. predregistrovať presný algoritmus K5 a jeho brány;
2. overiť jeden segment NID/deep a NIV/deep;
3. ak oba prejdú, overiť oba shallow povrchy;
4. až potom spustiť úplnú evolúciu a komponentový audit C7.7c;
5. pridať `+0.2` iba po úplnom PASS, nie za diagnostiku ani za jeden segment.

