# A2-K7 — stav a akčný plán po K3.1 Onsagerovej bráne

**Dátum:** 2026-07-13  
**Kanonický stav K7:** `PREŽÍVA K7.0 — 30/100`  
**Aktívna podkoľaj:** K7.1a-K3.1-K2  
**Aktívny krok:** K3.1-K2.1 — rozmerový bath/background closure

## Stav a maximálna hĺbka

| Podkoľaj | Stav | Max. hĺbka | Dôvod/stena |
|---|---|---:|---|
| K7.1a-K1 | `MŔTVA M-014a` | `32/100` | fixed-width produkcia nevie sledovať `H` |
| K7.1a-K2 | `PREŽÍVA IBA REKONŠTRUKCIU` | `34/100` | chýba kernel/noise |
| K7.1a-K3.0 | `PREŽILA FORMULAČNÚ BRÁNU` | `36/100` | chýbala termodynamická kompletizácia |
| K7.1a-K3.1-K1 | `MŔTVA M-014b` | `38/100` | holá Onsagerova matica má zápornú vlastnú hodnotu |
| **K7.1a-K3.1-K2** | **`PREŽÍVA IBA TERMODYNAMICKÚ FORMULÁCIU`** | **`38/100`** | chýbajú rozmerové coefficients, bulk-pressure background, bath a mikrofyzika |
| K7.1a-K4 | `ČAKÁ` | `5/100` | threshold vetva neauditovaná |

## K3.1-K2.1 — povinné kroky

1. fixovať rozmerovú normalizáciu chemical affinity a expansion force;
2. odvodiť transportnú maticu z collision integrálu alebo SK spektrálnej
   hustoty, nie z voľby `ell=1`;
3. vypočítať bulk pressure a jeho relaxačný čas;
4. znovu uzavrieť
   `rho_F,p_F,rho_M,p_M,rho_phi,p_phi,Pi_bulk` bez dvojitého započítania;
5. otestovať kladnú entalpiu na pôvodnom `epsilon/delta` gride;
6. odvodiť noise covariance a lokálny KMS/Markovovský rozsah;
7. kill ako M-014c pri zápornom eigenmode, neuzavretom backgrounde,
   skrytom bathe alebo post-hoc transportných koeficientoch;
8. iba pri prežití zvýšiť akceptované skóre K7 na najmenej `40/100` a
   pokračovať K7.1b.

## Zákaz návratu

M-014b sa nesmie obísť ponechaním cross-termu a vynechaním recipročného
stressu alebo noise. Taký model je stále mŕtva K3.1-K1.

