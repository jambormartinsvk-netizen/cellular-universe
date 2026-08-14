# A3-K5/K1 — MŔTVA M-012: CMB-normalizovaná rastová brána

**Dátum:** 2026-07-13  
**Koľaj:** A2-K5/K1, kanonický skalár s konformne viazaným CDM  
**Rozsudok:** `MŔTVA — ARCHIVOVANÁ M-012`  
**Rozsah rozsudku:** registrované parametre `lambda=0.15`,
`delta=0.02297`, `H0=66.37 km/s/Mpc`, `Omega_m0=0.3517`,
`Delta Neff=0.0535` a konkrétna akcia K5/K1

## 1. Čo sa rozhodovalo

A2-K5.1 dokázala, že akcia K5/K1 má konzistentný background, úplné lineárne
rovnice, nulový limit a regulárny superhorizontový mód. Zostala však červená
rastová brána: tá istá konformná väzba, ktorá realizuje tok energie A1,
vynucuje príťažlivú silu CDM a v subhorizontovej limite zvyšuje rast.

A3 mala rozhodnúť, či CMB normalizácia môže skorší alarm
`S8 približne 0.920` zachrániť. Pri tomto rozsudku sa piata sila nezakazuje.
Súdi sa iba jej povinné znamienko a veľkosť v akcii K5/K1.

## 2. Metóda a poctivé obmedzenie

Použitý bol CAMB 1.6.6 z lokálneho adresára `.deps/python`. Binárny CAMB
neobsahuje vlastné rovnice K5/K1, preto výpočet nie je označený ako plná
TT/TE/EE/lensing likelihood. Brána pozostáva z dvoch oddelených častí:

1. CAMB vytvoril CMB-normalizované lineárne `P(k)` pri registrovanom
   `A_s=2.1e-9`, `n_s=0.96432`, hustotách a dvoch vopred existujúcich
   backgroundových zástupcoch.
2. Akciou odvodené rovnice K5/K1 zo skriptu 33 vypočítali pomer váženého
   rastu CDM+baryónov na presnom A1 backgrounde.

V prospech koľaje bola korekcia rastu pre všetky
`k<0.01 h/Mpc` násilne nastavená na 1. Výsledok je teda konzervatívnejší než
priamy prenos kvázistatickej korekcie na všetky mierky.

KiDS-Legacy kotva je `S8=0.815 +0.016/-0.021`. Vopred zapísaná
jednorozmerná screeningová hrana bola

```text
S8_screen = 0.815 + 3*0.016 = 0.863.
```

Táto hrana nie je náhradou novej analýzy KiDS likelihood v modifikovanej
gravitácii. Slúži ako konzervatívna brána, ktorú výsledok minul s veľkou
rezervou. Primárny výsledok KiDS je v
[Wright et al., KiDS-Legacy](https://arxiv.org/abs/2503.19441).

## 3. Reprodukovateľné výsledky

### 3.1 Numerické kontroly

| Kontrola | Výsledok |
|---|---:|
| CAMB | 1.6.6 |
| Python | 3.11.3 |
| nezávislá integrácia `sigma8` vs CAMB, konštantné `w_f` | relatívna chyba `2.875e-4` |
| nezávislá integrácia `sigma8` vs CAMB, CPL | relatívna chyba `3.568e-4` |
| nulový limit `lambda=0` | `max abs(R_growth-1)=0.0` |
| K5/K1 vážený pomer rastu na `0.01–5 h/Mpc` | `1.051963–1.053053` |

### 3.2 CMB kotva a K5/K1 rast

| Backgroundový zástupca | CAMB `sigma8` | CAMB `S8` | hybridné K5/K1 `S8` |
|---|---:|---:|---:|
| konštantné `w_f=-0.97703` | 0.862480 | 0.933845 | **0.983642** |
| už používané CPL `w0=-0.919`, `wa=-0.612` | 0.882256 | 0.955257 | **1.006266** |

Oba zvýhodnené výsledky sú nad screeningovou hranou 0.863. Staršia interná
projekcia 0.920 bola nižšia, nie prísnejšia.

### 3.3 Pokus o záchranu amplitúdou

Pri pevnom transfere platí `S8 proportional sqrt(A_s)`. Na návrat iba k
3-sigma hrane 0.863 by bolo treba:

| Prípad | požadované `A_s` | pokles oproti `2.1e-9` |
|---|---:|---:|
| konštantné `w_f` | `1.6165e-9` | 23.03 % |
| CPL | `1.5446e-9` | 26.45 % |
| aj stará projekcia 0.920 | `1.8478e-9` | 12.01 % |

Planck uvádza pre základný model
`ln(10^10 A_s)=3.044 +/- 0.014`; záchrana prvých dvoch prípadov by ležala
diagnosticky 18.7 až 21.9 takýchto šírok nižšie. Toto číslo nie je K5/K1
likelihoodová signifikancia, ale dokazuje, že potrebný posun nie je malou
CMB-normalizačnou korekciou. Pozri
[Planck 2018 VI](https://arxiv.org/abs/1807.06209).

## 4. Prečo je rozsudok smrť a nie iba ďalší alarm

- Väzba K5/K1 je pri rekombinácii zanedbateľná, takže primárna CMB amplitúda
  nemá mechanizmus na pokles o 23–26 %.
- Rastová korekcia bola na veľkých mierkach odstránená v prospech koľaje.
- Dva rozdielne, vopred existujúce backgroundové zástupce zlyhali rovnakým
  smerom.
- Nulový limit je presný a nezávislá integrácia `sigma8` reprodukuje CAMB.
- Koľaj nemá voľný, mikrofyzicky odvodený člen, ktorý by povinnú príťažlivú
  silu kompenzoval. Jeho dodanie by definovalo novú akciu a novú koľaj.

Preto K5/K1 pri registrovaných parametroch neprechádza A3 rastovou bránou.
Rozsudok netvrdí, že každá tmavosektorová piata sila je zakázaná, ani že bola
vykonaná plná vlastná K5/K1 likelihood.

## 5. Obmedzenie staršej formulácie

Starší stav

```text
PREŽÍVA A2-K5.1 — 60/100; A3 RASTOVÁ BRÁNA ČERVENÁ
```

bol správny iba pred A3. Od tohto auditu ho nahrádza `MŔTVA M-012`.
A2-K5.1 sa nemaže: zostáva dôkazom, že smrť nevznikla chybou
superhorizontovej konzistencie, ale neskorým rastom konkrétnej akcie.

## 6. Zachované dôkazy

- `scripts/45_script_A3_K5_K1_CAMB_anchor_and_growth_bound.py`
- `scripts/46_script_A3_K5_K1_required_primordial_amplitude.py`
- `scripts/33_script_A2_K5_K1_quasistatic_growth_gate.py`
- `scripts/36_script_A2_K5_K1_weighted_matter_growth_and_S8_projection_corrected_labels.py`
- tento dokument a manifest balíka

Neúspešný pokus nainštalovať nedostupnú verziu CAMB 1.6.7 sa zachováva v
auditnej stope; dostupná a použitá verzia je 1.6.6. Oficiálny CAMB opisuje
výpočet CMB, lensingu a matter spectra v
[dokumentácii CAMB](https://camb.readthedocs.io/en/latest/).

## 7. Podmienka prípadného spätného auditu

K5/K1 sa nesmie vrátiť iba premenovaním alebo pridaním post-data brzdy.
Spätný audit M-012 je prípustný iba pri preukázanej chybe v skriptoch,
zmenenom registrovanom vstupe v novej verzii alebo plnej vlastnej likelihood,
ktorá zároveň vysvetlí CMB normalizáciu a lensing bez nového neodvodeného
rušiaceho parametra.
