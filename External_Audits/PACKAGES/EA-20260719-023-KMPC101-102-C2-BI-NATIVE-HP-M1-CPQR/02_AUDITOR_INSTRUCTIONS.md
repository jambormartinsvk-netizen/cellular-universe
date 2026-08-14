# Pokyny externému auditorovi — EA-023

Over manifest, source/copy paritu, runtime dependency closure a oddelenie
PF-104 od vecného CPQR výsledku. Reprodukcie rob v dvoch samostatných
čerstvých kópiách `REPRO`; generated artefakt jednej vetvy nesmie byť vstupom
druhej.

Over najmä:

- že predregistrácie 165/166 vznikli pred príslušnými Python behmi;
- V9 SHA je rovnaký v KMPC-101 aj routing-only KMPC-102;
- PF-104 vznikol v `guarded_import` pre basename output cestu a nevolal
  `run_atom`, M1 assembly ani production CPQR;
- shape `121×98`, rank `98/98`, absolute rank threshold `3.3618661e-58`;
- min resolved CPQR diagonal `0.7279919762` a max `336.1866148436`;
- ortogonalita `3.2077340e-81`, relatívna faktorizácia `1.0034615e-82`,
  relatívny normálový reziduál `7.8497783e-85` a unweighted L2
  `6.1837151e-83`;
- presne jeden native HP-M1 solve, nulové row scaling a pôvodný unweighted
  least-squares objective;
- lokálny M1 driver/holdout PASS, ale všetky physics summary polia false a
  explicitný diagnostic-only verdict role;
- že CPQR ratio nie je dokumentované ako SVD condition number;
- technický counter reset `1/10→0/10` nemení C2/P5/K4 skóre.

Pre každý príkaz zapíš exit code, wall time, SHA generated JSON a odchýlky.
PF-104 vetva má exit 2 a presný failure raw; KMPC-102 vetva má exit 0 a
field-level paritu okrem runtime. Každú ďalšiu odchýlku označ osobitne.
