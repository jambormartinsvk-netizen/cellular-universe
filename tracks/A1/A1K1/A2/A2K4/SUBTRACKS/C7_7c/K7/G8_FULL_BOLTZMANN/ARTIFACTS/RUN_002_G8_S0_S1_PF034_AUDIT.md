# RUN-002 — audit G8 SCREEN-S0+S1 po PF-034

**Verdikt:** `PASS_G8_SCREEN_S0_S1_STRUCTURAL`  
**Skóre:** `0` — support/WBS zostáva `90/100`  
**Fyzikálna evolúcia:** nie; ODE, rekombinácia ani CMB likelihood nebežali.  
**Autoritatívny strojový artefakt:** `RUN_002_G8_S0_S1_PF034_RESULT.json`

**SHA-256 JSON:** `7205D4680445F877A7D3AFC9AEB4DDC68E3194F8AA422ED3E772AF65B479971E`

## Výsledok

Prešlo **40/40** kontrol, každá so symbolickým rezíduom presne `0`.

Nezávislá post-run čítacia kontrola JSON potvrdila `CHECK_COUNT=40`,
`FAILED_COUNT=0`, všetky exportované rezíduá `0` a prítomnosť RUN-002 v
G8 manifeste.

- 22/22 CAMB koeficientov `J`, `E`, `G` a polarizačného zdroja;
- stavové registre: 32, 44, 56 pre `lmax=8,12,16` a presné poradie;
- všeobecná škálovaná bezkolízna rekurencia sa pre `l=3,4` presne zredukuje
  na K7, vrátane registrovaného limitu `L5=0`;
- Thomsonov člen presne ruší váženú fotónovo-baryónovú hybnosť;
- oddelené Eulerove rovnice v tight-coupling limite presne vracajú K7
  kombinovaný Euler a jeho `load_fraction`/`inv1r` zápis;
- plná definícia projektovaného `M` sa pri `U_b=U_gamma` vracia na K7.

Vnútorná algebra trvala `0.875 s`; celý Python proces vrátane importu CAMB
trval približne `6.0 s`, pod externým limitom `15 s`.

## Obmedzenie RUN-001

RUN-001 zostáva zachovaný a označený `TECHNICAL STOP`. Jeho 39/40 výsledok
nebol fyzikálny konflikt: chýbala len definujúca substitúcia
`inv1r=1/(1+R)`. PF-034 vytvoril samostatný runner 233, nepremenil výsledok
221 ani ho neprepísal. RUN-002 túto jedinú identitu testuje správnym smerom;
zvyšných 39 kontrol pochádza z nezmeneného modulu 221.

## Čo tento PASS znamená a neznamená

PASS dokazuje iba to, že deklarovaný budúci G8 operátor sa algebraicky
správne napája na K7 a používa auditované CAMB koeficienty. Nedokazuje
numerickú stabilitu, TCA/direct overlap, convergence v `lmax`, rekombináciu,
Einsteinove constrainty počas evolúcie ani kompatibilitu s CMB/S8 dátami.
Preto nepridáva bod ani nemení fyzikálny verdikt K7.

## Ďalší krok

Povolený je `SCREEN-S2` (skript 222): jedna krátka skorá evolúcia na
presnom K4 backgrounde s oddeleným TCA/direct operátorom, interným limitom
45 s a externým limitom 55 s. Pred ním musí vzniknúť nová predregistrácia
očakávania; nesmie sa preskočiť na S3 alebo FULL.
