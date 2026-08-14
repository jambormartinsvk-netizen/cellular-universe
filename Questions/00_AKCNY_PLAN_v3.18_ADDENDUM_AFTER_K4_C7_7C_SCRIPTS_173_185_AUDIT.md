# Akčný plán v3.18 — po audite skriptov 173–185

Dátum: 2026-07-15  
Stav: **A2-K4 ŽIVÁ, 66.5/100; K7c REVIEW**

## P0 — spevnenie autoritatívneho reťazca

1. V novom nemennom skripte nahradiť rank check explicitnou existenciou oboch kľúčov, typovou kontrolou, kladnosťou a rovnosťou. `.get(a)==.get(b)` samotné je zakázané.
2. Zopakovať fyzikálny `mu` gate na NID/NIV deep/shallow s rovnakými rovnicami a prahmi. Rozdiel oproti 175/176 smie byť iba fail-closed validácia dát.
3. V novom seed-handoff skripte odkázať na spevnený gate a exportovať identitu producenta, mód, povrch, `physical_mu`, rank a checksum zdroja.
4. Ak sa čísla oproti 175/176 zmenia, zastaviť K7c a zauditovať provenienciu. Ak sa nezmenia, K7b zostáva PASS bez nového bodu.

## P1 — poctivý K7c konvergenčný gate

1. Vytvoriť samostatnú implementáciu fixed RK4; nevkladať ju pred starý `solve_ivp` a nenechávať autoritatívny marker za skorým returnom.
2. Každý výstup označiť ako `independent_gate`, `enforced_identity` alebo `cancellation_monitor`. Tautológie a kancelácie majú `score_effect: NONE`.
3. Pred behom zaregistrovať tri vnorené mriežky, rovnakú normu endpoint rozdielu a pomer `previous/current`. Pre klasický RK4 smie asymptotický PASS vyžadovať preregistrované pásmo napríklad `8 < ratio < 32` okolo očakávania 16.
4. Zachovať aj absolútny endpoint prah `1e-6`; pomer ho nenahrádza. PASS vyžaduje oba testy.
5. Aktuálne dáta 184/185 sú REVIEW: `1.44327e-6 → 3.93124e-6`, pomer `0.367`. Ďalšie slepé zjemňovanie je zakázané.

## P2 — term ledger M-prime

1. Skript 186 ponechať bez zmeny ako nedokončenú technickú stopu.
2. Až po P0/P1 vytvoriť nový skript s novým číslom, ktorý pri rovnakých checkpointoch vypíše všetky členy `M'` a porovná bežný súčet, `math.fsum` a 80-dps súčet.
3. Každý child aj celý skript musí mať pevný limit; pri limite vzniká REVIEW.
4. Ak `math.fsum` zlepší chybu aspoň 10-násobne na každom aktívnom checkpointe, preregistrovať samostatnú fsum podkoľaj. Inak ju označiť za mŕtvu s ledgerom a skúmať algebraické preusporiadanie alebo vyššiu pracovnú presnosť.

## Skórovacia brána

Tieto opravy sú auditná robustnosť a nepridávajú body. `66.5/100` sa môže zvýšiť až po skutočne konvergovanej krátkej evolúcii a neskôr podľa už registrovaného štvorpovrchového K7d rozsahu.
