#!/usr/bin/env python3
"""Verify catalogued bytes and prepare an isolated copy; never execute science."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import sys
import tempfile


class AuditError(ValueError):
    pass


def relative_path(value):
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise AuditError(f"Unsafe relative path: {value!r}")
    parts = value.split("/")
    if any(p in ("", ".", "..") or p.endswith((" ", ".")) for p in parts):
        raise AuditError(f"Unsafe relative path: {value!r}")
    if any(ord(c) < 32 or c in '<>"|?*' for c in value):
        raise AuditError("Unsafe character in path")
    reserved = {"con", "prn", "aux", "nul"} | {f"{kind}{i}" for kind in ("com", "lpt") for i in range(1, 10)}
    if any(p.split(".")[0].casefold() in reserved for p in parts):
        raise AuditError("Reserved device name in path")
    return PurePosixPath(value)


def reject_links(path):
    """Reject symlinks and Windows junction/reparse points in every ancestor."""
    path = Path(os.path.abspath(path))
    for candidate in (*reversed(path.parents), path):
        try:
            info = candidate.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise AuditError(f"Symlink/reparse point is not allowed: {candidate}")
    return path


def within(root, value):
    rel = relative_path(value)
    path = reject_links(root.joinpath(*rel.parts))
    if not path.resolve().is_relative_to(root.resolve()):
        raise AuditError(f"Path escapes repository: {value}")
    return path


def new_output(root, output):
    output = Path(output)
    if not output.is_absolute():
        raise AuditError("Output must be an absolute path")
    output = reject_links(output)
    if output.exists():
        raise AuditError(f"Output already exists: {output}")
    if output.resolve().is_relative_to(root.resolve()):
        raise AuditError("Output must be outside the source repository")
    if not output.parent.is_dir():
        raise AuditError("Output parent must already exist")
    return output


def cleanup_owned(temporary, parent, prefix):
    temporary, parent = Path(temporary), Path(parent)
    reject_links(temporary)
    if (not temporary.is_absolute() or not temporary.name.startswith(prefix)
            or temporary.resolve().parent != parent.resolve()):
        raise AuditError("Temporary cleanup ownership check failed")
    shutil.rmtree(temporary)


def _no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise AuditError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def package_roots(case):
    related = case.get("related_packages", [])
    if not isinstance(related, list):
        raise AuditError("related_packages must be a list")
    return [relative_path(p) for p in [case.get("package_path"), *related]]


def load_catalog(root):
    root = reject_links(Path(root))
    catalog = json.loads(within(root, "audit_catalog.json").read_text(encoding="utf-8-sig"),
                         object_pairs_hook=_no_duplicate_keys)
    if not isinstance(catalog, dict) or catalog.get("schema_version") != 1:
        raise AuditError("Expected audit catalog schema_version 1")
    cases = catalog.get("cases")
    if not isinstance(cases, list) or not cases:
        raise AuditError("Catalog cases must be a nonempty list")
    ids, packages, all_names = set(), set(), set()
    for case in cases:
        if not isinstance(case, dict):
            raise AuditError("Invalid case")
        cid = case.get("id")
        if not isinstance(cid, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", cid):
            raise AuditError("Invalid case ID")
        if cid.casefold() in ids:
            raise AuditError(f"Duplicate case ID: {cid}")
        ids.add(cid.casefold())
        for field in ("title", "limitations"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                raise AuditError(f"Missing {field}: {cid}")
        roots = package_roots(case)
        package = roots[0]
        source = relative_path(case.get("prepare_source"))
        relative_path(case.get("guide_path"))
        for package_root in roots:
            name = package_root.as_posix().casefold()
            if any(name == p or name.startswith(p + "/") or p.startswith(name + "/") for p in packages):
                raise AuditError(f"Duplicate or overlapping package roots: {package_root}")
            packages.add(name)
        if not source.is_relative_to(package) or source == package:
            raise AuditError("prepare_source must be inside the package")
        commands = case.get("commands")
        if not isinstance(commands, list) or not commands or any(
                not isinstance(c, str) or not c.strip() for c in commands):
            raise AuditError(f"Missing commands: {cid}")
        files = case.get("files")
        if not isinstance(files, list) or not files:
            raise AuditError(f"Missing file manifest: {cid}")
        names = set()
        for item in files:
            if not isinstance(item, dict):
                raise AuditError("Invalid file entry")
            path = relative_path(item.get("path"))
            if not any(path.is_relative_to(p) and path != p for p in roots):
                raise AuditError(f"File outside package: {path}")
            if path.as_posix().casefold() in names or path.as_posix().casefold() in all_names:
                raise AuditError(f"Duplicate file path: {path}")
            names.add(path.as_posix().casefold())
            all_names.add(path.as_posix().casefold())
            if type(item.get("bytes")) is not int or item["bytes"] < 0:
                raise AuditError(f"Missing/invalid byte count: {path}")
            if not isinstance(item.get("sha256"), str) or not re.fullmatch(
                    r"[a-fA-F0-9]{64}", item["sha256"]):
                raise AuditError(f"Missing/invalid SHA-256: {path}")
    return catalog


def selected_cases(catalog, case_id=None):
    cases = catalog["cases"]
    if case_id is None:
        return cases
    selected = [c for c in cases if c["id"] == case_id]
    if not selected:
        raise AuditError(f"Unknown case: {case_id}")
    return selected


def check_bytes(data, item):
    if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"].lower():
        raise AuditError(f"Byte/hash mismatch: {item['path']}")


def _package_files(root, package):
    directory = within(root, package)
    if not directory.is_dir():
        raise AuditError(f"Missing package directory: {package}")
    found = set()
    for parent, dirs, files in os.walk(directory, followlinks=False):
        for name in dirs + files:
            path = reject_links(Path(parent) / name)
            if name in files:
                if not path.is_file():
                    raise AuditError(f"Not a regular file: {path}")
                found.add(path.relative_to(root).as_posix())
    return found


def verify(root, catalog, case_id=None):
    root = reject_links(Path(root))
    verified = []
    for case in selected_cases(catalog, case_id):
        expected = {f["path"] for f in case["files"]}
        actual = set()
        for package_root in package_roots(case):
            actual.update(_package_files(root, package_root.as_posix()))
        if expected != actual:
            missing, extra = sorted(expected - actual), sorted(actual - expected)
            raise AuditError(f"Package inventory mismatch ({case['id']}): missing={missing}, extra={extra}")
        if case["guide_path"] not in expected:
            raise AuditError("Reproduction guide must be covered by the package manifest")
        if not within(root, case["prepare_source"]).is_dir():
            raise AuditError("Missing preparation source directory")
        for item in case["files"]:
            path = within(root, item["path"])
            if not path.is_file():
                raise AuditError(f"Missing regular file: {item['path']}")
            check_bytes(path.read_bytes(), item)
        verified.append({"id": case["id"], "files": len(expected),
                         "bytes": sum(f["bytes"] for f in case["files"])})
    return {"status": "BYTES_VERIFIED_ONLY", "cases": verified,
            "science_verdict": "NOT_ASSESSED"}


def prepare(root, catalog, case_id, output):
    root = reject_links(Path(root))
    output = new_output(root, output)
    verify(root, catalog, case_id)
    case = selected_cases(catalog, case_id)[0]
    prefix = PurePosixPath(case["prepare_source"])
    selected = [f for f in case["files"] if PurePosixPath(f["path"]).is_relative_to(prefix)]
    if not selected:
        raise AuditError("No manifest-covered preparation files")
    # Only this tool's fresh staging directory is cleaned up after a failure.
    temporary = Path(tempfile.mkdtemp(prefix=".qcts-prepare-", dir=output.parent))
    try:
        for item in selected:
            relative = PurePosixPath(item["path"]).relative_to(prefix)
            target = temporary.joinpath(*relative.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            data = within(root, item["path"]).read_bytes()
            check_bytes(data, item)
            with target.open("xb") as stream:
                stream.write(data)
            check_bytes(target.read_bytes(), item)
        new_output(root, output)
        temporary.rename(output)
    except BaseException:
        if temporary.exists():
            cleanup_owned(temporary, output.parent, ".qcts-prepare-")
        raise
    return {"status": "PREPARED_NOT_EXECUTED", "case": case_id,
            "working_directory": str(output), "files": len(selected),
            "commands_to_review_and_run_yourself": case["commands"],
            "limitations": case["limitations"], "science_verdict": "NOT_ASSESSED"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    verify_parser = commands.add_parser("verify")
    verify_parser.add_argument("--case")
    prepare_parser = commands.add_parser("prepare")
    prepare_parser.add_argument("--case", required=True)
    prepare_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        root = reject_links(args.root)
        catalog = load_catalog(root)
        if args.command == "list":
            result = [{k: c[k] for k in ("id", "title", "guide_path", "limitations")}
                      for c in catalog["cases"]]
        elif args.command == "verify":
            result = verify(root, catalog, args.case)
        else:
            result = prepare(root, catalog, args.case, args.output)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (AuditError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
