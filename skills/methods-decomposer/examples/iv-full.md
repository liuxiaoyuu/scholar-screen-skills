> **Invented example.** The paper, data and numbers are fictional; they exist only to show the skill's output.

**User:** Full decomposition please.

```yaml
# handoff to methods-decomposer
handoff_version: 1
paper: "Coastal Distance, Environmental Regulation, and Foreign Investment in Chinese Cities"
verdict: deep-read
confidence: high
abstract: |
  Do stricter environmental regulations deter foreign direct investment? We study 280 Chinese prefecture-level cities from 2005 to 2018. Because regulation stringency is endogenous to investment, we instrument it with each city's distance to the coast interacted with national ventilation-based pollution targets. Two-stage least squares estimates show that a one-standard-deviation increase in stringency reduces FDI inflows by 12% on average across all cities, overturning the "pollution haven" scepticism in prior work.
claim: "a one-standard-deviation increase in stringency reduces FDI inflows by 12% on average across all cities"
design_sniff: "quasi-experimental — 2SLS with distance to the coast × national pollution targets as the instrument"
red_flags:
  - "Distance to the coast may affect FDI directly (trade and transport costs), not only through regulation"
  - "'on average across all cities' from 2SLS: a local effect presented as an average for everyone?"
  - "'overturning' prior work on the strength of one instrument"
unknowns:
  - "How stringency is measured"
  - "First-stage strength"
  - "Clustering level and number of clusters"
questions:
  - "What evidence supports exclusion beyond the J test?"
  - "Is β a LATE, and for whom?"
  - "How strong is the first stage?"
depth: full
data: "280 prefecture-level cities · 2005–2018"
reader_goal: "not stated"
```

> **4. Identification Strategy (fictitious)**
>
> Regulation stringency R_ct (the count of environmental enforcement actions per 1,000 firms) is likely endogenous: cities attracting more FDI may face different enforcement. We instrument R_ct with Z_ct = log(Distance_c) × Target_t, where Distance_c is the city's distance to the nearest coastline and Target_t is the national ventilation-coefficient-based pollution target in year t.
>
> First stage:   R_ct = π Z_ct + X_ct'ψ + α_c + δ_t + v_ct        (4)
> Second stage:  log(FDI_ct) = β R̂_ct + X_ct'κ + α_c + δ_t + e_ct      (5)
>
> X_ct includes log GDP, population and road density. The first stage is strong. Because we also use a second instrument (Z_ct squared), the Hansen J test of over-identifying restrictions does not reject (p = 0.41), which confirms that the exclusion restriction holds. β is the average effect of regulation on FDI across all cities. Standard errors are clustered by province.

---

**methods-decomposer:**

**TL;DR.** The design uses the changing national pollution target, felt differently by cities at different distances from the coast, to move enforcement intensity; at best it identifies a weighted local effect (LATE) for cities whose enforcement responds to that interaction, not "the average effect … across all cities". The biggest problem is exclusion: the only evidence offered is a Hansen J test between Z_ct and Z_ct², two instruments built from the same variable, which cannot speak to exclusion. All three handoff questions are answered in 9a; the short answers are "none in the paste", "yes, a weighted LATE; compliers undescribed", and "not reported as a number".

# Methods decomposition (full): Coastal Distance, Environmental Regulation, and Foreign Investment in Chinese Cities

> **Scope:** Methods paste + abstract from handoff
> **Design family:** IV (geography × national policy rule)
> **Parsing:** clear
> **Handoff from paper-triage:** yes (handoff_version 1)

## 0. Contract (intro / abstract)

- **Question:** "Do stricter environmental regulations deter foreign direct investment?" (from handoff)
- **Design in one sentence:** 2SLS, instrumenting regulation stringency with "distance to the coast interacted with national ventilation-based pollution targets" (from handoff); the Methods specify the interaction as log(Distance_c) × Target_t.
- **Data (as named):** "280 Chinese prefecture-level cities from 2005 to 2018" (from handoff). The Methods paste itself gives no sample size or years.
- **Claim strength:** causal and general — "reduces FDI inflows by 12% on average across all cities, overturning the 'pollution haven' scepticism" (from handoff). The Methods agree in strength: "β is the average effect of regulation on FDI across all cities." Contract and Methods don't disagree with each other; both claim more than the design delivers (section 1).
- **Scale note:** the abstract reports the effect per standard deviation of stringency; the Methods measure R_ct as enforcement actions per 1,000 firms. The SD of R_ct is not stated, so the 12% can't be traced to β from the paste.

## 1. Identification map

| Element | From the text |
|---|---|
| Source of variation | Z_ct = log(Distance_c) × Target_t: a fixed city trait (coastal distance) interacted with a national year-by-year target. With city and year FE, the main effects are absorbed; what remains is how the distance gradient in enforcement changes as the national target changes |
| Identifying assumptions (stated) | Relevance: "The first stage is strong" (no number). Exclusion: claimed via "the Hansen J test … confirms that the exclusion restriction holds". Independence and monotonicity: not stated |
| Estimand | **Named:** "the average effect of regulation on FDI across all cities". **Design-implied (my reading):** with heterogeneous effects, a weighted average of local effects for cities whose enforcement count is moved by the instrument (compliers), requiring monotonicity |
| Estimator | Two-stage least squares (named in the abstract, from handoff), equations (4)–(5), with Z_ct and Z_ct² as excluded instruments, controls X_ct, city and year FE; SEs clustered by province |
| Threats | **Addressed:** endogeneity of R_ct ("cities attracting more FDI may face different enforcement"). **Mentioned but not treated as a threat:** the second instrument Z_ct² is presented as enabling the J test, not as sharing Z_ct's exclusion risk. **Not discussed:** direct channels from distance × target to FDI, weak instruments, monotonicity, complier population, controls affected by regulation |

### 1a. Estimand ↔ estimator alignment

**misaligned: 2SLS delivers a complier-weighted local effect, not "the average effect … across all cities".**
The named estimand needs either homogeneous effects or compliers representative of all 280 cities; neither is argued in the paste.
With a continuous instrument plus its square, the weights over cities are set by the first stage and are not shown.

## 2. Data and sample

- **Units:** cities (c); "prefecture-level", 280 of them (from handoff).
- **Time:** years (t); 2005–2018 (from handoff).
- **Inclusion / exclusion:** not stated.
- **Treatment / key variable definition:** R_ct, "the count of environmental enforcement actions per 1,000 firms". Source of the counts and of the firm denominator: not stated.
- **Outcome definition:** log(FDI_ct). How FDI is measured (inflows, utilised, contracted) and how city-years with zero FDI are handled under the log: not stated.
- **Instrument pieces:** Distance_c = "distance to the nearest coastline"; Target_t = "the national ventilation-coefficient-based pollution target in year t". How the target is scaled (level, tightness index) is not stated.
- **Source, as named:** not stated.
- **Size:** 280 cities (from handoff); at most 280 × 14 = 3,920 city-years (my calculation, assuming a balanced panel, which is not stated).

## 3. Estimation / model

2SLS (name from handoff abstract). Both stages include the same controls X_ct ("log GDP, population and road density") and city (α_c) and year (δ_t) fixed effects. Excluded instruments: Z_ct and Z_ct². Over-identification test: Hansen J, p = 0.41. SEs clustered by province; number of provinces not stated. Weights, software: not stated.

## 4. Formulas

### Formula (4) — first stage

- **Symbols, as written:** `R_ct = π Z_ct + X_ct'ψ + α_c + δ_t + v_ct`
- **Plain English:** enforcement actions per 1,000 firms in city c, year t, explained by the distance × target interaction, the controls, a city constant and a year constant. π measures how much more (or less) enforcement rises with log distance when the national target tightens by one unit. ψ and v_ct are not defined in the paste.
- **If one piece moved:**
  - *Distance in levels instead of logs.* In logs, a move from 50 to 100 km counts as much as 500 to 1,000 km, so differences among near-coast cities carry relatively more of the variation; in levels, differences among far-inland cities would carry more.
  - *Drop α_c.* log(Distance_c) varies only across cities, so α_c is what forces identification onto changes in the distance gradient over time; without it, permanent coastal–inland differences in enforcement would feed into π.
- **Parsing:** `clear`

### Formula (5) — second stage

- **Symbols, as written:** `log(FDI_ct) = β R̂_ct + X_ct'κ + α_c + δ_t + e_ct`
- **Plain English:** log FDI in city c, year t, on the first-stage fitted value of enforcement (R̂_ct), the same controls and FE. β is the change in log FDI per one additional enforcement action per 1,000 firms, using only the part of R_ct predicted by the instruments. κ and e_ct are not defined in the paste.
- **If one piece moved:**
  - *Outcome in levels instead of logs.* β would be an absolute change in FDI, weighting large-FDI cities heavily; in logs it is an approximate proportional change, and city-years with zero FDI drop out or need special handling (not stated).
  - *R_ct per standard deviation instead of per 1,000 firms.* The same β rescaled by the SD of R_ct, which is how the abstract reports it; the SD itself is not stated.
- **Parsing:** `clear`

### Mentioned but not shown

- The second instrument, Z_ct², is described in words but appears in neither (4) nor (5); its first-stage coefficient is not written. Numbering starts at (4); (1)–(3) are neither shown nor cited in this paste.

## 5. Twists vs textbook baseline

- **Baseline used for this note (mine; the paper names none):** a just-identified 2SLS with one excluded instrument that is as-good-as-random conditional on pre-determined controls, with an argued exclusion restriction and a reported first-stage F.
- **Departure the text itself claims:** a second instrument (Z_ct²) added so that over-identification can be tested.
- **Looks different, but the text does not say so:** the instrument has a shift-share-like structure — a fixed local exposure (distance) times a national time series (the target). Identification then rests on how many distinct target changes occur over 2005–2018, which the paste doesn't discuss.

## 6. Assumptions and failure modes

| Assumption | Where stated | If it fails |
|---|---|---|
| Relevance | "The first stage is strong" | Weak instruments bias 2SLS toward OLS and distort SEs; without a number, can't be judged |
| Exclusion | "Hansen J … confirms that the exclusion restriction holds" | β absorbs any direct effect of distance × target on FDI |
| Independence (Z as-good-as-random given X, FE) | required by this estimator, not stated in the paste | β picks up whatever city traits co-move with the distance gradient over time |
| Monotonicity | required by this estimator, not stated in the paste | β is no longer a positively weighted average of complier effects |
| Homogeneous effects (for the named "all cities" estimand) | required by the named estimand, not stated | β describes compliers only |

## 7. Design-specific checks

- **Pieces named:** stated — treatment R_ct, instrument Z_ct (log distance × target), outcome log(FDI_ct), same controls and FE in both stages. Why R_ct is endogenous: stated ("cities attracting more FDI may face different enforcement").
- **Level of variation:** Distance_c varies by city, Target_t only by year, so the identifying "shocks" are the year-to-year changes in one national target — at most 14 years (my calculation, from the handoff's 2005–2018). Whether that is enough independent variation is not discussed.
- **Estimand:** finding — named as an all-cities average; design-implied is a weighted LATE (section 1a).
- **Relevance:** "strong" with no number — not stated in the design file's sense.
- **Exclusion:** finding — the only evidence is the J test, and Z_ct and Z_ct² come from the same variable, so they share any exclusion violation; J's non-rejection (p = 0.41) says almost nothing about validity. Channels worth asking about, as questions: Could the coastal–inland FDI gap change over these years for reasons that track the national target (trade costs, inland development policy)? Could tighter targets reach FDI through regulatory tools other than enforcement actions (permits, closures, energy prices), which R_ct doesn't count?
- **Instrument type (geography × policy rule):** distance is pre-determined (time-invariant), stated by construction. Whether the target affects FDI directly, not only via enforcement, is not discussed.
- **Inference:** stated — clustered by province, which is above the city level at which Z varies.
- **Abstract red flags:** "on average across all cities" → mismatch confirmed (1a). "Overturning … prior work" → no OLS estimate or comparison in the paste; whether IV and OLS target the same population is not discussed.
- **Controls (outside the checklist):** log GDP, population and road density are time-varying and could themselves respond to regulation or FDI; whether they're pre-determined is not stated.
- **Denominator (outside the checklist):** R_ct is per 1,000 firms; if FDI brings in new firms, the denominator moves with the outcome. Not discussed.
- **Not stated:** first-stage F or effective F; weak-instrument-robust inference; first-stage sign and sample; balance or placebo evidence on Z; placebo outcomes; falsification samples (e.g. pre-target years); sensitivity to exclusion violations; monotonicity; complier description; number of clusters.

## 8. Reproducibility checklist

| Item | Status | Pointer |
|---|---|---|
| Outcome defined | stated (partly) | log(FDI_ct); FDI measure and zeros not stated |
| Treatment / key variable defined | stated | "count of environmental enforcement actions per 1,000 firms" |
| Sample rule | not stated | 280 cities from handoff; inclusion rules absent |
| Time window | stated in handoff only | 2005–2018 |
| Estimator named | stated in handoff | "Two-stage least squares"; (4)–(5) in Methods |
| Uncertainty (SEs, clustering, intervals) | stated | "clustered by province"; cluster count not stated |
| Validation of any constructed measure | n.a. | R_ct is a count, not a model-built measure |
| Software / code | not stated | — |
| Data availability | not stated | — |

## 9. Answers to handoff questions and open questions

### 9a. Answers to handoff questions

1. **What evidence supports exclusion beyond the J test?** None in the paste. The J test compares Z_ct with Z_ct², which share their exclusion risk (section 7). No placebo outcome, no falsification sample, no sensitivity analysis and no substantive argument about other channels appears.
2. **Is β a LATE, and for whom?** Design-implied, yes: a weighted average of local effects for cities whose enforcement count responds to the distance × target interaction, valid only under monotonicity (not stated). The paper names it an average "across all cities" instead (1a). Who the compliers are is not described in the paste.
3. **How strong is the first stage?** Not stated as a number — only "The first stage is strong." Neither π, its SE, nor any F statistic is reported.

### 9b. Open questions

1. What is the first-stage F (or effective F with province clustering), and the sign and size of π?
2. Is there any reduced-form placebo — years before targets existed, or cities where targets didn't bind — that would support exclusion?
3. Does the paper argue homogeneous effects or describe the compliers? If not, can the "all cities" wording be supported?
4. How many distinct values or changes does Target_t take over 2005–2018?
5. What is the OLS estimate that the IV result is said to "overturn"?
