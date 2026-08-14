# Mobilné čítanie — problém K_MPC = 0.05

> **Aktualizácia 2026-07-15:** Tento pôvodný mobilný text slúžil na výber
> koľaje. Aktuálny zjednotený verdict je v
> `17_MOBILE_CHAT_FULL_RECONCILIATION_AUDIT_SK.md`: P2a už určila
> `A_f=7809.270101963506` bez nového fitu; skrátený K7 rad však zomrel iba
> ako plný neskorý background. Čítaj oba dokumenty spolu.

## O čo ide

Vesmír má mať jeden spoločný background: jednu históriu rozpínania `H(a)`.
Táto história nesmie závisieť od toho, akú vlnu poruchy práve skúmame.

`k` označuje vlnu (Fourierov mód). Pri `k=0.05 Mpc^-1` je typická dĺžka
vlny približne 126 Mpc. Je v poriadku, aby `k` určovalo správanie tejto
konkrétnej vlny. Nie je v poriadku, aby určovalo celkovú expanziu vesmíru.

## Čo audit dokázal

V aktuálnom K7 zápise sa po dosadení definícií background zjednoduší na:

```text
D(a,k) = 1 + Omega_m a/Omega_r + k^3.93109 · A(a).
```

Prvé dva členy sú v poriadku. Posledný — palivový — člen stále závisí od
`k`. To znamená: ak `K_MPC=0.05` znamená vlnu, výpočet by dal inú expanziu
pre inú vlnovú dĺžku. Takýto výraz nemožno vložiť do CLASS ako globálne
`H(a)`.

## Čo to NEznamená

Neznamená to, že teória je mŕtva. Znamená to, že ešte nemáme fyzikálne
uzavretú definíciu normalizácie palivového člena a významu `K_MPC`.

CLASS/HyRec backend už funguje a čaká. Zastavený je iba K4 adapter, kým sa
neurčí jedno univerzálne `H_K4(a)`.

## Koľaje

### K-N2 — hlavná živá koľaj

Možno pri `z^p` chýba normalizácia. Potom palivový člen v skutočnosti
reprezentuje `a^p`, nie `(k a)^p`. To by odstránilo chybnú závislosť od
konkrétnej vlny.

Táto hypotéza prejde iba ak:

- normalizácia vyplýva z bezrozmernosti alebo mechanizmu siete;
- nepridá sa nový voľný fit parameter;
- prepočet zachová alebo poctivo zmení už publikované predpovede.

### K-N1 — možná, ale náročnejšia koľaj

`0.05 Mpc^-1` môže byť skutočná pevná vlastnosť siete: jej korelačná dĺžka.
Potom to nie je vlna, ale fyzikálna konštanta `k_*`.

Museli by sme však odvodiť, prečo má presne túto hodnotu. Ak by bola iba
vybraná podľa dát, stala by sa novým fit parametrom.

### Mŕtve pre globálny background

- `K_MPC` je zároveň konkrétny Fourierov mód aj background scale;
- `0.05` je iba ľubovoľná publikačná konvencia;
- zmeniť exponent `p` na nulu len preto, aby problém zmizol.

## Čo potrebujem od autora teórie

Potrebujeme určiť, čo mal pôvodne znamenať `K_MPC=0.05`:

1. konkrétnu vlnu/meraný mód;
2. pevný scale siete;
3. len jednotkovú normalizáciu, ktorá sa omylom dostala do fyzikálneho
   palivového člena.

Podľa odpovede budeme poctivo auditovať K-N2 alebo K-N1.
