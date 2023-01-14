BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть типа int")
        if not id_ > 0:
            raise ValueError("Идентификатор должен быть больше 0")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if len(name) <= 0:
            raise ValueError("Название должно содержать хотя бы один символ")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if not pages > 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'
# TODO написать класс Book


class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books

    def get_next_book_id(self) -> int:
        if self.books is None:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        for _, book in enumerate(self.books):
            if book.id_ == id_:
                return _
        raise ValueError("Книги с запрашиваемым id не существует")
# TODO написать класс Library


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
