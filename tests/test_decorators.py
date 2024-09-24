import pytest

from src.decorators import log, my_function


def test_log_1():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 5)
    assert result == 6


def test_log_2():
    with pytest.raises(Exception):
        my_function()


def test_log_3(capsys):

    my_function(1, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
