import pytest

from src.decorators import log


def test_log_1():
    @log(filename="test_log.txt")
    def test_func_1(x, y):
        return x / y

    result = test_func_1(28, 7)
    assert result == 4.0


def test_log_2():
    @log(filename="test_log.txt")
    def test_func_2(a, b):
        return a + b

    with pytest.raises(Exception):
        test_func_2(2, [])


def test_log_3(capsys):
    @log()
    def test_func_3(f, v):
        return f * v

    result = test_func_3(4, 2)
    captured = capsys.readouterr()
    assert captured.out == f"test_func_3 ok\n"
