from src.item import Item


class KeyboardMixin:
    """
    Миксин, представляющий функциональность изменения раскладки клавиатуры.
    """

    def __init__(self):
        """
        Инициализация объекта KeyboardMixin.
        """
        self.__language = "EN"

    @property
    def lanquage(self):
        return self.__language

    @lanquage.setter
    def lanquage(self, value):
        self.__language = value

    def change_lang(self, new_lang: str = 'RU'):
        """
        Изменяет язык клавиатуры.
            Параметры:
                new_lang (str): Новый язык клавиатуры. По умолчанию - 'RU'.
            Возвращает:
                KeyBoard: Объект KeyBoard с измененным языком.
        """
        if new_lang.lower() == 'en':
            self.__language = 'EN'
        elif new_lang.lower() == 'ru':
            self.__language = 'RU'
        else:
            raise AttributeError('AttributeError')
        return self


class Keyboard(Item, KeyboardMixin):
    """
    Класс, представляющий клавиатуру.
    """

    def __init__(self, name, price, quantity):
        """
        Инициализация объекта KeyBoard.
        Параметры:
            name (str): Название клавиатуры.
            price (float): Цена клавиатуры.
            quantity (int): Количество клавиатур.
        """
        super().__init__(name, price, quantity)
        KeyboardMixin.__init__(self)
