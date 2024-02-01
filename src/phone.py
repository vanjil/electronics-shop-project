from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, sim_slots):
        super().__init__(name, price, quantity)
        self.number_of_sim = sim_slots

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name


    def __radd__(self, other):
        if isinstance(other, Item):
            return Item(self.name, self.price, self.quantity + other.quantity)
        else:
            raise ValueError("Cannot add Phone with non-Item object")
