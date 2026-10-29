# Instrumental variables

Read this when the paste uses an instrument: "instrument", "IV", "2SLS", "first stage", "exclusion restriction", "exogenous variation in X from Z", "shift-share", "Bartik", "judge leniency", "distance to", "historical".

Answer every question as **stated: <pointer>**, **not stated**, or a short finding. Questions, not accusations.

---

## 1. Name the pieces

| Piece | What to extract |
|---|---|
| Treatment X | The endogenous variable, and why it's endogenous (as stated) |
| Instrument Z | Exactly how it's built (levels, logs, interactions, squares) |
| Outcome Y | As defined |
| Controls / FE | Same in both stages? |
| Level of variation | At what level does Z vary (city, city-year, national-year)? That sets how many independent sources of variation identify the effect and the right clustering level. |

## 2. Estimand

- With **heterogeneous effects**, 2SLS with a binary instrument identifies a **LATE**: the average effect for **compliers**, the units whose treatment is moved by the instrument. With multiple or continuous instruments it's a weighted average of such local effects.
- This needs **monotonicity** (no defiers: the instrument doesn't push some units toward treatment and others away). Stated, argued, or not stated?
- **Common mismatch:** the paper calls β "the average effect for all units" or "the effect of X" in general. Unless it argues effects are homogeneous or that compliers are representative, the design delivers a local effect. Write the named and design-implied estimands separately.
- Who are the compliers here? Does the paper describe them (e.g. "cities whose enforcement responds to the national target")?

## 3. Relevance (first stage)

- Is first-stage strength **reported as a number** — a first-stage F, an effective F (robust to heteroskedasticity/clustering), or the coefficient with its SE? "The first stage is strong" without a number is **not stated**.
- Weak instruments bias 2SLS toward OLS and distort inference. If the first stage is modest, any weak-instrument-robust inference (e.g. Anderson–Rubin confidence sets)?
- Is the first stage's sign and size plausible, and is it shown for the same sample as the second stage?

## 4. Independence (as-good-as-random)

- Is Z as-good-as-random unconditionally, or only conditional on stated controls? Which controls, and are they pre-determined?
- Any balance or placebo evidence that Z isn't correlated with pre-existing differences?

## 5. Exclusion (the hard one)

- The exclusion restriction — Z affects Y **only** through X — is **not directly testable**. What does the paper offer?
  - A substantive argument about why other channels are closed
  - **Placebo outcomes** that Z shouldn't affect if exclusion holds
  - **Falsification samples** where X can't respond to Z (so Z should show no reduced-form effect on Y)
  - Sensitivity analysis for small violations (plausibly-exogenous-style bounds)
  - Or nothing
- **Over-identification tests (Hansen J / Sargan)** check whether multiple instruments **agree with each other**, not whether any is valid. If all instruments share the same flaw, J won't reject. Instruments built from the same variable (Z and Z², Z interacted with different years) share the same exclusion risk, so non-rejection says almost nothing. Watch for "the J test confirms exclusion".
- Raise channels the text mentions, plus the standard channels for the instrument type below — always as questions ("Could distance to the coast affect FDI through trade costs?"). Don't invent paper-specific facts.

## 6. Instrument types and their usual worries

| Type | How it looks | Standard questions |
|---|---|---|
| **Geography / distance** | Distance to coast, rivers, ports, borders; terrain | Does geography affect Y through trade/transport costs, income, climate, infrastructure, history? |
| **Historical** | Colonial institutions, past events, old infrastructure | Persistent effects through many channels; is X the only one? |
| **Shift-share / Bartik** | Local shares × national shifts | Are the **shares** or the **shifts** claimed exogenous? Shares often correlate with other local trends; shifts need many independent shocks. Which identification argument does the paper make? |
| **Policy / rule-based** | Eligibility rules, national targets × local exposure | Does the rule affect Y directly, not only via X? Is exposure pre-determined? |
| **Judge / examiner leniency** | Random assignment of cases to decision-makers | Random assignment stated? Monotonicity across judges plausible? Leave-one-out construction? |
| **Weather / natural shocks** | Rainfall, temperature, disasters | Weather affects many outcomes directly (agriculture, health, mobility) |
| **Lagged X as instrument** | X at t−k instruments X at t | Requires no persistence in the error — rarely credible; is it argued? |

## 7. Inference

- Cluster at the level the instrument varies (or higher). If Z varies only at the national-year level interacted with a fixed local trait, identification rests on few effective "experiments" — discussed?
- Number of clusters reported?

## 8. Abstract red flag → what to verify in Methods

| Abstract says | Check in Methods |
|---|---|
| "we instrument X with Z" + "average effect across all units" | Estimand (LATE vs ATE), monotonicity, complier description |
| "exploiting distance / geography / history" | Exclusion argument; placebo or falsification tests |
| "robust to overidentification tests" | Whether instruments share the same source |
| "overturns prior OLS estimates" | First-stage strength; whether IV and OLS target the same population |

## 9. Good vs weak write-ups (invented)

**Weaker:** "We instrument enforcement with distance to the coast. The first stage is strong. The Hansen J test does not reject, which confirms the exclusion restriction. β is the average effect of enforcement on FDI across all cities."

**Stronger:** "Our instrument interacts pre-determined distance to the coast with year-specific national targets. The first-stage effective F is 31. Because distance may affect FDI through trade costs, we show the reduced form is zero in years before targets existed and in inland cities where targets did not bind. Our estimate is a LATE for cities whose enforcement responds to national targets; we describe these compliers in Table 4."

## 10. What not to claim

- Don't assert the instrument is invalid — say which channel would violate exclusion and whether the paper addresses it.
- Don't infer the direction of bias without a reason in the text.
