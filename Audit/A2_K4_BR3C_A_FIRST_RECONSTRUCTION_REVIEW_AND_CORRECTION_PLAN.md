# A2-K4 BR3C-a — REVIEW prvého stavového exportu a plán korekcie

**Dátum:** 2026-07-14  
**Skripty:** 130 a 131  
**Rozsudok C7.7a:** `REVIEW / NEUZAVRETÁ`  
**Jemná hĺbka:** zostáva `66.0/100`  
**K4:** živá; žiadny dôvod fyzikálnej smrti

## Výsledok prvého behu

Skript 130 skončil:

```text
PASS_BR3C_A_TWO_SURFACE_STATE
74/74 interných kontrol
runtime približne 0.81 s
```

Tento machine PASS však nebol prijatý samostatne. Nezávislý skript 131
porovnal stav zostavený pri štandardnom ráde 5 a 6 a skončil:

```text
REVIEW_BR3C_A_ORDER_AUDIT_UNCLOSED
maximum_absolute_difference = 2.15616e4
maximum_scaled_difference   = 1.73729
```

Najväčšie rozdiely boli v rekonštruovaných `F3/F4`; neprešli ani niektoré
malé metric/species zložky. C7.7a preto nedostala `+0.2`.

## Hlavná príčina

Skript 130 vyhodnocoval surové least-squares koeficienty. Koeficientový
ledger pritom niektorým slotom ukladá **presnú nulu** z počiatočnej
normalizácie alebo gradientovej regularity. Numerický solver ich v surovom
vektore reprezentuje round-off hodnotami, napríklad pri NID:

```text
fractional L3, layer 0  =  3.94e-16
fractional L4, layer 0  = -1.39e-16
```

Pre coefficient-rank audit sú tieto hodnoty neškodné. Pri exporte fyzického
multipólu sa však používa `F3=L3/s` a `F4=L4/s^2`. Na hlbokom povrchu je
`s` veľmi malé, takže zakázaný round-off slot sa umelo zosilní. Pozorovaný
veľký `F4` rozdiel preto nie je dôkaz high-ell runaway; je dôkaz, že stavový
export nerešpektoval presné nulové podmienky vlastného ledgeru.

Druhá, menšia chyba skriptu 131 bola bitová rovnosť celého normalizačného
slovníka medzi dvoma least-squares rádmi. Predregistrácia vyžadovala rovnaký
anchor v tolerancii, nie identickú IEEE reprezentáciu.

## Povolená korekcia pred ďalším behom

Korekcia nesmie zaviesť prah typu „všetko menšie než epsilon nastav na
nulu“. Nulovať sa smú iba sloty, ktoré boli už pred behom explicitne
zaregistrované ako presné počiatočné alebo regularitné podmienky:

1. štandardné NID/NIV nulové počiatočné sloty;
2. štandardné `L3/L4` sloty pod prvým gradientovo dovoleným rádom;
3. fuel `delta_f/U_f` sloty `-1` a `0` fixované pôvodným ledgerom;
4. frakčné `L3/L4` sloty pod `first_l3/first_l4` z opravy 127.

Každý odstránený slot musí byť vypísaný v projection ledgeri. Nenulové
fyzikálne koeficienty sa nesmú meniť.

Normalizačný anchor sa v nezávislom audite porovná s absolútnou toleranciou
`2e-12`; názov anchoru, očakávaná hodnota, seed amplitude a fuel coefficient
musia zostať rovnaké presne.

## Rozhodovací strom

- Ak presná ledgerová projekcia prejde pôvodným stavovým testom rádov 5/6,
  C7.7a dostane `+0.2` a K4 postúpi na BR3C-b.
- Ak rozdiel zostane v nenulových fyzikálnych koeficientoch, C7.7a ostane
  `UNCLOSED` a musí sa auditovať conditioning koeficientového solvera.
- Ak sa po conditioning audite potvrdí, že spoločný regulárny stav
  neexistuje, až vtedy môže vzniknúť fyzikálny dôvod smrti.

Skripty 130/131 a ich negatívny výsledok sa zachovávajú; opravené verzie
musia dostať nové čísla.

