from src.item import Item
import pytest


@pytest.fixture
def item_class():
    return Item('Смартфон', 12.5, 15)


def test_calculate_total_price(item_class):
    assert item_class.calculate_total_price() == 187.5


def test_apply_discount(item_class):
    item_class.pay_rate = 0.5
    item_class.apply_discount()
    assert item_class.price == 6.25
