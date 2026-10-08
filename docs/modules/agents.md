# Agents and conversational intelligence

## Purpose and orchestration

The coordinator routes requests to specialist analyses and combines their structured outputs. Keyword-based routing and concurrent specialist execution are implemented; an autonomous agent that controls the entire acquisition-to-model lifecycle is not established.

## Specialist roles

| Specialist | Evidence consumed | Interpretation |
|---|---|---|
| Price | Persisted market and source observations | Current price context and source comparison |
| Risk | Historical price/return observations | Realized risk statistics with data-dependent assumptions |
| Anomaly | Price history and cross-source disagreement | Statistical anomaly signals |
| Data quality | Governance observations | Composite interpretation of data trust signals |
| Forecast | Market history, registry, features, decision evidence | Conditional model attempt or labelled baseline |
| Cross-reference | Historical observations through FDW | Historical comparisons |
| Portfolio | Returns across the requested basket | Covariance-aware portfolio statistics |
| Sentiment | Technical market inputs | Explicit momentum proxy, not news/social sentiment |
| Recommendation | Specialist evidence | Rule-based watch/hold/caution synthesis |
| Memory | Session context and optional market-event retrieval | Conversation continuity and analogous-event context |

## Contracts and failure handling

Specialists share an envelope containing data, status, confidence, and warnings. Confidence is a component-produced indicator; it is not automatically a calibrated probability. Partial failures remain visible rather than requiring every specialist to succeed before any useful response is returned.

Recommendations consume structured results and their limitations. They are auditable rules, not a learned trading policy, order-execution engine, or guarantee of investment performance.

## Knowledge retrieval and synthesis

Knowledge ingestion stores document and chunk provenance. Retrieval applies source/topic/coin filtering and can rank by embeddings or lexical matching. Retrieved passages retain evidence identities and are treated as untrusted excerpts.

The conversation layer resolves coin context, records turns, invokes specialists, and assembles a deterministic reply. Optional synthesis selects from an evidence catalogue; validation rejects unsupported identities or altered claims. Missing configuration, unavailable evidence, or synthesis failure returns to the deterministic path.

## Evidence limits

Code and tests establish routing, validation, and failure-handling mechanisms. They do not prove universal grounding, calibrated confidence, an independently verified financial conclusion, or an autonomous end-to-end operational loop. A claim can exactly match its catalogue entry while still inheriting stale or incorrect upstream evidence.

See [decision evidence](../governance/decision-evidence.md) and [runtime state](../operations/trusted-runtime-state.md).
