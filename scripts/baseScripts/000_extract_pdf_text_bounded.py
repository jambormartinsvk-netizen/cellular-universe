"""Bounded, reusable PDF-to-text extractor for audit source material.

This helper performs no scientific calculation. It preserves page boundaries so
that later audits can map extracted claims back to the original PDF pages.
An outer process timeout is still required because a damaged PDF can block
inside a third-party parser before the cooperative deadline check runs.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from pypdf import PdfReader


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_runtime_seconds <= 0:
        raise ValueError("--max-runtime-seconds must be positive")

    started = time.monotonic()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, object]] = []

    for input_path in args.inputs:
        if time.monotonic() - started > args.max_runtime_seconds:
            raise TimeoutError("cooperative PDF extraction deadline exceeded")
        input_path = input_path.resolve(strict=True)
        reader = PdfReader(str(input_path))
        chunks: list[str] = []
        for page_number, page in enumerate(reader.pages, start=1):
            if time.monotonic() - started > args.max_runtime_seconds:
                raise TimeoutError("cooperative PDF extraction deadline exceeded")
            chunks.append(f"\n===== PDF PAGE {page_number} =====\n")
            chunks.append(page.extract_text() or "")

        output_path = args.output_dir / f"{input_path.stem}.txt"
        output_path.write_text("\n".join(chunks), encoding="utf-8")
        manifest.append(
            {
                "input": str(input_path),
                "output": str(output_path.resolve()),
                "pages": len(reader.pages),
                "characters": sum(len(chunk) for chunk in chunks),
            }
        )

    print(
        json.dumps(
            {
                "status": "PASS",
                "runtime_seconds": time.monotonic() - started,
                "files": manifest,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
