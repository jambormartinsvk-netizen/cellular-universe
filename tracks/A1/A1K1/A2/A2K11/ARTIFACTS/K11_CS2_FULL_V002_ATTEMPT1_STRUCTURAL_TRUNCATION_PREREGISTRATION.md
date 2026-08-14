# K11-CS2 full v002 — pokus 1/10: exact register, interior a deklarovaný numerický rez

**Dátum:** 2026-07-16  
**Technická architektúra:** `ARCH-A / K11-TC-A3`  
**Counter pred behom:** `0/10`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`  
**Rozsah:** algebra a contract; bez ODE, bez CMB a bez bodov

## 1. Čo sa počíta ľudskou rečou

Skript nebude tvrdiť, že useknutá nekonečná hierarchia je presná fyzika.
Overí, že zoznam stavov je správny, že vnútorné CAMB rovnice majú presné
zdrojové koeficienty a že posledný riadok je viditeľne označený ako
numerická aproximácia bez skrytého `L+1`. Chybné zoznamy musí odmietnuť
rovnaký validator, aký používa kladný prípad.

## 2. Očakávaný výsledok pred behom

Pre `L=4,6,8` očakávame:

```text
state counts = 25, 33, 41;
E_gamma_0 a E_gamma_1 neprítomné;
všetky interior J/G/E residuals = presná algebraická nula;
zero-tail E top residual po explicitnom E_(L+1)=0 = presná nula;
všetky negatívne fixtures odmietnuté;
closure metadata: NUMERICAL_APPROXIMATION, nie EXACT_PHYSICS;
runtime < 5 s; exit 0.
```

Smoke overí `L=4`; full overí `L=4,6,8`. Výsledky budú samostatné immutable
JSON súbory. Každý proces má vonkajší limit najviac 10 s; runner aj base
majú vnútorný limit najviac 5 s.

## 3. PASS / STOP / REVIEW

**PASS iba ak:** všetky uvedené presné a contract kontroly prejdú.
Autoritatívny názov môže byť iba

```text
PASS_ARCH_A_ATTEMPT_1_EXACT_SET_INTERIOR_AND_REGISTERED_TRUNCATION_ONLY
```

**Technický FAIL:** syntax/import/runtime/validator chyba zvýši ARCH-A counter
na `1/10`, zachová traceback a dôvod. Nezabije K11.

**Algebraický STOP rozsahu pokusu:** nenulový CAMB interior alebo conditional
top residual zastaví attempt 1 a vyžiada source/sign audit. Neznamená smrť
K11 bez fyzikálneho no-go.

**Po PASS:** counter sa zapíše ako úspešne použitý pokus `1/10`; nasleduje
samostatná predregistrácia full TCA/opacity/DAE a neskôr povinný `lmax` a
closure-family konvergenčný test. Tento pokus sám nemení hĺbku.

## 4. Plánované artefakty

```text
scripts/baseScripts/a2_k11_cs2/finite_hierarchy_contract_v002.py
scripts/baseScripts/a2_k11_cs2/finite_hierarchy_preflight_v002.py
scripts/266_script_A2_K11_CS2_full_v002_structural_truncation_preflight.py
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_ATTEMPT1_SMOKE.json
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_ATTEMPT1.json
```

