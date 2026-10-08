# Recovery and replay

## Implemented recovery boundaries

Kafka retains events within its configured retention window. Spark checkpoints preserve stream progress. PostgreSQL constraints and write logic provide duplicate handling for represented identities. The dead-letter queue retains failed records and reasons. Manual consumer modes support recovery outside the scheduled Spark ownership path.

These mechanisms do not establish a durable immutable raw archive or unlimited historical replay. A Bronze archive and replay manifests remain roadmap work.

## DLQ replay eligibility

The current replay implementation selects pending records classified as Kafka publish errors that remain below the retry limit. It does not indiscriminately republish malformed or sink-contract-invalid records. Those records require diagnosis and a deliberate correction policy.

A successful republish marks an eligible record replayed. A failed republish increments retry state and can eventually abandon the record. The returned replay summary distinguishes attempted work, replayed records, abandoned records, and remaining pending records.

Kafka publication and the database status update do not form one atomic transaction. A publication followed by a failed database update can leave work eligible for repetition. Downstream idempotency therefore matters; the public documentation does not claim exactly-once behavior across this boundary.

## Stream restart

Checkpoint state, retained offsets, and sink identities must be assessed together. Restarting a process is not enough to prove that no input was missed. The inspected Spark reader is configured not to fail automatically on Kafka data loss, so the project cannot claim unconditional lossless consumption.

Processing-attempt accounting helps distinguish a failed execution from persisted data. An operator must inspect partial sink outcomes and audit state before assuming that an entire failed batch is safe to repeat without duplicates.

## Manual consumer paths

Direct consumer modes are not scheduled alongside Spark as alternative routine writers. Using them for backfill or recovery requires a reviewed ownership boundary, offset scope, and sink comparison. Their availability does not prove semantic equivalence to every Spark governance path.

## Recovery evidence to retain

Record the cause, affected stream and time range, available offset/checkpoint evidence, action taken, resulting sink state, duplicate/invalid dispositions, and reconciliation outcome. A future archive-based replay should also identify its immutable input selection and replay manifest.

## Evidence limit

The selected pending-DLQ observation establishes only an empty pending queue at that moment. It does not establish successful disaster recovery, complete historical replay, or absence of data loss.
