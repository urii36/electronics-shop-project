import csv
import os

from src.config import ITEMS_CSV_PATH
from src.instantiatecsverror import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        создание экземпляра класса item.
        """
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.name, self.price, self.__quantity}'

    def __str__(self):
        return self.__name

    @property
    def name(self) -> str:
        """
        Название товара.
        """
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """
        Устанавливает название товара.
        Если длина названия превышает 10 символов, обрезает его до первых 10 символов.
        :param value: Новое название товара.
        """
        self.__name = value if len(value) <= 10 else value[:10]

    @property
    def price(self) -> float:
        """
        Получает количество товара в магазине.

        """
        return self.__price

    @property
    def quantity(self) -> int:
        """
        Получает цену за единицу товара.

        :return: Цена за единицу товара.
        """
        return self.__quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.__quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.__price *= self.pay_rate

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Преобразует числовую строку в число.

        :param value: Числовая строка.
        :return: Преобразованное число.
        """
        return int(float(value))

    @classmethod
    def instantiate_from_csv(cls, path=ITEMS_CSV_PATH) -> None:
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Отсутствует файл {path.split('/')[-1]}")

            cls.all.clear()
            with open(path, 'r', encoding='windows-1251') as file:
                file_reader = csv.DictReader(file, delimiter=',')

                for row in file_reader:
                    if set(row) != {'name', 'price', 'quantity'}:
                        raise InstantiateCSVError(path)
                    cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))

        except FileNotFoundError:
            raise
        except Exception:
            raise InstantiateCSVError(path)
