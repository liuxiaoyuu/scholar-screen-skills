# paper-triage

**Screen with a rubric, not a vibe.** Paste a title and abstract (or a batch of them) and get a reading decision you can defend in one line.

## Minimum input

Title + abstract. That's it. An intro or an open-access PDF helps; a stated goal ("I'm writing about carbon markets") sharpens relevance. No setup, no profile.

## The four scores (0–2 each)

| Score | Asks |
|---|---|
| **claim** | Can you tell what's claimed, and how strongly (association vs cause)? |
| **design** | Does the design (or validated measure) support a claim that strong? Red flags cap it at 1. |
| **relevance** | topic (0/1) + method (0/1) — social science by default, or your stated goal |
| **payoff** | Does it offer something new: a question, data, measure or design others can reuse? |

## The four verdicts

| Verdict | Means |
|---|---|
| `deep-read` | Read it fully now |
| `methods-only` | Skip the story; learn the method or measure (→ `methods-decomposer`) |
| `skim-later` | Park it, with a concrete "reopen when …" trigger |
| `skip (off-topic)` / `skip (weak design)` | Don't spend time; the reason tells you which |

Plus **confidence** (high / low). Low confidence comes with the one paste that would most likely change the verdict.

## Batch example (invented abstracts)

| # | Paper | Verdict | Total | Relevance | Conf. | One-line why |
|---|---|---|---|---|---|---|
| 1 | Carbon markets & firm emissions | deep-read | 8/8 | 2 | high | Staggered rollout with a heterogeneity-robust estimator backs a causal claim scoped to covered firms |
| 3 | Synthetic-DID estimator | methods-only | 7/8 | 2 | high | The estimator is the contribution; benchmarked only against plain TWFE |
| 2 | LLM policy-stringency measure | methods-only | 6/8 | 2 | high | The measure is the contribution; no validation mentioned (待核) |
| 4 | "Social media causes polarization" | skip (weak design) | — | 1 | high | Causal claim from a cross-section with controls only |
| 5 | Mice and dietary fibre | skip (off-topic) | — | 0 | high | Not social science |

Full examples: `examples/single-deep-read.md`, `examples/batch-table.md`, `examples/handoff-iv.md`.

## Handoff

For keepers it writes a fixed-order YAML block (`handoff_version: 1`) with the abstract, claim, design sniff, red flags, unknowns, 2–3 questions and a suggested depth. Paste it into `methods-decomposer` together with the paper's Methods section.

## Never

Searches databases · invents findings · writes peer reviews · lets journal prestige or citation counts into a score.
