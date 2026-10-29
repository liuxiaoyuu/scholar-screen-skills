# Methods decomposition (full): <!-- title as printed, or "untitled paste" -->

> **Scope:** <!-- Methods paste | Methods + intro | OA PDF, Methods only -->
> **Design family:** <!-- DID / IV / RDD / synthetic control / text-ML measurement / network / other; can be two -->
> **Parsing:** <!-- clear | uncertain parsing on: … -->
> **Handoff from paper-triage:** <!-- yes (handoff_version 1 | older bullets) / no -->

Do not add a formula, a sample size, a standard-error choice or a causal claim that the source does not contain. Write `not stated` instead.

## 0. Contract (intro / abstract)

- **Question:**
- **Design in one sentence:**
- **Data (as named):**
- **Claim strength:** <!-- association vs causal; local vs general -->

<!-- If no intro was pasted: "Contract incomplete — only Methods supplied." -->

## 1. Identification map

| Element | From the text |
|---|---|
| Source of variation | |
| Identifying assumptions (stated) | |
| Estimand | |
| Estimator | |
| Threats (stated / not discussed) | |

### 1a. Estimand ↔ estimator alignment

<!-- One-line verdict: "aligned as stated" | "misaligned: <reason>" | "can't tell from paste: <what's missing>". Then at most three lines. In Chinese the heading is "目标量 ↔ 估计量对齐". -->

## 2. Data and sample

- **Units:**
- **Time:**
- **Inclusion / exclusion:**
- **Treatment / key variable definition:**
- **Outcome definition:**
- **Source, as named:**
- **Size:** <!-- only if printed -->

## 3. Estimation / model

<!-- Estimator name if given; controls, fixed effects, weights, SE / clustering, software. If only a formula appears, say the estimator is never named. -->

## 4. Formulas

### Formula <!-- n --> — <!-- role -->

- **Symbols, as written:**
- **Plain English:**
- **If one piece moved:**
- **Parsing:** `clear` | `uncertain parsing` — <!-- fragment -->

### Mentioned but not shown

<!-- Equation numbers cited but not displayed; "None" otherwise. -->

## 5. Twists vs textbook baseline

- **Baseline used for this note:** <!-- and whether the paper named it -->
- **Departure the text itself claims:**
- **Looks different, but the text does not say so:**

## 6. Assumptions and failure modes

| Assumption | Where stated | If it fails |
|---|---|---|

<!-- Rows only for stated assumptions, plus rows marked "required by this estimator, not stated in the paste". -->

## 7. Design-specific checks

<!-- From references/designs/<family>.md: each substantive item "stated: <pointer>" or a finding; group all plain "not stated" items into one final line. -->

## 8. Reproducibility checklist

| Item | Status | Pointer |
|---|---|---|
| Outcome defined | stated / not stated | |
| Treatment / key variable defined | stated / not stated | |
| Sample rule | stated / not stated | |
| Time window | stated / not stated | |
| Estimator named | stated / not stated | |
| Uncertainty (SEs, clustering, intervals) | stated / not stated | |
| Validation of any constructed measure (coding, ML, LLM) | stated / not stated / n.a. | |
| Software / code | stated / not stated | |
| Data availability | stated / not stated | |

## 9. Answers to handoff questions and open questions

### 9a. Answers to handoff questions

<!-- Only if a paper-triage handoff packet was given: answer each question from the paste, pointing to the section above. Otherwise delete 9a. -->

### 9b. Open questions

<!-- Questions only, no guessed answers. Put first the ones that would change section 1. -->

## 10. Reuse card

<!-- Include only when the user has said what they're working on (in chat or as "Reader's goal" in the handoff); otherwise delete this whole section. -->

- **Transferable trick:** <!-- the one design/measurement move worth borrowing -->
- **What it would need in my setting:** <!-- data, variation, validation -->
