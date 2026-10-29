> **Invented example.** The papers, numbers and abstracts are fictional; they exist only to show the skill's output.

**User:** Is this worth reading?

> **Coastal Distance, Environmental Regulation, and Foreign Investment in Chinese Cities**
> Do stricter environmental regulations deter foreign direct investment? We study 280 Chinese prefecture-level cities from 2005 to 2018. Because regulation stringency is endogenous to investment, we instrument it with each city's distance to the coast interacted with national ventilation-based pollution targets. Two-stage least squares estimates show that a one-standard-deviation increase in stringency reduces FDI inflows by 12% on average across all cities, overturning the "pollution haven" scepticism in prior work.

---

**paper-triage:**

## Verdict: deep-read  ·  confidence: high

**One-line why:** An important question with a named IV design, but read it critically: the instrument has an obvious direct channel to FDI, and the estimate is oversold as an effect for every city.

**Scores:** claim 2 · design 1 · relevance 2 (topic 1 + method 1) · payoff 1 = 6/8  (judged against: default social-science lens)

**Claim:** "A one-standard-deviation increase in stringency reduces FDI inflows by 12% on average across all cities" (abstract sentence 4). The language is causal and general ("on average across all cities"), and the abstract claims it overturns prior pollution-haven scepticism.

**Design sniff:** `quasi-experimental`. Regulation stringency is instrumented with distance to the coast interacted with national ventilation-based pollution targets, and the paper compares FDI across cities whose stringency is shifted by that instrument (2SLS).

**Red flags / unknowns:**
- **Red flag:** distance to the coast plausibly affects FDI directly, through trade costs, ports, market access and income. That gives a clear exclusion hook, so design is capped at 1. Check whether the uninteracted distance term and city fixed effects absorb this channel (待核).
- **Red flag:** the 2SLS estimate is sold as an effect "on average across all cities". 2SLS gives a LATE for complier cities. Check monotonicity and who the compliers are.
- **Red flag:** "overturning" prior work. The design has to carry a claim that strong.
- Unknown: first-stage strength is not reported in the abstract (待核).
- Unknown: how "regulation stringency" is measured is not in the abstract.

**Next action:** Deep-read, starting with the identification section: the exclusion argument for coastal distance, the first-stage F, and any placebo or falsification tests. Then decide whether the 12% figure survives. Want me to package this as a handoff for `methods-decomposer`?

Tell me what you're working on and I'll re-judge relevance for it.

---

**User:** give me the handoff

---

**paper-triage:**

```yaml
# handoff to methods-decomposer
handoff_version: 1
paper: "Coastal Distance, Environmental Regulation, and Foreign Investment in Chinese Cities"
verdict: deep-read
confidence: high
abstract: |
  Do stricter environmental regulations deter foreign direct investment? We study 280 Chinese prefecture-level cities from 2005 to 2018. Because regulation stringency is endogenous to investment, we instrument it with each city's distance to the coast interacted with national ventilation-based pollution targets. Two-stage least squares estimates show that a one-standard-deviation increase in stringency reduces FDI inflows by 12% on average across all cities, overturning the "pollution haven" scepticism in prior work.
claim: "A one-standard-deviation increase in environmental regulation stringency reduces FDI inflows by 12% on average across all cities (abstract sentence 4; causal, stated as general)."
design_sniff: "quasi-experimental — 2SLS instrumenting regulation stringency with coastal distance × national ventilation-based pollution targets across 280 cities."
red_flags:
  - "Exclusion: coastal distance plausibly affects FDI directly (trade costs, ports, market access, income)."
  - "LATE sold as an average effect 'across all cities' — check monotonicity and who the compliers are."
  - "'Overturning' prior work — strong claim resting on one instrument."
unknowns:
  - "First-stage strength (F-statistic) not reported in the abstract."
  - "How regulation stringency is measured."
  - "Whether the uninteracted coastal-distance term and city / year fixed effects are included."
questions:
  - "Once the main effect of coastal distance and city fixed effects are controlled, does identification come only from the interaction with national targets? If so, what makes that interaction excludable?"
  - "How strong is the first stage, and do placebo or falsification tests (e.g. pre-period FDI, non-pollution-sensitive sectors) support exclusion?"
  - "Which cities are the compliers, and how far does the 12% LATE generalise to 'all cities'?"
depth: quick
data: "280 Chinese prefecture-level cities · 2005–2018 · N not stated"
reader_goal: "not stated"
```
