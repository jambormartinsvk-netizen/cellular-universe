# Audity — route index

**Aktualizované:** 2026-07-16

`Audit/` zostáva fyzicky plochý, aby sa nerozbili citácie a kontrolné súčty.
Kanonické vlastníctvo auditu sa číta z route manifestu:

- A2 register: `tracks/A1/A1K1/A2/00_TRACK_REGISTER.md`;
- každá A2 koľaj: jej vlastný `ARTIFACTS/00_MANIFEST.md` pod
  `tracks/A1/A1K1/A2/` (konkrétne cesty sú v `00_TRACK_REGISTER.md`);
- A2-K4/P5: `tracks/A1/A1K1/A2/A2K4/SUBTRACKS/P5/00_ARTIFACT_INDEX_SK.md`;
- nezávislé lineage audity: `Independent_Audits/Implementation_Lineage/`;
- K_MPC/P4/P5 preregistrácie: `Independent_Audits/K_MPC_0_05/`.

Nový audit patrí do `AUDIT_THREADS` vlastníckej koľaje, ak ide o
viackolovú diskusiu. Starý audit sa pri námietke neprepisuje; vznikne nové
kolo alebo scope-limiting rozhodnutie.
