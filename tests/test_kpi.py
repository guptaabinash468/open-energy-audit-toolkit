from energy_audit_toolkit.kpi import sec_kwh_per_unit, eui_kwh_per_sqft


def test_sec_kwh_per_unit():
    assert sec_kwh_per_unit(1000, 100) == 10


def test_eui_kwh_per_sqft():
    assert eui_kwh_per_sqft(5000, 1000) == 5