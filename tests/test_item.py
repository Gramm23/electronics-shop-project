from src.item import Item
from src.phone import Phone
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


def test_item(item_class):
    assert repr(item_class) == "Item('Смартфон', 12.5, 15)"
    assert str(item_class) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_add_invalid():
    item1 = Item("Смартфон", 10000, 20)

    with pytest.raises(ValueError):
        item1 + 1000




