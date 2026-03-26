def kw_to_ton(kw: float) -> float:
    """
    Convert heat load from kW to refrigeration tons.

    1 refrigeration ton = 3.517 kW
    """
    if kw < 0:
        raise ValueError("kW cannot be negative")
    return kw / 3.517


def ton_to_kw(ton: float) -> float:
    """
    Convert refrigeration tons to kW.
    """
    if ton < 0:
        raise ValueError("Tons cannot be negative")
    return ton * 3.517