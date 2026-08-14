# Odpovede externého auditora

Pre každý balík `EA-...` vznikne rovnako pomenovaný priečinok. Auditor píše
iba Markdown odpovede a nikdy nemení dôkazy v `../PACKAGES/`.

Minimálny prvý súbor je `00_AUDITOR_AUDIT.md`. Ďalšie kolá diskusie sa
pridávajú poradovo bez prepisovania predchádzajúcich odpovedí.

Auditor má každý výstup uložiť ako nový očíslovaný `.md` súbor v response
priečinku príslušného balíka. Ak externé prostredie nemá zápisové právo,
auditor vráti celý text odpovede bez skracovania; hlavný orchestrátor ho
importuje verbatim do nového Markdownu a samostatne pridá autoritatívne
spracovanie. Odpoveď v chate alebo prílohe sa nepovažuje za trvalý záznam,
kým nie je takto importovaná.

Ak sa zistí chybne založená šablóna alebo odpoveď iného balíka, súbor sa
nevymaže ani ticho neprepíše. Označí sa `TEMPLATE_MISFILED_DO_NOT_CITE` a
správna odpoveď dostane nové poradové číslo.

Pravidlá: [protokol balíkov](../00_AUDITOR_PACKAGE_PROTOCOL_SK.md).
