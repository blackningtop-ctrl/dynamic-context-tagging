# Tag Schema

Dimensions: temporal, entity, domain, topic, intent, state, importance, relation.

Never store `#어제` alone. Keep surface text plus an absolute interval when the surface licenses a range.

| surface | parse | retrieval heuristic |
|---|---|---|
| 방금 / 아까 | last 2 hours | same |
| 어제 | previous calendar day | same |
| 지난주 | previous Mon–Sun | same |
| 최근 | last 14 days | same |
| 저번에 | surface only; start/end null | optional 14-day soft prior |
| 몇 달 전 | 60–120 days ago | same |
| 예전에 / 전에 | before 90 days | same |

`저번에` does not license 14 days. Counting a forced 14-day interval as licensed_filled is a false fill if the gold memory is older.

Closed domain vocab: `game`, `business`, `programming`, `design`, `research`.
`topic` is not `domain`.
Unlicensed fields stay null.

## Modifier scope

`몇 달 전에 폐기했던 설정 말고 새 전투 설정`

- time window describes the excluded event
- keep-set is `topic=combat` AND `state != deprecated`
- `temporal_scope: exclude` vs default `keep`
