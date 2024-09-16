import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_info, card_mask",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_get_mask_card_number(card_info: str, card_mask: str) -> str:
    assert get_mask_card_number(card_info) == card_mask


@pytest.mark.parametrize(
    "account_info, account_mask",
    [("64686473678894779589", "**9589"), ("35383033474447895560", "**5560"), ("73654108430135874305", "**4305")],
)
def test_get_mask_account(account_info: str, account_mask: str) -> str:
    assert get_mask_account(account_info) == account_mask


@pytest.mark.parametrize(
    "card_account_info, masks",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_account_info: str, masks: str) -> str:
    assert mask_account_card(card_account_info) == masks


@pytest.mark.parametrize("user_time, repair_time", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_get_date(user_time: str, repair_time: str) -> str:
    assert get_date(user_time) == repair_time
