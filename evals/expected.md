# Answer key (do NOT give to test agents)

## A-batch-five-abstracts.md
> Traps: #2 LLM measure with no validation; #3 method prize in an off-agenda domain; #4 causal language with only cross-sectional controls; #5 fully off-agenda.

## A-single-vague-abstract.md
> **Fiction.** This paper does not exist. Trap: on-agenda topic, causal-sounding claim, design and data never named — confidence should be low and the triage should ask for one specific paste.

## C-methods-llm-ocr.md
> Traps: LLM labels treated as ground truth with a thin validation (50 docs, no agreement metric); an OCR-damaged formula; causal over-claim ("proves") from an observational panel; topic labels chosen by authors.

## C-methods-staggered-did.md
> Traps: staggered adoption estimated with plain TWFE; "insignificant pre-trends confirm parallel trends"; SEs clustered at province-year while treatment is assigned by province; equation (3) cited but not shown; weights ω undefined.

## C-methods-llm-ocr.md (extra)
η_c t: city-specific trend vs η×t is ambiguous; the decomposer must flag uncertain parsing, not pick one.

## A-batch-three-abstracts.md (round 2)
- #1: on-agenda IV; red flags: LATE presented as "average effect across all cities"; geography-based instrument exclusion doubtful; "overturning" overclaim. Expect deep-read or skim-later with flags, confidence high.
- #2: pure methods, only a naive baseline + synthetic data + "generalises to any setting" overclaim → methods-only at most, design credibility low.
- #3: on-agenda network/text; descriptive ERGM, "ETS pilot provinces form more ties" is association; possible deep-read; flag document-based tie construction.

## C-methods-iv.md (round 2)
- Estimand: LATE for compliers, not "average effect across all cities"; monotonicity not stated.
- "First stage is strong" with no F reported.
- Hansen J does not confirm exclusion (tests only relative validity; Z and Z² share the same exclusion assumption).
- Distance to coast likely affects FDI directly (trade costs) → exclusion threat.
- Clustering by province vs instrument varying at city × year: fine-ish; number of clusters not stated (31 at most).
- R̂ in second stage: correct 2SLS shape; X in both stages OK.

## C-methods-rdd.md (round 2)
- Global 4th-order polynomials on full sample (discouraged); no local linear / bandwidth.
- Compound treatment at the same cutoff ("Civilised City" funding) → τ not just information disclosure.
- No density / manipulation test; population could be reported strategically.
- Estimand local to cities near 500,000.
- ε_c undefined, outcome year 2017 vs running variable 2014.
