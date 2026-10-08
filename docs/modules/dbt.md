# dbt analytics

## Purpose and connections

dbt builds analytical representations of persisted market data. Staging models read snapshot and source-price relations. Mart models derive daily OHLC and a latest-market view with coin-dimension enrichment.

This path supports analytical consumption. The ML feature builder reads historical data through PostgreSQL FDW separately; the existence of marts does not imply that training depends on their materialization.

## Data contracts and design

The daily OHLC mart groups snapshot prices by coin and day, with ordering used to identify opening and closing observations. Its incremental strategy revisits recent days so late-arriving recent observations can revise that scope. It does not imply automatic reconstruction of all older history after arbitrary corrections.

The latest-market mart combines a latest snapshot, prior-day context, and a coin dimension. Declared schema tests cover identities, nullability, relationships, and selected value constraints. Source freshness checks assess recency under configured policies.

## Failure handling and orchestration

Airflow sequences publishing, a fixed wait, source-governance work, freshness checks, transformations, and tests. The fixed wait does not establish complete ingestion before an analytical read. A model failure, a test failure, a freshness result, and an upstream delay are different outcomes requiring their own evidence.

Dependency installation or successful SQL generation is not model-execution evidence. A generated artifact can also describe only the most recent selected command, not the entire historical project state.

## Observed evidence

The retained run-results artifact records success for the latest-market mart. A separate freshness artifact records passing checks for selected sources at its own timestamp. Neither artifact proves that the whole pipeline completed, that all data tests passed in that same run, or that ML features were valid.

See [recorded metrics](../evidence/industrial-metrics.md).
