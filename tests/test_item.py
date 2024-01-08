# tests/test_item.py

from src.item import item

def test_calculate_total_price():
    item1 = item("Смартфон", 10000, 20)
    item2 = item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item.pay_rate = 0.8
    item1 = item("Смартфон", 10000, 20)
    item2 = item("Ноутбук", 20000, 5)

    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000

def test_all_items_list():
    # Очищаем список перед каждым тестом
    item.all = []

    item1 = item("Смартфон", 10000, 20)
    item2 = item("Ноутбук", 20000, 5)

    assert len(item.all) == 2
    assert item.all[0].name == "Смартфон"
    assert item.all[0].price == 10000
    assert item.all[0].quantity == 20

    assert item.all[1].name == "Ноутбук"
    assert item.all[1].price == 20000
    assert item.all[1].quantity == 5

def test_repr():
    item1 = item("Смартфон", 10000, 20)
    assert repr(item1) == "item(name='Смартфон', price=10000, quantity=20)"

def test_str():
    item1 = item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон - $10000 (Quantity: 20)"