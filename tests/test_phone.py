import pytest
from src.item import Item
from src.phone import Phone

def test_phone_creation():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test_phone_representation():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(phone) == "iPhone 14"

def test_add_phones():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 80_000, 3, 1)

    result = phone1 + phone2
    assert result.name == "iPhone 14"
    assert result.price == 120_000
    assert result.quantity == 8  # 5 + 3
    assert result.number_of_sim == 2

def test_add_phone_with_item():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("Smartphone Accessory", 10_000, 2)

    result = phone + item
    assert result.name == "iPhone 14"
    assert result.price == 120_000
    assert result.quantity == 7  # 5 + 2
    assert result.number_of_sim == 2

def test_add_item_with_phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("Smartphone Accessory", 10_000, 2)

    result = item + phone
    assert result.name == "Smartphone Accessory"
    assert result.price == 10_000
    assert result.quantity == 7  # 5 + 2

def test_invalid_phone_creation():
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        Phone("Invalid Phone", 50_000, 3, 0)
