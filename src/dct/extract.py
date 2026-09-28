from __future__ import annotations

import re
from datetime import datetime

from dct.schema import MemoryEvent, QueryTags
from dct.temporal import resolve_relative_time

_DOMAIN = {"게임": "game", "비즈니스": "business", "프로그래밍": "programming", "디자인": "design", "연구": "research"}
_TOPIC = {"전투": "combat", "음악": "music", "스토리": "story", "캐릭터": "character", "세계관": "lore", "발레": "ballet"}
_INTENT = {"바꾸": "modify", "수정": "modify", "다시": "recall", "보자": "recall", "비교": "compare", "결정": "decide"}
_STATE_EXCLUDE = {"폐기": "deprecated", "버린": "rejected"}


def extract_query_tags(text: str, now: datetime | None = None) -> QueryTags:
    tags = QueryTags(temporal=resolve_relative_time(text, now))
    for ko, slug in _DOMAIN.items():
        if ko in text:
            tags.domain = slug
    tags.topic = [slug for ko, slug in _TOPIC.items() if ko in text]
    for ko, slug in _INTENT.items():
        if ko in text:
            tags.intent = slug
            break
    tags.exclude_state = [slug for ko, slug in _STATE_EXCLUDE.items() if ko in text]
    if "프리마" in text or "Prima" in text:
        tags.project_id = "project-prima"
        tags.entities.append("Project Prima")
    return tags


def event_from_text(memory_id: str, text: str, created_at: datetime, project_id: str | None = None) -> MemoryEvent:
    q = extract_query_tags(text, created_at)
    return MemoryEvent(
        id=memory_id,
        created_at=created_at,
        text=text,
        summary=text[:180],
        project_id=project_id or q.project_id,
        domain=q.domain,
        topic=q.topic,
        intent=q.intent,
        temporal=q.temporal or None,
    )
