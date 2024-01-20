# src/phone.py

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        if isinstance(other, Item):
            return Item(self.name, self.price, self.quantity + other.quantity)
        raise TypeError("Unsupported operand type for +: {}".format(type(other)))

class Phone(Item):
    def __init__(self, name, price, quantity, supported_sim_cards):
        super().__init__(name, price, quantity)
        self.supported_sim_cards = supported_sim_cards

    def __add__(self, other):
        if isinstance(other, Phone):
            return Phone(self.name, self.price, self.quantity + other.quantity, self.supported_sim_cards)
        raise TypeError("Unsupported operand type for +: {}".format(type(other)))
