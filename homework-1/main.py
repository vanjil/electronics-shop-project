from src.item import item

if __name__ == '__main__':
    # Тестирование класса
    item1 = item("Смартфон", 10000, 20)
    item2 = item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000
    print(item2.calculate_total_price())  # 100000

    # Устанавливаем новый уровень цен
    item.pay_rate = 0.8
    # Применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(item.all)  # [<src.item.item object at 0x...>, <src.item.item object at 0x...>]  # Изменил путь импорта
