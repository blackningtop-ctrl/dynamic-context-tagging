# Benchmark

Parse: licensed_filled / false_fill.
`저번에` retrieve: domain filter, no 14-day AND.

Recency default OFF.
If enabled, `recency_mode='tiebreak'` only. Never add recency into the primary tag score.

Synthetic 2026-09-28:
- all tag-ties + near distractors: tiebreak MRR 1.000 → 0.323 (same harm as add)
- topic gap: 90d gold stays rank 1 under tiebreak
