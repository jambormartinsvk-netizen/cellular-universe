# Akčný dodatok — upratanie koľají, skriptov a auditov

**Dátum:** 2026-07-16  
**Organizačný stav:** `ORG-V2-P1 COMPLETE`  
**Fyzikálny stav:** A2-K4/P5.3g7 je `REVIEW_BLOCKED_ARCHITECTURE`; hĺbka ostáva `60/100`

## Hotové

1. vytvorený kanonický route strom A1-K1/A2 pre K1–K9, K11 a K12;
2. A2-K10 oddelená pod správnu backgroundovú route A1-K2;
3. každá A1-K1/A2 koľaj má ľudský track, artefaktový manifest, base register
   a append-only HISTORY;
4. A2-K4/P5 má samostatné registre BASE, RUNNERS, RESULTS a AUDIT_THREADS;
5. historické skripty ostali na pôvodných cestách; nič sa nestratilo ani
   neduplikovalo;
6. zdieľané moduly majú jedného vlastníka, importujúce runnery, scope a
   SHA-256;
7. hlavné stavové súbory boli zosúladené na fyzikálnu hĺbku K4 `60/100` a
   P5.3g7 blocker;
8. SK/EN register dostal párové neduplicitné pravidlo AR69;
9. finálna kontrola: 157 explicitných ciest, 0 chýbajúcich; 11 base hashov,
   0 nezhôd.

## Čo sa zámerne neurobilo

Fyzické presunutie stoviek starých skriptov a auditov. Inventár našiel 468
závislostí a aktuálne nie je potvrdený Git baseline. Presun bez neho by
rozbil reprodukciu viac než by zlepšil poriadok. Nové route manifesty už
umožňujú auditovať každú koľaj samostatne.

## Budúca ORG-V2-P2 — až po Git baseline

1. pripojiť/overiť Git repository a vytvoriť baseline commit;
2. zmraziť úplný path/SHA manifest;
3. zostaviť závislostné komponenty `Path(__file__).with_name()` a wrapperov;
4. pilotne presunúť iba jeden komponent s `OLD_PATH → NEW_PATH` mapou;
5. overiť odkazy, hashe, syntax a parity bez fyzikálnej zmeny;
6. pokračovať po komponentoch alebo migráciu zastaviť, ak neprináša úžitok.

## Aktuálny vedecký krok

Najbližší vedecký krok po PF-058 nie je ďalší skript. Treba odvodiť ledger
`Phi^0/Phi^1 × z^j`, synchronné palivové `delta_f,U_f` species rows a pred
kódom uzavrieť total-energy/momentum Bianchi/left-null mapu. Až ledger určí
potrebný počet frakčných stavov. M1 anchor a štandardný seed sú PASS; explicitný S1
seed a finite opacity ostávajú otvorené. Až potom jeden plný seed, P5.4 a
podmienené otvorenie G8.

Audit reorganizácie:
`Audit/DIRECTORY_AND_BASESCRIPT_REORGANIZATION_AUDIT_2026-07-16.md`.
