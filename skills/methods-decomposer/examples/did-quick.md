> **Invented example.** The paper, data and numbers are fictional; they exist only to show the skill's output.

**User:** What does this actually identify?

> **3. Empirical Strategy (fictitious)**
>
> Between 2014 and 2018, 11 of 31 provinces introduced a River Chief accountability system, in different years (three in 2014, four in 2016, four in 2018). The outcome is the annual share of monitored river sections meeting Grade III water quality, from provincial environmental bulletins (2009–2021). We estimate
>
> Y_pt = α_p + λ_t + β · RiverChief_pt + X_pt'θ + ε_pt        (1)
>
> where RiverChief_pt equals one from the year province p adopts the system onward, α_p and λ_t are province and year fixed effects, and X_pt includes GDP per capita and industrial output share. β captures the causal effect of the River Chief system on water quality.
>
> To examine dynamics we estimate an event-study version, equation (3), with leads and lags relative to adoption. The coefficients on the leads are small and statistically insignificant, which confirms the parallel trends assumption. Observations are weighted by ω_p as described in the appendix. Standard errors are clustered at the province-year level.

---

**methods-decomposer:**

As written, β is not a clean effect for anyone: it is a two-way fixed-effects (TWFE) weighted average of many before/after comparisons across three adoption cohorts (2014, 2016, 2018), some of which use already-treated provinces as controls. The design could identify an average effect on the treated (ATT) for the 11 adopting provinces, but the estimator shown does not deliver it if effects differ by cohort or grow over time — and the inference (province-year clustering, 11 treated provinces) is a second, separate problem.

Only Methods supplied, so the paper's own claim isn't checked.

# Methods decomposition (quick): untitled paste ("3. Empirical Strategy")

> Scope: Methods paste · Design family: DID, staggered adoption · Parsing: clear

## Identification map

| Element | From the text |
|---|---|
| Source of variation | Staggered adoption: "11 of 31 provinces … three in 2014, four in 2016, four in 2018"; 20 never-treated provinces (31 − 11, my calculation) |
| Identifying assumptions | Parallel trends, named only via the lead test ("confirms the parallel trends assumption"); scale and control group not stated |
| Estimand | **Named:** "the causal effect of the River Chief system on water quality" — one effect, population unspecified. **Design-implied (my reading):** ATTs for the adopting provinces, by cohort and by years since adoption, plus whatever aggregate of them the paper chooses |
| Estimator | TWFE regression (1) with one adoption dummy, controls X_pt, weights ω_p; a TWFE event study (3) for dynamics; SEs clustered by province-year |
| Threats | **Addressed:** pre-trends, via insignificant leads. **Mentioned but not treated as a threat:** none. **Not discussed:** effect heterogeneity across cohorts, anticipation, spillovers, concurrent policies, whether the controls respond to the policy |

## Estimand ↔ estimator alignment

**misaligned: staggered adoption estimated by single-dummy TWFE.**
With adoption in 2014, 2016 and 2018, β mixes 2×2 comparisons, including ones where earlier adopters act as controls for later ones; with heterogeneous or growing effects some weights can be negative.
The paste names no heterogeneity-robust estimator and no decomposition of β.
The weights ω_p (see Design-specific checks) change the mix again in a way the paste doesn't show.

## Data in one line

31 provinces (11 treated) · annual, 2009–2021 · outcome: "annual share of monitored river sections meeting Grade III water quality" from provincial bulletins (whether this means Grade III *or better*, and whether the set of monitored sections is fixed over time, is not stated) · treatment: RiverChief_pt = 1 from the adoption year onward.

## Formulas

**Formula (1) — main TWFE specification**

- **Symbols, as written:** `Y_pt = α_p + λ_t + β · RiverChief_pt + X_pt'θ + ε_pt`
- **Plain English:** the Grade III share in province p, year t, is modelled as a province constant, a year constant, a shift of β once the province has adopted, and the two controls (GDP per capita, industrial output share). Under parallel trends *and* an effect that is identical across cohorts and constant over time, β is the average post-adoption change in the share. θ and ε_pt are not defined in the paste.
- **If one piece moved:**
  - *Drop X_pt.* If adoption itself moves industrial output share or GDP per capita, then with X_pt included β is the change net of those channels; without it, β targets the total change. Whether the controls are measured before adoption is not stated.
  - *Unweighted instead of ω_p.* Each province would count equally in the comparisons; with ω_p, β averages over provinces in proportion to weights the paste never defines, so it can describe a different set of provinces.
- **Parsing:** `clear`

**Mentioned but not shown:** the event-study equation (3) is cited but not displayed (lead/lag window and reference period unknown). Numbering jumps from (1) to (3); (2) is never mentioned.

## Design-specific checks

- **Heterogeneous effects under staggered timing:** not stated. No acknowledgement that effects may differ by cohort, no decomposition of β, no robust estimator named.
- **Pre-trends:** stated — "leads are small and statistically insignificant, which confirms the parallel trends assumption." Insignificant leads don't establish parallel trends; power, minimum detectable pre-trend and sensitivity to violations are not stated. Because (3) is a TWFE event study under staggered timing, its leads can also be contaminated by effects from other periods.
- **Clustering level:** stated — province-year, which is below the level at which treatment is assigned (province). With 11 treated provinces, any few-cluster method (e.g. wild cluster bootstrap) is not stated.
- **Controls:** GDP per capita and industrial output share are time-varying; whether they are pre-treatment, or could themselves be moved by the policy, is not stated.
- **Anticipation, spillovers, concurrent policies:** not stated. Rivers cross provincial borders, so whether upstream adoption changes water quality in never-treated downstream provinces is a natural question the paste doesn't raise.
- **Weights ω_p (outside the checklist):** "as described in the appendix" — what they are and why they are used is unknown, so it is unclear which provinces dominate β.

## Biggest open question

1. Does the paper report cohort-by-year or otherwise heterogeneity-robust estimates (and with never-treated or not-yet-treated provinces as controls)? If not, β cannot be read as an ATT.
2. What is ω_p, and do the results hold unweighted?
3. When was each province's adoption announced relative to its adoption year? Early announcement would contaminate the "pre" years the lead test relies on.

Say "full" if you want the complete decomposition (assumptions table, reproducibility checklist, open questions).
