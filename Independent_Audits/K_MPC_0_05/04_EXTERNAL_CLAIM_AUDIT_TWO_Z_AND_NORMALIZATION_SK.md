# Audit externého tvrdenia: dve `z`, normalizácia a `H_K4`

**Vstup:** externý návrh dodaný 2026-07-15.  
**Celkový rozsudok:** `ČIASTOČNÝ PASS — algebraická oprava je správna; globálny
background ešte nie je uzavretý.`

## Rozsudok po bodoch

| Tvrdenie | Rozsudok | Dôvod |
|---|---|---|
| Existujú dve úlohy pre zápis `z`: homogénny pomer hustôt je funkcia `a`, kým `z=k/Hconf_r` je perturbatívna súradnica. | **PASS** | Exponent pochádza z backgroundovej continuity rovnice, no `z` a `s=k/Hconf` boli zavedené pri superhorizontovom rozvoji porúch. Starý kód ich nebezpečne zlial. |
| `p=4-3delta` je exponent skorého pomeru `rho_f/rho_r`. | **PASS** | Pri `rho_f,x=-3delta rho_f-lambda(H0/H)rho_f` a `rho_r,x=-4rho_r` je presne `y_f,x=(4-3delta-lambda H0/H)y_f`. |
| `Phi(k)=A_f(H0 sqrt(Omega_r0)/k)^p` zruší holé `k^p`. | **PASS (algebraický)** | `Phi z^p=A_f a^p` presne, bez aproximácie. |
| Cancelácia platí pre všetky zapísané fuel/ash členy. | **PASS pre K7 ansatz; nie ešte pre plnú nelineárnu teóriu.** | Každý ďalší `z` v zapísanom rade sa vyskytuje ako `g2 z^2=lambda a^2/sqrt(Omega_r0)`, takže je `k`-nezávislý. Chýba však odvodenie úplného spätnoväzbového riešenia mimo radiačného limitu. |
| Exponenciála `exp(-g2 z^2/2)` je presné celkové riešenie backgroundu. | **LEN V RADIÁČNOM LIMITE** | Platí pri `H=H0 sqrt(Omega_r0)a^-2`. Pri plnom backgrounde je `lambda H0/H=lambda a^2/(sqrt(Omega_r0)*sqrt(D))`, preto sa exponenciála nemôže vyhlásiť za presné plné riešenie bez ďalšieho odvodenia. |
| `H_K4^2=H0^2 Omega_r0 D/a^4` a `d tau/da=1/(H0 sqrt(Omega_r0) sqrt(D))`. | **PASS (algebraický)** | Pri `s=k/Hconf`, `s^2=z^2/D` a `z=k a/(H0 sqrt(Omega_r0))` to plynie priamo. |
| Kladnosť `D` a konečnosť `d tau/da` sú automatické pre každé `a>0`. | **NEPREŠLO / nepreukázané** | V starom skrátenom rade je palivový faktor `1-g2z^2/2` a denominator obsahuje `1+(1/(p+1)-1/2)g2z^2`; ich korekcie sú pri neskorom `a` záporné. Samotné `A_f>0` preto nedokazuje `D>0` v celom intervale. Treba otestovať alebo odvodiť plný pozitívny background. |
| Staré `Phi=1`, `k=0.05 Mpc^-1` zodpovedajú veľmi veľkému efektívnemu `A_f`. | **PASS ako diagnostika, nie ako dnešná hustota** | `A_f,old=[0.05/(H0 sqrt(Omega_r0))]^p` je rádovo `10^17` pri deklarovaných číslach. Keďže skorý rad neplatí automaticky do `a=1`, nie je to priamo dnešný pomer hustôt; je to silný signál zlej/nezavretej normalizácie. |
| `0.05 Mpc^-1` je štandardný Planck scalar pivot. | **OVERENÉ ako konvencia; NEPREUKÁZANÉ ako pôvod v našom kóde.** | Planck 2018 používa `k_*=0.05 Mpc^-1` pre skalárne spektrálne parametre, ale zdrojový kód K7 neobsahuje komentár ani citáciu, že túto hodnotu prebral od Plancku. |
| Ak je `k` v backgrounde konštanta, problém zmizne. | **NEPREŠLO** | Ľubovoľne zamrznuté číslo nezmení závislosť na neodvodenom scale na fyzikálnu predikciu. Musí ísť o odvodené `k_*` alebo o správne zrušený koordinátový `k`. |

## Presná cancelácia v implementovanom rade

Nech

```text
z = k a/(H0 sqrt(Omega_r0)),
g2 = lambda (H0/k)^2 sqrt(Omega_r0),
Phi(k) = A_f (H0 sqrt(Omega_r0)/k)^p.
```

Potom

```text
Phi z^p = A_f a^p,
g2 z^2 = lambda a^2/sqrt(Omega_r0).
```

Z toho bezprostredne vyplýva `k`-nezávislosť všetkých členov, ktoré K7
skutočne zapisuje:

```text
fuel: Phi z^p (1 - g2 z^2/2),
ash:  Phi z^p (g2 z^2)/(p+1),
D:    1 + mu z + Phi z^p [1 + (1/(p+1)-1/2)g2z^2].
```

Aj `mu z=Omega_m a/Omega_r0` je už nezávislé od `k`. Preto je to správna
algebraická cesta k `D_univ(a)`.

## Dôležité obmedzenie: „para" nie je samostatne dokázaná exponenciála

V dodanom tvrdení je `rho_f/rho_r` nazvané „para/steam faktor“. Presnejšie je
to **pomer paliva k radiácii**; `rho_r` zahŕňa fotóny a voľne prúdiacu
radiáciu. Exponenciála je presným riešením iba na čisto radiačnom pozadí.
Jej `k`-cancelácia je správna, ale sama o sebe neuzatvára plný neskorý vývoj.

## Pivot `0.05 Mpc^-1`

Planck naozaj používa `0.05 Mpc^-1` ako štandardný scalar pivot pre `A_s` a
`n_s`; je to konvencia primordiálneho spektra, nie meraná kozmická dĺžka ani
automaticky vlastnosť siete. To robí súvislosť so starým `K_MPC=0.05`
plausibilnou hypotézou, nie dôkazom autorovho úmyslu.

Zdroj: [Planck 2018 Results: Cosmological Parameter Tables](https://wiki.cosmos.esa.int/planck-legacy-archive/images/4/43/Baseline_params_table_2018_68pc_v2.pdf);
[Planck 2018 results I](https://www.aanda.org/articles/aa/pdf/2020/09/aa33880-18.pdf).

## Stav brán

- **P1 — k-univerzálnosť algebraického K7 radu:** PREŠLA po podmienke
  `Phi(k)=A_f(H0 sqrt(Omega_r0)/k)^p`.
- **P2a — `A_f` z už zmrazeného A1 closure bez nového fitu:** PREŠLA;
  `A_f=7809.27010196`, tri RK4 rozlíšenia sa zhodli na `5.34e-13`.
  Záznam: `06_AF_FROM_FROZEN_A1_RESULT_SK.md`.
- **P2b — mikrofyzikálny pôvod zmrazeného A1 closure:** OTVORENÁ;
  P2a ho nenahrádza.
- **P3 — plná kladnosť, dnešná normalizácia a konečný konformný čas:**
  skrátený K7 rad **NEPREŠIEL** ako plný background: po normalizácii P2a
  má `D=0` pri `a≈0.70896`. Plný A1 background zostal kladný; nová vetva
  musí poruchy odvodiť z neho, nie rad iba extrapolovať. Záznam `08`.
- **P4 — CLASS adapter a nulový limit:** BLOKOVANÁ P2+P3.

## Bezpečný ďalší krok

Pred akýmkoľvek CLASS patchom treba najprv napísať a skontrolovať plné
`a`-závislé ODE s neznámym, ale k-nezávislým `A_f`, vrátane dnešnej
normalizácie. Až potom sa môže skúmať, či existujúca mikrofyzika bunkovej
siete `A_f` určuje, alebo či by išlo o nový fit (čo by koľaj K-N2 zastavilo).

## Proveniencia

- `03_FUEL_TERM_PROVENANCE_AND_K_ROLE_SK.md` v tomto adresári.
- `tracks/.../FULL_BACKEND/04_IMPLICIT_D_TO_H_K4_MAPPING_LEDGER.md`.
- `Questions/A1_rozhodnutie_Q19_a_kovariantny_background_v3.18.md`.
- `scripts/128_script_A2_K4_3b_RG_BR3B2g_exact_order_and_hierarchy_audit.py`.
