from __future__ import annotations
from datetime import datetime, timedelta, timezone
from dct.retrieve import rerank, tag_filter
from dct.schema import MemoryEvent, QueryTags, TemporalRange

KST = timezone(timedelta(hours=9))
NOW = datetime(2026, 9, 28, 12, 0, tzinfo=KST)
AGES = (3, 10, 20, 45, 90)

def _mem(mid, days, domain="game"):
    return MemoryEvent(id=mid, created_at=NOW - timedelta(days=days), text="game talk", domain=domain)

def pool(gold_age, near):
    gold = _mem(f"gold-{gold_age}", gold_age)
    others = [_mem("d-30", 30), _mem("d-60", 60), _mem("d-200", 200), _mem("biz-4", 4, "business")]
    if near:
        others = [_mem("d-1", 1), _mem("d-7", 7), *others]
    return [gold, *others]
