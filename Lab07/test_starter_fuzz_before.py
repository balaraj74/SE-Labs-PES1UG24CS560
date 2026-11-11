from hypothesis import given, strategies as st
from processor import validate_height_and_fastpass, compute_dispatch_throughput, resolve_safety_restraint_code

@given(st.text() | st.none())
def test_validate_height_and_fastpass_unhandled(s):
    # Demonstrating the fuzz bug / unhandled crash on arbitrary input before defensive try-except
    validate_height_and_fastpass(s)

@given(st.text() | st.none())
def test_compute_dispatch_throughput_unhandled(s):
    # Demonstrating crash on invalid metric string before defensive try-except
    compute_dispatch_throughput(s)

@given(st.text() | st.none())
def test_resolve_safety_restraint_code_unhandled(s):
    # Demonstrating crash on invalid zone code before defensive try-except
    resolve_safety_restraint_code(s)
