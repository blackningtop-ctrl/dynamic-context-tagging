from __future__ import annotations

import re
from datetime import datetime, timedelta

from dct.schema import TemporalRange

_PATTERNS = [
    (re.compile(r"방금|아까"), "hours", 2),
    (re.compile(r"어제"), "yesterday", 1),
    (re.compile(r"지난주|저번주"), "last_week", 1),
    (re.compile(r"저번에"), "unresolved", 0),
    (re.compile(r"최근"), "days", 14),
    (re.compile(r"몇\s*달\s*전|몇달\s*전"), "months_ago", 1),
    (re.compile(r"예전에|(?<!저)전에"), "before_days", 90),
]


def resolve_relative_time(text: str, now: datetime | None = None) -> TemporalRange | None:
    now = now or datetime.now().astimezone()
    for pattern, kind, n in _PATTERNS:
        match = pattern.search(text)
        if not match:
            continue
        if kind == "unresolved":
            return None
        return _range(kind, n, now, match.group(0))
    return None


def _range(kind: str, n: int, now: datetime, surface: str) -> TemporalRange:
    start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if kind == "hours":
        return TemporalRange(now - timedelta(hours=n), now, surface)
    if kind == "yesterday":
        day = start_of_today - timedelta(days=1)
        return TemporalRange(day, day.replace(hour=23, minute=59, second=59), surface)
    if kind == "last_week":
        weekday = start_of_today.weekday()
        this_monday = start_of_today - timedelta(days=weekday)
        last_monday = this_monday - timedelta(days=7)
        last_sunday = this_monday - timedelta(seconds=1)
        return TemporalRange(last_monday, last_sunday, surface)
    if kind == "days":
        return TemporalRange(now - timedelta(days=n), now, surface)
    if kind == "months_ago":
        end = now - timedelta(days=60)
        start = now - timedelta(days=120)
        return TemporalRange(start, end, surface)
    return TemporalRange(datetime.min.replace(tzinfo=now.tzinfo), now - timedelta(days=n), surface)
