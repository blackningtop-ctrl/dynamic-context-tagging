from __future__ import annotations

from dct.schema import MemoryEvent


class MemoryStore:
    def __init__(self) -> None:
        self._items: dict[str, MemoryEvent] = {}

    def upsert(self, event: MemoryEvent) -> None:
        self._items[event.id] = event

    def all(self) -> list[MemoryEvent]:
        return list(self._items.values())

    def get(self, memory_id: str) -> MemoryEvent | None:
        return self._items.get(memory_id)

    def __len__(self) -> int:
        return len(self._items)
