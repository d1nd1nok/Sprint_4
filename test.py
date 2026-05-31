import pytest
from main import BooksCollector

# add_new_book
@pytest.mark.parametrize('name', ['Гарри Поттер', 'Шерлок Холмс', 'Властелин колец'])
def test_add_new_book_add_book_success(book_constructur, name):
    book_constructur.add_new_book(name)
    assert len(book_constructur.books_genre) == 1

def test_add_new_book_not_add_book_with_empty_name(book_constructur):
    book_constructur.add_new_book('')
    assert len(book_constructur.books_genre) == 0

def test_add_new_book_not_add_book_with_long_name(book_constructur):
    long_name = 'А' * 41
    book_constructur.add_new_book(long_name)
    assert len(book_constructur.books_genre) == 0  

def test_add_new_book_add_three_books_success_without_duplicates(book_constructur):
    book_constructur.add_new_book('Гарри Поттер')
    book_constructur.add_new_book('Шерлок Холмс')
    book_constructur.add_new_book('Властелин колец')
    book_constructur.add_new_book('Властелин колец')
    assert len(book_constructur.books_genre) == 3


# set_book_genre
def test_set_book_genre_set_valid_genre(book_constructur):
    book_constructur.add_new_book('Оно')
    book_constructur.set_book_genre('Оно', 'Ужасы')

    assert book_constructur.get_book_genre('Оно') == 'Ужасы'

def test_set_book_genre_not_set_invalid_genre(book_constructur):
    book_constructur.add_new_book('Оно')
    book_constructur.set_book_genre('Оно', 'Роман')
    assert book_constructur.get_book_genre('Оно') == ''

def test_set_book_genre_not_set_genre_for_missing_book(book_constructur):
    book_constructur.set_book_genre('Несуществующая книга', 'Ужасы')
    assert book_constructur.get_book_genre('Несуществующая книга') is None


# get_book_genre
def test_get_book_genre_return_genre_by_name(book_constructur):
    book_constructur.add_new_book('Дюна')
    book_constructur.set_book_genre('Дюна', 'Фантастика')   
    assert book_constructur.get_book_genre('Дюна') == 'Фантастика'

def test_get_book_genre_return_none_for_missing_book(book_constructur):
    assert book_constructur.get_book_genre('Неизвестная книга') is None




# get_books_with_specific_genre
@pytest.mark.parametrize('book, genre', [('Оно', 'Ужасы'), ('Сияние', 'Ужасы')])
def test_get_books_with_specific_genre_return_books(book_constructur, book, genre):
    book_constructur.add_new_book(book)
    book_constructur.set_book_genre(book, genre)

    result = book_constructur.get_books_with_specific_genre('Ужасы')

    assert result == [book]

def test_get_books_with_specific_genre_return_empty_list(book_constructur):
    book_constructur.add_new_book('Дюна')
    book_constructur.set_book_genre('Дюна', 'Фантастика')

    result = book_constructur.get_books_with_specific_genre('Комедии')

    assert result == []



# get_books_genre
def test_get_books_genre_return_dictionary(book_constructur):
    book_constructur.add_new_book('Дюна')
    expected_result = {'Дюна': ''}
    assert book_constructur.get_books_genre() == expected_result


   
# get_books_for_children

def test_get_books_for_children_return_safe_books(book_constructur):
        
    book_constructur.add_new_book('Дюна')
    book_constructur.add_new_book('Оно')
    book_constructur.set_book_genre('Дюна', 'Фантастика')
    book_constructur.set_book_genre('Оно', 'Ужасы')

    result = book_constructur.get_books_for_children()
    assert result == ['Дюна']

def test_get_books_for_children_not_return_horror_books(book_constructur):
        
    book_constructur.add_new_book('Оно')
    book_constructur.set_book_genre('Оно', 'Ужасы')

    result = book_constructur.get_books_for_children()
    assert 'Оно' not in result


# add_book_in_favorites
def test_add_book_in_favorites_add_book_success(book_constructur):
    book_constructur.add_new_book('Дюна')
    book_constructur.add_book_in_favorites('Дюна')
    assert book_constructur.get_list_of_favorites_books() == ['Дюна']

def test_add_book_in_favorites_not_add_missing_book(book_constructur):
    book_constructur.add_new_book('Дюна')
    book_constructur.add_book_in_favorites('Неизвестная книга')

    assert book_constructur.get_list_of_favorites_books() == []

def test_add_book_in_favorites_not_duplicate_book(book_constructur):
    book_constructur.add_new_book('Дюна')
    book_constructur.add_book_in_favorites('Дюна')
    book_constructur.add_book_in_favorites('Дюна')
    assert len(book_constructur.get_list_of_favorites_books()) == 1


# delete_book_from_favorites
def test_delete_book_from_favorites_delete_book_success(book_constructur):
    book_constructur.add_new_book('Дюна')
    book_constructur.add_book_in_favorites('Дюна')
    book_constructur.delete_book_from_favorites('Дюна')
    assert book_constructur.get_list_of_favorites_books() == []

def test_delete_book_from_favorites_not_fail_for_missing_book(book_constructur):
    book_constructur.delete_book_from_favorites('Неизвестная книга')
    assert book_constructur.get_list_of_favorites_books() == []