from datetime import datetime, timedelta, timezone
from dct.retrieve import recency_score, rerank, tag_filter
from dct.schema import MemoryEvent, QueryTags, TemporalRange
from dct.temporal import resolve_relative_time

KST = timezone(timedelta(hours=9))
NOW = datetime(2026, 9, 28, 12, 0, tzinfo=KST)

def _m(mid, days, domain="game"):
    return MemoryEvent(id=mid, created_at=NOW - timedelta(days=days), text="", domain=domain)

def test_jeobeone_does_not_resolve_as_jeone():
    assert resolve_relative_time("저번에 이야기했던 게임", NOW) is None

def test_tiebreak_does_not_override_topic_gap():
    gold = _m("old-gold", 90)
    gold.topic = ["combat"]
    near = _m("near", 1)
    q = QueryTags(domain="game", topic=["combat"])
    ranked = rerank([gold, near], q, now=NOW, recency_half_life=14.0, recency_mode="tiebreak")
    assert ranked[0].id == "old-gold"
