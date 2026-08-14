# Stav skriptov A1-K1: reťazec 11 → 12 → 13

**Dátum:** 2026-07-13  
**Test:** A1-K1-T5  
**Aktuálny validačný skript:** `13_script_A1_K1_cdm_background_audit_exact_zstar.py`  
**Konečný stav:** PASS

## 1. Auditná história

| Skript | Stav | Výsledok |
|---|---|---|
| `11_script_A1_K1_cdm_background_audit.py` | `FAIL` | Fyzikálne kontroly prešli, ale konvergenčný test odhalil interpolačnú chybu pri z_*; prah nebol splnený |
| `12_script_A1_K1_cdm_background_audit_exact_zstar.py` | `ERROR` | Pokus opravil mriežku, ale dynamický import zlyhal pred výpočtom pre chýbajúcu registráciu v `sys.modules` |
| `13_script_A1_K1_cdm_background_audit_exact_zstar.py` | **`PASS`** | Opravený import, presný bod z_* na mriežke, všetky fyzikálne a numerické brány prešli |

Pôvodné skripty 11 a 12 sa nemažú ani neprepisujú. Umožňujú zopakovať obe nájdené implementačné chyby.

Podrobnosti:

- `ERRATUM_11_12_A1_K1.md`,
- `ERRATUM_12_13_IMPORT.md`.

## 2. Prostredie úspešného behu

```text
Python 3.11.3
NumPy 2.4.4
Windows 10.0.26200, 64 bit
```

Príkaz:

```powershell
python scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py
```

Návratový kód: `0`.

## 3. Parametre

| Parameter | Hodnota |
|---|---:|
| h | 0.6637 |
| H₀ | 66.37 km s^-1 Mpc^-1 |
| Ω_m0 | 0.3517 |
| λ | 0.15 |
| δ | 0.02297 |
| ΔN_eff | 0.0535 |
| ω_b | 0.02237 |
| z_* | 1089.9 |
| x_min | -25 |
| základný krok | 0.001 |
| konvergenčný krok | 0.0005 |

Mriežka obsahuje `x_* = -ln(1+z_*)` ako presný bod.

## 4. Kľúčové fyzikálne výsledky

| Veličina | Výsledok |
|---|---:|
| X_b0 | 0.0507834672 |
| X_c0 | 0.3009165328 |
| Dnešný baryónový podiel v hmote | 0.1443942770 |
| Baryónový podiel v hmote pri z_* | 0.1564391128 |
| Podiel dnešného CDM vytvorený od z_* | 0.0899874321 |
| Komohybné CDM pri x = -25 | 0.2738378267 |
| Všetky hustoty kladné | áno |

Výsledok potvrdzuje približne `8.999 %` dnešnej komohybnej CDM hustoty vytvorenej od rekombinácie na tomto pracovnom bode.

## 5. Validačné brány

| Kontrola | Výsledok | Prah | Stav |
|---|---:|---:|---|
| Maximálny relatívny zvyšok zachovania | 4.8272×10^-16 | < 10^-12 | PASS |
| Chyba komohybného baryónového čísla | 2.2204×10^-16 | < 10^-12 | PASS |
| Chyba štandardnej limity λ = 0 | 5.0489×10^-11 | < 10^-9 | PASS |
| Maximálny rozdiel pri polovičnom kroku | 1.5950×10^-10 | < 10^-8 | PASS |
| Kladnosť všetkých hustôt | áno | povinné | PASS |

Absolútny zvyšok zachovania pri extrémne veľkých raných hustotách nie je vhodná bezrozmerná diagnostika. Verdikt používa relatívny zvyšok normalizovaný súčtom absolútnych členov.

## 6. Verdikt

Skript 13 je aktuálny reprodukovateľný validačný skript A1-K1-T5. Potvrdzuje backgroundový výsledok koľaje K1 na zadanom pracovnom bode. Neoveruje perturbačnú stabilitu, plný likelihood ani mikrofyziku CDM/popola.

Pri budúcej zmene rovníc alebo parametrov sa nesmie prepísať tento skript v publikovanom snapshote. Vytvorí sa nový očíslovaný skript a rozdiel sa uvedie v changelogu.
