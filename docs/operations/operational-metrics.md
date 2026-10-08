# Operational metrics

## Interpret a metric through its producer

The API assembles governance, ML, operational-policy, and chatbot metric exposition. Many values are computed from persisted records; some chatbot counters are process-local. Names alone do not establish the unit, population, time window, or completeness of a measurement.

| Metric family | Producer/input | Correct interpretation |
|---|---|---|
| Batch runs and rows | Governance exporter reading batch audit records | Cumulative recorded activity grouped by stream/status; not an independent count of unique sink events |
| Processing dispositions | Streaming processing-attempt evidence | What happened within an attempt; retries must be interpreted separately |
| DLQ backlog | Pending dead-letter records | Outstanding pending items at observation time, not historical loss or replay success |
| Source freshness and coverage | Persisted source-governance state | Evidence about source observations and logical coverage at the relevant evaluation time |
| Kafka/Spark lag | Kafka log ends and committed Spark checkpoint offsets | Downstream progress based on available partition/checkpoint evidence |
| Model registration and decisions | Model registry and promotion history | Registered candidates and recorded policy decisions, not successful serving requests |
| Operational-policy checks | Database evidence evaluated against configured targets | Internal policy evaluation, including whether a check is evaluable |
| Chatbot observations | Process-local instrumentation | Local process activity; replica aggregation and restarts affect interpretation |

## Acquisition is not sink throughput

The published WebSocket observation is a sum from batch-audit accounting. It must not be renamed as unique rows in PostgreSQL, records processed per second, or end-to-end throughput. Repeated work, differing acquisition units, and processing retries require explicit denominators and boundaries before rate calculations are meaningful.

## Missingness and evaluability

A missing series can mean absent underlying rows, a collection failure, or unavailable metadata. It is not automatically zero. Operational-policy exposition distinguishes compliance from evaluability; a non-evaluable freshness or reconciliation check must not be described as a measured passing or failing SLA.

Likewise, source-state timestamps and exporter collection time need not be the same. A scrape can successfully return a stale governance observation.

## Kafka and Spark

The governance code interprets lag using Kafka log-end offsets and Spark committed checkpoint offsets. This is different from assuming that a conventional Kafka consumer-group lag command describes Structured Streaming progress. Missing checkpoint or partition evidence remains unknown.

## Publication standard

Every public observation needs a measurement definition, timestamp, producing component, retained artifact reference, and explicit limits. The [industrial metrics](../evidence/industrial-metrics.md) meet that standard for selected snapshots. This repository does not publish configured target thresholds as achieved service guarantees.
