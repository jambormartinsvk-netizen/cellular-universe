# A16-K1. Kovariantné zobrazenie V1 pre koľaj „Q vytvára iba CDM“

**Verzia kandidáta:** v3.18 návrh  
**Koľaj:** A1-K1  
**Stav koľaje:** PREŽÍVA backgroundové testy; poruchy čakajú na A2  
**Rozsah:** kovariantný efektívny opis homogénneho pozadia, nie fundamentálna akcia siete

## A16-K1.1 Účel a hranica tvrdenia

Táto sekcia ukazuje, že backgroundové rovnice V1 možno zapísať ako kovariantný systém interagujúcich efektívnych tekutín vo všeobecnej relativite. Celkový tenzor energie a hybnosti sa zachováva identicky.

Sekcia zároveň odstraňuje nejednoznačnosť pôvodnej spoločnej zložky „hmota“: bunkový prenos Q prijíma iba CDM/popol. Baryóny tento neskorý prenos neprijímajú.

Toto zobrazenie nedokazuje mikroskopickú akciu siete, pôvod parametrov δ a λ ani správnosť pôvodnej rastovej rovnice V3.

## A16-K1.2 Zložky

Celkový tenzor je

```text
T_tot^{μν} = T_f^{μν} + T_c^{μν} + T_b^{μν} + T_r^{μν}.
```

Zložky majú na úrovni homogénneho pozadia stavové rovnice:

| Zložka | Význam | Stavová rovnica |
|---|---|---|
| f | palivo | `p_f = (-1 + δ) ρ_f` |
| c | CDM/popol | `p_c = 0` |
| b | baryóny | `p_b ≈ 0` |
| r | relativistické zložky | `p_r = ρ_r/3` |

Pre ideálnu tekutinu používame pri signatúre metriky `(-+++)`:

```text
T_i^{μν} = (ρ_i + p_i) u_i^μ u_i^ν + p_i g^{μν}.
```

V presne homogénnom FRW pozadí sú štvorrýchlosti komohybné. Pri poruchách sa všeobecne líšia.

## A16-K1.3 Prenosový štvorvektor

Definujeme konštantnú efektívnu mieru

```text
Γ = λ H₀
```

a lokálny skalár prenosu

```text
Q = Γ ρ_f.
```

Koľaj A1-K1 volí

```text
Q^ν = Q u_c^ν.
```

Kovariantné rovnice sú

```text
∇_μ T_f^{μν} = -Q^ν
∇_μ T_c^{μν} = +Q^ν
∇_μ T_b^{μν} = C_b^ν
∇_μ T_r^{μν} = C_r^ν

C_b^ν + C_r^ν = 0.
```

Členy `C_b^ν` a `C_r^ν` predstavujú iba štandardné kolízne procesy medzi baryónmi a žiarením. Nie sú súčasťou bunkového prenosu Q. Na backgrounde V1 sa ich čistá energetická výmena zanedbáva; v presnom Boltzmannovom výpočte sa použijú štandardné kolízne členy CLASS/CAMB.

Súčet rovníc dáva

```text
∇_μ T_tot^{μν} = -Q^ν + Q^ν + C_b^ν + C_r^ν = 0.
```

Celková energia a hybnosť sa teda zachovávajú konštrukciou. Einsteinove rovnice s týmto celkovým zdrojom sú na úrovni efektívneho opisu kompatibilné s Bianchiho identitou.

Konštanta H₀ v `Γ = λH₀` sa v tomto opise používa ako pevná kalibračná mierka s rozmerom inverzného času. Kovariancia zápisu sama osebe nevysvetľuje jej mikroskopický pôvod.

## A16-K1.4 FRW limita

Pre ploché FRW pozadie, `x = ln a`, čiarku `d/dx` a `H = ȧ/a` dostaneme

```text
ρ_f′ = -3δ ρ_f - λ(H₀/H)ρ_f
ρ_c′ = -3ρ_c + λ(H₀/H)ρ_f
ρ_b′ = -3ρ_b
ρ_r′ = -4ρ_r.
```

Po sčítaní:

```text
ρ_tot′ = -3δρ_f - 3ρ_c - 3ρ_b - 4ρ_r.
```

Pre

```text
p_tot = (-1 + δ)ρ_f + ρ_r/3
```

je pravá strana presne

```text
-3(ρ_tot + p_tot).
```

Prenosový člen sa vyruší s opačnými znamienkami. Energia odobratá palivu sa pridá do CDM.

## A16-K1.5 Bezrozmerné premenné

Pre numeriku odporúčame rozlíšiť hustotu normalizovanú dnešnou kritickou hustotou od okamžitej hustotnej frakcie:

```text
X_i(x) = ρ_i(x)/ρ_crit,0
E(x) = H(x)/H₀
Ω_i(x) = X_i(x)/E²(x).
```

V plochom modeli:

```text
E² = X_f + X_c + X_b + X_r.
```

Rovnice sú

```text
X_f′ = -3δX_f - λX_f/E
X_c′ = -3X_c + λX_f/E
X_b′ = -3X_b
X_r′ = -4X_r.
```

Súčasné skripty používajú označenie `Om` aj pre premenné typu X. Vo v3.18 sa musí táto konvencia uviesť alebo sa premenné premenujú, aby sa nezamieňali s okamžitým `Ω_i(x)`.

## A16-K1.6 Presná väzba na pôvodnú V1

Definujme

```text
X_m = X_b + X_c.
```

Potom

```text
X_m′ = -3X_m + λX_f/E.
```

To je presne pôvodná backgroundová rovnica V1 a rovnica použitá v skripte 09. Rozdelenie spoločnej hmoty preto nemení doterajší backgroundový výpočet.

Rozdelenie je však fyzikálne povinné pre baryónové zaťaženie zvukového horizontu, CMB píky, baryónovo-fotónové oscilácie, poruchy `δ_b`, `δ_c` a dnešný baryónový podiel. Skript 09 preto zostáva iba backgroundovým testom.

## A16-K1.7 Fyzikálna interpretácia baryónov

Neskorý člen `Q = λH₀ρ_f` vytvára CDM/popol, nie baryóny. Komohybné baryónové číslo sa po skončení skorého baryogenetického obdobia týmto členom nemení.

Opis „vzácneho zlyhania“, z ktorého vzniká obyčajná hmota, môže zostať ako kandidátska mikrofyzika skorého baryogenetického kanála. Musí však:

1. pôsobiť pred BBN,
2. vytvoriť pozorovanú baryónovú asymetriu,
3. rešpektovať elektrickú neutralitu a kvantové čísla,
4. po svojom ukončení nepredstavovať neskorý zdroj v baryónovej kontinuitnej rovnici.

Tento skorý mechanizmus nie je odvodený v A16-K1.

## A16-K1.8 Poruchy: čo vyplýva a čo nevyplýva

Voľba

```text
Q^μ = Q u_c^μ
```

znamená, že projekcia prenosu kolmá na štvorrýchlosť CDM je nulová. CDM preto v svojej pokojovej sústave neprijíma dodatočný prenos hybnosti a z tohto prenosu nevzniká nový člen podobný piatej sile v Eulerovej rovnici CDM.

Z tejto voľby však **nevyplýva**, že celé lineárne rovnice rastu majú štandardný tvar. Kontinuitná rovnica hustotnej poruchy CDM všeobecne obsahuje interakčné členy. Pre A2 treba určiť:

- poruchu lokálneho skalára prenosu `δQ`,
- perturbácie paliva a jeho pokojovú efektívnu zvukovú rýchlosť,
- prípadné anizotropné napätie,
- gauge a gauge-invariantné kombinácie,
- počiatočné podmienky,
- superhorizontovú, gradientovú a ghostovú stabilitu.

Pôvodná veta, že „celý vplyv vstupuje výlučne cez E(x) a Ω_m(x)“, sa v tejto koľaji nepoužíva. Rastová rovnica V3 zostáva neoverenou aproximáciou, kým neprejde A2.

## A16-K1.9 Stav testov

Koľaj A1-K1 prešla:

- analytickým súčtom zachovania,
- kontrolou rozmerov a znamienok,
- limitou `λ → 0`,
- algebraickou zhodou so backgroundom skriptov 08 a 09,
- testom kladnosti hustôt po `x = -25`, teda približne `z = 7.2×10^10`.

Pri pracovnom bode `H₀ = 66.37`, `Ω_m0 = 0.3517`, `λ = 0.15`, `δ = 0.02297` zostali všetky hustoty kladné. Background naznačuje, že od rekombinácie vznikne približne 9 % dnešnej komohybnej CDM hustoty. Tento dôsledok ešte musí prejsť plným dátovým testom.

## A16-K1.10 Auditný rozsah tvrdenia

Táto sekcia **tvrdí**:

1. background A1-K1 je kovariantne zapísateľný v rámci GR,
2. celkový tenzor energie a hybnosti sa zachováva identicky,
3. pôvodná spoločná rovnica V1 sa získa sčítaním baryónov a CDM,
4. neskorý bunkový prenos vytvára iba CDM.

Táto sekcia **netvrdí**:

1. fundamentálnu akciu siete,
2. mikroskopické odvodenie Γ, δ alebo λ,
3. odvodenie baryogenézy,
4. štandardný rast porúch,
5. stabilitu celej perturbačnej sústavy,
6. zhodu s plným CMB+BAO+SN+RSD+lensing likelihoodom.

## A16-K1.11 Primárne metodické opory

- [De-Santiago, Wands a Wang: Inhomogeneous and interacting vacuum energy](https://arxiv.org/abs/1209.0563) — rôzne kovariantné voľby interakcie vedú k rozdielnym poruchám a pozorovateľným spektrám.
- [Martinelli et al.: Constraints on the interacting vacuum — geodesic CDM scenario](https://arxiv.org/abs/1902.10694) — príklad úplnej lineárnej analýzy geodetickej interakcie s CDM.
- [Planck 2018: Cosmological parameters](https://arxiv.org/abs/1807.06209) — CMB rozlišuje baryónovú a CDM hustotu.

Tieto zdroje podporujú matematickú metodiku efektívneho modelu. Nie sú dôkazom bunkovej mikrofyziky.
