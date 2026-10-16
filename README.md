![Project Cover](./images/consensus.png)
# ConsensusFlow

**A governed real-time crypto market intelligence platform.**

ConsensusFlow brings market acquisition, event processing, raw-data preservation, analytical storage, model governance, and evidence-backed agents into one engineering project. Its central concern is traceability across the data-to-decision lifecycle: what arrived, how it was processed, which evidence supports a model decision, and what a response actually represents.

This repository is a curated technical portfolio documenting a private implementation and its observed limitations. It does not contain a runnable copy of the platform, deployment configuration, production data, trained models, or private source code.

## Start here

| Question | Documentation |
|---|---|
| How is the system organized? | [System overview](architecture/system-overview.md), [architecture diagram](diagrams/system-architecture.md) |
| How does an observation become usable data? | [Dataflow](architecture/dataflow.md), [acquisition](docs/modules/acquisition.md), [stream processing](docs/modules/kafka-spark.md) |
| How is raw data preserved? | [System overview](architecture/system-overview.md), [industrialization roadmap](architecture/industrialization-roadmap.md) |
| How is trust represented? | [Governance model](docs/governance/governance-model.md), [decision evidence](docs/governance/decision-evidence.md) |
| How are models evaluated and promoted? | [ML methodology](docs/ml/ml-methodology.md), [promotion](docs/ml/model-promotion.md) |
| What do predictions and agents actually do? | [Prediction](docs/modules/prediction.md), [agents](docs/modules/agents.md) |
| What has been observed? | [Evidence index](docs/evidence/evidence-index.md), [recorded metrics](docs/evidence/industrial-metrics.md) |
| What remains unfinished? | [Industrialization roadmap](architecture/industrialization-roadmap.md) |

## Current architecture

ConsensusFlow separates raw-data preservation, event transport, governed operational storage, analytics, model development, and decision serving. These are distinct responsibilities; the presence of a component does not establish that the entire end-to-end path is complete.

### 1. Acquisition and event transport

Market acquisition collects observations from multiple sources, including Binance WebSocket streams, CoinGecko REST endpoints, and CoinMarketCap scraping. Python acquisition components normalize events before publishing them to Kafka.

Kafka provides event transport and retention-bounded replay. A long-running PySpark Structured Streaming service consumes market events, processes micro-batches, and owns the scheduled persistence path into PostgreSQL.

### 2. Bronze raw-data boundary

A PostgreSQL Bronze schema has been implemented as an initial raw-data preservation and integrity boundary.

The schema includes:

- `bronze.market_raw` for raw market observations.
- `bronze.market_timeseries_raw` for raw time-series observations.
- JSON payload storage and SHA-256 payload hashing.
- An immutability trigger intended to protect stored raw records from modification.

**Implementation boundary:** the schema and integrity mechanisms are implemented, but the available evidence does not establish that every acquisition event passes through Bronze before Kafka publication. Nor does it establish a complete, tested recovery path that rebuilds downstream state from Bronze. Bronze must therefore not be described as the proven, authoritative replay source for the complete platform.

Kafka remains the established event-transport layer, with replay bounded by its configured retention. PostgreSQL Bronze is a separate raw-data persistence capability whose end-to-end operational guarantees remain to be verified.

### 3. Governed operational storage

PostgreSQL supports market snapshots, consensus records, historical market data, model-related evidence, and processing audits.

The governance design separates acquisition accounting from downstream processing accounting. Processing outcomes distinguish persisted records, duplicates, invalid records, dead-letter outcomes, and failures rather than treating successful task execution as proof of complete data delivery.

These controls provide evidence for reconciliation and investigation. They do not, by themselves, establish lossless processing or complete recovery.

### 4. Analytics and ML

PostgreSQL supports two distinct downstream paths.

- **Analytics:** dbt staging models and analytical marts transform snapshot observations into analytical datasets. Declared tests and freshness policies help identify data-quality and timeliness issues.
- **ML:** a shared feature builder accesses historical data through PostgreSQL FDW, constructs completed market bars, and aligns future prediction targets. The ML feature path does not directly consume dbt marts.

The ML lifecycle separates data suitability, feature selection, candidate training, evaluation, empirical model selection, and promotion. Registration, selection, promotion, and serving are treated as different events.

The available evidence shows that training workflows and candidate-model registration execute. It does not establish successful production-model promotion or a working, model-linked production forecasting path. Feature drift and data-suitability checks remain relevant constraints on promotion.

### 5. Serving and agents

FastAPI exposes data, analytics, governance, metrics, and conversational interfaces.

The agent layer combines deterministic market and governance analysis with knowledge retrieval, including optional pgvector-based retrieval. Recommendations are rule-based. Optional language-model synthesis selects from an evidence catalogue and validates selected claims; it is not the authority for market observations or model promotion.

The forecast agent can attempt inference using a registered production model, subject to artifact availability, feature compatibility, and decision-evidence checks. When the required model path is unavailable or fails validation, it explicitly falls back to naive persistence.

Consequently, an available prediction response is not sufficient evidence that a trained model generated it. The selected method and supporting evidence must be inspected.

## Engineering principles

1. Preserve the distinction between execution status and data validity.
2. Keep acquisition accounting separate from downstream persistence accounting.
3. Preserve raw observations and their integrity metadata without conflating raw-data storage with event transport.
4. Represent model registration, selection, promotion, and serving as separate events.
5. Make missing evidence visible rather than interpreting it as a healthy zero.
6. Treat recovery as another observable operation, not as a reason to erase failure history.
7. Publish measured outcomes with their scope, timestamp, and limitations.

## Technology responsibilities

| Technology | Role in the inspected implementation |
|---|---|
| Python | Acquisition, normalization, governance, API, agents, ML, and operational tooling |
| PostgreSQL Bronze schema | Raw market payload storage, SHA-256 payload hashes, and immutability enforcement |
| Kafka | Event transport and retention-bounded replay |
| PySpark Structured Streaming | Micro-batch processing, validation, and governed database persistence |
| PostgreSQL and FDW | Operational evidence, market storage, and historical-data access |
| dbt | Analytical transformations and declared data tests |
| Airflow and Celery | Scheduled workflows and worker execution |
| FastAPI | Data, analytics, governance, metrics, and conversational interfaces |
| scikit-learn, XGBoost, PyTorch, Optuna | Candidate model implementations and tuning infrastructure |
| pgvector | Optional vector-based knowledge and market-memory retrieval |
| Prometheus and Grafana | Metric exposition and private monitoring configuration |
| Docker, Kubernetes, GitHub Actions | Runtime packaging, deployment definitions, and CI configuration |

Technology or configuration presence does not establish a successful deployment. Neural model implementations exist, but the default scheduled training path does not automatically train every available model family.

## Evidence and current limits

The [evidence catalogue](docs/evidence/evidence-index.md) distinguishes implemented behavior, stored runtime observations, and historical test results. Published measurements are point-in-time snapshots, not permanent service guarantees.

### Verified implementation progress

- The Kafka-to-Spark processing architecture and PostgreSQL persistence path are established components of the platform.
- The Bronze schema and its raw-payload integrity mechanisms were applied on October 8, 2026.
- Previous recorded validation includes successful dbt runs, automated checks, and reconciliation evidence. Consult the evidence catalogue for the exact scope and timestamp of each result.
- The ML training workflow has completed successful runs, and candidate models have been registered. These are workflow and registration results, not proof of production forecasting.

### Outstanding operational limitations

- **Bronze integration:** the schema exists, but complete acquisition-to-Bronze coverage, authoritative replay, and end-to-end recovery have not been established by the available evidence.
- **Orchestration handoff:** the Airflow-to-Spark handoff uses a fixed wait rather than an offset-completion barrier. A completed orchestration task therefore does not necessarily prove that all expected Kafka events have been persisted.
- **Market-data freshness:** a runtime inspection on October 14, 2026, observed that `snapshot.market_snapshot` and `snapshot.consensus_log` had stopped advancing despite continued Spark processing. This is a recorded operational issue, not a claim that every component was stopped.
- **Prediction targets:** a recent inspection of the 30-minute market bars found 574 bars, of which 480 had an exact 24-hour future target and 94 did not. Exact-target coverage was 83.62% in that inspected dataset. This is a point-in-time measurement, not a permanent coverage rate.
- **Production ML:** the latest recorded model-lifecycle inspection found no models marked as production. Candidate registration and successful training tasks must not be represented as successful production-model deployment.
- **Forecast evidence:** the recorded forecast store contained two rows, with no registered-model linkage in that inspection. This does not establish a successful model-backed forecasting loop.
- **Model promotion:** feature-drift and suitability checks have blocked promotion in recorded evaluations. These controls must be resolved through appropriate data and model investigation rather than bypassed solely to obtain a production designation.
- **End-to-end autonomy:** the available evidence does not establish a complete autonomous acquisition-to-prediction loop with verified freshness, reconciliation, model inference, and decision evidence.
- **Sentiment semantics:** the sentiment-labelled component supplies a technical-momentum proxy, not news or social sentiment.
- **Service guarantees:** historical throughput, test counts, reconciliation totals, and audit counters do not establish a permanent SLA, uninterrupted availability, or lossless processing.

## Industrialization priorities

The remaining work is organized around verifiable guarantees rather than component count.

1. **Close the Bronze ingestion gap:** establish and test the actual write path, define the required persistence ordering, and verify that raw events can be reconciled against downstream processing.
2. **Establish recovery semantics:** define retention, replay boundaries, idempotency, and recovery evidence. Demonstrate a recovery run without erasing the original failure history.
3. **Strengthen streaming coordination:** replace fixed-delay assumptions with an explicit completion or offset-based barrier where appropriate.
4. **Restore freshness and completeness:** investigate stalled snapshot persistence, source freshness, and end-to-end reconciliation.
5. **Complete the model lifecycle:** resolve feature and target suitability issues, evaluate candidates on appropriate time-based splits, and demonstrate promotion and model-linked inference before claiming production forecasting.
6. **Validate the complete decision path:** demonstrate that a current market observation can be traced through ingestion, persistence, feature construction, model or fallback selection, and the evidence returned by the serving layer.

Completion should be demonstrated by repeatable tests and timestamped runtime evidence, not inferred from service availability or successful orchestration alone.

## Public interfaces and examples

[Public schemas](schemas/public/) describe deliberately reduced illustrative interfaces. The short programs in [examples](examples/) were written for this repository; they neither call private services nor reproduce production algorithms. Their values and policy versions are examples, not measured results or deployed contracts.

`screenshots/` and `dashboards/` are reserved for future owner-supplied, reviewed material and currently contain only `.gitkeep`.

## Repository policy

The private and public repositories have independent histories. The private repository remains the canonical implementation; this public repository contains curated documentation and selected illustrative artifacts without exposing private Git history or private source code.

Documentation changes use reviewed branches. Platform components are documented as directories rather than permanent component branches. See [branching strategy](architecture/branching-strategy.md) and [public security policy](docs/SECURITY.md).

Copyright (c) 2026 Adhil Nazim Nazeer. All rights reserved. See [LICENSE](LICENSE).
