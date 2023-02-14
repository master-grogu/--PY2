import doctest


class LabWork:
    """ Класс описывает модель Лабораторной работы. """
    def __init__(self, name: str, author: str, done: str = f"{False}", quantity_of_work: float = 1.0):
        """
        Создание и подготовка к работе объекта "Лабораторная работа"

        :param name: Название Лабораторной работы
        :param author: Имя Автора Лабораторной работы
        :param done: Готовность Лабораторной работы
        :param quantity_of_work: сложность Лабораторной работы

        Примеры:
        >>> labtest = LabWork("1", "11")
        """
        self._name = name
        self._author = author
        self._quantity_of_work = quantity_of_work
        self._done = done

    @property
    def name(self) -> str:  # атрибут name задается только при создания и не должно меняться
        return self._name

    @property
    def author(self) -> str:  # атрибут author задается только при создания и не должно меняться
        return self._author

    @property
    def done(self) -> str:  # атрибут done не задается, а имеет начальное значение, и должен изменять с помощью метода
        return self._done

    @property
    def quantity_of_work(self) -> float:
        return self._quantity_of_work

    @quantity_of_work.setter
    def quantity_of_work(self, new_quantity_of_work: float) -> None:
    # атрибут quantity_of_work должен задаваться в определенном формате
        if not isinstance(new_quantity_of_work, float):
            raise TypeError("Сложность работы должна быть типа float")
        if new_quantity_of_work <= 0:
            raise ValueError("Сложность работы должна быть положительным числом")
        self._quantity_of_work = new_quantity_of_work

    def __str__(self) -> str:
        return f"Лабораторная работа {self._name}. Автор {self._author}. Выполнено {self._done}. " \
               f"Сложность работы {self._quantity_of_work}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, " \
               f"done={self.done!r}, quantity_of_work={self.quantity_of_work!r})"

    def do_lab_work(self) -> None:
        """
        Функция выполняет Лабораторную работу

        Примеры:
        >>> labtest = LabWork("1", "11")
        >>> labtest.do_lab_work()
        """
        self._done = f"{True}"
    ...


class Task(LabWork):
    """ Класс описывает модель Задания Лабораторной работы. """
    def __init__(self, name: str, author: str, number_of_task: int, done: str = f"{False}",
                 quantity_of_works: float = 1.0):
        """
        Создание и подготовка к работе объекта "Задание Лабораторной работы"

        :param name: Название Задания Лабораторной работы
        :param author: Имя Автора Задания Лабораторной работы
        :param number_of_task: Номер Задания Лабораторной работы
        :param done: Готовность Задания Лабораторной работы
        :param quantity_of_works: сложность Задани Лабораторной работы

        Примеры:
        >>> labtest = Task("1", "11", 1)
        """
        super().__init__(name, author, done, quantity_of_works)
        self._number_of_task = number_of_task

    @property
    def number_of_task(self) -> int:
        return self._number_of_task

    @number_of_task.setter
    def number_of_task(self, new_number_of_task: int) -> None:
    # атрибут number_of_task должен задаваться в определенном формате
        if not isinstance(new_number_of_task, int):
            raise TypeError("Номер задания должен быть типа int")
        if new_number_of_task <= 0:
            raise ValueError("Номер задания должен быть положительным числом")
        self._number_of_task = new_number_of_task

    def __str__(self) -> str:
        return f"Задание Лабораторной работы {self._name}. Автор {self._author}. " \
               f"Номер заданий {self._number_of_task}. Выполнено {self._done}. " \
               f"Сложность работы {self._quantity_of_work}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, " \
               f"number_of_task={self._number_of_task}. done={self._done!r}, " \
               f"quantity_of_work={self._quantity_of_work!r})"

    def give_answer(self, answer: str) -> print:
        """
        Функция принимает и печатает полученный ответ

        Примеры:
        >>> labtest = Task("1", "11", 1)
        >>> labtest.give_answer("1111")
        """
        print("Ваш ответ =", answer)
    ...


class File(Task):
    """ Класс описывает модель Файла Задания Лабораторной работы. """
    def __init__(self, name: str, author: str, number_of_task: int, format_file: str, done: str = f"{False}",
                 quantity_of_works: float = 1.0):
        """
        Создание и подготовка к работе объекта "Файл Задания Лабораторной работы"

                :param name: Название Файла Задания Лабораторной работы
                :param author: Имя Автора Файла Задания Лабораторной работы
                :param number_of_task: Номер Задания Лабораторной работы
                :param format_file: Формат Файла Задания Лабораторной работы
                :param done: Готовность Задания Лабораторной работы
                :param quantity_of_works: сложность Задани Лабораторной работы

                Примеры:
                >>> labtest = Task("1", "11", 1, "pdf")
                """
        super().__init__(name, author, number_of_task, done, quantity_of_works)
        self._format = format_file

    @property
    def format_file(self) -> str:  # атрибут format_file задается только при создания и не должен меняться
        return self._format

    def __str__(self) -> str:
        return f"Файл Задание Лабораторной работы {self._name}. Автор {self._author}. " \
               f"Номер заданий {self._number_of_task}. Формат файла {self._format}. Выполнено {self._done}. " \
               f"Сложность работы {self._quantity_of_work}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, " \
               f"number_of_task={self._number_of_task}. forma_file={self._format!r},"  \
               f"done={self._done!r}, quantity_of_work={self._quantity_of_work!r})"

    def give_answer(self, answer: str, format_file_answer: str = "pdf") -> print:
        """
        Функция принимает и печатает полученный ответ

        Примеры:
        >>> labtest = File("1", "11", 1, "pdf")
        >>> labtest.give_answer("1111", "jpeg")

        Перезагрузка требуется, так как появляется новый аргумент format_file_answer
        """
        print("Ваш ответ =", answer + "." + format_file_answer)
    ...


if __name__ == "__main__":
    doctest.testmod()
    lab = LabWork("11", "1")
    print(lab.__str__())
    lab.do_lab_work()
    print(lab.__repr__())
    print("")
    lab1 = Task("22", "2", 2)
    print(lab1.__str__())
    lab1.give_answer("222")
    lab1.do_lab_work()
    print(lab1.__repr__())
    print("")
    lab2 = File("33", "3", 3, "pdf")
    print(lab2.__str__())
    lab2.give_answer("222", "jpeg")
    lab2.do_lab_work()
    print(lab2.__repr__())
    # Write your solution here
    pass
