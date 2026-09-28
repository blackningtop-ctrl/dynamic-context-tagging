# Benchmark

Parse: licensed_filled / false_fill. Recency OFF.
Conditional CE trigger: n>=8 or margin<0.04.

Synthetic only:
- stock 5 + MiniLM + CE: R@5 1.000 on filtered CE
- 80 template queries: always=cond R@5 0.912, 10.8% latency cut

These numbers are not generalization evidence.
Generalization wait: 50–100 owner-written queries in `data/benchmark/manual_holdout.jsonl`.
