# A2-K4.3a — stav a akčný plán

**Dátum:** 2026-07-14  
**Stav:** `K4.3a FORMULAČNE PREŠLA; K4 ŽIVÁ 60/100; G7 OTVORENÁ`

## Čo je uzavreté

- pevná Newtonova gauge konvencia `Psi`, `Phi` a `theta`;
- druhový ledger `c, f, b, gamma, nu, s`;
- nulový súčet tmavých energetických a hybnostných zdrojov;
- anisotropný Einsteinov constraint;
- návrat ku K4.2 pri nulovom anisotropnom strese;
- radiačný agregovaný limit;
- presná Thomsonova hybnostná konzervácia;
- predregistrácia parných vetiev S1–S3.

## Čo nie je uzavreté

- úplná fotónová polarizačná hierarchia;
- tight coupling a prechod z neho;
- rekombinačná história;
- úplné regulárne počiatočné módy rozšíreného systému;
- konvergencia v `l_max`, čase, `k` a solveri;
- nulový benchmark celej implementácie proti overenému backendu;
- fyzické transfery K4.

## Akčný plán K4.3b

1. **B1 — rovnicový ledger hierarchií:** zapísať exact teplotné a
   polarizačné fotónové multipóly a bezkolízne `nu/s` multipóly. Rovnice
   kotviť na jednej primárnej konvencii a vytvoriť mapovanie symbolov.
2. **B2 — uzávery:** predregistrovať `l_max`, ultrarelativistický fluidný
   approximation switch a tight-coupling switch; žiadny switch nesmie byť
   ladený na požadované `S8`.
3. **B3 — rekombinácia:** najprv použiť rovnakú štandardnú históriu ako
   nulová CAMB referencia. K4 nesmie meniť atómovú fyziku bez novej koľaje.
4. **B4 — regulárna báza:** odvodiť adiabatic a všetky nezávislé pravidelné
   izokurvatúrne módy rozšíreného systému. Neregulárny seed sa nesmie
   vydávať za smrť koľaje.
5. **B5 — automatizované brány:** constrainty `00`, `0i`, slip a `ij`;
   celková energia/hybnosť; nulový K4 limit; lineárne škálovanie; časová a
   multipólová konvergencia.

## Limity behov

- algebraické a čítacie operácie: najviac 15 s;
- každý numerický skript: vnútorný limit najviac 50 s;
- vonkajší limit numerického príkazu: najviac 60 s;
- polling najviac 10 s naraz;
- `TIMEOUT` znamená `NEUZAVRETÉ`, nie fyzikálnu smrť.

## Rozhodovací bod po K4.3b

- **PASS:** pokračovať K4.3c nezávislým implementačným a nulovým testom;
- **FAIL:** vydať nový dôvod smrti s presným rozsahom a zachovať skript aj
  výstup; potom určiť, či FAIL zabíja iba S1 alebo celú K4;
- **TIMEOUT/IMPLEMENTATION ERROR:** opraviť alebo zjednodušiť beh, bez
  fyzikálneho rozsudku.

