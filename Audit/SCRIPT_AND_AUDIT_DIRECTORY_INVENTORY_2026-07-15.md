# Inventár adresárov skriptov, auditov a koľají

Dátum: 2026-07-15  
Typ: read-only lexikálny a závislostný inventár  
Stav: počas inventára nebol presunutý ani premenovaný žiadny existujúci súbor

## Súhrn

| Oblasť | Počet |
|---|---:|
| Python skripty bez `__pycache__` | 203 |
| súbory v `Audit/` | 221 |
| súbory v `Questions/` | 184 |
| skripty obsahujúce citovanú závislosť na inom `.py` | 146 |
| rozpoznané väzby skript → skript | 468 |
| existujúce podadresáre v `scripts/` | iba `__pycache__` |
| existujúce podadresáre v `Audit/` | 0 |

Záver: fyzický presun bez závislostnej mapy by mohol rozbiť `Path(__file__).with_name(...)`, generované wrappery, manifesty SHA-256 a historické Markdown odkazy.

## Lexikálne pokrytie hlavných A2 koľají

Počty vychádzajú z identifikátora v názve súboru. Nula neznamená, že sa koľaj nikdy nepočítala; môže znamenať starší všeobecný názov alebo výsledok uložený iba v dokumente.

| Koľaj | Skripty | Audity | Questions/plány |
|---|---:|---:|---:|
| A2-K1 | 4 | 6 | 1 |
| A2-K2 | 0 | 1 | 0 |
| A2-K3 | 2 | 2 | 0 |
| A2-K4 | 133 | 85 | 41 |
| A2-K5 | 14 | 12 | 2 |
| A2-K6 | 2 | 4 | 0 |
| A2-K7 | 10 | 36 | 15 |
| A2-K8 | 3 | 1 | 1 |
| A2-K9 | 3 | 1 | 1 |
| A2-K10 | 0 | 0 | 0 |
| A2-K11 | 8 | 10 | 2 |
| A2-K12 | 1 | 3 | 1 |

## A1 a A1-K1

Rozpoznané skripty:

- `11_script_A1_K1_cdm_background_audit.py`
- `12_script_A1_K1_cdm_background_audit_exact_zstar.py`
- `13_script_A1_K1_cdm_background_audit_exact_zstar.py`

Rozpoznané rozhodovacie a metodické dokumenty zahŕňajú Q19 background gate, stopping kritériá a manifest A1-K1/A2. A1-K1 preto potrebuje samostatný `PASS` záznam pre bránu pozadia a `REVIEW` záznam pre pokračujúcu A2 fázu; nemožno ho označiť globálnym PASS.

## Prirodzené členenie A2-K4 podľa existujúcich názvov

| Vetva | Skripty | Audity | Questions/plány |
|---|---:|---:|---:|
| K4.1 | 2 | 2 | 0 |
| K4.2 | 3 | 3 | 1 |
| 3b/RG/BR1 | 1 | 0 | 0 |
| 3b/RG/BR2 | 6 | 0 | 0 |
| 3b/RG/BR3A | 1 | 1 | 0 |
| 3b/RG/BR3B | 33 | 11 | 0 |
| 3b/RG/BR3C | 12 | 3 | 3 |
| 3b/ostatné | 16 | 9 | 3 |
| C7.7c/K1 | 0 | 1 | 0 |
| C7.7c/K2 | 2 | 1 | 1 |
| C7.7c/K3 | 2 | 1 | 1 |
| C7.7c/K4 | 4 | 1 | 1 |
| C7.7c/K5 | 1 | 2 | 1 |
| C7.7c/K6 | 1 | 0 | 1 |
| C7.7c/K7a | 6 | 6 | 5 |
| C7.7c/K7b | 17 | 5 | 5 |
| C7.7c/K7c | 11 | 7 | 9 |
| C7.7c/spoločné | 7 | 5 | 3 |
| lexikálne nezaradené | 8 | 27 | 7 |

Jemné BR3 vetvy už existujú v názvoch: `BR3B1`, `BR3B2a` až `BR3B2g` a `BR3C_a` až `BR3C_c`. K7 vetvy už obsahujú `K7a`, `K7b1`, `K7b2`, `K7b3a`, `K7b3b`, `K7c1`, `K7c2`, `K7c3a` až `K7c3d`.

## Ručné zaradenie ôsmich všeobecne pomenovaných K4 skriptov

| Skripty | Navrhovaný uzol |
|---|---|
| 27–31, 64 | `A2K4/CORE_SUPERHORIZON` |
| 72 | `A2K4/K4_3a` |
| 187 | `A2K4/C7_7c/K7/SHARED_K7B_K7C` |

Tieto súbory sa nemajú odložiť do neurčitého `misc`. Spoločný súbor patrí do jedného `SHARED` uzla a ostatné vetvy naň iba odkazujú.

## Auditné obmedzenie inventára

Toto je lexikálny inventár, nie fyzikálny verdikt. Konečné zaradenie každého súboru musí overiť jeho vstupy, výstupy, následníka, status v centrálnom registri a rozhodnutie, ktoré podporuje. Fyzicky presúvať možno až po vytvorení úplného path-map a checksum manifestu.
