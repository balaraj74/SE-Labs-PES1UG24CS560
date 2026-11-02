import pytest
from amusement_park_ride_access import process_ride_admissions, inspect_safety_restraints

def test_code_coverage_baseline():
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "has_fast_lane": False,
            "patrons": [{"height_cm": 150, "health_warning": False, "is_child": False}]
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 10.0
    assert result["status"] == "COMPLETED"

def test_invalid_parameters():
    with pytest.raises(ValueError):
        process_ride_admissions("not_a_list", 5.0)
    with pytest.raises(ValueError):
        process_ride_admissions([], -2.0)

def test_closed_groups_and_zero_admissions():
    groups = [{"is_open": False, "ride_type": "family"}]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_ADMISSIONS"

def test_ride_types_and_pricing():
    groups = [
        {
            "is_open": True,
            "ride_type": "roller_coaster",
            "has_fast_lane": True,
            "patrons": [{"height_cm": 160, "health_warning": False, "is_child": False}]
        },
        {
            "is_open": True,
            "ride_type": "water_ride",
            "has_fast_lane": False,
            "patrons": [{"height_cm": 140, "health_warning": False, "is_child": True}]
        }
    ]
    result = process_ride_admissions(groups, 10.0)
    # 25 + 10 = 35 for roller_coaster; 18 * 0.6 = 10.8 for water_ride
    assert result["total_revenue"] == 45.8
    assert result["status"] == "COMPLETED"

def test_invalid_ride_type():
    groups = [{"is_open": True, "ride_type": "ferris_wheel"}]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_ADMISSIONS"

def test_health_warning_in_roller_coaster():
    groups = [
        {
            "is_open": True,
            "ride_type": "roller_coaster",
            "has_fast_lane": False,
            "patrons": [
                {"height_cm": 0, "health_warning": False, "is_child": False},
                {"height_cm": 150, "health_warning": True, "is_child": False}
            ]
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0

def test_health_warning_and_height_limit_in_family():
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "has_fast_lane": False,
            "patrons": [
                {"height_cm": 150, "health_warning": True, "is_child": False},
                {"height_cm": 110, "health_warning": False, "is_child": True}
            ]
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0

def test_safety_audit_status():
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "has_fast_lane": False,
            "patrons": [
                {"height_cm": -1, "health_warning": False, "is_child": False},
                {"height_cm": -2, "health_warning": False, "is_child": False},
                {"height_cm": -3, "health_warning": False, "is_child": False},
                {"height_cm": -4, "health_warning": False, "is_child": False},
                {"height_cm": -5, "health_warning": False, "is_child": False}
            ]
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["status"] == "SAFETY_AUDIT"

def test_inspect_safety_restraints_flows():
    assert inspect_safety_restraints([]) == "NO_DATA"
    assert inspect_safety_restraints([[1, 0, 1, 1]]) == "SAFE"
    assert inspect_safety_restraints([[1, 0, 0, 1]]) == "EMERGENCY_LOCK"
