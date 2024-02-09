import os
import tempfile
from src.item import Item, InstantiateCSVError
import pytest

def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("nonexistent_file.csv")

def test_instantiate_from_csv_corrupted_file():
    csv_data = "name,price\nProduct1,10.0\nProduct2,20.0"
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False, encoding='utf-8') as csv_file:
        csv_file.write(csv_data)
        csv_file_path = csv_file.name

    try:
        with pytest.raises(InstantiateCSVError):
            Item.instantiate_from_csv(csv_file_path)
    finally:
        os.remove(csv_file_path)

def test_instantiate_from_csv_corrupted_file():
    csv_data = "name,price\nProduct1,10.0\nProduct2,20.0"
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False, encoding='utf-8') as csv_file:
        csv_file.write(csv_data)
        csv_file_path = csv_file.name

    try:
        with pytest.raises(InstantiateCSVError):
            Item.instantiate_from_csv(csv_file_path)
    finally:
        os.remove(csv_file_path)


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    Item.pay_rate = 0.8  # Исправил имя класса на Item
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000

def test_all_items_list():
    Item.all = []  # Исправил имя класса на Item

    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert len(Item.all) == 2
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 10000
    assert Item.all[0].quantity == 20

    assert Item.all[1].name == "Ноутбук"
    assert Item.all[1].price == 20000
    assert Item.all[1].quantity == 5

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


