# Failure atlas

Use this as an adversarial prompt, not as a box-ticking proof. Most failures below are forms of one root mechanism: **an unavailable or inconvenient object is silently replaced by a nearby object, and the substitution is never registered**.

## A. Scope and identity substitutions

| Failure | Example shape | Required control |
|---|---|---|
| Cross-year | next year's page cap or later evidence applied to an older contest | sourced contest profile and historical cutoff |
| Cross-system | calibration performed on a harness/base lane, reported for the target system | system identity on every fit/result; target-match gate |
| Cross-population | statistic from one cohort/scenario used for another | population/scenario fields in result and claim contracts |
| Cross-index | wrong lane/class/category included by a generic index rule | synthetic multi-index tests and explicit set construction |
| Cross-space | plan distance/area proxy compared with surface/route quantity | name quantity and space/coordinate system together |
| Cross-boundary | one server rate compared with an aggregate parallel system | concurrency multiplier and matched boundary |
| Equal-value coupling | two concepts share a baseline number and one field | separate fields and perturbation-independence test |

## B. Statistical and metric substitutions

| Failure | Required control |
|---|---|
| Weighted sum treated as a count | model primitive count and mark; compound variance |
| Conditional binary total treated as homogeneous Poisson | binomial/Poisson-binomial or explicit approximation check |
| Non-significance called equivalence | predeclared margin and equivalence interval/test |
| Capped statistic called a bound | censoring fraction and proof of bound direction |
| Transient rate called capacity | window/horizon stability and full-clearance metric |
| Scenario band called confidence interval | explicit uncertainty type |
| Global rank correlation called top-k stability | report overlap and decision-specific ranking |
| Metric measures a proxy for the deliverable | counterfactual: what would it print if the claimed property were absent? |
| Missing value confused with missing structure | test information added by imputation; identify absent mechanism/geometry |

## C. Optimization and causal substitutions

| Failure | Required control |
|---|---|
| Feasible/best-found called optimal | certificate or same-metric valid bound; honest wording |
| Surrogate optimum called true optimum | evaluate on true objective and report both |
| Infeasible construction called lower bound | feasibility check under every required constraint |
| Bound on fixed candidates called global bound | state feasible set/generator scope |
| Overlapping unions summed and double-counted | global set union/accounting identity |
| Multiple inputs changed, one credited | controlled ablation/factorial design or joint-effect wording |
| Result-preserving scenario selected post hoc | predeclare selection criterion and report all branches |
| Local plateau called final bottleneck | extend sweep; inspect integer assignments/topology |

## D. Semantic and artifact substitutions

| Failure | Required control |
|---|---|
| Fallback initialized to plausible threshold | nullable/explicit absent state; threshold existence test |
| Signed number conflicts with direction word | generate relation/direction from the values |
| Scope promoted from representative run to all draws | provenance-matched quantifier gate |
| Fairness/safety/success definition drifts | objective register frozen before results |
| Number traces but sentence meaning is wrong | independent semantic review against definitions |
| Old equation/figure/table survives new model | forbidden-version tokens, artifact freshness, orphan sweep |
| One output overwritten by another scenario | scenario/producer in filename; one writer per artifact |
| Config centralized but decisions duplicated | one shared decision function; gate derived outputs |
| PDF stale while source/results current | dependency/hash freshness and compiled-content anchors |

## E. Gate failures

| Failure | Required control |
|---|---|
| Gate scans zero files and reports green | fail on empty/missing scan set; print coverage |
| Test invocation hides exit code | execute gate directly or preserve upstream status |
| Fixture reproduces author's assumption, not real input | test on a real artifact; preserve controls |
| Regex passes/fails due source formatting | test rendered text/context and inspect hits |
| Verdict and diagnostic message use different facts | derive both from the same result object |
| Compliance score substitutes for correctness | report completeness separately from validity |

## F. Production and presentation failures

- typed result literals become stale;
- digit-bearing LaTeX command names parse incorrectly;
- table column declarations disagree with row cells;
- `%`, `>`, `<`, or other characters render incorrectly under encoding;
- relative bar widths are drawn against absolute axes;
- dense/log ticks overlap;
- captions describe prior values/models;
- keywords/signature/memo spill to a forbidden extra page;
- correction history remains in the contest paper;
- operational deliverable names groups but does not assign actors/actions.

Controls: generated macros/tables, TeX-name validation, compile-log checks, visual geometry checks, per-deliverable rendered-page assertions, and page-by-page image inspection.

## G. Self-diagnostic warning signs

Stop and seek a more independent check when:

- writing a third fix for the same defect;
- every new gate passes on its first run;
- explaining why a discrepancy “does not matter” before quantifying it;
- about to write “not repairable” without recording an attempt;
- selecting a scenario after seeing which one preserves the narrative;
- reporting from a readiness document instead of the underlying artifact;
- adding another traceability check to address an interpretive-validity failure.

## H. Structural remedies that have held

- Put a program in the value path and leave the author a semantic name.
- One writer per artifact; scenario and producer in filenames.
- Centralize the decision algorithm, not only configuration.
- Freeze objectives, margins, and selection criteria before results.
- Compare artifacts created by different producers.
- Watch every gate fail on a planted defect and reject empty coverage.
- Audit the repair itself.
- Budget an independent semantic review because some definition/validity errors are not automatable.

Documentation alone does not prevent recurrence. Prefer constraints that make the invalid artifact impossible to produce.

