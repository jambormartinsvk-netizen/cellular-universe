# Čítaj ako prvé — A2 po úplnom breadth/re-entry kole

## Výsledok rozhodnutia

**Priorita sa vracia ku K4.**

Nie preto, že K7/K8/K9/K11/K12 zomreli, ale preto, že všetky potrebujú nový mikrofyzický operátor pred ďalším zmysluplným numerickým testom. K4 už má sekvenčne prejdenú G6 a rozpracovanú G7.

## Aktuálna porovnávacia tabuľka

| Koľaj | Stav | Jemná hĺbka | Pripravenosť ďalšieho kroku |
|---|---|---:|---|
| **K4** | **živá, technicky pozastavená** | **66,5** | **áno: krátke NIV profilovanie existujúcej ODE** |
| K7 | živý rodič | 20,0 | nie: treba nový pozitívny kernel |
| K8 | živá návrhová trieda | 10,0 | nie: treba produkčný `C[f]` |
| K9 | živá návrhová trieda | 10,0 | nie: treba spoločný produkčno-rozptylový kernel |
| K11 | živá hypotéza | 10,0 | nie: treba lokálny ortogonálny operátor |
| K12 | živý rodič cez K2/K3 | 10,0 | nie: treba párový kernel a separačný ledger |

## Bezprostredný K4 krok

Predregistrovať a vykonať C7.7c profilovanie s týmito obmedzeniami:

1. iba jeden mód/povrch/segment na proces;
2. interný limit najviac 8 s a externý najviac 10 s;
3. zaznamenať RHS volania, prijaté/odmietnuté kroky a čas podľa segmentu;
4. žiadne body za profilovanie;
5. podľa výsledku vybrať blokový/analytický Jacobian, solver alebo zmenu premennej pre C7.7c-K5;
6. až K5 smie znovu spustiť úplné štyri trajektórie s limitom 45 s.

## Zákaz návratu

- neopakovať K4 C7.7c-K2/K3/K4 bez novej numerickej zmeny;
- nevkladať voľný drag do K8/K9/K11/K12;
- neoživovať staré K11 skripty 45/47;
- nerozširovať úzke M-014 no-go na celý K7.

