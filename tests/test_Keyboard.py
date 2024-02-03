from src.keyboard import Keyboard
import pytest

@pytest.fixture
def keyboard_instance():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_str_representation(keyboard_instance):
    assert str(keyboard_instance) == "Dark Project KD87A"

def test_default_language(keyboard_instance):
    assert keyboard_instance.language == "EN"

def test_change_language(keyboard_instance):
    keyboard_instance.change_lang()
    assert keyboard_instance.language == "RU"

    keyboard_instance.change_lang()
    assert keyboard_instance.language == "EN"

def test_set_language_directly(keyboard_instance):
    keyboard_instance.language = 'RU'
    assert keyboard_instance.language == "RU"

    with pytest.raises(ValueError):
        keyboard_instance.language = 'CH'

def test_change_language_cycle(keyboard_instance):
    assert keyboard_instance.language == "EN"

    keyboard_instance.change_lang()
    assert keyboard_instance.language == "RU"

    keyboard_instance.change_lang()
    assert keyboard_instance.language == "EN"

def test_invalid_language(keyboard_instance):
    with pytest.raises(ValueError):
        keyboard_instance.language = 'InvalidLanguage'
