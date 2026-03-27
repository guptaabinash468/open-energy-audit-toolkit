# Open Energy Audit Toolkit

Open Energy Audit Toolkit is a student-built open-source Python toolkit for reproducible energy audit and building or industrial energy analysis workflows.

The goal of this project is to reduce dependence on scattered spreadsheets and one-off calculations by providing simple, reusable, and transparent functions for common analysis tasks. The toolkit is intended for students, researchers, and practitioners working on energy audits, building performance, and industrial energy analysis.

## Current features

This version includes:

- kW to ton and ton to kW conversions
- Specific Energy Consumption (SEC) calculation
- Energy Use Intensity (EUI) calculation
- Occupied-hours filtering for weekday schedules
- Outdoor temperature binning
- File-based workflows using CSV and Excel
- Automated tests for core functions

## Why this project exists

Many energy-analysis workflows are still performed using isolated spreadsheets, manual calculations, and scripts that are difficult to reuse or verify. This toolkit is designed to provide a cleaner and more reproducible starting point for common engineering calculations and small analysis workflows.

## Installation

Clone the repository and install the dependencies:

```bash
py -m pip install -r requirements.txt
py -m pip install -e .
```

If you are using an activated virtual environment, you may also use:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Project structure

```text
open-energy-audit-toolkit/
│
├─ README.md
├─ requirements.txt
├─ pyproject.toml
├─ src/
│  └─ energy_audit_toolkit/
│     ├─ conversions.py
│     ├─ kpi.py
│     ├─ schedules.py
│     └─ weather_bins.py
│
├─ tests/
├─ examples/
└─ data/
```

## Core modules

### `conversions.py`

Contains basic engineering unit conversions such as:

- kW to refrigeration ton
- refrigeration ton to kW

### `kpi.py`

Contains simple energy performance indicators such as:

- SEC in kWh per unit
- EUI in kWh per square foot

### `schedules.py`

Contains weekday occupied-hours filtering for time-series style data.

### `weather_bins.py`

Contains simple temperature binning logic for outdoor air temperature analysis.

## Example usage

### SEC example

```python
from energy_audit_toolkit.kpi import sec_kwh_per_unit

sec = sec_kwh_per_unit(25000, 5000)
print(sec)
```

### Temperature bin example

```python
import pandas as pd
from energy_audit_toolkit.weather_bins import create_temperature_bins

df = pd.DataFrame({"temp_f": [61, 62, 66, 67, 72]})
bins = create_temperature_bins(df, "temp_f", 5)
print(bins)
```

## File-based examples

### 1. CSV weather example

Run:

```bash
python examples/run_weather_from_csv.py
```

This script reads weather data from:

```text
data/sample_weather.csv
```

The sample weather file uses three columns:

- `date`
- `time`
- `temp_f`

The script combines date and time into a timestamp and then creates temperature bins.

### 2. Excel KPI example

Run:

```bash
python examples/run_kpi_from_excel.py
```

This script reads analysis inputs from:

```text
data/sample_inputs.xlsx
```

The sample Excel file includes a parameter-value table such as:

- `total_kwh`
- `production_units`
- `area_sqft`

The script then calculates:

- SEC
- EUI

## Running tests

Run the automated tests with:

```bash
python -m pytest
```

## Sample outputs

The current example workflows demonstrate:

- reading weather data from CSV
- creating outdoor temperature bins
- reading KPI input values from Excel
- calculating SEC and EUI
- filtering weekday occupied hours

## Roadmap

Planned future additions may include:

- degree-day calculations
- emissions calculations
- energy cost calculations
- psychrometric helper functions
- result export to CSV or Excel
- additional example notebooks and workflows

## Version

Current public release:

- `v0.1.0` Initial release

## License

MIT License

## Author

Abinash Gupta
