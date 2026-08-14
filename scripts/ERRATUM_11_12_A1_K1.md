# Erratum skriptov 11 a 12 pre test A1-K1-T5

**Dátum:** 2026-07-13  
**Dotknutý test:** A1-K1 — rozdelenie baryónov a CDM v backgrounde  
**Stav:** skript 11 reprodukovateľne zlyhal na konvergenčnej bráne; skript 12 opravuje identifikovanú numerickú príčinu bez zmeny fyzikálnych rovníc

## 1. Čo sa stalo

Prvý uložený skript

`11_script_A1_K1_cdm_background_audit.py`

vrátil `status: FAIL`. Prešli kontroly kladnosti, zachovania, komohybného baryónového čísla aj limita `λ = 0`, ale neprešla vopred nastavená konvergenčná brána `10^-8`.

Pri porovnaní kroku `0.001` a `0.0005` bol maximálny relatívny rozdiel kľúčových veličín

```text
5.4946×10^-6.
```

Rozdiel pochádzal z veličiny „podiel dnešného CDM vytvorený od rekombinácie“. Rekombinačný bod

```text
x_* = -ln(1 + z_*)
```

neležal presne na rovnomernej mriežke. Hodnota sa určovala lineárnou interpoláciou. Pri polovičnom kroku sa zmenila interpolačná chyba druhého rádu a dominovala nad chybou RK4.

## 2. Prečo sa prah nemení

Konvergenčný prah sa spätne neuvoľnil. Také uvoľnenie by zakrylo slabinu testu. Pôvodný skript 11 zostáva nezmenený, aby sa dal neúspešný výsledok zopakovať.

## 3. Oprava v skripte 12

Skript

`12_script_A1_K1_cdm_background_audit_exact_zstar.py`

importuje fyzikálne rovnice, diagnostiky, CLI a prahy priamo zo skriptu 11. Nahrádza iba konštrukciu integračnej mriežky:

1. interval sa rozdelí v bode `x_*`,
2. `x_*` je presným bodom oboch hrubostí mriežky,
3. každý RK4 krok je najviac rovný požadovanému kroku,
4. výpočet pri rekombinácii už nepotrebuje interpoláciu medzi krokmi.

Fyzikálne rovnice ani auditné prahy sa nezmenili.

## 4. Reprodukcia

Pôvodný neúspešný test:

```powershell
python scripts/11_script_A1_K1_cdm_background_audit.py
```

Opravený test:

```powershell
python scripts/12_script_A1_K1_cdm_background_audit_exact_zstar.py
```

Oba skripty musia zostať v balíku pracovnej evidencie. Pri publikovaní sa má ako aktuálny validačný skript použiť skript 12 a changelog má uviesť dôvod nahradenia skriptu 11.
