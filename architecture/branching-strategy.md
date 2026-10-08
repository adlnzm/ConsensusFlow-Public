# Branching strategy

## Independent public history

ConsensusFlow-Public is maintained independently from the private implementation. It is not a public fork, source mirror, or export of private Git history. Public commits contain intentionally authored explanations, diagrams, reduced interfaces, and illustrative examples.

## Stable branch and review branches

`main` is the reviewed public baseline. Substantial documentation changes use short-lived branches and a pull request. The initial documentation branch is `public-documentation`; subsequent changes can use descriptive documentation or correction branch names.

The review compares the proposed prose and artifacts against the private implementation and the approved evidence catalogue. It checks both disclosure risk and unsupported capability claims. A branch is eligible for deletion after its changes are integrated.

An empty repository requires a minimal initial base commit before GitHub can compare a documentation branch with `main`. Initializing that base is distinct from publishing the full documentation directly to the stable branch.

## Directories describe the system

Kafka, Spark, governance, ML, and agents belong to one integrated architecture. They are represented through documents and directory structure rather than permanent component branches. `screenshots/` and `dashboards/` are directories, not separate branches, and remain empty apart from `.gitkeep` until reviewed owner-supplied material is ready.

## Tags and evidence

Tags may identify reviewed public milestones. This initial draft does not assert a release tag. Public documentation versions and private implementation versions are separate identities: a public tag alone cannot identify the exact private executable state behind an older measurement.

When correcting evidence, preserve the distinction between the original observation and a later interpretation. A changed number must have a replacement source and scope; rewriting prose is not a new measurement.
