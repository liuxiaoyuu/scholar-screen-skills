# Default lens: a social-science reader

Used when the reader hasn't said what they're working on. It answers two questions for the **relevance** score: is the topic social science, and is the method one a social scientist should know?

## Topic counts as social science (topic = 1)

Studies people, groups, organisations, institutions, policies, markets, media or societies, in any of:

- Economics (incl. development, labour, public, environmental, health, urban)
- Political science and international relations
- Sociology and demography
- Public policy, public administration, governance
- Communication and media studies
- Social psychology and behavioural science (field or survey settings)
- Education, criminology, social work
- Computational social science (social questions studied with digital data)
- Human geography, planning, interdisciplinary environment–society work

Borderline (judge case by case): public health with a behavioural or policy angle (yes), management/business (yes if about organisations or markets), law (yes if empirical), history (yes if it makes a social-science argument).

Not social science (topic = 0): lab biology and medicine without a social or policy angle, pure engineering, pure mathematics, physical sciences.

## Method counts as worth knowing (method = 1)

**Causal / quasi-experimental:** randomised experiments (field, survey, lab with social outcomes), difference-in-differences and event studies, synthetic control, instrumental variables, regression discontinuity, matching / weighting with a credible design argument.

**Measurement and description done carefully:** representative surveys, panel data, administrative / register data, careful descriptive work that establishes a new fact.

**Computational:** text-as-data (topic models, embeddings, supervised classification), LLM annotation with validation, network analysis (ERGM, diffusion, SAOM), machine learning for measurement or prediction, geospatial analysis, agent-based models.

**Qualitative and mixed methods:** process tracing, comparative case studies, interviews/ethnography with a clear analytic strategy.

A method scores 0 when it's only a routine regression with controls and no design argument, or when the paper doesn't describe a method at all.

## Worked examples (invented papers)

**Topic = 1**
1. Minimum-wage changes and teen employment across counties.
2. How ministries coordinate climate policy, from inter-agency documents.
3. Social media exposure and voters' trust in elections (survey experiment).
4. Air-quality disclosure rules and household mask purchases.
5. A new estimator for staggered DID, **applied to** provincial environmental policy — the application is social science.

**Topic = 0**
1. Gut microbiome diversity in mice on high-fibre diets.
2. A battery chemistry that extends cell life by 20%.
3. A faster graph-matching algorithm benchmarked on synthetic graphs, with no social application.
4. Protein-folding prediction with a new neural architecture.
5. A pure econometric-theory proof with no application. (Topic 0, but method can still be 1 — that's a `methods-only` candidate.)

**Method = 1**
1. Staggered DID with a heterogeneity-robust estimator.
2. Regression discontinuity at an eligibility threshold.
3. LLM annotation of policy documents validated against hand-coding.
4. ERGM on an inter-agency coordination network.
5. A nationally representative panel survey establishing a new descriptive fact.

**Method = 0**
1. Cross-sectional OLS with controls and causal claims.
2. "We find a significant correlation" with no data or method described.
3. An opinion piece or commentary.
4. A case narrative with no stated analytic strategy.
5. Rankings or indices built with undisclosed weights.

## Payoff hints for a general reader

Higher payoff: a new data source or measure others can reuse; a credible design on an important question; a result that overturns or sharpens a well-known claim (with the design to back it); a clear methods contribution with a real application.

Lower payoff: small extensions of a familiar result; descriptive work on a narrow sample with broad claims; methods tested only on synthetic data against weak baselines.
