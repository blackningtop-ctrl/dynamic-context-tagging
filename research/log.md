# Research log

## 2026-09-28 — hybrid filter holds with real embeddings

- paraphrase-multilingual-MiniLM-L12-v2 on the same 17x5 set.
- Vector-only R@5 0.800. Hybrid 1.000. Candidates and tokens drop.
- Ballet gold was the vector miss. Deprecated combat ranked first without state filter.

## 2026-09-28 — recency stays off

- Tie-break only if enabled.
