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


def test_jeone_still_resolves():
    r = resolve_relative_time("전에 만들었던 발레", NOW)
    assert r is not None and r.surface == "전에"


def test_hard_14_drops_90_soft_keeps():
    mems = [_m("g90", 90), _m("g3", 3), _m("biz", 2, "business")]
    q = QueryTags(domain="game")
    assert {m.id for m in tag_filter(mems, q)} == {"g90", "g3"}
    hard = QueryTags(domain="game", temporal=TemporalRange(NOW - timedelta(days=14), NOW, "14"))
    hard_ids = {m.id for m in tag_filter(mems, hard)}
    assert "g90" not in hard_ids and "g3" in hard_ids


def test_soft_boost_does_not_drop_90_and_can_move_20():
    mems = [_m("g90", 90), _m("g20", 20), _m("g45", 45)]
    q = QueryTags(domain="game")
    cand = tag_filter(mems, q)
    boost = [m.id for m in rerank(cand, q, now=NOW, recency_half_life=14.0)]
    assert "g90" in boost
    assert boost.index("g20") < boost.index("g45")
    assert recency_score(_m("g20", 20), NOW) > recency_score(_m("g90", 90), NOW)
