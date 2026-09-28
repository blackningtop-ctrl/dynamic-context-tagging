# ChatGPT에 붙여넣는 글

---

DCT parse. One pass. Surface-licensed tags only.

```
QUERY_TAGS
temporal.surface:
temporal.start:
temporal.end:
temporal_scope: keep|exclude
domain:
topic: []
intent:
state_exclude: []
project_id:
entities: []
```

domain slugs: game, business, programming, design, research
topic slugs: combat, music, story, character, ballet, lore, backend
state slugs: active, considering, confirmed, deprecated, rejected
intent slugs: recall, modify, compare, continue, decide

한글 표면을 slug 필드에 넣지 말 것.
저번에: surface만. start/end null.
폐기 절의 시간: temporal_scope=exclude.

속도 테스트면 5개 연속.
끝줄: filled_tags / licensed_filled / false_fill / second_pass_queries.
