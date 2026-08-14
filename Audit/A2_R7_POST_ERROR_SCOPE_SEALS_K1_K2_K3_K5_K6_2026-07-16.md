# A2 R7 — post-error scope seals K1, K2, K3, K5 a K6

**Dátum:** 2026-07-16  
**Autorita rozsudku:** hlavný orchestrátor  
**Nezávislé vstupy:** read-only physics track auditor a math/script auditor  
**Účel:** zistiť, či rozsudky smrti po nájdených chybách K4/K11 stále
stoja na správnej rodičovskej formulácii a na dôvode nezávislom od
machine labelu pôvodného skriptu.

## Výsledok

| Koľaj | R7 verdikt | Kanonická hĺbka | Najhlbší vykonaný test | Rozsah smrti |
|---|---|---:|---|---|
| A2-K1 | `CONFIRMED_SCOPE M-009` | `40/100 = G4` | G5 superhorizontový no-go | constant-`Gamma`, constant-`w_f>-1`, `c_s,f^2=1`, `Q^mu || u_c` |
| A2-K2 | `CONFIRMED_SCOPE M-008` | `30/100 = G3` | G6 analytický high-`k` no-go | striktne barotropické palivo `c_s,f^2=w_f<0` |
| A2-K3 | `CONFIRMED_SCOPE M-010` | `40/100 = G4` | G5 superhorizontový no-go | constant-`Gamma`, constant-`w_f>-1`, `c_s,f^2=1`, `Q^mu || u_f` |
| A2-K5 | `CONFIRMED_SCOPE M-012` | `40/100 = G4` | G8 konzervatívny hybridný screen | konkrétna kanonická skalárna akcia s konformnou väzbou |
| A2-K6 | `CONFIRMED_SCOPE M-013` | `30/100 = G3` | G6 presný QS/`G_ij` no-go | akcia `f=-f1 rho_c+eta Z^2`, kanonické `G2`, zdravý interval `eta>=0` |

R7 nepridáva body. Potvrdzuje iba to, že uvedené scope-limited STOP-y
nevznikli z neskôr odhaleného fixed-`K_MPC`, chýbajúcej stavovej zložky
alebo z tolerančného bypassu.

## 1. Identity a nemenné zdroje

Rozhodujúce zdroje boli znovu identifikované 2026-07-16. Uvedené hashe sú
SHA-256 aktuálne auditovaných súborov:

| Koľaj | Zdroj | SHA-256 |
|---|---|---|
| spoločný A1 background | `scripts/13_script_A1_K1_cdm_background_audit_exact_zstar.py` | `7FB9E3BF82ABE1A1985E426AA37F00B40329EEA9781B4334B20359A99898BA6E` |
| K1 | `scripts/23_script_A2_K1_superhorizon_velocity_instability_converged.py` | `6AD94F01C7FCDDFB0C4481AC2003EEA0202481DB484C28572215287E92535FC6` |
| K1 | `scripts/24_script_A2_K1_equation_sign_and_null_limit_audit.py` | `2D95E4DFB7FDCAB632B22C1080B3AE9BEF1A487B2B2720E92CEC7EEACEAC7FCE` |
| K2 | `scripts/21_script_A2_barotropic_fuel_gradient_instability.py` | `D620AFDB6C0175D5AAC593131ABEDE2036090D8C04B53AEB540B1E5B91A04817` |
| K3 | `scripts/25_script_A2_K3_superhorizon_velocity_instability.py` | `7AECD362FE7106114D737163A70DD9AC059A4158E4465F8023CDB8FEFF6C1C9F` |
| K3 | `scripts/26_script_A2_K3_equation_sign_and_null_limit_audit.py` | `F41560EC69C75CF5FB1D60F0F659F0B348BEBE683FBAF1C3A24E54379E39FA7C` |
| K5 | `scripts/37_script_A2_K5_1_action_equations_sign_null_audit.py` | `BF6EC14A2FFD89F6F36DB55A7C843D5106BA639CC466EFD4290F371C12761566` |
| K5 | `scripts/42_script_A2_K5_1_quasistatic_limit_crosscheck.py` | `34349C68E65CDD3846EA52E1EA7365AAFD8BE6734853ECDFEDB07BCB5FA94C84` |
| K5 | `scripts/45_script_A3_K5_K1_CAMB_anchor_and_growth_bound.py` | `F0DE5BD1C801F86441F03861F1539980FB1CA36552D82E2D16BF9F2FF873689A` |
| K5 | `scripts/46_script_A3_K5_K1_required_primordial_amplitude.py` | `9F86BF5B35D66C96E9BD46A6242F6D4104977AE9FFADA1166991B2AC0B03DD15` |
| K6 | `scripts/48_script_A2_K6_1_exact_Gij_and_growth_gate.py` | `6E66E23D7A411F7E05DD42CAB36D6B5BAD8D6883ABAEFEA1702AE3655A533727` |
| K6 | `scripts/49_script_A2_K6_1_continuous_eta_no_go.py` | `BFBB2DE6A65783C12F4E59379559A709BEA5076F997E00BC3C3726EF6F277253` |

Závislostná kontrola: K1/K3 používajú ten istý auditovaný A1 background;
K6 skript 49 načítava skript 48 a ten presný A1 background. K5 term-map
vedie od akcie cez rovnice a kvázistatický limit do samostatnej
CMB-kotvenej rastovej a aritmetickej kontroly. V K1, K2, K3, K5 ani K6 sa
ako backgroundový vstup nepoužíva fixed `K_MPC=0.05`.

## 2. A2-K1 — nezávislý invariant

Rodičovská voľba je

```text
Q_c^mu=+Gamma rho_f u_c^mu,
Q_f^mu=-Q_c^mu,
1+w_f=delta>0.
```

Presná mapa referenčnej konvencie je `Gamma_ref=-Gamma_cell`. Po odčítaní
Eulerových rovníc je relatívna rýchlosť gauge-invariantná a jej vedúci
homogénny člen spĺňa

```text
d ln R/dt = 2 Gamma/delta.
```

Pre registrovaný background je exponent `12.2131073973`, teda
`R=201411.9108`. Znamienko plynie priamo z rovníc; nezávisí od integrátora.
Pri `Gamma->0` zmiznú všetky interakčné členy a párové backgroundové zdroje
sa presne rušia. Rozmery `Gamma/delta` sú inverzný čas. Tým je M-009
potvrdená iba v uvedenej fluidnej triede.

## 3. A2-K2 — hlavný symbol

Striktne barotropická definícia dáva

```text
c_s,f^2 = dp_f/d rho_f = w_f = -0.97703 < 0,
delta_f'' + c_s,f^2 k^2 delta_f = 0.
```

Preto `omega^2=c_s,f^2 k^2<0` a rastová miera
`mu=sqrt(-c_s,f^2)|k|` rastie bez obmedzenia s `k`. Nižšie derivatívne
interakčné alebo Hubbleove členy nemôžu zmeniť znamienko hlavného
`k^2` symbolu. Nulový limit interakcie teda problém neodstraňuje; problém
je v samotnej barotropickej uzávere. M-008 je analyticky potvrdená bez
potreby ODE replayu.

## 4. A2-K3 — nezávislý invariant

Rodičovská voľba je

```text
Q_c^mu=+Gamma rho_f u_f^mu,
Q_f^mu=-Q_c^mu.
```

Po presnom mapovaní znamienka a odčítaní Eulerov platí

```text
d ln R/dt = Gamma/delta.
```

Registrovaný exponent je `6.1065536987`, teda `R=448.7893835`.
Gauge-invariantná relatívna rýchlosť preto stále rastie fatálne, hoci
pomalšie než v K1. Pri `Gamma->0` zmiznú interakčné členy, backgroundové
zdroje sa rušia a rozmery sadzby sú správne. M-010 je potvrdená iba pre
presnú constant-rate `Q^mu || u_f` triedu.

## 5. A2-K5 — akcia, sila a observačne obmedzený no-go

Konkrétna akcia používa konformnú hmotnosť popola `A(varphi)` s
`beta=d ln A/d varphi`. Rovnaká väzba dáva naraz

```text
rho_c,dot+3H rho_c = beta varphi,dot rho_c,
G_eff/G = 1 + 2 beta^2 F(k,a),  F>=0.
```

Nenulový registrovaný tok vyžaduje `beta!=0`; obyčajné otočenie znamienka
`beta` nemení príťažlivý člen `beta^2`. Pri `lambda->0` platí `beta->0`,
zmizne tok aj piata sila. Akcia preto nemôže ponechať rovnaký tok a ručne
odstrániť silu bez zmeny teórie.

Konzervatívny CMB-kotvený screen dal `S8=0.983642--1.006266` a nezávislá
aritmetika

```text
A_s,req/A_s = (0.863/S8)^2
```

vyžaduje zníženie primordiálnej amplitúdy o `23.0255--26.4477 %`.
Toto nie je vlastná úplná Boltzmannova likelihood K5, preto sa nezvyšuje
kanonická hĺbka a rozsudok sa nesmie rozšíriť na všetky piate sily.
Je to však konzervatívny nutný screen konkrétnej akcie: jej povinný
príťažlivý príspevok tlačí zhlukovanie nesprávnym smerom. M-012 je preto
potvrdená v presnom rozsahu akcie.

## 6. A2-K6 — spojitá veta namiesto gridového dojmu

Pre akciu K6 a `r=2 eta>=0` má auditovaný kvázistatický koeficient tvar

```text
mu_cc(r) = (n0+r n1)/(1+r d).
```

Derivácia má na fyzickom intervale konštantné znamienko. Endpointy sú

```text
mu_cc(eta=0,z=0)=5.674661891,
lim eta->infinity mu_cc(z=0)=163.646709760.
```

Teda `mu_cc(z=0)>1` pre každý `eta>=0`; medzi bodmi gridu nemôže byť
skrytý ostrov s požadovaným `mu_cc<=1`. Presný `eta->0` limit reprodukuje
konformnú K5 silu a `f1->0` limit reprodukuje čistý momentum limit.
M-013 je potvrdená iba pre uvedenú akciu a zdravý interval, nie pre každý
možný momentum operátor.

## 7. Kontrola falošného PASS a falošnej smrti

- žiadny z piatich rozsudkov nepoužíva historický fixed-`K_MPC`
  denominator K4/K7;
- rozhodujúci dôvod je analytický hlavný symbol, gauge-invariantný
  relatívny mód, znamienko vynútené akciou alebo spojitá racionálna veta;
- žiadny verdikt nestojí iba na `PASS/FAIL` reťazci v JSON;
- skoré zastavenie K1/K2/K3/K6 je oprávnené, lebo neskoršie brány nemôžu
  opraviť porušenú nutnú podmienku bez zmeny fyziky;
- K5 nezískava späť historických `75/100`; neskorý screen zabíja akciu,
  ale preskočené G5–G7 sa nepovažujú za prejdené.

## 8. Autoritatívny záver R7

R7 je pre A2-K1, K2, K3, K5 a K6 **uzavretá ako
`CONFIRMED_SCOPE`**. Tieto koľaje nedosiahnu `50/100`, pretože zomreli na
nutnej fyzikálnej podmienke skôr. Oživenie je možné iba ako nová koľaj s
explicitne zmeneným mechanizmom a sekciou, ktorá odstráni konkrétnu príčinu
smrti; nie premenovaním skriptu, zmenou gauge alebo jemnejším solverom.

Súvisiace autoritatívne dokumenty:

- `Audit/A2_K1_K5_RETROSPEKTIVNY_AUDIT_MAX_HLBKY_ROVNIC_VYPOCTOV_A_ROZSUDKOV.md`;
- `Audit/A2_K6_MRTVA_M013_exact_Gij_a_spojity_eta_no_go.md`;
- `Audit/JEDNOTNA_SEKVENCNA_STUPNICA_HLBKY_A2_A_REKALIBRACIA_K1_K12.md`;
- `Independent_Audits/00_RETROSPECTIVE_AUDIT_MASTER_PLAN_SK.md`.
