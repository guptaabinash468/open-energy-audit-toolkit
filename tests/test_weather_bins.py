import pandas as pd
from energy_audit_toolkit.weather_bins import create_temperature_bins


def test_create_temperature_bins():
    df = pd.DataFrame({"temp_f": [61, 62, 66, 67, 72]})
    result = create_temperature_bins(df, "temp_f", 5)

    assert "temperature_bin" in result.columns
    assert "hours" in result.columns
    assert result["hours"].sum() == 5