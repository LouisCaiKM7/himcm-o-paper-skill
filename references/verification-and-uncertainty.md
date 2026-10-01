# Verification and uncertainty

## 1. Verification matrix

Create a table whose rows are material claims and whose columns are:

```text
claim | failure that would invalidate it | check | independent producer
input | expected/hand value | observed value | tolerance | status
```

A model that merely runs has not been validated. A sensitivity sweep over the same wrong structure is not validation.

## 2. Universal checks

### Dimensions and semantics

- Every equation is dimensionally valid.
- Numerator/denominator, per-unit/total, plan/surface, instantaneous/cumulative, and mean/tail quantities are explicit.
- Signs and verbal directions agree.
- Every comparison uses the same population, scenario, and system boundary unless the difference is the object being studied.

### Hand and small-case checks

Build a case simple enough to calculate independently. Do not import the production model. Include a known-good control before interpreting experimental variants.

### Limiting and boundary cases

For each parameter, specify expected behavior at zero, infinity, equality, saturation, empty/full demand, or another meaningful limit. Assert that the intended derived quantity actually changed and unrelated quantities did not.

### Conservation and feasibility

Check mass/people/vehicles/energy/probability/accounting identities. For optimization, recompute the objective and every constraint from the returned decision.

### Metamorphic tests

Use transformations with known consequences:

- unit rescaling;
- rigid spatial translation/rotation where applicable;
- relabeling/permutation symmetry;
- duplicate/removal behavior;
- common scalar rescaling of arbitrary weights;
- monotonicity only where mathematically justified.

Write the dimensionless groups or invariants before claiming a transformation should preserve the result.

## 3. External and independent checks

The strongest available verification uses a different producer or knowledge source:

- primary published measurement;
- independent implementation that does not import model code;
- alternative model with different assumptions;
- cross-artifact comparison;
- reviewer who did not build the model;
- rendered output rather than source.

State exactly what the independent check covers. Do not say “all results verified” when it checks a list of headline scalars.

## 4. Make gates prove coverage

Every automated gate must:

- resolve paths relative to an explicit project root;
- print the files/records/pages scanned;
- fail on missing or zero-item input;
- surface unreadable/ignored artifacts;
- return a nonzero exit code on failure even through wrappers/pipelines;
- report check and failure counts;
- distinguish `PASS`, `FAIL`, `NOT_APPLICABLE`, and `NOT_VERIFIED`.

Before trusting a new gate:

1. inject a known defect and watch it fail;
2. restore the artifact and watch it pass;
3. run it on a real paper;
4. read all hits once;
5. preserve false-positive/false-negative examples as fixtures.

Synthetic fixtures are necessary but not sufficient; they can inherit the gate author's blind spot.

## 5. Uncertainty taxonomy

Keep separate:

- **measurement uncertainty** — errors in observed inputs;
- **sampling/process variability** — stochastic repetitions/events;
- **parameter uncertainty** — unknown calibrated values;
- **structural uncertainty** — alternative model forms;
- **scenario uncertainty** — future/context assumptions;
- **decision preference uncertainty** — weights, thresholds, risk tolerance.

Choose methods accordingly: analytic propagation, bootstrap, posterior simulation, Monte Carlo, robust optimization, scenario analysis, or decision-boundary analysis.

Do not label a scenario range a confidence interval.

## 6. Decision-relevant sensitivity

Sensitivity should answer:

- Which assumptions dominate the decision?
- Where does the recommendation flip?
- Which variables have zero effect in the current regime, and why?
- Does a plausible structural alternative change the conclusion?
- Are local flat regions discrete plateaus rather than permanent limits?
- Which measurement would most reduce decision uncertainty?

Use one-at-a-time sweeps only when interactions are negligible. Otherwise use factorial/global designs, uncertainty propagation, or targeted interaction grids.

For discrete systems, extend the sweep beyond adjacent equal points and inspect assignments/topology. A capacity-only crossover is a diagnostic, not automatically the realized transition.

## 7. Convergence and stochastic reporting

For simulation:

- declare seed policy and common-random-number pairing;
- show replication error/convergence against run count;
- distinguish within-run randomness from parameter/scenario uncertainty;
- report distributions/tails relevant to the decision;
- verify that the horizon/warm-up does not determine the result;
- store per-replication results when paired tests are used.

## 8. Verification stop condition

No headline claim is ready until its verification strength matches its wording. If an external check is impossible, narrow the claim and state what remains unverified.

