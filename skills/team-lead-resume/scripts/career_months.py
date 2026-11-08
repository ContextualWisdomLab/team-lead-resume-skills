#!/usr/bin/env python3
"""Count explicitly included employment months once; never decide eligibility."""
import argparse
import json
from pathlib import Path
import re


def month_number(value):
    """Parse YYYY-MM into an ordinal, rejecting partial or invalid dates."""
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}", value):
        raise ValueError("dates must use YYYY-MM")
    year, month = map(int, value.split("-"))
    if not 1 <= year <= 9999 or not 1 <= month <= 12:
        raise ValueError("invalid year or month")
    return year * 12 + month - 1


def month_text(value):
    """Format a validated ordinal as YYYY-MM."""
    year, month = divmod(value, 12)
    return f"{year:04d}-{month + 1:02d}"


def summarize(periods, as_of):
    """Return the inclusive calendar-month union and explicit exclusions."""
    cutoff = month_number(as_of)
    if not isinstance(periods, list):
        raise ValueError("input must be an array of records")
    intervals, excluded = [], []
    for index, record in enumerate(periods, 1):
        if not isinstance(record, dict) or type(record.get("include")) is not bool:
            raise ValueError(f"record {index}: include must be an explicit boolean")
        label = record.get("label", f"record-{index}")
        if not isinstance(label, str):
            raise ValueError(f"record {index}: label must be text")
        if not record["include"]:
            reason = record.get("reason")
            if not isinstance(reason, str) or not reason.strip():
                raise ValueError(f"record {index}: an exclusion needs a reason")
            excluded.append({"label": label, "reason": reason})
            continue
        if "start" not in record or "end" not in record:
            raise ValueError(f"record {index}: start and end are required; use null for current")
        start = month_number(record["start"])
        end = cutoff if record["end"] is None else month_number(record["end"])
        if start > end:
            raise ValueError(f"record {index}: start is after end")
        if end > cutoff:
            raise ValueError(f"record {index}: end is after as-of")
        intervals.append((start, end))
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    raw = sum(end - start + 1 for start, end in intervals)
    months = sum(end - start + 1 for start, end in merged)
    years, remainder = divmod(months, 12)
    return {
        "as_of": as_of,
        "method": "inclusive_calendar_month_union_not_eligibility",
        "months": months,
        "years": years,
        "remaining_months": remainder,
        "raw_included_months": raw,
        "overlap_months": raw - months,
        "unique_ranges": [{"start": month_text(start), "end": month_text(end)}
                          for start, end in merged],
        "excluded": excluded,
    }


def main():
    """Read a local JSON array and emit a reproducible calculation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="local JSON records")
    parser.add_argument("--as-of", required=True, help="reference month YYYY-MM")
    args = parser.parse_args()
    try:
        periods = json.loads(args.input.read_text(encoding="utf-8"))
        result = summarize(periods, args.as_of)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
