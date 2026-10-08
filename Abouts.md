# ConsensusFlow

### Governed Real-Time Crypto Data, ML & Decision Intelligence Platform

**ConsensusFlow** is an industrial-grade data and machine-learning platform for acquiring, reconciling, governing, transforming, modeling, and interpreting cryptocurrency market data.

The system is designed around a simple engineering principle:

> **Deterministic data and governance establish what is known; machine learning establishes what can be inferred; agents operate only within the evidence and permissions established by the system.**

ConsensusFlow is not designed as a collection of disconnected ingestion, analytics, ML, and chatbot components. It is designed as a **controlled data-to-decision system** in which every important state transition can be observed, reconciled, governed, traced, and eventually replayed.

---

# 1. System Objective

ConsensusFlow provides an end-to-end path from external market observations to governed predictions and decision intelligence:

```text
External Market Sources
        │
        ▼
┌───────────────────────┐
│ Acquisition Layer     │
│ API / WS / Scraping   │
│ Source fallback       │
│ Source metadata       │
└───────────┬───────────┘
            │
            ├──────────────────────┐
            │                      │
            ▼                      ▼
┌───────────────────┐    ┌──────────────────────┐
│ Bronze / Raw      │    │ Kafka Event Transport │
│ Immutable         │    │ Governed Topics       │
│ Replay Authority  │    │ Event Provenance      │
└─────────┬─────────┘    └──────────┬───────────┘
          │                         │
          │                         ▼
          │              ┌─────────────────────┐
          │              │ Spark Streaming     │
          │              │ Validation          │
          │              │ Normalization       │
          │              │ Watermarks          │
          │              │ Late Arrivals       │
          │              └──────────┬──────────┘
          │                         │
          └─────────────┬───────────┘
                        ▼
              ┌─────────────────────┐
              │ PostgreSQL          │
              │ Snapshot / TS / DQ  │
              │ Governance / ML     │
              └──────────┬──────────┘
                         │
                         ▼
                 ┌──────────────┐
                 │ dbt          │
                 │ Transform    │
                 │ Test         │
                 │ Lineage      │
                 └──────┬───────┘
                        │
                        ▼
              ┌─────────────────────┐
              │ Feature / ML Layer  │
              │ Training            │
              │ Evaluation          │
              │ Selection            │
              │ Registry             │
              │ Promotion            │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Prediction Layer    │
              │ Forecast             │
              │ Validation           │
              │ Persistence          │
              │ Monitoring           │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Decision Intelligence│
              │ Agents / RAG / KB    │
              │ Evidence-grounded    │
              │ Recommendations      │
              └─────────────────────┘
```

Cross-cutting all layers:

```text
                 ┌──────────────────────────────┐
                 │ Governance & Trusted State   │
                 ├──────────────────────────────┤
                 │ Data Quality                 │
                 │ Lineage                      │
                 │ Reconciliation               │
                 │ Batch accounting              │
                 │ Schema governance             │
                 │ Model governance              │
                 │ Audit evidence                │
                 │ Observability                 │
                 │ Security                      │
                 │ Recovery / Replay             │
                 └──────────────────────────────┘
```

---

# 2. Design Philosophy

ConsensusFlow follows six architectural principles.

## 2.1 Deterministic facts before intelligence

The system must establish reliable facts before ML or LLM-based reasoning is allowed to operate.

```text
Sources
  ↓
Validation
  ↓
Reconciliation
  ↓
Governance
  ↓
Features
  ↓
ML
  ↓
Prediction
  ↓
Agent reasoning
```

An agent should never become the mechanism by which data correctness is established.

---

## 2.2 Raw observations must remain recoverable

The Bronze layer provides the durable raw boundary.

The system should never depend exclusively on Kafka retention or transformed PostgreSQL tables for historical reconstruction.

```text
External Observation
        │
        ▼
     BRONZE
        │
        ├──► Kafka
        │
        └──► Replay / Recovery
```

Bronze therefore becomes the authoritative source for selective replay and historical reconstruction.

---

## 2.3 Every important state transition produces evidence

ConsensusFlow treats operational evidence as first-class data.

Examples include:

* acquisition attempts
* source selection
* source fallback
* schema validation
* reconciliation
* duplicate detection
* batch processing
* DLQ events
* replay attempts
* model training
* evaluation
* model selection
* promotion decisions
* prediction generation
* agent actions
* verification results

The objective is not merely:

> "Did the pipeline run?"

The objective is:

> "Can the system prove what happened?"

---

## 2.4 Failed execution is not the same as invalid data

ConsensusFlow explicitly separates:

* `started`
* `completed`
* `failed`
* `replayed`
* `recovered`
* `quarantined`
* `invalid`
* `stale`
* `superseded`

This distinction is essential to the trusted-state model.

A historical failed attempt must not automatically make a successfully recovered pipeline unhealthy.

Likewise, a started execution must not be counted as a terminal success.

---

## 2.5 Governance is upstream of intelligence

Governance is not an afterthought attached to ML or agents.

It exists throughout the pipeline:

```text
Acquisition Governance
        ↓
Schema Governance
        ↓
Transport Governance
        ↓
Data Governance
        ↓
Transformation Governance
        ↓
Feature Governance
        ↓
ML Governance
        ↓
Prediction Governance
        ↓
Agent Governance
```

---

## 2.6 Industrialization means operational proof

A component is not considered industrial merely because it exists.

ConsensusFlow distinguishes:

| State         | Meaning                                                                 |
| ------------- | ----------------------------------------------------------------------- |
| `DESIGNED`    | Architecture exists                                                     |
| `IMPLEMENTED` | Code/capability exists                                                  |
| `VALIDATED`   | Runtime/test evidence exists                                            |
| `GOVERNED`    | Evidence, ownership and controls exist                                  |
| `INDUSTRIAL`  | Failure, recovery, observability and operational behavior are validated |
| `LOCKED`      | Capability meets the project's defined production gate                  |

---

# 3. Current System

As of October 2026, ConsensusFlow already contains substantial implementation across the data, governance, ML, and agent layers.

## Current strengths

* Multi-source crypto acquisition
* Source fallback
* Deterministic acquisition metadata
* Kafka/KRaft event transport
* Schema governance
* Spark Structured Streaming
* Checkpointing
* Micro-batch processing
* Late-arrival research/validation
* PostgreSQL persistence
* Reconciliation
* Data-quality governance
* DLQ
* Replay capability
* dbt transformations
* Governance analytics
* Prometheus/Grafana foundation
* Airflow orchestration
* Celery execution foundation
* ML training
* Walk-forward evaluation
* Feature-selection suitability
* Evaluation suitability
* Model selection
* Model registry
* Promotion governance
* Production-model lookup
* Feature-version validation
* Prediction fallback behavior
* Agent coordination
* Recommendation logic
* Evidence-grounded decision architecture
* Automated test coverage across the platform

The latest full test state has reached approximately:

```text
319 passed
38 warnings
```

The exact number should always be treated as a runtime snapshot rather than a permanent project metric.

---

# 4. Industrialization Baseline

The current engineering assessment is approximately:

| Component               |     Industrialization |
| ----------------------- | --------------------: |
| Acquisition             |                  ~95% |
| Kafka                   |               ~75–80% |
| Schema                  |               ~80–85% |
| Spark                   |               ~90–95% |
| PostgreSQL              |               ~75–80% |
| dbt                     |               ~70–75% |
| Data Quality            |                  ~95% |
| Governance              | ~100% core capability |
| Governance Analytics    | ~100% core capability |
| Observability           |                  ~85% |
| Airflow                 |               ~65–70% |
| Celery                  |               ~35–40% |
| ML                      |               ~75–80% |
| ML Registry             |                  ~75% |
| ML Evaluation           |               ~80–85% |
| Predictions             |               ~60–65% |
| RAG / Vector            |               ~30–35% |
| Bronze                  |               ~10–15% |
| Replay / Backfill       |                  ~70% |
| DLQ                     |                  ~95% |
| Security / Secrets      |               ~15–20% |
| CI/CD                   |               ~55–60% |
| Deployment              |               ~40–45% |
| Infrastructure Recovery |               ~75–80% |
| Performance / Load      |                  ~50% |
| Cost Controls           |               ~25–30% |
| Agent Tools             |               ~60–65% |
| Agent Memory            |               ~20–25% |
| Agent Reasoning         |               ~55–60% |
| Agent Actions           |               ~45–50% |
| Agent Verification      |                  ~70% |
| Agent Guardrails        |                  ~70% |
| Agent Evaluation        |                  ~65% |
| E2E Agent Scenarios     |                  ~60% |
| Documentation           |               ~50–55% |

These percentages represent **engineering maturity estimates**, not test coverage percentages.

---

# 5. The Current Major Gap: Bronze

The next major architectural milestone is the Bronze layer.

Currently, Kafka and downstream databases provide substantial operational persistence. However, a fully industrial architecture requires a durable immutable raw layer independent of streaming retention.

The target becomes:

```text
                    External Sources
                          │
                          ▼
                  Acquisition Layer
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
       Bronze Object Store          Kafka
       Immutable Raw                Event Transport
             │                         │
             │                         ▼
             │                       Spark
             │                         │
             │                         ▼
             └──────────────────► PostgreSQL
                                      │
                                      ▼
                                     dbt
                                      │
                                      ▼
                                    ML
                                      │
                                      ▼
                                  Prediction
```

---

# 6. Bronze Layer Responsibilities

Bronze is responsible for preserving the acquired observation before downstream transformation changes its representation.

Bronze should preserve:

* original payload
* source
* acquisition timestamp
* event timestamp
* ingestion timestamp
* source request/response metadata where appropriate
* schema version
* acquisition method
* source reliability metadata
* correlation/run identifier
* content hash
* record identifier
* partition metadata
* validation state
* replay provenance

Bronze should **not** contain business transformations.

It is a raw preservation layer.

---

# 7. Bronze Data Model

A conceptual Bronze object should contain metadata equivalent to:

```text
record_id
source
source_type
coin_id
symbol

event_time
acquired_at
ingested_at

schema_version
payload_format

payload
payload_hash

acquisition_run_id
pipeline_run_id
correlation_id

source_status
validation_status

replay_of
replay_reason
```

The physical object layout should be partitionable by dimensions such as:

```text
bronze/
  market/
    source=<source>/
      date=<YYYY-MM-DD>/
        hour=<HH>/
          ...
```

The exact partitioning strategy should be chosen based on measured access patterns rather than prematurely fixed.

---

# 8. Bronze Format

The preferred industrial target is an object-store format that supports:

* immutable raw retention
* efficient batch access
* schema evolution
* partition pruning
* replay
* downstream Spark processing

A practical initial implementation is:

```text
S3-compatible object storage
        +
Parquet
        +
explicit metadata envelope
```

MinIO may be used locally for development and validation.

The production architecture should remain object-storage compatible rather than coupling the application to a single vendor.

---

# 9. Bronze Immutability Rule

Bronze records should not be updated in place.

Corrections happen through new evidence.

For example:

```text
Original record
      │
      ├── validation failure
      │
      └── replay
             │
             ▼
       new processing attempt
```

The original acquisition remains auditable.

This is essential for forensic analysis and reproducibility.

---

# 10. Replay Architecture

Bronze changes replay from:

```text
Kafka retention
      ↓
best-effort replay
```

to:

```text
Bronze
   ↓
select records
   ↓
replay manifest
   ↓
Kafka
   ↓
Spark
   ↓
normal downstream pipeline
```

A replay must itself be governed.

Every replay should have:

```text
replay_id
source_run
requested_by
requested_at
selection criteria
record count
reason
target pipeline
status
started_at
completed_at
failure information
```

The replay must never silently overwrite historical evidence.

---

# 11. Kafka Architecture

Kafka is the transport layer.

It should not become the only historical data store.

Current logical streams include:

```text
crypto.market.raw
crypto.market.timeseries.raw
```

The industrial target is:

```text
Bronze
   │
   ├── acquisition preservation
   │
   └── replay source

Kafka
   │
   ├── transport
   ├── decoupling
   ├── buffering
   └── stream processing
```

Kafka responsibilities:

* event transport
* decoupling
* buffering
* ordering within partitions
* consumer-group coordination
* stream replay within retention
* transport observability

Bronze responsibilities:

* durable historical preservation
* long-term retention
* forensic reconstruction
* selective replay authority

---

# 12. Spark Architecture

Spark Structured Streaming consumes governed Kafka events.

Conceptual flow:

```text
Kafka
  │
  ▼
Schema decode
  │
  ▼
Validation
  │
  ├── invalid → DLQ
  │
  ▼
Normalization
  │
  ▼
Watermark / event-time handling
  │
  ▼
Deduplication
  │
  ▼
Quality checks
  │
  ▼
Persistence
  │
  ├── market snapshot
  ├── time series
  ├── governance evidence
  └── reconciliation metadata
```

Spark must preserve enough metadata to establish:

* source offset
* partition
* batch ID
* event time
* processing time
* checkpoint state
* records processed
* records rejected
* records written

---

# 13. PostgreSQL Architecture

PostgreSQL provides the governed relational state layer.

Logical areas include:

```text
snapshot
timeseries
governance
ml
```

The database stores transformed and governed operational state rather than replacing Bronze.

Important principles:

* migrations are versioned
* ownership is explicit
* privileges are explicit
* writes are idempotent where required
* batch accounting is persisted
* reconciliation is persisted
* ML evidence is persisted
* model registry state is persisted
* prediction state is persisted

---

# 14. dbt Architecture

dbt provides the analytical transformation layer.

Target flow:

```text
PostgreSQL source tables
          │
          ▼
       staging
          │
          ▼
 intermediate models
          │
          ▼
       marts
          │
          ├── analytics
          ├── ML features
          └── governance analytics
```

dbt must provide:

* model contracts
* schema tests
* uniqueness tests
* not-null tests
* accepted-value tests
* freshness
* lineage
* documentation
* incremental strategy where justified
* performance validation

---

# 15. Data Quality Architecture

ConsensusFlow treats data quality as a measurable state.

Core dimensions:

```text
Completeness
Validity
Uniqueness
Consistency
Freshness
Accuracy / reconciliation
Anomaly detection
Schema conformity
```

A quality result should never be represented only as a log message.

Where operationally relevant, it should become structured evidence.

Example:

```text
dataset
batch_id
expected_count
observed_count
valid_count
invalid_count
duplicate_count
late_count
freshness_seconds
quality_status
```

---

# 16. Reconciliation

Reconciliation establishes whether multiple observations agree sufficiently for downstream use.

The system already uses consensus-style acquisition evidence.

Conceptually:

```text
Source A ─┐
Source B ─┼──► normalization ─► comparison ─► consensus
Source C ─┘
```

The reconciliation layer should establish:

* source count
* valid source count
* observed values
* consensus value
* spread
* spread percentage
* disagreement state
* source provenance

This is one of the defining capabilities of ConsensusFlow.

---

# 17. Governance Architecture

Governance is implemented as structured evidence rather than documentation alone.

Governance areas include:

```text
Data Governance
Schema Governance
Pipeline Governance
Batch Governance
Replay Governance
ML Governance
Model Governance
Prediction Governance
Agent Governance
```

The system should be able to answer:

> What data was used?

> Where did it come from?

> Which transformations occurred?

> Which model was selected?

> Why was it selected?

> Was it promoted?

> Which feature version was used?

> Which prediction was generated?

> What evidence supported the decision?

---

# 18. ML Architecture

The ML pipeline is governed end-to-end.

```text
Governed Data
      │
      ▼
Feature Construction
      │
      ▼
Feature Version
      │
      ▼
Training Dataset
      │
      ▼
Candidate Models
      │
      ▼
Walk-Forward Evaluation
      │
      ▼
Suitability Checks
      │
      ▼
Model Selection
      │
      ▼
Promotion Decision
      │
      ▼
Model Registry
      │
      ▼
Production Model
```

Current model governance includes:

* feature versioning
* training-run logging
* walk-forward evaluation
* evaluation windows
* minimum training bars
* label embargo
* suitability governance
* model selection evidence
* promotion decisions
* production model lookup
* fallback behavior
* latency gating

---

# 19. Model Selection

Model selection must not simply select the model with the best score from a single random split.

ConsensusFlow uses a governed selection process based on walk-forward evaluation.

Conceptually:

```text
Historical Data
      │
      ├── train window
      ├── validation window
      ├── embargo
      ├── next evaluation window
      └── repeat
             │
             ▼
       candidate metrics
             │
             ▼
      suitability checks
             │
             ▼
       selection evidence
```

The selection decision is persisted.

This enables retrospective analysis of why a model was selected.

---

# 20. Model Registry

The registry provides controlled model lifecycle management.

Target lifecycle:

```text
candidate
   ↓
evaluated
   ↓
selected
   ↓
approved
   ↓
production
   ↓
monitored
   │
   ├── retained
   ├── replaced
   └── rolled back
```

A production model must have:

* artifact
* model ID
* version
* feature version
* training run
* evaluation evidence
* promotion decision
* production state

---

# 21. Prediction Architecture

Prediction is not simply:

```python
model.predict(features)
```

A governed prediction requires:

```text
Feature version validation
        │
        ▼
Schema validation
        │
        ▼
Production model resolution
        │
        ▼
Inference
        │
        ▼
Latency validation
        │
        ▼
Prediction persistence
        │
        ▼
Prediction lineage
        │
        ▼
Monitoring
```

If the production model or feature contract cannot be safely resolved, the system must fail closed or use an explicitly governed fallback.

Fallback behavior must be observable.

---

# 22. Agent Architecture

Agents operate downstream of deterministic infrastructure.

The intended architecture is:

```text
                 Coordinator
                      │
       ┌──────────────┼───────────────┐
       ▼              ▼               ▼
   Price Agent    Risk Agent     Data Quality
       │              │               │
       └──────────────┼───────────────┘
                      ▼
              Evidence synthesis
                      │
                      ▼
              Recommendation
```

The coordinator must not manufacture missing evidence.

Price data remains grounded in deterministic system state.

Recommendation logic must distinguish:

```text
fact
inference
uncertainty
insufficient evidence
```

---

# 23. Agent Safety Model

Agents are not granted unrestricted infrastructure access.

The intended progression is:

```text
Observe
  ↓
Reason
  ↓
Plan
  ↓
Request tool
  ↓
Permission check
  ↓
Execute
  ↓
Observe result
  ↓
Verify
  ↓
Continue / stop / escalate
```

Destructive or high-impact operations require stronger controls.

Examples:

* replay
* backfill
* quarantine
* retraining
* model promotion
* rollback
* pipeline restart

---

# 24. Trusted Runtime State

Trusted state is a control-plane concept.

It must not simply count rows.

The trusted-state engine must understand execution semantics.

For each execution:

```text
started
   │
   ├── completed
   ├── failed
   ├── replayed
   ├── recovered
   └── abandoned
```

The state engine must distinguish:

```text
current failure
historical failure
recoverable failure
recovered failure
active execution
terminal execution
stale execution
```

A historical failed attempt must not automatically invalidate a recovered current state.

This is currently one of the key hardening tasks for ConsensusFlow.

---

# 25. Operational Metrics

ConsensusFlow should expose measurable operational characteristics.

## Acquisition

* acquisition attempts
* successful acquisitions
* failed acquisitions
* valid records
* invalid records
* source fallback rate
* source availability
* source latency
* acquisition freshness

## Kafka

* records produced
* records consumed
* consumer lag
* partition distribution
* throughput
* retry volume
* DLQ volume
* offset continuity
* replay volume

## Spark

* batches processed
* records per batch
* processing latency
* batch duration
* input rate
* output rate
* late records
* rejected records
* checkpoint health
* processing failures

## PostgreSQL

* insert/update throughput
* query latency
* connection utilization
* storage growth
* transaction failures
* reconciliation rate

## Data Quality

* completeness
* validity
* uniqueness
* freshness
* anomaly rate
* reconciliation exceptions

## ML

* training runs
* candidate models
* evaluation duration
* validation metrics
* selected model
* promotion rate
* rejection rate
* prediction latency
* prediction freshness
* fallback rate

## Platform Reliability

* availability
* failure rate
* recovery time
* MTTA
* MTTR
* replay success rate
* failed-run recovery rate

---

# 26. Existing Evidence Snapshot

Recent evidence has demonstrated substantial operational capability.

Representative evidence includes:

```text
dbt validation:
23 PASS
0 FAIL
0 ERROR

Reconciliation:
2,823 reconciled
0 exceptions

Lineage:
44 records

Acquisitions:
787

Valid acquisitions:
784

Full test state:
319 passed
38 warnings
```

Other validated areas include:

* ML decision evidence
* model selection evidence
* model registry integration
* production model resolution
* feature-version checks
* agent decision integrity
* coordinator routing
* recommendation safety behavior
* PostgreSQL integration
* Docker build validation
* migration validation
* Kafka producer operation
* Spark processing infrastructure
* controlled replay/recovery

These values are **historical runtime evidence**, not hard-coded acceptance thresholds.

---

# 27. Industrial Target Architecture

The long-term architecture is:

```text
                           ┌─────────────────────┐
                           │ External Sources    │
                           │ APIs / WS / Web     │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │ Acquisition         │
                           │ Validation          │
                           │ Fallback             │
                           │ Source Provenance    │
                           └──────────┬──────────┘
                                      │
                       ┌──────────────┴──────────────┐
                       │                             │
                       ▼                             ▼
             ┌──────────────────┐          ┌──────────────────┐
             │ Bronze Object     │          │ Kafka            │
             │ Storage           │          │ Event Transport  │
             │ Immutable         │          │ Governed Topics  │
             └────────┬─────────┘          └────────┬─────────┘
                      │                             │
                      │                             ▼
                      │                    ┌──────────────────┐
                      │                    │ Spark Streaming  │
                      │                    │ Validation       │
                      │                    │ DQ               │
                      │                    │ Event Time       │
                      │                    └────────┬─────────┘
                      │                             │
                      └──────────────┬──────────────┘
                                     ▼
                           ┌─────────────────────┐
                           │ PostgreSQL          │
                           │ Operational State   │
                           │ Governance          │
                           │ Time Series         │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │ dbt                 │
                           │ Staging / Marts     │
                           │ Tests / Lineage     │
                           └──────────┬──────────┘
                                      │
                         ┌────────────┴────────────┐
                         ▼                         ▼
                ┌─────────────────┐       ┌─────────────────┐
                │ Feature Store   │       │ Governance      │
                │ Feature Version │       │ Analytics       │
                └────────┬────────┘       └─────────────────┘
                         │
                         ▼
                ┌─────────────────────┐
                │ ML Training         │
                │ Evaluation          │
                │ Selection           │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Model Registry      │
                │ Promotion           │
                │ Rollback            │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Prediction          │
                │ Monitoring          │
                │ Lineage             │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ RAG / Knowledge     │
                │ Research Layer      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Agent Intelligence  │
                │ Reason / Plan       │
                │ Tool / Verify       │
                └─────────────────────┘


        ╔══════════════════════════════════════════════╗
        ║              CONTROL PLANE                  ║
        ║                                              ║
        ║ Governance • Observability • Security       ║
        ║ Lineage • Trusted State • Recovery          ║
        ║ Audit • SLOs • Alerts • Cost Controls       ║
        ╚══════════════════════════════════════════════╝
```

---

# 28. Target Repository Structure

The repository should evolve toward:

```text
ConsensusFlow/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docker-compose.yml
├── Makefile
│
├── app/
│   ├── acquisition/
│   ├── bronze/
│   ├── kafka/
│   ├── streaming/
│   ├── governance/
│   ├── reconciliation/
│   ├── features/
│   ├── ml/
│   ├── prediction/
│   ├── agents/
│   └── api/
│
├── airflow/
│   └── dags/
│
├── dbt/
│   ├── models/
│   ├── tests/
│   ├── macros/
│   ├── snapshots/
│   └── seeds/
│
├── schemas/
│   ├── avro/
│   ├── protobuf/
│   └── registry/
│
├── migrations/
│
├── scripts/
│   ├── bootstrap/
│   ├── validation/
│   ├── recovery/
│   ├── replay/
│   └── observability/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── system/
│   ├── governance/
│   ├── ml/
│   └── agents/
│
├── monitoring/
│   ├── prometheus/
│   └── grafana/
│
├── docs/
│   ├── architecture/
│   ├── adr/
│   ├── contracts/
│   ├── runbooks/
│   ├── ml/
│   └── operations/
│
└── infra/
    ├── docker/
    ├── k8s/
    └── security/
```

The exact directory structure should follow the existing implementation during migration rather than forcing a large repository rewrite.

---

# 29. Engineering Roadmap to 100%

ConsensusFlow should be industrialized in dependency order.

## Phase 1 — Durable Data Foundation

### Bronze

* object-storage abstraction
* MinIO local implementation
* immutable raw records
* partition strategy
* metadata envelope
* content hashing
* retention policy
* Bronze validation
* Bronze → Kafka replay
* replay manifests
* provenance

**Primary objective:**

> Make historical raw acquisition independently recoverable.

---

## Phase 2 — Trusted Runtime State

Fix the control-plane semantics.

Required properties:

* authoritative execution identity
* terminal-state semantics
* replay awareness
* recovery awareness
* stale-run handling
* current-state computation
* historical-state separation
* deterministic status aggregation

**Primary objective:**

> Make the system's reported health agree with its actual evidence.

---

## Phase 3 — One Complete Flow

Execute:

```text
Acquisition
    ↓
Bronze
    ↓
Kafka
    ↓
Spark
    ↓
PostgreSQL
    ↓
dbt
    ↓
Features
    ↓
ML evaluation
    ↓
Model selection
    ↓
Registry
    ↓
Prediction
```

The execution should produce one coherent evidence chain.

---

## Phase 4 — Failure Matrix

Intentionally validate:

```text
Source failure
Kafka failure
Consumer failure
Spark failure
Checkpoint recovery
PostgreSQL failure
Airflow worker failure
Celery worker failure
dbt failure
ML training failure
Model promotion failure
Prediction failure
Replay failure
```

Every failure should have:

```text
detect
→ record
→ recover
→ verify
→ report
```

---

# 30. Security Roadmap

The current `.env` architecture is suitable for development but not production.

Target:

```text
Secrets Manager / Vault
        ↓
short-lived credentials
        ↓
service identities
        ↓
least privilege
        ↓
audited access
```

Required controls:

* secret rotation
* database role separation
* Kafka authentication/authorization
* service identities
* environment separation
* credential isolation
* encrypted transport
* audit logging

---

# 31. Deployment Roadmap

Current development:

```text
Docker Compose
```

Target production deployment:

```text
Container images
      ↓
CI validation
      ↓
security scanning
      ↓
artifact registry
      ↓
deployment
      ↓
readiness checks
      ↓
controlled rollout
      ↓
post-deployment verification
```

Kubernetes is an intended production deployment target where operational requirements justify it.

---

# 32. CI/CD Target

Every significant change should eventually pass:

```text
Lint
  ↓
Unit Tests
  ↓
Integration Tests
  ↓
Governance Tests
  ↓
Data Contract Tests
  ↓
ML Tests
  ↓
Agent Tests
  ↓
Docker Build
  ↓
Security Scan
  ↓
System Test
  ↓
Deployment Gate
```

No component should be considered production-ready solely because its unit tests pass.

---

# 33. Definition of Industrial Completion

ConsensusFlow reaches its target industrial state when the system can demonstrate:

### Data

* durable raw preservation
* deterministic acquisition
* governed schemas
* reliable streaming
* replayability
* reconciliation
* quality controls

### Platform

* repeatable deployment
* recovery
* observability
* security
* resource controls
* formal SLOs

### ML

* reproducible training
* governed evaluation
* model selection
* registry
* promotion
* rollback
* prediction lineage
* monitoring

### Intelligence

* grounded retrieval
* evidence-backed reasoning
* governed tool access
* bounded actions
* verification
* persistent operational context

### Control Plane

Most importantly:

```text
The system knows what happened.
The system can prove what happened.
The system can recover from what went wrong.
The system can explain why a model or decision was produced.
```

---

# 34. Industrial Acceptance Flow

The final acceptance test should look approximately like:

```text
                    START
                      │
                      ▼
              Acquire observations
                      │
                      ▼
              Preserve in Bronze
                      │
                      ▼
              Publish to Kafka
                      │
                      ▼
              Process with Spark
                      │
                      ▼
             Validate / reconcile
                      │
                      ▼
                Persist state
                      │
                      ▼
                   dbt
                      │
                      ▼
              Build ML features
                      │
                      ▼
          Evaluate candidate models
                      │
                      ▼
              Select model
                      │
                      ▼
             Registry / promote
                      │
                      ▼
                 Predict
                      │
                      ▼
              Persist prediction
                      │
                      ▼
             Observe everything
                      │
                      ▼
              Verify trusted state
                      │
                      ▼
                     END
```

The acceptance condition is not merely that every stage returns exit code `0`.

The acceptance condition is:

```text
DATA + LINEAGE + GOVERNANCE + STATE + OBSERVABILITY
                         │
                         ▼
                   CONSISTENT
```

---

# 35. Project Positioning

ConsensusFlow is intended to demonstrate engineering capability across:

* Data Engineering
* Streaming Systems
* Data Quality
* Data Governance
* Data Warehousing
* Distributed Processing
* MLOps
* Model Governance
* Observability
* Reliability Engineering
* AI Agents
* Decision Intelligence

The project deliberately avoids treating an LLM as the core of the system.

Instead:

```text
Reliable Data
      ↓
Governed State
      ↓
Statistical / ML Intelligence
      ↓
Evidence
      ↓
Agent Reasoning
```

This architecture makes the AI layer accountable to the underlying data platform.

---

# 36. Current Priority

The next implementation milestone is:

## Bronze Layer → Trusted State → Full E2E Run

The order is intentional.

```text
1. Bronze
      ↓
2. Replay / provenance
      ↓
3. Trusted-state correction
      ↓
4. Full acquisition → prediction run
      ↓
5. Capture authoritative metrics
      ↓
6. Validate recovery
      ↓
7. Update industrialization matrix
      ↓
8. Continue remaining 100% gaps
```

No unnecessary rebuild should occur.

Existing validated capabilities should be retained and incrementally industrialized.

---

# 37. Guiding Principle

ConsensusFlow is ultimately built around one question:

> **Can a production system make a data-driven decision and subsequently prove exactly how that decision was produced, what evidence supported it, what state the system was in, and whether the result can be reproduced or recovered?**

If the answer is yes, the system is approaching true industrialization.

---

**Project:** ConsensusFlow
**Domain:** Real-Time Data Engineering · MLOps · Governance · Decision Intelligence
**Primary architecture:** Event-driven · Governed · Observable · Replayable · Evidence-based
**Development principle:** Incremental industrialization, not unnecessary reconstruction
