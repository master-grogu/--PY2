import doctest
from typing import Union


class Fuel:
    """
    Документация на класс.
    Класс описывает модель топлива для Ядерного реактора .
    """
    def __init__(self, quantity: Union[int, float], capacity: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Топлово"

        :param quantity: Колличество топлива
        :param capacity: Вместимость топлива в ЯР

        Примеры:
        >>> fuil = Fuel(500,1000)
        """
        if not isinstance(quantity, (int, float)):
            raise TypeError("Колличество топлива должено быть типа int или float")
        if quantity < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        self.quantity = quantity

        if not isinstance(quantity, (int, float)):
            raise TypeError("Вместимость топлива должена быть типа int или float")
        if quantity < 0:
            raise ValueError("Вместимость топлива не может быть отрицательным числом")
        self.capacity = capacity

        self.temperature = None
        self.set_temperature(power=0)  # Вызываем метод который посчитает температуру

    def set_temperature(self, power: Union[int, float]) -> None:
        """
        Функция считает и задает температуру топлива

        :param power: Мощность реактора
        :return: None

        Примеры:
        >>> fuil = Fuel(500,1000)
        >>> fuil.set_temperature(500)
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должена быть типа int или float")
        if power < 0:
            raise ValueError("Мощность не может быть отрицательным числом")
        if power == 0:
            self.temperature = 100
        else:
            self.temperature = 100 + power * 9

    def reduce_quantity(self, spent_fuel: Union[int, float]) -> None:
        """
        Функция учитывает удаление топлива
        :param spent_fuel: Потраченое топливо
        :return: None

        Примеры:
        >>> fuil = Fuel(500,1000)
        >>> fuil.reduce_quantity(200)
        """
        if not isinstance(spent_fuel, (int, float)):
            raise TypeError("Потраченое топливо должено быть типа int или float")
        if spent_fuel < 0:
            raise ValueError("Потраченое топливо не может быть отрицательным числом")
        self.quantity -= spent_fuel

    def increase_quantity(self, new_fuel: Union[int, float]) -> None:
        """
        Функция учитывает добавление топлива
        :param new_fuel: Потраченое топливо
        :return: None

        Примеры:
        >>> fuil = Fuel(500,1000)
        >>> fuil.increase_quantity(200)
        """
        if not isinstance(new_fuel, (int, float)):
            raise TypeError("Новое топливо должено быть типа int или float")
        if new_fuel < 0:
            raise ValueError("Новое топливо не может быть отрицательным числом")
        self.quantity += new_fuel


class Coolant:
    """
    Документация на класс.
    Класс описывает модель теплоносителя.
    """
    def __init__(self, sort: str, volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Теплоноситель"

        :param sort: тип теплоносителя 'Н2O','Na' либо 'CO2'
        :param volume: объем теплоносителя

        Примеры:
        >>> coolant = Coolant('Н2O',10000)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Колличество топлива должено быть типа int или float")
        if volume < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        self.volume = volume

        if sort not in ('Н2O', 'Na', 'CO2'):
            raise TypeError("Теплоноситель должен быть 'Н2O','Na' либо 'CO2'")
        if not isinstance(sort, str):
            raise TypeError("Теплоноситель должен быть 'Н2O','Na' либо 'CO2'")
        self.sort = sort

        self.temperature = None
        self.set_temperature(power=0)  # Вызываем метод который посчитает температуру

    def set_temperature(self, power: Union[int, float]) -> None:
        """
        Функция считает и задает температуру теплоносителя

        :param power: Мощность реактора
        :return: None

        Примеры:
        >>> coolant = Coolant('Н2O',10000)
        >>> coolant.set_temperature(500)
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должена быть типа int или float")
        if power < 0:
            raise ValueError("Мощность не может быть отрицательным числом")
        if power == 0:
            self.temperature = 100
        else:
            self.temperature = 100 + power * 9

    def drain_coolant(self) -> None:
        """
        Функция сливающая теплоноситель

        :return: None

        Примеры:
        >>> coolant = Coolant('Н2O',10000)
        >>> coolant.drain_coolant()
        """
        self.volume = 0


class NuclearReactor:
    """
    Документация на класс.
    Класс описывает модель Ядерного реактора(ЯР) .
    """
    def __init__(self, fuel: Fuel, coolant: Coolant, power: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Реактор"

        :param fuel: Объект топливо
        :param coolant: Объект теплоноситель
        :param power: Мощность реактора

        Примеры:
        >>> fuel_test = Fuel(50,100)
        >>> coolant1_test = Coolant('H2O',1000)
        >>> reactor = NuclearReactor(fuel_test, coolant1_test, 100)
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должена быть типа int или float")
        if power < 0:
            raise ValueError("Мощность не может быть отрицательным числом")
        self.power = power
        self.fuel = fuel
        self.coolant = coolant

    def launch_reactor(self) -> None:
        """
        Функция запускающая реактор

        :return: None

        Примеры:
        >>> fuel_test = Fuel(50,100)
        >>> coolant1_test = Coolant('H2O',1000)
        >>> reactor = NuclearReactor(fuel_test, coolant1_test, 100)
        >>> reactor.launch_reactor()
        """
        if self.fuel.quantity < 10:
            print("Недостаточно топлива")
        if self.coolant.volume < 100:
            print("Недостаточно теплоносителя")
        self.fuel.set_temperature(self.power)
        self.coolant.set_temperature(self.power)
        if self.fuel.temperature > 1000:
            print("Топливо расплавилось")
        if self.coolant.temperature > 1000:
            print("Теплоноситель выкипел")
        else:
            print(f"Реактор вышел на мощность {self.power} МВт")

    def stop_reactor(self) -> None:
        """
        Функция останавливающая реактор

        :return: None

        Примеры:
        >>> fuel_test = Fuel(50,100)
        >>> coolant1_test = Coolant('H2O',1000)
        >>> reactor = NuclearReactor(fuel_test, coolant1_test, 100)
        >>> reactor.launch_reactor()
        >>> reactor.stop_reactor()
        """
        self.power = 0
        self.fuel.set_temperature(self.power)
        self.coolant.set_temperature(self.power)
        print(f"Реактор остановлен")

    def set_power(self, new_power:  Union[int, float]) -> None:
        """
        Функция задающая новую мощность реактора

        :param new_power: Номая мощность
        :return: None

        Примеры:
        >>> fuel_test = Fuel(50,100)
        >>> coolant1_test = Coolant('H2O',1000)
        >>> reactor = NuclearReactor(fuel_test, coolant1_test, 100)
        >>> reactor.set_power(50)
        """
        if not isinstance(new_power, (int, float)):
            raise TypeError("Мощность должена быть типа int или float")
        if new_power < 0:
            raise ValueError("Мощность не может быть отрицательным числом")
        self.power = new_power


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    # TODO работоспособность экземпляров класса проверить с помощью doctest
