import pandas as pd
from energy_audit_toolkit.kpi import sec_kwh_per_unit, eui_kwh_per_sqft

# Read Excel input file
df = pd.read_excel("data/sample_inputs.xlsx")

# Convert the parameter/value table into a dictionary
inputs = dict(zip(df["parameter"], df["value"]))

# Read values
total_kwh = float(inputs["total_kwh"])
production_units = float(inputs["production_units"])
area_sqft = float(inputs["area_sqft"])

# Run calculations
sec = sec_kwh_per_unit(total_kwh, production_units)
eui = eui_kwh_per_sqft(total_kwh, area_sqft)

print("Inputs from Excel:")
print(df)

print("\nCalculated results:")
print(f"SEC (kWh/unit): {sec}")
print(f"EUI (kWh/sqft): {eui}")