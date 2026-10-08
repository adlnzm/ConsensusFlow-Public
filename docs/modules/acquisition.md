# Acquisition

## Purpose and connections

Acquisition translates heterogeneous market observations into events for Kafka. The current producer contains REST acquisition with fallback providers, bounded WebSocket collection, a continuous WebSocket mode, scraping, and historical-series acquisition. Airflow schedules publishing work; configured long-running acquisition services have separate execution lifecycles.

## Input and output contracts

Snapshot observations carry coin identity, price, optional market fields, source identity, ingestion mode, and observation time. Historical observations carry price and historical timestamp with ingestion context. A source's own event time and the time the acquisition process observed it must not be treated as interchangeable without contract evidence.

The public [market-event schema](../../schemas/public/market-event.json) is a reduced educational projection. It does not expose provider endpoints, authentication, internal topics, or the complete normalization rules.

## Design decisions

REST fallback is an ordered failure path, not evidence that every REST provider was queried successfully for each cycle. Source/feed identity is retained so governance can evaluate freshness and logical coverage without counting repeated observations as independent providers.

Publication waits for acknowledgement. Acquisition/batch accounting and source-attempt records make empty, partial, failed, and successful activity distinguishable. Historical requests have retry and scheduling logic separate from the live snapshot path.

## Failure handling

Required-field checks can reject records before publication. Publishing errors can be retained in the DLQ. Upstream rate limits, provider failures, empty returns, or incomplete coin coverage can produce partial results rather than a uniform success assertion. Observing an acknowledgement does not establish downstream persistence.

## Evidence and limitations

The selected live-WebSocket audit observation demonstrates recorded cumulative acquisition activity. It does not prove transport throughput, unique database persistence, or provider availability. Durable Bronze storage ahead of publication is not established in the inspected acquisition path.

See [operational metrics](../operations/operational-metrics.md) for accounting boundaries and [recovery](../operations/recovery-and-replay.md) for replay limits.
