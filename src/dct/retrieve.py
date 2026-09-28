from __future__ import annotations

import math
from datetime import datetime

from dct.schema import MemoryEvent, QueryTags


def tag_filter(memories: list[MemoryEvent], query: QueryTags) -> list[MemoryEvent]:
    out: list[MemoryEvent] = []
    for mem in memories:
        if query.project_id and mem.project_id and query.project_id != mem.project_id:
            continue
        if query.domain and mem.domain and query.domain != mem.domain:
            continue
        if query.topic and mem.topic and not set(query.topic) & set(mem.topic):
            continue
        if query.exclude_state and mem.state in query.exclude_state:
            continue
        if query.temporal and mem.created_at:
            ts = mem.created_at
            if ts.tzinfo is None and query.temporal.start.tzinfo is not None:
                ts = ts.replace(tzinfo=query.temporal.start.tzinfo)
            if ts < query.temporal.start or ts > query.temporal.end:
                if not (
                    mem.temporal
                    and _overlap(
                        mem.temporal.start,
                        mem.temporal.end,
                        query.temporal.start,
                        query.temporal.end,
                    )
                ):
                    continue
        out.append(mem)
    return out


def _overlap(a0, a1, b0, b1) -> bool:
    return a0 <= b1 and b0 <= a1


def recency_score(mem: MemoryEvent, now: datetime, half_life_days: float = 14.0) -> float:
    age = (now - mem.created_at).total_seconds() / 86400.0
    if age < 0:
        age = 0.0
    return math.exp(-age / half_life_days)


def rerank(
    memories: list[MemoryEvent],
    query: QueryTags,
    now: datetime | None = None,
    recency_half_life: float | None = None,
) -> list[MemoryEvent]:
    def score(mem: MemoryEvent) -> float:
        s = 0.0
        if query.project_id and mem.project_id == query.project_id:
            s += 3.0
        s += 1.5 * len(set(query.topic) & set(mem.topic))
        if query.domain and mem.domain == query.domain:
            s += 1.0
        if mem.importance == "high":
            s += 0.5
        if mem.importance == "critical":
            s += 1.0
        if mem.state == "deprecated":
            s -= 1.0
        if recency_half_life and now is not None:
            s += recency_score(mem, now, recency_half_life)
        return s

    return sorted(memories, key=lambda m: (score(m), m.id), reverse=True)
