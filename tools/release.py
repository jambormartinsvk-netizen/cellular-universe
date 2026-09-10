#!/usr/bin/env python3
"""Export a clean public Git commit for review. No upload, tag or release approval."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
import zipfile

from audit import AuditError, cleanup_owned, new_output, reject_links, relative_path

MAX_FILE_BYTES = 50 * 1024 * 1024
REPOSITORY = "github.com/jambormartinsvk-netizen/cellular-universe"
ALLOWED_REMOTE_URLS = {
    f"https://{REPOSITORY}", f"https://{REPOSITORY}.git",
    f"git@{REPOSITORY.replace('/', ':', 1)}", f"git@{REPOSITORY.replace('/', ':', 1)}.git",
    f"ssh://git@{REPOSITORY}", f"ssh://git@{REPOSITORY}.git",
}
MANIFEST = "RELEASE_STAGING_MANIFEST.tsv"


def _git(root, deadline, *args, input_bytes=None):
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise AuditError("Git operation exceeded the 60-second budget")
    result = subprocess.run(["git", "-C", str(root), *args], input=input_bytes,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=remaining, check=False)
    if result.returncode:
        raise AuditError(f"Git command failed: {args[0]}")
    return result.stdout


def public_path(path):
    parts = relative_path(path).parts
    forbidden = {".git", ".agents", ".codex", ".backups", ".publication", ".ssh",
                 "working", "workspace", "secrets", "credentials", "__pycache__", ".venv", "venv"}
    if any(p.casefold() in forbidden for p in parts):
        raise AuditError(f"Non-public directory in Git tree: {path}")
    if parts[0].casefold() in {"tracks", "scripts", "work", "scratch"}:
        raise AuditError(f"Working corpus at repository root: {path}")
    name = parts[-1].casefold()
    if (name == ".env" or name.startswith(".env.") or name in {
            "id_rsa", "id_ed25519", "credentials.json", "credentials.toml", "token", "tokens"}
            or name.endswith((".pem", ".key", ".p12", ".pfx"))):
        raise AuditError(f"Potential secret file in Git tree: {path}")
    return path


def snapshot(root):
    deadline = time.monotonic() + 60
    if Path(_git(root, deadline, "rev-parse", "--show-toplevel").decode().strip()).resolve() != root.resolve():
        raise AuditError("--root must be the public repository root")
    branch = _git(root, deadline, "symbolic-ref", "--short", "HEAD").decode().strip()
    if branch not in {"main", "codex/publication"}:
        raise AuditError("Expected main or codex/publication branch")
    remote = _git(root, deadline, "remote", "get-url", "origin").decode().strip()
    if remote not in ALLOWED_REMOTE_URLS:
        raise AuditError("Origin is not the intended public GitHub repository")
    commit = _git(root, deadline, "rev-parse", "HEAD").decode().strip()
    if _git(root, deadline, "status", "--porcelain=v1", "--untracked-files=all"):
        raise AuditError("Public Git working tree/index is not clean")
    raw_tree = _git(root, deadline, "ls-tree", "-rlz", "--full-tree", commit)
    records, names = [], set()
    for raw in raw_tree.split(b"\0"):
        if not raw:
            continue
        header, path_bytes = raw.split(b"\t", 1)
        mode, kind, oid, size = header.decode("ascii").split()
        path = public_path(path_bytes.decode("utf-8"))
        if path.casefold() in names:
            raise AuditError(f"Colliding Git paths: {path}")
        names.add(path.casefold())
        if mode not in {"100644", "100755"} or kind != "blob":
            raise AuditError(f"Only regular tracked files may be exported: {path}")
        if int(size) > MAX_FILE_BYTES:
            raise AuditError(f"Tracked file exceeds 50 MiB: {path}")
        records.append((path, oid, int(size), mode))
    if not records:
        raise AuditError("Empty public Git tree")
    raw_blobs = _git(root, deadline, "cat-file", "--batch",
                     input_bytes=("\n".join(r[1] for r in records) + "\n").encode("ascii"))
    stream, files = io.BytesIO(raw_blobs), {}
    for path, oid, size, mode in records:
        header = stream.readline().decode("ascii").strip().split()
        if header != [oid, "blob", str(size)]:
            raise AuditError(f"Unexpected Git blob response: {path}")
        data = stream.read(size)
        if len(data) != size or stream.read(1) != b"\n":
            raise AuditError("Truncated Git blob stream")
        if re.search(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", data):
            raise AuditError(f"Private key content in tracked file: {path}")
        files[path] = {"data": data, "mode": mode, "sha256": hashlib.sha256(data).hexdigest(), "bytes": size}
    if stream.read():
        raise AuditError("Trailing Git blob data")
    if _git(root, deadline, "rev-parse", "HEAD").decode().strip() != commit or _git(
            root, deadline, "status", "--porcelain=v1", "--untracked-files=all"):
        raise AuditError("Repository changed during snapshot")
    return {"commit": commit, "branch": branch, "origin": remote, "files": files}


def zenodo_members(files):
    if MANIFEST not in files:
        raise AuditError(f"Missing {MANIFEST} in commit")
    reader = csv.DictReader(io.StringIO(files[MANIFEST]["data"].decode("utf-8-sig")), delimiter="\t")
    required = {"release_path", "zenodo_filename", "bytes", "sha256", "zenodo_payload"}
    if not required.issubset(reader.fieldnames or []):
        raise AuditError("Invalid release staging manifest columns")
    members, names, source_names = [], set(), set()
    for row in reader:
        if row.get("zenodo_payload") != "yes":
            continue
        path = public_path(row.get("release_path"))
        name = relative_path(row.get("zenodo_filename"))
        if len(name.parts) != 1:
            raise AuditError("Zenodo filenames must be flat")
        name = name.as_posix()
        if name.casefold() in names or path.casefold() in source_names:
            raise AuditError("Duplicate Zenodo filename or source")
        names.add(name.casefold())
        source_names.add(path.casefold())
        if path not in files:
            raise AuditError(f"Manifest source absent from Git commit: {path}")
        entry = files[path]
        self_entry = (path in {MANIFEST, "MANIFEST.sha256"} and
                      row.get("bytes") == "SELF" and row.get("sha256") == "SELF_EXCLUDED")
        if not self_entry:
            try:
                matches = int(row["bytes"]) == entry["bytes"] and row["sha256"].lower() == entry["sha256"]
            except (TypeError, ValueError):
                matches = False
            if not matches:
                raise AuditError(f"Manifest bytes/hash do not match committed source: {path}")
        members.append((name, path))
    if not members:
        raise AuditError("No Zenodo payload entries")
    return members


def write_zip(path, members, files):
    with zipfile.ZipFile(path, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, source in sorted(members):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = int(files[source]["mode"], 8) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[source]["data"])
    with zipfile.ZipFile(path) as archive:
        if set(archive.namelist()) != {name for name, _ in members}:
            raise AuditError("Archive member mismatch")
        for name, source in members:
            if archive.read(name) != files[source]["data"]:
                raise AuditError(f"Archive round-trip mismatch: {name}")
    return {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size, "file_count": len(members),
            "files": [{"path": name, "source_path": source, "sha256": files[source]["sha256"],
                       "bytes": files[source]["bytes"]} for name, source in sorted(members)]}


def export(root, output):
    root = reject_links(Path(root))
    output = new_output(root, output)
    data = snapshot(root)
    files = data.pop("files")
    zenodo = zenodo_members(files)
    temporary = Path(tempfile.mkdtemp(prefix=".qcts-release-", dir=output.parent))
    try:
        archives = [write_zip(temporary / "github-source.zip", [(p, p) for p in files], files),
                    write_zip(temporary / "zenodo-upload.zip", zenodo, files)]
        manifest = {"schema_version": 1, "status": "STAGING_ONLY", "source": data,
                    "science_verdict": "NOT_ASSESSED", "publication_authorized": False,
                    "archives": archives,
                    "note": "Exact committed bytes. Review before any upload. Historical release manifests are preserved."}
        (temporary / "export_manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        new_output(root, output)
        temporary.rename(output)
    except BaseException:
        if temporary.exists():
            cleanup_owned(temporary, output.parent, ".qcts-release-")
        raise
    return {"status": "STAGING_ONLY", "commit": data["commit"], "output": str(output),
            "github_files": len(files), "zenodo_files": len(zenodo), "publication_authorized": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(export(args.root, args.output), indent=2))
        return 0
    except (AuditError, OSError, ValueError, subprocess.TimeoutExpired) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
