# Fixture C2 — invented Methods paste: LLM-coded measure + OCR damage

> **Fiction.** The paper, model and numbers are invented to test methods-decomposer.

**Handoff packet (from paper-triage)**
- Paper: Measuring Environmental Policy Stringency with Large Language Models
- Claim (as written): "Cities with higher stringency scores file significantly more green patents in subsequent years."
- Design sniff: computational measurement — LLM-coded stringency, then a city-year panel regression
- Red flags to check in Methods: LLM validation; causal language
- Questions for C: (1) How was the LLM score validated against humans? (2) Does the regression support a causal reading?
- Suggested depth: full

**Methods (fictitious)**

*Measurement.* We apply GPT-class model "M-4" (temperature 0) to 48,000 municipal environmental policy documents. The prompt asks the model to rate stringency from 1 (symbolic) to 5 (binding with penalties). We validate the scores on 50 randomly selected documents read by one research assistant and find the labels "highly consistent." City-year stringency S_ct is the mean score of documents issued by city c in year t.

We also fit a 20-topic LDA model to the same corpus; we label topics by inspecting top words and select the three "enforcement" topics as controls.

*Estimation.* We estimate

Patents_c,t+1 = μ_c + τ_t + γ S_ct + Σ_k φ_k Topic_k,ct + η_c t + u_ct          (2)

[OCR note from the user: in the PDF the line reads "+ η c t" with c and t on different baselines]

where Topic_k,ct are the selected topic shares and the final term is as in the original. Standard errors are clustered by city. The positive and significant γ proves that stricter environmental policy drives green innovation.
