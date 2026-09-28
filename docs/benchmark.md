# Benchmark

Parse score: licensed_filled / false_fill. filled_tags is not quality.

Retrieval for `저번에`: domain filter, no 14-day AND.
Soft recency `exp(-age/14)` is implemented in `rerank(..., recency_half_life=14)` and **off by default**.

Synthetic result 2026-09-28: hard filter drops 20/45/90. Soft boost keeps 90 in-set but lowers MRR when nearer same-domain memories exist.
