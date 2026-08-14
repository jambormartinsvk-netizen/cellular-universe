# Dodatok k 05 — A2-K4.3b, gauge-regulárnosť a rozšírená báza (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR28 vyžaduje, aby primordiálny kill test patril do úplnej regulárnej bázy.
Neurčuje však, v ktorých premenných sa posudzuje regulárnosť, ani čo sa
stane, keď rozšírenie druhov pridá velocity-isocurvature módy so singulárnymi
Newtonovými potenciálmi. AR31 dopĺňa túto chýbajúcu gauge podmienku; AR28
nenahrádza ani neduplikuje.

## AR31 — Primordiálna regulárnosť sa posudzuje gauge-invariantne

Koľaj alebo mód sa nesmie zabiť iba preto, že potenciál alebo rýchlostná
premenná diverguje v jednej gauge, ak sú frame-invariantné fyzikálne
veličiny a vhodná regulárna gauge konečné.

Pred rozsudkom treba:

1. identifikovať gauge-invariantnú krivostnú, entropickú a relatívnu
   rýchlostnú veličinu;
2. zostaviť počiatočný rad v gauge, kde je mód regulárny;
3. až pri konečnom čase vykonať explicitné gauge mapovanie;
4. odlíšiť gauge singularitu od divergencie invariantného tenzora alebo
   fyzického transferu;
5. po pridaní nového druhu znovu auditovať dimenziu úplnej bázy.

Staršia báza zostáva úplná iba pre presne deklarovaný druhový a uzáverový
systém. Nesmie automaticky zdediť označenie „úplná“ po rozdelení jednej
tekutiny na viac kinetických zložiek.

## Q59 — Prešla A2-K4 podbránou K4.3b?

**Stav:** `NEUZAVRETÁ; K4 ŽIVÁ 60/100; ŽIADNY NOVÝ DÔVOD SMRTI.`

Prešli:

- úplný hierarchy ledger a krížová kontrola s CAMB 1.6.6;
- exact rozklad neutrín a S1 pary na kolektívnu a internú hierarchiu;
- Thomsonov collision block;
- nulový rekombinačný/tight-coupling interface.

Audit ukázal sedem nezávislých štandardných analytických skalárnych módov.
K4.1 mala tri, pretože používala jednu perfektnú radiačnú tekutinu. Jej
starší výrok bol správny v deklarovanom rozsahu, ale po rozšírení druhov už
nie je úplným G7 tvrdením.

Dva velocity-isocurvature módy majú `U~1/(k tau)` a singulárne Newtonove
potenciály, hoci gauge-invariantný mód je regulárny. K4.3b čaká na sedem
konečno-štartových radov v regulárnej gauge vrátane podvedúcich K4 členov.

**Ďalšia otázka Q59a:** Prejdú všetky siedme rady reziduálnymi `00`, `0i`,
slip, `ij`, gauge-map a linearity testami?

