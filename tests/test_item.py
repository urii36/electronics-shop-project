"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture
def item1():
    item = Item("Ноутбук", 10000, 20)
    return item
def test_item1_name(item1):
    assert item1.name == 'Ноутбук'


def test_item1_name_change(item1):
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


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

