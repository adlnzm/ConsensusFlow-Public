# End-to-end flow

This diagram shows the intended composition of implemented stages, including explicit alternative outcomes. It is not evidence of one successful autonomous execution.

```mermaid
flowchart TD
    Observe[Acquire observation] --> Publish[Validate and publish]
    Publish --> Consume[Spark micro-batch]
    Publish --> PublishError[Eligible publish failure to DLQ]
    Consume --> Outcome[Classify processing outcome]
    Outcome --> Persist[Persist eligible observations]
    Outcome --> Quarantine[Invalid or quarantined input]
    Outcome --> Duplicate[Duplicate accounting]
    Outcome --> Failed[Failed-attempt accounting]
    Persist --> Analytics[dbt analytical path]
    Persist --> History[Historical FDW feature path]
    History --> Eligible{Sufficient eligible history?}
    Eligible -->|No| Skip[Record skipped training]
    Eligible -->|Yes| Train[Tune and evaluate candidates]
    Train --> Select[Select empirical candidate]
    Select --> Gate{Promotion policy passes?}
    Gate -->|No| Reject[Record non-promotion]
    Gate -->|Yes| Designate[Update production designation]
    Request[Analysis request] --> Serve{Usable model and matching evidence?}
    Designate --> Serve
    Serve -->|No| Baseline[Labelled persistence baseline]
    Serve -->|Yes| Attempt[Attempt validated model forecast]
    Attempt -->|Failure| Baseline
    Attempt -->|Valid result| Evidence[Forecast with model evidence]
    Baseline --> Response[Specialist and conversational response]
    Evidence --> Response
```

Training and analysis requests have separate triggers. The graph does not imply that each newly acquired event initiates training or that each training run results in model promotion.

See [dataflow](../architecture/dataflow.md) and [prediction](../docs/modules/prediction.md).
