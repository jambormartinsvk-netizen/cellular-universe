# K11-CS2/S0 — PF-062 erratum state registra

**Dátum:** 2026-07-16  
**Dotknutý výsledok:**
`K11_CS2_S0_STRUCTURAL_RESULT_AND_AUDIT.md`  
**Dotknutý base hash:**
`19263A674E1F342E06E6D0D3999E65E58687CCFF20E5EE083A05D06D7BB107FF`  
**Autoritatívne obmedzenie:**
`PASS_FORMULA_IDENTITIES / STOP_STATE_REGISTER_V001`

## Chyba

S0 state register vytvoril photon polarization položky

```text
E_gamma_0, E_gamma_1, ..., E_gamma_lmax.
```

Pinovaný CAMB scalar E-mode reťazec však začína pri `E_2`. Zdroj
`camb.symbolic.E_eq(2)` explicitne používa nulový predchádzajúci multipól;
`E_0` ani `E_1` nie sú stavmi tejto hierarchie.

S0 audit overil správne rovnice `E_l` pre `l=2...8`, ale samostatná
state-count kontrola porovnávala register iba s vlastnou chybnou formulou
`4*lmax+11`. Preto všetky checks mohli byť `true`, hoci register obsahoval
dve nadbytočné premenné. Ide o internú tautologickú parity kontrolu, nie
fyzický state-contract PASS.

## Správny register a počty

Pri zachovaní ostatných S0 konvencií:

```text
base dark/baryon/photon/metric states = 9,
photon temperature F_2...F_lmax      = lmax-1,
photon E polarization E_2...E_lmax   = lmax-1,
neutrino density/velocity/F_2...     = lmax+1,
steam density/velocity/F_2...        = lmax+1.
```

Teda

```text
state_count = 4*lmax+9,
lmax=4 -> 25,
lmax=6 -> 33,
lmax=8 -> 41.
```

## Čo zostáva platné

RUN-002 naďalej presne dokazuje:

- `d_c+d_f=Gamma/H` pre K11-R;
- váženú momentum reaction;
- interaction-only determinant;
- A1 background transfer cancellation a nulovú Fourierovu závislosť;
- CAMB `J_l`, `G_l`, `E_l` koeficientové identity pre `l=2...8`;
- CAMB polarization source identity;
- úspešné interné a vonkajšie execution limity.

## Čo sa ruší

Rušia sa tvrdenia:

- „S0 má fyzicky úplný správny state register“;
- „počty 27/35/43 sú fyzické počty“;
- „36/36 znamená úplný structural PASS“.

Autoritatívny stav RUN-002 je odteraz

```text
PASS_K11_CS2_S0_FORMULA_IDENTITIES_ONLY
STOP_K11_CS2_S0_STATE_REGISTER_V001
```

Nie je to fyzikálna smrť K11 a nemení hĺbku `10/100`.

## Posledná technická oprava 2/2

S0 v001 sa neprepisuje a runner 263 sa nesmie použiť na state/basis
verdikt. Nový full v002 base musí:

1. mať iba `E_2...E_lmax`;
2. očakávať `4*lmax+9` stavov;
3. porovnať presnú množinu state names s nadradeným kontraktom, nie iba
   lokálny count;
4. zaradiť negatívny fixture, ktorý odmietne `E_0` alebo `E_1`;
5. vykonať všetky zostávajúce full DAE brány bez ďalšieho opravného runnera.

Toto je druhá a posledná technická oprava povolená CS2 predregistráciou.
Ďalšia formálna/numerická chyba znamená `REVIEW_BLOCKED_IMPLEMENTATION`, nie
nový suffix ani tretí rerun.

## Neskoršie obmedzenie

Označenie `2/2` uzatvára iba chybný S0-v001 state register. Full v002 nie je
tretí patch v001: je to preregistrovaná úplná architektúra s exact-set
paritou, negatívnym fixture a vlastným capom `0/10`. Technická chyba v002
sa eviduje, ale sama nedáva fyzikálny STOP K11.
