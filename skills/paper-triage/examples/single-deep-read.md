> **Invented example.** The papers, numbers and abstracts are fictional; they exist only to show the skill's output.

**User:** Should I read this?

> **Carbon Markets and Firm Emissions: Evidence from China's Staggered Pilot Rollout**
> We study how regional emissions trading pilots affect industrial emissions. Pilots began in seven provinces between 2013 and 2016. Using a firm-level panel of 12,400 manufacturing firms (2008–2019), we exploit the staggered timing of pilot launches and estimate group-time average treatment effects that are robust to heterogeneous effects. Pilots reduced covered firms' CO2 intensity by 9%, with no detectable pre-trends; effects grow over time and are concentrated in firms with prior energy audits.

---

**paper-triage:**

## Verdict: deep-read  ·  confidence: high

**One-line why:** A causal claim scoped to covered firms, backed by a staggered rollout and an estimator built for heterogeneous effects. That is the design you'd want for this question.

**Scores:** claim 2 · design 2 · relevance 2 (topic 1 + method 1) · payoff 2 = 8/8  (judged against: default social-science lens)

**Claim:** Emissions trading pilots "reduced covered firms' CO2 intensity by 9%" (abstract sentence 4). The language is causal and local: it applies to covered firms in pilot provinces, not to all firms. Two secondary claims: the effect grows over time, and it is concentrated in firms with prior energy audits (sentence 4, second half). The energy-audit split is heterogeneity, not a mechanism the design identifies.

**Design sniff:** `quasi-experimental`. Covered firms are compared with not-yet-treated or never-treated firms across the 2013–2016 staggered pilot launches, using group-time ATTs instead of plain two-way fixed effects.

**Red flags / unknowns:**
- "No detectable pre-trends": check what evidence is offered and whether insignificant leads are treated as proof (待核). I'm treating this as something to check rather than a cap on the design score, because the abstract already names a heterogeneity-robust estimator.
- Comparison group not in abstract: are covered firms compared with uncovered firms in the same pilot provinces (risk of leakage and spillover) or with firms in non-pilot provinces?
- How firms became "covered" is not stated. If coverage depends on a size or emissions threshold, selection into coverage needs an argument (待核).
- Inference with only seven treated provinces: the clustering level and the number of treated clusters are 待核.
- The estimand is the ATT for covered firms in the pilots. Don't read it as the effect of a nationwide market.

**Next action:** Deep-read. Start with the data section (what "covered" means and who the comparison firms are), then the event-study figure and the pre-trend evidence, then the energy-audit heterogeneity. Want me to package this as a handoff for `methods-decomposer`?

Tell me what you're working on and I'll re-judge relevance for it.
