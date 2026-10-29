# Synthetic control (and close relatives)

Read this when one or a few treated units are compared with a weighted combination of untreated units: "synthetic control", "donor pool", "synthetic DID", "augmented synthetic control", "counterfactual built from".

Answer every question as **stated: <pointer>**, **not stated**, or a short finding.

---

## 1. Name the pieces

| Piece | What to extract |
|---|---|
| Treated unit(s) and date | Which, when, and how the date is defined (announcement vs implementation) |
| Donor pool | Which units, and which were excluded and why |
| Predictors | Pre-period outcomes only, or covariates too; which years |
| Weights | Reported? Sparse? Which donors matter most? |
| Outcome window | Pre-period length, post-period length |

## 2. Estimand

- The effect **for the treated unit(s)** over the post-period, relative to a counterfactual built from donors. Not an average effect for other units.
- With multiple treated units: separate synthetic controls averaged, or a pooled method? Weights across treated units stated?

## 3. Checks

- **Pre-treatment fit:** shown (plot, pre-period RMSPE)? A poor pre-period fit undermines the post-period comparison. Fit achieved by matching many outcome lags can be mechanical — are some pre-periods held out for validation?
- **Donor pool hygiene:** units with similar policies, or affected by spillovers from the treated unit, should be excluded. Discussed?
- **Interpolation vs extrapolation:** is the treated unit outside the range of donors (largest economy, most polluted city)? Non-negative weights can't extrapolate — the synthetic unit may not resemble it.
- **Anticipation:** effects before the official date? Is the treatment date backdated to the announcement?
- **Concurrent shocks** to the treated unit at the same time?

## 4. Inference

- Conventional standard errors don't apply with one treated unit. What is used?
  - **Placebo-in-space:** assign treatment to each donor and compare the treated unit's effect to that distribution (often via the ratio of post- to pre-period RMSPE)
  - **Placebo-in-time:** fake treatment dates in the pre-period
  - Conformal or other inference methods
- How is a p-value or interval obtained, and how many donors are there? (With 20 donors, the smallest possible placebo-in-space p-value is about 1/21.)

## 5. Variants

- **Synthetic DID:** combines unit weights with time weights and a DID structure; needs parallel-trends-like assumptions on the weighted comparison.
- **Augmented / penalised SC:** bias correction when pre-fit is imperfect.
- Only treat a variant as used if the paste names it.

## 6. Abstract red flag → what to verify in Methods

| Abstract says | Check in Methods |
|---|---|
| "a synthetic counterfactual shows a 20% reduction" | Pre-fit quality; placebo distribution |
| One very distinctive treated region | Extrapolation outside donor range |
| "significant" with one treated unit | How inference was done |

## 7. Good vs weak write-ups (invented)

**Weaker:** "We construct a synthetic Province A from the other 30 provinces. After the policy, emissions in Province A fall 15% below the synthetic control, which is statistically significant."

**Stronger:** "We exclude four provinces that adopted similar caps within two years. The synthetic unit, built from pre-2012 emissions and industrial structure, tracks Province A closely through 2011 (pre-RMSPE 0.8). Among 27 placebo runs Province A has the largest post/pre RMSPE ratio (p ≈ 1/27). Results hold when we drop the two donors with the largest weights."
