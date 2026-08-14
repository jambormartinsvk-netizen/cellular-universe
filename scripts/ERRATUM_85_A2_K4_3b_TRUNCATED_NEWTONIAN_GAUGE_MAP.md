# Erratum skriptu 85 — nedostatočný rád Newtonovskej gauge transformácie

Skript 85 použil vedúce regulárne synchronous série CLASS a transformoval ich
do Newtonovej gauge. Pri NID a najmä NIV však konečný Newtonovský potenciál
vzniká až po zrušení viacerých vedúcich kompenzovaných členov. Zdrojové série
84 boli dostatočné na regulárny synchronous seed, ale nie na túto transformáciu.

Výsledky `delta_c≈2.85e5`, zlá štartová konvergencia NID/NIV a zlyhaný
`lambda=0` test sú preto chybou rozsahu skriptu, nie smrťou K4 ani fyzikálnou
nestabilitou. Skript 86 zostáva vo všeobecnej synchronous gauge, používa
regulárny metrický zdroj `h_x` a po zapnutí K4 dynamicky vyvíja `theta_c`.

Skript 85 a jeho výstup sa zachovávajú ako negatívny audit: vedúci synchronous
rad sa nesmie bez dodatočných vyšších koeficientov používať na Newtonovský
NID/NIV test.
