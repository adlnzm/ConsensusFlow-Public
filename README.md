# ConsensusFlow

**A governed real-time crypto market intelligence platform.**

ConsensusFlow brings market acquisition, event processing, analytical storage, model governance, and evidence-backed agents into one engineering project. Its central concern is the traceability of the data-to-decision lifecycle: what arrived, how it was processed, which evidence supports a model decision, and what a response actually represents.

This repository is a curated technical portfolio. It describes the private implementation and its observed limitations. It does not contain a runnable copy of the platform, deployment configuration, production data, trained models, or private source code.

## Start here

| Question | Documentation |
|---|---|
| How is the system organized? | [System overview](architecture/system-overview.md), [architecture diagram](diagrams/system-architecture.md) |
| How does an observation become usable data? | [Dataflow](architecture/dataflow.md), [acquisition](docs/modules/acquisition.md), [stream processing](docs/modules/kafka-spark.md) |
| How is trust represented? | [Governance model](docs/governance/governance-model.md), [decision evidence](docs/governance/decision-evidence.md) |
| How are models evaluated and promoted? | [ML methodology](docs/ml/ml-methodology.md), [promotion](docs/ml/model-promotion.md) |
| What do predictions and agents actually do? | [Prediction](docs/modules/prediction.md), [agents](docs/modules/agents.md) |
| What has been observed? | [Evidence index](docs/evidence/evidence-index.md), [recorded metrics](docs/evidence/industrial-metrics.md) |
| What remains unfinished? | [Industrialization roadmap](architecture/industrialization-roadmap.md) |

## Current architecture

Market acquisition publishes normalized events to Kafka. A long-running PySpark Structured Streaming service owns the scheduled path from Kafka into PostgreSQL. Airflow orchestrates acquisition, source-governance evaluation, dbt work, ML training, and reconciliation through separate workflows.

PostgreSQL supports two distinct downstream paths:

- **Analytics:** dbt staging models and analytical marts transform snapshot observations.
- **ML:** a shared feature builder reads historical data through PostgreSQL FDW, constructs completed bars, and aligns future targets. dbt marts do not directly supply this feature path.

The ML lifecycle separates data suitability, feature selection, candidate training, evaluation, empirical selection, and promotion. The forecast agent can attempt registered-model inference, subject to artifact, feature, and decision-evidence checks. It explicitly falls back to naive persistence when the required model path is unavailable or fails validation.

The agent layer combines deterministic market and governance analysis with knowledge retrieval. Recommendations are rule-based. Optional language-model synthesis selects from an evidence catalogue and validates selected claims; it is not the authority for market observations or model promotion.

## Engineering principles

1. Preserve the distinction between execution status and data validity.
2. Keep acquisition accounting separate from downstream persistence accounting.
3. Represent model registration, selection, promotion, and serving as different events.
4. Make missing evidence visible rather than interpreting it as a healthy zero.
5. Treat recovery as another observable operation, not as a reason to erase failure history.

## Technology responsibilities

| Technology | Role in the inspected implementation |
|---|---|
| Python | Acquisition, governance, API, agents, ML, and operational tooling |
| Kafka | Event transport and retention-bounded replay |
| PySpark Structured Streaming | Micro-batch processing and governed database persistence |
| PostgreSQL and FDW | Operational evidence, market storage, and historical-data access |
| dbt | Analytical transformations and declared data tests |
| Airflow and Celery | Scheduled workflows and worker execution configuration |
| FastAPI | Data, analytics, governance, metrics, and conversational interfaces |
| scikit-learn, XGBoost, PyTorch, Optuna | Candidate model implementations and tuning infrastructure |
| pgvector | Optional vector-based knowledge and market-memory retrieval |
| Prometheus and Grafana | Metric exposition and private monitoring configuration |
| Docker, Kubernetes, GitHub Actions | Runtime packaging, deployment definitions, and CI configuration |

Technology or configuration presence does not establish a successful deployment. Neural model implementations exist, but the default scheduled training path does not automatically train every available model family.

## Evidence and current limits

The [evidence catalogue](docs/evidence/evidence-index.md) separates implemented behavior from stored runtime observations and historical test results. Published measurements are point-in-time snapshots. They do not establish throughput, availability, a permanent SLA, or lossless processing.

Current boundaries include:

- Durable Bronze storage is a roadmap item, not the established ingestion path.
- The Airflow-to-Spark handoff uses a fixed wait rather than an offset-completion barrier.
- Stored model-registration and non-promotion observations do not demonstrate successful production ML inference.
- The available evidence does not establish a complete autonomous acquisition-to-prediction loop.
- A sentiment-labelled component supplies a technical-momentum proxy, not news or social sentiment.

## Public interfaces and examples

[Public schemas](schemas/public/) describe deliberately reduced illustrative interfaces. The short programs in [examples](examples/) were written for this repository; they neither call private services nor reproduce production algorithms. Their values and policy versions are examples, not measured results or deployed contracts.

`screenshots/` and `dashboards/` are reserved for future owner-supplied, reviewed material and currently contain only `.gitkeep`.

## Repository policy

The private and public repositories have independent histories. Documentation changes use reviewed branches; platform components are documented as directories rather than permanent component branches. See [branching strategy](architecture/branching-strategy.md) and [public security policy](docs/SECURITY.md).

Copyright (c) 2026 Adhil Nazim Nazeer. All rights reserved. See [LICENSE](LICENSE).
