# Trusted runtime state

## Why task status is insufficient

A scheduler reports execution state. Downstream readers need to know whether data is present, fresh, eligible, reconciled, and associated with the claimed model or response. These questions can disagree without either record being incorrect.

A task can fail after persisting valid records. A successful task can have skipped training because history was insufficient. A registered model can fail promotion. A forecast response can succeed using a labelled baseline.

## Current evidence surfaces

| Surface | What it establishes | What it cannot establish alone |
|---|---|---|
| Acquisition audit | Recorded provider/publishing activity | Unique downstream persistence |
| Processing attempt | Recorded input dispositions for that attempt | Whole-history recovery or cross-system atomicity |
| Source-governance state | Evaluated freshness and logical coverage | Current upstream-provider availability |
| Reconciliation result | Comparison of the selected historical scope | Every future observation will agree |
| Training and decision records | Candidate lifecycle and policy outcome | A request successfully served a learned prediction |
| Forecast method and evidence references | Which path a forecast reports using | General model quality or trading utility |
| Chat-turn audit | Recorded response/evidence association | Completeness of every platform event |

## State dimensions

Interpret execution outcome, processing disposition, business freshness, and evidence completeness separately. Fresh and stale describe an observation's business relevance. Persisted and duplicate describe disposition. Failed and completed describe an execution boundary. These labels are not one mutually exclusive global state machine.

Current source state and its transition history are implemented. A unified runtime projection spanning all workflows, recovery events, model state, and evidence freshness remains an industrialization objective. The deterministic trusted-market-state component is narrower than that objective.

## Recovery interpretation

Retries retain their relationship to earlier attempts. Recovering a sink write does not erase a historical failure. A replayed DLQ record means the republishing path acknowledged the event; downstream correctness still needs a persistence and governance check.

## Operator reading order

Identify the observation time and execution scope, inspect the actual outcome, check evidence completeness, then check freshness and downstream eligibility. If a required artifact is missing or empty, report the outcome as unverified rather than reconstructing success from adjacent counters.

The selected runtime log ends with an incomplete sample, and an expected final task-state file is empty. Those limits are preserved in the [evidence index](../evidence/evidence-index.md).
