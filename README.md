## Набор тестовых методов класса TestBooksCollector:
- test_add_new_book_have_no_genre_success: Добавление книги без жанра
- test_add_new_book_adding_two_books_success: Добавление двух книг
- test_add_new_book_duplicate_book_not_added: Добавление дубликата
- test_add_new_book_invalid_name_not_added: Невалидные значения
- test_set_book_genre_added_genre_book_success: Добавление жанра
- test_set_book_genre_changed_success: Изменение жанра
- test_set_book_genre_add_genre_is_not_list_not_added: Добавление несуществующего жанра
- test_get_books_with_specific_genre_success: Вывод список книг с определённым жанром
- test_get_books_with_specific_genre_no_such_book_not_added: Отсутствие книги определенного жанра
- test_get_books_for_children_success: Возвращает книги, которые подходят детям
- test_add_book_in_favorites_add_book_success: Добавляет книгу в избранное
- test_add_book_in_favorites_add_duplicate_book_not_added: Проверка на повторное добавление в избранное
- test_delete_book_from_favorites_deleted_book: Удаление книги из списка избранного
- test_get_list_of_favorites_books_got_list: Получение списка избранных книг

### Команда для запуска тестов
`pytest -v`
