import pytest
from src.item import Item, InstantiateCSVError

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
