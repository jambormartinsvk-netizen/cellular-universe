# KMPC-101 — natívny 80-dps rank-revealing M1 CPQR: predregistrácia

**Dátum:** 2026-07-19  
**Autor teórie:** Martin Jambor  
**Tvorca skriptu:** Codex (OpenAI)  
**Stav:** `PREREGISTERED / NOT_RUN`  
**Technický counter pred behom:** `0/10`

## Dôvod a jediná otázka

KMPC-099/100 ukázal, že natívna 80-dps a nezávisle zostavená frozen
binary64 M1 matica majú po projekcii rovnaký plný rank `98/98`, condition
približne `634.52` a líšia sa iba v 26 prvkoch na úrovni najviac
`1.7763568394002505e-15`. Predošlé `mpmath.qr_solve` preto nie je dôkaz
singularity; otvorená je hranica nepivotovaného QR algoritmu.

KMPC-101 smie zodpovedať iba:

> Má tá istá natívne zostavená 80-dps reduced M1 matica hodnosť 98 a dá sa
> jej pôvodný nevážený least-squares problém vyriešiť explicitne
> rank-revealing stĺpcovo pivotovaným QR?

## Zmrazená numerická metóda

- presnosť: presne `80 dps`;
- matica/RHS: natívna M1 assembly, očakávaný rozmer `121 × 98`;
- solver: modified Gram-Schmidt QR so stĺpcovým pivotovaním;
- reortogonalizácia: presne dva priechody;
- relatívny rank prah: `1e-60 × max(initial column norm)`;
- objective: pôvodné `min ||Ax-b||_2`, bez váh;
- škálovanie riadkov: zakázané;
- zmena rovníc, supportu, anchoru alebo fyzikálnych prahov: zakázaná;
- rank-deficientná vetva: trailing pivot premenné ostanú nulové a vyrieši sa
  iba rozlíšený horný trojuholníkový blok; rank sa nesmie falšovať;
- presne jeden production CPQR solve.

Numerický kontrakt pre plný rank vyžaduje súčasne:

- `rank = 98`;
- `max|Q^TQ-I| <= 1e-60`;
- relatívnu chybu faktorizácie `max|AP-QR|/max(max column norm,1) <= 1e-60`;
- relatívny normálový reziduál
  `max|A^T(Ax-b)|/(||A||_F max(||Ax-b||_2,1)) <= 1e-55`;
- konečné diagnostické hodnoty.

Smoke pred official behom musí preukázať:

1. plnohodnostnú `5 × 3` maticu s vynúteným stĺpcovým pivotom, presným
   riešením a nulovým reziduálom v tolerancii `1e-60`;
2. presne rank-deficientnú `4 × 3` maticu s identifikovaným rankom `2`;
3. obnovenie runtime ownera a nulový zápis result súboru.

## Rozhodovací strom

- Ak numerický kontrakt prejde, kandidát je
  `REVIEW_C2_BI_K0p15_NATIVE_HP_M1_CPQR_COMPLETE`.
- Ak matica nemá rank 98 alebo niektorá numerická invariantná kontrola
  neprejde, kandidát je
  `REVIEW_C2_BI_K0p15_NATIVE_HP_M1_CPQR_UNCLOSED`.
- Skript nesmie udeliť fyzikálny PASS, zmeniť C2 skóre, P5 stav ani K4
  hĺbku. Raw driver/holdout výsledky sú iba vstup pre následný interný audit.

## Scope

Zahrnuté sú iba natívna M1 assembly a jej CPQR. Vylúčené sú F0, M3,
coefficient attribution, C2 physics gate, ďalšie módy/k/varianty, `[0,9]`,
S–M, ODE, P5.4, G8/G9 a release trigger.

## Zmrazená implementácia pred prvým Python behom

- V9 CPQR modul:
  `8EBDA7232BEADF0640A2C8361B444A9A896EB215E159E552AC494EAE2C0CCD0A`;
- runner 345:
  `227DDD650B34859F485AAE165173991AD450BB160F7E2998AA9124C4FF317478`;
- atomický/high-precision harness:
  `735A52A6098274EDCDEA187BC940709307C6E6231FCDF4AE906FE661420B13B5` /
  `8DBDA0837A088E0F26137DAB226AA6D49DBF5E52FDD014F81925DAC86DF1906D`;
- statická kontrola: `38/38` source a `14/14` prerequisite hashov sedí.

Do vytvorenia tejto predregistrácie nebol V9 ani runner 345 spustený cez
Python. Od tohto bodu sú V9, runner 345, metóda, prahy a rozhodovací strom
immutable.
