import pandas as pd
from energy_audit_toolkit.kpi import sec_kwh_per_unit
from energy_audit_toolkit.weather_bins import create_temperature_bins
from energy_audit_toolkit.schedules import filter_occupied_hours

# Example 1: SEC calculation
monthly_kwh = 25000
production_units = 5000
sec = sec_kwh_per_unit(monthly_kwh, production_units)
print("SEC (kWh/unit):", sec)

# Example 2: Temperature bins
weather_df = pd.DataFrame({
    "temp_f": [61, 62, 66, 67, 72, 74, 75, 78, 80]
})

bins = create_temperature_bins(weather_df, "temp_f", 5)
print("\nTemperature bins:")
print(bins)

# Example 3: Occupied hours filtering
schedule_df = pd.DataFrame({
    "timestamp": [
        "2026-03-16 05:00:00",
        "2026-03-16 06:00:00",
        "2026-03-16 12:00:00",
        "2026-03-16 18:00:00",
        "2026-03-21 10:00:00",
    ],
    "value": [10, 20, 30, 40, 50]
})

occupied = filter_occupied_hours(schedule_df, "timestamp", 6, 18)
print("\nOccupied hours only:")
print(occupied)