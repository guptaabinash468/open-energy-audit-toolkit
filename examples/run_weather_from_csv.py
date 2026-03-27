import pandas as pd
from energy_audit_toolkit.weather_bins import create_temperature_bins


# Read CSV file
df = pd.read_csv("data/sample_weather.csv")

# Combine date and time into one datetime column
df["timestamp"] = pd.to_datetime(df["date"] + " " + df["time"])

# Create temperature bins
bins = create_temperature_bins(df, "temp_f", 5)

print("Weather data read from CSV:")
print(df)

print("\nTemperature bins from CSV:")
print(bins)