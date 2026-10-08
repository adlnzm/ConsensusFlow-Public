# Feature construction

## Purpose and inputs

A shared market-frame builder supplies the training and forecasting paths. It reads historical prices through PostgreSQL FDW and constructs time-indexed market features. This is separate from dbt's analytical marts.

## Temporal contract

Historical reads constrain both observation time and ingestion time to the requested cutoff. Bars become eligible only after their full interval has elapsed. Feature rows containing unusable values are removed, and future labels are matched to the requested target time rather than assumed to be the next available row.

The serving and training paths share feature construction and a version identifier. Artifacts carry feature metadata so serving can assess compatibility rather than silently assuming that similarly named frames have the same contract.

## Engineering and selection

The feature library includes price-derived technical indicators, returns, volatility measures, and lags. The inspected shared historical-price path does not provide actual volume to the builder; availability of volume-based helper functions does not prove their use in that dataset.

Suitability policies choose a defensible feature-selection method from the development-data profile. Selection returns retained columns and method-specific evidence. Feature scores from different methods are not directly interchangeable.

## Failure handling

Insufficient usable history or an empty engineered frame prevents a normal training path. A missing target cannot be treated as an observed future price. Training reserves held-out data and applies a label embargo after target alignment.

At serving time, feature version and column checks can reject an artifact. In particular, a selected subset must be compatible with what the current serving path supplies. Sharing a builder alone does not establish that every registered candidate passes serving checks.

## Evidence boundary

These controls establish intended point-in-time eligibility and compatibility checks. They do not prove that historical data was never revised, that all upstream timestamps are genuine source-event times, or that the selected runtime evidence contains successful learned-model serving.

See [ML methodology](../ml/ml-methodology.md) and [prediction](prediction.md).
