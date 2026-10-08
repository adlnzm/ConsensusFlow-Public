# Industrial metrics

These are selected **point-in-time observations**, not SLAs, throughput benchmarks, uptime claims, or proof of a complete autonomous loop. Evidence labels resolve through the [evidence index](evidence-index.md). Values retain their recorded precision; no estimated or rounded performance results are introduced.

## Runtime observations

All entries in this table come from E-RUNTIME at **7 October 2026, 06:12:15 +03:00**. The capture contains metric output in an otherwise incomplete final sample.

| Measurement | Recorded value | Producing component and meaning | What it proves | What it does not prove |
|---|---:|---|---|---|
| Live-WebSocket cumulative batch-audit rows | 1,245,184 | Governance exporter summing the batch-audit rows field for the live-WebSocket stream | The retained scrape reported this cumulative audit activity | Unique warehouse rows, throughput, losslessness, or successful end-to-end processing |
| Pending dead-letter backlog | 0 | Governance exporter counting records with pending DLQ status | No pending items were reported at this observation | No historical errors, no abandoned items, complete recovery, or no data loss |
| Bitcoin random-forest registrations | 6 | ML exporter counting registry rows for that coin and model family | Registered-model records were observed | Successful promotion, artifact usability, or live inference |
| Bitcoin XGBoost registrations | 6 | ML exporter counting registry rows for that coin and model family | Registered-model records were observed | Successful promotion, artifact usability, or live inference |
| Bitcoin decisions labelled not promoted | 6 | ML exporter counting promotion-log entries labelled false for that coin | Explicit non-promotion decisions were recorded | A failed training run, a measured production-model count, or the reason for every rejection |

Other coin-labelled registration and non-promotion observations are present in the private capture. They are not aggregated here into a new performance metric. Missing production-model series are not converted into a numerical count.

## dbt execution

| Evidence | Recorded result | Producing component and time | What it proves | What it does not prove |
|---|---|---|---|---|
| E-DBT-RUN | Latest-market mart status: success | dbt run-results artifact generated 7 October 2026 at 08:26:56.609353 +03:00 | That model execution reported success | A full-project build, all tests passing, source correctness, or ML feature eligibility |

The retained artifact is scoped to the recorded model execution. Generated SQL and private run arguments are not reproduced.

## dbt freshness

E-DBT-FRESHNESS was generated on **7 October 2026 at 07:23:31.958091 +03:00**. The individual source checks recorded the following times:

| Source role | Status | Observation time, +03:00 | Producing component | Interpretation and limit |
|---|---|---|---|---|
| Consensus observations | pass | 07:23:31.809913 | dbt source freshness | The configured check passed then; no permanent freshness guarantee follows |
| Market snapshots | pass | 07:23:31.816308 | dbt source freshness | The configured check passed then; it does not establish source accuracy |
| Source-price observations | pass | 07:23:31.817851 | dbt source freshness | The configured check passed then; it does not establish complete provider coverage |

These observations occurred after the selected runtime scrape. They are not treated as one simultaneous system state.

## Historical test evidence

E-TEST-HISTORICAL records a suite timestamp of **30 September 2026, 13:06:36.887201 +03:00**.

| Measurement | Recorded value | Producer | What it proves | What it does not prove |
|---|---:|---|---|---|
| Passed tests | 229 | pytest console summary | Those cases passed in the recorded environment | Current-source correctness, production operation, or all integration boundaries |
| Skipped tests | 6 | pytest summary and JUnit XML | Integration prerequisites prevented those cases from running | Successful live-database verification |
| Failures | 0 | JUnit XML | No recorded test failures in this suite result | Absence of defects outside the tested contracts |
| Errors | 0 | JUnit XML | No recorded suite errors in this result | Successful execution of the skipped cases |

This is historical contract evidence. The source tree contains later changes, and this documentation task did not execute the private pipeline or rerun its tests.

## Measurements deliberately absent

No verified table is supplied here for end-to-end throughput, end-to-end latency, sustained availability, reconciliation totals, lineage totals, acquisition-validity totals, or successful learned-model serving. Narrative values without an attributable stored result are omitted rather than estimated.
