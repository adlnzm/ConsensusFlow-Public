# Reconciliation

## Purpose and inputs

Cross-database reconciliation compares snapshot observations with historical price observations available through PostgreSQL FDW. It evaluates the most recent settled day rather than assuming that differently sampled streams must match row for row at every instant.

## Comparison contract

Coverage is evaluated before paired price differences. The module retains price correlation as a diagnostic, while paired percentage deviation supplies the price-agreement criterion. High correlation alone would not establish equal prices, and differing sampling patterns can make correlation misleading.

The output is a per-coin reconciliation result persisted for governance/API consumption. The daily workflow also invokes separate forecast-actual reconciliation so stored forecasts can later be associated with realized outcomes.

## Design and failure handling

A mismatch is an observable governance signal rather than necessarily a scheduler exception. The reconciliation workflow records and logs discrepancies without treating every mismatch as a fatal task failure. Database or execution errors remain distinct from a completed comparison with adverse findings.

Forecast actuals are a separate evidence path from source-price agreement. Completing source reconciliation does not establish forecast accuracy, and having a forecast row does not establish that its actual target value has become available.

## Evidence boundary

The implementation establishes a comparison mechanism. The narrative reconciliation total encountered during review has no corroborating stored run artifact in the selected evidence set, so it is not published as a measured result. No claim of universal agreement or exception-free future execution follows.

See [governance model](../governance/governance-model.md) and [evidence index](../evidence/evidence-index.md).
