# Model cards, evidence, and provenance

## Model card purpose

A model card is an executable contract between formulation, code, evidence, and prose. It is not a promotional summary. Create one JSON object per active model/component using `templates/model_card.schema.json`.

Required content:

- stable ID/version and status (`active`, `validation-only`, `rejected`, `superseded`);
- decision contract and claims owned;
- entities, indices, variables, domains, units, and coordinate/system boundaries;
- equations or algorithm detailed enough to implement;
- objective and constraints where relevant;
- initial/boundary conditions;
- assumptions, rationale, directional consequence, and failure condition;
- parameter/data provenance and identifiability;
- solver/estimator/simulation settings;
- expected failure modes;
- validation and uncertainty plan;
- fallback conclusion if the model fails.

No two active cards may silently own the same claim. Rejected/superseded model outputs must be quarantined outside final artifact paths.

## Parameter ledger

Every parameter needs:

```text
name | physical meaning | symbol | unit | domain | baseline | range
source/status | system/population/time | transformation | consumers
```

Do not reuse a field for two physical quantities because their baseline values happen to be equal. Perturb each parameter and assert unrelated derived quantities stay invariant.

For sourced parameters, verify definition, population, geography, date, unit, and measurement regime. “From the literature” is not provenance.

## Source ledger

Prefer original/primary sources. Record:

- bibliographic identity and stable URL/DOI;
- publication and access date;
- exact claim/parameter supported;
- table/figure/page locator;
- source population/system and target mapping;
- unit/definition transformation;
- contest-time cutoff status;
- local hash where a copy is allowed.

One source may support a value without supporting the mechanism or causal language attached to it. Verify attribution, not just numerical equality.

## Run manifest

Each official run records:

- run ID and model-card versions;
- input/config hashes;
- command, environment, dependency versions;
- seed policy and actual seeds;
- solver status/tolerances/termination;
- start/end time and exit code;
- output paths, schemas, hashes;
- known warnings or incomplete branches.

Failed and exploratory runs remain distinguishable from official results. A later run must not overwrite an earlier scenario's generic filename.

## Result contract

Machine-readable results should carry:

- metric name and definition;
- value and unit;
- aggregation, denominator, population, scenario, and time horizon;
- model/run ID;
- epistemic status;
- uncertainty type and interval meaning;
- validation status;
- downstream artifacts.

Avoid naked scalars. `12.4` is not evidence without its meaning and scope.

## Claim ledger

Use `templates/claim_ledger.schema.json`. Record every headline, recommendation, superlative, causal statement, bound/optimum claim, and major limitation.

Allowed epistemic states:

- `OBSERVED`
- `SOURCE_FACT`
- `ASSUMED`
- `DERIVED`
- `ESTIMATED`
- `SIMULATED`
- `OPTIMIZED_EXACT`
- `BEST_FOUND`
- `BOUNDED`
- `SCENARIO`
- `RECOMMENDED`
- `NOT_IDENTIFIED`

The paper wording must match the state. A scenario range is not a confidence interval; a posterior interval for a mean is not a prediction interval; a feasible heuristic result is not an optimum.

## Artifact dependency graph

Record producer and upstream hashes for every generated table, figure, macro file, and PDF. One writer per artifact. If a result changes, stale descendants must fail freshness checks rather than coexist with the new model.

Compare artifacts pairwise where they describe the same object. This detects disagreement without first deciding which artifact is correct.

