# Contest and problem contracts

Use this reference at the beginning of every build, resume, or audit.

## 1. Input census before interpretation

Create an input manifest before reading selectively. For every file record:

- stable relative path;
- media/type and byte size;
- SHA-256 hash;
- extraction method (`native-text`, `table-parser`, `OCR`, `visual`, `manual`);
- extraction status and any unreadable region;
- role: statement, supplied data, diagram, template, rule, or background.

For PDFs and images, text extraction is not visual verification. Inspect diagrams, axes, footnotes, legends, labels, and page structure. When OCR is used, record confidence/uncertainty and compare critical numerals against the image.

Coverage language must be exact:

- **inventoried** — file existence/type/hash recorded;
- **extracted** — machine-readable content obtained;
- **visually inspected** — relevant pages/images viewed;
- **interpreted** — requirements or evidence mapped into the contract;
- **human-verified** — a person confirmed uncertain content.

Never convert “all files extracted” into “all files understood.”

## 2. Contest profile

Create `paper_output/contest_profile.json`. Each binding rule needs:

- contest, year, problem, submission deadline;
- exact rule text or faithful paraphrase;
- primary source URL/document and access date;
- applicability to this problem;
- enforcement method;
- status: `VERIFIED`, `UNVERIFIED`, or `NOT_APPLICABLE`.

Check at least:

- allowed file type and naming;
- Summary Sheet or cover requirements;
- page-count method and exclusions;
- font/margin/spacing requirements if any;
- team-number/header/page-number requirements;
- anonymity and identifying-information restrictions;
- citation/reference requirements;
- use of code, external data, AI, or other tools;
- required appendices, letters, memos, presentations, or articles.

Rules are year-specific. Never infer a page limit from a neighboring year, a current webpage, an old template, or a remembered judge comment. If an official page is unavailable, use an archived primary copy and mark the retrieval path.

## 3. Historical cutoff and contamination

For a historical reconstruction, set `source_cutoff` to the contest deadline. Divide sources into:

- `CONTEST_TIME_ALLOWED`;
- `POST_CONTEST_RETROSPECTIVE`;
- `UNVERIFIED_DATE`.

Post-contest judge commentary and later research may be used only in a clearly labeled retrospective audit unless the user explicitly requests a modern re-analysis.

If the agent or team has read an awarded solution to the current problem, record the contamination. The work may still be useful practice, but it is not a blind test and its model-selection quality cannot be evaluated as though no answer key had been seen.

## 4. Requirement ledger

Create `paper_output/problem_analysis.json` using the supplied schema. Split every prompt clause into an entry with:

- exact or near-exact prompt wording;
- task type: describe, estimate, predict, explain, optimize, allocate, schedule, design, compare, recommend, or communicate;
- decision user and action enabled;
- required output and format;
- population/system, geography, time horizon, and scenario;
- metric, unit, direction, aggregation, and completion rule;
- constraints and fixed inputs;
- evidence needed;
- planned model owner and paper location;
- ambiguity/missing-input status;
- final answer and evidence path when complete.

Do not merge subquestions merely because one model can answer several. Do not add decorative objectives that the prompt does not license.

## 5. Decision contract

For each material output, state:

```text
Actor: who uses the result?
Decision: what can they choose or do?
System boundary: what is inside/outside?
Scenario: under what conditions?
Metric: exactly what is optimized/estimated/reported?
Units and aggregation: per person, per day, total, mean, tail, etc.
Direction: maximize/minimize/meet threshold/describe trade-off.
Constraints: physical, logical, budget, equity, policy, time.
Uncertainty: what could change the action?
Completion rule: what evidence constitutes an answer?
```

An operational deliverable must let the named actor act. A schedule that names waves but does not assign participants is incomplete; a site ranking without a feasible design is not a design.

## 6. Missing inputs and ambiguity branches

For each missing quantity ask:

1. Is it identifiable from supplied evidence?
2. Is an authoritative external source allowed and matched in time/place/population/definition?
3. If assumed, what range and direction of effect are defensible?
4. Could the assumption flip the recommendation?

Use scenario branches when ambiguity is material. Choose a base case only with a criterion written before results are compared. Do not select the branch that preserves a preferred narrative.

## 7. Pre-model gate

Do not begin headline computation until:

- every input is inventoried;
- every prompt clause appears in the requirement ledger;
- every binding rule has a source or is explicitly unverified;
- historical cutoff/contamination is recorded;
- every material missing input has a handling plan;
- the decision contract has an explicit metric and completion rule.

