---
name: methods-decomposer
description: >-
  Use when the user pastes a paper's Methods section or formulas and asks what
  it actually identifies ("这篇方法到底怎么识别的", "帮我拆一下这段 Methods",
  "what does this paper identify", "is this design believable"), or hands off a
  paper from paper-triage. Signature move: an identification map with an
  estimand ↔ estimator alignment check, then each formula in three layers and
  design-specific checks (DID, IV, RDD, synthetic control, text/ML, networks,
  panel FE). Quick or full depth. Never invents an equation. Concepts to learn
  go to pop-explainer (separate skill).
---

# Methods decomposer

> Read this file first. Open `references/designs/<family>.md` and `templates/decomposition.md` only at the step that names them.

Break down **one paper's empirical strategy** so a researcher can
follow and judge the design. Read the intro as a **contract**, map
**identification** before drowning in estimators, and stay inside the text the
user supplied. A hole in that text stays a hole.

Method names (LATE, parallel trends, exclusion restriction …) are vocabulary,
not citations. Don't invent quotations, page numbers or attributed sayings.

## Inputs

| Input | Rule |
|---|---|
| Methods text | Preferred. Local paste. |
| Formulas | Part of the paste. Undefined symbols → say so. |
| Intro / abstract | Optional; used for the contract. If absent, say the contract is incomplete. |
| Open-access PDF | Only if the user supplies the file or link and asks. Read Methods (+ appendices they point to). |
| Handoff packet from `paper-triage` | Optional. Accept the YAML block (`handoff_version: 1`: paper, verdict, confidence, abstract, claim, design_sniff, red_flags, unknowns, questions, depth, optional data / reader_goal / reopen_trigger) or the older Markdown bullet list — same content, map by meaning. Start from its claim, design sniff, red flags, unknowns and **questions for methods-decomposer** — answer those questions explicitly in the output. Use its suggested depth unless the user overrides. The abstract / intro inside the packet counts as the contract source (mark facts "from handoff"); its data facts and reader's goal can be used too, including for "(my calculation)" arithmetic. If the packet's title or claim clearly doesn't match the Methods paste, ask before decomposing. |
| Textbook baseline | Optional. If unnamed, state a one-sentence baseline and label the comparison as **yours**. |

No paste and no OA file → ask for the Methods paste. Never scrape a paywall or
hunt for "the" paper.

**Failure path — no Methods in the paste.** If the user supplies only a
results table, coefficients, a figure caption or an abstract, don't
reconstruct the design from it. Say what you can read off (e.g. "the table
reports a coefficient on Treat×Post with province FE"), say what's missing, and
ask for the minimum paste: "the paragraph that defines the treatment and the
estimating equation" (usually the first page of the Methods / empirical
strategy section).

## Step 1 — Inventory and choose depth

1. Inventory the paste: which formulas are fully on the page, which are cited
   by number but missing, which sections of the skeleton can be filled at all.
2. **Detect the design family** and read the matching file(s) in
   `references/designs/` before writing: `did.md`, `iv.md`, `rdd.md`,
   `synthetic-control.md`, `text-ml-measurement.md`, `network.md`, and
   `panel-fe.md` for a plain panel / fixed-effects regression with no named
   quasi-experiment. A paper can need two (e.g. DID on an LLM-coded outcome,
   or an LLM measure fed into a panel regression).
3. **Choose depth:**
   - **quick** — the user wants to know "what does it identify and is it
     believable"; short paste; or the handoff says quick.
   - **full** — the user wants to follow, replicate or borrow the design; or
     the handoff says full. When unsure, do quick and offer full.
   - **Who wins:** the user's own words in this message beat the handoff's
     `depth` ("quick read on this?" → quick, even if the handoff says full).
     Mention the other depth is available in one line.

## Step 2 — Build the identification map first

From the text only:

| Element | Fill from the text |
|---|---|
| Source of variation | Quote, or "not claimed" |
| Identifying assumptions | As stated |
| Estimand | **Named:** what the text says it targets. **Design-implied:** what the design as written delivers (ATT, LATE at compliers, effect at a cutoff …), labelled "my reading" when it differs from the named one. |
| Estimator | What they actually compute |
| **Estimand ↔ estimator alignment** | Does the estimator, as written, deliver the stated estimand under the stated assumptions? Name the specific mismatch if the design file flags one (e.g. TWFE with staggered timing); otherwise "aligned as stated" or "can't tell from paste". |
| Threats | Three kinds: **addressed** by the authors · **mentioned but not treated as a threat** (e.g. a second policy at the same cutoff noted in passing) · **not discussed** |

Separate **design** from **regression**: a coefficient is not automatically an
identification strategy. If the text makes no causal claim, write "no causal
claim is stated" and don't upgrade it.

## Step 3 — Formulas, three layers each

For every displayed formula (skip none; don't create blocks for formulas only
mentioned):

1. **Symbols as written** — copy exactly; keep indices, hats, signs. Don't
   normalise notation or add an error term, a normalisation or a threshold
   "because that's usual".
2. **Plain English** — what quantity it defines or estimates. A symbol the text
   never defines → "undefined in the paste", not the definition you remember.
3. **If one piece moved** — one or two pieces that are *in* the expression,
   or how they're specified in the text (a polynomial's order, a lag, the
   estimation sample); say how the meaning shifts. No new estimates, no new
   symbols. A different estimator altogether (local linear instead of a global
   polynomial, Callaway–Sant'Anna instead of TWFE) belongs in the
   design-specific checks or open questions, not here.

If the user adds an OCR note that disagrees with the pasted text, copy the
paste as "symbols as written" and quote the OCR reading right next to it.

`Parsing: clear | uncertain parsing` — quote the doubtful fragment (OCR breaks,
ambiguous subscripts, a symbol used two ways). Don't silently repair. If the
ambiguous term is the one you vary in layer 3, describe each candidate reading
conditionally ("if it is a city-specific trend, … ; if it is …") without
choosing one. Cited but absent equations go under **Mentioned but not shown**
— including model pieces described in words but never written out (e.g. "a
second instrument" missing from the first-stage equation); note numbering gaps
or a paste that starts mid-sequence (e.g. (1) then (3), or only (4)–(5)) there
in one line. In quick depth this sub-list sits at the end of **Formulas**.

**What counts as defined:** a symbol is defined if the prose ties it to a
meaning ("the outcome is …" defines Y). Conventional terms the text never
describes (an error term ε, a coefficient θ) get one short "not defined in the
paste" — don't belabour them.

**Your own arithmetic** (31 − 11 = 20 never-treated provinces) is allowed when
it helps, labelled "(my calculation)". Never compute new estimates.

## Step 4 — Write it up

**Length budget.** Quick: about one to one-and-a-half screens (roughly
600–900 words or 1,000–1,500 Chinese characters). Full: about 1,500–2,500
words. Stop adding when the next bullet would only repeat a "not stated" or an
ambiguity already flagged — flag each ambiguity once and point back to it.

**Signature section.** Both depths carry a heading titled exactly
**Estimand ↔ estimator alignment** (Chinese: **目标量 ↔ 估计量对齐**), right
after the identification map, with a one-line verdict — `aligned as stated`,
`misaligned: <reason>`, or `can't tell from paste: <what's missing>` — then
at most three lines of explanation.

**Quick depth** — open with a 1–2 sentence direct answer to the user's
question (what it identifies and the single biggest problem). If no intro was
pasted, add one line: "Only Methods supplied, so the paper's own claim isn't
checked." Then this skeleton:

```markdown
# Methods decomposition (quick): <title or "untitled paste">

> Scope: <Methods paste | + intro | + handoff> · Design family: <…> · Parsing: <clear | uncertain on …>

## Identification map
<the table from Step 2>

## Estimand ↔ estimator alignment
<one-line verdict + up to three lines>

## Data in one line
<units · time · outcome as defined (flag ambiguity) · treatment as defined>

## Formulas
<three-layer block per displayed formula; "none displayed" if none>

## Design-specific checks
<3–5 most important bullets from the design file, each with a finding or
"stated: …"; group the plain "not stated" items into one closing line; plus
at most 2 bullets from the general traps or your own reading of the paste,
labelled "(outside the checklist)">

## Answers to handoff questions   (only if a handoff packet was given)

## Biggest open question
1–3 questions whose answer would change the identification map.

**Bottom line** (only if the user asked whether it's believable): one or two
sentences.
```

In quick depth, skip design-file items that don't apply; in full depth mark
them "n/a". Flag each ambiguity once and point back to it ("see Data")
rather than repeating it. Don't claim a direction of bias (e.g. "τ is an upper
bound") unless the text gives a reason for it.

**Full depth** — open with a 2–3 sentence TL;DR (what it identifies, the
biggest problem, whether the handoff questions are answered), then fill
`templates/decomposition.md`, sections 0–10 in order:
contract, identification map (with the alignment subsection), data, estimation, formulas, twists vs baseline,
assumptions & failure modes, design-specific checks, reproducibility
checklist, answers to handoff questions + open questions, reuse card. Keep
every heading and say why if one doesn't apply — except the **reuse card**,
which you include only when the user has said what they're working on (in
chat, or as `reader_goal` in a handoff) and omit entirely otherwise. In the
design-specific checks, go through every item in the design file but **group
all plain "not stated" items into one line** at the end of the section — never
one bullet per "not stated". Your own observations beyond the design file are
welcome in full depth too; label them "(outside the checklist)".

**Contract sources:** a pasted abstract/intro, or the `abstract` field of a
handoff. An older bullet-style handoff with only a claim → "Contract
incomplete — the handoff gives only the claim". In the threats row, write
"none" for an empty kind rather than stretching a category.

**Contract vs Methods disagree** (e.g. the abstract says "associated with",
the Methods says "proves … drives"): report both, quoted, in section 0 and use
the weaker one unless the design supports the stronger.

## Rules

- **Never invent an equation.** Missing stays missing.
- **Flag, don't repair.** Uncertain parsing is quoted and flagged.
- **No causal upgrade.** Don't promote a regression to IV/DID/RDD because that
  shape often is one.
- **Quote or point.** Substantive statements trace to the paste; a short quote
  beats a paraphrase that adds a step.
- **"Not stated" is an answer** — for sample rules, SEs, software, thresholds,
  validation, disagreement rules.
- **Design-file items are questions, not accusations.** If the paper is silent
  on a trap, write "not stated"; never claim what the authors "must have done".
- **Language.** Answer in the user's language, including section headings and
  all template labels (in Chinese: 识别策略图、数据与样本、公式、范围、解析…) —
  translate labels outright, don't add the English in parentheses. Keep the
  paper's technical terms, estimator names and the stated / not stated status
  words in English, glossing a technical term once. Quote the paste in its original language. If the user
  says the note is for the portfolio, write the whole note in English.
- **Privacy.** Don't store the full pasted Methods in the skill folder, a shared
  digest or a commit; short quotes inside the note the user asked for are fine.
  Don't send the paste to new external services. Restricted microdata →
  describe the design and stop.

## General traps (always worth a glance)

- Many outcomes / bandwidths / specifications → is adjustment or a
  pre-analysis plan stated?
- Clustering level vs the level at which treatment is assigned; number of
  clusters (especially treated clusters) reported?
- Selected samples / attrition → is selection into the observed sample discussed?
- Prediction vs causation → does an importance score get read as an effect?

## Hand-offs

- The user signals they don't understand a concept (LATE, parallel trends …)
  → suggest `pop-explainer` (a separate skill, github.com/liuxiaoyuu/pop-explainer)
  for an intuitive story; don't turn this note into
  a tutorial, and don't add the pointer unprompted.
- The user wants to know whether a paper is worth decomposing at all → that's
  `paper-triage`.

## Not this skill

Estimating the model, filling in missing equations, running code on the
paper's data, writing the paper's results, or literature search.
