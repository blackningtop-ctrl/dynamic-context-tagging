# Benchmark

Uniform topic filter scales ~linear in N (10k → ~792 cand).
`project_id` with a fixed project size stays flat (3.4 cand at 116/1k/10k).
Topic long-tail without a rare key still tracks N.
