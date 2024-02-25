import pytest
from src.connect_HH import connect_HH
from src.sort_vacancies import SortVacancies


@pytest.fixture
def test_hh():
    return connect_HH("python", 1)


def test_sort_vacancies():
    r = SortVacancies()
    assert r.hh_sort == []
    assert r.date_format is None


def test_sort_vacancies_hh():
    r = SortVacancies()
    assert r.sort_vacancies_hh == [{'city': 'Оренбург',
                                    'data': '29.01.2024',
                                    'employer': 'Комаров Геннадий',
                                    'name': 'Стажер-разработчик Python',
                                    'payment_from': 50000,
                                    'payment_to': 50000,
                                    'schedule': 'Полный день'}]


def test_error_sort_vacancies():
    with pytest.raises(TypeError):
        SortVacancies(10)
