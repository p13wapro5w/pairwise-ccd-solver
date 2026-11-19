import pytest
from physics import ccd_solver as mod

CASES = [
    ("swept", 'm.swept_distance(10.0, 0.1) == approx(1.0)'),
    ("swept_zero", 'm.swept_distance(0.0, 0.1) == approx(0.0)'),
    ("expanded_x", 'm.expanded_extents((1.0, 1.0), (2.0, 0.0), 0.5) == approx((2.0, 1.0))'),
    ("expanded_y", 'm.expanded_extents((1.0, 1.0), (0.0, 2.0), 0.5) == approx((1.0, 2.0))'),
    ("substeps", 'm.adaptive_substeps(2.5, 0.5) == 5'),
    ("substeps_one", 'm.adaptive_substeps(0.1, 0.5) == 1'),
    ("angular", 'm.angular_sweep(10.0, 0.1) == approx(1.0)'),
    ("trigger", 'm.is_trigger(2, 2) is True'),
    ("entity", 'm.is_trigger(1, 2) is False'),
    ("mask", 'm.refresh_mask(1, 4) == 4'),
    ("push", 'm.kinematic_push(2.0, 0.5) == approx(1.0)'),
    ("normal_front", 'm.contact_normal(1.0, 3.0) == 1'),
    ("normal_back", 'm.contact_normal(3.0, 1.0) == -1'),
    ("safe", 'm.safe_position(2.0, 1.0, 0.5) == approx(2.5)'),
    ("order", 'm.deterministic_order([3, 1, 2]) == [1, 2, 3]')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
