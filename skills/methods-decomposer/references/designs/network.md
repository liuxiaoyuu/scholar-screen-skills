# Network analysis (ERGM, diffusion, peer effects, network regressions)

Read this when ties between units matter: "network", "ties", "ERGM", "centrality", "diffusion", "contagion", "peer effects", "neighbours", "spatial lag", "co-sponsorship", "policy learning".

Answer every question as **stated: <pointer>**, **not stated**, or a short finding.

---

## 1. Name the pieces

| Piece | What to extract |
|---|---|
| Nodes | What a node is (person, agency, city) and how the node set is bounded |
| Ties | How a tie is defined: threshold, time window, direction, weight, data source |
| Completeness | Complete network or sampled / partial (capped name generators, scraped lists, API limits) |
| Question type | Network formation (why ties form), network effects (how ties affect outcomes), or description |

## 2. Network construction

- Is the **boundary specification** argued (why these nodes and not others)?
- Ties built from documents, co-occurrence or interactions: what counts as a tie, and how sensitive are results to that threshold?
- Missing ties or nodes discussed? Network statistics (centrality, clustering) can be badly biased by missing data.

## 3. Dependence and inference

- Network observations aren't independent: a dyad (A,B) shares nodes with (A,C). Standard OLS/logit SEs on dyads or nodes are usually too small.
- What accounts for dependence? **ERGM** or **SAOM** (models of the whole network), **QAP** permutation tests, dyadic-robust or multi-way clustered SEs, or nothing?
- **ERGM:** terms listed (edges, reciprocity, transitivity/GWESP, homophily on attributes)? Convergence and **degeneracy** diagnostics? **Goodness-of-fit** plots comparing simulated and observed degree, edgewise-shared-partner and geodesic distributions?

## 4. Network effects: influence vs homophily vs shared environment

The core identification problem in network effects:

- **Homophily:** similar units connect, so connected units look alike even without influence.
- **Shared environment / common shocks:** connected units face the same conditions (same province, same central directive).
- **Reflection problem:** in linear-in-means models, the group's average outcome and the individual's outcome are determined together.

What design does the paper use to separate influence? Random assignment of ties or peers, timing (adoption after a tie forms), instruments for peers' behaviour, exogenous shocks to some nodes, or none? If none, write the estimand as an association along ties.

## 5. Diffusion specifically

- Is diffusion (adoption spreading over ties) separated from **common exposure** (everyone reacting to the same central signal at slightly different speeds)?
- **Event-history / hazard models:** is the risk set defined correctly (units drop out after adopting)? Time-varying network exposure measured before adoption?
- Could **ties be a result of adoption** (cities that adopt start collaborating)? Ties measured before or after?
- Multiple tie types (geography, trade, official rotation, ideology) compared — and is "learning" claimed from one of them without ruling out the others?

## 6. Abstract red flag → what to verify in Methods

| Abstract says | Check in Methods |
|---|---|
| "connected units are more likely to adopt" + "policy learning" | Homophily and common-shock controls; timing of ties |
| "network position matters more than X" | Is this a horse race of predictors (association) or an identified effect? |
| "using an ERGM we find…" | GOF and degeneracy diagnostics; term specification |
| Ties built from co-mention in documents | Tie threshold sensitivity; what co-mention captures |

## 7. Good vs weak write-ups (invented)

**Weaker:** "Cities connected to early adopters are 30% more likely to adopt, showing policy learning."

**Stronger:** "Ties are defined by the rotation of party secretaries between cities before 2010, which is set by the provincial personnel system rather than by cities' policy choices. Conditional on province-year fixed effects (common directives) and similarity in pollution and income (homophily), exposure to adopting former-colleague cities raises the adoption hazard. Placebo ties to cities a secretary was assigned to but never served in show no effect."
