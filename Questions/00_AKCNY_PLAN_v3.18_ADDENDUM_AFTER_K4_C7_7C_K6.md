# Akčný plán v3.18 — po smrti C7.7c-K6

**Dátum:** 2026-07-14  
**Aktívna koľaj:** A2-K4  
**Jemná hĺbka:** `66.5/100`  
**Stav:** živá; C7.7c otvorená; ďalší krok K7a bez ODE evolúcie.

## Dokončené

1. C7.7c-K4 analytická obálka — mŕtva numerická podkoľaj.
2. Segmentový profil a lokálny Jacobian — dokončené bez bodov.
3. C7.7c-K5 maticové vyváženie — mŕtva numerická podkoľaj.
4. C7.7c-K6 fyzikálny stav s vektorovým `atol` — mŕtva numerická podkoľaj.
5. Počiatočná condition mapa — PASS ako diagnostika; NID hustota/`h_x` lokalizované pod roundoff hranicou.

## Bezprostredné kroky

1. **K7a.1:** odvodiť `D'` z backgroundových `Omega_A'` a všetkých kontinuitných rovníc.
2. **K7a.2:** odvodiť `M'` z Eulerových rovníc a backgroundových derivácií.
3. **K7a.3:** získať NID/NIV počiatočné Puiseuxove koeficienty `D,M` bez double odčítania.
4. **K7a.4:** overiť nulový limit, znamienka a NIV direct-sum kontrolu `<10^-10`.
5. **K7b:** až potom koeficientový a constraintový audit.

## Zakázané skratky

- ďalšie predlžovanie timeoutov K4–K6;
- ďalšie plošné znižovanie `atol`;
- označenie tiny komponentu za aktívny iba podľa názvu alebo nenulového počiatočného kľúča;
- spustenie K7 evolúcie pred PASS K7a/K7b;
- zvýšenie skóre pred úplným C7.7c PASS.

## Neskoršie kroky po K4

Po uzavretí alebo fyzikálnej smrti A2-K4 pokračuje pôvodný plán A1-K1/A2. Dokumentačné upratanie, logické adresáre, GitHub commit pred Zenodo a publikačný changelog zostávajú otvorené, ale nemenia aktuálny fyzikálny rozsudok.

