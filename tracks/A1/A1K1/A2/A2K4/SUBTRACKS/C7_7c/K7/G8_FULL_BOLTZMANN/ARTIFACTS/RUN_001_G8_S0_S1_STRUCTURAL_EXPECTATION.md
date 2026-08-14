# RUN-001 — G8 SCREEN-S0+S1: očakávanie pred behom

**Dátum:** 2026-07-15  
**Rodič:** `A1-K1 → A2-K4 → C7.7c-K7 → G8`  
**Skript:** `scripts/221_script_A2_K4_C7_7c_K7_G8_S0_S1_structural_audit.py`  
**Fyzikálny stav pred behom:** `K7d G0–G7 PASS; G8 NOT RUN; support/WBS 90/100`

## Čo sa počíta ľudskou rečou

Toto nie je simulácia vesmíru ani fit dát. Kontroluje sa iba algebra, ktorá
musí platiť skôr, ako má zmysel spúšťať drahú plnú Boltzmannovu hierarchiu.
Skript porovná CAMB koeficienty, spočíta presný register budúcich stavov,
overí, že vyššie multipóly pri `l=3,4` vrátia dnešné K7 rovnice, a že
Thomsonov rozptyl len prenáša hybnosť medzi fotónmi a baryónmi — nevytvára
ju z ničoho. Nakoniec sa oddelené fotónové a baryónové Eulerove rovnice
v tesnom väzobnom limite musia presne zložiť späť na aktuálny kombinovaný
K7 Euler.

## Očakávanie a hranice

- CAMB: presne `22/22` nulových symbolických rezíduí;
- registre: presne `32`, `44`, `56` stavov pre `lmax=8,12,16`;
- K7 redukcie, Thomsonova hybnostná kancelácia a kombinovaný Euler: všetky
  symbolické rezíduá sú presne `0`;
- runtime: bez ODE a bez fitu, vnútorný deadline `10 s`, vonkajší timeout
  `15 s`.

Prijateľný fyzikálny výsledok SCREEN-u je iba úplný PASS všetkých presných
identít. Tento PASS však nemení skóre: `score_effect=0`, pretože ešte
neexistuje rekombinačný/full-hierarchy beh na K4 backgrounde.

## Rozhodnutie po behu

- **PASS:** zapísať immutable JSON, audit, manifest; povoliť iba SCREEN-S2
  skript 222.
- **symbolická nezhoda:** `STOP_G8_IMPLEMENTATION_MAPPING`; zastaviť G8
  implementáciu a auditovať mapovanie, nie vyhlásiť fyzikálnu smrť K7.
- **import/parser/timeout:** technický `REVIEW`; zachovať skript a výsledok,
  použiť najviac dve predregistrované technické opravy.

## Preflight podľa error ledgeru

Pred autoritatívnym behom sú povinné oddelené, krátke procesy: `py_compile`,
`--help`, `--smoke`, až potom samotný JSON export. Žiadne z nich neobsahuje
ODE. Každý má vlastný vonkajší timeout; `--smoke` ani preflight nevytvára
autoritatívny výsledok.

## Dodatok po technickom preflighte

Oprava PF-032 prešla `py_compile`. Prvý `--help` však korektne skončil na
vonkajšom limite `10 s` počas importu CAMB; nebol vykonaný SCREEN ani export.
Predregistrovaný limit pre exact/structural balík je `15 s`, preto je
dovolený jeden opakovaný izolovaný import/CLI beh s vonkajším limitom `15 s`.
Ak ani ten neprejde, G8 ostane technické `REVIEW`; nepovolí sa obchádzanie
importu ani dlhší neobmedzený proces.
