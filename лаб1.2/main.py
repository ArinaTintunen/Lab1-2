# TODO Написать 3 класса с документацией и аннотацией типов

class Book(ABC):
    """
    Абстрактный класс для книг.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
    """

    def __init__(self, title: str, author: str) -> None:
        if not title or not isinstance(title, str):
            raise ValueError("Название книги должно быть непустой строкой.")
        if not author or not isinstance(author, str):
            raise ValueError("Автор книги должен быть непустой строкой.")

        self.title = title
        self.author = author

    def get_description(self) -> str:
        """
        Возвращает описание книги.

        Returns:
            str: Описание книги.

        >>> book = FictionBook("1984", "George Orwell", "Dystopian")
        >>> book.get_description()
        '1984 by George Orwell - Genre: Dystopian'
        """
        ...


    def read(self) -> None:
        """
        Симулирует чтение книги.

        Returns:
            None

        >>> book = FictionBook("1984", "George Orwell", "Dystopian")
        >>> book.read()
        'Reading 1984 by George Orwell...'
        """
        ...


class FictionBook(Book):
    """
    Класс для художественных книг.

    Attributes:
        genre (str): Жанр книги.
    """

    def __init__(self, title: str, author: str, genre: str) -> None:
        super().__init__(title, author)

        if not genre or not isinstance(genre, str):
            raise ValueError("Жанр книги должен быть непустой строкой.")

        self.genre = genre

    def get_description(self) -> str:
        return f"{self.title} by {self.author} - Genre: {self.genre}"

    def read(self) -> None:
        print(f"Reading {self.title} by {self.author}...")


class NonFictionBook(Book):
    """
    Класс для научно-популярных книг.

    Attributes:
        subject (str): Тематика книги.
    """

    def __init__(self, title: str, author: str, subject: str) -> None:
        super().__init__(title, author)

        if not subject or not isinstance(subject, str):
            raise ValueError("Тематика книги должна быть непустой строкой.")

        self.subject = subject

    def get_description(self) -> str:
        return f"{self.title} by {self.author} - Subject: {self.subject}"

    def read(self) -> None:
        print(f"Reading {self.title} by {self.author}...")


class Textbook(NonFictionBook):
    """
    Класс для учебников.

    Attributes:
        level (str): Уровень сложности учебника.
    """

    def __init__(self, title: str, author: str, subject: str, level: str) -> None:
        super().__init__(title, author, subject)

        if not level or not isinstance(level, str):
            raise ValueError("Уровень сложности должен быть непустой строкой.")

        self.level = level

    def get_description(self) -> str:
        return f"{self.title} by {self.author} - Subject: {self.subject}, Level: {self.level}"

    def read(self) -> None:
        print(f"Studying {self.title} by {self.author}...")
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
