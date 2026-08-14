# Akčný plán v3.18 — korekcia Jacobianovej diagnostiky 151/152

**Dátum:** 2026-07-14  
**Skóre:** bez zmeny, `66.5/100`  
**A2-K4:** živá; C7.7c otvorená.

## Záväzná korekcia

- `max|J|`, SVD a condition proxy skriptov 151/152 sú vlastnosti obálkových numerických súradníc, nie fyzikálne invarianty.
- `scaled_jacobian_resolved_condition_proxy` je stiahnutý a nesmie vstupovať do ďalšieho rozsudku.
- Spektrálny polomer zostáva iba kontrolou podobnostnej transformácie a musí sa krížovo overiť proti fyzikálnemu Jacobianu.

## Krátky technický dlh bez ODE

Keď shell vrstva opäť spoľahlivo vracia krátke procesy:

1. zostaviť `J_y` priamo z bázových vektorov;
2. analyticky vytvoriť `J_local` a `J_env`;
3. porovnať spektrá;
4. spraviť FD sweep `10^-4...10^-8`;
5. zapísať meranú FD chybu a až z nej prípadný SVD cutoff.

Tento technický dlh nepridáva body a neoprávňuje nový evolučný beh.

## Hlavný fyzikálny ďalší krok

K7a projektovanej kompenzovanej bázy ostáva prioritou, pretože vychádza z nezávislej termovej condition mapy 155/156, nie zo stiahnutého SVD proxy.
