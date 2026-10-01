# Statistical and measurement integrity

Read this reference whenever a paper uses probability, uncertainty intervals, weighted indices, rates, rankings, repeated measures, or hierarchical data.

## 1. Reconstruct the primitive observation

Write down what one row/event actually is before choosing a distribution.

| Observed structure | Common adequate starting model | Common invalid shortcut |
|---|---|---|
| event count over exposure | Poisson/negative-binomial/point process with exposure | Poisson without exposure or independence check |
| successes in fixed opportunities | binomial; Poisson-binomial if probabilities differ | Poisson solely because the result is an integer |
| weighted event total `S=sum w_i` | compound count/mark model or conditional resampling | Poisson on `S` with `Var(S)=E(S)` |
| repeated/grouped counts | hierarchical/mixed/cluster-robust model | treating every row as independent |
| proportion/rate | binomial/beta-binomial or count+denominator model | Gaussian error with missing denominator |
| time-to-event | survival/hazard model with censoring | ordinary mean of censored times |
| truncated/capped measurement | censored/truncated likelihood or bound-aware report | treating cap hits as observed true values |
| ranking from uncertain scores | posterior/bootstrap/weight-region rank stability | one deterministic rank presented as fact |

For a compound sum with count `N` and mark/severity `W`:

```text
E[S]   = E[N] E[W]
Var(S) = E[N] Var(W) + Var(N) E[W]^2
```

Under Poisson `N`, this becomes `Var(S)=E[N]E[W^2]`, not `E[S]` unless the marks are unit-valued.

## 2. Match the inferential target

Distinguish:

- descriptive total versus latent rate;
- latent-mean interval versus future-observation/prediction interval;
- conditional-on-observed-data resampling versus process uncertainty;
- parameter uncertainty versus day-to-day/cluster variability;
- association versus intervention effect;
- population risk versus raw event volume;
- stable capacity versus transient throughput.

State exactly what randomness an interval represents. Do not combine incompatible uncertainty layers without a generative model.

## 3. Exposure, denominators, and opportunities

Rates require a denominator matched in time, geography, and population. If area, population, operating hours, opportunities, or time-at-risk are missing, report volume or a scenario—not risk.

For binary outcomes conditional on events, model the number of opportunities and heterogeneous success probabilities. A Poisson approximation must be justified by rarity/independence or checked against the exact alternative.

## 4. Dependence and aggregation

Inspect temporal clustering, spatial grouping, repeated measures, shared shocks, and common random numbers. Use paired comparisons when arms share the same random inputs; an unpaired test discards that control.

Aggregation can hide Simpson reversals, unequal exposure, and compositional differences. Standardization must use one declared reference distribution and be applied consistently across comparison groups.

## 5. Non-significance is not equivalence

Failing to reject a difference does not show the effect is zero or practically negligible. To claim equivalence:

1. declare a practical equivalence margin before seeing the comparison;
2. use an equivalence procedure or interval;
3. show the interval lies inside the margin;
4. distinguish statistical from operational relevance.

Words such as “tie,” “same,” “free,” and “no effect” require equivalence evidence or must be weakened to “not detected under this experiment.”

## 6. Censoring, bounds, and capacity

- Report the censoring/cap-hit fraction.
- A capped mean or queue length is not automatically a lower or upper bound on a difference between groups.
- Extend the observation window/domain until censoring is negligible, fit a censoring-aware model, or state that the direction is unidentified.
- A fixed-window flow rate that moves materially with the window is not a steady-state capacity.
- Keep separate: stable service/discharge capacity, total completed count, clearance time, and transient inventory.

## 7. Weight and unit invariance

For arbitrary severity, utility, currency, or score scales:

- multiplying all weights by a common constant must scale dimensional outputs and intervals accordingly;
- dimensionless ratios/ranks should remain invariant only when the mathematics warrants it;
- changing relative weights is a different preference model and may change the recommendation;
- verify with extreme and plausible weight schedules;
- report top-k membership and decision stability, not only global rank correlation.

A high Spearman correlation can coexist with a largely different top ten.

## 8. Missing data

Separate missing **values** from missing **structure**. Imputing a correlated column may add almost no new information, while a missing trajectory, geometry, exposure, or mechanism cannot be repaired by more precise imputation.

Check whether missingness depends on outcome, group, or observed covariates. Use leakage-safe fitting and compare conclusions with/without imputation. Test whether the missing feature could materially change the deliverable before citing it as the main limitation.

## 9. Time series and seasonality

A short sample cannot identify long-run seasonality merely because a seasonal curve can be imposed. Label unsupported seasonal adjustments as scenarios. Use rolling/blocked validation, respect forecast origin, and report horizon-specific uncertainty.

## 10. Mandatory statistical checks

For every statistical headline, record:

- primitive observations and sampling unit;
- target estimand;
- likelihood/resampling mechanism;
- dependence/exposure treatment;
- interval type and interpretation;
- diagnostics and comparator;
- sensitivity to definitions, thresholds, weights, and aggregation;
- external or independent reconstruction.

An independent verifier should reconstruct primitive totals and at least one distributional identity without importing the model under test.

