# A2-K4/P5.3g4 — výsledok: prvý fotónový TCA kvadrupól a polarizácia

**Dátum:** 2026-07-16  
**Pôvodný JSON verdict:** `DERIVATION_PASS_P5_3G4_PHOTON_TCA_FIRST_ORDER_OPACITY_UNCLOSED`  
**Aktuálny auditný stav:** `FORMULA_PASS_PHOTON_TCA_WITH_SYNCHRONOUS_GAUGE_BRIDGE` (021)  
**Fyzikálna hĺbka A2-K4:** nezmenená, `60/100`.  
**Skóre koľaje:** nezmenené. Tento výsledok nie je P5.4 ani G8 PASS.

## Čo sa overilo

V báze `[F_gamma2, G_gamma0, G_gamma2]` má auditovaný kolízny blok determinant
`-3/10`, plnú hodnosť a nulový priestor iba `{0}`. V tesnoväzbovom limite preto
fotónový kvadrupól ani polarizácia nemôžu mať voľnú nenulovú konštantu.

Pre `epsilon=1/opacity` a deklarovaný skúšobný drive

```text
D = (2 k q_gamma / 5 + 8 k shear / 15, 0, 0),
```

vyšlo presne riešenie `C X + epsilon D = 0`:

```text
F_gamma2 = 8 epsilon k (3 q_gamma + 4 shear) / 45
G_gamma0 = 2 epsilon k (3 q_gamma + 4 shear) / 9
G_gamma2 = 2 epsilon k (3 q_gamma + 4 shear) / 45.
```

Kolízne rezíduum je presne `(0,0,0)` a všetky zložky sú presne nulové pri
`epsilon=0`. To však samo neurčuje, že tento drive je správny v synchronnej
seedovej báze.

## Čo to ešte nepreukazuje

- použitý `shear` je teraz explicitne zmapovaný do synchronnej MB bázy
  výsledkom 021; stále však nejde o celý photon/neutrino seed;
- nepoznáme úplnú `opacity_K4(a)`, teda ani časový rád/amplitúdu seedu;
- `l=3` a vyššie multipóly sú v tomto prvom TCA kroku zámerne odložené;
- neexistuje ešte nezávislý Einsteinov/constraint ledger ani porovnanie dvoch
  počiatočných plôch;
- neprebehla ODE evolúcia, P5.4, G8 ani likelihood.

Preto je to iba formula/provenance PASS podbrány P5.3g4. Nemôže sa používať na
zvýšenie fyzikálnej hĺbky alebo ako dôkaz životaschopnosti A1-K1.

## Reprodukovanie a dôkazy

- predregistrácia: `Questions/A2_K4_P5_3G4_PHOTON_TCA_PREREGISTRATION_2026-07-16.md`;
- runner: `scripts/255_script_KMPC_018_P5_3g4_photon_l2_tca_seed.py`;
- zdieľaná algebra: `scripts/baseScripts/p5_general_synchronous/photon_tca_first_order.py`;
- immutable výstup: `scripts/results/k_mpc_005/RUN_KMPC_018_P5_3G4_PHOTON_TCA_FIRST_ORDER.json`.

Všetkých 13 kontrol prešlo za `0.203 s` pri vnútornom limite 5 s. Výstup nesie
SHA-256 troch zdrojov (73, 76, 84), aby budúci audit vedel odhaliť ich zmenu.

## Ďalší povinný krok

`P5.3g7`: skladať plný fotónový/neutrínový seed na dvoch štartoch a priamo
testovať Einsteinove rezíduá. Gauge most je v
`P5_3_SEEDS/24_P5_3G6_RERUN1_GAUGE_BRIDGE_RESULT_SK.md`.
