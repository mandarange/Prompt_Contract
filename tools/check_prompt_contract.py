#!/usr/bin/env python3
"""Validate a Prompt Contract Development v6 markdown file."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "Goal": r"^##\s+1\.\s+Goal\b",
    "After": r"^##\s+2\.\s+After\b",
    "Scope": r"^##\s+3\.\s+Scope\b",
    "No": r"^##\s+4\.\s+No\b",
    "Proof": r"^##\s+5\.\s+Proof\b",
    "Taste": r"^##\s+6\.\s+Taste\b",
    "Decision Ledger": r"^##\s+Decision Ledger\b",
}

PROOF_PATTERNS = {
    "Claim": r"^###\s+Claim\b",
    "Evidence": r"^###\s+Evidence\b",
    "Gap": r"^###\s+Gap\b",
    "Confidence": r"^###\s+Confidence\b",
}

SENSITIVE_TERMS = (
    "secret",
    "token",
    "customer personal data",
    "payment data",
    "private key",
)

RISK_TERMS = (
    "auth",
    "payment",
    "privacy",
    "billing",
    "security",
    "migration",
    "infra",
)


def has(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE) is not None


def line_value(name: str, text: str) -> str | None:
    match = re.search(rf"^{re.escape(name)}:\s*(.+)$", text, flags=re.IGNORECASE | re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 tools/check_prompt_contract.py <contract.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for name, pattern in REQUIRED_PATTERNS.items():
        if not has(pattern, text):
            errors.append(f"Missing required section: {name}")

    mode = line_value("Mode", text)
    if mode is None:
        errors.append("Missing Mode metadata")
    elif mode.lower() not in {"fast", "standard", "guarded"}:
        template_modes = {"fast", "standard", "guarded"}
        mode_words = set(re.findall(r"[a-z]+", mode.lower()))
        if template_modes.issubset(mode_words):
            warnings.append("Mode is a template placeholder; choose exactly one mode in real contracts")
        else:
            errors.append("Mode must be Fast, Standard, or Guarded")

    for name, pattern in PROOF_PATTERNS.items():
        if not has(pattern, text):
            errors.append(f"Missing Proof Case subsection: {name}")

    if not has(r"Stop if:", text):
        errors.append("Missing Stop Conditions (`Stop if:`)")

    if not has(r"external input|logs?|issue text|user-generated|data, not instructions", text):
        warnings.append("Context Firewall language is weak or missing")

    for term in SENSITIVE_TERMS:
        if term not in text.lower():
            warnings.append(f"Proof redaction term missing: {term}")

    open_decisions = re.search(
        r"Open decisions:\s*(?P<body>.*?)(?:\n##|\Z)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if open_decisions:
        body = open_decisions.group("body")
        unresolved = [
            line
            for line in body.splitlines()
            if line.strip().startswith("-") and not line.strip().endswith(":")
        ]
        if unresolved:
            warnings.append("Open decisions appear unresolved; implementation should not start")

    no_section = re.search(
        r"^##\s+4\.\s+No\b(?P<body>.*?)(?:^##\s+5\.|\Z)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    no_body = no_section.group("body").lower() if no_section else ""
    if not any(term in no_body for term in RISK_TERMS):
        warnings.append("No/Stop Conditions do not mention common guarded-risk domains")

    if errors:
        verdict = "Red"
    elif warnings:
        verdict = "Yellow"
    else:
        verdict = "Green"

    print(f"Verdict: {verdict}")
    if mode:
        print(f"Mode: {mode}")
    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"- {item}")
    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"- {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
