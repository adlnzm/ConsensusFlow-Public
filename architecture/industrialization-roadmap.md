# Industrialization roadmap

This roadmap separates implemented foundations from work needed to establish stronger operational claims. It contains no estimated completion percentages or promised delivery dates.

| Area | Implemented foundation | Next evidence required |
|---|---|---|
| Raw durability | Kafka transport, persisted observations, checkpoints, DLQ | Immutable Bronze boundary, retention policy, durability verification, and archive-to-Kafka replay |
| Processing accounting | Attempt-aware classifications and database evidence | Fault-injected validation across sink writes, audit updates, and checkpoint commits |
| Workflow handoff | Scheduled publishing, fixed wait, downstream dbt tasks | Explicit offset or batch completion barrier with failure semantics |
| Trusted runtime state | Source state, processing attempts, quality events, model and turn evidence | Unified interpretation that distinguishes current, historical, failed, and recovered observations |
| ML governance | Suitability, feature selection, evaluation, registration, promotion policy | Reproducible promotion and serving evidence tied to a compatible dataset and artifact |
| Prediction | Registered-model attempt and labelled baseline fallback | Successful inference trace proving model identity, feature compatibility, and decision provenance |
| Recovery | Eligible DLQ republishing and manual consumer paths | Replay manifests, bounded concurrency, duplicate handling, and verified recovery outcomes |
| Agents | Structured specialists, rule-based recommendations, evidence validation | Full request-level failure and provenance evaluation across deployment conditions |
| Deployment | Container, orchestration, monitoring, and CI definitions | Environment-specific deployment validation, access-control review, and restore exercises |

## Acceptance sequence

The strongest next demonstration would preserve an observation at a durable raw boundary, track it through transport and persistence, construct an eligible feature dataset, record a model decision, and show the actual serving method used in a downstream response. Every transition needs its own evidence and failure interpretation.

If the promotion decision is rejection, that is a valid governed outcome. An acceptance demonstration must report that outcome rather than silently substituting a baseline and calling it production ML inference.

## Statistical and serving hardening

Candidate comparisons currently disclose that multiplicity correction is absent. Future statistical work should preserve that qualification until an implemented, validated correction exists. Selected feature subsets must also be exercised through the actual serving compatibility checks; sharing a feature builder alone does not prove every trained artifact can serve successfully.

## Recovery and atomicity

Validate failures between publishing and audit persistence, between database writes and checkpoint progress, and between registry updates and decision-evidence persistence. These operations cross boundaries; the documentation does not claim a distributed transaction.

## Publication criterion

A roadmap item becomes a current capability only when its implementation and call sites exist. It becomes a demonstrated operational result only when an attributable stored run establishes the behavior under stated conditions. Presence of a deployment file or a planned diagram is insufficient.
