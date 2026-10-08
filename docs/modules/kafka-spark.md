# Kafka and Spark processing

## Purpose and ownership

Kafka separates acquisition from persistence. The long-running Spark service consumes snapshot and historical streams and owns their scheduled database-write path. Airflow publishes and schedules downstream work; it does not synchronously own each Spark micro-batch.

## Contracts

The inspected Spark reader parses JSON and retains Kafka metadata alongside raw payload information for processing. Snapshot and historical streams use separate schemas, handlers, and checkpoints. Avro schema and canary support exists elsewhere, but it does not establish a fully migrated Avro consumer pipeline.

Processing attempts distinguish persisted, duplicate, dead-lettered, invalid, and failed input. Their accounting should reconcile to the attempt's input population. Stale and late are business-state attributes that may coexist with those dispositions.

## Design decisions

Attempt identity includes the stream, micro-batch, and retry attempt. Database duplicate handling supports replay-aware writes. Fresh observations from the latest eligible source events participate in current consensus, while stale observations can retain historical value.

Kafka lag is interpreted from log-end offsets and committed Spark checkpoint progress. A conventional consumer-group metric is not assumed to describe this implementation's Structured Streaming progress.

## Failure handling

Malformed JSON and sink-contract violations have quarantine paths. Business-invalid inputs and duplicate records have separate accounting. Persistence failures update attempt evidence, and the historical ingestion watermark is advanced after persistence in the implemented path.

The processing code crosses Kafka, Spark checkpoints, and PostgreSQL boundaries. It does not establish a single distributed transaction. The reader's data-loss setting also prevents a blanket lossless-processing claim. Retention gaps and partial sink outcomes require explicit inspection.

## Evidence limits

Source code establishes these processing mechanisms. Acquisition counters and a passing downstream mart do not independently prove that every Kafka event reached its intended sink exactly once. The fixed orchestration wait is not an offset-completion barrier.

See [runtime state](../operations/trusted-runtime-state.md) and [replay](../operations/recovery-and-replay.md).
