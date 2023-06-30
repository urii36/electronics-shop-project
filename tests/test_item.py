"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture(autouse=True)
def clear_items():
    Item.all = []


@pytest.mark.parametrize(
    ['price', 'quantity', 'total_price'], (
            (10_000, 20, 200_000),
            (1_000, 5, 5_000),
            (1_000, 0, 0),
    )
)
def test_calculate_total_price(price, quantity, total_price):
    item = Item('test_item', price, quantity)
    assert item.calculate_total_price() == total_price


@pytest.mark.parametrize(
    ['discount', 'price_with_discount'], (
            (0, 10_000),
            (0.15, 8_500),
            (0.27, 7_300),
    )
)
def test_apply_discount(discount, price_with_discount):
    item = Item('test_item', 10_000, 20)
    Item.pay_rate = 1 - discount

    item.apply_discount()

    assert item.price == price_with_discount


def test_all_items():
    item1 = Item('test_1', 10_000, 20)
    item2 = Item('test_2', 20_000, 5)

    assert Item.all == [item1, item2]


def test_instantiate_from_csv():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5

    assert Item.string_to_number('5.5') == 5


def string_to_number(value: str):
    assert value == 5


@pytest.fixture
def test_item1_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


@pytest.fixture
def test_item1_str(item1):

    assert str(item1) == 'Смартфон'


def test_item1_price(item1):
    assert item1.price == 10000


def test_item1_quantity(item1):
    assert item1.quantity == 20


def test_item1_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_item1_discount(item1):
    item1.pay_rate = 0.9
    item1.apply_discount()
    assert item1.price == 9000

def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_item_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.0') == 10
    assert Item.string_to_number('10.5') == 10


