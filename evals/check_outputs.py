#!/usr/bin/env python3
"""Lightweight structural checks for saved skill outputs.

These don't judge quality — they catch the mechanical failures that matter
most: illegal verdict labels, incomplete handoffs, equations that don't appear
in the pasted Methods.

Usage:
  python3 check_outputs.py triage    OUTPUT.md
  python3 check_outputs.py decomposer OUTPUT.md --paste fixtures/C-methods-iv.md

Exit code 0 = all checks passed, 1 = at least one failure.
"""
import argparse
import re
import sys
from pathlib import Path

VERDICTS = {"deep-read", "methods-only", "skim-later", "skip"}
HANDOFF_REQUIRED = ["handoff_version", "paper", "verdict", "confidence", "abstract",
                    "claim", "design_sniff", "red_flags", "unknowns", "questions", "depth"]


def report(results):
    ok = True
    for passed, msg in results:
        print(("PASS  " if passed else "FAIL  ") + msg)
        ok &= passed
    return 0 if ok else 1


def check_triage(text):
    res = []
    labels = re.findall(r"Verdict:\s*([a-z-]+)", text)
    col = None
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.lstrip().startswith("|") else None
        if cells is None:
            col = None
        elif "Verdict" in cells:
            col = cells.index("Verdict")
        elif col is not None and col < len(cells) and not set(cells[col]) <= set("-: "):
            labels.append(re.match(r"[a-z-]*", cells[col]).group(0))
    bad = [l for l in labels if l not in VERDICTS]
    res.append((bool(labels), f"found {len(labels)} verdict label(s)"))
    res.append((not bad, "all verdict labels legal" + (f" (bad: {bad})" if bad else "")))
    for prestige in ("impact factor", "citation count", "top journal", "prestigious"):
        if re.search(rf"\b{prestige}\b", text, re.I):
            res.append((False, f"mentions '{prestige}' — prestige must not drive scores"))
    if "handoff_version" in text:
        block = text[text.index("handoff_version"):]
        block = block.split("```")[0]
        missing = [k for k in HANDOFF_REQUIRED if not re.search(rf"^\s*{k}\s*:", "handoff_version" + block[len("handoff_version"):], re.M)]
        res.append((not missing, "handoff has all required fields" + (f" (missing: {missing})" if missing else "")))
        qs = re.search(r"questions:\s*\n((?:\s+-.*\n?)+)", block)
        n = len(re.findall(r"^\s+-", qs.group(1), re.M)) if qs else 0
        res.append((2 <= n <= 3, f"handoff has 2–3 questions (found {n})"))
    return res


def norm(s):
    return re.sub(r"\s+", "", s).replace("`", "")


def check_decomposer(text, paste):
    res = []
    res.append((bool(re.search(r"Estimand\s*↔\s*estimator alignment|目标量\s*↔\s*估计量对齐", text)),
                "has the 'Estimand ↔ estimator alignment' section"))
    res.append((bool(re.search(r"Identification map|识别策略图", text)), "has an identification map"))
    if paste is not None:
        p = norm(paste)
        eqs = re.findall(r"Symbols?,? as written[^\n]*\n?\s*`?([^`\n]*=[^`\n]*)`?", text)
        eqs += re.findall(r"Symbols?,? as written:?\*{0,2}\s*`([^`]*=[^`]*)`", text)
        eqs = {e.strip() for e in eqs if e.strip()}
        res.append((bool(eqs), f"found {len(eqs)} copied formula(s) to verify"))
        for e in eqs:
            res.append((norm(e) in p, f"formula appears verbatim in the paste: {e[:60]}"))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill", choices=["triage", "decomposer"])
    ap.add_argument("output")
    ap.add_argument("--paste", help="fixture with the pasted Methods (decomposer)")
    a = ap.parse_args()
    text = Path(a.output).read_text(encoding="utf-8")
    if a.skill == "triage":
        res = check_triage(text)
    else:
        res = check_decomposer(text, Path(a.paste).read_text(encoding="utf-8") if a.paste else None)
    sys.exit(report(res))


if __name__ == "__main__":
    main()
