# ERRATUM M-011 — K4: zisk voči zanikajúcej referencii nie je absolútna explózia

**Dátum:** 2026-07-13  
**Historický rozsudok:** `MŔTVA M-011`  
**Opravený stav 2026-07-13:** **`M-011 POZASTAVENÁ; A2-K4 ZNOVU OTVORENÁ NA K4.1`**  
**Aktuálny stav 2026-07-14:** **`K4.1 PREŠLA; A2-K4 PREŽÍVA 55/100`**  
**Max. hĺbka:** `55/100`

## Chyba rozsudku

Skript 30 správne vypočítal

```text
T_K4=1.5873084655,
T_0=1.4693472258e-5,
T_K4/T_0=108028.1391.
```

Historický kill test použil `ln(T_K4/T_0)=11.5901` ako dôkaz viac než
jedného e-foldu absolútnej nestability. V skutočnosti
`ln(T_K4)=0.4620<1`; veľký pomer vznikol najmä tým, že nulová referencia
silno zanikla.

## Čo zostáva platné

- definícia entalpicky váženého `u_d`;
- odvodené K4 rovnice a nulový limit;
- `det M=-r^2/(1+delta r)<0` pre interakčný podblok;
- číselné výsledky, constrainty a konvergencia skriptu 30;
- maximálna dosiahnutá hĺbka `50/100`.

## Čo sa už nesmie citovať ako dokázané

- že K4 má 11.590 e-foldov **absolútneho** rastu;
- že kladný okamžitý eigenvalue interakčného podbloku sám dokazuje kladný
  globálny exponent celej Einsteinovej sústavy;
- že jediný velocity-isocurvature vektor uzatvára všetky regulárne
  počiatočné módy;
- že M-011 je konečný fyzikálny rozsudok bez K4.1.

## Nový dôkaz

Skripty 63 a 64 pridali regulárny constrained adiabatický mód. Nevznikla
explózia (`1.43903e-6` po normalizácii), no veľmi prísna `k` konvergencia
tesne neprešla (`1.13550e-6 > 1e-6`). Preto sa K4 nevyhlasuje za preživšiu;
iba sa ruší konečnosť starého rozsudku.

## Podmienka nového konečného rozsudku

K4.1 musí otestovať úplnú bázu constraintovo prípustných módov hlboko v
radiačnej ére a osobitne hlásiť absolútny transfer, nulovú referenciu a ich
pomer. Ak vznikne absolútna divergencia, strata linearity alebo neprípustný
observačný transfer, M-011 sa znovu potvrdí s novým dôvodom. Všetky staré
skripty a tento erratum zostanú zachované.

## Aktualizácia po dokončení K4.1 — 2026-07-14

Skripty 66 a 67 nezávisle potvrdili, že deklarovaný perfect-radiation systém
má presne tri regulárne primordiálne módy. Historický fuel-only velocity seed
má projekčné rezíduum `0.9789492202` voči ich úplnému priestoru, a preto nie
je prípustným regulárnym primordiálnym módom.

Najväčší absolútny singulárny transfer regulárnej bázy je `26.4369073223`;
pri amplitúde `1e-5` zostáva auditná norma `2.64369e-4`. Hlavný aj nezávislý
výpočet prešli constraintovou a krokovou konvergenciou. K4.1 preto **prešla**
a K4 prežíva na `55/100`.

M-011 sa nemaže: zostáva historickým rozsudkom s identifikovanou chybou
`ln(T/T0) -> ln(T)`. Už sa však nesmie obnoviť ako dôvod smrti. Prípadná
budúca smrť K4 musí dostať nový dôvod z K4.2 alebo neskoršej brány.

Autoritatívny rozpis je v
`Audit/A2_K4_1_UPLNA_REGULARNA_CONSTRAINT_BAZA_A_ROZSUDOK.md`.

