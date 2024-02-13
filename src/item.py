from csv import reader

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        # ...

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

    @classmethod
    def instantiate_from_csv(cls):
        """
        Считывает данные о товарах из CSV-файла и создает экземпляры класса Item.

        :return: Список экземпляров класса Item.
        """
        try:
            with open('items.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) != 3:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    item = cls(*row)
                    cls.all.append(item)
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError as e:
            print(e)

class InstantiateCSVError(Exception):
    """
    Исключение, возникающее при повреждении CSV-файла с данными о товарах.
    """
    pass

