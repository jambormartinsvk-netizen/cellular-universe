# P5.3g7-M3-FULL/R-A — pokus 6/10, predregistrácia seedového solve

**Dátum zmrazenia:** 2026-07-16  
**Run ID:** `KMPC-027`  
**Route:** `A1-K1 -> A2-K4 -> P5 -> P5.3g7-M3-FULL/R-A`  
**Stav pri zmrazení:** `ATTEMPT_6_PREREGISTERED / NOT_RUN`  
**Autoritatívny rozsah:** podmienený `M3-TCA0` skorý seed; bez ODE, finite
opacity, plnej Boltzmannovej hierarchie, CMB alebo `S8`  
**Fyzikálna hĺbka pred behom:** bez zmeny, `60/100 = G6`

## 1. Ľudský význam výpočtu

Výpočet sa pýta, či úplný trinásťzložkový skorý stav K4 možno zostaviť bez
vymazania rýchlosti popola `U_c` a bez použitia Einsteinových constraintov
`00` a `0i` ako rovníc, ktoré si samy vynútia neskorší PASS. Pre každý z
piatich štandardných počiatočných módov sa najprv vyrieši štandardná
metrická kotva, potom úplná palivová veža pri `Phi^0` a napokon prvá K4
odozva pri `Phi^1`.

Očakávame plný rank určujúcej matice, malé rezíduá určujúcich rovníc a malé
nezávislé `00/0i` rezíduá. Rovnaký fyzický background sa musí
zrekonštruovať pre tri rôzne Fourierove módy. Rozšírenie radu o dva rády
nesmie meniť spoločné nízke koeficienty nad predregistrovanú toleranciu.

Ak výsledok leží v očakávanom rozsahu, dostane iba
`PASS_M3_TCA0_SEED_CONDITIONAL`; otvorené zostanú S1 mikrofyzika, finite
opacity, P5.4 a G8. Ak zlyhá rank alebo numerická kondícia bez invariantného
rozporu, výsledok je `REVIEW_NUMERICAL_OR_TRUNCATION`, nie fyzikálna smrť.
Fyzikálny STOP je prípustný iba pri reprodukovateľnom algebraickom rozpore
správneho kontraktu aj po rozšírení rádu a nulových limitoch.

## 2. Nemenný state/driver/holdout kontrakt

Importuje sa jediný frozen kontrakt z
`scripts/baseScripts/p5_general_synchronous/full_ra_contract.py`:

```text
STATE = (
 h, eta, delta_gamma, delta_fs, delta_b, delta_c,
 U_gamma, U_fs, sigma_fs, U_b, U_c, delta_f, U_f
)

DRIVER = (
 gamma_continuity, gamma_Euler,
 fs_continuity, fs_shear, fs_Euler,
 baryon_continuity,
 cdm_continuity, cdm_Euler,
 tight_coupling,
 fuel_continuity, fuel_Euler,
 Einstein_trace, Einstein_traceless
)

HOLDOUT = (Einstein_00, Einstein_0i)
```

`00` ani `0i` nesmú vstúpiť do určujúcej matice. Trace a traceless sú
určujúce Einsteinove rows, nie ďalšie holdouty. Ich nezávislá krížová
kontrola vzniká z frozen total-energy/total-momentum a dvoch Bianchi
left-null identít spolu s presným produkčným TCA0 redukčným guardom.
Produkčný validator musí odmietnuť chýbajúci, extra, falošný,
preusporiadaný alebo prekrývajúci sa stav/riadok.

## 3. Povolené a zakázané zdroje

Povolené sú iba:

- štandardná M1 kotva cez
  `mode_resolved_puiseux_v2_m1_anchored.solve_standard_seed_anchored` a
  `solve_hard_anchored_linear_system`;
- algebra/background triedy zo staršieho modulu iba tam, kde ich hash a
  význam kontroluje nový shared modul;
- opravené B1 rovnice a tlak z dokumentu 32.

Zakázané je volať legacy `solve_fractional_seed`,
`run_m3_tca0_anchored`, monkeypatchovať starý runner alebo použiť jeho
frakčný trace/holdout. Legacy tlak PF-063 mal trojnásobnú neadiabatickú
časť a nie je fyzikálnym zdrojom tohto behu.

M1 je výslovne prijatá frozen výnimka: používa už prejdený hard-anchor
helper a jeho pôvodný rank/reziduálny audit. Nová row/column ekvilibrácia,
per-row term norm a fixed `rcond` tejto predregistrácie sa vzťahujú na nový
F0 a M3 solve. Výsledok nesmie tvrdiť, že M1 znovu prešla novým
ekvilibračným auditom.

## 4. Zmrazené rovnice tmavého sektora

```text
delta_c,x = -s2 U_c - h_x/2 + gamma r(delta_f-delta_c)
U_c,x     = (h_c-1)U_c + gamma r beta(U_f-U_c)

delta_f,x = -3(2-delta)delta_f
            -delta(s2 U_f+h_x/2)
            -9delta(2-delta)U_f
            -3gamma(2-delta)U_f

U_f,x     = (h_c+2)U_f + delta_f/delta
            +(gamma/delta)(2U_f-U_d)

U_d       = (1-beta)U_c + beta U_f
delta p_f/rho_f = delta_f +(2-delta)(3delta+gamma)U_f
```

Dvojitá expanzia je

```text
X = sum_e X[0,e] z^e + Phi z^p sum_j X[1,j] z^j + O(Phi^2),
p=4-3delta,
Phi(k)=A_f[H0 sqrt(Omega_r0)/k]^p,
Phi z^p=A_f a^p.
```

Na `Phi^1` Einsteinove zdroje vstupuje `Omega_f[1]*fuel[0]`.
`Omega_f[1]*fuel[1]` je zakázané, pretože patrí až do `O(Phi^2)`.
`fuel[1]` zostáva spectator blokom s vlastnými dvoma rovnicami.

Keďže `r=O(Phi)` a `beta=O(Phi)`, CDM recoil člen
`gamma*r*beta=O(Phi^2)`. Pokus 6 na `Phi^1` overuje dynamickú prítomnosť a
regularitu `U_c`, nie fyzikálnu veľkosť recoil/drag sily na popol.

## 5. Módy, podpory a očakávané rozmery

M1 používa rády `-1..5`: 77 plných koeficientov, po tvrdej normalizačnej
kote 76 neznámych.

| Mód | vedúci `n` | primárne `Phi^0/Phi^1` okno | M1 matica/rank | F0 matica/rank | M3 matica/rank | M3 holdout koef. |
|---|---:|---|---:|---:|---:|---:|
| AD | 2 | `0..2` | `99x76 / 76` | `6x6 / 6` | `39x39 / 39` | 6 |
| CDI | 1 | `0..1` | `99x76 / 76` | `4x4 / 4` | `26x26 / 26` | 4 |
| BI | 1 | `0..1` | `99x76 / 76` | `4x4 / 4` | `26x26 / 26` | 4 |
| NID | 3 | `0..3` | `99x76 / 76` | `8x8 / 8` | `52x52 / 52` | 8 |
| NIV | 2 | `-1..2` | `96x76 / 76` | `8x8 / 8` | `52x52 / 52` | 8 |

Rozšírenie `J+2` sa musí naozaj znovu vyriešiť, nie iba odhadnúť ochranným
pásmom. Očakávané počty M3 neznámych sú AD 65, CDI 52, BI 52, NID 78 a NIV
78; F0 počty sú 10, 8, 8, 12 a 12. Ranková strata najprv znamená REVIEW,
nie automatický fyzikálny STOP.

Vedúca fuel formula je kontrola po solve, nie ďalšia tvrdá kotva.

## 6. Numerický a rank kontrakt

- lineárne matice sa reportujú v surových aj riadkovo/stĺpcovo
  ekvilibrovaných súradniciach;
- SVD cutoff je pevný `rcond=1e-12`;
- PASS ranku vyžaduje očakávaný rank a
  `sigma_min/sigma_max >= 1e-10`; interval medzi cutoffom a PASS prahom je
  `REVIEW_RANK_OR_CONDITION`;
- škálované driver rezíduum každého coefficient row je
  `|R|/sum|terms| <= 1e-10`;
- ak `sum|terms| <= 1e-12`, namiesto noise/noise delenia sa vyžaduje
  absolútne `|R| <= 1e-12`;
- M1 anchor/row a F0 driver majú rovnaký prah `1e-10`;
- nezávislé `00/0i` holdouty vyžadujú škálované rezíduum `<=1e-9` s tou
  istou absolútnou vetvou `<=1e-12` pri skoro nulovej norme;
- zakázaná nižšia vrstva a `Omega_f[1]*fuel[1]` príspevok musia byť
  `<=1e-10` na jednotku `Phi`;
- vedúci `U_c` regularity check má toleranciu `1e-12`.

Condition proxy zo SVD sa neinterpretuje ako fyzika; je iba numerický
diagnostický údaj. Prahy sa po zhliadnutí výstupu nemenia. Ak by bola zmena
nutná, vznikne nové odôvodnené preregistrované pokračovanie.

## 7. Truncation a seedové plochy

Použijú sa `z_deep=1e-4` a `z_shallow=1e-2`; bezpečnostný cap je
`z<=0.05`. Plocha je odvodená z dynamického Fourierovho módu, nie zo
starého pevného `K_MPC=0.05`.

- rozdiel spoločných nízkych koeficientov primárneho a `J+2` solve:
  `<=1e-8`;
- fyzický príspevok vynechaného chvosta na oboch seedových plochách:
  `<=1e-6`;
- deep/shallow power-law pomer sa exportuje iba ako diagnostika. Nemá PASS
  účinok, pretože legitímne subleading členy pri `z_shallow=1e-2` dávajú
  prirodzenú odchýlku od čistej vedúcej mocniny;
- prekročenie `z` capu je fail-closed technický REVIEW.

## 8. Povinné k a nulové limity

Každý mód sa overí pre dynamické
`k={0.005,0.05,0.15} Mpc^-1`. Pri rovnakom fyzickom
`a={1e-8,3e-8}` musia `D,H,rho_f,rho_ash` súhlasiť medzi k s relatívnym
rozdielom `<=1e-12`. Porovnávajú sa fyzické rekonštrukcie, nie surové
koeficienty v `z`.

Oba limity sú nové solve, nie post-hoc vynulovanie stĺpcov:

1. `gamma->0`: transfer a transferom produkovaný popol zaniknú, ale
   neinteragujúce palivo a jeho gravitácia zostávajú;
2. `A_f->0`: fyzická `O(A_f)` korekcia zanikne a rekonštruovaný seed sa
   vráti k M1. Derivačné `Phi^1` koeficienty samy nemusia byť nulové.

Conditional steam kontrola je iba `S-C`; jej vážená split identita musí
mať rezíduum `<=1e-14`. Tento beh nedokazuje fyzickú `S-M` mikrofyziku.

Frozen B1 guard musí znovu prejsť presné total-energy, total-momentum a obe
Bianchi identity. Produkčný kombinovaný photon-baryon Euler musí navyše
prejsť nezávislú presnú identitu
`(Euler_gamma+R Euler_b)/(1+R)` s `U_b=U_gamma` a nulovou Thomsonovou
hybnostnou sumou. Bez oboch guardov shard nemôže prejsť.

## 9. Procesy, vnútorné a vonkajšie limity

Shared modul bude
`scripts/baseScripts/p5_general_synchronous/full_ra_m3_seed.py`; tenký
runner bude
`scripts/271_script_KMPC_027_P5_3g7_m3_full_ra_seed_attempt6.py`.

Jeden technický pokus 6 tvorí celý vopred zmrazený balík:

1. `py_compile` shared modulu a runnera;
2. `--help`;
3. jeden smoke mód/k;
4. päť samostatných módových shardov AD, CDI, BI, NID, NIV;
5. ľahká agregácia existujúcich shardov.

Presné immutable názvy sú:

```text
RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_AD.json
RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_CDI.json
RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_BI.json
RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_NID.json
RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_NIV.json
RUN_KMPC_027_P5_3G7_M3_FULL_RA_SEED_ATTEMPT6.json
```

Každý Python proces má vnútorný deadline najviac 5 s a vonkajší shell
timeout najviac 10 s. Shardovanie nemení počet technických pokusov: celý
balík je pokus `6/10`. JSON výsledky sú immutable prílohy; autoritatívny
rozsudok sa zapíše do následného Markdownu.

## 10. Vopred zmrazené vetvy rozsudku

### PASS

Všetkých päť módov, tri k, primary aj `J+2`, oba nulové limity, ranky,
driver a holdout tolerancie prejdú:

```text
PASS_M3_TCA0_SEED_CONDITIONAL
```

K4 zostáva najviac `60/100`, kým sa neuzavrie celá G7 brána. Nasleduje
explicitný S1/S-M blocker a potom P5.4; nejde sa priamo na G8.

Ani tento conditional PASS neuzatvára `Phi^2` CDM recoil, `k->0`
finite-`U`/`theta=O(k^2)`, `rho_c->0` singulárny rail alebo `delta->0` pól.

### REVIEW

Technický pád, deadline, rank blízko cutoffu, zlá kondícia alebo
truncation-only nezhoda:

```text
REVIEW_TECHNICAL_OR_NUMERICAL_UNRESOLVED
```

Zapíše sa presná príčina a zachová sa výstup. Technická chyba je pokus
`6/10`, ale nie fyzikálny pokus ani smrť K4.

### STOP konkrétnej formulácie

Iba nezávisle reprodukovateľný invariantný rozpor správneho B1 kontraktu,
ktorý pretrvá primary/J+2, nulové limity a správne škálovanie, povoľuje:

```text
STOP_FULL_R_A_M3_TCA0_FORMULATION
```

Ani tento prvý nález automaticky nezabíja celú A2-K4. Musí nasledovať
nezávislý audit a analýza príčiny, z ktorej sa odvodia nové koľaje bez
konkrétneho zlyhania.

## 11. Release a auditná hranica

Samotný pokus 6 nemení tabuľku predpovedí, release trigger ani Zenodo
verziu. Neudeľuje CMB, `S8`, P5.4 alebo G8 podporu. Všetky neskoršie zmeny
prahov, rovníc alebo podpôr musia dostať nové Markdown odôvodnenie pred
ďalším Python behom.

## 12. Finálny implementačný hash freeze pred prvým behom

Statický delta audit fyzikálneho a matematického audítora po oprave guardov
nenašiel ďalší pre-run blocker. Nasledujúce hashe sú zmrazené pred prvým
Python procesom:

| Zdroj | SHA-256 |
|---|---|
| `full_ra_contract.py` | `F3839DA931D24939FA9C5925FD29B1484E722D1A0F24117DC91EBE5F4436D464` |
| `full_ra_b1_preflight.py` | `62D6DEEFBDB81C0619FD58C668185FF9CA76926A90D00DCE9C092AD4797D6B5D` |
| `full_ra_b1_preflight_v2.py` | `27C0D6ADA828CA2F59C0D128EB6339074D5940F294272CDABE8127CB84867C7C` |
| `mode_resolved_puiseux.py` | `5A89CF82006CB5ECC1D8B4BE1FD56A463453EE3D6261968CB64DE8CCF2C8B7AE` |
| `mode_resolved_puiseux_v2_m1_anchored.py` | `5DE2C280B0E9DAF528A9E3011368361B37AE53DE38827FB6F6CE4AB2019A4455` |
| `full_ra_m3_seed.py` | `070F217B45A385369ECAFAA3D409A1210BAE3C3AF8A600A9171225B258751BF2` |
| runner `271/KMPC-027` | `E72DD58E8D2719DE1DF9286D9E7D8D8FE5938670DCF74C2EC5E64171BE01554A` |

Runner porovná prvých šesť hashov fail-closed pred výpočtom. Hash runnera
sa overí samostatným shell krokom pred `py_compile`, pretože súbor nemôže
bez rekurzívneho paradoxu obsahovať vlastný očakávaný hash. Ak sa čo i len
jeden hash zmení, pokus 6 sa nesmie vydávať za tento frozen balík.

**Stav po freeze:** `ATTEMPT_6_FROZEN_READY / NOT_RUN`; counter stále
`5/10` až do prvého Python procesu.
