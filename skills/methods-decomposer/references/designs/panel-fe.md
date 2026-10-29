# Plain panel / fixed-effects regression (no named quasi-experiment)

The most common shape in applied social science: an outcome regressed on a continuous or binary variable with unit and time fixed effects, maybe controls and trends, but no discontinuity, instrument, randomisation or clean adoption event. Read this when the paste has `μ_i + τ_t + γ X_it` with no design argument beyond "we control for…".

Answer every question as **stated: <pointer>**, **not stated**, or a short finding.

---

## 1. What identifies the coefficient

- With unit fixed effects, the coefficient comes from **within-unit changes over time**, net of common time shocks. What makes those changes as-good-as-random? A stated argument, or nothing?
- If nothing is stated, the honest estimand is a **conditional association**. Does the text claim more ("effect", "impact", "drives", "proves")? Write named vs design-implied estimand.
- Units with no variation in X contribute nothing to the within estimate — how many are there, and are the identifying units unusual?

## 2. Timing

- **Reverse causality / anticipation:** could Y (or expectations about Y) move X? Leading the outcome (Y at t+1) establishes order but doesn't rule out that X responds to anticipated Y or that both respond to a common shock.
- Why this lag length? Results with other lags, or with leads of X as a placebo (future X shouldn't predict current Y)?

## 3. Time-varying confounding

- Unit FE remove time-invariant differences; time FE remove shocks common to all units. What **time-varying, unit-specific** factors could move both X and Y (growth, leadership change, industrial restructuring)? Discussed or controlled?
- **Unit-specific trends:** included? They change the comparison to deviations from each unit's own trend and can absorb part of a gradual effect — so results with and without trends answer different questions.
- **Region-by-year FE** (e.g. province × year for cities) as a check?

## 4. Controls

- **Bad controls:** controls plausibly affected by X (post-treatment variables, mediators) change what γ means and can bias it. Are controls measured before X changes?
- **Same-source controls:** controls built from the same data or documents as the key regressor may measure part of the same thing.
- Lagged dependent variable with unit FE in short panels → dynamic panel (Nickell) bias; discussed?

## 5. Treatment intensity

- Continuous X in a TWFE regression yields a weighted average of unit-specific slopes; with heterogeneous effects the weights may not be intuitive. Discussed?
- Functional form: logs, levels, per-capita? Do conclusions depend on it?

## 6. Inference

- Cluster at the unit level (or higher if X varies higher up). Number of clusters?
- Long panels: serial correlation handled by clustering?

## 7. Abstract red flag → what to verify in Methods

| Abstract says | Check in Methods |
|---|---|
| "we find that X increases Y" from a panel with FE | Any design argument beyond FE; reverse causality |
| "controlling for a rich set of covariates" | Whether covariates are post-treatment |
| "X in year t predicts Y in t+1" + causal language | Anticipation, common shocks, lead-of-X placebo |

## 8. Good vs weak write-ups (invented)

**Weaker:** "We regress next-year patents on city policy stringency with city and year fixed effects and controls for GDP and enforcement topics. The positive coefficient proves that stringency drives innovation."

**Stronger:** "Our estimates are conditional associations. Stringency in t predicts patents in t+1 but not in t−1, and the relationship survives province-by-year fixed effects and city-specific trends. Because stringency may respond to anticipated innovation, we do not interpret γ causally; Section 6 uses a central inspection campaign as a source of plausibly exogenous variation."
