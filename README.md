## Набор тестовых методов класса TestBooksCollector:
- test_add_new_book_have_no_genre_success: Проверка наличия жанра по умолчанию
- test_add_new_book_adding_two_books_success: Проверка добавления двух книг
- test_add_new_book_duplicate_book_not_added: Проверка на добавление дубликата
- test_add_new_book_invalid_name_not_added: Проверка добавления книг с невалидными значения
- test_set_book_genre_added_genre_book_success: Проверка добавления жанра книге
- test_set_book_genre_changed_success: Проверка изменения жанра книги
- test_set_book_genre_add_genre_is_not_list_not_added: Проверка на добавление несуществующего жанра
- test_get_book_genre_success: Проверка вывода жанра книги по её имени
- test_get_books_with_specific_genre_success: Проверка вывода список книг с определённым жанром
- test_get_books_with_specific_genre_no_such_book_not_added: Проверка фильра по несуществующему жанру
- test_get_books_for_children_success: Проверка вывода книги, которые подходят детям
- test_add_book_in_favorites_add_book_success: Проверка добавления книг в избранное
- test_add_book_in_favorites_add_duplicate_book_not_added: Проверка на повторное добавление книги в избранное
- test_delete_book_from_favorites_deleted_book: Проверка удаления книги из избранного
- test_get_list_of_favorites_books_got_list: Проверка получения избранных книг

### Команда для запуска тестов
`pytest -v`

### Команда для подробной оценки покрытия с учетом ветвления
`pytest --cov=main --cov-branch --cov-report=html`


