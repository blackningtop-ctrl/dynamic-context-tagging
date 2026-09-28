from datetime import datetime, timedelta, timezone
from dct.extract import extract_query_tags
from dct.retrieve import rerank, tag_filter
from dct.schema import MemoryEvent

KST = timezone(timedelta(hours=9))


def _mem(mid, day, state="active", project="project-prima"):
    return MemoryEvent(
        id=mid,
        created_at=datetime(2026, 9, day, 12, 0, tzinfo=KST),
        text="",
        summary=mid,
        project_id=project,
        domain="game",
        topic=["combat"],
        state=state,
        importance="high",
    )


def test_exclude_deprecated_on_new_combat_query():
    now = datetime(2026, 9, 21, 11, 0, tzinfo=KST)
    q = extract_query_tags("폐기했던 설정 말고 새 전투 설정", now)
    got = [m.id for m in tag_filter([_mem("old", 2, "deprecated"), _mem("new", 20)], q)]
    assert "old" not in got and "new" in got
