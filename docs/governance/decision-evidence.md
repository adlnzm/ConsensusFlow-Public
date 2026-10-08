# Decision evidence

## What an evidence record explains

A useful decision record ties an outcome to its subject, data scope, policy identity, reasons, assumptions, and supporting observations. A label such as selected or promoted is insufficient without the evidence that gives it meaning.

The private ML evidence path records the governed chain: dataset context, feature-selection suitability and results, model-family suitability, evaluation suitability, candidate selection, and promotion outcome. Retrieval can connect a forecast's claimed model to this decision history.

## Lifecycle boundaries

Training begins with a persisted run identity. Candidate processing can result in trained models, an explicit skip, a rejected promotion, or an exception. The outer runner persists decision evidence before marking its run complete; an evidence-persistence exception marks the run failed.

This is not a promise that registry state and all evidence writes occur in one transaction. Promotion can occur inside the inner runner before the outer evidence write. A failure at that boundary requires inspection of both model state and run/evidence state.

The forecast path checks that retrieved evidence matches the intended coin, horizon, selected model, and model type. If prerequisites or checks fail, it serves an identified persistence baseline rather than attaching a successful learned-model claim to that result.

## Agent and conversational evidence

Specialists return a common result envelope with data, status, confidence, and warnings. The coordinator tolerates partial failures. Conversational auditing associates a turn with outputs and an evidence snapshot. Retrieved passages retain provenance and are treated as untrusted material.

Optional synthesis is constrained to selectable catalogue claims. Validation checks the evidence identity and exact claim correspondence. A rejected or unavailable synthesis path falls back to the deterministic response path. This reduces opportunities for unsupported additions; it does not independently verify that every upstream numeric input is correct.

## Public representation

The [illustrative governance schema](../../schemas/public/governance-decision.json) presents a small interface for decision stage, outcome, policy, reasons, and evidence references. It intentionally omits internal identifiers, private records, policy thresholds, database layout, and implementation details. It is not a database export or a deployed API specification.

## What evidence does not prove

Persisted evidence does not automatically establish complete coverage, tamper resistance, independent replication, or the scientific validity of every assumption. Registration is not selection; selection is not promotion; promotion is not proof that a request successfully used that artifact.
