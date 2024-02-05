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

class MyClass(LanguageMixin):
    def __init__(self):
        super().__init__()

# Пример использования
obj = MyClass()
print(obj.language)  # Вывод: 'EN'

obj.change_lang()
print(obj.language)  # Вывод: 'RU'


