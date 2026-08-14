# K11-CS2 full v002 — posledná oprava po PF-062

**Dátum zmrazenia:** 2026-07-16  
**Koľaj:** `A1-K1 -> A2-K11 -> K11-R -> K11-CS2`  
**Stav:** `PREREGISTERED / NOT_EXECUTED`  
**Technická oprava:** `2/2 — posledná; v003, CS3 ani tretí rerun nevzniknú`  
**Fyzikálna hĺbka:** bez zmeny, `10/100 = G1`  
**Autorita budúceho verdiktu:** iba hlavný orchestrátor

Tento dodatok nemení pôvodnú CS2 predregistráciu ani PF-062 erratum.
Spresňuje poslednú dovolenú implementáciu tak, aby odstránila chybný register
stavov, hornú multipólovú dieru a možnosť zameniť aproximovanú termálnu
históriu za fyzický dôkaz.

## 1. Ľudskou rečou

Výpočet má sledovať všetky malé poruchy vesmíru od skorého obdobia po
dnešok a zistiť, či regulárne trenie K11-R naozaj zastaví nebezpečný
relatívny pohyb paliva a popola. Nestačí však vypočítať iba tieto dve
zložky. Fotóny, baryóny, neutrína, para a metrika si počas evolúcie
odovzdávajú hybnosť a určujú Einsteinove constrainty.

Posledný full beh sa preto spustí iba vtedy, keď jeden versioned base
obsahuje celý fyzický systém. Ak by sme použili termálnu históriu z iného
backgroundu alebo horný multipól bez uzáveru, výsledok by nevedel rozlíšiť
fyzickú nestabilitu od chyby implementácie.

## 2. Autoritatívny ordered state contract

Pre `L=lmax` je jediný povolený register

```text
Phi,
delta_c, W_c,
delta_f, W_f,
delta_b, W_b,
delta_gamma, W_gamma,
F_gamma_2, ..., F_gamma_L,
E_gamma_2, ..., E_gamma_L,
delta_nu, W_nu, F_nu_2, ..., F_nu_L,
delta_steam, W_steam, F_steam_2, ..., F_steam_L.
```

`Psi` je algebraická premenná určená slip rovnicou. Nie je evolvovaným
stavom. Presný počet je

```text
state_count = 4*L+9,
L=4 -> 25,
L=6 -> 33,
L=8 -> 41.
```

Register sa porovná s explicitným nadradeným ordered manifestom. Count,
unikátnosť a kontrola prvého/posledného mena samy nie sú parity dôkaz.
Rovnaká exact parity sa vyžaduje medzi stavmi a RHS riadkami.

Povinné negatívne fixtures musia odmietnuť:

- pridané `E_gamma_0` alebo `E_gamma_1`;
- chýbajúce `E_gamma_2` alebo `F_steam_L`;
- rovnako dlhý register s `fake_state` namiesto `E_gamma_2`;
- duplicitu alebo prehodené poradie;
- runnerom vytvorenú lokálnu kópiu registra.

## 3. Multipólové rekurencie a horný uzáver

Generic CAMB koeficientové identity sa používajú iba pre
`2 <= ell < L`. Pri `ell=L` by generic riadok odkazoval na neregistrovaný
`L+1` stav. Full v002 preto musí mať pre každú rodinu

```text
F_gamma, E_gamma, F_nu, F_steam
```

explicitný vopred zapísaný regulárny top closure. V superhorizontovom
rozsahu sa referenčný closure odvodí z regularnej Bessel/Frobeniovej vetvy,
nie nastavením `F_(L+1)=0` bez auditu. Všetky RHS závislosti musia spĺňať

```text
RHS.keys == ordered_state_manifest,
dependencies(row) subset state_manifest + declared algebraic/background inputs.
```

Povinný negatívny fixture s odkazom na `*_L+1` musí zlyhať. Closure sa
overí sweepom `L=4,6,8`; nízke spoločné stavy sa párujú podľa mena, nie
pozičným slice.

## 4. Exact-A1 background a thermal history

Fyzický profil musí používať jediný módovo nezávislý A1 background:

```text
X_f,N = -3 delta X_f-lambda X_f/E,
X_c,N = -3 X_c+lambda X_f/E,
X_b,N = -3 X_b,
X_r,N = -4 X_r,
E^2   = X_f+X_c+X_b+X_r.
```

Z dnešných vstupov sa explicitne zostavia
`Omega_b0, Omega_c0, Omega_gamma0, Omega_nu0, Omega_steam0, Omega_f0`.
Povinné sú flatness, positivity, zrušenie párového transferu a analytické
`s=d ln mathcal H/dN`. Perturbatívne `k`, historické `K_MPC`, opacity ani
interpolácia nesmú vstúpiť do `H`, `Omega_A`, `Gamma/H` alebo
`Upsilon/H`.

Fyzický beh do `a=1` navyše potrebuje

```text
K_T(a)=a n_e(a) sigma_T/mathcal H(a) >= 0,
x_e(a), T_b(a), c_b^2(a), visibility(a)
```

vypočítané na tom istom exact-A1 `H(a)`. Musia byť pripnuté:

- zdroj a verzia recombination/HyRec implementácie;
- `T_CMB`, helium fraction a atómové konštanty;
- reionizačný profil alebo jeho explicitný observačný vstup;
- jednotky, interpolácia a povolené hranice tabuľky;
- nulový referenčný beh backendu pred A1/K11 zmenou.

Kopírovaná ΛCDM/CAMB opacity tabuľka, `opacity=0` alebo konštantné skúšobné
`chi` smú byť iba diagnostickým fixture. Nemôžu udeliť fyzický PASS ani
STOP. Existujúci source-auditable CLASS/HyRec reference backend možno
použiť až po samostatnom exact-A1 adapteri a jeho nulovom teste.

## 5. TCA a handoff

Ak skorá tuhá časť používa tight-coupling approximation, redukovaný TCA
stav musí mať vlastný state/row manifest a presnú mapu do 41-stavového
registra. Povinné sú:

- `opacity -> 0` limit;
- skorý spoločný photon-baryon velocity limit a správny shear/slip rád;
- TCA/full overlap bez skoku stavu, RHS a `00`/trace rezíduí;
- citlivosť na posun switch plochy alebo zvýšenie TCA rádu;
- presné vážené zrušenie Thomsonovej hybnostnej reakcie.

Post-recombination handoff je fyzicky prípustný iba po nezávislom skorom
výpočte celej regulárnej bázy, ktorý preukáže vynechanú chybu `<1e-5` v
stave aj fyzickej norme a prenesie polarizáciu, NID/NIV, steam aj fuel módy
s constraintmi. Samotný CAMB/ΛCDM seed alebo štart pri `z_star=1089.9`
znamená `REVIEW_BLOCKED_SEED_HANDOFF`.

## 6. Rovnice, conservation a netautologické holdouty

Dark rovnice, K11-R operátor a nulové profily ostávajú presne podľa hlavnej
CS2 predregistrácie. Navyše base musí mať:

1. všetky finite-`k` členy `epsilon^2=(k/mathcal H)^2`;
2. samostatnú neutrínovú aj parnú hierarchy/shear;
3. term-by-term total-energy a total-momentum ledger;
4. presné zrušenie dark transferu, K11 dragu a Thomsonovej reakcie;
5. regresný COMP fixture, ktorý zachová density/momentum compensation, ale
   reprodukuje nenulový pressure escape a zapnutie metriky/species.

`0i` evolvuje `Phi` a slip určuje `Psi`; tieto dva riadky nie sú nezávislé
holdouty. Povinné nezávislé kontroly sú:

- `00` bez priebežnej projekcie stavu na constraint;
- trace Einsteinova rovnica z analytických RHS derivácií a nezávislého
  `delta p_total`;
- total-energy a total-momentum conservation zostavené druhou cestou;
- Bianchi/left-null mapa `c_N+cA` porovnaná s nezávislým conservation
  výrazom.

Absolútny fallback sa používa pri near-zero norme; pomer šum/šum sa
neinterpretuje ako fyzikálny FAIL. Zmena jedného znamienka v dark,
Thomson alebo shear riadku musí Bianchi fixture odhaliť.

## 7. Tri fyzické profily a dve nezlučované metriky

Povinné sú:

```text
FULL_K11     = exact A1, Gamma>0, Upsilon_R,
DRAG_NULL_K1 = bitovo ten istý A1/thermal background, Upsilon=0,
COMMON_NULL  = prepočítané lambda=Gamma=Upsilon=0 vrátane thermal history.
```

`NONPHYSICAL_OPERATOR_NULL` ostáva iba algebraický fixture.

Predbehové očakávania sa odteraz zapisujú oddelene:

```text
absolútny K1-like relative rast FULL: ln A_full približne 10 až 13,
samotný účinok K11-R dragu:
ln(A_full/A_drag_null) približne -0.14.
```

Tieto veličiny sa nesmú zlúčiť. Primárny údaj je absolútna najväčšia
singular value fyzickej mapy; osobitne sa reportuje gauge-invariantný
`W_f-W_c`, curvature, total density, `Phi` a `Psi`.

## 8. Konvergencia

Zostávajú prahy hlavnej CS2 predregistrácie. Spresnenie sa porovnáva na
pevných fyzických checkpointoch, nie iba v endpointe. Pri adaptívnych
metódach sa nevyžaduje RK4 pomer 16. Nad floorom musí jemnejší rozdiel
spĺňať

```text
D_fine < 1e-6,
D_fine <= D_coarse/3.
```

Pod numerickým floorom sa hodnotí absolútny rozdiel, nie pomer. Povinné je
porovnanie nezávislých metód, skorších štartov, `k -> k/2`, amplitúd,
holdout rezíduí a `L=4,6,8`. Pri `lmax` sa spoločné stavy mapujú presne
podľa mien.

## 9. Verdict vetvy

### `STABILITY_PASS_SCOPE_K11_R`

Iba ak prejdú exact-A1 thermal history/handoff, úplná báza, state/row
parita, všetky holdouty a konvergencie a na každej konfigurácii platí
`ln A_full <= 1` pre relatívny sektor a počiatočná amplitúda `1e-5`
zostane vo fyzickej norme `<1`.

### `STOP_SCOPE_K11_R`

Iba po úplnom technickom PASS, ak robustný constraint-compatible
gauge-invariantný mód dá `ln A_full>1`, nekonvergentný rast pri skoršom
štarte/`k->0`, dosiahne nelineárnu normu alebo stabilita vyžaduje anti-drag,
nový fit či singularitu `1/delta`.

### `REVIEW_BLOCKED_IMPLEMENTATION`

Povinné pri chýbajúcej exact-A1 thermal history, steam closure, mode rank,
handoff bounde, nezávislom constrain­te, konvergencii, timeoute alebo novej
formálnej chybe. Keďže ide o opravu 2/2, nevznikne v003, CS3 ani tretí
runner.

## 10. Jediné povolené implementačné cesty

```text
scripts/baseScripts/a2_k11_cs2/full_multispecies_constrained_dae_v002.py
scripts/264_script_A2_K11_CS2_full_v002_multispecies_constrained_DAE_runner.py
scripts/results/a2_k11_cs2/RUN_A2_K11_CS2_FULL_V002_001.json
tracks/A1/A1K1/A2/A2K11/ARTIFACTS/K11_CS2_FULL_V002_RESULT_AND_AUDIT.md
```

Runner importuje v002 modul priamo; package-level v001 export sa nemení.
V001 base, runnery 262/263 a RUN-001/002 zostávajú immutable. Každý Python
beh používa priamo `C:\\Python311\\python.exe`, vnútorný limit `<=5 s` a
vonkajší `<=10 s`. Pred syntax/help/smoke/full behom sa v tomto dokumente
alebo v jeho append-only dodatku zapíše ľudský cieľ, očakávaný rozsah a
PASS/STOP ďalší krok.

Full v002 sa nespustí, kým neexistuje celý fyzický base. Čiastkový S0
runner by iba spotreboval poslednú opravu bez možnosti fyzikálneho
verdiktu.

## 11. Release

Predregistrácia nemení skóre, verejný mechanizmus, predikčnú tabuľku ani
Zenodo trigger. Výsledok zostane route-local; nevznikne nový `theory/05`
ani duplicitný koreňový `Audit/` dokument.

## 12. Append-only spresnenie backendovej bázy pred prvým behom

**Zapísané:** 2026-07-16, pred vytvorením v002 a pred akýmkoľvek Python
behom. Toto spresnenie nemení fyziku ani prahy; odstraňuje nejednoznačnosť
medzi CAMB-E auditným kontraktom a natívnou bázou externého backendu.

Počty `25/33/41` pre `L=4/6/8` sú kanonickým externým CAMB-E auditným
registrom. Externý backend smie interne používať inú presnú polarizačnú
bázu alebo redukovaný TCA stav iba ak sú splnené naraz:

1. interný ordered state manifest a RHS parita sú overené v jeho vlastnej
   báze;
2. na full-state checkpointoch existuje explicitná algebraická mapa do
   kanonického CAMB-E registra a spätná mapa na fyzický obraz;
3. mapy majú požadovaný rank a zachovávajú stress-energy, constrainty a
   evolučné riadky;
4. TCA/full overlap sa porovná podľa fyzických mien, nie pozičným slice;
5. negatívny fixture s chybnou, chýbajúcou alebo prehodenou položkou zlyhá.

CLASS scalar polarization stavy `pol0_g` a `pol1_g` nie sú položky
`E_gamma_0` a `E_gamma_1`, ktorých pridanie spôsobilo PF-062. Zároveň nie
je povolené tvrdiť `CLASS pt_size == 4L+9`; veľkosť natívneho CLASS vektora
sa mení s bázou a TCA/RSA/UFA aproximáciami. Bez presného adaptera je CLASS
iba source-auditable background/thermal/koeficientová referencia, nie
dôkaz state-contract PASS.

Zdrojová mapa a podmienky sú pripnuté v
`K11_CS2_CLASS_HYREC_ARCHITECTURE_SOURCE_MAP_AND_FEASIBILITY_AUDIT.md`.

## 13. Append-only obmedzenie formulácie „technická oprava 2/2“

**Zapísané:** 2026-07-16 na priamy pokyn používateľa, stále pred vznikom
v002 a pred prvým full behom.

Staršie časti tejto predregistrácie používali výraz „posledná technická
oprava 2/2“. Tento výraz už nesmie blokovať opravu syntaxe, importu,
timeoutu, závislosti, registra, adaptera, state/RHS parity, serializácie,
jednotiek ani inej implementačnej chyby. Taký incident sa zapíše do error
ledgeru, artefakt sa označí a oprava sa znovu preverí. Nespotrebuje fyzikálny
pokus a nevytvorí v003 ani CS3, kým sa nemení fyzika.

Rozpočet `2/2` odteraz znamená najviac dve vopred odlíšené fyzikálne
formulácie alebo fyzikálne pokusy v rámci K11-CS2, ktoré technicky prešli a
majú interpretovateľné holdouty. Technická chyba nemôže vydať fyzikálny
PASS/STOP ani natrvalo zablokovať koľaj. Pri opakovaní rovnakej chyby sa
mení technická architektúra alebo zdieľaný base test, nie fyzikálny verdict.

Toto obmedzenie zachováva históriu PF-062 a v002. Ruší iba nesprávnu
interpretáciu, že počet technických incidentov je dôvodom na
`REVIEW_BLOCKED_IMPLEMENTATION` bez ďalšej opravy.

## 14. Append-only technický cap 10 na implementačnú vetvu

Neskoršie spresnenie používateľa z 2026-07-16 nahrádza iba vetu o
neobmedzenom počte technických opráv. Jedna konkrétna implementačná
architektúra má najviac 10 očíslovaných technických pokusov. Autoritatívny
counter pre v002/ARCH-A je v
`K11_CS2_FULL_V002_TECHNICAL_ATTEMPT_LEDGER.md` a začína `0/10`.

Po desiatom technickom neúspechu dostane iba ARCH-A stav
`TECHNICAL_STOP` s presným dôvodom: chyba skriptu, Python/dependency,
sandbox/prostredie alebo build/adapter. K11 zostane fyzicky REVIEW a nesmie
byť označená za mŕtvu. Nová technická architektúra musí najprv vysvetliť,
ako odstráni tento dôvod, a dostane vlastný ledger `0/10`; v003 nevznikne,
ak sa nemení fyzika.
