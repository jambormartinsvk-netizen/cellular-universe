# A2-K4 / K7b P0 — predregistrácia offline agregácie segmentov

Dátum: 2026-07-15  
Typ: `REGRESSION`, bez nového vedeckého behu  
Skóre: `NONE`

Skript 195 nesmie importovať ani volať `subprocess`. Smie iba prečítať deväť zachovaných JSON segmentov a manifest ich pozorovaných exit kódov/hashov. Overovacie predikáty sa nemenia oproti skoršej P0 a segmentovanej predregistrácii:

- šesť pozitívnych verdictov a nulové failed checks;
- zaokrúhlené metriky v relatívnej tolerancii `1e-4`;
- NID baseline/kandidát exact SHA-256 kanonického fyzikálneho payloadu;
- solver counts `fixed/free/rank/conflict = 30/58/58/0` a fixed error pod `1e-60`;
- tri negatívne pozorované exity `1`, REVIEW verdict, presne tri rank checky false, presná fault metadata a nezmenený dynamics fingerprint;
- súlad každého raw súboru s hashom v manifeste.

Interný aj externý limit offline agregácie je najviac 5 s. Ak chýba súbor, hash nesedí alebo niektorý predikát zlyhá, výsledok je REVIEW, nie smrť K4.

Po pridaní skriptov 195/196 má checker 196 očakávať 200 ostatných `.py` súborov a 68 karanténnych položiek. Pridá 193 a 194 ako `SUPERSEDED`; 193 sa rutinne neopakuje, pretože monoliticky timeoutoval a jeho funkciu nahrádza segmentovaná agregácia 195.

