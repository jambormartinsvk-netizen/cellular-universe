# PF-035 — nepredregistrovaný importový probe SciPy

**Fyzika vykonaná:** nie  
**ODE vykonaná:** nie  
**Výsledok:** `SCIPY=1.17.1`

Pri read-only inventári S2 bol spustený krátky Python príkaz `import scipy`
bez samostatného Markdown očakávania pred jeho behom. Nebol otvorený žiadny
výpočtový model, nevznikol JSON a výsledok nemá fyzikálny ani bodový účinok.

Je to však porušenie pravidla „pred každým Python behom Markdown“. Odteraz
je každé overenie závislosti súčasťou S2 preflight očakávania; tento probe sa
nesmie citovať ako autoritatívny S2 výsledok.
