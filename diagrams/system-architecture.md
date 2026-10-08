# System architecture

Solid edges show implemented data or invocation relationships. The dashed Bronze branch is a roadmap target. None of the edges implies that a complete production run has been demonstrated.

```mermaid
flowchart TB
    Sources[External market observations] --> Acquire[Acquisition and normalization]
    Acquire --> Kafka[Kafka event transport]
    Kafka --> Spark[Structured Streaming]
    Spark --> PG[PostgreSQL market and governance storage]
    PG --> DBT[dbt staging and analytical marts]
    PG --> FDW[Historical prices through FDW]
    FDW --> Features[Shared feature construction]
    Features --> Train[Training and evaluation]
    Train --> Registry[Candidate registry]
    Train --> Decision[Selection and promotion decisions]
    Decision --> Registry
    Registry --> Forecast[Forecast agent]
    Features --> Forecast
    PG --> Forecast
    Forecast --> Agents[Specialist coordination and recommendations]
    PG --> Agents
    KB[Knowledge retrieval] --> Chat[Conversation and optional constrained synthesis]
    Agents --> Chat
    Acquire -. planned durability boundary .-> Bronze[Immutable Bronze archive]
    Bronze -. planned replay .-> Kafka
```

## Reading the boundaries

- dbt analytics and FDW-based ML features are separate branches.
- A registry-to-forecast edge means an artifact lookup and conditional inference path, not proven successful learned-model serving.
- Agent recommendations do not control acquisition or model promotion in this diagram.
- Kafka retention and checkpoints do not replace the planned durable raw archive.

See [system overview](../architecture/system-overview.md).
