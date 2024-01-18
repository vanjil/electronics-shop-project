import csv
import os

class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name  # Приватный атрибут name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")
            self._name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, file_name: str) -> object:
        # Получаем абсолютный путь к файлу относительно текущего каталога
        file_path = os.path.join(os.path.dirname(__file__), '..', file_name)

        with open(file_path, 'r', encoding='utf-16') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
                cls.all.append(item)

    @staticmethod
    def string_to_number(value: str):
        return int(float(value))

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= Item.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name
