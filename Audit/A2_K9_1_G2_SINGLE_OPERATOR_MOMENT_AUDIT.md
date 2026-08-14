# A2-K9.1 — G2 audit jedného produkčno-rozptylového operátora

## Rozsudok

**A2-K9 zostáva živou návrhovou triedou na G1, 10,0/100. G2 neprešla.**

Pomenovanie „jeden operátor“ je fyzikálne užitočná podmienka proti post-data ladeniu, ale nie je ešte lokálny operátor. Bez konkrétneho collision kernelu, maticového elementu, stavov a distribučných funkcií neurčuje pomer produkcie, momentum transferu a šumu.

## Hlavný dôkaz

Pre produkciu konštantne hmotných častíc s malým pôrodným driftom `v` je štvorhybnostný moment úmerný

```text
Q_prod^mu=m S_n gamma(v) (1,v,0,0).
```

Oproti nulovému driftu:

```text
Delta Q^0 = O(v^2),
Delta Q^x = O(v).
```

Preto dva kernely môžu mať rovnaký počet aj rovnaký FLRW background do lineárneho rádu, ale opačný alebo rozdielny lineárny momentum transfer.

Skript 153 nameral rády:

- energia: `2.00003225`, `2.00000031`, `1.99999998`,
- hybnosť: `1.00002150`, `1.00000021`, `1.000000002`.

To je presne očakávané `v^2` proti `v`.

## Elastická degenerácia

Number-conserving elastický moment

```text
R^mu=(0,-kappa Delta v,0,0)
```

má nulový nultý moment a nulovú backgroundovú energiu, ale mení lineárnu hybnosť. Skript preveril `kappa=0,0.01,0.03,0.10`; všetky mali rovnaký počet a background, no momentum bolo `0,-0.002,-0.006,-0.020`.

Z toho plynie: A1 background ani produkčná sadzba neurčujú `kappa`. Súčet `C_prod+C_el` sa nestáva odvodeným jedným operátorom iba tým, že ho tak pomenujeme.

Kinetická teória všeobecne konštruuje prúd a stresovo-energetický tenzor ako rôzne momenty distribúcie; úplný collision kernel môže určiť oba, ale jeden z momentov nemožno spätne invertovať na celý kernel. Pozri [Sarbach a Zannias](https://arxiv.org/abs/1303.2899). Pri redukcii disipujúceho otvoreného systému sa navyše spravidla objavuje zodpovedajúci šum; príklad odvodenia Boltzmann-Langevinovej štruktúry poskytujú [Calzetta a Hu](https://arxiv.org/abs/hep-ph/9903291). Toto je opora všeobecného metodického požiadavku, nie dôkaz konkrétneho kozmologického kernelu K9.

## Čo by K9 umožnilo prejsť G2/G3

Musí zadať jeden konkrétny mikrofyzický proces, napríklad akciou alebo úplným `C[f]`, a z neho odvodiť:

1. `S_n` a reprodukciu `Gamma rho_f`,
2. prvý moment `Q_c^mu` aj reakciu paliva,
3. tlak a anizotropný stres vzniknutého popola,
4. elastickú relaxačnú sadzbu bez druhého nezávislého post-data parametra,
5. šum/memory a podmienky pozitivity,
6. nulový limit bez produkcie aj bez rozptylu.

Jedna Lagrangiánová väzba môže generovať viac procesov, no ich kozmologické sadzby závisia aj od hmotností, fázového priestoru a distribúcií. Preto sa nesmie vopred tvrdiť jednoduchá rovnosť `gamma_drag=Gamma` bez odvodenia.

## Vzťah ku K8

- K8-Fkin požaduje úplný produkčný collision kernel.
- K9 je nezávislá iba vtedy, ak ten istý konkrétny mikrofyzický proces dá aj nenulový elastický momentum transfer s odvodenou väzbou medzi sadzbami.
- Ak `C_el=0`, K9 sa zlieva s K8-Fkin.
- Ak sa `gamma_drag` pridá nezávisle, návrh poruší definíciu K9 a patrí medzi zamietnuté fenomenologické kombinácie.

## Skripty

- 153: 4/4 PASS, momentové rády a rodina `kappa`.
- 154: 6/6 PASS, nezávislá kontrola interpretácie.
- oba limity 5 s; pozorované runtime pod 0,11 s.

## Stav

K9 nie je mŕtva, ale nemá konkrétnu dcéru pripravenú na G2. Skóre zostáva 10,0/100; pokrok je zaznamenaný ako uzavretý negatívny test dostatočnosti samotného názvu mechanizmu.

