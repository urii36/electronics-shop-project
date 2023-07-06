import pytest


@pytest.fixture()
def test_repr_phone(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000.0, 2, 5)"


def test_add_items(item1, phone1):
    assert item1 + phone1 == 7
    assert phone1 + phone1 == 4


def test_add_different_types(phone1):
    with pytest.raises(TypeError):
        phone1 + "Some String"


def test_set_number_of_sim(phone1):
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3


def test_set_invalid_number_of_sim(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_str_phone(phone1):
    assert str(phone1) == "iPhone 14"
