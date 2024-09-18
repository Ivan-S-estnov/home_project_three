import pytest

@pytest.fixture
def widget_input():
    return """Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305"""


@pytest.fixture
def widget_result_one():
    return """Maestro 1596 83** **** 5199
Счет **9589
MasterCard 7158 30** **** 6758
Счет **5560
Visa Classic 6831 98** **** 7658
Visa Platinum 8990 92** **** 5229
Visa Gold 5999 41** **** 6353
Счет **4305"""
