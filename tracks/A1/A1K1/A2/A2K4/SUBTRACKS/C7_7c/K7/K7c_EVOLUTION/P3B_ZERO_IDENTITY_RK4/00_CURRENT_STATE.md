# P3b — RK4 po kanonizácii presných núl

Stav: **PASS na izolovanej krokovej bráne**  
Stabilné ID: `SCI-A2K4-C7G5-K7C-P3B-ZERO-IDENTITY-RK4`  
Score effect: `NONE`

Skript 205 zmenil voči P1 iba dva koeficienty, ktoré P3a-A dokázalo ako
presné nuly. Na mriežkach 100/200/400 dosiahol `diff200/400 =
3.0308221211e-14` a pomer `16.004121`. Obe preregistrované brány prešli.

Tento PASS obmedzuje starý P1 FAIL na legacy float64 zápis. Neuzatvára celý
C7-G5, G4 ani G6. Najbližší krok je samostatne preregistrovaný metódový a
tolerančný cross-check, potom netautologická aktivita a štyri plochy.

