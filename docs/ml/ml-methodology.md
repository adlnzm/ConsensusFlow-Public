# ML methodology

## Objective and input contract

The ML subsystem forecasts market prices under an explicit data and model lifecycle. It does not equate fitting a model with delivering a production forecast.

Historical prices are read through PostgreSQL FDW using observation and ingestion cutoffs. The shared feature builder constructs completed OHLC bars, engineers indicators and lagged values, removes unusable feature rows, and aligns targets by the requested future horizon. Analytical dbt marts are a separate path.

## Temporal separation

The training runner reserves a held-out evaluation window. Development rows whose future labels reach the holdout boundary are purged before candidate work. Insufficient history after target alignment, holdout reservation, or the label embargo produces a recorded skip rather than a fabricated training result.

Training-data profiling and feature-selection suitability use the development frame. Model-family suitability determines eligible families; it does not predict the winning candidate. Feature-method evidence records how the retained feature set was obtained. Scores from different feature-selection methods are not treated as interchangeable units.

## Candidate work

The default scheduled path uses tree-model families, subject to eligibility. Neural implementations are available through an explicit opt-in path and suitability requirements. Available model classes do not imply that each family trained or served in a recorded run.

Optuna tuning and walk-forward evaluation operate on the development portion. Trained candidates are registered with model and feature context so unsuccessful promotion does not erase the experiment. Per-family exceptions are isolated; a run with no viable candidates has an explicit non-success outcome.

## Evaluation and selection

Evaluation suitability supplies a primary metric, direction, and comparison-loss interpretation. The selection layer ranks already-trained candidates and records pairwise comparisons and a baseline comparison. The runner checks that candidate walk-forward actuals align before selection.

A metric winner need not be statistically distinguishable from every alternative. The current selection policy discloses the absence of multiple-comparison correction. Supporting comparisons are evidence, not an undocumented weighted score or a guarantee of future returns.

The library contains strategies for additional task types. Their presence does not mean the scheduled market workflow performs classification, clustering, and ranking in production.

## Held-out promotion

Promotion compares the selected challenger against an eligible incumbent on held-out targets. Without an available production model, the comparison uses contemporaneous persistence. Incumbents without independent holdout eligibility are not accepted merely because a registry row exists.

The runner supplies measured single-row inference latency and feature distributions to the promotion engine. Cost checks exist as optional policy inputs; the inspected runner does not establish a measured inference-cost result.

## Serving and evidence limits

Serving checks the artifact feature version and columns. A shared builder does not automatically resolve every selected-subset compatibility case. Production inference requires its own request-level trace, which is not established by the selected runtime observations in this repository.

See [feature construction](../modules/features.md), [model promotion](model-promotion.md), and [recorded evidence](../evidence/industrial-metrics.md).
