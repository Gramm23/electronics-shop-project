from src.phone import Phone
import pytest


def test_repr():
    phone1 = Phone("Test", 70_000, 6, 1)
    assert repr(phone1) == "Phone('Test', 70000, 6, 1)"


def test_number_of_sim_getter():
    phone = Phone("Test", 3_000, 64, 1)
    assert phone.number_of_sim == 1


def test_number_of_sim_setter():
    phone = Phone("Test", 4_000, 55, 1)
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_number_of_sim_error():
    phone = Phone("Test", 1000, 64, 1)
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
