# System overview

## Scope

ConsensusFlow is a governed market-intelligence engineering project. Its implementation joins streaming ingestion, database-backed control records, analytical transformations, model lifecycle management, and evidence-backed responses. This document describes implemented relationships; it does not imply that all components have been demonstrated together in a production run.

## Data plane

Acquisition adapters gather observations through REST, WebSocket, scraping, and historical-data requests. Kafka transports normalized snapshot and historical events. Spark consumes these streams continuously and owns scheduled database writes from live Kafka data.

PostgreSQL separates source observations, consensus snapshots, historical prices, forecasts, and analytical or model metadata. dbt builds analytical views of snapshot data. ML features take a separate route: historical prices are read through FDW and transformed by a shared feature builder.

The training runner registers candidates and records evaluation/selection evidence. Promotion governs production designation independently. Forecasting checks the production registry and artifact compatibility before attempting model inference; it can instead return a labelled persistence baseline.

## Control plane

Governance records acquisition attempts, processing dispositions, source freshness and coverage, reconciliation, quality events, model decisions, and selected lineage relationships. These records answer different questions. A publisher's successful acknowledgement is not proof of a database write, and a database write is not proof of a trustworthy current consensus.

The API exposes market and governance information and delegates analysis to agents. The conversational layer records turn-level evidence and may use optional synthesis over constrained evidence. It does not own the upstream truth or promotion policy.

## Orchestration boundaries

Airflow has separate data, ML, and reconciliation workflows. The data workflow publishes events, waits a fixed interval, evaluates source governance, and executes dbt work. The wait is an eventual-consistency handoff rather than a specific-offset completion check. A later analytical run can observe records that arrived after the preceding run.

Direct Kafka-to-database consumer modes remain available for manual recovery. Their existence does not make them co-owners of the scheduled streaming path, nor does it establish that their semantics are identical to Spark in every failure case.

## Storage and durability boundary

Kafka retention, PostgreSQL persistence, Spark checkpoints, and dead-letter records support bounded recovery mechanisms. A durable immutable Bronze archive with a replay manifest is a target architecture. It is not asserted as the implemented acquisition boundary.

## Read this architecture with its evidence

See the [system diagram](../diagrams/system-architecture.md), [dataflow](dataflow.md), and [evidence hierarchy](../docs/evidence/evidence-index.md). Configuration files establish intended integration. Runtime observations establish only the states and measurements captured in the associated artifacts.
