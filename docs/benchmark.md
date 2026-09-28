# Benchmark

Focus queries: yesterday that game, ballet-related setting, deprecated combat vs new combat, last week's music decision, unnamed prior game.

## Metrics

- Recall@k, temporal accuracy, state accuracy, tokens, latency
- **Fill precision:** fraction of non-null tags licensed by the surface query
- **False fill:** tags that would filter out a gold memory

Do not treat `filled_tags` count as quality. A higher fill rate can be worse if the extra fields are guessed.

Issue #5 clean vs P0: 24 → 28 filled. The gain included `creative_project`, inherited `game`, and `topic=[game]`. Those are not automatic wins.
