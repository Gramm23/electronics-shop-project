from src.item import Item
import pytest
from unittest.mock import patch, mock_open


@pytest.fixture
def item_class():
    return Item('Смартфон', 12.5, 15)


def test_calculate_total_price(item_class):
    assert item_class.calculate_total_price() == 187.5


def test_apply_discount(item_class):
    item_class.pay_rate = 0.5
    item_class.apply_discount()
    assert item_class.price == 6.25


def test_name_setter():
    item = Item('LongNameProduct', 10.0, 5)
    item.name = "LongNameProduct"
    assert item.name == 'LongNamePr'

    item.name = 'ShortName'
    assert item.name == 'ShortName'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number("123") == 123
    assert Item.string_to_number("3.14") == 3
    assert Item.string_to_number("42.0") == 42

