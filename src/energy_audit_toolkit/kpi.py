def sec_kwh_per_unit(total_kwh: float, production_units: float) -> float:
    """
    Calculate Specific Energy Consumption (SEC).

    SEC = total_kwh / production_units
    """
    if total_kwh < 0:
        raise ValueError("total_kwh cannot be negative")
    if production_units <= 0:
        raise ValueError("production_units must be greater than zero")
    return total_kwh / production_units


def eui_kwh_per_sqft(total_kwh: float, area_sqft: float) -> float:
    """
    Calculate Energy Use Intensity (EUI).

    EUI = total_kwh / area_sqft
    """
    if total_kwh < 0:
        raise ValueError("total_kwh cannot be negative")
    if area_sqft <= 0:
        raise ValueError("area_sqft must be greater than zero")
    return total_kwh / area_sqft