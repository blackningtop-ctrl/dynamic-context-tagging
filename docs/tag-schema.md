# Tag Schema

차원: temporal, entity, domain, topic, intent, state, importance, relation.

`#어제`만 저장하지 말고 surface 표현 + 절대 구간을 함께 둔다.

|표현|변환|
|---|---|
|방금 / 아까|최근 2시간|
|어제|전일 00:00–23:59|
|지난주|지난 주 월–일|
|최근|최근 14일|
|몇 달 전|60–120일 전|
|예전에|·90일 이전|

저장 단위는 메시지가 아니라 Event.

## Modifier scope

A relative-time phrase may attach to the excluded memory, not the desired one.

Example: `몇 달 전에 폐기했던 설정 말고 새 전투 설정`

- temporal window describes the deprecated event
- the keep-set is `topic=combat` AND `state != deprecated`
- do not AND the months-ago window onto the active combat event

Record this as `temporal_scope: exclude` when the time phrase modifies the rejected clause. Default remains `temporal_scope: keep`.
