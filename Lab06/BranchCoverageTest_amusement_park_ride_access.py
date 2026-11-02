import pytest
from amusement_park_ride_access import process_ride_admissions, inspect_safety_restraints

def test_branch_validation_and_types():
    # Test valid and invalid types to cover both True and False branches of type checks
    with pytest.raises(ValueError):
        process_ride_admissions("invalid_type", 5.0)
    with pytest.raises(ValueError):
        process_ride_admissions([], -1.0)

def test_branch_open_status_and_defaults():
    # False branch for is_open (continue)
    closed_group = [{"is_open": False, "ride_type": "family"}]
    res_closed = process_ride_admissions(closed_group, 5.0)
    assert res_closed["status"] == "ZERO_ADMISSIONS"

    # True branch for is_open with default values
    open_default = [{"is_open": True}]
    res_default = process_ride_admissions(open_default, 0.0)
    assert res_default["status"] == "ZERO_ADMISSIONS"

def test_branch_ride_type_branches():
    # roller_coaster branch
    g_rc = [{
        "is_open": True,
        "ride_type": "roller_coaster",
        "has_fast_lane": True,
        "patrons": [{"height_cm": 150, "health_warning": False, "is_child": False}]
    }]
    res_rc = process_ride_admissions(g_rc, 5.0)
    assert res_rc["total_revenue"] == 30.0

    # water_ride branch
    g_wr = [{
        "is_open": True,
        "ride_type": "water_ride",
        "has_fast_lane": False,
        "patrons": [{"height_cm": 130, "health_warning": False, "is_child": False}]
    }]
    res_wr = process_ride_admissions(g_wr, 0.0)
    assert res_wr["total_revenue"] == 18.0

    # family branch
    g_fam = [{
        "is_open": True,
        "ride_type": "family",
        "has_fast_lane": False,
        "patrons": [{"height_cm": 130, "health_warning": False, "is_child": True}]
    }]
    res_fam = process_ride_admissions(g_fam, 0.0)
    assert res_fam["total_revenue"] == 6.0

    # else branch (unknown ride_type)
    g_unknown = [{"is_open": True, "ride_type": "haunted_house"}]
    res_unknown = process_ride_admissions(g_unknown, 0.0)
    assert res_unknown["status"] == "ZERO_ADMISSIONS"

def test_branch_patron_conditions():
    # height <= 0 branch
    g1 = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [{"height_cm": 0}]
    }]
    assert process_ride_admissions(g1, 0.0)["total_revenue"] == 0.0

    # has_health_warning in roller_coaster (break branch)
    g2 = [{
        "is_open": True,
        "ride_type": "roller_coaster",
        "patrons": [{"height_cm": 150, "health_warning": True}]
    }]
    assert process_ride_admissions(g2, 0.0)["total_revenue"] == 0.0

    # has_health_warning in non-roller_coaster (group_total += 0.0 branch)
    g3 = [{
        "is_open": True,
        "ride_type": "water_ride",
        "patrons": [{"height_cm": 150, "health_warning": True}]
    }]
    assert process_ride_admissions(g3, 0.0)["total_revenue"] == 0.0

    # height < 120 (continue branch)
    g4 = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [{"height_cm": 110, "health_warning": False}]
    }]
    assert process_ride_admissions(g4, 0.0)["total_revenue"] == 0.0

def test_branch_safety_audit_and_completed_status():
    # rejected_patrons > 4 branch
    g_audit = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [{"height_cm": -1} for _ in range(5)]
    }]
    assert process_ride_admissions(g_audit, 0.0)["status"] == "SAFETY_AUDIT"

    # normal completed branch
    g_comp = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [{"height_cm": 140, "is_child": False}]
    }]
    assert process_ride_admissions(g_comp, 0.0)["status"] == "COMPLETED"

def test_branch_safety_restraints():
    # not restraint_streams branch
    assert inspect_safety_restraints([]) == "NO_DATA"

    # unlatched_streak >= 2 (EMERGENCY_LOCK)
    assert inspect_safety_restraints([[1, 0, 0, 1]]) == "EMERGENCY_LOCK"

    # sensor_val != 0 (resets streak) and finishes as SAFE
    assert inspect_safety_restraints([[0, 1, 0, 1, 1]]) == "SAFE"
