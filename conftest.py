import pytest
from main import BooksCollector

@pytest.fixture
def book_collection():
    return BooksCollector()


@pytest.fixture
def collection_five_book(book_collection):
    books = ['Гарри Поттер и философский камень', 'Унесенные ветром', 'Шерлок Холмс', 'Зелёная миля', 'Прислуга']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(5):
        book_collection.add_new_book(books[i])

    for i in range(5):
        book_collection.set_book_genre(books[i], genre[i])

    return book_collection