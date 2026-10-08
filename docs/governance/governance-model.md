# Governance model

## Purpose

Governance makes processing outcomes and trust decisions inspectable. It is implemented through explicit validation, database records, policies, and API/monitoring surfaces rather than delegated to language-model reasoning.

## Independent governance domains

| Domain | Input | Decision or output |
|---|---|---|
| Acquisition | Provider attempts and returned observations | Success, partial, empty, or failed acquisition accounting |
| Processing | Kafka micro-batch and persistence outcomes | Attempt-level disposition accounting |
| Source quality | Persisted observations and expected logical coverage | Freshness, missingness, invalid timestamps, current state, transitions |
| Consensus | Eligible observations across sources | Deterministic market-state evidence |
| Reconciliation | Snapshot and historical observations | Coverage and paired-price comparison results |
| ML | Dataset profile, evaluation, artifact, operational observations | Suitability, selection, promotion, and decision evidence |
| Response | Specialist outputs and retrieved passages | Structured response status and traceable claim selection |

## Processing disposition versus business state

Each processing attempt accounts for input as persisted, duplicate, dead-lettered, invalid, or failed. A stale observation can be persisted historically, and a late observation can be a duplicate. Staleness and lateness must therefore not be added again as mutually exclusive processing outcomes.

The processing-attempt identity includes the stream, Spark batch identity, and attempt number. A retry is not evidence that the preceding attempt never happened. Audit interpretation must distinguish attempts from unique source events.

## Current source state and history

Source governance evaluates logical source/feed coverage from eligible fresh observations. Unknown or future timestamps have distinct interpretations. The persistence layer writes current source state and transition events within its caller-owned transaction, allowing dashboards to distinguish the latest state from the history of changes.

Trusted market-state reconciliation uses deterministic source selection and a median reference. This is a specific market-data capability; it is not proof of a complete platform-wide trusted-runtime-state engine.

## Failure handling

Malformed or invalid records can be isolated while other inputs continue. Source-governance transitions retain degradation evidence. Reconciliation discrepancies are recorded and surfaced without necessarily failing the reconciliation workflow. Promotion rejection is an expected policy result, not automatically an orchestration failure.

Some audit or lineage helpers are best effort, whereas final ML decision-evidence persistence is required for the training wrapper to complete successfully. These differing boundaries prevent a claim that every platform operation has an atomic evidence write.

## Evidence boundary

Implementation demonstrates policy and persistence paths. Stored metrics demonstrate the captured observations. Tests demonstrate the contracts exercised by that run. None of these alone establishes complete governance coverage, immutable audit history, or a security certification.

See [decision evidence](decision-evidence.md) and [runtime-state interpretation](../operations/trusted-runtime-state.md).
