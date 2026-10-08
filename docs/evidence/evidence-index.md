# Evidence index

## Evidence hierarchy

1. Executable implementation and current call sites establish implemented behavior.
2. Stored runtime, database, and dbt artifacts establish point-in-time observations.
3. Tests establish contracts exercised under the recorded test conditions.
4. Documentation and comments establish intent where execution does not corroborate them.
5. File or folder presence establishes that an artifact exists, not that its capability works.

The review date is 7 October 2026. Older observations do not certify subsequent source changes. The catalogue uses public evidence labels; original runtime artifacts remain private because they contain environment information. Public readers receive a curated summary rather than an independently runnable reproduction package.

## Selected catalogue

| Public label | Retained artifact and producing component | Recorded time | Scope |
|---|---|---|---|
| E-RUNTIME | Runtime sample log; governance and ML metric exporters | 7 October 2026, final selected sample at 06:12:15 +03:00 | Cumulative audit activity, pending DLQ, registration and non-promotion observations |
| E-DBT-RUN | dbt run-results JSON; dbt executor | 7 October 2026, generated at 08:26:56.609353 +03:00 | Successful latest-market-mart execution |
| E-DBT-FRESHNESS | dbt source-results JSON; dbt freshness checks | 7 October 2026, generated at 07:23:31.958091 +03:00 | Recorded source freshness statuses and their individual observation times |
| E-TEST-HISTORICAL | Historical pytest console log and JUnit XML | 30 September 2026, suite timestamp 13:06:36.887201 +03:00 | Existing test suite with explicitly skipped integration cases |

The [metric tables](industrial-metrics.md) state the exact selected results and their limits. No current throughput, end-to-end latency, uptime, losslessness, or production-inference metric is established by these selections.

## Excluded and incomplete evidence

- Previously rejected summary metrics and their identical archived copy are excluded.
- Narrative claims about reconciliation totals, lineage counts, and acquisition-validity counts lack a corroborating run artifact in this review and are not published as measurements.
- Estimated implementation-completion percentages are not measurements.
- A directory labelled with a later date does not override the recorded timestamps of its contents.
- Empty final task-state captures cannot establish workflow completion.
- The final selected runtime sample is incomplete; only its present metric observations are used.
- Database-access collection labelled as not yet reviewed is not a security certification.

## Reuse rules

An evidence reference is usable only within its original measurement scope. A newer document can reinterpret an older observation but cannot make it a new experiment. When new material is supplied, retain its producing component, run condition, exact timestamp, units, failures, omissions, and distinction between observed and derived values.

Source code, raw records, deployment details, screenshots, and dashboard exports are not included merely to make an evidence claim appear stronger.
