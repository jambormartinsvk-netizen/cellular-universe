# KMPC-087 — BI/k=.15 high-precision driver assembly: výsledok a interný audit

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu a interný audítor:** Codex (OpenAI)  
**Stav:** `INTERNALLY_AUDITED / VALID_REVIEW`  
**Autoritatívny výsledok:** `REVIEW_C2_BI_K0p15_UPSTREAM_COEFFICIENT_PRECISION_REQUIRED`

## Dôkazová identita

- predregistrácia 148 pred behom:
  `0136ED90A1AD3EECABBA6EC78E44A32F42A75844DB271C85775765732DFF95DC`;
- výpočtový modul:
  `4C11A3EE3C08B084E53E5F313152A29C768E2F0F48D74588D0F5E37688B50B46`;
- runner 331:
  `F297F116ADC873999AF15E41CA3D4CCB9110293C8E97B404A86E607B6471400C`;
- immutable raw `RUN_KMPC_087_P5_3G7_C2_BI_K0p15_HIGH_PRECISION_DRIVER_ASSEMBLY.json`:
  `EA0B4403318516D4503379246A882222E64681CB0248A4EFB00F10201CCE2144`;
- pred prvým Python behom sedelo `32/32` deklarovaných source/prerequisite
  hashov a všetky hash literály mali 64 hex znakov;
- samostatné `py_compile`, `--help`, behaviorálny smoke a official beh
  skončili exit code 0. Official runtime payloadu bol `33.328 s`.

## Zistené čísla

| Kontrola | Výsledok | Brána |
|---|---:|---|
| baseline float64-assembled driver SHA | `FE5E5A7C...127240F` | parita s KMPC-083/086 |
| 80-dps driver matrix+constant SHA | `CEBB46C4...43EF2` | nová exact-assembly identita |
| zmenené affine položky | `678 / 10920 = 6.20879 %` | diagnostika |
| najväčšia absolútna assembly zmena | `2.0448033936872889e-13` | `Einstein_traceless[6]::eta[6]` |
| exact-driver maximum | `8.720279045183271e-82` | PASS, limit `1e-10` |
| exact holdout `Einstein_0i[7]` | `3.019756577618421e-9` | FAIL, limit `1e-9` |
| absolútny residual `Einstein_0i[7]` | `-5.497017142831483e-17` | diagnostika |
| holdout riadky pridané do solve | `0` | PASS |
| high-precision solve celkom | `2` | PASS: baseline 1 + exact driver 1 |

Oproti KMPC-086 (`3.0197567116259885e-9`) sa holdout metrika zmenila iba o
`-1.340075676e-16`, relatívne `-4.437694e-8`. Nová hodnota je stále
`3.0197566`-násobok prahu, teda približne `201.98 %` nad ním. High-precision
zostavenie drivera preto hranicu prakticky neposunulo.

## Interný audit

1. Poradie 13 stavov a 13 driver rovníc zodpovedá
   `full_ra_contract.py`; 104x104 systém vzniká z nuly a 104 jednotkových
   afinných sond pri 80 dps.
2. Prepis driver rovníc bol riadok po riadku porovnaný s
   `full_ra_m3_seed.py`: nezmenil znamienka, koeficienty, support ani
   normalizáciu. Binary64 upstream čísla sú prenesené presne cez ich binárny
   pomer, nie cez zaokrúhlený desiatkový text.
3. Driver bol ekvilibrovaný po riadkoch a stĺpcoch a vyriešený cez
   `mpmath.lu_solve`; jeho vlastný residual prechádza s rezervou približne
   71 rádov voči `1e-10`.
4. `Einstein_00/0i` ostali 16x104 nezávislým holdoutom. Ich fingerprint
   `2DE8C982...06E2DE` sa zhoduje s KMPC-086 a počet pridaných riadkov je
   nula.
5. Owner lifecycle, source hashes, prerequisite hashes, serializácia,
   immutable output a autorstvo prešli. Nevznikol technický incident;
   aktívny counter sa po vecnom výsledku drží na `0/10`.
6. Reportingová poznámka: zdedený top-level `contract_guard` v raw nezobrazil
   štyri nové driver-specific názvy kontrol, pretože rodič používa skoršie
   naviazaný guard. Povinné fakty sú však priamo v
   `high_precision_driver_assembly_boundary`, v smoke výstupe a v source;
   nejde o numerickú ani fyzikálnu chybu. Ďalší balík má tieto kontroly
   vyžadovať priamo vo svojom field-level preflighte.

## Autoritatívna interpretácia

KMPC-087 vylučuje float64 zostavenie 104x104 driver matice ako vysvetlenie
holdout hranice v tomto atóme. Spolu s KMPC-083 a KMPC-086 je teraz
vylúčený solve-roundoff, posledné holdout zostavenie/odčítanie aj driver
assembly roundoff. Zostávajúci presne pomenovaný scope je upstream: M1,
F0/fuel a background koeficienty boli stále vytvorené v binary64.

Toto nie je dôkaz nesprávnej rovnice ani fyzikálny STOP. BI/k=.15 sa
nepripočítava; C2 ostáva `5/10 PASS`, P5 `3.5/6` a K4 `LIVE / 60/100`.
Release, Zenodo a prediction-table trigger sú `NONE`.

## Ďalší predregistrovaný smer

Najprv sa vytvorí jeden read-only coefficient-attribution successor, ktorý
pre `Einstein_0i[7]` exportuje úplný konvolučný term ledger a oddelí
príspevky backgroundu, štandardného M1 stavu, F0/fuel vstupu a exact-driver
neznámych. Holdout ostane mimo solve a rovnice/prah sa nemenia. Až podľa
dominantného a auditovateľného zdroja sa znovu zostaví najmenší potrebný
upstream generátor pri vysokej presnosti; nebude sa naslepo prepisovať celá
pipeline.
