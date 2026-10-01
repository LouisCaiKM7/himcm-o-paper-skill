# Model selection and family map

This reference is a search and decision aid, not a requirement to use many models. Complexity earns its place only when it answers a material part of the decision contract.

## 1. Classify the task before choosing mathematics

| Task | Typical question | Suitable starting families | Required evidence |
|---|---|---|---|
| Description/accounting | What happened or how much? | identities, aggregation, geometry, descriptive statistics | complete definitions, denominator/accounting checks |
| Estimation/inference | What latent quantity generated observations? | likelihood/Bayesian/hierarchical models | data-generating process, uncertainty, diagnostics |
| Prediction | What will happen out of sample? | regression, classification, time series, ML | leakage-safe holdout/backtest, comparator, calibration |
| Causal explanation | What changes what? | mechanistic model, experiment/quasi-experiment, causal graph | identification assumptions, controls, alternative explanations |
| Optimization/design | What decision is best? | LP/MILP/NLP, DP, network flow, facility location, control | objective/constraints, feasibility, bounds/certificates |
| Allocation/scheduling | Who/what/when/where? | matching, flow, scheduling, routing, integer optimization | operational assignment, capacity/time constraints |
| Reliability/risk | How likely is failure and what drives it? | survival, reliability blocks, fault trees, Monte Carlo | event definition, dependence, tails, stress scenarios |
| Behavior/strategy | How do interacting actors respond? | game theory, discrete choice, agent models | payoff/behavior evidence, equilibrium/behavior validation |
| Ranking/selection | Which alternatives are preferred? | Pareto analysis, MCDA, outranking, robust ranking | criterion direction, weights, dominance, rank stability |
| Communication | What must a stakeholder understand/do? | decision table, scenarios, concise memo/letter | audience/action, same evidence as technical analysis |

## 2. Candidate families and common traps

### Analytic, algebraic, and geometric

Use for identities, scaling laws, bounds, closed-form approximations, geometry, and transparent baselines.

Check domains, units, limiting cases, discretization, and whether the bound applies to the same metric and feasible set. A plan-distance bound does not certify surface distance; a rectangle side is not a curving ridge length.

### Physical/mechanistic and dynamical systems

Use conservation laws, differential/difference equations, compartment/flow models, kinematics, energy, or system dynamics when mechanisms and state transitions matter.

Check conservation, initial/boundary conditions, regime validity, parameter identifiability, numerical stability, and physical anchors. Do not force a constitutive law outside its measured regime.

### Statistical inference and prediction

Use when observed variability informs unknown parameters, associations, forecasts, or classifications.

Start from the primitive observation and sampling process. Choose distributions after defining exposure, opportunities, dependence, censoring, aggregation, and target population. Validate out of sample when prediction is claimed.

### Time series

Use trend/seasonality/state-space/ARIMA/renewal models when time ordering is informative and sufficient history exists.

Check stationarity or modeled nonstationarity, forecast origin, rolling backtest, event/structural breaks, leakage, horizon-specific error, and interval coverage. A short window cannot identify annual seasonality merely because a sinusoid can be fitted.

### Optimization and control

Use direct objective/constraints when decisions must be chosen. Consider LP/MILP/NLP, convex optimization, dynamic programming, optimal control, robust/stochastic optimization, or heuristics.

Prefer exploitable structure before generic solvers. Report exact/heuristic status, objective recomputation, feasibility residuals, gap/bounds, solver termination, and sensitivity to uncertain constraints. If a surrogate is optimized, evaluate its solution on the real objective.

### Networks and spatial models

Use graphs, flows, routing, matching, centrality, spatial accessibility, raster/vector geometry, clustering, or facility location when topology or location matters.

Define nodes/edges/weights/coordinate reference system, connectivity, obstacles, boundaries, surface versus plan distance, resolution effects, and construction provenance. Shared edges must not be double-counted across classes.

### Queues and stochastic processes

Use queueing theory, Markov chains, renewal processes, point processes, inventory/arrival-service models, or discrete-event simulation for congestion, waiting, reliability, and transitions.

Match arrival/service assumptions to evidence; distinguish transient, steady-state, full-clearance, and capacity quantities. Aggregate parallel servers at the same system boundary. Local plateaus can result from discrete assignment rather than a bottleneck transition.

### Simulation and agent-based models

Use when heterogeneity, interaction, stochastic trajectories, or geometry defeat tractable analytic models.

Define agents, states, transitions, time/space resolution, random processes, warm-up/horizon, seeds, replications, convergence, and calibration target. Validate emergent outputs, not only code execution. Use a transparent analytic baseline.

### Reliability, risk, and Monte Carlo

Use for uncertainty propagation, failure probability, stress testing, and distributions of outcomes.

Separate aleatory variability, epistemic parameter uncertainty, structural uncertainty, and scenario uncertainty. Preserve dependence and tails. Monte Carlo cannot rescue unjustified inputs; it only propagates them precisely.

### Decision analysis and MCDA

Use when the prompt genuinely contains multiple incommensurable objectives and no direct objective is supplied.

Predeclare criteria and directions. Justify normalization and weights. Check Pareto dominance, common-unit rescaling, weight regions, rank reversals, top-k stability, and non-monotone preferences. A weighted score is not a physical quantity, probability, fairness fact, or causal effect.

### Game and behavioral models

Use when strategic response or rule compliance changes system outcomes.

State actors, information, actions, payoff/proxy, timing, equilibrium or decision rule, and empirical basis. Distinguish posted policy, individual compliance behavior, and emergent aggregate state.

### Hybrid architecture

Use only when components answer different necessary questions. Draw a component graph and define every handoff:

```text
component_id | input | output | unit | uncertainty | downstream consumer | claim owner
```

Test interfaces independently. Two individually valid components can form an invalid hybrid through a population, unit, or scenario mismatch.

## 3. Selection record

Before running candidates, record:

- decision-contract coverage;
- evidence/parameter demand;
- assumptions and expected directional bias;
- identifiability;
- interpretability for the judge/stakeholder;
- computational feasibility;
- falsification/validation opportunity;
- uncertainty propagation;
- failure modes;
- reason selected/rejected.

The selection criterion must precede preferred outputs. If two plausible structures yield different recommendations, report structural uncertainty or collect the discriminating evidence.

## 4. Minimum adequate architecture

The preferred architecture usually contains:

1. a transparent baseline or analytic identity;
2. the principal model that answers the decision;
3. an independent check or competing explanation;
4. uncertainty/sensitivity linked to the recommendation;
5. an operational translation for the named decision user.

Do not add a model merely to increase mathematical variety. Do not omit an essential constraint merely to preserve a clean narrative.

