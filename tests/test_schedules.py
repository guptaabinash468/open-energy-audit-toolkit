import pandas as pd
from energy_audit_toolkit.schedules import filter_occupied_hours


def test_filter_occupied_hours():
    df = pd.DataFrame(
        {
            "timestamp": [
                "2026-03-16 05:00:00",  # Monday, before occupied hours
                "2026-03-16 06:00:00",  # Monday, included
                "2026-03-16 12:00:00",  # Monday, included
                "2026-03-16 18:00:00",  # Monday, excluded
                "2026-03-21 10:00:00",  # Saturday, excluded
            ]
        }
    )

    result = filter_occupied_hours(df, "timestamp", 6, 18)
    assert len(result) == 2