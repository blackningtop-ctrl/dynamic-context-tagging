from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
import json

from dct.extract import extract_query_tags
from dct.retrieve import rerank, tag_filter
from dct.schema import MemoryEvent, TemporalRange
from dct.store import MemoryStore

KST = timezone(timedelta(hours=9))


def load_examples() -> list[MemoryEvent]:
    path = Path(__file__).resolve().parents[2] / "data" / "examples" / "sample_memories.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    events = []
    for row in raw:
        start = datetime.fromisoformat(row["temporal"]["start"])
        end = datetime.fromisoformat(row["temporal"]["end"])
        events.append(
            MemoryEvent(
                id=row["id"],
                created_at=datetime.fromisoformat(row["created_at"]),
                text=row["text"],
                summary=row["summary"],
                project_id=row.get("project_id"),
                domain=row.get("domain"),
                topic=row.get("topic", []),
                intent=row.get("intent"),
                state=row.get("state", "active"),
                importance=row.get("importance", "medium"),
                entities=row.get("entities", []),
                temporal=TemporalRange(start, end, row["temporal"].get("surface")),
            )
        )
    return events


def run_query(store: MemoryStore, text: str, now: datetime) -> None:
    tags = extract_query_tags(text, now)
    candidates = tag_filter(store.all(), tags)
    ranked = rerank(candidates, tags)[:5]
    print(f"\nQ: {text}")
    print(f"  tags domain={tags.domain} topic={tags.topic} exclude={tags.exclude_state}")
    print(f"  top={[m.id for m in ranked]}")
    for mem in ranked:
        print(f"    - {mem.id} [{mem.state}/{mem.topic}] {mem.summary}")


def main() -> None:
    now = datetime(2026, 9, 21, 11, 0, tzinfo=KST)
    store = MemoryStore()
    for event in load_examples():
        store.upsert(event)
    queries = json.loads((Path(__file__).resolve().parents[2] / "data" / "examples" / "sample_queries.json").read_text(encoding="utf-8"))
    print(f"stored memories: {len(store)}")
    for row in queries:
        run_query(store, row["query"], now)


if __name__ == "__main__":
    main()
