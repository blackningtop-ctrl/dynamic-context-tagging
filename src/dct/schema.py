from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class TemporalRange:
    start: datetime
    end: datetime
    surface: str | None = None


@dataclass
class QueryTags:
    domain: str | None = None
    topic: list[str] = field(default_factory=list)
    intent: str | None = None
    state: str | None = None
    project_id: str | None = None
    entities: list[str] = field(default_factory=list)
    temporal: TemporalRange | None = None
    exclude_state: list[str] = field(default_factory=list)


@dataclass
class MemoryEvent:
    id: str
    created_at: datetime
    text: str
    summary: str = ""
    project_id: str | None = None
    domain: str | None = None
    topic: list[str] = field(default_factory=list)
    intent: str | None = None
    state: str = "active"
    importance: str = "medium"
    entities: list[str] = field(default_factory=list)
    temporal: TemporalRange | None = None
    relations: list[dict[str, str]] = field(default_factory=list)
    extra: dict[str, Any] = field(default_factory=dict)
