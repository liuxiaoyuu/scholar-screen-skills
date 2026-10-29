# Regression discontinuity

Read this when treatment changes at a threshold of a continuous score: "cutoff", "threshold", "discontinuity", "RD", "running variable", "bandwidth", "eligible if X ≥ c", population/score/age/date thresholds.

Answer every question as **stated: <pointer>**, **not stated**, or a short finding.

---

## 1. Name the pieces

| Piece | What to extract |
|---|---|
| Running variable | What it is, when it was measured, how precisely (continuous? integers? rounded?) |
| Cutoff | Value and the rule that creates it |
| Treatment rule | What switches at the cutoff |
| Sharp or fuzzy | Does everyone above get treated (sharp), or does the **probability** jump (fuzzy)? |
| Outcome | What, measured when, measured how — on both sides |

## 2. Estimand

- Sharp RD identifies the average effect **for units at the cutoff**. It says nothing directly about units far from it. Does the paper generalise?
- Fuzzy RD identifies a **local LATE** at the cutoff for compliers (units whose treatment status responds to crossing). Is it estimated as IV at the cutoff (first-stage jump reported)? If the paper treats a fuzzy design as sharp, the estimate is an intention-to-treat jump.
- **Named vs design-implied:** papers often name the estimand by the policy they care about ("the effect of disclosure") when the cutoff triggers more than that. Write both.

## 3. Identification threats

- **Manipulation / sorting:** can units precisely control their running variable to land just above or below (self-reported population, test retakes, fiscal reporting)?
  - Evidence: a density test of the running variable at the cutoff (McCrary-type or local polynomial density tests), plus institutional arguments that precise sorting was impossible.
  - Heaping at round numbers?
- **Covariate balance:** pre-determined covariates should not jump at the cutoff. Shown?
- **Compound treatment:** do other policies, programs or eligibilities switch at the **same** cutoff? Then the jump is the bundle, not the named policy. (Population thresholds are notorious for this.)
- **Measurement changing at the cutoff:** if the treatment changes how the outcome is measured (new monitors, new reporting, new auditors), a jump may be a measurement artefact. Is the outcome measured the same way on both sides?
- **Timing:** was the running variable measured before the rule was known? If not, sorting is more plausible.

## 4. Estimation

- **Local linear (or local quadratic) within a bandwidth** is current practice. **Global high-order polynomials** (cubic, quartic on the full sample) are generally discouraged: they weight distant observations heavily, can produce spurious jumps, and give poor coverage. Robustness to a different polynomial order on the full sample doesn't fix this.
- Bandwidth: data-driven (e.g. MSE-optimal) or ad hoc? Robustness across bandwidths shown?
- Kernel stated (triangular is common)?
- **Inference:** robust bias-corrected confidence intervals, or conventional SEs that ignore smoothing bias?
- **Effective sample:** how many units fall within the bandwidth? With few units near the cutoff, precision is low regardless of total N.
- **Discrete running variable** (few distinct values: years, integer scores): standard methods assume continuity; any adjustment or discussion?

## 5. Variants

- **Regression kink:** the slope (not level) of treatment changes at the threshold — needs smoothness in derivatives; very data-hungry.
- **Geographic RD:** a boundary between regions is the cutoff — check for other differences at the border (other policies, people sorting across it).
- **RD in time:** a date as the running variable — anticipation, other changes on the same date, serial correlation; often closer to an interrupted time series than an RD.
- **Multi-cutoff / multi-score:** are effects pooled across cutoffs? Normalised how?

## 6. Abstract red flag → what to verify in Methods

| Abstract says | Check in Methods |
|---|---|
| "exploiting a population threshold" | Other policies at the same threshold; manipulation of reported population |
| "the effect of X" from an eligibility cutoff | Sharp vs fuzzy; first-stage jump |
| A large effect with a sample of a few hundred units | Effective sample within bandwidth |
| "robust to polynomial order" | Whether all specifications are global polynomials |

## 7. Good vs weak write-ups (invented)

**Weaker:** "Cities above 500,000 must disclose air quality. We fit fourth-order polynomials on both sides using all 612 cities. τ is the effect of disclosure; results are robust to third-order polynomials."

**Stronger:** "We estimate local linear regressions with a triangular kernel and MSE-optimal bandwidth (about 140 cities on each side), reporting robust bias-corrected intervals. The density of reported population shows no bunching at the cutoff. Because the same threshold also triggers funding eligibility, we interpret τ as the joint effect of disclosure and funding and use a 2018 change in the funding rule to separate them."

## 8. What not to claim

- Don't assert manipulation happened — ask whether it was tested and whether units could sort.
- Don't claim a direction of bias from compound treatment unless the text says how the other policy affects the outcome.
