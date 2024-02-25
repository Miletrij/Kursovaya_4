import pytest
from src.vacancies import Vacancies


@pytest.fixture
def test_vacancies():
    return Vacancies("python", 1)


def test_str(test_vacancies):
    assert str(test_vacancies) == "python"


def test_repr(test_vacancies):
    assert repr(test_vacancies) == "Vacancies(('python', 1))"


def test_name_error(test_vacancies):
    with pytest.raises(AttributeError):
        test_vacancies.name = "hello"


def test_page_error(test_vacancies):
    with pytest.raises(AttributeError):
        test_vacancies.page = 10
