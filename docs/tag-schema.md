# Tag Schema

Parse slugs: domain/topic/state/intent in English.

`저번에` parse: surface only, start/end null.
`저번에` retrieve default: do not AND a 14-day window. Filter with licensed tags (usually domain=game). Optional recency boost in the ranker only.

Thought-table 2026-09-28: hard 14-day window kept 2/5 golds (dropped 20/45/90). Domain-only kept 5/5.
