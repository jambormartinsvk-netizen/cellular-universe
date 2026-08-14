# Čítaj ako prvé — A2 po breadth triage K8 a K9

## Porovnateľný stav

| Koľaj | Stav | Jemná hĺbka | Najbližšia stena |
|---|---|---:|---|
| K4 | živá, technicky pozastavená | 66,5 | C7.7c/G7: efektívna stuhnutá evolúcia a potom plná Boltzmannova brána |
| K7 | živý rodič | 20,0 | konkrétny pozitívny lokálny kernel G3 |
| K8 | živá návrhová trieda | 10,0 | collision kernel musí určiť prvý/tlakový/šumový moment |
| K9 | živá návrhová trieda | 10,0 | konkrétny spoločný produkčno-rozptylový operátor |
| K11 | živá hypotéza | 10,0 | regulárny lokálny pôvod ortogonálneho transferu |
| K12 | živý rodič cez K2/K3 | 10,0 | asymetrický alebo párový production operator a separačný mód |

## Výsledok breadth triage

K8 ani K9 neodhalili lacný hotový uzáver. Obe zostávajú fyzikálne možné, ale ich ďalší krok je konštrukcia novej mikrofyziky, nie krátky numerický test. K4 preto zostáva najsilnejší existujúci kandidát, hoci jej bezprostredná numerická stena je drahá.

## Odporúčané poradie

1. krátky re-entry audit K11 a K12: preveriť, či odvtedy vznikol konkrétny operátor; bez neho ich ponechať na G1 bez ďalších behov,
2. krátky re-entry audit otvorených K7 listov: identifikovať jediný list s explicitným kernelom,
3. ak žiadny nemá pripravený operátor, vrátiť sa ku K4 a urobiť iba časovo ohraničené profilovanie NIV — nie štvrtý slepý plný beh,
4. na základe profilu predregistrovať C7.7c-K5 s analytickým/blokovým Jacobianom alebo vhodným solverom.

