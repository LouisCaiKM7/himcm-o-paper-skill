# Outstanding-ready standard

This is a readiness contract, not a score and not an award predictor. Mark each item `PASS`, `FAIL`, `NOT_APPLICABLE`, or `NOT_VERIFIED`; never turn an unchecked item into a pass.

## A. Problem and rules

- All supplied files are inventoried; critical visuals/tables are inspected.
- Every prompt clause maps to an explicit answer and evidence location.
- Applicable contest-year rules are verified from primary/archived official sources.
- Historical cutoff and prior-solution contamination are disclosed.
- Material ambiguities/missing inputs are branched, sourced, assumed transparently, or declared unidentified.

## B. Decision and model

- Decision user, action, system boundary, scenario, metric, unit, direction, constraints, and completion rule are explicit.
- Model selection criteria were declared before preferred outputs.
- Active model cards are complete; rejected/superseded models are quarantined.
- Hybrid interfaces match population, scenario, unit, and uncertainty.
- Objectives and definitions do not drift after results are seen.

## C. Evidence and computation

- Sources match claim, time, geography, population, definition, and unit.
- Raw data are immutable and transformations reproducible.
- Code and run manifests reproduce current result contracts.
- One writer owns each generated artifact; no scenario overwrites another.
- Solver/simulation/statistical status and limitations are honest.

## D. Validation and uncertainty

- Headline claims have claim-matched validation, not sensitivity alone.
- Independent checks do not import the model under test where independence is claimed.
- Boundary, small-case, conservation/feasibility, unit-rescaling, and cross-artifact checks pass as applicable.
- Gates fail on missing/empty inputs and have been mutation-tested.
- Uncertainty type is correct and decision-flipping thresholds/structural alternatives are reported.
- Causal, fairness, safety, capacity, bound, optimum, and equivalence language is supported.

## E. Argument and communication

- Summary Sheet, body, visuals, conclusion, and recommendation use the same current evidence.
- Every subquestion receives a direct answer in requested units/context.
- Assumptions have rationale and decision consequence.
- Variables include units and stable definitions.
- Final model is explicit; judge need not infer which model is current.
- Figures/tables are readable, sourced, discussed, and decision-relevant.
- Limitations identify the direction or condition under which the answer may change.
- Requested nontechnical deliverables are usable by their named audience.

## F. LaTeX/PDF

- LaTeX compiles without errors, unresolved references/citations, or placeholders.
- Page count, font, header, anonymity, file type, and disclosure requirements pass.
- Generated values/integers/relations trace to current results or named source constants.
- Artifact hashes/freshness pass; rejected figures/tables are absent.
- Every rendered page has been visually inspected with no clipping, overlap, missing glyphs, unreadable plot, or broken transition.
- No DOCX/Word artifact is required or delivered.

## G. Completion evidence

- Readiness report states the nonempty scan/check counts.
- Reproduction command and environment are recorded.
- Final PDF hash and page count are recorded.
- Final handoff separates repaired defects from residual limitations.
- Required human substitutions (team number, disclosure, signatures, etc.) are explicit blockers.

The paper is `READY` only when every binding item is `PASS` or justified `NOT_APPLICABLE`. Use `READY_WITH_BLOCKERS` for external human substitutions that do not affect model validity. Otherwise use `NOT_READY`.

