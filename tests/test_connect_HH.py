import pytest
from src.connect_HH import connect_HH


@pytest.fixture
def test_connect_HH():
    return connect_HH("python", 1)


def test_str(test_connect_HH):
    assert str(test_connect_HH) == "python"


def test_repr(test_connect_HH):
    assert repr(test_connect_HH) == "connect_HH(python, 1)"


def test_url(test_connect_HH):
    assert test_connect_HH.url == "https://api.hh.ru"


def test_error_connection():
    with pytest.raises(TypeError):
        connect_HH()
