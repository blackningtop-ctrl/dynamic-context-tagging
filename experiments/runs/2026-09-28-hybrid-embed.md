# Hybrid filter + real embeddings

Model: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
Set: same 17 memories / 5 queries as the BOW run.

| query | R@5 vec | R@5 hyb | cand | gold drop |
|---|---|---|---|---|
| yesterday combat | 1 | 1 | 17→1 | 0 |
| old ballet | 0 | 1 | 17→2 | 0 |
| new combat not deprecated | 1 | 1 | 17→6 | 0 |
| last week music | 1 | 1 | 17→2 | 0 |
| prior game | 1 | 1 | 17→9 | 0 |

macro R@5 0.800 → 1.000
mean cand 17 → 4
mean tok 170 → 41

Vector-only missed ballet gold and ranked deprecated combat first on query 3.
