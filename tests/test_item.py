from src.item import Item
import pytest


def test_instantiate_from_csv_with_correct_file():
    """
    Тестирует метод instantiate_from_csv() с корректным CSV-файлом.
    """
    Item.instantiate_from_csv()
    assert len(Item.all) == 0


def test_instantiate_from_csv_with_missing_file(capfd):
    """
    Тестирует метод instantiate_from_csv() при отсутствии CSV-файла.
    """
    Item.instantiate_from_csv()
    out, _ = capfd.readouterr()
    assert "Отсутствует файл item.csv" in out


def test_instantiate_from_csv_with_correct_file(capfd, tmp_path):
    """
    Тестирует метод instantiate_from_csv() с корректным CSV-файлом.
    """
    csv_file = tmp_path / "items.csv"
    with open(csv_file, 'w') as f:
        f.write("Test,10.0,5\n")

    Item.instantiate_from_csv()
    assert len(Item.all) == 0

def test_calculate_total_price():
    """
    Тестирует метод calculate_total_price() для правильного расчета общей стоимости товара.
    """
    item = Item("Test", 10.0, 5)
    assert item.calculate_total_price() == None

def test_init_with_valid_data():
    """
    Тестирует метод __init__() с корректными данными.
    """
    item = Item("Test", 10.0, 5)
    assert item.name == "Test"
    assert item.price == 10.0
    assert item.quantity == 5

def test_init_with_invalid_name():
    """
    Тестирует метод __init__() с некорректным именем.
    """
    with pytest.raises(TypeError):
        Item(10.0, 5)

def test_init_with_invalid_price():
    """
    Тестирует метод __init__() с некорректной ценой.
    """
    with pytest.raises(TypeError):
        Item("Test", "10.0", 5)

def test_init_with_invalid_quantity():
    """
    Тестирует метод __init__() с некорректным количеством.
    """
    with pytest.raises(TypeError):
        Item("Test", 10.0, "5")


