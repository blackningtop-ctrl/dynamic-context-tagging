# Tag Schema

Parse writes slugs, not surface Korean, for domain/topic/state.

Domain: game, business, programming, design, research
Topic: combat, music, story, character, ballet, lore, backend
State: active, considering, confirmed, deprecated, rejected

`전투` → combat. `폐기` → deprecated. Do not store the Korean token in those fields.

`저번에`: surface only in parse. start/end null. 14-day window is retrieval heuristic only.

Modifier scope: time on a rejected clause uses temporal_scope=exclude.
