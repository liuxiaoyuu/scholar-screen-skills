---
name: paper-triage
description: >-
  Use when the user asks whether a social-science paper is worth reading, or
  wants several abstracts ranked ("这篇值得读吗", "帮我筛一下这几篇", "先看哪篇",
  "should I read this", "triage my inbox"). Scores claim, design, relevance and
  payoff 0–2 from title + abstract, gives a verdict (deep-read / methods-only /
  skim-later / skip) with confidence, and writes a handoff for
  methods-decomposer. No setup needed. Concepts to learn go to pop-explainer (separate skill).
  Never searches databases, invents findings or writes peer reviews.
---

# Paper triage

> Read this file first. Open a file in `references/` only when a step below names it.

A **screen-before-deep-read** pass: decide where the user's reading
hours go. The habit comes from the credible-identification tradition — pull the
claim and the design smell out of the front matter first, and only spend deep
time when claim, identification prospect and relevance to what the reader is
looking for justify it. It's a general tool for any social-science reader — it
needs no profile of the user.

Stay inside the supplied text. A gap in the abstract stays a gap (`待核` /
"not in abstract"). Method names (DID, IV, RDD, LATE …) are vocabulary, not
citations.

## Before you start

1. **Find the reader's goal.** If the user says what they're working on or
   looking for ("I'm writing about minimum wages", "I need DID examples"), that
   is the **goal** — judge relevance against it. If they don't, use the
   **default lens**: a social-science reader who wants credible, useful work
   (see `references/social-science-scope.md`). Don't ask for a goal before
   answering. **Invitation rule:** single paper under the default lens → end
   with one line inviting them to share their goal; batch → mention it once,
   after the table; goal already given → never invite again. Never ask what
   they have already read.
2. **Count the papers.** One paper → single mode. Two or more → batch mode.
3. **Language.** Answer in the user's language. Keep method names, verdict
   labels and the paper's own key terms in English.

## Inputs

Accept, best first: title + abstract (paste) · intro (better for the paper's
"contract") · an open-access PDF or link that loads without login. If the
material is missing, ask for the minimum ("paste the abstract"). Never invent
an abstract, never bypass a paywall, never search for the paper.

## Scoring rubric

Score each paper on four dimensions, 0–2, from the supplied text only.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| **Claim clarity** | Can't tell what is claimed | Claim stated but vague in scope or strength | Clear question + clear claim, strength of language evident |
| **Design credibility** (relative to the claim) | Causal language with no design named, or design contradicts the claim | Descriptive / observational and honest about it, or design named but thin | Named source of variation or validated measurement that matches the claim's strength |
| **Relevance** = topic (0/1) + method (0/1) | Neither topic nor method is relevant | Topic *or* method is relevant (or one reusable piece: data, measure, trick) | Topic *and* method are relevant |
| **Payoff** | Little new: incremental, or the contribution is unclear | Moderate, or can't tell | High: a new question, data source, measure or design others can reuse, or a result that changes how a debate is framed |

**Scoring notes**

- **Several claims** (e.g. a measurement claim and a substantive finding):
  score the paper's main contribution — the measure itself for a measurement
  paper, the finding for a substantive one; mention the others under Claim.
- **Causal language** includes causal framing anywhere in the abstract —
  motivation and conclusion sentences too ("shapes", "drives", "leads to",
  "mechanism", "policy learning") — not only the results sentence.
- **Red flags cap the design score:** a red flag with a clear hook in the
  supplied text (e.g. an instrument that plausibly affects the outcome
  directly, an IV estimate sold as an effect for everyone) caps design
  credibility at 1, even if a design is named. Naming a design is not enough
  for a 2. Routine statements ("no detectable pre-trends", "robust to
  controls") are things to verify in Methods, not hooks; the hook is
  overreach ("pre-trends *prove* parallel trends") or a stated flaw.
- **Deep-read with a capped design:** a paper can reach `deep-read` with design
  = 1 when it is central to the reader's topic; say "read critically: <the
  flaw>" in the one-line why so the verdict isn't mistaken for an endorsement.
- **Pure-methods papers:** score design credibility on the evidence offered for
  the method (proof, simulations, comparison against strong — not only weak —
  baselines, a real application), judged against the headline claim. A claim
  that outruns the evidence ("works in any setting" from synthetic data only)
  caps design at 1. Topic relevance for a pure-methods paper is 1 only if its
  application or target problem is relevant (social science under the default
  lens, or the reader's goal).
- **Relevance under the default lens:** topic = 1 if the paper studies a
  social-science question (people, organisations, institutions, policies,
  markets, media, societies); method = 1 if it uses a social-science design or
  method worth knowing (see the scope file). Papers outside social science
  (lab biology, pure engineering) score topic 0.
- **Relevance with a stated goal:** topic = 1 only if it bears on the goal's
  subject; method = 1 if the method is one the goal needs or names, or the
  paper offers a reusable piece the goal would need (e.g. a policy-intensity
  measure for a study of policy effects).
- **Payoff:** judge from what the front matter claims as new; length is rarely
  stated — don't penalise for it. Default to 1 when unsure.

**Verdict rules** (apply in order):

1. **Veto → `skip`:** relevance = 0 *and* nothing reusable; or claim clarity = 0
   with no way to recover it from what was supplied; or design credibility = 0
   *and* the claim is causal (a cause claimed with no design to back it →
   `skip (weak design)`).
2. **`methods-only`:** method = 1 and topic = 0; *or* the paper's main
   contribution is a method or a measure (pure methods, or a new measure whose
   substantive finding is secondary) and the reader's goal isn't that method
   or measure itself; *or* the design is worth learning but the substantive
   claim doesn't matter to the reader's stated goal — **and**
   design credibility ≥ 1 (a thinly evidenced method is not worth learning
   from; send it to `skim-later`).
3. **`deep-read`:** relevance = 2, design credibility ≥ 1, total ≥ 6.
4. **`skim-later`:** relevance ≥ 1 and total ≥ 4 (this includes relevant papers
   held back by design credibility = 0).
5. Otherwise **`skip`**.

Label skips by reason — `skip (off-topic)` or `skip (weak design)` — because
they mean different things. **Tie-break** between papers with the same verdict:
higher design credibility first, then higher relevance, then higher total,
then the order the user pasted them.

The rubric is a scaffold, not a formula to hide behind: if your judgement
overrides it, say why in one line.

Do not use journal prestige, author fame or citation counts as evidence. In
batch mode you may list the venue if it is in the paste, but it never moves the
score.

## How to read the front matter

1. **Claim.** Question; main claim (short quote or paraphrase + pointer such as
   "abstract sentence 2"); claim strength as written — association vs causal,
   local vs general. Never upgrade the language.
2. **Design sniff.** Label the smell, not a full identification map:
   `quasi-experimental` (a named contrast: policy discontinuity, instrument,
   shock, staggered rollout) · `observational / descriptive` ·
   `computational measurement` (text, image, network, ML-derived variable) ·
   `pure methods` · `review / theory` · `unclear (待核)`. Mentioning "fixed
   effects" or "controls" is regression vocabulary, not a design.
3. **Red flags.** Suspects, not verdicts — flag only when the text gives a hook.
   See `references/red-flags.md` for the econometric and computational lists.
4. **Confidence.** `high` if the abstract/intro states question, data and design;
   `low` if the design, the data, or a fact that decides relevance (e.g. which
   country) must be guessed. Details abstracts normally omit
   (validation statistics, robustness checks, clustering) are red flags marked
   `待核`, not reasons for low confidence. A missing fact that couldn't change
   the verdict either way stays an unknown and doesn't lower confidence. With
   low confidence, name **the one
   paste that would most likely change the verdict** (e.g. "the first paragraph
   of the data section").

## Output — single mode

```markdown
## Verdict: deep-read | methods-only | skim-later | skip  ·  confidence: high | low

**One-line why:** …

**Scores:** claim 0–2 · design 0–2 · relevance 0–2 (topic 0/1 + method 0/1) · payoff 0–2 = total/8  (judged against: your goal "…" | default social-science lens)

**Claim:** … (quote or paraphrase + pointer)

**Design sniff:** <label> — one sentence on the implied comparison

**Red flags / unknowns:**
- …

**To raise confidence, paste:** … (only when confidence is low)

**Reopen when:** … (skim-later only — a concrete trigger, e.g. "you need an example of staggered DID")

**Override:** … (only if you departed from the rubric — one line on why)

**Next action:** … (for deep-read / methods-only, include where to focus, e.g.
"read the measurement and validation sections first")
```

Under the default lens (and only then), add one last line: "Tell me what
you're working on and I'll re-judge relevance for it."

## Output — batch mode

One table, sorted deep-read → methods-only → skim-later → skip, then by the
tie-break rule (skip rows can stay in any order):

```markdown
| # | Paper (short title) | Verdict | Total | Relevance | Conf. | One-line why |
|---|---|---|---|---|---|---|
```

For skip rows write the total as "—": the veto decided them, and a high total
on an off-topic paper only misleads.

Keep each "one-line why" to one sentence; the details belong in single mode.
Then at most five short lines:

1. Which paper to start with and why.
2. Low-confidence rows that need one more paste (leave this line out if none).
3. Any place you overrode the rubric, and why.
4. What relevance was judged against: the reader's goal, or the default
   social-science lens plus a one-time invitation to share their goal.
5. One closing question: which papers to expand in single mode, and/or which
   deep-read / methods-only papers to package as a handoff for `methods-decomposer`.

Reopen triggers for skim-later rows go at the end of their "one-line why"
cell, as "reopen when …".

**Re-ranking** (the user shares a goal after a default-lens batch): restate the
full table, mark rows whose verdict or skip reason changed (↑ / ↓ / ↔ for a
changed skip reason), add one line on what moved and why (including rows that
only changed position), keep the other post-table lines, and drop the "share
your goal" invitation. When both skip reasons apply, use the first veto that
fires (off-topic before weak design).

## Next action and handoff

- `deep-read` / `methods-only` → offer the **handoff packet** for
  `methods-decomposer`. Produce it when the user says yes or asks for it. Use
  this exact block — fixed field order, so people and scripts can parse it:

  ```yaml
  # handoff to methods-decomposer
  handoff_version: 1
  paper: "<title as given>"                      # required
  verdict: deep-read                             # required: deep-read | methods-only | skim-later | skip
  confidence: high                               # required: high | low
  abstract: |                                    # required: verbatim as supplied
    <abstract or intro text>
  claim: "<main claim, quoted or paraphrased>"   # required
  design_sniff: "<label> — <one sentence>"       # required; label from the design-sniff list
  red_flags:                                     # required; [] if none
    - "<suspect to check in Methods>"
  unknowns:                                      # required; [] if none
    - "<what the front matter left out>"
  questions:                                     # required; 2–3 specific questions
    - "<e.g. Is the rollout staggered, and which estimator handles it?>"
  depth: full                                    # required: quick | full
  depth_reason: "<one line>"                     # optional; e.g. "verdict is deep-read but the open question is believability"
  data: "<units · time · N, as named>"           # optional
  reader_goal: "<as stated, or 'not stated'>"    # optional
  reopen_trigger: "<skim-later only>"            # optional
  ```

  **depth:** `full` when the verdict rests on a design or measure the reader
  could reuse, or they want to replicate/borrow it; `quick` when the question
  is mainly "is the claim believable?"

- **User asks for a handoff on a `skim-later` / `skip` paper:** give it — it's
  their reading time. Restate the verdict in one line first, and fill
  "Unknowns to check first" carefully.
- `skim-later` → one reopen trigger ("reopen if you need an example of
  staggered DID", or tied to the reader's goal when stated), then stop.
- `skip` → stop. No free summary unless asked.
- A concept in the abstract the user doesn't know → suggest
  `pop-explainer` (a separate skill, github.com/liuxiaoyuu/pop-explainer) for
  that concept; don't teach it here.

## Hard bans

- **Journal prestige, author fame and citation counts never enter a score.**
- Don't invent findings, samples, coefficients or designs absent from the text.
- Don't search OpenAlex, Google Scholar or any database — this skill screens
  papers the user already has; it doesn't find them.
- Don't write a peer review, a grade or an accept/reject recommendation.
- Don't download, bypass or scrape paywalled text.
- Don't do the Methods decomposition here — hand off to `methods-decomposer`.
