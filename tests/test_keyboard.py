import pytest


def test_keyboard_attributes(keyboard):
    assert str(keyboard) == "Dark Project KD87A"
    assert str(keyboard.language) == "EN"


def test_change_language(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"

    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"


def test_set_unsupported_language(keyboard):
    with pytest.raises(AttributeError) as e:
        keyboard.language = 'CH'

    assert str(e.value) == "property 'language' of 'KeyBoard' object has no setter"
