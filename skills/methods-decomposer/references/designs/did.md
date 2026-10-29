# Difference-in-differences and event studies

Read this when the paste compares treated and untreated units before and after a policy, rollout, shock or adoption — words like "difference-in-differences", "DID", "event study", "two-way fixed effects", "staggered", "pilot", "rollout", "post × treat".

Answer every question as **stated: <pointer>**, **not stated**, or a short finding. These are questions, never accusations — don't claim what the authors "must have done".

---

## 1. Recognise the variant

| Variant | How it shows up in the paste | What it needs |
|---|---|---|
| Canonical 2×2 | One treated group, one control group, one adoption date | Parallel trends between the two groups |
| Common timing, many units | All treated units adopt in the same year | Parallel trends; TWFE is fine if effects are homogeneous across units |
| **Staggered adoption** | Treated units adopt in different years ("phased", "pilot then expansion", "three provinces in 2014, four in 2016") | Parallel trends for each cohort; a heterogeneity-robust estimator, or an argument that effects don't vary across cohorts and over time |
| Treatment switching on and off | Units enter and exit treatment | Estimators that allow exit; assumptions about carryover |
| Continuous / dose DID | Treatment intensity varies ("exposure", "share", "intensity") | Parallel trends across dose levels, plus assumptions about how effects scale with dose; much stronger than binary DID |
| Triple differences (DDD) | A third dimension (e.g. affected vs unaffected industries within treated regions) | Parallel trends in the *difference* between groups |

## 2. Estimand

- Is the target named? Usually it should be an **ATT** (average effect on the treated). Write the named estimand and the design-implied one separately.
- With staggered timing, "the" effect is ambiguous: group-time ATTs, an event-time profile, or an aggregated ATT with stated weights. Which one does the text promise?
- Dynamic effects: does the paper distinguish an average post-period effect from effects by years since adoption?

## 3. The estimand ↔ estimator check (the most common failure)

**Staggered adoption + TWFE with one treatment dummy** (`Y_it = α_i + λ_t + β D_it + ε_it`):

- When effects differ across cohorts or grow over time, β is a weighted average of many 2×2 comparisons, including **"forbidden" comparisons** where already-treated units serve as controls for later-treated units. Some weights can be negative, so β can even have the wrong sign relative to every underlying effect.
- What to look for in the paste:
  - Does the paper acknowledge heterogeneous effects?
  - Does it show a decomposition of β into its 2×2 comparisons?
  - Does it use a heterogeneity-robust estimator? Common families: group-time ATT aggregation (Callaway–Sant'Anna), interaction-weighted event studies (Sun–Abraham), imputation (Borusyak–Jaravel–Spiess), switching estimators (de Chaisemartin–D'Haultfœuille), stacked DID. Only say an estimator is **used** if the paste names it.
- **Event studies estimated by TWFE with leads and lags** have the same problem: lead and lag coefficients can be contaminated by effects from other periods, so "flat leads" from a TWFE event study under staggered timing are weaker evidence than they look.

**Common timing + TWFE:** fine as an estimator of the ATT under parallel trends; the remaining questions are about the assumptions below.

## 4. Parallel trends

- Is the assumption stated, for which outcome, and on which scale? Parallel trends in levels and in logs can't both hold in general — which does the paper pick, and why?
- **Pre-trend evidence:** event-study leads, a plot, or a placebo test on pre-periods?
  - **Failing to reject pre-trends does not establish parallel trends.** Pre-tests can have low power, and conditioning the analysis on passing a pre-test distorts later inference. Watch for "insignificant leads confirm/prove parallel trends".
  - Stronger practice: report power or minimum detectable pre-trends, show sensitivity to violations of a given size (e.g. "honest DID"-style bounds), or argue substantively why trends would have been parallel.
- **Conditional parallel trends:** if covariates are used, are they measured *before* treatment? Time-varying covariates that the policy itself could change are bad controls.
- **Why these controls?** Is the choice of control units argued (similar pre-trends, same region, not-yet-treated) or just "all other units"?

## 5. Anticipation, spillovers, composition

- **Anticipation:** could units react to an announcement before the official date? If so, the "pre" period is contaminated. Is the announcement date discussed, or are pre-periods trimmed?
- **Spillovers (SUTVA):** could the policy affect control units (neighbouring provinces, shared markets, displaced pollution or activity)? Discussed?
- **Composition:** do units enter or exit the sample in ways related to treatment (firms closing, cities merging)? Balanced panel?
- **Concurrent policies:** did something else change at the same time for the same units?

## 6. Inference

- Clustering at the level of treatment assignment (e.g. province when provinces adopt), not lower (province-year).
- **Report the number of treated clusters.** With few treated clusters (a handful to a couple of dozen), conventional cluster-robust SEs can over-reject — any wild cluster bootstrap, randomization inference, or other few-cluster method?
- Many outcomes or many event-time coefficients → any multiple-testing adjustment?

## 7. Abstract red flag → what to verify in Methods

| Looks like this in the abstract | Check this in Methods |
|---|---|
| "exploit the staggered rollout" + "two-way fixed effects" | Estimator under heterogeneity; forbidden comparisons |
| "no pre-trends" / "parallel trends hold" | What evidence, how much power, what scale |
| Large effect from a policy adopted by few units | Number of treated clusters; inference method |
| "effect of X across all regions" from a pilot in a few regions | Estimand is the ATT for pilots; external validity |
| "We control for GDP and industrial structure" | Are controls pre-treatment or could the policy move them? |

## 8. Good vs weak write-ups (invented)

**Weaker:** "We estimate a two-way fixed-effects model with province and year fixed effects. The coefficients on the leads are insignificant, which confirms the parallel trends assumption. β captures the causal effect of the policy."
→ Staggered timing unaddressed, pre-test treated as proof, estimand unnamed.

**Stronger:** "Because adoption is staggered and effects may grow over time, we estimate cohort-by-year ATTs using never-treated provinces as controls and aggregate them to an event-time profile. We report pre-period estimates with confidence bands and show how large a linear pre-trend would have to be to overturn the result. Standard errors are clustered by province; with 11 treated provinces we also report wild-cluster bootstrap p-values."
→ Estimand named, estimator matches staggered timing, pre-trends treated as evidence with limits, inference matches the few-cluster setting.

## 9. What not to claim

- Don't say an estimate is biased in a particular direction unless the text gives a reason (TWFE under heterogeneous, growing effects can bias toward zero or flip sign, but you can't know which without the paper's numbers).
- Don't name an estimator as "the right one" — say what the problem is and that robust alternatives exist.
