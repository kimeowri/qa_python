import pytest
from main import BooksCollector


class TestBooksCollector:

    # 1)тест для метода add_new_book
    def test_add_new_book_have_no_genre_success(self, book_collection):
        book = 'Оно'
        book_collection.add_new_book(book)
        assert book_collection.get_book_genre(book) == ''

    # 2)тест для метода add_new_book
    def test_add_new_book_adding_two_books_success(self, book_collection):
        books = ['Оно', 'Джек Ричер']
        for book in books:
            book_collection.add_new_book(book)
        assert len(book_collection.get_books_genre()) == 2

    # 3)тест для метода add_new_book
    def test_add_new_book_duplicate_book_not_added(self, book_collection):
        books = ['Унесенные ветром', 'Унесенные ветром']
        for book in books:
            book_collection.add_new_book(book)
        assert len(book_collection.get_books_genre()) == 1

    # 4) тест для метода add_new_book
    @pytest.mark.parametrize('book',
                             ['', # 0 миволов
                              'Радости и горести знаменитой Молль Флендерс, которая родилась в Ньюгетской тюрьме', # 71 символ без пробелов
                              'Радости и горести знаменитой Молль Флендерс, ко'] # 41 символ без пробелов
                             )
    def test_add_new_book_invalid_name_not_added(self, book, book_collection):
        book_collection.add_new_book(book)
        assert len(book_collection.get_books_genre()) == 0

    # 5) тест для метода set_book_genre
    def test_set_book_genre_added_genre_book_success(self, book_collection):
        book = 'Гарри Поттер и философский камень'
        genre = 'Фантастика'
        book_collection.add_new_book(book)
        book_collection.set_book_genre(book, genre)
        assert book_collection.get_book_genre(book) == genre

    # 6) тест для метода set_book_genre
    def test_set_book_genre_changed_success(self, book_collection):
        book = 'Гарри Поттер и философский камень'
        genre = 'Фантастика'
        new_genre = 'Ужасы'
        book_collection.add_new_book(book)
        book_collection.set_book_genre(book, genre)
        book_collection.set_book_genre(book, new_genre)
        assert book_collection.get_book_genre(book) == new_genre

    # 6) тест для метода set_book_genre
    def test_set_book_genre_add_genre_is_not_list_not_added(self, book_collection):
        book = 'Гарри Поттер и философский камень'
        new_book_genre = 'Комикс'
        book_collection.add_new_book(book)
        book_collection.set_book_genre(book, new_book_genre)
        assert book_collection.get_book_genre(book) == ''

    # 7) тест для метода get_book_genre
    def test_get_book_genre_success(self, book_collection):
        book = 'Гарри Поттер и философский камень'
        genre = 'Фантастика'
        book_collection.add_new_book(book)
        book_collection.set_book_genre(book, genre)
        assert book_collection.get_book_genre(book) == genre

    # 8) тест для метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_success(self, collection_five_book):
        assert collection_five_book.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс']

    # 9) тест для метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_no_such_book_not_added(self, collection_five_book):
        assert len(collection_five_book.get_books_with_specific_genre('Комикс')) == 0

    # 10) тест метода get_books_for_children
    def test_get_books_for_children_success(self, collection_five_book):
        children_book = collection_five_book.get_books_for_children()
        assert len(children_book) == 3 and children_book == ['Гарри Поттер и философский камень', 'Зелёная миля', 'Прислуга']

    # 11) тест метода add_book_in_favorites
    def test_add_book_in_favorites_add_book_success(self, book_collection):
        book = 'Гарри Поттер и философский камень'
        book_collection.add_new_book(book)
        book_collection.add_book_in_favorites(book)
        favorites = book_collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] ==book

    # 12) тест метода add_book_in_favorites
    def test_add_book_in_favorites_add_duplicate_book_not_added(self,book_collection):
        book = 'Гарри Поттер и философский камень'
        book_collection.add_new_book(book)
        book_collection.add_book_in_favorites(book)
        book_collection.add_book_in_favorites(book)
        favorites = book_collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == book

    # 13) тест метода delete_book_from_favorites
    def test_delete_book_from_favorites_deleted_book(self, book_collection):
        book = 'Гарри Поттер и философский камень'
        book_collection.add_new_book(book)
        book_collection.add_book_in_favorites(book)
        book_collection.delete_book_from_favorites(book)
        assert len(book_collection.get_list_of_favorites_books()) == 0

    # 14) тест метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_got_list(self, book_collection):
        books = 'Гарри Поттер и философский камень'
        book_collection.add_new_book(books)
        book_collection.add_book_in_favorites(books)
        assert len(book_collection.get_list_of_favorites_books()) == 1

