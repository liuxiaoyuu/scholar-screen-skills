# Red flags (suspects, not verdicts)

Flag one only when the supplied text gives a hook, and label it **red flag** or **unknown**. An abstract that omits detail is normal — mark `待核`, don't invent the missing design. A red flag with a clear hook caps design credibility at 1.

Each entry: **what it looks like in an abstract** → **what methods-decomposer (or you, reading Methods) should verify**. The deep checklists live in `methods-decomposer/references/designs/`.

---

## Any design

| Looks like this in the abstract | Verify in Methods |
|---|---|
| Causal verbs ("effect", "impact", "causes", "drives", "shapes", "leads to", "policy learning") with no named source of variation | Is there any design, or only controls? |
| "We control for a rich set of confounders" offered as the identification | Which controls; are they pre-treatment; what's left uncontrolled |
| A result that "overturns" or "proves" | Whether the design supports a claim that strong |
| Implausibly large or "too clean" effect for the setting | Sample size, specification search, outliers |
| Few treated units, short panel or single site → general conclusions | Number of treated clusters; scope of the claim |
| One province / one city / one platform → "implications for all" | External validity discussion |
| Many outcomes or specifications hinted, only significant ones headlined | Pre-registration, multiple-testing adjustment |

## Difference-in-differences

| Abstract | Methods |
|---|---|
| "exploit the staggered rollout" + "two-way fixed effects" | Heterogeneity-robust estimator or TWFE with forbidden comparisons |
| "pre-trends prove / confirm parallel trends" (overreach; a plain "no detectable pre-trends" is routine — verify it, don't flag it) | Evidence offered; insignificant leads treated as proof? |
| Pilot regions → "effect of the policy" nationwide | Estimand is the effect on pilots (ATT) |
| Voluntary adoption | Why adopters and non-adopters would have trended alike |

## Instrumental variables

| Abstract | Methods |
|---|---|
| Instrument named, no exclusion argument hinted | Exclusion argument, placebo/falsification tests |
| Geography, distance or history as the instrument | Other channels from Z to Y (trade costs, income, institutions) |
| IV estimate described as "the average effect across all units" | 2SLS gives a LATE for compliers; monotonicity |
| "Robust to overidentification tests" | Instruments from the same source share the same flaw |
| "Overturns OLS" | First-stage strength reported as a number |

## Regression discontinuity

| Abstract | Methods |
|---|---|
| A population, size or score threshold | Other policies switching at the same threshold |
| Self-reported or manipulable running variable | Density test; ability to sort |
| "The effect of X" from an eligibility cutoff | Sharp vs fuzzy; effect is local to the cutoff |
| Treatment changes how the outcome is measured | Measurement comparable on both sides |

## Synthetic control

| Abstract | Methods |
|---|---|
| One distinctive treated unit, "synthetic counterfactual" | Pre-period fit; donor pool; extrapolation |
| "Significant" with one treated unit | Placebo-based inference |
| Neighbours or similar adopters in the donor pool | Spillovers and contaminated donors |

## Text, ML and LLM measurement

| Abstract | Methods |
|---|---|
| "We use an LLM / classifier to score N documents" with no validation mentioned | Gold set, agreement metric, held-out performance |
| A new measure + "X predicts Y" | Construct validity; shared artefacts between X and Y |
| Topics with evocative labels reported as findings | Who labelled, when, stability across K |
| "Millions of posts" → "the public" | Who's in the corpus; generalisation |
| Predicted labels used directly in regressions | Measurement-error correction (DSL, prediction-powered inference) |

## Networks

| Abstract | Methods |
|---|---|
| "Connected units are more likely to adopt" + "learning" / "influence" | Homophily and common-shock controls; timing of ties |
| "Network position matters more than X" | Predictor horse race (association) vs identified effect |
| Sampled or scraped network analysed as complete | Missing ties; boundary specification |
| Standard errors on dyads | Dependence handled (ERGM, QAP, dyadic clustering) |

## Pure methods papers

| Abstract | Methods |
|---|---|
| Beats "a naive baseline", or only the method it claims to fix (e.g. a new staggered-DID estimator vs plain TWFE only) | Comparison with strong current alternatives |
| Synthetic data only | Any real application |
| "Generalises to any setting" | Evidence beyond the tested setting |

## Not red flags by themselves

- Observational data honestly described as descriptive.
- An abstract that doesn't name the estimator.
- A small but well-defined sample with modest claims.
- A paper in a lower-profile venue (venue never enters the score).
