class LanguageMixin:
    def __init__(self):
        self._current_language = 'EN'

    @property
    def language(self):
        return self._current_language

    @language.setter
    def language(self, new_language):
        if new_language in ['EN', 'RU']:
            self._current_language = new_language
        else:
            raise ValueError("Недопустимый язык. Поддерживаемые значения: EN, RU")

    def change_lang(self):
        if self._current_language == 'EN':
            self._current_language = 'RU'
        else:
            self._current_language = 'EN'


class Keyboard(LanguageMixin):
    def __init__(self, model, baud_rate, key_count):
        super().__init__()
        self._model = model
        self._baud_rate = baud_rate
        self._key_count = key_count

    def __str__(self):
        return self._model


if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    print(str(kb))  # Вывод: Dark Project KD87A

    print(kb.language)  # Вывод: EN

    kb.change_lang()
    print(kb.language)  # Вывод: RU

    kb.change_lang()
    print(kb.language)  # Вывод: EN

    kb.language = 'CH'  # Теперь должно работать
    print(kb.language)  # Вывод: CH
