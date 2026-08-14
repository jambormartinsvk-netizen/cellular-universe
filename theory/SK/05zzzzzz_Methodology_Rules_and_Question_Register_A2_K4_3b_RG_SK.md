# Dodatok k 05 — A2-K4.3b-RG, backendové nuly a rád gauge mapy (SK)

**Dátum:** 2026-07-14  
**Stav:** záväzný dodatok; staršie pravidlá sa nemenia

## Kontrola duplicity

AR31 prikazuje posudzovať regulárnosť gauge-invariantne. Nehovorí však, ako
zaobchádzať s nulovými riadkami pred interným štartom numerického backendu
ani koľko rádov zdrojovej série treba pri transformácii do gauge s
cancellation alebo Laurentovým správaním. AR32 a AR33 dopĺňajú tieto dve
odlišné medzery; staršie pravidlá neduplikujú.

## AR32 — Backendový nulový prefix nie je fyzikálny seed

Pred použitím časového výstupu solvera sa musí určiť jeho prvý aktívny
perturbačný riadok. Presný nulový prefix, ktorý backend vracia pred internou
inicializáciou, sa eviduje ako placeholder a nesmie vstúpiť do ranku,
normalizácie, rezídua ani fyzikálneho rozsudku.

Ak sa aktívny štart nedá jednoznačne určiť, test zostáva neuzavretý.

## AR33 — Gauge transformácia musí mať dostatočný rád

Regulárny zdrojový rad sa smie mapovať do inej gauge iba vtedy, ak obsahuje
všetky koeficienty, ktoré po zrušení vedúcich členov prispievajú k cieľovej
veličine. Konečný nenulový čas sám osebe nie je dôkazom dostatočného rádu.

Ak skrátený synchronous NID/NIV rad po Newtonovskej transformácii vyrobí
veľkú hodnotu alebo poruší nulový limit, najprv sa musí otestovať vyšší rád
alebo zostať v regulárnej gauge. Takýto interface failure nie je fyzikálnou
smrťou.

## Q59a — Prešli všetky siedme rady?

**Stav:** `ČIASTOČNE.`

- päť kolektívnych regulárnych synchronous seedov prešlo;
- dva interné `nu-steam` rady prešli exact;
- general-synchronous K4 test-field odpoveď prešla;
- full back-reacted Puiseux rady a spoločné `00/0i/slip/ij` rezíduá chýbajú.

K4 preto zostáva živá na `60/100`, ale K4.3b nie je uzavretá.

## Q60 — Je interný `nu-steam` PASS bezpodmienečný?

**Odpoveď:** Nie. Platí v S1, kde už decouplovaná para má rovnaký
bezkolízny operátor ako neutrína a K4 na ňu priamo nepôsobí. Pri zavedení
priameho prenosu do parnej hierarchie musí vzniknúť nová kinetická koľaj a
rank, kompenzácia aj constrainty sa auditujú znovu.

## Q61 — Čo ešte chýba na uzavretie K4.3b?

Back-reacted general-synchronous Puiseux solver musí zahrnúť fuel
stress-energy v ráde `a^(4-3delta)=a^3.93109`, následnú ash korekciu
`a^(5-3delta)=a^4.93109` a pre všetkých sedem módov prejsť `00`, `0i`, slip,
`ij`, nulový limit a dve štartové hĺbky.

