# Auditná korekcia organizačného modelu — stanice a cesty koľají

Dátum: 2026-07-15

## Čo bolo v návrhu V1 nepresné

V1 správne navrhol nemenné `PASS/REVIEW/STOP`, jediného vlastníka artefaktu, detailné podvetvy A2-K4 a dvojfázovú migráciu. Nedostatočne však rozlíšil stanice od koľají: vnorenie A1-K1/A2 bolo opísané prevažne ako rodičovstvo mechanizmov, nie ako konkrétny prefix cesty prechádzajúci kontrolnými stanicami.

## Neskoršie spresnenie používateľa

- A1, A2, A3, ... sú stanice;
- úlohou je nájsť postupnosť koľají vedúcu až na poslednú stanicu;
- každá cesta musí ukázať, na ktorej stanici prešla alebo zastala;
- auditov môže byť viac;
- dokumentácia musí uchovať odpovede, reaudity a viac-kolovú diskusiu.

## Dosah korekcie

Inventár 203 skriptov, 221 auditných súborov, 184 Questions a 468 väzieb zostáva platný. Mení sa navrhovaná informačná architektúra:

1. primárny strom je cesta `stanica/koľaj/ďalšia stanica/ďalšia koľaj`;
2. všeobecné definície staníc sú sekundárny katalóg;
3. podkoľaje zostávajú v rámci jednej stanice;
4. každý uzol obsahuje nemenné viac-kolové `AUDIT_THREADS`;
5. terminálny STOP uvádza poslednú dosiahnutú stanicu;
6. výsledok závislý od predchádzajúcej koľaje patrí do konkrétneho route prefixu.

V1 sa nemaže. Jeho organizačný význam je obmedzený týmto dokumentom a návrhom V2; platné bezpečnostné pravidlá V1 sa preberajú do V2.
