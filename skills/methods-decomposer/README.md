# methods-decomposer

**Decompose identification before algebra.** Paste a paper's Methods section (formulas included) and get a note that says what the design actually identifies, where the estimator and the claimed estimand part ways, and what the paper doesn't say.

## Minimum input

The Methods / empirical-strategy section as text. Better: plus the abstract or intro (for the paper's own claim), or a `paper-triage` handoff block. Only a results table? It will tell you what it can read off and ask for the paragraph that defines treatment and the estimating equation — it won't reconstruct a design.

## What you get

1. **Identification map** — source of variation, assumptions, named vs design-implied estimand, estimator, threats.
2. **Estimand ↔ estimator alignment** — the signature check: `aligned as stated`, `misaligned: <reason>` (e.g. staggered adoption estimated with plain TWFE; an IV estimate sold as an average effect for everyone), or `can't tell from paste`.
3. **Formulas in three layers** — symbols exactly as written, plain English, what changes if one piece moves. Missing or OCR-damaged pieces are flagged, never repaired.
4. **Design-specific checks** from `references/designs/` — DID, IV, RDD, synthetic control, text/ML/LLM measurement, networks, plain panel FE.
5. Full depth adds data and sample, twists vs a textbook baseline, assumptions and failure modes, a stated / not-stated reproducibility checklist, open questions and — if you say what you're working on — a **reuse card** ("what's worth borrowing for your project").

## Depth

- **quick** (default for "what does this identify / is it believable?") — about one screen.
- **full** (say "full version", or a handoff with `depth: full`) — the 0–10 section template.

## Examples (invented papers)

- `examples/did-quick.md` — staggered DID estimated with TWFE.
- `examples/iv-full.md` — full IV decomposition answering a handoff's questions.
- `examples/uncertain-parsing.md` — an OCR-damaged formula handled without guessing.

## Never

Invents or "fixes" an equation · upgrades an association to a cause · names an estimator as used unless the paste does · claims a direction of bias without a reason in the text.
