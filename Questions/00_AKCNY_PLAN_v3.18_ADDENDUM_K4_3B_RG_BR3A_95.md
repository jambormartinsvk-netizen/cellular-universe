# Akčný plán v3.18 — dodatok po K4.3b-RG-BR3A

**Dátum:** 2026-07-14  
**Supersession:** nahrádza iba aktívny K4.3b-RG-BR krok staršieho dodatku 86.

## Priorita

```text
A1-K1 background: živý.
A2-K4: živá, 60/100 = G6.
BR1/BR2/BR3A: dokončené.
Aktívne: BR3B indukované frakčné metric/species koeficienty.
```

## Poradie ďalšej práce

1. **BR3B-1:** zostaviť módovo závislý Puiseuxov koeficientový ansatz;
2. **BR3B-2:** vyriešiť metric, photon–baryon a collective free-streaming
   korekcie pri fuel/ash zdrojoch zo skriptu 95;
3. **BR3B-3:** overiť hodnosť, nulové/gauge smery a štyri Einsteinove
   koeficientové rezíduá;
4. **BR3B-4:** residual-scaling a dve hĺbky;
5. **K4.3b backendová brána:** plná photon hierarchia, polarizácia, opacity,
   tight-coupling switch a recombination s hard limitmi;
6. **nulový a konvergenčný balík:** `lambda->0`, krok, `lmax`, štart;
7. **rozsudok K4.3b/G7:** PASS, REVIEW/NEUZAVRETÁ alebo fyzikálna smrť s
   uchovaným dôvodom a skriptmi;
8. **až potom K4.3c/A3:** CMB/LSS transfery a likelihood.

## Dokumentačné a vydávacie úlohy

- po uzavretí K4.3b rozdeliť dokumentáciu do logických adresárov;
- skontrolovať odkazy a odstrániť iba duplicity, nie historické negatívne
  behy ani mŕtve koľaje;
- vytvoriť changelog a SHA-256 manifest;
- commitnúť na GitHub pred Zenodo vydaním;
- pokiaľ sa nemení fundament, verzia zostáva v rade `3.x`.

