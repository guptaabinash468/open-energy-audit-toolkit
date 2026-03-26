import pandas as pd


def create_temperature_bins(
    df: pd.DataFrame,
    temp_col: str,
    bin_size: int = 5,
) -> pd.DataFrame:
    """
    Create temperature bins and return the number of hours in each bin.

    Example bin labels for 5F bins:
    60-64, 65-69, 70-74
    """
    if temp_col not in df.columns:
        raise KeyError(f"Column '{temp_col}' not found in dataframe")

    if bin_size <= 0:
        raise ValueError("bin_size must be greater than zero")

    data = df.copy()

    min_temp = float(data[temp_col].min())
    max_temp = float(data[temp_col].max())

    lower_edge = int(min_temp // bin_size) * bin_size
    upper_edge = int(max_temp // bin_size + 1) * bin_size

    bins = list(range(lower_edge, upper_edge + bin_size, bin_size))
    labels = [f"{b}-{b + bin_size - 1}" for b in bins[:-1]]

    data["temperature_bin"] = pd.cut(
        data[temp_col],
        bins=bins,
        labels=labels,
        right=False,
        include_lowest=True,
    )

    result = (
        data["temperature_bin"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    result.columns = ["temperature_bin", "hours"]

    return result