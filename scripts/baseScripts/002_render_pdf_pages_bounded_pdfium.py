"""Render selected one-based PDF pages with pypdfium2 and a deadline.

This supersedes the quarantined fitz-only script 001 in this runtime. Keep an
outer process timeout because a parser can block before cooperative checks run.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import pypdfium2 as pdfium


def parse_pages(value: str) -> list[int]:
    pages = sorted({int(item.strip()) for item in value.split(",") if item.strip()})
    if not pages or pages[0] < 1:
        raise argparse.ArgumentTypeError("pages must be positive one-based integers")
    return pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--pages", required=True, type=parse_pages)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--dpi", type=float, default=144.0)
    parser.add_argument("--max-runtime-seconds", type=float, default=45.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.dpi <= 0 or args.max_runtime_seconds <= 0:
        raise ValueError("dpi and max runtime must be positive")

    started = time.monotonic()
    input_path = args.input.resolve(strict=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    document = pdfium.PdfDocument(input_path)
    outputs: list[str] = []

    try:
        for page_number in args.pages:
            if time.monotonic() - started > args.max_runtime_seconds:
                raise TimeoutError("cooperative PDF render deadline exceeded")
            if page_number > len(document):
                raise IndexError(
                    f"page {page_number} exceeds document length {len(document)}"
                )
            page = document[page_number - 1]
            output = args.output_dir / f"{input_path.stem}_page_{page_number:03d}.png"
            try:
                page.render(scale=args.dpi / 72.0).to_pil().save(output)
            finally:
                page.close()
            outputs.append(str(output.resolve()))
    finally:
        document.close()

    print(
        json.dumps(
            {
                "status": "PASS",
                "backend": "pypdfium2",
                "input": str(input_path),
                "pages": args.pages,
                "outputs": outputs,
                "runtime_seconds": time.monotonic() - started,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
