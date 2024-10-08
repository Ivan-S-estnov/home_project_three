import pytest

from src.masks import get_mask_account, get_mask_card_number


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
