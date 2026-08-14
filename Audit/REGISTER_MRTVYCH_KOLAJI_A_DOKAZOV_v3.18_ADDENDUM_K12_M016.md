# Register mŕtvych koľají — dodatok M-016

**Dátum:** 2026-07-14  
**Rozsah:** iba A2-K12/K1

## M-016 — presne symetrický dvojzložkový popol bez produkčného operátora

**Koľaj:** dva druhy popola s `beta_+=+beta`, `beta_-=-beta`,
`rho_+=rho_-`; jediným zdrojom údajného toku je konformná výmena so
skalárom.

**Maximálna dosiahnutá hĺbka:** `25/100` — kovariantný ansatz,
backgroundový súčet a prvá kvázistatická vlastná matica.

**Dôvod smrti:** pri presnej symetrii

```text
Q_scalar,total = beta varphi' (rho_+ - rho_-) = 0.
```

Koľaj preto nereprodukuje požadovaný nenulový tok palivo -> popol. Súčasne
má jej celkový symetrický lineárny mód v testovanom ľahkom skalárnom limite
vlastnú hodnotu `mu_total=1`, takže samotné opačné náboje neposkytli ani
požadované lineárne zníženie `S8`.

**Čo M-016 nezabíja:**

- asymetrickú K12-K2, kým neprejde vlastným testom toku a rastu;
- K12-K3 so samostatne odvodenou produkciou páru `fuel -> c+ + c-`;
- všeobecne všetky viaczložkové modely alebo všetky piate sily.

**Podmienka zákazu návratu:** K12-K1 sa nesmie oživiť iba tvrdením, že
odpudzovanie opačných nábojov vytvára energiu alebo automaticky znižuje
`sigma8`. Nová koľaj musí pridať fyzikálne odlišný produkčný operátor alebo
preukázateľne nenulovú asymetriu a dostať nové označenie.

## Zachované dôkazy

- `Audit/A2_K12_0_DVOJZLOZKOVY_POPOL_OPACNE_SKALARNE_NABOJE.md`
- `Questions/A2_K12_PROBLEM_KOLAJE_A_DALSI_POSTUP.md`
- `scripts/65_script_A2_K12_two_opposite_charge_ash_analytic_gate.py`
- `scripts/OUTPUT_A2_K12_0_65.md`

