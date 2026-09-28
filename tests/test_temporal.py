from datetime import datetime, timedelta, timezone
from dct.temporal import resolve_relative_time

KST = timezone(timedelta(hours=9))


def test_yesterday_is_previous_calendar_day():
    now = datetime(2026, 9, 21, 11, 0, tzinfo=KST)
    r = resolve_relative_time("어제 만들던 게임", now)
    assert r is not None
    assert r.start.date().isoformat() == "2026-09-20"
