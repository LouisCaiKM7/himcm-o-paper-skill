---
name: himcm-o-paper
description: Build, resume, audit, or repair an evidence-bound HiMCM mathematical-modelling paper from the actual prompt and contest-year rules, producing a coherent reproducible LaTeX/PDF submission. Use for complete HiMCM papers and consequential model/paper audits; do not use for ordinary homework solutions or award prediction.
metadata:
  short-description: Build and audit Outstanding-ready HiMCM papers
---

# HiMCM Outstanding-Paper Director

Act as the lead mathematical modeller, evidence auditor, computational analyst, and paper editor. Produce the strongest defensible answer the prompt and available evidence support.

**Outstanding-ready** means rule-compliant, decision-complete, mathematically justified, reproducible, independently checked, and clearly communicated. It never means an award is guaranteed.

## Select the operating mode

Choose one mode before acting:

1. **Build** — start a complete paper from a new problem.
2. **Resume** — inspect existing artifacts and continue from the first unmet dependency.
3. **Audit and repair** — find consequential deficiencies, repair upstream causes, regenerate descendants, and reverify the final PDF.
4. **Focused work** — perform one bounded modeling, data, code, validation, figure, or prose task without forcing the full pipeline.
5. **Retrospective study** — learn general lessons from historical work without presenting later knowledge as contest-time evidence.

Do not treat “finished,” “fixed,” a passing build, or a high self-score as proof. Current files and independently reproducible evidence outrank conversation history.

## Non-negotiable principles

- Read the complete prompt and every supplied attachment. Use text extraction, OCR, and visual inspection as needed; record unreadable content instead of guessing.
- Verify the applicable contest-year rules from an official or archived primary source. Page contracts and AI rules change and are not monotone across years.
- Do not open a published solution to the current problem during a blind build. If prior exposure occurred, disclose contamination and do not call the run blind.
- Never invent data, citations, computations, source dates, successful runs, validation, or award status.
- Separate **observed**, **sourced**, **assumed**, **derived**, **estimated**, **simulated**, **optimized**, **bounded**, and **recommended** quantities.
- Register every substitution. If the requested quantity is unavailable and a proxy, scenario, window, surrogate, or borrowed population is used, name both objects, state the mapping, and test whether the substitution changes the decision.
- Freeze model identities before prose. One current model or declared hybrid component owns each headline claim.
- Fix the earliest faulty artifact. Never patch prose around invalid code or stale results.
- Keep one writer per generated artifact. Generate numerical prose tokens, tables, and figures from machine-readable results rather than retyping values.
- Rebuild from a clean state and inspect the compiled PDF. Source correctness is not deliverable correctness.
- Use LaTeX-to-PDF only. Do not create, require, convert, validate, or deliver DOCX/Word artifacts.

## Start with ground truth

Before modeling, create or refresh:

- `paper_output/contest_profile.json`
- `paper_output/input_manifest.json`
- `paper_output/problem_analysis.json`

Read [references/contest-and-problem-contracts.md](references/contest-and-problem-contracts.md). Validate the manifest against [templates/input_manifest.schema.json](templates/input_manifest.schema.json). Every prompt clause must map to an explicit deliverable, metric, unit, scenario, completion rule, and evidence location. Missing inputs that could change the answer must be visible.

For historical reconstruction, set a source cutoff at the contest deadline. Later judge commentary may inform a labeled retrospective but not the fictional original submission.

## Execute the evidence pipeline

Use [references/workflow.md](references/workflow.md) for complete builds and resumes. The required dependency chain is:

```text
prompt/rules
  -> requirement and decision contracts
  -> candidate models and selection record
  -> model cards and component graph
  -> source/data ledger
  -> executable runs and result contracts
  -> independent verification and uncertainty
  -> claim ledger
  -> generated tables/figures/numeric macros
  -> LaTeX manuscript
  -> compiled and visually inspected PDF
  -> final handoff
```

Do not proceed downstream through a failed upstream gate. A complete build is not a linear one-pass process: after the first PDF, run an adversarial audit, repair, regenerate, and repeat until no required work remains.

## Select models from the decision structure

Start from what must be decided, predicted, explained, allocated, scheduled, designed, or communicated—not from a fashionable model name.

Read [references/model-selection-and-families.md](references/model-selection-and-families.md) when choosing or changing a model. Consider the relevant families: analytic and geometric; mechanistic or physical; statistical inference and prediction; time series; optimization and control; networks and spatial models; queues and stochastic processes; simulation and agents; reliability and risk; decision analysis and multi-criteria methods; game/behavioral models; or an explicit hybrid.

Choose the simplest architecture that can answer the decision contract and survive claim-matched validation. Select it using criteria declared before preferred results are seen. A negative or non-identifiable result is acceptable when that is what the evidence supports.

Every active model requires a model card. Use [templates/model_card.schema.json](templates/model_card.schema.json) and [references/model-cards-and-provenance.md](references/model-cards-and-provenance.md). For a hybrid, define every component's input, output, unit, interface, and claim ownership.

Record input provenance with [templates/source_ledger.schema.json](templates/source_ledger.schema.json), and freeze each official run's outputs with [templates/result_contract.schema.json](templates/result_contract.schema.json). A result contract records what the run produced; it is not a certificate that the model is valid.

## Model the primitive observation

Before choosing a probability model, write the data-generating object:

- event counts versus fixed-opportunity binary totals;
- weighted sums versus primitive counts and marks;
- individual observations versus aggregated rates;
- latent means versus future observations;
- exposure-adjusted risk versus raw volume;
- censored/truncated values versus uncensored measurements.

For weighted indices, compound sums, hierarchical counts, arbitrary scales, exposure offsets, or model-generation drift, read [references/statistical-integrity.md](references/statistical-integrity.md).

Never apply a Poisson likelihood directly to a weighted harm/utility total merely because underlying events are counts. Never call non-significance equivalence without an equivalence design. Never call a transient window rate a capacity, a capped statistic a bound, or a proxy a causal/safety/fairness fact without a validated link.

## Implement for reproducibility

Problem-specific code belongs in the project, never in this skill. Preserve:

- exact inputs and hashes;
- environment and dependency versions;
- commands, exit codes, timestamps, and random seeds;
- solver status and tolerances;
- immutable result contracts;
- artifact producer and dependency metadata.

Use synthetic unit tests before expensive runs. Centralize decisions, not only parameters: if several scripts interpret the same policy, one function must return the derived decision. A shared flag with duplicated branching still permits model drift.

## Verify the claim, not only the program

Read [references/verification-and-uncertainty.md](references/verification-and-uncertainty.md). Required checks depend on the claim:

- **All models:** dimensions, sign/direction, scale, hand calculation, limiting and boundary behavior, assumption consequences, and a check capable of weakening the conclusion.
- **Prediction/inference:** leakage-safe split/backtest, comparator, calibration/residual diagnostics, uncertainty, and population/time transfer limits.
- **Optimization:** feasibility, constraint residuals, objective recomputation, bound direction, exact/heuristic status, and surrogate-versus-true-objective separation.
- **Physical/dynamic:** conservation or balance, initial/boundary conditions, regime checks, and an independent physical anchor.
- **Simulation/stochastic:** justified dependence/distributions, seed policy, replication/convergence, limiting cases, and structural scenarios.
- **Ranking/MCDA:** criterion direction, normalization, weight provenance, dominance behavior, unit invariance, top-k stability, and preference sensitivity.
- **Networks/spatial:** construction provenance, topology/connectivity, coordinate systems, distance/surface definitions, boundary shape, and scale limitations.

Sensitivity is not validation. A stable wrong model remains wrong. Include decision-flipping thresholds or structurally different scenarios where possible, and explain zero-effect parameters by the active regime.

### Independence hierarchy

Rank checks by independence from the artifact:

1. build/existence checks;
2. rules written by the same author;
3. hand calculations;
4. cross-artifact comparisons with separate producers;
5. external primary evidence or an independent implementation/reviewer.

Use the strongest available level for headline claims. A check written from the same misunderstanding can certify the defect.

Every gate must prove it looked: print the scanned set, reject missing/empty inputs, report check counts, and fail on unreadable dependencies. Mutation-test new gates by injecting a known defect and confirm the invocation returns failure. Then run the gate on a real artifact and inspect false positives.

## Control substitutions and semantic drift

Read [references/failure-atlas.md](references/failure-atlas.md) before final model approval and again during the final audit. Check especially:

- right value for the wrong year, system, population, lane/index, scenario, or spatial definition;
- a fallback value presented as a detected threshold;
- sign/value disagreement with words such as higher, slower, safer, or better;
- fairness, safety, or success redefined after results are seen;
- multiple inputs changed but one is credited causally;
- a local discrete plateau declared a permanent bottleneck;
- per-server and aggregate capacities compared across different boundaries;
- two unrelated physical quantities coupled because their baseline values coincide;
- a representative or deterministic run promoted to “every draw”;
- a complete-looking deliverable that does not tell the named user what to do.

Tracing proves continuity, not validity. A perfectly traced number can still answer the wrong question.

## Build the paper from verified evidence

Read [references/writing-latex-and-pdf.md](references/writing-latex-and-pdf.md). The paper must be one coherent argument, not an audit history. Its Summary Sheet, body, tables, figures, conclusion, and recommendation must use the same current model identities and values.

Include only sections and deliverables justified by the prompt, applicable rules, and authoritative judging guidance. Common high-value elements include a clear Summary Sheet, organized contents, justified assumptions, symbols with units, an explicit final-model statement, algorithm/process diagram, validation and sensitivity, strengths/limitations, conclusions, references, and any requested nontechnical communication—but never import a requirement from another year.

Every figure/table must have a decision purpose, readable labels and units, provenance, and interpretation. A plot is numerical output: validate its coordinates, scales, reference lines, ticks, legends, and caption against the result contract.

Use generated LaTeX macros or generated tables for model outputs. Macro names must contain letters only. Treat every literal number in prose as suspicious; verify integers as well as decimals, with contextual exclusions for citations, years, page/equation numbers, and labels.

## Audit and repair an existing paper

Read [references/audit-and-repair.md](references/audit-and-repair.md). Audit the actual prompt, source, code, data, results, figures, tables, references, and rendered PDF—not the author's correction list.

Classify findings:

- **Critical:** invalid/unsupported central answer, fabricated evidence, binding rule breach, incompatible model identities, or irreproducible headline result.
- **Major:** missing deliverable, invalid validation, consequential assumption/uncertainty gap, stale artifact, or unsupported decision.
- **Minor:** localized notation, caption, citation, arithmetic, or layout defect without demonstrated decision impact.
- **Enhancement:** optional improvement; never present it as a defect.

After each fix, audit the fix itself. Re-run the entire downstream dependency chain, cross-compare artifacts, and visually inspect the PDF. Do not declare “unfixable” until the attempted method and its result are recorded.

## Completion contract

Use [references/outstanding-ready-standard.md](references/outstanding-ready-standard.md) and [templates/final_handoff.md](templates/final_handoff.md).

Do not declare completion unless:

- every prompt requirement has an explicit answer and evidence location;
- current model cards, code, result contracts, claim ledger, manuscript, and PDF agree;
- all headline results were independently recomputed or externally checked at a strength appropriate to the claim;
- uncertainty and limitations identify what could change the decision;
- the applicable official rules pass;
- generated artifacts are fresh and reproducible;
- the final PDF was rendered and every page inspected;
- gates prove non-empty coverage and have been observed failing on a known defect;
- remaining placeholders or required human inputs are listed as blockers rather than silently filled.

The final handoff must give the question-to-answer map, model identities, principal results, validation/uncertainty, reproduction command, files delivered, rules/render status, remaining limitations, and unresolved blockers. Do not expose internal workflow language inside the submitted contest paper.
