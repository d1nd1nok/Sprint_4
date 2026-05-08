# Sprint_4

В тестах используются:

- фикстуры (`pytest.fixture`);
- параметризация (`pytest.mark.parametrize`);
- позитивные и негативные сценарии;
- проверки граничных значений.



Реализованные тесты

add_new_book
- Тесты:
    test_add_new_book_add_book_success
    test_add_new_book_not_add_book_with_empty_name
    test_add_new_book_not_add_book_with_long_name
    test_add_new_book_add_three_books_success_without_duplicates


set_book_genre
- Тесты:
    test_set_book_genre_set_valid_genre
    test_set_book_genre_not_set_invalid_genre
    test_set_book_genre_not_set_genre_for_missing_book


get_book_genre
- Тесты:
    test_get_book_genre_return_genre_by_name
    test_get_book_genre_return_none_for_missing_book


get_books_with_specific_genre
- Тесты:
    test_get_books_with_specific_genre_return_books
    test_get_books_with_specific_genre_return_empty_list


get_books_genre
- Тесты:
    _get_books_genre_return_dictionary


get_books_for_children
- Тесты:
    test_get_books_for_children_return_safe_books
    test_get_books_for_children_not_return_horror_books


add_book_in_favorites
- Тесты:
    test_add_book_in_favorites_add_book_success
    test_add_book_in_favorites_not_add_missing_book
    test_add_book_in_favorites_not_duplicate_book


delete_book_from_favorites
- Тесты:
    test_delete_book_from_favorites_delete_book_success
    test_delete_book_from_favorites_not_fail_for_missing_book