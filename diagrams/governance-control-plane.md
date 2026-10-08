# Governance control plane

The diagram groups implemented evidence surfaces. The unified runtime interpretation is a target beyond the individual records currently available.

```mermaid
flowchart LR
    Acquisition[Acquisition attempts] --> Audit[Batch and source audit]
    Stream[Stream processing] --> Attempts[Attempt dispositions]
    Observations[Persisted observations] --> SourceState[Freshness and coverage state]
    SourceState --> Transitions[Source transition evidence]
    Observations --> Reconcile[Cross-database reconciliation]
    Observations --> Trusted[Deterministic market-state reconciliation]
    Training[Candidate lifecycle] --> Decisions[ML decision evidence]
    Decisions --> Promotion[Promotion policy and registry state]
    Turns[Conversational turns] --> TurnEvidence[Outputs and evidence snapshots]
    Audit --> Visibility[API and monitoring surfaces]
    Attempts --> Visibility
    SourceState --> Visibility
    Reconcile --> Visibility
    Decisions --> Visibility
    TurnEvidence --> Visibility
    Visibility -. roadmap .-> Runtime[Unified trusted runtime interpretation]
    Runtime -. roadmap .-> Recovery[Evidence-led recovery and replay decisions]
```

Current market trust, source freshness, processing success, model eligibility, and conversational grounding are different questions. A single green task status cannot replace their evidence.

See [governance model](../docs/governance/governance-model.md).
