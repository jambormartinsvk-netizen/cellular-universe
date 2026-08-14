# A2-K7.1a-K3.1-K2.2-K1a2a — audit nekoherentného KMS gravitonového prechodu

**Dátum:** 2026-07-13  
**Skript:** `scripts/62_script_A2_K7_K3_1_K2_2_K1a2a_incoherent_KMS_graviton_transition.py`  
**Verdikt:** `MŔTVA M-014d1b`  
**Max. hĺbka:** `42/100`  
**Akceptované skóre K7:** `30/100`

## 1. Hypotéza a rozsah

K1a2a skúma jediný nekoherentný prechod palivo/mediátor, ktorý emituje a
absorbuje kvantum registrovanej gravitonovej pary cez štandardnú univerzálnu
gravitačnú väzbu. Ide o inú realizáciu než thermal `2->2` K1a1.

Skript používa úmyselne optimistickú rozmerovú obálku

```text
Gamma_1 <= C omega^3/Mbar_Pl^2,  C=1.
```

Nie je to presná šírka konkrétneho K7 prechodu. Skutočný quadrupole rate,
výberové pravidlá alebo form factor ho môžu ďalej znížiť. Obálka dáva
nekoherentnej koľaji maximálnu šancu.

Koherentné zosilnenie sa netestuje; patrí do K1a2b.

## 2. KMS/detailed-balance brána

Lokálny termálny bath musí mať nielen spontánnu emisiu, ale aj zodpovedajúci
reverse absorption kanál. Prechod s `omega>>T` má absorpciu potlačenú
Boltzmannovým faktorom. Ako explicitné KMS okno bolo použité

```text
omega/T <= 1.
```

V tomto okne je optimistický maximálny rate

```text
Gamma_KMS,max = T^3/Mbar_Pl^2.
```

## 3. Výsledok

| Veličina | Rekombinácia | Dnes |
|---|---:|---:|
| `Gamma_KMS,max/H` | `3.109e-30` | `5.650e-35` |
| požadované zosilnenie | `2.19e26` až `1.95e28` | `2.67e33` až `3.67e33` |
| potrebné `omega` bez zosilnenia | `51.2` až `229 MeV` | `10.8` až `12.0 MeV` |
| potrebné `omega/T` | `6.02e8` až `2.69e9` | `1.39e11` až `1.54e11` |

Pri potrebnej frekvencii je logaritmus reverse absorption faktora približne
`-2.6e8` až `-1.17e9` pri rekombinácii a `-6.0e10` až `-6.7e10` dnes.
Termálny reverse kanál je teda prakticky nulový.

## 4. Rozsudok

K1a2a je `MŔTVA M-014d1b`:

- v KMS okne `omega<=T` je aj optimistická nekoherentná gravitácia
  nedostatočná najmenej o 26 až 33 rádov;
- frekvencia potrebná na rate bez zosilnenia leží miliardy až stovky
  miliárd krát nad `T`, takže realizácia opúšťa lokálny termálny bath.

Max. hĺbka je `42/100`. Nadradená K1a/K1 ani K7 týmto nezomierajú:
koherentná K1a2b je otvorená. Vysokofrekvenčná spontánna emisia bez reverse
absorption sa presúva do už existujúcej vákuovej/farebnej K2, kde musí byť
auditovaná ako non-KMS memory/noise kernel.

## 5. Čo chýba K1a2b

Potrebné kolektívne alebo maticové zosilnenie je presne vyčíslené, ale
nebolo odvodené. K1a2b musí určiť koherentnú doménu, počet aktívnych
jednotiek, škálovanie amplitúdy/rate, form factor, dekoherenciu, kauzálny
rozmer domény a backreaction. Samotný veľký počet Planckových buniek nie je
dôkaz koherencie.

## 6. Primárne zdroje

- Hu et al., *Gravitational Wave Probe of Planck-scale Physics After
  Inflation*, <https://arxiv.org/abs/2403.13882> — Planckovské potlačenie
  gravitonového bremsstrahlung pri rozpadoch.
- Scandi, Alhambra, *Thermalization in open many-body systems and KMS
  detailed balance*, <https://arxiv.org/abs/2505.20064>.
- Haehl, Loganayagam, Rangamani, *Effective Action for Relativistic
  Hydrodynamics*, <https://arxiv.org/abs/1803.11155>.

