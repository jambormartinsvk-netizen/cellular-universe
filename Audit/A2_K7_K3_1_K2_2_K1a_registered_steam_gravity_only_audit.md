# A2-K7.1a-K3.1-K2.2-K1a — audit registrovanej pary s iba gravitačnou väzbou

**Dátum:** 2026-07-13  
**Skript:** `scripts/60_script_A2_K7_K3_1_K2_2_K1a_registered_steam_gravity_rate.py`  
**Verdikt:** `MŔTVA M-014d1`  
**Max. hĺbka:** `40/100`  
**Akceptované skóre K7:** `30/100`

## 1. Hypotéza

Ako lokálny termálny bath sa použije už registrovaná „para“: tepelný
gravitonový relikt s `T_0=0.905 K` a `Delta N_eff=0.0535`. Výhodou je, že
jej backgroundová energia už je započítaná v radiačnom sektore; nepridáva sa
nová skrytá hustota.

Audit tejto podkoľaji prijal hodnoty pary v jej vlastný prospech, hoci
Register 05 už v Q18/Q23 a obmedzení L2 označuje jej dnešnú teplotu a
`Delta N_eff` za podmienené, kým nie je odvodený exit/reheating a história
zdroja.

## 2. Dve odlišné časové podmienky

Bath môže mať krátku vnútornú oscilačnú škálu `tau_corr~1/T`, ale zároveň
takmer vôbec neinteragovať so systémom. Preto sa osobitne testovalo:

1. kinematické oddelenie `T/H >> 1`;
2. interakčná rýchlosť schopná vytvoriť požadovanú disipáciu.

Prvý bod nestačí na druhý.

## 3. Optimistický gravitačný odhad

Pri energiách hlboko pod Planckovou škálou dáva rozmerová low-energy
gravitačná EFT pre proces `2->2`

```text
sigma_grav ~ T^2/Mbar_Pl^4,
Gamma_grav ~ n sigma ~ T^5/Mbar_Pl^4.
```

Skript úmyselne použil prefaktor 1 a zníženú Planckovu hmotnosť
`Mbar_Pl=2.435e27 eV`, čo maximalizuje odhadovanú rýchlosť. K7 pritom
vyžaduje

```text
Q1/(H rho_F) = (1-epsilon) lambda/E
                + 3 epsilon(1-delta).
```

Porovnanie je nevyhnutná rádová brána: procesy s interakčnou rýchlosťou o
viac než 80 rádov menšou než požadovaná frakčná konverzia energie nemôžu
generovať registrovaný lokálny transportný člen. Neurčitosť prefaktora
rádu 1 tento záver nemení.

## 4. Výsledok

| Veličina | Rekombinácia | Dnes |
|---|---:|---:|
| `T/H` | `2.547e27` | `5.509e28` |
| `Gamma_grav/H` | `3.795e-87` | `5.796e-98` |
| požadované `Q1/(H rho_F)` | `6.796e-4` až `6.060e-2` | `0.1506` až `0.2075` |

Najlepší bod v celej histórii zaostáva za požadovanou rýchlosťou o
`83.25` rádu pri `epsilon/delta=0.01`; pri vyššom mediátorovom podiele sa
deficit zväčšuje až na `85.20` rádu. Dnes je deficit približne 96–97 rádov.

Kinematická korelačná škála teda prešla, ale fyzikálna interakčná rýchlosť
nie.

## 5. Dôvod smrti

K2.2-K1a je `MŔTVA M-014d1`: registrovaný gravitonový relikt s iba
gravitačnou väzbou je príliš slabo viazaný, aby vytvoril K7 reakčný a
disipatívny kernel. Smrť nespôsobila energia ani tlak bathu — tie boli už
v backgrounde — ale 83–97-rádový nedostatok interakčnej rýchlosti.

Koľaj si ponecháva `Max. hĺbka 40/100`, pretože konkrétny bath kandidát
prešiel rozmerovou, backgroundovou a mikrofyzickou rate bránou až k
falzifikácii. To nepromuje nadradenú K7; jej prijatý stav ostáva `30/100`.

## 6. Obmedzenie staršej formulácie

Staršia veta „para je tepelný gravitonový relikt“ neznamená „para je
aktívny lokálny termalizačný bath pre palivo“. Tepelný tvar distribúcie
môže prežiť po decouplingu, zatiaľ čo interakčná rýchlosť je zanedbateľná.
Odteraz sa tieto dve tvrdenia nesmú zamieňať.

Pridanie novej negravitačnej väzby nie je oprava K1a. Je to nová podkoľaj
K1b a musí prejsť konzistenciou hmotnostne nulového spin-2 poľa,
univerzálnosťou väzby a observačnými dôsledkami.

## 7. Primárne zdroje

- Weinberg, *Photons and Gravitons in S-Matrix Theory*,
  <https://doi.org/10.1103/PhysRev.135.B1049> — konzistencia a univerzálnosť
  väzby hmotnostne nulového spin-2 poľa.
- Ghiglieri et al., *Double-graviton production from Standard Model plasma*,
  <https://arxiv.org/abs/2401.08766> — Planckovsky potlačené gravitonové
  produkčné rýchlosti v termálnej plazme.
- Choi, Chiang, LoVerde, *Probing Decoupling in Dark Sectors with the CMB*,
  <https://arxiv.org/abs/1804.10180> — rozlíšenie free-streaming a
  tightly-coupled relatívnych reliktov.

