# Tag Schema

Dimensions: temporal, entity, domain, topic, intent, state, importance, relation.

Never store `#어제` alone. Keep surface text plus an absolute interval.

| surface | range |
|---|---|
| 방금 / 아까 | last 2 hours |
| 어제 | previous calendar day |
| 지난주 | previous Mon–Sun |
| 최근 | last 14 days |
| 저번에 | last 14 days, or null + ambiguity |
| 몇 달 전 | 60–120 days ago |
| 예전에 / 전에 | before 90 days |

Closed domain vocab: `game`, `business`, `programming`, `design`, `research`. No free labels such as `creative_project`.

`topic` is not `domain`. `game` is a domain. Do not copy it into `topic`.

A tag that is not licensed by the current surface string stays null. Discourse/history inheritance is a separate mode, not default parse.

## Modifier scope

`몇 달 전에 폐기했던 설정 말고 새 전투 설정`

- time window describes the excluded event
- keep-set is `topic=combat` AND `state != deprecated`
- do not AND the months-ago window onto the active event
- `temporal_scope: exclude` vs default `keep`
