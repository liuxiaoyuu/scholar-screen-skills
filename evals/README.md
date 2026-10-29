# Evals

A small, honest test kit: invented fixtures with known traps, a checklist of what a good answer must catch, and a script for the mechanical checks. It doesn't call a model — you run the skill, save the reply, then check it.

## Files

| File | What it is |
|---|---|
| `fixtures/A-*.md` | Invented abstracts for `paper-triage` (batch of five, batch of three, one vague abstract) |
| `fixtures/C-*.md` | Invented Methods pastes for `methods-decomposer` (staggered DID, IV, RDD, LLM measure with an OCR-damaged formula) |
| `expected.md` | The traps in each fixture and what a good answer must flag. **Don't show it to the model.** |
| `check_outputs.py` | Mechanical checks (Python 3, no dependencies) |

## How to run

1. Install the skills (see the root README) and open a fresh session.
2. Paste a fixture (everything below its title) with a natural request, e.g. "Triage these five" or "What does this actually identify?".
3. Save the reply to a file, e.g. `out/C-iv.md`.
4. Run the mechanical checks:

   ```bash
   python3 evals/check_outputs.py triage out/A-batch5.md
   python3 evals/check_outputs.py decomposer out/C-iv.md --paste evals/fixtures/C-methods-iv.md
   ```

5. Read the reply against `expected.md` and tick off each trap it caught.

## What the script checks

- **triage:** verdict labels are one of `deep-read / methods-only / skim-later / skip`; no prestige language; a handoff block, if present, has every required field and 2–3 questions.
- **decomposer:** the identification map and the *Estimand ↔ estimator alignment* section exist; every formula quoted under "Symbols as written" appears verbatim (whitespace-insensitive) in the paste — the "never invent an equation" rule.

## What it can't check

Whether a verdict is *right*, or whether a decomposition caught the real problem. That's what `expected.md` and a human reader are for.
