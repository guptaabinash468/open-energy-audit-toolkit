import pandas as pd


def filter_occupied_hours(
    df: pd.DataFrame,
    datetime_col: str,
    start_hour: int = 6,
    end_hour: int = 18,
) -> pd.DataFrame:
    """
    Filter a dataframe to weekday occupied hours.

    Default schedule:
    Monday-Friday
    6:00 <= hour < 18:00
    """
    if datetime_col not in df.columns:
        raise KeyError(f"Column '{datetime_col}' not found in dataframe")

    data = df.copy()
    data[datetime_col] = pd.to_datetime(data[datetime_col])

    weekday_mask = data[datetime_col].dt.weekday < 5
    hour_mask = (
        (data[datetime_col].dt.hour >= start_hour)
        & (data[datetime_col].dt.hour < end_hour)
    )

    return data[weekday_mask & hour_mask].reset_index(drop=True)