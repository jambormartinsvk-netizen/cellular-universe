# K11-TC-A — audit konečnej CAMB-E uzávery a rozhodnutie o numerickom reze

**Dátum:** 2026-07-16  
**Rozsah:** read-only fyzikálny a matematický audit lokálnych CAMB/CLASS zdrojov  
**Autoritatívny rozsudok:** `STOP_UNIVERSAL_EXACT_FINITE_L_CAMB_E_CLOSURE`  
**Nedopad pri audite:** K11 ani K11-CS2 neumierajú; counter bol `0/10`; hĺbka zostáva `10/100 = G1`  
**Neskorší stav:** source-AST preflight prešiel v pokuse 5/10; full DAE stále `NOT_RUN`

## 1. Ľudský záver

Nekonečnú polarizačnú Boltzmannovu hierarchiu nemožno všeobecne nahradiť
presnou lokálnou rovnicou pre konečný posledný multipól. Dve uhlové
distribúcie môžu mať v jednom čase rovnaké `E_2...E_L`, ale rozdielne
`E_(L+1)`. Potom majú podľa presnej CAMB rovnice rozdielne `E_L'`.

Preto je mŕtve iba tvrdenie, že existuje univerzálna presná Markovova
uzávera závislá od konečného registrovaného stavu. Fyzikálna K11 ostáva
živá ako hypotéza. Správny numerický postup je otvorene deklarovať rez a
preukázať, že nízke multipóly a observables konvergujú pri rastúcom `lmax`.

## 2. Presná neuzavretá CAMB-E rovnica

Lokálny zdroj `.deps/python/camb/symbolic.py` dáva pre `ell >= 2`

```text
E_ell' = k/(2ell+1) [
            ell E_(ell-1)
           -((ell+3)(ell-1)/(ell+1)) Kf[ell] E_(ell+1)
         ]
         - opacity E_ell
         + delta_(ell,2) opacity polter.
```

Pre `ell=2` je dolný člen nulový. Reťazec teda začína `E_2`; `E_0,E_1`
nie sú stavy kanonickej CAMB scalar E bázy. `get_hierarchies(lmax)`
generuje iba vnútorné rovnice a nedodáva fyzikálne presnú hornú uzáveru.

## 3. Prečo sa CLASS top row nesmie kopírovať

CLASS používa natívne `pol_l` s inými vnútornými koeficientmi. V plochej
geometrii má jeho zdrojovo pripnutý horný riadok tvar

```text
pol_L' = k pol_(L-1) -(L+1)/tau pol_L - scattering_rate pol_L.
```

CAMB-E horný koeficient susedného multipólu je

```text
(L+3)(L-1)/(L+1),
```

nie `L+1`. Priamy prepis by miešal dve bázy. Prenos je prípustný iba po
presnej mape celého operátora vrátane prípadného člena `P_tau` a po
dôkaze zachovania zdrojov, stressu, TCA handoffu a observables.

## 4. Rozsudok nad technickými podkoľajami

| Podkoľaj | Stav | Dôvod / použitie |
|---|---|---|
| `K11-TC-A0` univerzálna exact finite-L CAMB-E closure | **MŔTVA** | invariantný rozpor s voľným `E_(L+1)` |
| `K11-TC-A1` mode-by-mode Frobeniova closure | **ŽIVÁ IBA PRE SKORÝ SEED** | kontrolovaná asymptotická aproximácia s explicitným exponentom a chybovým rádom; nie full evolúcia po vstupe do horizontu |
| `K11-TC-A3` rozšírená CAMB-E hierarchia + registrovaný numerický rez | **PRVÁ AKTÍVNA TECHNICKÁ CESTA** | presné vnútorné riadky, otvorene približný top a povinná `lmax`/closure konvergencia |
| `K11-TC-B` natívny CLASS backend + presná mapa | **ŽIVÁ ALTERNATÍVA** | zdrojovo auditovaný CLASS top, ale nutná netriviálna CLASS↔CAMB-E mapa |

Tieto suffixy sú technické realizácie jedného K11 mechanizmu. Nepridávajú
fyzikálny parameter, koľaj ani body.

## 5. Zmrazené pravidlo ďalšieho pokusu

Pokus 1/10 smie overiť iba:

- presný ordered register `4L+9 = 25/33/41` pre `L=4/6/8`;
- presné CAMB vnútorné koeficienty pre `ell<L`;
- explicitne pomenovaný numerický top bez neregistrovaného `L+1`;
- negatívne contract fixtures cez tú istú produkčnú validačnú cestu;
- metadata `is_exact_physics=false` a `requires_lmax_convergence=true`.

Taký PASS je iba štrukturálny. Nesmie sa citovať ako dôkaz fyzikálnej
uzávery ani ako náhrada neskoršieho `lmax` a closure-family sweepu.

## 6. Zdrojové body nezávislých auditov

- CAMB: `.deps/python/camb/symbolic.py`, spin-2 E rekurencia a rozsah
  generátora hierarchie;
- CLASS: `external/CLASS/source/perturbations.c`, vnútorná `pol_l`
  rekurencia, horný closure a plochá identita `cotKgen=1/(k tau)`;
- fyzikálny audit: konečný closure je numerická aproximácia, nie nový zákon;
- matematický audit: univerzálna konečnorozmerná lokálna uzávera neexistuje
  na celom priestore riešení nekonečnej hierarchie.
