# Dynamic Context Tagging research notes

Canonical long-form notes live in this file. Structured design docs:

- docs/hypothesis.md
- docs/architecture.md
- docs/tag-schema.md
- docs/poc-plan.md
- docs/benchmark.md
- docs/cost-simulation.md
- docs/related-work.md
- docs/roadmap.md

The source write-up is also kept locally in the conversation attachment `DYNAMIC_CONTEXT_TAGGING_RESEARCH_NOTES.md`.

Core claim: keep stored memory large while keeping per-query active context almost constant by extracting the same multi-dimensional tags from memories and queries, filtering with tags and time/state first, then running semantic search.
