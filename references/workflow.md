# End-to-end workflow

Use these stages for complete builds and resumes. Focused tasks may enter at one stage, but they must preserve dependencies.

## S0 — Preflight and state reconstruction

1. Inventory the project, tools, current artifacts, and hashes.
2. Read the problem, attachments, contest profile, prior run manifests, and handoff.
3. Determine whether the current state is new, resumable, stale, incompatible, or contaminated.
4. Identify the first unmet or invalid dependency. Do not restart correct work or trust a claimed completion state.

**Outputs:** input manifest, status note, dependency graph.

**Gate:** all referenced current artifacts exist and hashes/freshness are known.

## S1 — Problem and rule contract

Build the contest profile, requirement ledger, decision contracts, ambiguity register, and source cutoff using [contest-and-problem-contracts.md](contest-and-problem-contracts.md).

**Gate:** every prompt clause maps to a completion rule and planned evidence location.

## S2 — Candidate architecture

1. Draw the system/entity/causal or process map.
2. Generate a shortlist across relevant model families.
3. Specify data and assumptions each candidate requires.
4. Declare selection criteria before computing preferred outputs.
5. Select the simplest adequate model or hybrid; document rejected alternatives.

**Outputs:** selection record, component graph, model cards, planned falsification checks.

**Gate:** one current model owner per claim; interfaces and units match.

## S3 — Evidence and data

Acquire only necessary data. Prefer primary, authoritative, contest-time-compatible sources. Record:

- source identity, URL, publication/access dates;
- geography, population, time span, definition, unit, resolution;
- license/usage constraints;
- raw hash and transformation log;
- missingness, duplicates, exclusions, imputation, and leakage controls.

Keep raw data immutable. Derived data must be reproducible from raw inputs.

**Gate:** every external parameter and dataset has provenance; every transformation is executable or documented precisely.

## S4 — Model implementation

Write problem-specific code in the paper project. Separate:

- configuration/parameter ledger;
- data ingestion and cleaning;
- model logic;
- experiment/scenario orchestration;
- result serialization;
- figure/table generation;
- independent verification.

Use one writer per artifact and stable result schemas. Add small synthetic tests before full runs. Record environment, commands, seeds, solver status, tolerances, timings, and hashes.

**Gate:** tests pass; baseline result contract is generated from a complete run; no manual result values are inserted downstream.

## S5 — Validation and uncertainty

Execute claim-matched checks from [verification-and-uncertainty.md](verification-and-uncertainty.md). Include at least:

- independent hand/small-case calculation;
- boundary/limiting behavior;
- cross-artifact consistency;
- one external anchor or independent implementation where feasible;
- sensitivity capable of changing the answer;
- structural alternatives for major assumptions.

**Gate:** evidence supports the exact strength and scope of each intended claim.

## S6 — Claim ledger and frozen results

Create a claim ledger using the schema. Every material sentence planned for the Summary Sheet or conclusion needs:

- claim text/function;
- metric, unit, scope, scenario, population;
- model/result owner;
- evidence path;
- epistemic status;
- verification method and strength;
- uncertainty/limitations;
- allowed wording.

Freeze model IDs and result contracts before drafting. Changes after freeze reopen all dependent claims.

**Gate:** no duplicate ownership, orphan claim, unverified superlative, or silent substitution.

## S7 — Generated evidence artifacts

Generate numerical macros, tables, and figures from frozen results. Each artifact records its producer, source result, hash, and caption metadata.

Validate:

- numbers and arithmetic;
- integer and decimal traceability;
- axes, scales, units, ticks, legends, and reference lines;
- figure/table freshness;
- no rejected-model artifacts remain.

**Gate:** every displayed value and visual encoding agrees with the current result contract.

## S8 — LaTeX paper and PDF

Write one concise argument using [writing-latex-and-pdf.md](writing-latex-and-pdf.md). Compile from LaTeX, inspect the log, extract the PDF text layer, render every page, and visually inspect it.

**Gate:** applicable rules pass; all pages are legible; Summary Sheet/body/conclusion agree; named deliverables satisfy their physical-page constraints.

## S9 — Adversarial audit and repair loop

Use [audit-and-repair.md](audit-and-repair.md) and [failure-atlas.md](failure-atlas.md).

1. Reconstruct the paper's current models without trusting its declarations.
2. Recompute headline claims independently.
3. Compare prompt ↔ contract ↔ model ↔ results ↔ manuscript ↔ PDF.
4. Attempt to falsify the recommendation.
5. Repair the earliest cause.
6. Regenerate and audit the repair itself.
7. Repeat until no required work remains.

**Gate:** completion contract in [outstanding-ready-standard.md](outstanding-ready-standard.md).

## Dependency invalidation

When an upstream artifact changes, invalidate at least:

| Changed artifact | Mandatory descendants |
|---|---|
| contest rule/problem interpretation | requirement ledger, paper structure, gates |
| source/data/parameter | model run, results, verification, claims, visuals, prose, PDF |
| model equation/algorithm | tests, run, results, validation, claims, visuals, prose, PDF |
| result contract | macros, tables, figures, claim ledger, prose, PDF |
| figure/table generator | artifact hash, manuscript/PDF render inspection |
| prose with a numerical or relational claim | semantic gate, PDF rebuild/inspection |
| LaTeX/layout | PDF format/render checks and page-by-page inspection |

Never update a readiness report without regenerating the evidence it summarizes.

## Stopping conditions

Stop and request user input only when a missing choice materially changes the model or requires authority not already granted. Otherwise use a reasonable reversible assumption, label it, and continue.

If an external item is unavailable, complete all independent work, record the exact blocker, attempted methods, and fallback conclusion. “Not yet done” is not “impossible.”

