# A2-K4 / C7.7c / K7c / P3b — formálna predletová kontrola skriptu 205

**Dátum:** 2026-07-15  
**Stav:** `PASS_FORMAL_PREFLIGHT_ONLY`  
**Fyzikálny výsledok P3b:** ešte neudelený

## Účel

Pred prvým a jediným autoritatívnym fyzikálnym behom sa overuje, že kandidátsky skript 205 implementuje iba vopred registrovanú zmenu: z rovnice pre `M'` vypúšťa dva koeficienty, ktoré skript 201 dokázal ako presné algebraické nuly. Táto kontrola sama osebe neposkytuje dôkaz konvergencie RK4 ani fyzikálny rozsudok koľaje.

## Zmrazené artefakty

| Artefakt | SHA-256 | Úloha |
|---|---|---|
| `scripts/205_script_A2_K4_C7_7c_K7c_P3b_zero_identity_RK4_audited.py` | `B7EC8BAD3BFB0D48EC91D6F1BB0A602FA1834A021BB94C92D6D1B398D5F3CDC2` | kandidátsky fyzikálny beh |
| `scripts/207_script_A2_K4_C7_7c_K7c_P3b_source_delta_audit_tuple_fixed.py` | `00B2B1DDC87FA9E544A3A2A9C196D94E621B4E440D99B0C1C4AEF551EE047070` | nezávislý statický audit rozdielu zdrojov |
| `Audit/A2_K4_K7C_P3B_SOURCE_DELTA_207_2026-07-15.json` | `AE07F945D4B199D0E47A41227A62FE3C2747D8FCA9B51EB4583748673C51A904` | výsledok auditu rozdielu zdrojov |
| `scripts/208_script_python_corpus_status_audit_before_K7c_P3b_script205.py` | `213B16AFF89ADF076D86025FEEED5611B87AA58DDF4C95EE5EBF678C8CA79989` | kontrola karantény a stavu korpusu |
| `Audit/A2_K4_K7C_P3B_CORPUS_CHECKER_208_2026-07-15.json` | `EF485ECE8102D0210E38406C6A0D0D21EFD84C11E23B0868222FBEE151AC0C26` | výsledok kontroly korpusu |
| `Questions/A2_K4_C7_7C_K7C_P3B_ZERO_IDENTITY_RK4_PREREGISTRATION_2026-07-15.md` | `5FF6A16B60CC5AFFF7D62F1F1C92D85E5F3D7DCBCFACF1DA97ED8E9C1F04AA8F` | preregistrované brány a rozsudky |

## Výsledky formálnych kontrol

- `py_compile`: PASS.
- `--help`: PASS; parameter `--output` je dostupný.
- Poradie parsera: PASS; `--output` je zaregistrovaný pred `parse_args`.
- Rozdiel zdrojov 197 → 205: `PASS_P3B_SOURCE_DELTA_ONLY_TWO_ZERO_TERMS`.
- Rovnica `M'`: počet členov 9 → 7; nepribudol žiadny nový člen a chýbajú práve dve registrované presné nuly.
- Ostatných 12 zložiek RHS, pozadie, škálovanie, integrátor a tri RK4 mriežky: staticky zhodné.
- Kontrola korpusu: PASS; skript 205 nie je v karanténe.
- Skripty 203, 204 a 206 sú zachované a označené `DO_NOT_RUN_TECHNICAL` s dokumentovanými príčinami.
- Autoritatívne výstupy P3b pred behom neexistovali; nehrozí ich tiché prepísanie.

## Preregistrované očakávanie a rozhodnutie

Počíta sa rovnaká NID/deep trajektória na intervale 0,25 e-foldu a rovnaké mriežky 100/200/400 ako v P1. Jedinou fyzikálnou zmenou je odstránenie dvoch presne nulových členov.

Centrálny očakávaný výsledok, ak floatové artefakty týchto núl spôsobovali nekonvergenciu:

- `difference_200_400 < 1e-6`,
- `8 <= classical_RK4_ratio <= 32`.

Rozhodnutia:

- obe brány PASS → `PASS_P3B_ZERO_IDENTITY_RK4_CONVERGENCE`;
- platný výpočet, ale aspoň jedna brána FAIL → `STOP_P3B_ZERO_IDENTITY_NOT_SUFFICIENT`;
- timeout, porucha proveniencie, neúplný výstup alebo technická chyba → `REVIEW`, nie fyzikálna smrť.

## Limity behu

- interný limit skriptu: 25 s,
- limit zdrojového kroku: 15 s,
- limit dcérskeho procesu: 6 s,
- vonkajší limit príkazu: 30 s,
- jeden autoritatívny beh; bez automatického opakovania a bez prepísania výstupov.

## Povolenie na beh

Formálna brána je splnená. Je povolený jeden autoritatívny beh skriptu 205 podľa preregistrácie. Tento dokument nemení hĺbkové skóre A2-K4 a neposkytuje fyzikálny PASS.
