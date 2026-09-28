# Benchmark

## Metrics

- Recall@k, temporal accuracy, state accuracy, tokens, latency
- licensed_filled / false_fill
- filled_tags count is not quality

A forced `저번에 → 14일` interval is a heuristic. Score it separately from licensed tags.

Falsify the 14-day heuristic with gold memories at 3, 10, 20, 45, 90 days. If 14 days drops valid golds, keep parse unresolved.
