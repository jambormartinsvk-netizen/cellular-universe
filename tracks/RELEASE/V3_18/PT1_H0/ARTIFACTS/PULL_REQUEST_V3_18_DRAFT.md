# Návrh pull requestu — v3.18

**Stav:** `DRAFT_READY / NOT_SUBMITTED / WAITING_MARTIN_REVIEW`  
**Zdrojová vetva:** `codex/v3.18-release`  
**Cieľový repozitár:** `jambormartinsvk-netizen/cellular-universe`  
**Parent:** `e9e3579afdffc3c719f0beabb4ec33929cfb4d62`  
**Autor Git identity:** `jambormartinsvk-netizen <jambor.martin.svk@gmail.com>`

## Navrhovaný názov PR

```text
release: add the complete self-contained v3.18 reader edition
```

## Navrhované telo PR

### Summary

This pull request prepares Quantum Cellular Theory of Space v3.18 as a
complete, self-contained Slovak/English reader edition. It preserves the
published v3.17 bytes as optional history, adds exact release manifests, and
connects only materially supported equations to selected sealed external
audit packages.

### What changes

- replace the current reader surface with numbered SK/EN v3.18 documents:
  reader guide (`00`), standalone main document (`01`), prediction-status
  table (`02`), and methodology/question register Q1–Q34 (`03`);
- add a bilingual changelog, Zenodo description, staging manifest, and
  SHA-256 payload manifest;
- preserve the exact 16-file v3.17 snapshot under `HISTORY/v3.17/` and
  remove redundant old root/nested reader copies;
- add selected Git-only external-audit evidence under `External_Audits/`;
- link equations (17)–(22)/(30) to EA-004, equations (25)–(27) to EA-047,
  and the two halves of equation (38) to EA-029/EA-039 with explicit scope
  limits;
- preserve the complete EA-047 -> R1 -> R2 package-control history without
  representing R1/R2 as new scientific calculations;
- replace unresolved internal/future permalink placeholders by explicit
  “internal working evidence / no canonical external package” boundaries.

### Scientific and audit boundary

- No formula value, raw result, route verdict, score, or physical depth was
  changed by the PR-integration batch.
- `A2-K4` remains live at `60/100`; no A2 route has passed the complete
  perturbation station and A3/CLASS/CAMB remains blocked.
- A sealed package is not automatically a `PASS`.
- EA-029 is a sealed C2 aggregate capsule whose external response was not
  completed at the content cutoff.
- EA-004, EA-039, and EA-047 reached T2 only in their declared limited
  scopes. None of the included results reached T3 independent
  implementation.
- The 232-file `External_Audits/` tree is Git-only and is not part of the
  fixed 13-file Zenodo payload.

### Verification performed

- 13/13 staging-manifest payload rows and 12/12 non-self SHA-manifest rows;
- 264 Git-tree files excluding the worktree `.git` pointer;
- 231/231 source-to-Git SHA-256 checks for immutable audit copies;
- 40/40 SK/EN equation-tag parity;
- all relative Markdown links and all intended `v3.18` tag targets map to
  existing files in the prepared tree;
- no unresolved `scripts/`, `tracks/`, `Audit/`, or `Questions/` evidence
  placeholder remains in the two main documents;
- `.gitattributes` applies `-text` to the exact release and audit evidence;
- trailing-whitespace scan and `git diff --check` pass;
- independent math/formula-lineage audit: `RECOMMEND_RC_AUDIT_PASS`;
- independent documentation/release audit: no correction item.

### Reviewer checklist

- [ ] Read root `README.md` and both language `00` guides.
- [ ] Review SK `01` as semantic authority, then compare EN `01`.
- [ ] Review prediction rows P01–P11 in both `02` CSV files.
- [ ] Review methodology and Q1–Q34 in both `03` files.
- [ ] Check formula-adjacent external-audit links and their mandatory
      nonclaims.
- [ ] Confirm v3.17 files moved to `HISTORY/v3.17/` are byte preserved.
- [ ] Confirm the 13-file Zenodo boundary excludes `External_Audits/` and
      `HISTORY/`.
- [ ] Confirm no staged content exists before Martin Jambor's explicit
      approval.

### Publication state

This PR does not publish Zenodo v3.18, create the immutable `v3.18` tag, or
claim peer review. Tagging, GitHub merge/release, and Zenodo publication
remain separate approval-gated steps.

## Pred odoslaním PR

Po výslovnom schválení Martinom Jamborom:

1. stage presného current tree;
2. zopakovať staged-tree hash, link, `git diff --cached --check` a
   `.gitattributes` kontrolu;
3. commitnúť do `codex/v3.18-release`;
4. pushnúť vetvu na osobný remote;
5. otvoriť PR s textom vyššie;
6. tag `v3.18` vytvoriť až nad schváleným commitom, aby absolútne auditné
   odkazy začali smerovať na nemenný strom.
