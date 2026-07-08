#!/usr/bin/env python3
"""Sanitize accidental literal newlines inside assembly .string quotes.

FireRed text files must contain escaped newlines like \n inside strings.
If a Python patch writes an actual line break inside a quoted .string, the
assembler fails with errors like:

    unexpected character U+A in UTF-8 string

This script repairs those cases after story patches run.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sanitize_text(text: str) -> tuple[str, int]:
    out: list[str] = []
    line_buf: list[str] = []
    in_string = False
    fixes = 0

    i = 0
    while i < len(text):
        ch = text[i]

        if ch == '"':
            if in_string:
                # End the current .string quote unless the quote is escaped.
                prev = out[-1] if out else ""
                if prev != "\\":
                    in_string = False
            else:
                # Only start quote tracking for assembly text directives.
                if ".string" in "".join(line_buf):
                    in_string = True
            out.append(ch)
            line_buf.append(ch)
            i += 1
            continue

        if ch == "\n":
            if in_string:
                # A real line break inside a .string is invalid for the assembler.
                # Convert it into the intended escaped newline.
                out.append("\\n")
                fixes += 1
            else:
                out.append(ch)
                line_buf.clear()
            i += 1
            continue

        out.append(ch)
        if not in_string:
            line_buf.append(ch)
            if len(line_buf) > 200:
                line_buf = line_buf[-200:]
        i += 1

    return "".join(out), fixes


def main() -> None:
    total_fixes = 0
    files_changed = 0

    for path in sorted((ROOT / "data").rglob("*.inc")):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"skipped non-utf8 file: {path.relative_to(ROOT)}")
            continue

        sanitized, fixes = sanitize_text(text)
        if fixes:
            path.write_text(sanitized, encoding="utf-8")
            total_fixes += fixes
            files_changed += 1
            print(f"sanitized {fixes} string newline(s): {path.relative_to(ROOT)}")

    print(f"Assembly string sanitizer complete: {total_fixes} fix(es) in {files_changed} file(s).")


if __name__ == "__main__":
    main()
