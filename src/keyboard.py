class LayoutMixin:
    supported_languages = ['EN', 'RU']

    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'

    @property
    def language(self):
        return self._language


class Keyboard(LayoutMixin):
    def __init__(self, name, brand, price):
        super().__init__()
        self.name = name
        self.brand = brand
        self.price = price

    def __str__(self):
        return self.name
