# Reproducing and auditing published results

Start from this preparation branch:

```sh
git clone --branch codex/publication https://github.com/jambormartinsvk-netizen/cellular-universe.git qcts-audit
cd qcts-audit
python tools/audit.py list
python tools/audit.py verify
```

The helper requires Python 3.11 or newer and uses only the standard library. Verification checks file identity, not scientific correctness. It never runs the scientific scripts.

| Case | What is available | Main limitation |
|---|---|---|
| EA004 | Background universality, normalization and comparison; runners 224/234/235, bases, reference JSON | Conditional historical models. Runner 224 requires SymPy; its exact original version was not recorded. The expected official exit code is 1 with the specified JSON, not a generic tool failure. |
| EA029 | C2 aggregate, runner 371, base, ten inputs and reference output | Coverage of stated logical obligations is not an existence proof for a physical model. Standard-library-only imports. |
| EA039 | C3 aggregate, runner 392, base, JSON and authority inputs, reference output | Same scope limitation; 45 logical entries do not certify a compatible model. Standard-library-only imports. |
| EA047 | Three-point legacy sensitivity, runner 393, base and staged reference raw | Conditional diagnostics, not a likelihood or confirmation. Use the primary commands together with the R2 parity correction. |

[audit_catalog.json](audit_catalog.json) contains the exact files, SHA-256 values, source guides and preparation paths. Existing [packages](External_Audits/PACKAGES) retain their original bytes. The catalog includes control revisions of EA047 as one case; they are not independent scientific confirmations. Historical scripts under HISTORY are evidence, not an automatic run queue.

## Prepare a clean run

Choose an **absolute, nonexistent directory outside this repository**:

```sh
python tools/audit.py prepare --case EA029 --output /absolute/new/location/ea029
```

On Windows, for example, use C:/audit-runs/ea029. The tool verifies the catalog, copies the complete declared REPRO tree and prints the working directory and commands. Run those commands yourself only after reading the linked package guide. All sources and accepted raw remain in the repository; your outputs belong in the new copy.

For EA004, commands printed by the helper use paths relative to the copied REPRO root. The original guide uses REPRO/ prefixes from its package root. This is a working-directory translation; no script or scientific parameter is changed. Run 234 before 235 and use the fresh 234 output. Do not interpret exit codes without the guide.

For EA047, the recorded environment is CPython 3.11.3, NumPy 2.4.4 and SciPy 1.17.1; requirements-audit.txt records the two package versions. Use a separate virtual environment for a numerical reproduction. EA004 needs a separately installed SymPy and a report of its actual version; no missing historical version has been invented.

Follow the full primary guide for EA047's hash-linked stages. R2 specifies how fresh-chain integrity and comparison with historical outputs differ: never substitute historical hashes for fresh provenance. Preserve every physical value, threshold and field required by that guide.

## What to report

Keep the commit ID, Python and dependency versions, command, exit code, elapsed time, source/input/output hashes and all unexpected differences. A hash match alone is not an independent check of the equations. A matching aggregate is not a new proof that QCTS exists. This infrastructure setup did not rerun the historical science.

Submit a scoped positive, negative or inconclusive audit using [CONTRIBUTING.md](CONTRIBUTING.md). LLM reviews must name the model and remain model reviews. No result here is promoted to final human verification by these tools.

## Exporting a future release

Maintainers can export a clean publication commit with:

```sh
python tools/release.py --root . --output /absolute/new/location/release-export
```

It produces a public-source ZIP, the flat Zenodo attachment ZIP selected by RELEASE_STAGING_MANIFEST.tsv, and an exact export manifest. It does not publish a DOI, push, tag or approve scientific claims. The current historical selection contains 13 files; older embedded staging metadata saying 14 is preserved as history. This branch prepares access and maintenance around v3.18, not a new scientific version.
