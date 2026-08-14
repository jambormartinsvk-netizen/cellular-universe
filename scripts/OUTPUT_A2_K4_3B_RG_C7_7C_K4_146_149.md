# Výstup skriptov 146–149 — A2-K4 C7.7c-K4

## Účel

Reprodukovateľný záznam pokusu rozlíšiť aktivitu všetkých 13 zložiek BR3C-b pomocou analytickej obálkovej normalizácie.

## Skripty

- `146_script_A2_K4_3b_RG_C7_7c_K4_analytic_reference_state.py`
- `147_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_evolution.py`
- `148_script_A2_K4_3b_RG_C7_7c_K4_analytic_envelope_activity_audit.py`
- `149_script_A2_K4_3b_RG_C7_7c_K4_manifest_sha256.py`

## Výsledky

### Skript 146

- verdict: `PASS_C7_7C_K4_ANALYTIC_REFERENCE_STATE`
- kontroly: 94/94 PASS
- `NID/reference/L4_fs = 1.8039092102682284e-24`
- `NIV/reference/L4_fs = 5.135204691461256e-20`

Referenčná plocha je iba numerická mierka. Nie je to numericky evolvovaný koncový stav.

### Skripty 147–148

- evolučný interný limit: 45 s
- auditný obal: 50 s
- externý limit: 60 s
- pozorovaný čas obalu: približne 46,4 s
- verdict: `ERROR_UNCLOSED`
- vnorený verdict: `TIMEOUT_UNCLOSED`
- chyba: `BR3C-b internal deadline exceeded`

Brána aktivity nebola vyhodnotená, pretože nevznikol úplný výsledok všetkých trajektórií.

## Bodovanie

Predregistrovaných `+0,2` bodu sa neprideľuje. A2-K4 ostáva na `66,5/100`.

## Reprodukcia

Každé spustenie musí zachovať tri limity. Ak sa optimalizuje implementácia, vznikne nová očíslovaná podkoľaj a nové skripty; tieto súbory sa neprepisujú ani nemažú.

