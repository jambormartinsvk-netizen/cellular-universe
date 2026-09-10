"""Offline synthetic tests only: no scientific runner is imported or executed."""
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock
import zipfile

import audit
import release


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "public"
        self.root.mkdir()
        self.contents = {"pkg/guide.md": b"Fixture guide\n",
                         "pkg/REPRO/scripts/never_run.py": b"raise RuntimeError('must not execute')\n",
                         "pkg/REPRO/raw.json": b'{"synthetic": true}\r\n'}
        for path, value in self.contents.items():
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(value)
        self.catalog = {"schema_version": 1, "cases": [{
            "id": "fixture", "title": "Synthetic fixture", "package_path": "pkg",
            "guide_path": "pkg/guide.md", "prepare_source": "pkg/REPRO",
            "commands": ["python scripts/never_run.py"],
            "limitations": "Synthetic control fixture; no physical claim.",
            "files": [{"path": p, "sha256": hashlib.sha256(v).hexdigest(), "bytes": len(v)}
                      for p, v in self.contents.items()]}]}
        self.save()

    def save(self):
        (self.root / "audit_catalog.json").write_text(json.dumps(self.catalog), encoding="utf-8")

    def test_cleanup_refuses_a_different_parent(self):
        other = self.base / ".qcts-prepare-foreign"
        other.mkdir()
        marker = other / "keep.txt"
        marker.write_text("keep", encoding="utf-8")
        with self.assertRaises(audit.AuditError):
            audit.cleanup_owned(other, self.root, ".qcts-prepare-")
        self.assertEqual(marker.read_text(encoding="utf-8"), "keep")

    def test_verified_prepare_exact_bytes_and_no_execution(self):
        loaded = audit.load_catalog(self.root)
        verified = audit.verify(self.root, loaded)
        self.assertEqual(verified["status"], "BYTES_VERIFIED_ONLY")
        output = self.base / "isolated"
        result = audit.prepare(self.root, loaded, "fixture", output)
        self.assertEqual(result["status"], "PREPARED_NOT_EXECUTED")
        self.assertEqual(result["science_verdict"], "NOT_ASSESSED")
        self.assertEqual((output / "raw.json").read_bytes(), self.contents["pkg/REPRO/raw.json"])
        self.assertEqual({p.relative_to(output).as_posix() for p in output.rglob("*") if p.is_file()},
                         {"scripts/never_run.py", "raw.json"})

    def test_tamper_and_missing_file_fail_without_output(self):
        source = self.root / "pkg/REPRO/raw.json"
        source.write_bytes(b"corrupt")
        with self.assertRaises(audit.AuditError):
            audit.prepare(self.root, self.catalog, "fixture", self.base / "isolated")
        self.assertFalse((self.base / "isolated").exists())
        source.unlink()
        with self.assertRaises(audit.AuditError):
            audit.verify(self.root, self.catalog)

    def test_extra_prepare_file_rejected(self):
        (self.root / "pkg/REPRO/untracked.py").write_text("raise Exception()", encoding="utf-8")
        with self.assertRaisesRegex(audit.AuditError, "inventory mismatch"):
            audit.prepare(self.root, self.catalog, "fixture", self.base / "isolated")
        self.assertFalse((self.base / "isolated").exists())

    def test_related_package_tamper_missing_and_overlap_are_rejected(self):
        case = self.catalog["cases"][0]
        case["related_packages"] = ["control-r1"]
        related = self.root / "control-r1/decision.md"
        related.parent.mkdir()
        payload = b"Synthetic supplementary control correction\n"
        related.write_bytes(payload)
        case["files"].append({"path": "control-r1/decision.md", "bytes": len(payload),
                              "sha256": hashlib.sha256(payload).hexdigest()})
        self.save()
        catalog = audit.load_catalog(self.root)
        self.assertEqual(audit.verify(self.root, catalog)["cases"][0]["files"], 4)
        output = self.base / "isolated"
        audit.prepare(self.root, catalog, "fixture", output)
        self.assertFalse((output / "decision.md").exists())
        related.write_bytes(b"tampered")
        with self.assertRaisesRegex(audit.AuditError, "mismatch"):
            audit.verify(self.root, catalog)
        related.unlink()
        with self.assertRaisesRegex(audit.AuditError, "inventory mismatch"):
            audit.verify(self.root, catalog)
        case["related_packages"] = ["pkg/REPRO"]
        self.save()
        with self.assertRaisesRegex(audit.AuditError, "overlapping"):
            audit.load_catalog(self.root)

    def test_absent_output_and_outside_repo_guards(self):
        outside = self.base / "existing"
        outside.mkdir()
        (outside / "untouched.txt").write_bytes(b"keep")
        for output in (outside, self.root / "new", Path("relative")):
            with self.subTest(output=output), self.assertRaises(audit.AuditError):
                audit.prepare(self.root, self.catalog, "fixture", output)
        self.assertEqual((outside / "untouched.txt").read_bytes(), b"keep")

    def test_schema_requires_hash_bytes_and_unique_ids_paths(self):
        original = copy.deepcopy(self.catalog)
        mutations = [lambda c: c["cases"].append(copy.deepcopy(c["cases"][0])),
                     lambda c: c["cases"][0]["files"].append(copy.deepcopy(c["cases"][0]["files"][0])),
                     lambda c: c["cases"][0]["files"][0].pop("sha256"),
                     lambda c: c["cases"][0]["files"][0].pop("bytes"),
                     lambda c: c["cases"][0].update(prepare_source="other/REPRO")]
        for mutate in mutations:
            self.catalog = copy.deepcopy(original)
            mutate(self.catalog)
            self.save()
            with self.assertRaises(audit.AuditError):
                audit.load_catalog(self.root)

    def test_unsafe_relative_paths_and_duplicate_json_keys(self):
        for value in ("../escape", "/absolute", "C:/absolute", "pkg\\file", "pkg/./file", "pkg//file"):
            with self.subTest(value=value), self.assertRaises(audit.AuditError):
                audit.relative_path(value)
        (self.root / "audit_catalog.json").write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
        with self.assertRaisesRegex(audit.AuditError, "Duplicate JSON"):
            audit.load_catalog(self.root)

    def test_symlink_escape_rejected(self):
        target = self.base / "elsewhere"
        target.mkdir()
        link = self.root / "linked"
        try:
            link.symlink_to(target, target_is_directory=True)
        except OSError:
            self.skipTest("Platform does not allow test symlinks")
        with self.assertRaises(audit.AuditError):
            audit.within(self.root, "linked/file")

    def test_copy_failure_does_not_publish_partial_directory(self):
        with mock.patch.object(audit, "check_bytes", side_effect=[None, None, None, audit.AuditError("changed after verification")]):
            with self.assertRaises(audit.AuditError):
                audit.prepare(self.root, self.catalog, "fixture", self.base / "isolated")
        self.assertFalse((self.base / "isolated").exists())
        self.assertEqual(list(self.base.glob(".qcts-prepare-*")), [])

    def test_cli_returns_nonzero_for_unknown_case(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(audit.main(["--root", str(self.root), "verify", "--case", "missing"]), 2)


@unittest.skipUnless(shutil.which("git"), "Git is required for export fixtures")
class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "public"
        self.root.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Synthetic fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "commit.gpgsign", "false")
        self.git("remote", "add", "origin", "https://github.com/jambormartinsvk-netizen/cellular-universe.git")
        self.payload = b"Synthetic line one\nline two\n"
        (self.root / "theory").mkdir()
        (self.root / "theory/paper.md").write_bytes(self.payload)
        (self.root / "README.md").write_bytes(b"Synthetic public fixture\n")
        self.manifest = ("release_path\tzenodo_filename\tbytes\tsha256\tzenodo_payload\n"
                         f"theory/paper.md\tpaper.md\t{len(self.payload)}\t{hashlib.sha256(self.payload).hexdigest()}\tyes\n"
                         "RELEASE_STAGING_MANIFEST.tsv\tRELEASE_STAGING_MANIFEST.tsv\tSELF\tSELF_EXCLUDED\tyes\n"
                         "#META\told_count\t14\tNA\tno\n").encode()
        (self.root / release.MANIFEST).write_bytes(self.manifest)
        self.commit()

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, timeout=10, check=True).stdout

    def commit(self):
        self.git("add", "--all")
        self.git("commit", "-m", "Synthetic fixture")

    def test_export_round_trip_uses_git_blob_bytes_preserves_manifest(self):
        self.git("config", "core.autocrlf", "true")
        (self.root / ".gitattributes").write_bytes(b"theory/paper.md text eol=crlf\n")
        self.commit()
        (self.root / "theory/paper.md").unlink()
        self.git("checkout", "--", "theory/paper.md")
        self.assertEqual((self.root / "theory/paper.md").read_bytes(), self.payload.replace(b"\n", b"\r\n"))
        self.assertEqual(self.git("status", "--porcelain"), b"")
        output = self.base / "export"
        result = release.export(self.root, output)
        self.assertEqual(result["status"], "STAGING_ONLY")
        self.assertFalse(result["publication_authorized"])
        manifest = json.loads((output / "export_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["source"]["commit"], self.git("rev-parse", "HEAD").decode().strip())
        for record in manifest["archives"]:
            self.assertEqual(hashlib.sha256((output / record["path"]).read_bytes()).hexdigest(), record["sha256"])
        with zipfile.ZipFile(output / "github-source.zip") as archive:
            self.assertEqual(archive.read("theory/paper.md"), self.payload)
            self.assertEqual(archive.read(release.MANIFEST), self.manifest)
            self.assertFalse(any(".git/" in n for n in archive.namelist()))
        with zipfile.ZipFile(output / "zenodo-upload.zip") as archive:
            self.assertEqual(set(archive.namelist()), {"paper.md", release.MANIFEST})
            self.assertEqual(archive.read("paper.md"), self.payload)

    def test_dirty_git_untracked_and_modified_fail(self):
        path = self.root / "new.txt"
        path.write_bytes(b"untracked")
        with self.assertRaisesRegex(audit.AuditError, "not clean"):
            release.export(self.root, self.base / "out")
        path.unlink()
        (self.root / "README.md").write_bytes(b"modified")
        with self.assertRaisesRegex(audit.AuditError, "not clean"):
            release.export(self.root, self.base / "out")
        self.assertFalse((self.base / "out").exists())

    def test_wrong_remote_and_branch_fail(self):
        self.git("remote", "set-url", "origin", "https://example.invalid/other.git")
        with self.assertRaisesRegex(audit.AuditError, "Origin"):
            release.export(self.root, self.base / "out")
        self.git("remote", "set-url", "origin", "https://github.com/jambormartinsvk-netizen/cellular-universe")
        self.git("switch", "-c", "codex/research")
        with self.assertRaisesRegex(audit.AuditError, "branch"):
            release.export(self.root, self.base / "out")

    def test_output_guard_preserves_existing_and_rejects_inside_repository(self):
        output = self.base / "out"
        output.mkdir()
        (output / "keep").write_bytes(b"keep")
        for target in (output, self.root / "new"):
            with self.assertRaises(audit.AuditError):
                release.export(self.root, target)
        self.assertEqual((output / "keep").read_bytes(), b"keep")

    def test_manifest_tamper_missing_source_and_nonflat_name(self):
        files = release.snapshot(self.root)["files"]
        for invalid in (self.manifest.replace(b"paper.md\t27\t", b"paper.md\t99\t"),
                        self.manifest.replace(b"theory/paper.md", b"missing.md"),
                        self.manifest.replace(b"\tpaper.md\t", b"\tfolder/paper.md\t")):
            if invalid == self.manifest:
                invalid = self.manifest.replace(hashlib.sha256(self.payload).hexdigest().encode(), b"0" * 64)
            changed = copy.deepcopy(files)
            changed[release.MANIFEST]["data"] = invalid
            with self.assertRaises(audit.AuditError):
                release.zenodo_members(changed)

    def test_secret_and_working_paths_and_oversized_blobs_fail(self):
        for path in (".env", "nested/.git/config", "tracks/00_STATE.json", "working/draft.md", "id_rsa"):
            with self.subTest(path=path), self.assertRaises(audit.AuditError):
                release.public_path(path)
        with mock.patch.object(release, "MAX_FILE_BYTES", 5):
            with self.assertRaisesRegex(audit.AuditError, "50 MiB"):
                release.export(self.root, self.base / "out")
        (self.root / "harmless.txt").write_bytes(b"-----BEGIN " + b"PRIVATE KEY-----\nfixture")
        self.commit()
        with self.assertRaisesRegex(audit.AuditError, "Private key"):
            release.export(self.root, self.base / "out")

    def test_failed_archive_write_does_not_publish(self):
        with mock.patch.object(release, "write_zip", side_effect=OSError("synthetic disk failure")):
            with self.assertRaises(OSError):
                release.export(self.root, self.base / "out")
        self.assertFalse((self.base / "out").exists())
        self.assertEqual(list(self.base.glob(".qcts-release-*")), [])


if __name__ == "__main__":
    unittest.main()
