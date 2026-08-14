# P5.3g3 — obmedzenie prvého kandidáta a dôvod opakovania

Strojový záznam `RUN_KMPC_014_P5_3G3_STANDARD_NEUTRINO_L2_SERIES.json` a
skript 251 sa **nesmú použiť** ako neutrínový `F2` seed. PF-044 odhalil, že
symbolický prepis použil pomocnú veličinu `tn` zo stredu `class_seed`, zatiaľ
čo BR2 dostáva až návratový `qn=4 tn/(3k)`.

To vysvetľuje podozrivú závislosť NIV kandidáta od `q`. Nejde o fyzikálnu smrť
K4, ani o popretie P5.3g2: P5.3g2 pracoval priamo s návratovým `qn` a jeho
normalizačný most zostáva platný. Oprava musí pochádzať z nového skriptu a
nového immutable JSON; 251 ani jeho výstup sa potichu neprepisujú.

Aj prvý test 252 má PF-045: vyžadoval presnú invariantnosť `eta` pri fixnom
`k tau`, hoci materiový parameter `Omega_m tau` sa pri zmene `k` mení. Jeho
NIV `qn` výsledok je informatívny, ale jeho verdikt sa nesmie použiť ako STOP.
