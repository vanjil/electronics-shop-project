# src/item.py

class Item:
    # Статическое поле для хранения всех созданных объектов Item
    all = []

    # Статическое поле для установки уровня цен
    pay_rate = 1.0

    def __init__(self, name, base_price, quantity):
        self.name = name
        self.base_price = base_price
        self.quantity = quantity
        self.price = self.calculate_total_price()
        # Добавляем текущий объект в список всех объектов
        Item.all.append(self)

    def calculate_total_price(self):
        return self.base_price * self.quantity

    def apply_discount(self):
        # Применяем скидку с использованием уровня цен
        self.price *= Item.pay_rate

if __name__ == '__main__':
    # Тестирование класса
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000
    print(item2.calculate_total_price())  # 100000

    # Устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # Применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(Item.all)  # [<__main__.Item object at 0x...>, <__main__.Item object at 0x...>]
