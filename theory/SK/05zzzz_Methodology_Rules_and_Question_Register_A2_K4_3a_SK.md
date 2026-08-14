# Dodatok k 05 — stav A2-K4.3a (SK)

**Dátum:** 2026-07-14  
**Rozsah:** otázka registra a obmedzenie interpretácie; staršie pravidlá sa nemenia

## Kontrola duplicity pravidiel

Nové pravidlo sa nepridáva. AR30 už prikazuje udeľovať skóre iba za celú
sekvenčne prejdenú bránu a existujúce pravidlá už vyžadujú nulové,
konzervačné a znamienkové testy. Tento dodatok iba zaznamenáva výsledok
čiastkovej otázky K4.3a a bráni jej zámene s celou G7.

## Q58 — Je rozhranie druhov a anisotropného stresu K4.3 pripravené na plnú Boltzmannovu implementáciu?

**Stav:** `K4.3a FORMULAČNE PREŠLA; K4 OSTÁVA 60/100; G7 JE OTVORENÁ.`

Prešli presné algebraické kontroly:

- párová konzervácia energie a hybnosti K4;
- Einsteinov anisotropný constraint a limit `Psi -> Phi`;
- návrat `0i` rozhrania ku K4.2 pri nulovom anisotropnom strese;
- agregácia fotónov, neutrín a pary na perfektnú radiáciu v deklarovanom limite;
- vyrušenie Thomsonovej hybnosti medzi baryónmi a fotónmi.

Test neobsahoval úplnú fotónovú polarizačnú hierarchiu, tight coupling,
rekombináciu, regulárnu bázu rozšíreného systému ani fyzické transfery.
Preto neuzatvára G7 a nemení skóre.

Vetva pary S1 je predregistrovaná ako voľne letiace extra žiarenie, pretože
takto ju používala doterajšia CAMB referencia. S2 (samointeragujúca para) a
S3 (odvodený sieťový kolízny kernel) zostávajú samostatné čakajúce vetvy;
smrť jednej automaticky nezabíja ostatné.

**Ďalšia otázka Q58a:** Prejde K4.3b úplnou hierarchiou, tight coupling,
rekombináciou a úplnými regulárnymi počiatočnými módmi bez porušenia
constraintov?

**Auditná stopa:**

- `Questions/A2_K4_3_G7_PROBLEM_PODBRANY_A_KILL_KRITERIA.md`;
- `Audit/A2_K4_3A_SPECIES_LEDGER_ANISOTROPIC_STRESS_AND_NULL_AUDIT.md`;
- `scripts/72_script_A2_K4_3a_species_ledger_and_anisotropic_stress_audit.py`;
- `scripts/OUTPUT_A2_K4_3A_72.md`.

