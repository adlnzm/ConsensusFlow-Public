# Dataflow

## Acquisition to persistence

1. **Observe:** REST fallback adapters, WebSocket collection, scraping, and historical acquisition produce source observations. Source identity and acquisition mode remain meaningful provenance.
2. **Validate and publish:** required fields are checked; publishing waits for acknowledgement. Failures can be written to a dead-letter queue and acquisition/batch records preserve accounting.
3. **Consume:** Spark reads the snapshot and historical Kafka paths with separate checkpoints. The inspected consumer parses JSON; Schema Registry and Avro canary facilities do not prove an end-to-end Avro migration.
4. **Classify and persist:** Spark separates malformed input, invalid records, duplicates, persistence outcomes, and failed work. Freshness and lateness are business attributes rather than additional processing outcomes.
5. **Construct current state:** historical observations can remain persisted while stale observations are excluded from current consensus calculations. Source governance evaluates freshness and logical feed coverage separately.

## Two downstream paths

| Path | Input | Transformation | Output |
|---|---|---|---|
| Analytical | Snapshot/source records | dbt staging, daily OHLC, dimension enrichment | Analytical marts and test/freshness artifacts |
| ML | Historical prices accessed through FDW | Completed bars, feature engineering, target alignment | Training and serving feature frames |

The analytical mart path is not a prerequisite data source for the implemented ML feature builder. A passing dbt model cannot, by itself, establish that the ML feature frame is eligible for training.

## Training to response

Training separates development data from held-out evaluation data and purges development labels that reach into the holdout. Suitability policies govern feature methods and model families. Tuned candidates are evaluated and registered; a selection decision identifies an empirical winner and supporting comparisons.

Promotion then compares a challenger with an eligible incumbent, or a contemporaneous persistence reference where no production model is available. Operational and drift checks can block promotion before statistical comparison. Forecasting independently validates the serving prerequisites and can return a baseline.

Agents read market, historical, governance, and forecast evidence. The coordinator combines structured results and partial failures. A conversational turn can retrieve knowledge and use optional evidence-constrained synthesis; retrieved text remains untrusted content.

## Completion boundaries

Publishing completion, stream-attempt completion, dbt success, training completion, promotion, and response generation are separate boundaries. The available workflow and runtime evidence do not establish one atomic, autonomous acquisition-to-prediction transaction.

See [end-to-end diagram](../diagrams/end-to-end-flow.md), [trusted runtime state](../docs/operations/trusted-runtime-state.md), and [recovery](../docs/operations/recovery-and-replay.md).
