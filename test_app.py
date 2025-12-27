# test_hostel_allocation.py

from app import allocate_room


def test_premium_ac_room():
    assert allocate_room(9.5) == "Premium AC Room"


def test_ac_room():
    assert allocate_room(8.4) == "AC Room"


def test_deluxe_non_ac_room():
    assert allocate_room(7.6) == "Deluxe Non-AC"


def test_standard_room():
    assert allocate_room(6.3) == "Standard Room"


def test_not_eligible():
    assert allocate_room(5.2) == "Not Eligible"
