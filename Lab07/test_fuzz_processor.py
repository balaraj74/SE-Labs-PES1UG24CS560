from hypothesis import given, strategies as st, settings, Verbosity
import pytest
from processor import validate_height_and_fastpass, compute_dispatch_throughput, resolve_safety_restraint_code

# ---------------------------------------------------------
# Part A: Robustness Fuzzing (Safe Handling of Arbitrary Input)
# ---------------------------------------------------------

@settings(verbosity=Verbosity.normal, max_examples=100)
@given(st.text() | st.none())
def test_validate_height_and_fastpass_no_crash(s):
    """Ensure the function either succeeds or raises expected validation exceptions gracefully."""
    try:
        validate_height_and_fastpass(s)
    except (ValueError, KeyError, TypeError, AttributeError, IndexError):
        pass

@settings(verbosity=Verbosity.normal, max_examples=100)
@given(st.text() | st.none())
def test_compute_dispatch_throughput_safe(s):
    """Ensure throughput calculation handles arbitrary formats/zeros safely."""
    try:
        compute_dispatch_throughput(s)
    except (ValueError, ZeroDivisionError, TypeError, AttributeError, IndexError):
        pass

@settings(verbosity=Verbosity.normal, max_examples=100)
@given(st.text() | st.none())
def test_resolve_safety_restraint_code_safe(s):
    """Ensure restraint resolver handles invalid codes/lengths/types safely."""
    try:
        resolve_safety_restraint_code(s)
    except (KeyError, TypeError, AttributeError, IndexError):
        pass

# ---------------------------------------------------------
# Part B: Semantic & Property-Based Verification
# ---------------------------------------------------------

@given(st.integers(min_value=0, max_value=300), st.sampled_from(["YES", "NO", "yes", "no", "Yes", "No"]))
def test_validate_height_and_fastpass_valid_specs(height, fastpass):
    spec = f"{height}:{fastpass}"
    res = validate_height_and_fastpass(spec)
    assert f"Height {height}cm" in res
    if height >= 120:
        assert "Approved" in res
    else:
        assert "Denied" in res
    
    if fastpass.upper() == "YES":
        assert "FastPass Priority" in res
    else:
        assert "Standard Entry" in res

@given(st.floats(min_value=0.0, max_value=1000.0, allow_nan=False, allow_infinity=False),
       st.floats(min_value=0.1, max_value=120.0, allow_nan=False, allow_infinity=False))
def test_compute_dispatch_throughput_properties(riders, mins):
    metric_str = f"{riders}/{mins}"
    rate = compute_dispatch_throughput(metric_str)
    expected = round(riders / mins, 2)
    assert rate == expected

@given(st.sampled_from(["CST", "WTR", "DRP", "WHL"]), st.text(alphabet="0123456789_ABCXYZ", min_size=0, max_size=10))
def test_resolve_safety_restraint_code_known_prefixes(prefix, suffix):
    code = f"{prefix}_{suffix}"
    expected_map = {
        "CST": "Over-the-Shoulder Harness",
        "WTR": "Lap Bar and Seatbelt",
        "DRP": "Hydraulic Shoulder Vest",
        "WHL": "Manual Safety Bar"
    }
    res = resolve_safety_restraint_code(code)
    assert res == expected_map[prefix]
from unittest.mock import patch
import processor

def test_main_cli_execution():
    """Test CLI main interactive loop with mocked user inputs."""
    with patch('builtins.input', side_effect=["140:YES", "50/2.0", "CST_01"]), \
         patch('builtins.print') as mock_print:
        processor.main()
        assert mock_print.called
