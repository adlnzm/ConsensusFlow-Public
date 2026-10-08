# Model promotion

## Separate decisions

The lifecycle distinguishes an eligible model family, a trained candidate, a registered artifact, an empirical selection, a promotion decision, and a served forecast. These are not synonyms.

Selection identifies an empirical winner and its statistical context. Promotion answers a different question: whether that challenger clears the deployment policy relative to an eligible reference. A valid outcome is to retain the current state and record why no promotion occurred.

## Policy inputs and order

| Stage | Inputs | Failure interpretation |
|---|---|---|
| Operational checks | Training success, supplied latency and optional cost observations | A hard operational failure blocks further promotion work |
| Drift | Challenger training features and reference feature distributions | Excessive distribution change can block the decision before model comparison |
| Comparative evaluation | Shared actuals, challenger/reference predictions, metric direction, strategy | Insufficient improvement, unsupported significance, or inconsistent direction prevents promotion |
| Registry designation | Selected candidate identity and artifact availability | Registry/artifact problems must not be interpreted as a successful serving deployment |

The runner supplies drift inputs and a measured latency observation. The reusable engine can skip drift when inputs are absent; documentation of the library must not imply that every possible caller enforces the same evidence requirements.

## Reference model

An existing production artifact must have a suitable independent evaluation window and compatible feature metadata. Different candidate and incumbent feature selections are handled as separate evaluation schemas. When no production model is available, the challenger is compared with contemporaneous naive persistence on the held-out targets.

## Registry and audit behavior

Model registration persists metadata and an artifact. Production designation has registry-level consistency controls, including a uniqueness constraint for the governed production identity. This does not make the filesystem, model registry, promotion log, and final decision record a single distributed transaction.

The wrapper treats final decision-evidence persistence as required for successful run completion. Promotion logging and lineage have their own error boundaries. Operators must inspect recorded model state and evidence when a run fails after candidate work.

## Observed status

The selected runtime evidence contains registered-model counters and decisions labelled as not promoted. It does not establish successful production inference. Missing production series are not published as a measured production-model count.

## Post-promotion serving

A request can still fall back because an artifact is unavailable, history is insufficient, feature compatibility fails, predictions are invalid, or matching decision evidence cannot be verified. A production flag alone is therefore insufficient evidence that a response used the learned model.

See [prediction behavior](../modules/prediction.md) and [decision evidence](../governance/decision-evidence.md).
