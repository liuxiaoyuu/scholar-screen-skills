# Text-as-data, ML and LLM measurement

Read this when a key variable — treatment, outcome or control — is **constructed by a model**: dictionaries, topic models, embeddings, supervised classifiers, LLM annotation or scoring, image or audio models, network inference from text. Often paired with another design file (a DID whose outcome is LLM-coded; a panel regression on an ML-built index).

Answer every question as **stated: <pointer>**, **not stated**, or a short finding.

---

## 1. Name the measurement pipeline

| Step | What to extract |
|---|---|
| Corpus | Which documents/images/posts, from where, which years, how collected |
| Unit of measurement | Document, sentence, user, city-year (and how documents aggregate to it) |
| Construct | What concept the measure is supposed to capture, in the authors' words |
| Method | Dictionary / topic model / embedding / supervised classifier / LLM prompt / other |
| Output | Label, score, share, probability — scale and range |
| Validation | Against what, by whom, on how many items, with which metric |
| Downstream use | Which regression or analysis uses it, and as what (X, Y, control) |

## 2. Construct validity

- Is the construct **defined before** seeing model output (codebook, rubric), or are labels assigned afterwards ("we label topic 7 'enforcement' after inspecting top words")? Post-hoc labels that then become findings are a red flag.
- Does the measure capture the construct or a proxy that's easier to see (e.g. "stringency" measured as the number of penalty words)?
- Could the measure pick up **writing style, document length, genre or language** rather than substance? Any controls or checks for that?

## 3. Validation against people

- **Gold standard:** a hand-coded set? Size, how sampled (random? stratified?), who coded it (trained coders? authors? one RA?), blind to model output?
- **Agreement:** among human coders (Krippendorff's α, Cohen's κ) and between humans and the model. "Highly consistent" without a number is **not stated**.
- **Performance metrics** on held-out data: accuracy, F1, precision/recall **per class** (aggregate accuracy hides failures on rare classes); for scores, correlation or mean absolute error against human scores.
- **Subgroup validity:** does performance hold across years, regions, languages, document types? Measurement error that varies with treatment or outcome is much worse than uniform noise.
- **External validation:** correlation with an independent measure of the same construct (survey, administrative data, expert rating)?

## 4. LLM annotation specifically

- Model name, **version or date**, prompt (in an appendix?), temperature/decoding settings, and whether the model could have seen the documents in training.
- **Prompt sensitivity:** results under alternative wordings, label orders or models?
- **Reproducibility:** closed models change over time — any archived outputs?
- **Few-shot examples:** where from, and were they excluded from validation?

## 5. Measurement error and downstream bias

- Model-built variables contain error. **Using predicted labels as if they were true** in a regression can bias coefficients and understate uncertainty — even with high accuracy, if errors correlate with other variables.
- What does the paper do?
  - Nothing (LLM/ML labels treated as ground truth)
  - Uses the gold set to correct downstream estimates — e.g. **design-based supervised learning (DSL)**, **prediction-powered inference**, or other measurement-error corrections
  - Sensitivity analysis with alternative measures
- As X: classical noise attenuates the coefficient; non-classical error can bias it either way. As Y: noise inflates variance; error correlated with X biases the estimate. State which role the measure plays; don't claim a direction unless the text supports it.

## 6. Topic models and unsupervised methods

- How was K (number of topics) chosen? Stability across K and random seeds?
- Who labelled the topics, and were labels decided before the analysis that uses them?
- Topic shares used as regressors carry estimation uncertainty — acknowledged?
- **Same-source controls:** controls built from the same corpus as the key regressor may measure part of the same thing.

## 7. Supervised classifiers

- Training data source and size; class balance.
- **Leakage:** could features encode the outcome or post-outcome information? Train/test split by time or unit when the downstream analysis is over time or across units?
- Was the classifier tuned on the same data used to evaluate it?

## 8. Corpus and selection

- What's missing: deleted posts, censored content, untranslated documents, paywalled sources, non-digitised years?
- Does **selection into the corpus** relate to the outcome (e.g. only cities that publish policies online)?
- Preprocessing stated: tokenisation, stopwords, stemming; **Chinese word segmentation** method; handling of multiple languages.

## 9. Abstract red flag → what to verify in Methods

| Abstract says | Check in Methods |
|---|---|
| "we use an LLM to score/classify N documents" | Validation set, agreement metric, downstream correction |
| "a new measure of X" + "X predicts Y" | Construct validity; whether X and Y share measurement artefacts |
| "topics reveal…" | Who labelled topics, when; stability |
| "using millions of posts" | Who's in the data; generalisation claims |

## 10. Good vs weak write-ups (invented)

**Weaker:** "We apply an LLM to 48,000 policy documents to rate stringency from 1 to 5. A research assistant checked 50 documents and found the labels highly consistent. We then regress patents on city-level mean stringency."

**Stronger:** "Two trained coders labelled a stratified random sample of 600 documents using a pre-registered rubric (α = 0.78). Against this gold set the LLM achieves a weighted κ of 0.71, stable across years and provinces. We archive prompts and outputs. Downstream regressions use DSL to correct for prediction error, and results hold with a dictionary-based alternative measure."

## 11. What not to claim

- Don't assume a measure is invalid because it's model-built — ask how it was validated.
- Don't claim the direction of measurement-error bias without knowing its structure.
