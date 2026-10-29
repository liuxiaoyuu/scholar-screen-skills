> **Invented example.** The papers, numbers and abstracts are fictional; they exist only to show the skill's output.

**User:** Triage these five

> **1. Carbon Markets and Firm Emissions: Evidence from China's Staggered Pilot Rollout**
> We study how regional emissions trading pilots affect industrial emissions. Pilots began in seven provinces between 2013 and 2016. Using a firm-level panel of 12,400 manufacturing firms (2008–2019), we exploit the staggered timing of pilot launches and estimate group-time average treatment effects that are robust to heterogeneous effects. Pilots reduced covered firms' CO2 intensity by 9%, with no detectable pre-trends; effects grow over time and are concentrated in firms with prior energy audits.
>
> **2. Measuring Environmental Policy Stringency with Large Language Models**
> We construct a new measure of local environmental policy stringency by applying a large language model to 48,000 municipal policy documents (2010–2022). The LLM scores each document on a 1–5 stringency scale. Cities with higher stringency scores file significantly more green patents in subsequent years. Our measure opens new possibilities for studying policy design at scale.
>
> **3. A Synthetic Difference-in-Differences Estimator for Monetary Policy Transmission**
> We propose a modified synthetic difference-in-differences estimator that accommodates multiple treated units with different adoption dates and time-varying covariates. We prove consistency under a factor-model structure and show in simulations that it reduces bias by up to 40% relative to standard two-way fixed effects. We apply it to euro-area bank lending after national macroprudential policy changes.
>
> **4. Social Media Use Causes Political Polarization: Survey Evidence**
> Using a cross-sectional survey of 3,000 adults, we show that heavier social media use causes greater affective polarization. We control for a rich set of demographic and political confounders. The effect is large and robust, implying that regulating platforms would substantially reduce polarization nationwide.
>
> **5. Dietary Fibre and Gut Microbiome Diversity in Laboratory Mice**
> We randomly assigned 120 mice to high- or low-fibre diets for eight weeks and measured gut microbiome diversity. High-fibre diets increased Shannon diversity by 0.6 units. Results suggest fibre-mediated microbial pathways relevant to metabolic health.

---

**paper-triage:**

| # | Paper (short title) | Verdict | Total | Relevance | Conf. | One-line why |
|---|---|---|---|---|---|---|
| 1 | Carbon markets & firm emissions | deep-read | 8/8 | 2 | high | A staggered pilot rollout with a heterogeneity-robust estimator backs a causal claim scoped to covered firms. |
| 3 | Synthetic-DID estimator | methods-only | 7/8 | 2 | high | The estimator is the contribution, with a proof, simulations and a real application, but it is benchmarked only against plain TWFE. |
| 2 | LLM policy-stringency measure | methods-only | 6/8 | 2 | high | The measure is the contribution, and the abstract mentions no validation of the LLM scores (待核). |
| 4 | "Social media causes polarization" | skip (weak design) | — | 1 | high | It claims "causes" from one cross-section with controls only. |
| 5 | Mice and dietary fibre | skip (off-topic) | — | 0 | high | Lab biology, not social science. |

- Start with #1: it has the clearest claim and the design that best matches it, and a credible design on an important question pays off for most social-science readers.
- One override: #1 keeps design 2. "No detectable pre-trends" is something to check in Methods (待核), not a flaw stated in the text. #3 sits above #2 only on total (design and relevance are tied).
- I judged relevance against the default social-science lens. Tell me what you're working on and I'll re-rank.
- Should I expand any of these in single mode, or package #1, #3 or #2 as a handoff for `methods-decomposer`?

---

**User:** I'm writing about the effects of China's environmental policies — re-rank.

---

**paper-triage:**

| # | Paper (short title) | Verdict | Total | Relevance | Conf. | One-line why |
|---|---|---|---|---|---|---|
| 1 | Carbon markets & firm emissions | deep-read | 8/8 | 2 | high | It estimates the effect of a Chinese environmental policy (the ETS pilots) on firms, with the staggered design your topic often needs. |
| 2 | LLM policy-stringency measure | methods-only | 6/8 | 2 | high | It offers a reusable policy-intensity measure for studying policy effects; the abstract never says which country's municipalities it covers (待核). |
| 3 | Synthetic-DID estimator | methods-only | 6/8 | 1 | high | Euro-area bank lending is off your topic, but the estimator fits staggered pilot rollouts like China's. |
| 4 ↔ | "Social media causes polarization" | skip (off-topic) | — | 0 | high | Neither the topic nor the method serves your goal, and the design is weak anyway. |
| 5 | Mice and dietary fibre | skip (off-topic) | — | 0 | high | Unrelated to environmental policy. |

- What moved: no verdict changed, so no row is marked ↑ or ↓. #3's topic drops to 0 (euro-area banking), so #2 moves above it on relevance. #4's skip reason changes from weak design to off-topic (↔).
- Start with #1. It is directly on your question, and its event-study and comparison-group choices are templates you can reuse.
- #2 doesn't say which country it covers; that's an unknown to check, but it wouldn't change the verdict.
- I judged relevance against your goal: "the effects of China's environmental policies".
- Which of #1, #2 or #3 should I package as a handoff for `methods-decomposer`?
