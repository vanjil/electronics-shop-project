# tests/test_item.py
from src.item import Item  # Исправил имя класса на Item

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
    # Очищаем список перед каждым тестом
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

#def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "item(name='Смартфон', price=10000, quantity=20)"

#def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон - $10000 (Quantity: 20)"


#def test_instantiate_from_csv():
    Item.all = []  # Очищаем список перед тестом
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    # Добавьте проверки для остальных данных из файла
