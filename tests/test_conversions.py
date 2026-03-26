from energy_audit_toolkit.conversions import kw_to_ton, ton_to_kw


def test_kw_to_ton():
    assert round(kw_to_ton(3.517), 3) == 1.000


def test_ton_to_kw():
    assert round(ton_to_kw(1.0), 3) == 3.517