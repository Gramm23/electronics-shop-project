from src.keyboard import Keyboard
import pytest


def test_str():
    kb = Keyboard('Test', 9600, 5)
    assert str(kb) == 'Test'
    assert repr(kb) == "Keyboard('Test', 9600, 5)"
    assert str(kb.language) == "EN"


def test_change_lang():
    kb = Keyboard('Test', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_error():
    kb = Keyboard('Test', 9600, 5)

    with pytest.raises(AttributeError):
        kb.language = "CH"
