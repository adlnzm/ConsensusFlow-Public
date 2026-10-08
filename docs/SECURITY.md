# Public repository security and disclosure policy

## Publication boundary

This repository contains curated explanations, Mermaid diagrams, reduced illustrative schemas, and short examples written for public presentation. It must not contain the private implementation, its history, runtime configuration, database migrations, orchestration code, tests, trained artifacts, database backups, raw captures, or environment-bearing reports.

Environment files, credentials, access tokens, private keys, connection strings, infrastructure addresses, account identifiers, and local filesystem paths are excluded. The explicitly authorized copyright attribution is retained in the license and repository introduction.

## Public interfaces

Schemas are educational projections, not exported internal contracts. Examples use caller-supplied illustrative values and do not connect to services. They are not substitutes for production validation, access control, or deployment guidance.

## Evidence publication

Runtime artifacts remain private. Public evidence is a carefully scoped summary naming the producing component and recorded time without copying environment details. Missing evidence remains unverified; a documentation review is not a penetration test, compliance assessment, or security certification.

## Future screenshots and dashboards

Both reserved directories currently contain only `.gitkeep`. Any future artifact must be reviewed for credentials, query text, private data, internal addresses, account names, filesystem information, and embedded datasource configuration before publication. The current ignore rules intentionally block unreviewed additions to those directories.

## Review and incident handling

Use a pull request to review the exact publication diff. Check both current contents and new Git history before merging. Deleting sensitive content from a later revision does not remove it from earlier commits.

If sensitive information is discovered, contact the repository owner privately through an already established channel. Do not reproduce a suspected secret in a public issue. No private contact details or invented reporting address are published here.
