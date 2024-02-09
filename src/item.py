import csv
import os

class InstantiateCSVError(Exception):
    """Исключение для ошибок при инстанцировании из CSV файла"""
    pass

class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
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
    def instantiate_from_csv(cls, file_name: str = 'items.csv') -> None:
        file_path = os.path.join(os.path.dirname(__file__), '..', file_name)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        item = cls(row['name'], float(row['price']), int(row['quantity']))
                        cls.all.append(item)
                    except (KeyError, ValueError):
                        raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

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

    def __add__(self, other):
        if isinstance(other, Item):
            # Создаем новый экземпляр Item с учетом суммы количеств
            return Item(self.name, self.price, self.quantity + other.quantity)
        else:
            raise ValueError("Неподдерживаемый тип операнда для +: {}".format(type(other)))
